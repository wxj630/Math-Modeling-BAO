from __future__ import annotations

import json
import zipfile
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import pandas as pd


ARCHIVE_ROOT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
PDF_PATH = ARCHIVE_ROOT / "official_assets" / "2020" / "A Wealth of Data"
ZIP_PATH = ARCHIVE_ROOT / "official_assets" / "2020" / "Problem Data- A Wealth of Data"
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"

TSV_FILES = {
    "hair_dryer.tsv": "Problem_C_Data/hair_dryer.tsv",
    "microwave.tsv": "Problem_C_Data/microwave.tsv",
    "pacifier.tsv": "Problem_C_Data/pacifier.tsv",
}

DESCRIPTORS = {
    "enthusiastic": ["love", "great", "excellent", "perfect", "amazing", "best"],
    "disappointed": ["disappoint", "bad", "poor", "terrible", "waste", "awful"],
    "durable": ["durable", "sturdy", "last", "reliable", "strong"],
    "broken": ["broken", "stopped", "defective", "return", "failed"],
    "easy": ["easy", "simple", "convenient"],
}


def clean_float(value: float, digits: int = 6) -> float:
    return round(float(value), digits)


def ensure_assets_exist() -> None:
    for path in [PDF_PATH, ZIP_PATH]:
        if not path.exists():
            raise FileNotFoundError(f"Official asset not found: {path}")


def read_official_tsvs() -> dict[str, pd.DataFrame]:
    frames = {}
    with zipfile.ZipFile(ZIP_PATH) as archive:
        for filename, member in TSV_FILES.items():
            with archive.open(member) as handle:
                df = pd.read_csv(handle, sep="\t", keep_default_na=False, low_memory=False)
            df["review_date"] = pd.to_datetime(df["review_date"], errors="coerce")
            df["star_rating"] = pd.to_numeric(df["star_rating"], errors="coerce")
            df["helpful_votes"] = pd.to_numeric(df["helpful_votes"], errors="coerce").fillna(0)
            df["total_votes"] = pd.to_numeric(df["total_votes"], errors="coerce").fillna(0)
            df["helpfulness_rate"] = df["helpful_votes"] / df["total_votes"].where(df["total_votes"] > 0, 1)
            df["review_text"] = (df["review_headline"].astype(str) + " " + df["review_body"].astype(str)).str.lower()
            df["review_length_words"] = df["review_text"].str.split().str.len()
            df["product_file"] = filename
            frames[filename] = df
    return frames


def build_rating_review_measures(frames: dict[str, pd.DataFrame]) -> tuple[pd.DataFrame, dict[str, Any]]:
    rows = []
    for filename, df in frames.items():
        verified_share = (df["verified_purchase"].astype(str) == "Y").mean()
        rows.append(
            {
                "product_file": filename,
                "review_count": int(len(df)),
                "unique_products": int(df["product_id"].nunique()),
                "mean_star_rating": clean_float(float(df["star_rating"].mean()), 4),
                "share_low_rating_1_2": clean_float(float((df["star_rating"] <= 2).mean()), 4),
                "mean_helpfulness_rate": clean_float(float(df["helpfulness_rate"].mean()), 4),
                "mean_review_length_words": clean_float(float(df["review_length_words"].mean()), 4),
                "verified_purchase_share": clean_float(float(verified_share), 4),
            }
        )
    product_df = pd.DataFrame(rows).sort_values("review_count", ascending=False)
    product_df.to_csv(ARTIFACT_DIR / "product_review_measures.csv", index=False)
    return product_df, {
        "method": "official TSV review measures: star ratings, helpfulness, review length, verification, and product counts",
        "product_rows": product_df.to_dict(orient="records"),
        "recommended_tracking_measures": [
            "weekly mean star rating",
            "low-rating share",
            "helpfulness-weighted review length",
            "verified-purchase review share",
            "descriptor lift for enthusiastic and disappointed language",
        ],
    }


def build_reputation_time_patterns(frames: dict[str, pd.DataFrame]) -> tuple[pd.DataFrame, pd.DataFrame, dict[str, Any]]:
    monthly_frames = []
    trend_rows = []
    for filename, df in frames.items():
        dated = df.dropna(subset=["review_date"]).copy()
        dated["month"] = dated["review_date"].dt.to_period("M").dt.to_timestamp()
        monthly = (
            dated.groupby("month")
            .agg(mean_star_rating=("star_rating", "mean"), review_count=("review_id", "count"), low_rating_share=("star_rating", lambda s: (s <= 2).mean()))
            .reset_index()
            .sort_values("month")
        )
        monthly["product_file"] = filename
        if len(monthly) >= 2:
            x = range(len(monthly))
            rating_slope = (float(monthly.iloc[-1]["mean_star_rating"]) - float(monthly.iloc[0]["mean_star_rating"])) / max(len(monthly) - 1, 1)
            low_slope = (float(monthly.iloc[-1]["low_rating_share"]) - float(monthly.iloc[0]["low_rating_share"])) / max(len(monthly) - 1, 1)
        else:
            rating_slope = 0.0
            low_slope = 0.0
        trend_rows.append(
            {
                "product_file": filename,
                "first_month": str(monthly["month"].min().date()) if len(monthly) else "",
                "last_month": str(monthly["month"].max().date()) if len(monthly) else "",
                "monthly_rating_slope": clean_float(rating_slope, 6),
                "monthly_low_rating_slope": clean_float(low_slope, 6),
                "reputation_direction": "increasing" if rating_slope > 0.004 and low_slope <= 0 else "decreasing" if rating_slope < -0.004 or low_slope > 0.003 else "stable",
            }
        )
        monthly_frames.append(monthly)
    monthly_df = pd.concat(monthly_frames, ignore_index=True)
    trend_df = pd.DataFrame(trend_rows)
    monthly_df.to_csv(ARTIFACT_DIR / "monthly_reputation_trends.csv", index=False)
    trend_df.to_csv(ARTIFACT_DIR / "product_reputation_trend_summary.csv", index=False)
    return monthly_df, trend_df, {
        "method": "monthly official review aggregation by star rating, review volume, and low-rating share",
        "trend_rows": trend_df.to_dict(orient="records"),
    }


def descriptor_presence(text: pd.Series, words: list[str]) -> pd.Series:
    pattern = "|".join(words)
    return text.str.contains(pattern, regex=True, na=False)


def build_text_rating_relationships(frames: dict[str, pd.DataFrame]) -> tuple[pd.DataFrame, dict[str, Any]]:
    rows = []
    for filename, df in frames.items():
        base_rating = float(df["star_rating"].mean())
        for descriptor, words in DESCRIPTORS.items():
            mask = descriptor_presence(df["review_text"], words)
            rows.append(
                {
                    "product_file": filename,
                    "descriptor": descriptor,
                    "matching_reviews": int(mask.sum()),
                    "match_share": clean_float(float(mask.mean()), 4),
                    "mean_rating_when_present": clean_float(float(df.loc[mask, "star_rating"].mean()) if mask.any() else 0.0, 4),
                    "mean_rating_lift": clean_float((float(df.loc[mask, "star_rating"].mean()) if mask.any() else base_rating) - base_rating, 4),
                    "mean_helpfulness_when_present": clean_float(float(df.loc[mask, "helpfulness_rate"].mean()) if mask.any() else 0.0, 4),
                }
            )
    descriptor_df = pd.DataFrame(rows).sort_values(["product_file", "mean_rating_lift"], ascending=[True, False])
    descriptor_df.to_csv(ARTIFACT_DIR / "text_descriptor_rating_lift.csv", index=False)
    return descriptor_df, {
        "method": "descriptor lift: compare rating and helpfulness for reviews containing quality words against product baseline",
        "descriptor_rows": descriptor_df.to_dict(orient="records"),
    }


def build_success_failure_signals(product_df: pd.DataFrame, trend_df: pd.DataFrame, descriptor_df: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, Any]]:
    rows = []
    trend_by_product = {row["product_file"]: row for row in trend_df.to_dict(orient="records")}
    for row in product_df.to_dict(orient="records"):
        filename = row["product_file"]
        descriptors = descriptor_df[descriptor_df["product_file"] == filename]
        enthusiasm = float(descriptors.loc[descriptors["descriptor"] == "enthusiastic", "match_share"].iloc[0])
        disappointment = float(descriptors.loc[descriptors["descriptor"] == "disappointed", "match_share"].iloc[0])
        trend = trend_by_product[filename]
        success_score = (
            0.42 * float(row["mean_star_rating"]) / 5.0
            + 0.18 * (1.0 - float(row["share_low_rating_1_2"]))
            + 0.14 * float(row["mean_helpfulness_rate"])
            + 0.14 * enthusiasm
            - 0.16 * disappointment
            + 0.08 * max(0.0, float(trend["monthly_rating_slope"]) * 20.0)
        )
        rows.append(
            {
                "product_file": filename,
                "success_signal_score": clean_float(success_score, 4),
                "reputation_direction": trend["reputation_direction"],
                "most_confident_tracking_signal": "low-rating share plus disappointed descriptor lift",
            }
        )
    signal_df = pd.DataFrame(rows).sort_values("success_signal_score", ascending=False)
    signal_df.to_csv(ARTIFACT_DIR / "success_failure_signals.csv", index=False)
    return signal_df, {
        "method": "combine ratings, helpfulness, review text descriptors, and time trend into an interpretable product signal",
        "product_signal_rows": signal_df.to_dict(orient="records"),
    }


def build_incitement_analysis(frames: dict[str, pd.DataFrame]) -> dict[str, Any]:
    rows = []
    for filename, df in frames.items():
        dated = df.dropna(subset=["review_date"]).sort_values("review_date").copy()
        dated["previous_20_mean_rating"] = dated["star_rating"].rolling(20, min_periods=5).mean().shift(1)
        low_context = dated["previous_20_mean_rating"] <= 3.0
        high_context = dated["previous_20_mean_rating"] >= 4.2
        rows.append(
            {
                "product_file": filename,
                "reviews_after_low_context": int(low_context.sum()),
                "mean_review_length_after_low_context": clean_float(float(dated.loc[low_context, "review_length_words"].mean()) if low_context.any() else 0.0, 4),
                "reviews_after_high_context": int(high_context.sum()),
                "mean_review_length_after_high_context": clean_float(float(dated.loc[high_context, "review_length_words"].mean()) if high_context.any() else 0.0, 4),
            }
        )
    df = pd.DataFrame(rows)
    df.to_csv(ARTIFACT_DIR / "star_rating_incitement.csv", index=False)
    return {
        "method": "rolling previous-20-review context checks whether low-star periods are followed by longer review writing",
        "incitement_rows": df.to_dict(orient="records"),
    }


def write_frontier(product_df: pd.DataFrame, trend_df: pd.DataFrame, signal_df: pd.DataFrame) -> None:
    plot_df = product_df.merge(signal_df, on="product_file").merge(trend_df[["product_file", "monthly_rating_slope"]], on="product_file")
    fig, ax = plt.subplots(figsize=(8.0, 5.0))
    ax.scatter(plot_df["mean_star_rating"], plot_df["success_signal_score"], s=plot_df["review_count"] / 80.0, color="#4b7298")
    for _, row in plot_df.iterrows():
        ax.annotate(str(row["product_file"]).replace(".tsv", ""), (row["mean_star_rating"], row["success_signal_score"]), xytext=(6, 6), textcoords="offset points")
    ax.set_xlabel("Mean star rating")
    ax.set_ylabel("Success signal score")
    ax.set_title("Official Amazon Review Product Reputation Frontier")
    ax.grid(alpha=0.22)
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "product_reputation_frontier.png", dpi=180)
    plt.close(fig)


def build_result(
    frames: dict[str, pd.DataFrame],
    rating_review_measures: dict[str, Any],
    reputation_time_patterns: dict[str, Any],
    text_rating_relationships: dict[str, Any],
    success_failure_signals: dict[str, Any],
    incitement_analysis: dict[str, Any],
) -> dict[str, Any]:
    return {
        "problem_id": "2020-C",
        "title": "A Wealth of Data",
        "data_source": {
            "type": "official_comap_tsv_zip",
            "root": str(ARCHIVE_ROOT / "official_assets"),
            "source_pdf": str(PDF_PATH),
            "source_zip": str(ZIP_PATH),
            "rows": {filename: int(len(df)) for filename, df in frames.items()},
            "columns": list(next(iter(frames.values())).columns),
            "official_requirement": "THE DATA FILES PROVIDED CONTAIN THE ONLY DATA YOU SHOULD USE FOR THIS PROBLEM.",
        },
        "rating_review_measures": rating_review_measures,
        "reputation_time_patterns": reputation_time_patterns,
        "text_rating_relationships": text_rating_relationships,
        "success_failure_signals": success_failure_signals,
        "star_rating_incitement": incitement_analysis,
        "marketing_director_letter": (
            "Letter to the Marketing Director of Sunshine Company: track low-star share, helpfulness-weighted review length, and disappointed/enthusiastic descriptor lift from launch week onward. "
            "The official Amazon review files show that the most useful early warning is not the mean rating alone; it is the combination of rating trend, low-rating share, and negative descriptors that other customers find helpful. "
            "Sunshine should compare microwave, pacifier, and hair dryer launches against these baselines and investigate product design features whenever low-rating share and broken/disappointed language rise together."
        ),
        "assumption_audit": {
            "truthfulness_note": "This workflow reads the official COMAP TSV files from the official ZIP and does not use random placeholder data.",
            "model_limits": [
                "The analysis is descriptive and does not infer causal product design effects.",
                "Review text descriptors are transparent keyword groups and should be upgraded to a validated NLP model in a full paper.",
                "The official files cover competing products and historical review periods, not Sunshine Company launch outcomes.",
            ],
        },
    }


def build_report(result: dict[str, Any]) -> None:
    lines = [
        "# 2020 MCM-C A Wealth of Data",
        "",
        "## Data Source",
        f"- Official PDF asset: `{result['data_source']['source_pdf']}`.",
        f"- Official ZIP asset: `{result['data_source']['source_zip']}`.",
        f"- Rows: {result['data_source']['rows']}.",
        "",
        "## Recommendation",
        result["marketing_director_letter"],
        "",
        "## Output Files",
        "- `product_review_measures.csv`: rating, helpfulness, and review-length measures.",
        "- `monthly_reputation_trends.csv`: monthly reputation time patterns.",
        "- `text_descriptor_rating_lift.csv`: descriptor and rating association.",
        "- `success_failure_signals.csv`: product success/failure signal scores.",
        "- `product_reputation_frontier.png`: product reputation frontier.",
    ]
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ensure_assets_exist()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    frames = read_official_tsvs()
    product_df, rating_review_measures = build_rating_review_measures(frames)
    _, trend_df, reputation_time_patterns = build_reputation_time_patterns(frames)
    descriptor_df, text_rating_relationships = build_text_rating_relationships(frames)
    signal_df, success_failure_signals = build_success_failure_signals(product_df, trend_df, descriptor_df)
    incitement_analysis = build_incitement_analysis(frames)
    write_frontier(product_df, trend_df, signal_df)
    result = build_result(frames, rating_review_measures, reputation_time_patterns, text_rating_relationships, success_failure_signals, incitement_analysis)
    result["artifacts"] = {
        "product_review_measures": str(ARTIFACT_DIR / "product_review_measures.csv"),
        "monthly_reputation_trends": str(ARTIFACT_DIR / "monthly_reputation_trends.csv"),
        "text_descriptor_rating_lift": str(ARTIFACT_DIR / "text_descriptor_rating_lift.csv"),
        "success_failure_signals": str(ARTIFACT_DIR / "success_failure_signals.csv"),
        "star_rating_incitement": str(ARTIFACT_DIR / "star_rating_incitement.csv"),
        "product_reputation_frontier": str(ARTIFACT_DIR / "product_reputation_frontier.png"),
    }
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    build_report(result)
    print(json.dumps({"result": str(RESULT_PATH), "report": str(REPORT_PATH), "artifacts": str(ARTIFACT_DIR)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
