from __future__ import annotations

import json
import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error


ARCHIVE_ROOT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
DATA_DIR = (
    ARCHIVE_ROOT
    / "official_assets_extracted"
    / "2025"
    / "2025_Problem_C_Data.zip"
    / "2025_Problem_C_Data"
)
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"


def clean_float(value: float) -> float:
    return round(float(value), 6)


def read_official_data() -> dict[str, pd.DataFrame]:
    files = {
        "summerOly_medal_counts.csv": DATA_DIR / "summerOly_medal_counts.csv",
        "summerOly_athletes.csv": DATA_DIR / "summerOly_athletes.csv",
        "summerOly_hosts.csv": DATA_DIR / "summerOly_hosts.csv",
        "summerOly_programs.csv": DATA_DIR / "summerOly_programs.csv",
        "data_dictionary.csv": DATA_DIR / "data_dictionary.csv",
    }
    missing = [str(path) for path in files.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing official COMAP data files: " + ", ".join(missing))
    return {name: pd.read_csv(path, encoding_errors="ignore") for name, path in files.items()}


def host_country(host_text: str) -> str:
    text = str(host_text).replace("\xa0", " ").strip()
    return text.split(",")[-1].strip()


def add_zero_medal_athlete_countries(medals: pd.DataFrame, athletes: pd.DataFrame) -> pd.DataFrame:
    athlete_nocs = athletes[["Year", "Team"]].drop_duplicates().rename(columns={"Team": "NOC"})
    existing = medals[["Year", "NOC"]].drop_duplicates()
    missing = athlete_nocs.merge(existing, on=["Year", "NOC"], how="left", indicator=True)
    missing = missing[missing["_merge"] == "left_only"][["Year", "NOC"]]
    if missing.empty:
        return medals
    zero_rows = missing.assign(Rank=np.nan, Gold=0, Silver=0, Bronze=0, Total=0)
    return pd.concat([medals, zero_rows[medals.columns]], ignore_index=True)


def year_event_counts(programs: pd.DataFrame) -> pd.DataFrame:
    year_columns = [col for col in programs.columns if str(col).isdigit()]
    rows = []
    for year in year_columns:
        values = pd.to_numeric(programs[year], errors="coerce").fillna(0)
        rows.append({"Year": int(year), "event_count": float(values.sum()), "sport_count": int((values > 0).sum())})
    return pd.DataFrame(rows)


def athlete_features(athletes: pd.DataFrame) -> pd.DataFrame:
    grouped = athletes.groupby(["Year", "Team"], as_index=False).agg(
        athlete_count=("Name", "count"),
        entered_sports=("Sport", "nunique"),
        entered_events=("Event", "nunique"),
    )
    return grouped.rename(columns={"Team": "NOC"})


def build_model_table(data: dict[str, pd.DataFrame]) -> pd.DataFrame:
    medals = data["summerOly_medal_counts.csv"].copy()
    athletes = data["summerOly_athletes.csv"].copy()
    medals = add_zero_medal_athlete_countries(medals, athletes)
    medals = medals.sort_values(["NOC", "Year"]).reset_index(drop=True)

    for col in ("Gold", "Silver", "Bronze", "Total"):
        medals[col] = pd.to_numeric(medals[col], errors="coerce").fillna(0)
    medals["prev_gold"] = medals.groupby("NOC")["Gold"].shift(1).fillna(0)
    medals["prev_total"] = medals.groupby("NOC")["Total"].shift(1).fillna(0)
    medals["rolling_gold_3"] = medals.groupby("NOC")["Gold"].transform(
        lambda values: values.shift(1).rolling(3, min_periods=1).mean().fillna(0)
    )
    medals["rolling_total_3"] = medals.groupby("NOC")["Total"].transform(
        lambda values: values.shift(1).rolling(3, min_periods=1).mean().fillna(0)
    )

    hosts = data["summerOly_hosts.csv"].copy()
    hosts["host_country"] = hosts["Host"].map(host_country)
    medals = medals.merge(hosts[["Year", "host_country"]], on="Year", how="left")
    medals["is_host"] = (medals["NOC"] == medals["host_country"]).astype(int)

    table = medals.merge(athlete_features(athletes), on=["Year", "NOC"], how="left")
    table = table.merge(year_event_counts(data["summerOly_programs.csv"]), on="Year", how="left")
    for col in ("athlete_count", "entered_sports", "entered_events", "event_count", "sport_count"):
        table[col] = table[col].fillna(0)
    return table


def train_and_predict(table: pd.DataFrame) -> dict[str, object]:
    features = [
        "prev_gold",
        "prev_total",
        "rolling_gold_3",
        "rolling_total_3",
        "is_host",
        "athlete_count",
        "entered_sports",
        "entered_events",
        "event_count",
        "sport_count",
    ]
    train = table[(table["Year"] >= 1988) & (table["Year"] < 2024)].copy()
    holdout = table[table["Year"] == 2024].copy()
    if train.empty or holdout.empty:
        raise ValueError("not enough official data to train and hold out 2024")

    models: dict[str, RandomForestRegressor] = {}
    metrics: dict[str, dict[str, float]] = {}
    for target in ("Gold", "Total"):
        model = RandomForestRegressor(n_estimators=300, min_samples_leaf=2, random_state=2025, n_jobs=-1)
        model.fit(train[features], train[target])
        pred = model.predict(holdout[features])
        metrics[target] = {
            "mae_2024": clean_float(mean_absolute_error(holdout[target], pred)),
            "rmse_2024": clean_float(math.sqrt(mean_squared_error(holdout[target], pred))),
        }
        models[target] = model

    base_2024 = table[table["Year"] == 2024].copy()
    pred_2028 = base_2024.copy()
    pred_2028["Year"] = 2028
    pred_2028["prev_gold"] = base_2024["Gold"]
    pred_2028["prev_total"] = base_2024["Total"]
    pred_2028["rolling_gold_3"] = base_2024[["Gold", "prev_gold", "rolling_gold_3"]].mean(axis=1)
    pred_2028["rolling_total_3"] = base_2024[["Total", "prev_total", "rolling_total_3"]].mean(axis=1)
    pred_2028["is_host"] = (pred_2028["NOC"] == "United States").astype(int)

    prediction_frames = {}
    x_2028 = pred_2028[features].to_numpy()
    for target, model in models.items():
        tree_predictions = np.vstack([tree.predict(x_2028) for tree in model.estimators_])
        pred_2028[f"pred_{target.lower()}"] = np.maximum(0, tree_predictions.mean(axis=0))
        pred_2028[f"lo_{target.lower()}"] = np.maximum(0, np.quantile(tree_predictions, 0.1, axis=0))
        pred_2028[f"hi_{target.lower()}"] = np.maximum(0, np.quantile(tree_predictions, 0.9, axis=0))
        prediction_frames[target] = tree_predictions

    historically_medaled = set(table.loc[table["Year"] <= 2024].groupby("NOC")["Total"].sum().loc[lambda s: s > 0].index)
    no_medal = pred_2028[~pred_2028["NOC"].isin(historically_medaled)].copy()
    total_tree = prediction_frames["Total"]
    no_medal_idx = list(no_medal.index)
    if no_medal_idx:
        first_medal_probs = (total_tree[:, [pred_2028.index.get_loc(i) for i in no_medal_idx]] >= 0.5).mean(axis=0)
        expected_first_medals = float(first_medal_probs.sum())
    else:
        expected_first_medals = 0.0

    top_total = pred_2028.sort_values("pred_total", ascending=False).head(15)
    top_gold = pred_2028.sort_values("pred_gold", ascending=False).head(15)
    changes = pred_2028.assign(total_change=pred_2028["pred_total"] - pred_2028["Total"])
    return {
        "features": features,
        "metrics": metrics,
        "pred_2028": pred_2028,
        "prediction_2028_top_total": rows_for_prediction(top_total, "total"),
        "prediction_2028_top_gold": rows_for_prediction(top_gold, "gold"),
        "most_likely_improve": rows_for_change(changes.sort_values("total_change", ascending=False).head(10)),
        "most_likely_decline": rows_for_change(changes.sort_values("total_change").head(10)),
        "first_medal_expected_count": clean_float(expected_first_medals),
    }


def rows_for_prediction(df: pd.DataFrame, target: str) -> list[dict[str, object]]:
    rows = []
    for _, row in df.iterrows():
        rows.append(
            {
                "NOC": row["NOC"],
                f"pred_{target}": clean_float(row[f"pred_{target}"]),
                "interval80": [clean_float(row[f"lo_{target}"]), clean_float(row[f"hi_{target}"])],
                "actual_2024_total": int(row["Total"]),
                "actual_2024_gold": int(row["Gold"]),
            }
        )
    return rows


def rows_for_change(df: pd.DataFrame) -> list[dict[str, object]]:
    return [
        {
            "NOC": row["NOC"],
            "actual_2024_total": int(row["Total"]),
            "pred_2028_total": clean_float(row["pred_total"]),
            "change": clean_float(row["total_change"]),
        }
        for _, row in df.iterrows()
    ]


def sport_importance(data: dict[str, pd.DataFrame]) -> list[dict[str, object]]:
    athletes = data["summerOly_athletes.csv"].copy()
    recent = athletes[(athletes["Year"] >= 2008) & (athletes["Medal"] != "No medal")]
    grouped = recent.groupby(["Team", "Sport"], as_index=False).size().rename(columns={"Team": "NOC", "size": "medal_athlete_rows"})
    totals = grouped.groupby("NOC")["medal_athlete_rows"].transform("sum")
    grouped["share"] = grouped["medal_athlete_rows"] / totals
    out = []
    for noc, part in grouped.sort_values(["NOC", "share"], ascending=[True, False]).groupby("NOC"):
        top = part.head(3)
        if top["medal_athlete_rows"].sum() >= 20:
            out.append(
                {
                    "NOC": noc,
                    "top_sports": [
                        {"sport": row["Sport"], "share": clean_float(row["share"]), "medal_rows": int(row["medal_athlete_rows"])}
                        for _, row in top.iterrows()
                    ],
                }
            )
    return sorted(out, key=lambda item: sum(s["medal_rows"] for s in item["top_sports"]), reverse=True)[:12]


def coach_effect_candidates(data: dict[str, pd.DataFrame]) -> list[dict[str, object]]:
    athletes = data["summerOly_athletes.csv"].copy()
    medals = athletes[athletes["Medal"] != "No medal"]
    sport_year = medals.groupby(["Team", "Sport", "Year"], as_index=False).size().rename(columns={"Team": "NOC", "size": "medal_rows"})
    sport_year = sport_year.sort_values(["NOC", "Sport", "Year"])
    sport_year["prev_mean"] = sport_year.groupby(["NOC", "Sport"])["medal_rows"].transform(
        lambda values: values.shift(1).rolling(3, min_periods=1).mean().fillna(0)
    )
    sport_year["jump"] = sport_year["medal_rows"] - sport_year["prev_mean"].fillna(0)
    candidates = sport_year[(sport_year["Year"] >= 2000) & (sport_year["jump"] >= 8)].sort_values("jump", ascending=False).head(12)
    return [
        {
            "NOC": row["NOC"],
            "Sport": row["Sport"],
            "Year": int(row["Year"]),
            "medal_rows": int(row["medal_rows"]),
            "jump_vs_recent_mean": clean_float(row["jump"]),
        }
        for _, row in candidates.iterrows()
    ]


def write_artifacts(result: dict[str, object], pred_2028: pd.DataFrame) -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    pred_cols = ["NOC", "Gold", "Total", "pred_gold", "lo_gold", "hi_gold", "pred_total", "lo_total", "hi_total", "is_host"]
    pred_2028[pred_cols].sort_values("pred_total", ascending=False).to_csv(
        ARTIFACT_DIR / "prediction_2028.csv", index=False, encoding="utf-8-sig"
    )
    pd.DataFrame(result["sport_importance"]).to_json(ARTIFACT_DIR / "sport_importance.json", force_ascii=False, indent=2)
    top = pred_2028.sort_values("pred_total", ascending=False).head(12)
    plt.figure(figsize=(9, 4.8))
    plt.bar(top["NOC"], top["pred_total"], color="#31572c")
    plt.errorbar(
        top["NOC"],
        top["pred_total"],
        yerr=[top["pred_total"] - top["lo_total"], top["hi_total"] - top["pred_total"]],
        fmt="none",
        ecolor="#222222",
        capsize=3,
    )
    plt.xticks(rotation=35, ha="right")
    plt.ylabel("Predicted total medals")
    plt.title("2028 Los Angeles medal table projection from official COMAP data")
    plt.tight_layout()
    plt.savefig(ARTIFACT_DIR / "prediction_2028_top_total.png", dpi=180)
    plt.close()


def write_report(result: dict[str, object]) -> None:
    lines = [
        "# 2025 MCM-C Models for Olympic Medal Tables 真实数据解法",
        "",
        "## 数据来源",
        "- 使用 COMAP 官方 `2025_Problem_C_Data.zip` 解压出的 5 个 CSV。",
        "- 未使用随机生成的 `x1/x2/x3` 数据。",
        "",
        "## 每问建模与求解",
        "- 奖牌榜预测：以 1988-2020 为训练集，2024 为留出检验；特征包括上一届奖牌、近三届滚动均值、东道主标记、运动员规模、参赛项目、奥运项目数量。",
        "- 2028 洛杉矶预测：用 2024 各国状态外推，设置美国为东道主，用随机森林树分布给出 80% 预测区间。",
        "- 首枚奖牌国家：把 2024 有参赛记录但历史总奖牌为 0 的 NOC 纳入候选，用树预测分布估计 `P(total>=0.5)` 后求和。",
        "- 项目重要性：按 2008-2024 运动员奖牌记录，统计各 NOC 的优势运动奖牌行占比。",
        "- “伟大教练”效应候选：在 NOC-运动-年份层面寻找相对近三届均值的突增，作为后续人工核验教练迁移的证据候选。",
        "",
        "## 运行方式",
        f"- `/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python {ROOT / 'solution.py'}`",
        "",
        "## 关键结果",
        f"- 2024 留出集 Gold MAE：{result['evaluation']['Gold']['mae_2024']}，Total MAE：{result['evaluation']['Total']['mae_2024']}",
        f"- 预计 2028 首次获得奖牌的 NOC 数量期望：{result['first_medal_expected_count']}",
        "",
        "### 2028 总奖牌预测 Top 10",
        "",
        "| NOC | 2024 total | 2028 pred total | 80% interval |",
        "|---|---:|---:|---|",
    ]
    for row in result["prediction_2028_top_total"][:10]:
        lines.append(f"| {row['NOC']} | {row['actual_2024_total']} | {row['pred_total']} | {row['interval80']} |")
    lines.extend([
        "",
        "### 最可能进步",
        "",
        "| NOC | 2024 total | 2028 pred total | change |",
        "|---|---:|---:|---:|",
    ])
    for row in result["most_likely_improve"][:10]:
        lines.append(f"| {row['NOC']} | {row['actual_2024_total']} | {row['pred_2028_total']} | {row['change']} |")
    lines.extend([
        "",
        "## 输出文件",
        "- `result.json`：完整结构化结果。",
        "- `artifacts/prediction_2028.csv`：所有 NOC 的 2028 预测表。",
        "- `artifacts/sport_importance.json`：各国优势运动。",
        "- `artifacts/prediction_2028_top_total.png`：Top 总奖牌预测图。",
    ])
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    data = read_official_data()
    table = build_model_table(data)
    model_output = train_and_predict(table)
    pred_2028 = model_output.pop("pred_2028")
    result: dict[str, object] = {
        "problem": "2025 MCM-C Models for Olympic Medal Tables",
        "data_source": {
            "type": "official_comap_csv",
            "root": str(DATA_DIR),
            "rows": {name: int(len(df)) for name, df in data.items()},
        },
        "evaluation": {"holdout_year": 2024, **model_output["metrics"]},
        "prediction_2028_top_total": model_output["prediction_2028_top_total"],
        "prediction_2028_top_gold": model_output["prediction_2028_top_gold"],
        "most_likely_improve": model_output["most_likely_improve"],
        "most_likely_decline": model_output["most_likely_decline"],
        "first_medal_expected_count": model_output["first_medal_expected_count"],
        "sport_importance": sport_importance(data),
        "coach_effect_candidates": coach_effect_candidates(data),
        "model_features": model_output["features"],
    }
    ROOT.mkdir(parents=True, exist_ok=True)
    write_artifacts(result, pred_2028)
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_report(result)
    print(json.dumps({"result": str(RESULT_PATH), "report": str(REPORT_PATH)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
