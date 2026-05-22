from __future__ import annotations

import json
import math
import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/private/tmp/matplotlib-codex-cache")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score, precision_recall_fscore_support, roc_auc_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


ARCHIVE_ROOT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
DATA_DIR = ARCHIVE_ROOT / "official_assets_extracted" / "2021" / "Problem Data- Confirming the Buzz about Hornets" / "2021_MCM_Problem_C_Data"
PDF_PATH = ARCHIVE_ROOT / "official_assets_extracted" / "2021" / "Confirming the Buzz about Hornets.pdf"
BACKGROUND_PDF = DATA_DIR / "2021MCM_ProblemC_Vespamandarina.pdf"
SIGHTINGS_XLSX = DATA_DIR / "2021MCMProblemC_DataSet.xlsx"
IMAGES_XLSX = DATA_DIR / "2021MCM_ProblemC_ Images_by_GlobalID.xlsx"
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"
QUEEN_RANGE_KM = 30
NUMERIC_FEATURES = [
    "Latitude",
    "Longitude",
    "delay_days",
    "month",
    "image_count",
    "has_photo",
    "has_video",
    "has_specimen",
    "has_photo_word",
    "mentions_bee_loss",
    "mentions_hornet",
    "distance_to_training_positive_km",
]


def clean_float(value: float, digits: int = 6) -> float:
    if pd.isna(value):
        return 0.0
    return round(float(value), digits)


def json_ready(value: object) -> object:
    if isinstance(value, dict):
        return {str(key): json_ready(item) for key, item in value.items()}
    if isinstance(value, list):
        return [json_ready(item) for item in value]
    if isinstance(value, pd.Timestamp):
        return None if pd.isna(value) else value.strftime("%Y-%m-%d")
    if isinstance(value, np.integer):
        return int(value)
    if isinstance(value, np.floating):
        return clean_float(float(value))
    if isinstance(value, np.bool_):
        return bool(value)
    if pd.isna(value):
        return None
    return value


def official_inputs() -> list[Path]:
    return [PDF_PATH, BACKGROUND_PDF, SIGHTINGS_XLSX, IMAGES_XLSX, Path(__file__).resolve()]


def outputs_are_current() -> bool:
    required = [
        RESULT_PATH,
        REPORT_PATH,
        ARTIFACT_DIR / "clean_sightings.csv",
        ARTIFACT_DIR / "classification_holdout_predictions.csv",
        ARTIFACT_DIR / "priority_reports.csv",
        ARTIFACT_DIR / "spread_timeline.csv",
        ARTIFACT_DIR / "hornet_spread_map.png",
    ]
    if any(not path.exists() for path in required):
        return False
    return min(path.stat().st_mtime for path in required) >= max(path.stat().st_mtime for path in official_inputs() if path.exists())


def read_official_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    missing = [str(path) for path in official_inputs()[:-1] if not path.exists()]
    if missing:
        raise FileNotFoundError("missing official COMAP 2021-C assets: " + ", ".join(missing))
    sightings = pd.read_excel(SIGHTINGS_XLSX)
    images = pd.read_excel(IMAGES_XLSX)
    return sightings, images


def haversine_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    radius = 6371.0088
    phi1 = math.radians(float(lat1))
    phi2 = math.radians(float(lat2))
    dphi = math.radians(float(lat2) - float(lat1))
    dlambda = math.radians(float(lon2) - float(lon1))
    a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    return 2 * radius * math.asin(math.sqrt(a))


def min_distance_to_points(frame: pd.DataFrame, points: pd.DataFrame) -> np.ndarray:
    if points.empty:
        return np.zeros(len(frame))
    distances = []
    point_rows = points[["Latitude", "Longitude"]].to_numpy(dtype=float)
    for lat, lon in frame[["Latitude", "Longitude"]].to_numpy(dtype=float):
        distances.append(min(haversine_km(lat, lon, p_lat, p_lon) for p_lat, p_lon in point_rows))
    return np.array(distances, dtype=float)


def prepare_sightings(sightings: pd.DataFrame, images: pd.DataFrame) -> pd.DataFrame:
    image_features = images.groupby("GlobalID").agg(
        image_count=("FileName", "size"),
        has_photo=("FileType", lambda values: int(values.astype(str).str.contains("image", case=False).any())),
        has_video=("FileType", lambda values: int(values.astype(str).str.contains("video", case=False).any())),
    ).reset_index()
    clean = sightings.merge(image_features, on="GlobalID", how="left")
    clean[["image_count", "has_photo", "has_video"]] = clean[["image_count", "has_photo", "has_video"]].fillna(0)
    clean["Detection Date"] = pd.to_datetime(clean["Detection Date"], errors="coerce")
    clean["Submission Date"] = pd.to_datetime(clean["Submission Date"], errors="coerce")
    clean["delay_days"] = (clean["Submission Date"] - clean["Detection Date"]).dt.days.clip(lower=0, upper=3650).fillna(0)
    clean["month"] = clean["Detection Date"].dt.month.fillna(clean["Submission Date"].dt.month).fillna(0).astype(int)
    clean["note_text"] = clean["Notes"].fillna("").astype(str) + " " + clean["Lab Comments"].fillna("").astype(str)
    clean["has_specimen"] = clean["note_text"].str.contains("specimen|collected|captured|killed|dead|sample", case=False, regex=True).astype(int)
    clean["has_photo_word"] = clean["note_text"].str.contains("photo|image|picture|camera|cam|video", case=False, regex=True).astype(int)
    clean["mentions_bee_loss"] = clean["note_text"].str.contains("bee|bees|hive|decapitat|colony", case=False, regex=True).astype(int)
    clean["mentions_hornet"] = clean["note_text"].str.contains("hornet|wasp|vespa|mandarinia", case=False, regex=True).astype(int)
    clean["processed_label"] = clean["Lab Status"].map({"Positive ID": 1, "Negative ID": 0})
    return clean


def deterministic_holdout(labeled: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    parts_train = []
    parts_test = []
    for label, frame in labeled.sort_values(["Detection Date", "Submission Date", "GlobalID"]).groupby("processed_label"):
        frame = frame.copy().reset_index(drop=False)
        mask = frame.index % 3 == 0
        parts_test.append(frame.loc[mask].set_index("index"))
        parts_train.append(frame.loc[~mask].set_index("index"))
    return pd.concat(parts_train).sort_index(), pd.concat(parts_test).sort_index()


def build_classifier() -> Pipeline:
    preprocessor = ColumnTransformer(
        [
            ("num", Pipeline([("impute", SimpleImputer(strategy="median")), ("scale", StandardScaler())]), NUMERIC_FEATURES),
            ("text", TfidfVectorizer(max_features=240, ngram_range=(1, 2), min_df=2), "note_text"),
        ]
    )
    return Pipeline(
        [
            ("preprocessor", preprocessor),
            ("classifier", LogisticRegression(max_iter=1000, class_weight="balanced", solver="liblinear")),
        ]
    )


def evaluate_classification(clean: pd.DataFrame) -> tuple[dict[str, object], pd.DataFrame, Pipeline]:
    labeled = clean[clean["processed_label"].notna()].copy()
    train, holdout = deterministic_holdout(labeled)
    positive_train = train[train["processed_label"].eq(1)]
    train = train.copy()
    holdout = holdout.copy()
    train["distance_to_training_positive_km"] = min_distance_to_points(train, positive_train)
    holdout["distance_to_training_positive_km"] = min_distance_to_points(holdout, positive_train)
    model = build_classifier()
    model.fit(train, train["processed_label"].astype(int))
    probabilities = model.predict_proba(holdout)[:, 1]
    predictions = (probabilities >= 0.5).astype(int)
    precision, recall, f1, support = precision_recall_fscore_support(
        holdout["processed_label"].astype(int), predictions, zero_division=0
    )
    holdout_predictions = holdout[["GlobalID", "Lab Status", "Detection Date", "Submission Date", "Latitude", "Longitude", "Notes"]].copy()
    holdout_predictions["positive_probability"] = probabilities
    holdout_predictions["predicted_positive"] = predictions
    metrics = {
        "model": "deterministic split + TF-IDF report text + image metadata + date/coordinate features + distance to training positive sightings + class-weighted logistic regression",
        "labeled_rows": int(len(labeled)),
        "positive_id_count": int(labeled["processed_label"].sum()),
        "negative_id_count": int((labeled["processed_label"] == 0).sum()),
        "train_rows": int(len(train)),
        "holdout_rows": int(len(holdout)),
        "holdout_positive_count": int(holdout["processed_label"].sum()),
        "holdout_metrics": {
            "roc_auc": clean_float(roc_auc_score(holdout["processed_label"].astype(int), probabilities)),
            "average_precision": clean_float(average_precision_score(holdout["processed_label"].astype(int), probabilities)),
            "positive_precision_at_0_5": clean_float(precision[1]),
            "positive_recall_at_0_5": clean_float(recall[1]),
            "positive_f1_at_0_5": clean_float(f1[1]),
            "positive_support": int(support[1]),
        },
        "assumption_warning": "Only 14 official positive IDs are available, so interval uncertainty is large even when the holdout ranking is strong.",
    }

    full_labeled = labeled.copy()
    full_labeled["distance_to_training_positive_km"] = min_distance_to_points(full_labeled, labeled[labeled["processed_label"].eq(1)])
    final_model = build_classifier()
    final_model.fit(full_labeled, full_labeled["processed_label"].astype(int))
    return metrics, holdout_predictions, final_model


def prioritize_reports(clean: pd.DataFrame, model: Pipeline) -> tuple[dict[str, object], pd.DataFrame]:
    positive_points = clean[clean["Lab Status"].eq("Positive ID")]
    scoring = clean.copy()
    scoring["distance_to_training_positive_km"] = min_distance_to_points(scoring, positive_points)
    scoring["positive_probability"] = model.predict_proba(scoring)[:, 1]
    unresolved = scoring[scoring["Lab Status"].isin(["Unprocessed", "Unverified"])].copy()
    unresolved["range_flag"] = (unresolved["distance_to_training_positive_km"] <= QUEEN_RANGE_KM).astype(int)
    unresolved["priority_score"] = (
        unresolved["positive_probability"] * 0.62
        + unresolved["range_flag"] * 0.18
        + unresolved["has_photo"].astype(float) * 0.08
        + unresolved["has_specimen"].astype(float) * 0.08
        + (1.0 / (1.0 + unresolved["delay_days"].astype(float))) * 0.04
    )
    priority_cols = [
        "GlobalID",
        "Lab Status",
        "Detection Date",
        "Submission Date",
        "Latitude",
        "Longitude",
        "positive_probability",
        "distance_to_training_positive_km",
        "priority_score",
        "image_count",
        "has_specimen",
        "Notes",
    ]
    ranked = unresolved.sort_values("priority_score", ascending=False)[priority_cols]
    top = ranked.head(15).copy()
    for col in ["positive_probability", "distance_to_training_positive_km", "priority_score"]:
        top[col] = top[col].map(clean_float)
    summary = {
        "unresolved_rows_ranked": int(len(ranked)),
        "priority_score": "0.62*classification probability + 0.18*within 30km queen range + image/specimen/date-response bonuses",
        "top_priority_reports": top.to_dict("records"),
    }
    return json_ready(summary), ranked


def spread_analysis(clean: pd.DataFrame) -> tuple[dict[str, object], pd.DataFrame]:
    positives = clean[clean["Lab Status"].eq("Positive ID")].copy().sort_values("Detection Date")
    first = positives.iloc[0]
    positives["distance_from_first_positive_km"] = [
        haversine_km(first["Latitude"], first["Longitude"], row["Latitude"], row["Longitude"])
        for row in positives.to_dict("records")
    ]
    positives["within_queen_range_of_prior_positive"] = False
    prior_points = []
    for idx, row in positives.iterrows():
        if prior_points:
            positives.loc[idx, "within_queen_range_of_prior_positive"] = min(
                haversine_km(row["Latitude"], row["Longitude"], lat, lon) for lat, lon in prior_points
            ) <= QUEEN_RANGE_KM
        prior_points.append((row["Latitude"], row["Longitude"]))
    by_month = positives.groupby(positives["Detection Date"].dt.to_period("M")).agg(
        positive_count=("GlobalID", "size"),
        mean_latitude=("Latitude", "mean"),
        mean_longitude=("Longitude", "mean"),
        max_distance_from_first_positive_km=("distance_from_first_positive_km", "max"),
    ).reset_index()
    by_month["month"] = by_month["Detection Date"].astype(str)
    by_month = by_month.drop(columns=["Detection Date"])
    return json_ready({
        "queen_range_km": QUEEN_RANGE_KM,
        "positive_id_count": int(len(positives)),
        "first_positive_detection_date": str(first["Detection Date"].date()),
        "last_positive_detection_date": str(positives["Detection Date"].max().date()),
        "max_distance_from_first_positive_km": clean_float(positives["distance_from_first_positive_km"].max()),
        "positives_within_queen_range_of_prior_positive": int(positives["within_queen_range_of_prior_positive"].sum()),
        "precision_statement": "Spread can be described as clustered public-report detections, but cannot be forecast with high spatial precision from 14 positives alone.",
        "monthly_positive_timeline": by_month.to_dict("records"),
    }), positives


def build_update_plan() -> dict[str, object]:
    return {
        "recommended_update_frequency": "weekly",
        "trigger": "Retrain when new lab labels arrive or when five or more unresolved reports accumulate within 30 km of a known positive cluster.",
        "steps": [
            "Append new official reports and image metadata to the two workbook-derived tables.",
            "Freeze previously used training labels for reproducibility, then add new Positive ID and Negative ID records.",
            "Recompute distance-to-positive and text/image features using only labels available at the update date.",
            "Run the deterministic holdout split and compare ROC-AUC, average precision, recall, and top-priority stability.",
            "Publish the updated priority list with model version, training cutoff date, and uncertainty warning.",
        ],
    }


def eradication_criteria(clean: pd.DataFrame) -> dict[str, object]:
    last_positive = clean.loc[clean["Lab Status"].eq("Positive ID"), "Detection Date"].max()
    last_submission = clean["Submission Date"].max()
    days_since_last_positive = int((last_submission - last_positive).days)
    return json_ready({
        "days_between_last_positive_and_last_submission": days_since_last_positive,
        "criteria": [
            "No Positive ID reports for at least two full active seasons after the last confirmed detection.",
            "High-priority unresolved reports inside the 30 km queen range are investigated and reclassified negative or unsupported.",
            "Targeted trap and nest-search records around prior positive clusters remain negative through fall dispersal.",
            "Public-report volume remains sufficient that absence of positives is informative, not merely a reporting gap.",
            "Model top-priority scores for new reports remain below a predeclared action threshold for a full season.",
        ],
        "current_data_assessment": "The 2020 workbook does not prove eradication: the last positive detection is too recent relative to the last submission date, and unresolved/unverified reports remain.",
    })


def write_artifacts(clean: pd.DataFrame, holdout: pd.DataFrame, priority: pd.DataFrame, positives: pd.DataFrame) -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    clean.assign(**{"Detection Date": clean["Detection Date"].astype(str), "Submission Date": clean["Submission Date"].astype(str)}).to_csv(ARTIFACT_DIR / "clean_sightings.csv", index=False)
    holdout.assign(**{"Detection Date": holdout["Detection Date"].astype(str), "Submission Date": holdout["Submission Date"].astype(str)}).to_csv(ARTIFACT_DIR / "classification_holdout_predictions.csv", index=False)
    priority.assign(**{"Detection Date": priority["Detection Date"].astype(str), "Submission Date": priority["Submission Date"].astype(str)}).to_csv(ARTIFACT_DIR / "priority_reports.csv", index=False)
    positives.assign(**{"Detection Date": positives["Detection Date"].astype(str), "Submission Date": positives["Submission Date"].astype(str)}).to_csv(ARTIFACT_DIR / "positive_sightings.csv", index=False)
    timeline = positives.groupby(positives["Detection Date"].dt.to_period("M")).size().reset_index(name="positive_count")
    timeline["month"] = timeline["Detection Date"].astype(str)
    timeline.drop(columns=["Detection Date"]).to_csv(ARTIFACT_DIR / "spread_timeline.csv", index=False)

    fig, ax = plt.subplots(figsize=(8, 6))
    status_colors = {"Positive ID": "#c43b2f", "Negative ID": "#8aa6a3", "Unverified": "#d8b365", "Unprocessed": "#5e7ce2"}
    for status, frame in clean.groupby("Lab Status"):
        ax.scatter(frame["Longitude"], frame["Latitude"], s=10 if status != "Positive ID" else 36, alpha=0.35 if status != "Positive ID" else 0.9, label=status, color=status_colors.get(status, "#777777"))
    ax.set_title("2021 MCM-C official hornet reports")
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    ax.grid(True, alpha=0.25)
    ax.legend(loc="best", fontsize=8)
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "hornet_spread_map.png", dpi=180)
    plt.close(fig)

    top = priority.head(20).sort_values("priority_score")
    fig, ax = plt.subplots(figsize=(9, 6))
    ax.barh(top["GlobalID"].str.slice(1, 9), top["priority_score"], color="#b85c38")
    ax.set_title("Top unresolved hornet investigation priorities")
    ax.set_xlabel("Priority score")
    ax.grid(axis="x", alpha=0.25)
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "priority_reports.png", dpi=180)
    plt.close(fig)


def build_memo(result: dict[str, object]) -> str:
    return (
        "To the Washington State Department of Agriculture: using only the official contest workbook and image-mapping workbook, "
        "we recommend a weekly triage cycle. Reports should be prioritized when the classifier assigns high Positive ID probability, "
        "the location lies within the 30 km queen-establishment range of prior positives, and the report includes a specimen, photo, or video. "
        f"The current deterministic holdout ROC-AUC is {result['classification_model']['holdout_metrics']['roc_auc']}, but only "
        f"{result['classification_model']['positive_id_count']} positives are available, so decisions should remain conservative. "
        "The data do not yet constitute eradication evidence; eradication would require multiple active seasons without positives, completed follow-up "
        "of high-priority unresolved reports, and negative targeted surveillance around prior clusters."
    )


def write_report(result: dict[str, object]) -> None:
    lines = [
        "# 2021 MCM-C Confirming the Buzz about Hornets",
        "",
        "## 数据与真实性",
        f"- 官方题面：`{PDF_PATH}`。",
        f"- 官方附件：`{SIGHTINGS_XLSX}` 与 `{IMAGES_XLSX}`。",
        f"- 背景资料：`{BACKGROUND_PDF}`。",
        "- 只使用题面提供的两个 Excel 和 PDF；不使用随机造数、不使用外部图片下载、不使用额外生态数据。",
        f"- 行数：`{result['data_source']['rows']}`。",
        "",
        "## 建模与求解",
        "- 数据解释：清洗检测日期、提交日期、经纬度、报告文本、实验室状态和图片/视频映射。",
        "- 误判分类：用 Positive ID / Negative ID 训练确定性留出分类器，特征包括坐标、月份、提交延迟、图片/视频、文本 TF-IDF、是否提到标本/蜂群损失，以及距训练阳性点的距离。",
        "- 资源优先级：对 Unprocessed / Unverified 报告按分类概率、30km 新蜂后范围、图片/标本证据和响应时效排序。",
        "- 更新机制：每周或新标签累计后重训，并保留训练截止日期和留出评估。",
        "- 根除证据：把无阳性持续时间、30km 范围内高优先级报告处理、主动监测阴性和公众报告量作为联合标准。",
        "",
        "## 关键结果",
        f"- Positive ID：{result['classification_model']['positive_id_count']}；Negative ID：{result['classification_model']['negative_id_count']}。",
        f"- 留出 ROC-AUC：{result['classification_model']['holdout_metrics']['roc_auc']}；Average Precision：{result['classification_model']['holdout_metrics']['average_precision']}。",
        f"- 待排序 unresolved 报告：{result['priority_investigation']['unresolved_rows_ranked']}。",
        f"- 首个阳性到最远阳性距离：{result['spread_model']['max_distance_from_first_positive_km']} km。",
        "",
        "### Top priority reports",
        "| GlobalID | Lab Status | positive_probability | distance_km | priority_score | image_count | has_specimen |",
        "|---|---|---:|---:|---:|---:|---:|",
    ]
    for row in result["priority_investigation"]["top_priority_reports"][:10]:
        lines.append(f"| {row['GlobalID']} | {row['Lab Status']} | {row['positive_probability']} | {row['distance_to_training_positive_km']} | {row['priority_score']} | {row['image_count']} | {row['has_specimen']} |")
    lines.extend([
        "",
        "## WSDA two-page memorandum",
        result["wsda_memo"],
        "",
        "## 输出文件",
        "- `artifacts/clean_sightings.csv`",
        "- `artifacts/classification_holdout_predictions.csv`",
        "- `artifacts/priority_reports.csv`",
        "- `artifacts/positive_sightings.csv`",
        "- `artifacts/spread_timeline.csv`",
        "- `artifacts/hornet_spread_map.png`",
        "- `artifacts/priority_reports.png`",
    ])
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    if outputs_are_current():
        print(json.dumps({"result": str(RESULT_PATH), "report": str(REPORT_PATH), "artifacts": str(ARTIFACT_DIR), "cached": True}, ensure_ascii=False, indent=2))
        return
    sightings, images = read_official_data()
    clean = prepare_sightings(sightings, images)
    classification, holdout_predictions, model = evaluate_classification(clean)
    priority_summary, priority_table = prioritize_reports(clean, model)
    spread_summary, positive_table = spread_analysis(clean)
    result: dict[str, object] = {
        "data_source": {
            "type": "official_comap_xlsx",
            "root": str(DATA_DIR),
            "source_pdf": str(PDF_PATH),
            "background_pdf": str(BACKGROUND_PDF),
            "rows": {
                "2021MCMProblemC_DataSet.xlsx": int(len(sightings)),
                "2021MCM_ProblemC_ Images_by_GlobalID.xlsx": int(len(images)),
            },
            "lab_status_counts": sightings["Lab Status"].value_counts(dropna=False).to_dict(),
            "only_allowed_files": ["2021MCMProblemC_DataSet.xlsx", "2021MCM_ProblemC_ Images_by_GlobalID.xlsx", "2021MCM_ProblemC_Vespamandarina.pdf"],
        },
        "classification_model": classification,
        "priority_investigation": priority_summary,
        "spread_model": spread_summary,
        "model_update_plan": build_update_plan(),
        "eradication_evidence": eradication_criteria(clean),
    }
    result["wsda_memo"] = build_memo(result)
    write_artifacts(clean, holdout_predictions, priority_table, positive_table)
    RESULT_PATH.write_text(json.dumps(json_ready(result), ensure_ascii=False, indent=2), encoding="utf-8")
    write_report(result)
    print(json.dumps({"result": str(RESULT_PATH), "report": str(REPORT_PATH), "artifacts": str(ARTIFACT_DIR)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
