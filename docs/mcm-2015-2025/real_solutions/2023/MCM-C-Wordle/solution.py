from __future__ import annotations

import json
import math
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.linear_model import RidgeCV
from sklearn.metrics import accuracy_score, mean_absolute_error, mean_squared_error
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


ARCHIVE_ROOT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
DATA_PATH = (
    ARCHIVE_ROOT
    / "official_assets_extracted"
    / "2023"
    / "Problem Data- Predicting Wordle Results"
    / "2023_MCM_Problem_C_Data.xlsx"
)
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"
PREDICTION_DATE = pd.Timestamp("2023-03-01")
PREDICTION_WORD = "EERIE"
TRY_COLUMNS = ["1 try", "2 tries", "3 tries", "4 tries", "5 tries", "6 tries", "7 or more tries (X)"]
ATTEMPT_WEIGHTS = np.array([1, 2, 3, 4, 5, 6, 7], dtype=float)
FEATURE_COLUMNS = [
    "days_since_start",
    "days_since_start_sq",
    "contest_number",
    "weekday",
    "is_weekend",
    "unique_letters",
    "repeated_letters",
    "max_letter_count",
    "vowel_count",
    "repeated_vowel_count",
    "rare_letter_count",
    "word_entropy",
    "letter_frequency_score",
]


def clean_float(value: float, digits: int = 6) -> float:
    if pd.isna(value):
        return float("nan")
    return round(float(value), digits)


def read_wordle_workbook() -> pd.DataFrame:
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"missing COMAP Wordle workbook: {DATA_PATH}")
    raw = pd.read_excel(DATA_PATH, header=None)
    headers = raw.iloc[1].tolist()
    df = raw.iloc[2:].copy()
    df.columns = headers
    df = df.drop(columns=[col for col in df.columns if pd.isna(col)])
    df.columns = [" ".join(str(col).split()) for col in df.columns]
    rename = {"Number of reported results": "Number of reported results"}
    df = df.rename(columns=rename)
    df["Date"] = pd.to_datetime(df["Date"])
    df["Word"] = df["Word"].astype(str).str.upper()
    numeric_cols = ["Contest number", "Number of reported results", "Number in hard mode", *TRY_COLUMNS]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.dropna(subset=["Date", "Contest number", "Word", "Number of reported results", *TRY_COLUMNS])
    df = df.sort_values("Date").reset_index(drop=True)
    df["hard_mode_rate"] = df["Number in hard mode"] / df["Number of reported results"]
    pct = df[TRY_COLUMNS].div(df[TRY_COLUMNS].sum(axis=1), axis=0) * 100
    df[TRY_COLUMNS] = pct
    df["expected_attempts"] = (df[TRY_COLUMNS].to_numpy() @ ATTEMPT_WEIGHTS) / 100.0
    return df


def letter_frequency(words: pd.Series) -> dict[str, float]:
    letters = "".join(words.astype(str).str.upper().tolist())
    counts = Counter(letters)
    total = sum(counts.values()) or 1
    return {letter: counts.get(letter, 0) / total for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}


def word_feature_row(word: str, freq: dict[str, float]) -> dict[str, float]:
    cleaned = "".join(ch for ch in word.upper() if ch.isalpha())
    counts = Counter(cleaned)
    vowels = "AEIOU"
    rare = "QZXJKV"
    probs = np.array(list(counts.values()), dtype=float) / max(1, len(cleaned))
    entropy = -float(np.sum(probs * np.log2(probs))) if len(probs) else 0.0
    vowel_count = sum(counts.get(vowel, 0) for vowel in vowels)
    repeated_vowel_count = sum(max(0, counts.get(vowel, 0) - 1) for vowel in vowels)
    return {
        "unique_letters": float(len(counts)),
        "repeated_letters": float(max(0, len(cleaned) - len(counts))),
        "max_letter_count": float(max(counts.values()) if counts else 0),
        "vowel_count": float(vowel_count),
        "repeated_vowel_count": float(repeated_vowel_count),
        "rare_letter_count": float(sum(counts.get(letter, 0) for letter in rare)),
        "word_entropy": entropy,
        "letter_frequency_score": float(np.mean([freq.get(ch, 0.0) for ch in cleaned])) if cleaned else 0.0,
    }


def add_features(df: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, float]]:
    enriched = df.copy()
    start = enriched["Date"].min()
    freq = letter_frequency(enriched["Word"])
    enriched["days_since_start"] = (enriched["Date"] - start).dt.days.astype(float)
    enriched["days_since_start_sq"] = enriched["days_since_start"] ** 2
    enriched["contest_number"] = enriched["Contest number"].astype(float)
    enriched["weekday"] = enriched["Date"].dt.weekday.astype(float)
    enriched["is_weekend"] = (enriched["weekday"] >= 5).astype(float)
    word_features = pd.DataFrame([word_feature_row(word, freq) for word in enriched["Word"]])
    for col in word_features.columns:
        enriched[col] = word_features[col]
    return enriched, freq


def future_feature_frame(df: pd.DataFrame, freq: dict[str, float], word: str, date: pd.Timestamp) -> pd.DataFrame:
    start = df["Date"].min()
    last = df.sort_values("Date").iloc[-1]
    days_after_last = (date - last["Date"]).days
    row: dict[str, float] = {
        "days_since_start": float((date - start).days),
        "contest_number": float(last["Contest number"] + days_after_last),
        "weekday": float(date.weekday()),
        "is_weekend": float(date.weekday() >= 5),
    }
    row["days_since_start_sq"] = row["days_since_start"] ** 2
    row.update(word_feature_row(word, freq))
    return pd.DataFrame([row], columns=FEATURE_COLUMNS)


def split_train_holdout(df: pd.DataFrame, holdout_days: int = 45) -> tuple[pd.DataFrame, pd.DataFrame]:
    ordered = df.sort_values("Date").reset_index(drop=True)
    return ordered.iloc[:-holdout_days].copy(), ordered.iloc[-holdout_days:].copy()


def report_count_analysis(df: pd.DataFrame, future_x: pd.DataFrame) -> dict[str, object]:
    train, holdout = split_train_holdout(df)
    model = make_pipeline(StandardScaler(), RidgeCV(alphas=np.logspace(-3, 3, 25)))
    model.fit(train[FEATURE_COLUMNS], np.log(train["Number of reported results"]))
    holdout_log = model.predict(holdout[FEATURE_COLUMNS])
    holdout_pred = np.exp(holdout_log)
    mae = mean_absolute_error(holdout["Number of reported results"], holdout_pred)
    rmse = math.sqrt(mean_squared_error(holdout["Number of reported results"], holdout_pred))

    train_residual = np.log(train["Number of reported results"]) - model.predict(train[FEATURE_COLUMNS])
    future_log = float(model.predict(future_x)[0])
    lo_log = future_log + float(np.quantile(train_residual, 0.10))
    hi_log = future_log + float(np.quantile(train_residual, 0.90))

    hard_model = make_pipeline(StandardScaler(), RidgeCV(alphas=np.logspace(-3, 3, 25)))
    hard_features = [col for col in FEATURE_COLUMNS if col not in {"days_since_start_sq", "contest_number"}]
    hard_model.fit(train[hard_features], train["hard_mode_rate"])
    hard_holdout_pred = np.clip(hard_model.predict(holdout[hard_features]), 0, 1)
    hard_mae = mean_absolute_error(holdout["hard_mode_rate"], hard_holdout_pred)
    hard_future_rate = float(np.clip(hard_model.predict(future_x[hard_features])[0], 0, 1))
    ridge = hard_model.named_steps["ridgecv"]
    hard_effects = [
        {"feature": feature, "coefficient": clean_float(coef)}
        for feature, coef in sorted(zip(hard_features, ridge.coef_), key=lambda item: abs(item[1]), reverse=True)[:8]
    ]

    return {
        "model": "log-linear RidgeCV for report counts; RidgeCV for hard-mode rate",
        "prediction_date": PREDICTION_DATE.date().isoformat(),
        "prediction_word": PREDICTION_WORD,
        "holdout_days": len(holdout),
        "holdout_mae_reported_results": clean_float(mae, 3),
        "holdout_rmse_reported_results": clean_float(rmse, 3),
        "predicted_reported_results": int(round(math.exp(future_log))),
        "prediction_interval_80": [int(round(math.exp(lo_log))), int(round(math.exp(hi_log)))],
        "hard_mode_holdout_mae_rate": clean_float(hard_mae),
        "predicted_hard_mode_rate": clean_float(hard_future_rate),
        "word_attribute_effects_on_hard_mode": hard_effects,
    }


def distribution_analysis(df: pd.DataFrame, future_x: pd.DataFrame) -> dict[str, object]:
    train, holdout = split_train_holdout(df)
    model = RandomForestRegressor(n_estimators=500, min_samples_leaf=4, random_state=20230301, n_jobs=-1)
    model.fit(train[FEATURE_COLUMNS], train[TRY_COLUMNS])
    holdout_pred = model.predict(holdout[FEATURE_COLUMNS])
    holdout_pred = normalize_distribution(holdout_pred)
    bucket_mae = np.mean(np.abs(holdout[TRY_COLUMNS].to_numpy() - holdout_pred), axis=0)
    pred = normalize_distribution(model.predict(future_x))[0]
    future_array = future_x.to_numpy()
    tree_pred = np.stack([tree.predict(future_array)[0] for tree in model.estimators_])
    tree_pred = normalize_distribution(tree_pred)
    lo = np.quantile(tree_pred, 0.10, axis=0)
    hi = np.quantile(tree_pred, 0.90, axis=0)
    rows = []
    for idx, col in enumerate(TRY_COLUMNS):
        rows.append(
            {
                "bucket": col,
                "predicted_percent": clean_float(pred[idx], 3),
                "interval80_low": clean_float(lo[idx], 3),
                "interval80_high": clean_float(hi[idx], 3),
                "holdout_mae_percent_points": clean_float(bucket_mae[idx], 3),
            }
        )
    return {
        "model": "RandomForestRegressor on official percentage buckets, clipped and normalized to 100%",
        "word": PREDICTION_WORD,
        "date": PREDICTION_DATE.date().isoformat(),
        "holdout_mean_bucket_mae_percent_points": clean_float(float(np.mean(bucket_mae)), 3),
        "predicted_distribution_percent": {row["bucket"]: row["predicted_percent"] for row in rows},
        "prediction_intervals_80": {row["bucket"]: [row["interval80_low"], row["interval80_high"]] for row in rows},
        "bucket_holdout_mae_percent_points": {row["bucket"]: row["holdout_mae_percent_points"] for row in rows},
        "table_rows": rows,
    }


def normalize_distribution(values: np.ndarray) -> np.ndarray:
    arr = np.asarray(values, dtype=float)
    arr = np.maximum(arr, 0.0)
    if arr.ndim == 1:
        arr = arr.reshape(1, -1)
    totals = arr.sum(axis=1, keepdims=True)
    totals[totals == 0] = 1.0
    return arr / totals * 100.0


def difficulty_analysis(df: pd.DataFrame, future_x: pd.DataFrame, eerie_distribution: dict[str, float]) -> dict[str, object]:
    train, holdout = split_train_holdout(df)
    q1, q2 = train["expected_attempts"].quantile([1 / 3, 2 / 3]).tolist()

    def classify(value: float) -> str:
        if value <= q1:
            return "easy"
        if value <= q2:
            return "medium"
        return "hard"

    labels = df["expected_attempts"].map(classify)
    train_labels = labels.loc[train.index]
    holdout_labels = labels.loc[holdout.index]
    model = RandomForestClassifier(n_estimators=400, min_samples_leaf=4, random_state=20230302, n_jobs=-1)
    model.fit(train[FEATURE_COLUMNS], train_labels)
    holdout_pred = model.predict(holdout[FEATURE_COLUMNS])
    accuracy = accuracy_score(holdout_labels, holdout_pred)
    model_eerie_class = str(model.predict(future_x)[0])
    eerie_expected_attempts = sum(eerie_distribution[col] * weight for col, weight in zip(TRY_COLUMNS, ATTEMPT_WEIGHTS)) / 100.0
    threshold_eerie_class = classify(eerie_expected_attempts)
    importances = [
        {"feature": feature, "importance": clean_float(value)}
        for feature, value in sorted(zip(FEATURE_COLUMNS, model.feature_importances_), key=lambda item: item[1], reverse=True)[:10]
    ]
    table = df[["Date", "Contest number", "Word", "expected_attempts"]].copy()
    table["difficulty_class"] = labels
    table = table.sort_values("expected_attempts", ascending=False)
    return {
        "model": "difficulty tertiles by expected attempts plus RandomForestClassifier from date and word attributes",
        "thresholds_expected_attempts": {"easy_max": clean_float(q1), "medium_max": clean_float(q2)},
        "holdout_days": len(holdout),
        "holdout_accuracy": clean_float(accuracy),
        "eerie_expected_attempts_from_distribution": clean_float(eerie_expected_attempts),
        "eerie_class": threshold_eerie_class,
        "eerie_classifier_class": model_eerie_class,
        "feature_importance": importances,
        "hardest_words": [
            {
                "date": row["Date"].date().isoformat(),
                "word": row["Word"],
                "expected_attempts": clean_float(row["expected_attempts"]),
                "difficulty_class": row["difficulty_class"],
            }
            for _, row in table.head(12).iterrows()
        ],
        "easiest_words": [
            {
                "date": row["Date"].date().isoformat(),
                "word": row["Word"],
                "expected_attempts": clean_float(row["expected_attempts"]),
                "difficulty_class": row["difficulty_class"],
            }
            for _, row in table.tail(12).sort_values("expected_attempts").iterrows()
        ],
    }


def interesting_features(df: pd.DataFrame) -> dict[str, object]:
    first30 = df.head(30)["Number of reported results"].mean()
    last30 = df.tail(30)["Number of reported results"].mean()
    repeated = df[df["repeated_letters"] > 0]
    non_repeated = df[df["repeated_letters"] == 0]
    corr = df[["Number of reported results", "hard_mode_rate", "expected_attempts", "repeated_letters", "unique_letters", "vowel_count"]].corr()
    weekday_summary = (
        df.groupby("weekday", as_index=False)
        .agg(mean_reported_results=("Number of reported results", "mean"), mean_expected_attempts=("expected_attempts", "mean"))
        .assign(weekday=lambda part: part["weekday"].map({0: "Mon", 1: "Tue", 2: "Wed", 3: "Thu", 4: "Fri", 5: "Sat", 6: "Sun"}))
    )
    return {
        "reported_results_first30_mean": clean_float(first30, 2),
        "reported_results_last30_mean": clean_float(last30, 2),
        "reported_results_change_pct_first30_to_last30": clean_float((last30 - first30) / first30 * 100, 2),
        "repeated_letter_word_count": int(len(repeated)),
        "non_repeated_letter_word_count": int(len(non_repeated)),
        "repeated_letter_expected_attempts_mean": clean_float(repeated["expected_attempts"].mean()),
        "non_repeated_expected_attempts_mean": clean_float(non_repeated["expected_attempts"].mean()),
        "hard_mode_rate_mean": clean_float(df["hard_mode_rate"].mean()),
        "correlations": {
            f"{a}__{b}": clean_float(corr.loc[a, b])
            for a, b in [
                ("Number of reported results", "hard_mode_rate"),
                ("expected_attempts", "repeated_letters"),
                ("expected_attempts", "unique_letters"),
                ("expected_attempts", "vowel_count"),
            ]
        },
        "weekday_summary": [
            {
                "weekday": row["weekday"],
                "mean_reported_results": clean_float(row["mean_reported_results"], 2),
                "mean_expected_attempts": clean_float(row["mean_expected_attempts"]),
            }
            for _, row in weekday_summary.iterrows()
        ],
    }


def write_artifacts(
    df: pd.DataFrame,
    report_count: dict[str, object],
    eerie_prediction: dict[str, object],
    difficulty: dict[str, object],
) -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(ARTIFACT_DIR / "wordle_clean_data.csv", index=False, encoding="utf-8-sig")
    pd.DataFrame(eerie_prediction["table_rows"]).to_csv(ARTIFACT_DIR / "eerie_prediction.csv", index=False, encoding="utf-8-sig")
    pd.DataFrame(difficulty["feature_importance"]).to_csv(
        ARTIFACT_DIR / "difficulty_feature_importance.csv", index=False, encoding="utf-8-sig"
    )
    difficulty_rows = []
    for key in ("hardest_words", "easiest_words"):
        for row in difficulty[key]:
            tagged = dict(row)
            tagged["group"] = key
            difficulty_rows.append(tagged)
    pd.DataFrame(difficulty_rows).to_csv(ARTIFACT_DIR / "difficulty_by_word.csv", index=False, encoding="utf-8-sig")

    fig, ax = plt.subplots(figsize=(9, 4.8))
    ax.plot(df["Date"], df["Number of reported results"], color="#2a6f97", linewidth=1.6, label="official daily reports")
    ax.scatter([PREDICTION_DATE], [report_count["predicted_reported_results"]], color="#d62828", zorder=3, label="2023-03-01 forecast")
    lo, hi = report_count["prediction_interval_80"]
    ax.vlines(PREDICTION_DATE, lo, hi, color="#d62828", linewidth=3, alpha=0.55, label="80% interval")
    ax.set_title("Wordle reported-result trend and March 1 forecast")
    ax.set_xlabel("Date")
    ax.set_ylabel("Reported results")
    ax.grid(alpha=0.25)
    ax.legend(loc="best")
    fig.autofmt_xdate()
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "reported_results_forecast.png", dpi=180)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(8.5, 4.8))
    rows = eerie_prediction["table_rows"]
    ax.bar([row["bucket"] for row in rows], [row["predicted_percent"] for row in rows], color="#52796f")
    ax.set_title("Predicted distribution for EERIE on 2023-03-01")
    ax.set_ylabel("Percent")
    ax.tick_params(axis="x", rotation=30)
    ax.grid(axis="y", alpha=0.25)
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "eerie_distribution.png", dpi=180)
    plt.close(fig)


def write_report(result: dict[str, object]) -> None:
    report = result["report_count_model"]
    pred = result["eerie_prediction"]
    difficulty = result["difficulty_model"]
    features = result["interesting_features"]
    lines = [
        "# 2023 MCM-C Wordle 真实数据实验报告",
        "",
        "## 数据来源",
        f"- 官方附件：`{result['data_source']['path']}`。",
        f"- 清洗后记录数：{result['data_source']['records']}，日期范围：{result['data_source']['date_min']} 到 {result['data_source']['date_max']}。",
        "- 读取字段包括日期、比赛编号、答案词、报告人数、困难模式人数和 1/2/3/4/5/6/X 百分比分布。",
        "",
        "## Q1 报告人数变化与困难模式比例",
        "- 模型：对报告人数取对数后做 RidgeCV 回归，特征包含时间趋势、星期、比赛编号和答案词字母属性。",
        f"- 最近 {report['holdout_days']} 天留出检验 MAE/RMSE：{report['holdout_mae_reported_results']} / {report['holdout_rmse_reported_results']}。",
        f"- 对 {report['prediction_date']} 的报告人数预测：{report['predicted_reported_results']}，80% 区间 {report['prediction_interval_80']}。",
        f"- EERIE 的困难模式比例预测：{report['predicted_hard_mode_rate']}；困难模式比例留出 MAE：{report['hard_mode_holdout_mae_rate']}。",
        "- 词属性影响用标准化 Ridge 系数排序，绝对值越大代表关联更强。",
        "",
        "## Q2 EERIE 分布预测",
        f"- 模型：{pred['model']}。",
        f"- 留出集平均桶 MAE：{pred['holdout_mean_bucket_mae_percent_points']} 个百分点。",
        "",
        "| bucket | predicted_percent | interval80 | holdout_mae_pp |",
        "|---|---:|---|---:|",
    ]
    for row in pred["table_rows"]:
        interval = pred["prediction_intervals_80"][row["bucket"]]
        lines.append(f"| {row['bucket']} | {row['predicted_percent']} | {interval} | {row['holdout_mae_percent_points']} |")
    lines.extend(
        [
            "",
            "## Q3 难度分类",
            "- 难度指标：用 1/2/3/4/5/6/X 分布计算期望尝试次数，其中 X 按第 7 档处理。",
            f"- easy/medium 阈值：{difficulty['thresholds_expected_attempts']['easy_max']}；medium/hard 阈值：{difficulty['thresholds_expected_attempts']['medium_max']}。",
            f"- 最近 {difficulty['holdout_days']} 天分类留出准确率：{difficulty['holdout_accuracy']}。",
            f"- EERIE 按预测分布得到期望尝试次数 {difficulty['eerie_expected_attempts_from_distribution']}，分类为 `{difficulty['eerie_class']}`。",
            "",
            "## Q4 数据集其他特征",
            f"- 前 30 天平均报告人数：{features['reported_results_first30_mean']}；后 30 天平均报告人数：{features['reported_results_last30_mean']}；变化 {features['reported_results_change_pct_first30_to_last30']}%。",
            f"- 重复字母词平均期望尝试次数：{features['repeated_letter_expected_attempts_mean']}；非重复字母词：{features['non_repeated_expected_attempts_mean']}。",
            f"- 困难模式平均占比：{features['hard_mode_rate_mean']}。",
            "",
            "## 给纽约时报 Puzzle Editor 的摘要信",
            str(result["editor_letter"]),
            "",
            "## 输出文件",
            f"- `result.json`：{RESULT_PATH}",
            f"- `wordle_clean_data.csv`：{ARTIFACT_DIR / 'wordle_clean_data.csv'}",
            f"- `eerie_prediction.csv`：{ARTIFACT_DIR / 'eerie_prediction.csv'}",
            f"- `reported_results_forecast.png`：{ARTIFACT_DIR / 'reported_results_forecast.png'}",
            f"- `eerie_distribution.png`：{ARTIFACT_DIR / 'eerie_distribution.png'}",
        ]
    )
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def editor_letter(report_count: dict[str, object], pred: dict[str, object], difficulty: dict[str, object], features: dict[str, object]) -> str:
    peak_bucket = max(pred["predicted_distribution_percent"].items(), key=lambda item: item[1])
    return (
        "Dear Puzzle Editor,\n\n"
        "Using the official 2022 Wordle result file, we modeled participation, score distribution, and word difficulty "
        "from observed Twitter-reported outcomes rather than from generated placeholder data. Report counts decline strongly over "
        "the year, so the March 1, 2023 forecast is driven mainly by time trend with word attributes as secondary corrections. "
        f"For EERIE on 2023-03-01, the model predicts about {report_count['predicted_reported_results']} reports "
        f"with an 80% interval of {report_count['prediction_interval_80']}. The most likely score bucket is {peak_bucket[0]} "
        f"at {peak_bucket[1]}%. Its expected-attempt difficulty is {difficulty['eerie_expected_attempts_from_distribution']}, "
        f"classified as {difficulty['eerie_class']}. Repeated letters and lower unique-letter counts are associated with higher "
        "expected attempts, which is consistent with EERIE's repeated vowel structure.\n\n"
        f"The data also show a participation drop from the first 30 days to the last 30 days of {features['reported_results_change_pct_first30_to_last30']}%, "
        "and a stable concentration of outcomes around the middle attempt buckets. We recommend using the model as an operational "
        "forecasting baseline and re-estimating it monthly as new official Wordle outcomes become available.\n\n"
        "Sincerely,\nMCM modeling team"
    )


def main() -> None:
    df = read_wordle_workbook()
    df, freq = add_features(df)
    future_x = future_feature_frame(df, freq, PREDICTION_WORD, PREDICTION_DATE)
    report_count = report_count_analysis(df, future_x)
    eerie_prediction = distribution_analysis(df, future_x)
    difficulty = difficulty_analysis(df, future_x, eerie_prediction["predicted_distribution_percent"])
    features = interesting_features(df)
    result = {
        "problem_id": "2023-C-Wordle",
        "data_source": {
            "type": "official_comap_xlsx",
            "root": str(DATA_PATH.parent),
            "path": str(DATA_PATH),
            "records": int(len(df)),
            "date_min": df["Date"].min().date().isoformat(),
            "date_max": df["Date"].max().date().isoformat(),
            "columns": ["Date", "Contest number", "Word", "Number of reported results", "Number in hard mode", *TRY_COLUMNS],
        },
        "model_features": FEATURE_COLUMNS,
        "report_count_model": report_count,
        "eerie_prediction": eerie_prediction,
        "difficulty_model": difficulty,
        "interesting_features": features,
        "editor_letter": editor_letter(report_count, eerie_prediction, difficulty, features),
    }
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    write_artifacts(df, report_count, eerie_prediction, difficulty)
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_report(result)
    print(f"wrote {RESULT_PATH}")
    print(f"wrote {REPORT_PATH}")
    print(f"wrote artifacts under {ARTIFACT_DIR}")


if __name__ == "__main__":
    main()
