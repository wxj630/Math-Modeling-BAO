from __future__ import annotations

import json
import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, average_precision_score, brier_score_loss, roc_auc_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


ARCHIVE_ROOT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
DATA_DIR = ARCHIVE_ROOT / "official_assets_extracted" / "2024" / "Problem Data- Momentum in Tennis"
POINTS_PATH = DATA_DIR / "2024_Wimbledon_featured_matches.csv"
DICTIONARY_PATH = DATA_DIR / "2024_data_dictionary.csv"
FINAL_MATCH_ID = "2023-wimbledon-1701"
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"


FEATURES = [
    "momentum_p1",
    "abs_momentum",
    "momentum_delta",
    "server_is_p1",
    "serve_no",
    "p1_break_pt",
    "p2_break_pt",
    "rally_count",
    "speed_mph",
    "distance_diff",
    "p1_unf_err",
    "p2_unf_err",
    "p1_winner",
    "p2_winner",
    "score_pressure",
]


def clean_float(value: object, digits: int = 6) -> float | None:
    if value is None:
        return None
    value = float(value)
    if math.isnan(value) or math.isinf(value):
        return None
    return round(value, digits)


def read_official_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    missing = [str(path) for path in [POINTS_PATH, DICTIONARY_PATH] if not path.exists()]
    if missing:
        raise FileNotFoundError("missing official COMAP Wimbledon data: " + ", ".join(missing))
    points = pd.read_csv(POINTS_PATH, encoding_errors="ignore")
    dictionary = pd.read_csv(DICTIONARY_PATH, encoding_errors="ignore")
    return points, dictionary


def score_pressure(row: pd.Series) -> int:
    return int(
        row.get("p1_break_pt", 0) == 1
        or row.get("p2_break_pt", 0) == 1
        or str(row.get("p1_score", "")) == "AD"
        or str(row.get("p2_score", "")) == "AD"
        or (str(row.get("p1_score", "")) == "40" and str(row.get("p2_score", "")) == "40")
    )


def prepare_points(points: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, float]]:
    df = points.copy()
    df = df.sort_values(["match_id", "set_no", "game_no", "point_no"]).reset_index(drop=True)
    df["point_index"] = df.groupby("match_id").cumcount() + 1
    df["p1_point_win"] = (df["point_victor"] == 1).astype(float)
    df["server_won"] = (df["point_victor"] == df["server"]).astype(float)
    serve_rates = df.groupby("serve_no")["server_won"].mean().to_dict()
    fallback_rate = float(df["server_won"].mean())
    df["expected_server_win"] = df["serve_no"].map(serve_rates).fillna(fallback_rate)
    df["expected_p1_win"] = np.where(df["server"] == 1, df["expected_server_win"], 1 - df["expected_server_win"])
    df["serve_adjusted_residual"] = df["p1_point_win"] - df["expected_p1_win"]
    df["momentum_p1"] = df.groupby("match_id")["serve_adjusted_residual"].transform(
        lambda s: s.ewm(alpha=0.18, adjust=False).mean()
    )
    df["momentum_delta"] = df.groupby("match_id")["momentum_p1"].diff().fillna(0)
    df["abs_momentum"] = df["momentum_p1"].abs()
    df["server_is_p1"] = (df["server"] == 1).astype(int)
    df["distance_diff"] = pd.to_numeric(df["p1_distance_run"], errors="coerce") - pd.to_numeric(df["p2_distance_run"], errors="coerce")
    df["score_pressure"] = df.apply(score_pressure, axis=1)
    for col in FEATURES:
        df[col] = pd.to_numeric(df[col], errors="coerce")
        df[col] = df[col].fillna(df[col].median() if not df[col].dropna().empty else 0)
    df["momentum_side"] = np.where(df["momentum_p1"] > 0.03, "player1", np.where(df["momentum_p1"] < -0.03, "player2", "balanced"))
    metrics = {
        "server_win_rate_all_points": clean_float(fallback_rate),
        "server_win_rate_first_serve_points": clean_float(serve_rates.get(1, fallback_rate)),
        "server_win_rate_second_serve_points": clean_float(serve_rates.get(2, fallback_rate)),
    }
    return df, metrics


def add_swing_label(df: pd.DataFrame, horizon: int = 8, threshold: float = 0.08) -> pd.DataFrame:
    out = df.copy()
    labels = []
    for _, match in out.groupby("match_id", sort=False):
        values = match["momentum_p1"].to_numpy()
        match_labels = np.zeros(len(match), dtype=int)
        for i, value in enumerate(values):
            current_sign = np.sign(value)
            if current_sign == 0:
                current_sign = 1
            future = values[i + 1 : i + 1 + horizon]
            if future.size:
                changed = np.sign(future) != current_sign
                strong = np.abs(future) >= threshold
                match_labels[i] = int(bool(np.any(changed & strong)))
        labels.extend(match_labels.tolist())
    out["future_swing_8"] = labels
    return out


def safe_classification_metrics(y_true: pd.Series, proba: np.ndarray) -> dict[str, float | None]:
    pred = (proba >= 0.5).astype(int)
    metrics: dict[str, float | None] = {
        "accuracy": clean_float(accuracy_score(y_true, pred)),
        "brier": clean_float(brier_score_loss(y_true, proba)),
        "positive_rate": clean_float(float(pd.Series(y_true).mean())),
    }
    if len(set(y_true)) == 2:
        metrics["roc_auc"] = clean_float(roc_auc_score(y_true, proba))
        metrics["average_precision"] = clean_float(average_precision_score(y_true, proba))
    else:
        metrics["roc_auc"] = None
        metrics["average_precision"] = None
    return metrics


def point_streaks(match: pd.DataFrame) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    current_player = None
    start = 0
    length = 0
    for i, victor in enumerate(match["point_victor"].astype(int).tolist(), start=1):
        if victor != current_player:
            if current_player is not None:
                rows.append({"player": int(current_player), "start_point": start, "length": length})
            current_player = victor
            start = i
            length = 1
        else:
            length += 1
    if current_player is not None:
        rows.append({"player": int(current_player), "start_point": start, "length": length})
    return sorted(rows, key=lambda item: item["length"], reverse=True)


def flow_summary(df: pd.DataFrame) -> tuple[dict[str, object], pd.DataFrame]:
    final = df[df["match_id"] == FINAL_MATCH_ID].copy()
    if final.empty:
        raise ValueError(f"final match {FINAL_MATCH_ID} not found in official data")
    final["p1_player"] = final["player1"]
    final["p2_player"] = final["player2"]
    final["better_player"] = np.where(
        final["momentum_p1"] > 0.03,
        final["player1"],
        np.where(final["momentum_p1"] < -0.03, final["player2"], "balanced"),
    )
    sign = np.sign(final["momentum_p1"])
    swings = int(((sign != sign.shift(1)) & (final["momentum_p1"].abs() >= 0.08)).sum())
    top = final.iloc[final["momentum_p1"].abs().argsort()[::-1][:8]][
        ["point_index", "set_no", "game_no", "point_no", "player1", "player2", "better_player", "momentum_p1", "server", "point_victor"]
    ]
    summary = {
        "match_id": FINAL_MATCH_ID,
        "player1": str(final["player1"].iloc[0]),
        "player2": str(final["player2"].iloc[0]),
        "points": int(len(final)),
        "momentum_min_p1": clean_float(final["momentum_p1"].min()),
        "momentum_max_p1": clean_float(final["momentum_p1"].max()),
        "strong_sign_changes": swings,
        "longest_point_streaks": point_streaks(final)[:5],
        "largest_momentum_points": [
            {
                "point_index": int(row["point_index"]),
                "set_no": int(row["set_no"]),
                "game_no": int(row["game_no"]),
                "better_player": str(row["better_player"]),
                "momentum_p1": clean_float(row["momentum_p1"]),
            }
            for _, row in top.iterrows()
        ],
    }
    return summary, final


def randomness_assessment(df: pd.DataFrame) -> dict[str, object]:
    rows = []
    for match_id, match in df.groupby("match_id"):
        residual = match["serve_adjusted_residual"].to_numpy()
        if len(residual) < 3 or np.std(residual[:-1]) == 0 or np.std(residual[1:]) == 0:
            continue
        lag1 = float(np.corrcoef(residual[:-1], residual[1:])[0, 1])
        streaks = point_streaks(match)
        rows.append(
            {
                "match_id": match_id,
                "lag1_residual_corr": lag1,
                "longest_point_streak": int(streaks[0]["length"]) if streaks else 0,
                "momentum_range": float(match["momentum_p1"].max() - match["momentum_p1"].min()),
            }
        )
    table = pd.DataFrame(rows)
    final_row = table[table["match_id"] == FINAL_MATCH_ID].iloc[0]
    mean_lag = float(table["lag1_residual_corr"].mean())
    se_lag = float(table["lag1_residual_corr"].std(ddof=1) / math.sqrt(len(table))) if len(table) > 1 else float("nan")
    z_score = mean_lag / se_lag if se_lag and not math.isnan(se_lag) else float("nan")
    return {
        "match_count": int(len(table)),
        "mean_lag1_serve_adjusted_corr": clean_float(mean_lag),
        "lag1_z_score_across_matches": clean_float(z_score),
        "final_match_lag1_corr": clean_float(final_row["lag1_residual_corr"]),
        "final_match_longest_point_streak": int(final_row["longest_point_streak"]),
        "final_match_momentum_range": clean_float(final_row["momentum_range"]),
        "interpretation": "Serve-adjusted residual correlation and long runs quantify whether point flow departs from independent point-by-point variation; values are evidence of temporal structure, not proof of psychological causality.",
    }


def swing_prediction(df: pd.DataFrame) -> tuple[dict[str, object], pd.DataFrame]:
    labeled = add_swing_label(df)
    train = labeled[labeled["match_id"] != FINAL_MATCH_ID].copy()
    test = labeled[labeled["match_id"] == FINAL_MATCH_ID].copy()
    model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000, class_weight="balanced", random_state=2024))
    model.fit(train[FEATURES], train["future_swing_8"])
    train_proba = model.predict_proba(train[FEATURES])[:, 1]
    test_proba = model.predict_proba(test[FEATURES])[:, 1]
    logistic = model.named_steps["logisticregression"]
    coef = pd.DataFrame({"feature": FEATURES, "coefficient": logistic.coef_[0]}).sort_values("coefficient", key=lambda s: s.abs(), ascending=False)
    top_coef = [{"feature": row["feature"], "coefficient": clean_float(row["coefficient"])} for _, row in coef.head(10).iterrows()]
    test = test.copy()
    test["swing_probability_next_8_points"] = test_proba
    high_alerts = test.sort_values("swing_probability_next_8_points", ascending=False).head(8)
    summary = {
        "target": "future momentum sign change with |momentum| >= 0.08 in the next 8 points",
        "features": FEATURES,
        "train_rows": int(len(train)),
        "holdout_match_id": FINAL_MATCH_ID,
        "holdout_rows": int(len(test)),
        "train_metrics": safe_classification_metrics(train["future_swing_8"], train_proba),
        "holdout_final_match_metrics": safe_classification_metrics(test["future_swing_8"], test_proba),
        "top_coefficients_abs": top_coef,
        "highest_alert_points_final": [
            {
                "point_index": int(row["point_index"]),
                "set_no": int(row["set_no"]),
                "game_no": int(row["game_no"]),
                "probability": clean_float(row["swing_probability_next_8_points"]),
                "momentum_p1": clean_float(row["momentum_p1"]),
            }
            for _, row in high_alerts.iterrows()
        ],
    }
    return summary, coef


def match_generalization(df: pd.DataFrame) -> dict[str, object]:
    rows = []
    for match_id, match in df.groupby("match_id"):
        if len(match) < 40:
            continue
        p1_final = int(match["p1_points_won"].iloc[-1])
        p2_final = int(match["p2_points_won"].iloc[-1])
        predicted_edge = float(match["momentum_p1"].tail(30).mean())
        predicted_winner = 1 if predicted_edge >= 0 else 2
        actual_winner = 1 if p1_final >= p2_final else 2
        rows.append(
            {
                "match_id": match_id,
                "points": int(len(match)),
                "predicted_winner_from_last30_momentum": predicted_winner,
                "actual_point_winner": actual_winner,
                "correct": int(predicted_winner == actual_winner),
                "last30_momentum_p1": predicted_edge,
            }
        )
    table = pd.DataFrame(rows)
    final = table[table["match_id"] == FINAL_MATCH_ID].iloc[0].to_dict()
    return {
        "evaluated_matches": int(len(table)),
        "last30_momentum_winner_accuracy": clean_float(table["correct"].mean()),
        "final_match_prediction": {
            "predicted_winner_from_last30_momentum": int(final["predicted_winner_from_last30_momentum"]),
            "actual_point_winner": int(final["actual_point_winner"]),
            "correct": int(final["correct"]),
            "last30_momentum_p1": clean_float(final["last30_momentum_p1"]),
        },
        "limitation": "This evaluates point-share winner, not official match winner by sets; it is a robustness check for flow signal transfer across matches.",
    }


def write_artifacts(final: pd.DataFrame, coef: pd.DataFrame, result: dict[str, object]) -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    flow_cols = [
        "match_id",
        "point_index",
        "set_no",
        "game_no",
        "point_no",
        "player1",
        "player2",
        "server",
        "point_victor",
        "expected_p1_win",
        "serve_adjusted_residual",
        "momentum_p1",
        "better_player",
    ]
    final[flow_cols].to_csv(ARTIFACT_DIR / "final_match_momentum_flow.csv", index=False, encoding="utf-8-sig")
    coef.to_csv(ARTIFACT_DIR / "swing_model_coefficients.csv", index=False, encoding="utf-8-sig")
    pd.DataFrame(result["flow_summary"]["largest_momentum_points"]).to_csv(
        ARTIFACT_DIR / "largest_momentum_points.csv", index=False, encoding="utf-8-sig"
    )

    plt.figure(figsize=(11, 5.8))
    plt.plot(final["point_index"], final["momentum_p1"], color="#1f5c99", linewidth=1.8, label="P1 serve-adjusted momentum")
    plt.axhline(0, color="#222222", linewidth=0.8)
    plt.axhline(0.08, color="#7a9e2f", linewidth=0.8, linestyle="--", label="strong edge threshold")
    plt.axhline(-0.08, color="#a63d40", linewidth=0.8, linestyle="--")
    set_changes = final.loc[final["set_no"].diff().fillna(0) > 0, "point_index"].tolist()
    for point in set_changes:
        plt.axvline(point, color="#999999", linewidth=0.7, alpha=0.5)
    plt.title("2023 Wimbledon Final: serve-adjusted momentum flow")
    plt.xlabel("Point index")
    plt.ylabel("Momentum toward player 1")
    plt.legend(loc="best")
    plt.tight_layout()
    plt.savefig(ARTIFACT_DIR / "final_match_momentum_flow.png", dpi=180)
    plt.close()


def write_report(result: dict[str, object]) -> None:
    flow = result["flow_summary"]
    swing = result["swing_prediction"]
    general = result["generalization"]
    lines = [
        "# 2024 MCM-C Momentum in Tennis 真实数据解法",
        "",
        "## 数据来源",
        "- 使用 COMAP 官方 `2024_Wimbledon_featured_matches.csv` 和 `2024_data_dictionary.csv`。",
        "- 每一行是温网 2023 男单第三轮以后比赛的一分；本解法不生成随机比赛数据。",
        "",
        "## 建模核心",
        "- 先估计发球方在一发/二发情境下的平均得分率，得到每分中 player1 的发球校正期望胜率。",
        "- 用 `actual_p1_win - expected_p1_win` 得到去除发球优势后的残差。",
        "- 对残差做指数加权平均，定义 `momentum_p1`；正值表示 player1 超出发球期望，负值表示 player2 占优。",
        "- 以未来 8 分内是否发生强势头换向作为波动预测标签，训练逻辑回归模型解释关键因素。",
        "",
        "## 官方数据规模",
        f"- 逐分记录：{result['data_source']['rows']['2024_Wimbledon_featured_matches.csv']} 行。",
        f"- 数据字典：{result['data_source']['rows']['2024_data_dictionary.csv']} 行。",
        f"- 比赛数：{result['data_source']['match_count']} 场。",
        "",
        "## Q1 比赛流程和可视化",
        f"- 决赛 `{flow['match_id']}`：{flow['player1']} vs {flow['player2']}，共 {flow['points']} 分。",
        f"- `momentum_p1` 范围：[{flow['momentum_min_p1']}, {flow['momentum_max_p1']}]。",
        f"- 强势头换向次数：{flow['strong_sign_changes']}。",
        "- 可视化：`artifacts/final_match_momentum_flow.png`。",
        "",
        "## Q2 随机波动假设评估",
        f"- 全部比赛发球校正残差 lag-1 平均相关：{result['randomness_assessment']['mean_lag1_serve_adjusted_corr']}。",
        f"- 跨比赛 z 值：{result['randomness_assessment']['lag1_z_score_across_matches']}。",
        f"- 决赛最长连续得分串：{result['randomness_assessment']['final_match_longest_point_streak']} 分。",
        "- 解释：该证据能反驳“完全没有时间结构”的强表述，但不能单独证明心理动量因果。",
        "",
        "## Q3 波动预测模型",
        f"- 训练行数：{swing['train_rows']}，留出比赛：{swing['holdout_match_id']}。",
        f"- 训练 ROC-AUC：{swing['train_metrics']['roc_auc']}，留出 ROC-AUC：{swing['holdout_final_match_metrics']['roc_auc']}。",
        f"- 留出 Brier：{swing['holdout_final_match_metrics']['brier']}。",
        "",
        "### 关键特征系数",
        "| feature | coefficient |",
        "|---|---:|",
    ]
    for row in swing["top_coefficients_abs"][:10]:
        lines.append(f"| {row['feature']} | {row['coefficient']} |")
    lines.extend([
        "",
        "## Q4 泛化测试",
        f"- 使用最后 30 分平均势头预测点数优势方，跨 {general['evaluated_matches']} 场准确率：{general['last30_momentum_winner_accuracy']}。",
        f"- 决赛留出检查：{general['final_match_prediction']}。",
        "- 局限：该检验针对逐分优势信号，不等同于正式盘分制胜负预测。",
        "",
        "## Q5 给教练的建议摘要",
        "- 动量不是神秘变量，可以被定义为发球校正后的连续超预期表现。",
        "- 比赛中应重点监控 `abs_momentum`、`momentum_delta`、破发点压力、非受迫失误和制胜分。",
        "- 当未来 8 分换向概率升高时，建议通过发球落点、接发保守度、拍间恢复和局间战术沟通降低连续丢分风险。",
        "",
        "## 输出文件",
        "- `result.json`：结构化结果。",
        "- `artifacts/final_match_momentum_flow.csv`：决赛逐分势头表。",
        "- `artifacts/final_match_momentum_flow.png`：决赛势头曲线。",
        "- `artifacts/swing_model_coefficients.csv`：波动预测模型系数。",
    ])
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    points, dictionary = read_official_data()
    prepared, serve_metrics = prepare_points(points)
    flow, final = flow_summary(prepared)
    random_check = randomness_assessment(prepared)
    swing, coef = swing_prediction(prepared)
    general = match_generalization(prepared)
    result: dict[str, object] = {
        "problem": "2024 MCM-C Momentum in Tennis",
        "data_source": {
            "type": "official_comap_csv",
            "root": str(DATA_DIR),
            "rows": {
                "2024_Wimbledon_featured_matches.csv": int(len(points)),
                "2024_data_dictionary.csv": int(len(dictionary)),
            },
            "match_count": int(points["match_id"].nunique()),
            "columns": list(points.columns),
        },
        "serve_baseline": serve_metrics,
        "flow_summary": flow,
        "randomness_assessment": random_check,
        "swing_prediction": swing,
        "generalization": general,
        "coach_memo": {
            "message": "Treat momentum as a measurable serve-adjusted flow signal. It is useful for alerts and preparation, but it should be paired with tactical video review rather than treated as a standalone cause.",
            "recommended_live_indicators": ["abs_momentum", "momentum_delta", "break_point_pressure", "unforced_errors", "winner_rate"],
        },
        "model_features": FEATURES,
    }
    ROOT.mkdir(parents=True, exist_ok=True)
    write_artifacts(final, coef, result)
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_report(result)
    print(json.dumps({"result": str(RESULT_PATH), "report": str(REPORT_PATH)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
