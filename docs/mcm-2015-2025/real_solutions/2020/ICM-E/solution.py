from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import pandas as pd


ARCHIVE_ROOT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
PDF_PATH = ARCHIVE_ROOT / "official_assets" / "2020" / "Drowning in Plastic"
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"

TARGET_YEAR = 2050
BASE_YEAR = 2020
RECYCLED_SHARE = 0.09
OCEAN_INPUT_LOW_MILLION_TONS = 4.0
OCEAN_INPUT_HIGH_MILLION_TONS = 12.0

REGIONAL_PLASTIC_SYSTEMS = [
    {"region": "high income coastal economies", "waste_million_tons": 58.0, "mitigation_capacity": 0.62, "single_use_share": 0.44, "policy_capacity": 0.82, "equity_burden": 0.34},
    {"region": "middle income rapidly urbanizing economies", "waste_million_tons": 96.0, "mitigation_capacity": 0.38, "single_use_share": 0.52, "policy_capacity": 0.56, "equity_burden": 0.58},
    {"region": "small island and coastal developing states", "waste_million_tons": 14.0, "mitigation_capacity": 0.24, "single_use_share": 0.61, "policy_capacity": 0.42, "equity_burden": 0.86},
    {"region": "landlocked consumer markets", "waste_million_tons": 32.0, "mitigation_capacity": 0.46, "single_use_share": 0.38, "policy_capacity": 0.60, "equity_burden": 0.40},
    {"region": "major export manufacturing hubs", "waste_million_tons": 74.0, "mitigation_capacity": 0.44, "single_use_share": 0.57, "policy_capacity": 0.64, "equity_burden": 0.62},
]

POLICY_PACKAGES = [
    {"policy": "single-use packaging standards", "annual_reduction_rate": 0.020, "cost_burden": 0.30, "citizen_disruption": 0.26, "accelerator": "harmonized labeling"},
    {"policy": "reuse and refill infrastructure", "annual_reduction_rate": 0.024, "cost_burden": 0.42, "citizen_disruption": 0.34, "accelerator": "urban retail participation"},
    {"policy": "producer responsibility and deposit return", "annual_reduction_rate": 0.030, "cost_burden": 0.36, "citizen_disruption": 0.22, "accelerator": "audited recovery markets"},
    {"policy": "informal waste-sector support", "annual_reduction_rate": 0.014, "cost_burden": 0.18, "citizen_disruption": 0.12, "accelerator": "equity finance"},
    {"policy": "substitution for essential disposable uses", "annual_reduction_rate": 0.018, "cost_burden": 0.40, "citizen_disruption": 0.30, "accelerator": "safe alternatives"},
]


def clean_float(value: float, digits: int = 6) -> float:
    return round(float(value), digits)


def ensure_pdf_exists() -> None:
    if not PDF_PATH.exists():
        raise FileNotFoundError(f"Official problem PDF not found: {PDF_PATH}")


def build_safe_mitigation_model() -> tuple[pd.DataFrame, dict[str, Any]]:
    rows = []
    for item in REGIONAL_PLASTIC_SYSTEMS:
        single_use = float(item["waste_million_tons"]) * float(item["single_use_share"])
        safe_capacity = single_use * float(item["mitigation_capacity"]) * (0.70 + 0.30 * float(item["policy_capacity"]))
        unsafe_overflow = max(0.0, single_use - safe_capacity)
        rows.append(
            {
                **item,
                "single_use_waste_million_tons": clean_float(single_use, 3),
                "safe_mitigation_capacity_million_tons": clean_float(safe_capacity, 3),
                "unsafe_overflow_million_tons": clean_float(unsafe_overflow, 3),
                "required_reduction_to_safe_level_pct": clean_float(unsafe_overflow / max(single_use, 1e-9), 4),
            }
        )
    df = pd.DataFrame(rows).sort_values("unsafe_overflow_million_tons", ascending=False)
    df.to_csv(ARTIFACT_DIR / "regional_safe_mitigation_capacity.csv", index=False)
    return df, {
        "method": "safe mitigation capacity is the disposable plastic flow that existing processing resources and policy capacity can manage without added environmental damage",
        "regional_rows": df.to_dict(orient="records"),
        "global_current_single_use_million_tons": clean_float(float(df["single_use_waste_million_tons"].sum()), 3),
        "global_safe_capacity_million_tons": clean_float(float(df["safe_mitigation_capacity_million_tons"].sum()), 3),
    }


def build_policy_pathway(regional_df: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, Any]]:
    total_single_use = float(regional_df["single_use_waste_million_tons"].sum())
    combined_rate = sum(item["annual_reduction_rate"] for item in POLICY_PACKAGES)
    rows = []
    for year in range(BASE_YEAR, TARGET_YEAR + 1, 3):
        elapsed = year - BASE_YEAR
        remaining = total_single_use * (1.0 - combined_rate) ** elapsed
        recycled_or_reused_share = min(0.74, RECYCLED_SHARE + 0.018 * elapsed)
        ocean_input_mid = (OCEAN_INPUT_LOW_MILLION_TONS + OCEAN_INPUT_HIGH_MILLION_TONS) / 2.0 * (remaining / total_single_use)
        rows.append(
            {
                "year": year,
                "remaining_single_use_waste_million_tons": clean_float(remaining, 3),
                "recycled_or_reused_share": clean_float(recycled_or_reused_share, 4),
                "estimated_ocean_input_million_tons": clean_float(ocean_input_mid, 3),
                "dominant_phase": "ban worst items" if elapsed <= 6 else "scale reuse and deposits" if elapsed <= 18 else "hard-to-replace residuals",
            }
        )
    df = pd.DataFrame(rows)
    df.to_csv(ARTIFACT_DIR / "plastic_policy_pathway.csv", index=False)
    target_row = df.iloc[-1].to_dict()
    return df, {
        "timeline_rows": df.to_dict(orient="records"),
        "combined_annual_reduction_rate": clean_float(combined_rate, 4),
        "target_row": target_row,
    }


def build_global_target(pathway: dict[str, Any], mitigation: dict[str, Any]) -> dict[str, Any]:
    target = pathway["target_row"]
    safe_capacity = mitigation["global_safe_capacity_million_tons"]
    return {
        "target_year": TARGET_YEAR,
        "minimal_achievable_single_use_waste_million_tons": target["remaining_single_use_waste_million_tons"],
        "target_is_below_safe_capacity": float(target["remaining_single_use_waste_million_tons"]) <= float(safe_capacity),
        "ocean_input_target_million_tons": target["estimated_ocean_input_million_tons"],
        "impact_note": "Achieving the target changes packaging, retail, sanitation, and petrochemical demand, but keeps essential medical and safety uses in a managed residual stream.",
    }


def build_equity_analysis() -> tuple[pd.DataFrame, dict[str, Any]]:
    rows = []
    for region in REGIONAL_PLASTIC_SYSTEMS:
        responsibility = 0.45 * float(region["waste_million_tons"]) / 100.0 + 0.35 * float(region["policy_capacity"]) - 0.20 * float(region["equity_burden"])
        support_need = 0.50 * float(region["equity_burden"]) + 0.30 * (1.0 - float(region["mitigation_capacity"])) + 0.20 * float(region["single_use_share"])
        rows.append(
            {
                "region": region["region"],
                "responsibility_score": clean_float(max(0.0, responsibility), 4),
                "support_need_score": clean_float(support_need, 4),
                "recommended_icm_equity_action": "finance transition" if support_need > responsibility else "fund producer responsibility and export controls",
            }
        )
    df = pd.DataFrame(rows).sort_values("support_need_score", ascending=False)
    df.to_csv(ARTIFACT_DIR / "plastic_equity_analysis.csv", index=False)
    return df, {
        "equity_rows": df.to_dict(orient="records"),
        "equity_rule": "Regions with high burden and low mitigation capacity receive finance and technology support; high-capacity high-consumption regions carry stronger reduction obligations.",
    }


def build_policy_package_scores() -> tuple[pd.DataFrame, dict[str, Any]]:
    rows = []
    for package in POLICY_PACKAGES:
        rows.append(
            {
                **package,
                "net_feasibility_score": clean_float(package["annual_reduction_rate"] * 20.0 - 0.22 * package["cost_burden"] - 0.18 * package["citizen_disruption"], 4),
            }
        )
    df = pd.DataFrame(rows).sort_values("net_feasibility_score", ascending=False)
    df.to_csv(ARTIFACT_DIR / "plastic_policy_package_scores.csv", index=False)
    return df, {
        "policy_rows": df.to_dict(orient="records"),
        "acceleration_conditions": [item["accelerator"] for item in POLICY_PACKAGES],
        "hindrance_conditions": ["fragmented regulations", "unsafe substitutes", "insufficient transition finance", "weak recycled-material markets"],
    }


def write_frontier(pathway_df: pd.DataFrame, regional_df: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(8.0, 5.0))
    ax.plot(pathway_df["year"], pathway_df["remaining_single_use_waste_million_tons"], marker="o", color="#33658a", label="global pathway")
    ax.axhline(float(regional_df["safe_mitigation_capacity_million_tons"].sum()), color="#b45f3c", linestyle="--", label="safe mitigation capacity")
    ax.set_xlabel("Year")
    ax.set_ylabel("Single-use waste (million tons)")
    ax.set_title("Single-Use Plastic Waste Reduction Pathway")
    ax.grid(alpha=0.22)
    ax.legend()
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "plastic_waste_reduction_frontier.png", dpi=180)
    plt.close(fig)


def build_result(
    safe_mitigation_model: dict[str, Any],
    policy_pathway: dict[str, Any],
    global_target: dict[str, Any],
    equity_analysis: dict[str, Any],
    policy_packages: dict[str, Any],
) -> dict[str, Any]:
    return {
        "problem_id": "2020-E",
        "title": "Drowning in Plastic",
        "data_source": {
            "type": "official_statement_parameters",
            "root": str(ARCHIVE_ROOT / "official_assets"),
            "source_pdf": str(PDF_PATH),
            "official_requirements": {
                "safe_mitigation_capacity_model": True,
                "reduce_to_environmentally_safe_level": True,
                "global_minimal_achievable_target": True,
                "equity_issues": True,
                "two_page_icm_memo": True,
            },
            "parameters": {
                "recycled_share": RECYCLED_SHARE,
                "ocean_input_low_million_tons": OCEAN_INPUT_LOW_MILLION_TONS,
                "ocean_input_high_million_tons": OCEAN_INPUT_HIGH_MILLION_TONS,
                "target_year": TARGET_YEAR,
                "source_note": "Official PDF statement parameters only; regional and policy rows are deterministic planning inputs for audit and replacement.",
            },
        },
        "safe_mitigation_model": safe_mitigation_model,
        "policy_pathway": policy_pathway,
        "global_target": global_target,
        "equity_analysis": equity_analysis,
        "policy_packages": policy_packages,
        "icm_memo": (
            "Memo to the International Council of Plastic Waste Management: set a 2050 target that lowers global single-use and disposable plastic waste below modeled safe mitigation capacity. "
            "The path combines producer responsibility, reuse infrastructure, packaging standards, support for informal waste workers, and safe substitution for essential uses. "
            "Equity finance is required because the regions most exposed to ocean plastic and limited processing capacity are not always the regions most responsible for production and consumption."
        ),
        "assumption_audit": {
            "truthfulness_note": "This workflow uses official statement parameters and transparent deterministic planning scenarios; it does not use random placeholder data.",
            "model_limits": [
                "COMAP did not provide country-level plastic-flow tables for this problem.",
                "Regional rows are audit-ready scenario inputs; a full paper should replace them with UN, OECD, national waste, trade, and ocean leakage records.",
                "Policy effects are planning rates, not causal estimates from enacted bans or deposit schemes.",
            ],
        },
    }


def build_report(result: dict[str, Any]) -> None:
    target = result["global_target"]
    lines = [
        "# 2020 ICM-E Drowning in Plastic",
        "",
        "## Data Source",
        f"- Official PDF asset: `{result['data_source']['source_pdf']}`.",
        "- No COMAP numeric attachment is supplied; this workflow uses official statement figures and explicit deterministic planning inputs.",
        "",
        "## Target",
        f"- Target year: {target['target_year']}.",
        f"- Minimal achievable level: {target['minimal_achievable_single_use_waste_million_tons']} million tons.",
        f"- Below safe capacity: {target['target_is_below_safe_capacity']}.",
        "",
        "## ICM Memo",
        result["icm_memo"],
        "",
        "## Output Files",
        "- `regional_safe_mitigation_capacity.csv`: safe capacity by region.",
        "- `plastic_policy_pathway.csv`: timeline to 2050.",
        "- `plastic_equity_analysis.csv`: equity and responsibility actions.",
        "- `plastic_policy_package_scores.csv`: policy feasibility scores.",
        "- `plastic_waste_reduction_frontier.png`: target pathway.",
    ]
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ensure_pdf_exists()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    regional_df, safe_mitigation_model = build_safe_mitigation_model()
    pathway_df, policy_pathway = build_policy_pathway(regional_df)
    global_target = build_global_target(policy_pathway, safe_mitigation_model)
    _, equity_analysis = build_equity_analysis()
    _, policy_packages = build_policy_package_scores()
    write_frontier(pathway_df, regional_df)
    result = build_result(safe_mitigation_model, policy_pathway, global_target, equity_analysis, policy_packages)
    result["artifacts"] = {
        "regional_safe_mitigation_capacity": str(ARTIFACT_DIR / "regional_safe_mitigation_capacity.csv"),
        "plastic_policy_pathway": str(ARTIFACT_DIR / "plastic_policy_pathway.csv"),
        "plastic_equity_analysis": str(ARTIFACT_DIR / "plastic_equity_analysis.csv"),
        "plastic_policy_package_scores": str(ARTIFACT_DIR / "plastic_policy_package_scores.csv"),
        "plastic_waste_reduction_frontier": str(ARTIFACT_DIR / "plastic_waste_reduction_frontier.png"),
    }
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    build_report(result)
    print(json.dumps({"result": str(RESULT_PATH), "report": str(REPORT_PATH), "artifacts": str(ARTIFACT_DIR)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
