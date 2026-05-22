"""2016 MCM-C Goodgrant Challenge real-data workflow.

Uses only the official COMAP ProblemCDATA.zip workbooks. The ROI score is a
transparent charitable-return index built from Scorecard/IPEDS fields, not a
claim of causal impact and not random synthetic data.
"""

from __future__ import annotations

import json
import math
import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/private/tmp/matplotlib-cache")
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd


REPO_ROOT = Path(__file__).resolve().parents[5]
ARCHIVE_ROOT = REPO_ROOT / "docs" / "mcm-2015-2025"
DATA_ROOT = ARCHIVE_ROOT / "official_assets_extracted" / "2016" / "Problem Data- The Goodgrant Challenge"
PDF_PATH = ARCHIVE_ROOT / "official_assets_extracted" / "2016" / "The Goodgrant Challenge.pdf"
SCORECARD_PATH = DATA_ROOT / "Problem C - Most Recent Cohorts Data (Scorecard Elements).xlsx"
CANDIDATE_UID_PATH = DATA_ROOT / "Problem C - IPEDS UID for Potential Candidate Schools.xlsx"
DICTIONARY_PATH = DATA_ROOT / "Problem C - CollegeScorecardDataDictionary-09-08-2015.xlsx"
IPEDS_VARIABLES_PDF = DATA_ROOT / "IPEDS Variables for Data Selection.pdf"
OUT_ROOT = ARCHIVE_ROOT / "real_solutions" / "2016" / "MCM-C"
ARTIFACT_DIR = OUT_ROOT / "artifacts"

ANNUAL_BUDGET_USD = 100_000_000
YEARS = 5
MIN_RECOMMENDED_GRANT_USD = 2_000_000
MAX_RECOMMENDED_GRANT_USD = 10_000_000


def require_assets() -> None:
    missing = [str(path) for path in [PDF_PATH, SCORECARD_PATH, CANDIDATE_UID_PATH, DICTIONARY_PATH, IPEDS_VARIABLES_PDF] if not path.exists()]
    if missing:
        raise FileNotFoundError("missing official COMAP Goodgrant assets: " + ", ".join(missing))


def numeric(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series.replace({"PrivacySuppressed": pd.NA, "NULL": pd.NA, "nan": pd.NA}), errors="coerce")


def minmax(series: pd.Series, invert: bool = False) -> pd.Series:
    values = numeric(series)
    lo = values.quantile(0.05)
    hi = values.quantile(0.95)
    clipped = values.clip(lo, hi)
    scaled = (clipped - lo) / (hi - lo) if hi != lo else clipped * 0
    if invert:
        scaled = 1 - scaled
    return scaled.fillna(scaled.median()).clip(0, 1)


def clean_and_score(scorecard: pd.DataFrame, candidate_uids: pd.DataFrame) -> pd.DataFrame:
    candidate_ids = set(candidate_uids["UNITID"].astype(int))
    df = scorecard[scorecard["UNITID"].astype(int).isin(candidate_ids)].copy()
    df = df[(df["CURROPER"] == 1) & (df["PREDDEG"].isin([3, 4])) & (numeric(df["UGDS"]) > 500)].copy()
    df["completion_rate"] = numeric(df["C150_4_POOLED_SUPP"]).fillna(numeric(df["C200_L4_POOLED_SUPP"]))
    df["retention_rate"] = numeric(df["RET_FT4"]).fillna(numeric(df["RET_FTL4"]))
    df["earnings_10yr"] = numeric(df["md_earn_wne_p10"])
    df["repayment_rate"] = numeric(df["RPY_3YR_RT_SUPP"])
    df["pell_share"] = numeric(df["PCTPELL"])
    df["loan_share"] = numeric(df["PCTFLOAN"])
    df["undergrad_size"] = numeric(df["UGDS"])
    df["net_price"] = numeric(df["NPT4_PUB"]).fillna(numeric(df["NPT4_PRIV"]))
    df["grant_need_index"] = minmax(df["pell_share"]) * 0.65 + minmax(df["net_price"], invert=True) * 0.20 + minmax(df["undergrad_size"]) * 0.15
    df["student_success_index"] = minmax(df["completion_rate"]) * 0.40 + minmax(df["retention_rate"]) * 0.25 + minmax(df["repayment_rate"]) * 0.20 + minmax(df["earnings_10yr"]) * 0.15
    df["leverage_index"] = minmax(df["pell_share"]) * 0.30 + minmax(df["loan_share"], invert=True) * 0.20 + minmax(df["undergrad_size"]) * 0.30 + minmax(df["net_price"], invert=True) * 0.20
    df["roi_score"] = 100 * (0.45 * df["student_success_index"] + 0.35 * df["grant_need_index"] + 0.20 * df["leverage_index"])
    df["recommended_annual_grant_usd"] = (
        MIN_RECOMMENDED_GRANT_USD + (MAX_RECOMMENDED_GRANT_USD - MIN_RECOMMENDED_GRANT_USD) * minmax(df["undergrad_size"])
    ).round(-5)
    df["expected_students_reached"] = (df["undergrad_size"] * df["pell_share"].fillna(df["pell_share"].median())).round(0)
    df["charitable_roi_units_per_million"] = (df["roi_score"] * df["expected_students_reached"] / (df["recommended_annual_grant_usd"] / 1_000_000)).round(6)
    df["rank_score"] = (0.70 * df["roi_score"] + 0.30 * minmax(df["charitable_roi_units_per_million"]) * 100).round(6)
    keep = [
        "UNITID", "INSTNM", "CITY", "STABBR", "CONTROL", "PREDDEG", "UGDS", "PCTPELL", "PCTFLOAN",
        "completion_rate", "retention_rate", "repayment_rate", "earnings_10yr", "net_price", "grant_need_index",
        "student_success_index", "leverage_index", "roi_score", "recommended_annual_grant_usd", "expected_students_reached",
        "charitable_roi_units_per_million", "rank_score",
    ]
    return df[keep].sort_values(["rank_score", "roi_score"], ascending=False).reset_index(drop=True)


def build_funding_plan(ranked: pd.DataFrame) -> pd.DataFrame:
    selected = []
    remaining = ANNUAL_BUDGET_USD
    for _, row in ranked.iterrows():
        grant = float(row["recommended_annual_grant_usd"])
        if grant <= remaining and len(selected) < 25:
            selected_row = row.to_dict()
            selected_row["annual_grant_usd"] = grant
            selected_row["five_year_grant_usd"] = grant * YEARS
            selected.append(selected_row)
            remaining -= grant
        if remaining < MIN_RECOMMENDED_GRANT_USD:
            break
    plan = pd.DataFrame(selected)
    if not plan.empty:
        plan["portfolio_share"] = plan["annual_grant_usd"] / ANNUAL_BUDGET_USD
    return plan


def robustness(ranked: pd.DataFrame) -> tuple[dict[str, object], pd.DataFrame]:
    scenarios = [
        {"scenario": "base", "success_w": 0.45, "need_w": 0.35, "leverage_w": 0.20},
        {"scenario": "need_priority", "success_w": 0.30, "need_w": 0.50, "leverage_w": 0.20},
        {"scenario": "outcome_priority", "success_w": 0.60, "need_w": 0.25, "leverage_w": 0.15},
        {"scenario": "scale_priority", "success_w": 0.35, "need_w": 0.25, "leverage_w": 0.40},
    ]
    rows = []
    for scenario in scenarios:
        temp = ranked.copy()
        temp["scenario_score"] = 100 * (
            scenario["success_w"] * temp["student_success_index"]
            + scenario["need_w"] * temp["grant_need_index"]
            + scenario["leverage_w"] * temp["leverage_index"]
        )
        top = temp.sort_values("scenario_score", ascending=False).head(20)
        rows.append(
            {
                "scenario": scenario["scenario"],
                "success_w": scenario["success_w"],
                "need_w": scenario["need_w"],
                "leverage_w": scenario["leverage_w"],
                "top20_unitids": ";".join(str(int(value)) for value in top["UNITID"]),
                "top20_overlap_with_base": int(len(set(top["UNITID"]).intersection(set(ranked.head(20)["UNITID"])))),
                "top_school": str(top.iloc[0]["INSTNM"]),
            }
        )
    return {"weight_scenarios": rows}, pd.DataFrame(rows)


def make_plot(plan: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(10, 6))
    top = plan.head(12).copy().sort_values("rank_score")
    ax.barh(top["INSTNM"], top["rank_score"], color="#386641")
    ax.set_xlabel("Goodgrant rank score")
    ax.set_title("2016 MCM-C Goodgrant top recommended schools")
    ax.grid(axis="x", alpha=0.25)
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "goodgrant_top_schools.png", dpi=180)
    plt.close(fig)


def build_report(result: dict) -> str:
    lines = [
        "# 2016 MCM-C The Goodgrant Challenge：官方 Scorecard/IPEDS 实验报告",
        "",
        "## 数据来源",
        f"- 官方题面：`{PDF_PATH}`。",
        f"- 官方附件目录：`{DATA_ROOT}`。",
        f"- Scorecard 行数：{result['data_source']['rows']['scorecard']}。",
        f"- 候选 UID 行数：{result['data_source']['rows']['candidate_uids']}。",
        "- 本实验不使用随机生成的 x1/x2/x3；ROI 是透明 charitable-return 指数，不声明因果。",
        "",
        "## ROI 定义",
        result["roi_model"]["definition"],
        "",
        "## 推荐资助组合",
        f"- 年预算：{result['funding_strategy']['annual_budget_usd']} USD，持续 {result['funding_strategy']['years']} 年。",
        f"- 推荐学校数：{len(result['funding_strategy']['recommended_schools'])}。",
        "| rank | school | state | annual grant | roi score | students reached |",
        "|---:|---|---|---:|---:|---:|",
    ]
    for i, row in enumerate(result["funding_strategy"]["recommended_schools"][:15], start=1):
        lines.append(f"| {i} | {row['INSTNM']} | {row['STABBR']} | {row['annual_grant_usd']} | {row['roi_score']} | {row['expected_students_reached']} |")
    lines.extend(["", "## 稳健性", "| scenario | top school | top20 overlap |", "|---|---|---:|"])
    for row in result["robustness"]["weight_scenarios"]:
        lines.append(f"| {row['scenario']} | {row['top_school']} | {row['top20_overlap_with_base']} |")
    lines.extend(["", "## CFO letter", result["cfo_letter"], ""])
    return "\n".join(lines)


def main() -> None:
    require_assets()
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    scorecard = pd.read_excel(SCORECARD_PATH)
    candidate_uids = pd.read_excel(CANDIDATE_UID_PATH)
    dictionary = pd.read_excel(DICTIONARY_PATH)
    ranked = clean_and_score(scorecard, candidate_uids)
    plan = build_funding_plan(ranked)
    robust, robust_df = robustness(ranked)
    ranked.to_csv(ARTIFACT_DIR / "goodgrant_ranked_candidates.csv", index=False)
    plan.to_csv(ARTIFACT_DIR / "goodgrant_funding_plan.csv", index=False)
    robust_df.to_csv(ARTIFACT_DIR / "roi_weight_sensitivity.csv", index=False)
    make_plot(plan)
    recommended = plan.head(25).round(6).to_dict(orient="records")
    result = {
        "data_source": {
            "type": "official_comap_xlsx_zip",
            "root": str(DATA_ROOT),
            "source_pdf": str(PDF_PATH),
            "scorecard_workbook": str(SCORECARD_PATH),
            "candidate_uid_workbook": str(CANDIDATE_UID_PATH),
            "dictionary_workbook": str(DICTIONARY_PATH),
            "ipeds_variables_pdf": str(IPEDS_VARIABLES_PDF),
            "rows": {"scorecard": int(len(scorecard)), "candidate_uids": int(len(candidate_uids)), "dictionary": int(len(dictionary))},
        },
        "roi_model": {
            "definition": "Charitable ROI = weighted student-success potential, demonstrated need, and scalable leverage per grant dollar. It is appropriate for philanthropy because it values Pell-serving institutions, completion/retention/repayment/earnings outcomes, and students reached rather than private profit.",
            "candidate_rows_after_filters": int(len(ranked)),
            "candidate_rows_scored": int(ranked["rank_score"].notna().sum()),
            "weights": {"student_success_index": 0.45, "grant_need_index": 0.35, "leverage_index": 0.20, "portfolio_rank_blend": "70% ROI score + 30% ROI units per million"},
            "filtering": "Official candidate UID list joined to Scorecard, current operating schools, predominant degree 3 or 4, UGDS > 500.",
        },
        "funding_strategy": {
            "annual_budget_usd": ANNUAL_BUDGET_USD,
            "years": YEARS,
            "total_five_year_budget_usd": ANNUAL_BUDGET_USD * YEARS,
            "recommended_school_count": int(len(plan)),
            "recommended_schools": recommended,
        },
        "robustness": robust,
        "cfo_letter": (
            "Dear Mr. Alpha Chiang: We recommend that the Goodgrant Foundation invest the annual $100 million in a ranked portfolio of "
            "candidate institutions selected from the official IPEDS UID list and College Scorecard outcomes. Our ROI is not financial profit; it is "
            "a charitable return index combining student success, service to high-need students, and scale per grant dollar. The attached plan funds "
            "multiple institutions for five years, avoids duplicating purely prestige-driven giving, and should be re-estimated annually as new Scorecard "
            "and IPEDS data arrive."
        ),
    }
    (OUT_ROOT / "result.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    (OUT_ROOT / "report.md").write_text(build_report(result), encoding="utf-8")
    print(json.dumps({"result": str(OUT_ROOT / "result.json"), "artifacts": str(ARTIFACT_DIR)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
