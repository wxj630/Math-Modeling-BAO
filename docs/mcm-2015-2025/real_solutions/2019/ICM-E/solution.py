from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import pandas as pd


ARCHIVE_ROOT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
PDF_PATH = ARCHIVE_ROOT / "official_assets" / "2019" / "What is the Cost of Environmental Degradation-"
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"

ECOSYSTEM_SERVICES = [
    {"service": "water filtration", "annual_value_usd_ha": 1350, "degradation_sensitivity": 0.74, "recovery_years": 18},
    {"service": "pollination and food production support", "annual_value_usd_ha": 980, "degradation_sensitivity": 0.62, "recovery_years": 12},
    {"service": "carbon sequestration and oxygen cycling", "annual_value_usd_ha": 720, "degradation_sensitivity": 0.58, "recovery_years": 25},
    {"service": "waste assimilation", "annual_value_usd_ha": 1120, "degradation_sensitivity": 0.81, "recovery_years": 20},
    {"service": "biodiversity and habitat support", "annual_value_usd_ha": 860, "degradation_sensitivity": 0.88, "recovery_years": 30},
]

LAND_USE_PROJECTS = [
    {"project": "small community road and sewer extension", "scale": "community", "area_ha": 14, "private_benefit_musd": 7.5, "direct_cost_musd": 4.6, "disturbance_index": 0.22, "mitigation_share": 0.35},
    {"project": "new suburban housing district", "scale": "regional", "area_ha": 95, "private_benefit_musd": 84.0, "direct_cost_musd": 55.0, "disturbance_index": 0.46, "mitigation_share": 0.42},
    {"project": "corporate headquarters relocation", "scale": "regional", "area_ha": 180, "private_benefit_musd": 230.0, "direct_cost_musd": 155.0, "disturbance_index": 0.38, "mitigation_share": 0.50},
    {"project": "cross-country pipeline corridor", "scale": "national", "area_ha": 1250, "private_benefit_musd": 1400.0, "direct_cost_musd": 910.0, "disturbance_index": 0.57, "mitigation_share": 0.48},
    {"project": "expanded commercial waterway", "scale": "national", "area_ha": 820, "private_benefit_musd": 960.0, "direct_cost_musd": 640.0, "disturbance_index": 0.64, "mitigation_share": 0.40},
]

DISCOUNT_RATE = 0.03
EVALUATION_YEARS = 30


def clean_float(value: float, digits: int = 6) -> float:
    return round(float(value), digits)


def ensure_pdf_exists() -> None:
    if not PDF_PATH.exists():
        raise FileNotFoundError(f"Official problem PDF not found: {PDF_PATH}")


def annuity_factor(rate: float, years: int) -> float:
    return (1.0 - (1.0 + rate) ** (-years)) / rate


def build_valuation_model() -> tuple[pd.DataFrame, dict[str, Any]]:
    rows = []
    for service in ECOSYSTEM_SERVICES:
        present_value = float(service["annual_value_usd_ha"]) * annuity_factor(DISCOUNT_RATE, EVALUATION_YEARS)
        rows.append(
            {
                **service,
                "present_value_usd_ha_30yr": clean_float(present_value, 2),
                "accounting_role": "include as avoided loss, mitigation target, or restoration liability in project cost-benefit analysis",
            }
        )
    df = pd.DataFrame(rows)
    df.to_csv(ARTIFACT_DIR / "ecosystem_service_values.csv", index=False)
    return df, {
        "service_rows": df.to_dict(orient="records"),
        "valuation_rule": "environmental cost equals area disturbed times discounted service value times degradation sensitivity after mitigation",
        "discount_rate": DISCOUNT_RATE,
        "evaluation_years": EVALUATION_YEARS,
    }


def build_project_cost_benefit(service_df: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, Any]]:
    service_value = float((service_df["present_value_usd_ha_30yr"] * service_df["degradation_sensitivity"]).sum())
    rows = []
    for project in LAND_USE_PROJECTS:
        gross_service_loss_musd = float(project["area_ha"]) * float(project["disturbance_index"]) * service_value / 1_000_000.0
        residual_loss_musd = gross_service_loss_musd * (1.0 - float(project["mitigation_share"]))
        traditional_npv = float(project["private_benefit_musd"]) - float(project["direct_cost_musd"])
        true_npv = traditional_npv - residual_loss_musd
        rows.append(
            {
                **project,
                "ecosystem_service_loss_musd": clean_float(residual_loss_musd, 3),
                "traditional_npv_musd": clean_float(traditional_npv, 3),
                "true_npv_after_services_musd": clean_float(true_npv, 3),
                "cost_benefit_ratio_after_services": clean_float(float(project["private_benefit_musd"]) / max(float(project["direct_cost_musd"]) + residual_loss_musd, 1e-9), 4),
                "decision": "approve with service accounting" if true_npv > 0 else "redesign, mitigate, or reject under full-cost accounting",
            }
        )
    df = pd.DataFrame(rows).sort_values("true_npv_after_services_musd", ascending=False)
    df.to_csv(ARTIFACT_DIR / "project_true_costs.csv", index=False)
    return df, {
        "project_rows": df.to_dict(orient="records"),
        "projects_reversed_by_ecosystem_accounting": int((df["traditional_npv_musd"].gt(0) & df["true_npv_after_services_musd"].lt(0)).sum()),
    }


def build_model_effectiveness(project_df: pd.DataFrame) -> dict[str, Any]:
    changed = int((project_df["decision"] != "approve with service accounting").sum())
    return {
        "effectiveness_summary": "The model is most effective as a screening and redesign tool because it exposes costs that are invisible in a traditional direct-cost ledger.",
        "projects_flagged_for_redesign": changed,
        "strengths": [
            "uses transparent service categories named in the official problem statement",
            "works across community, regional, and national land-use scales",
            "separates direct cost, private benefit, mitigation, and residual ecological liability",
        ],
        "weaknesses": [
            "service values vary by local ecosystem and should be calibrated with field or satellite data",
            "discount rate and recovery time assumptions can change the ranking",
            "non-market cultural and biodiversity values remain partly qualitative",
        ],
    }


def build_planner_implications() -> dict[str, Any]:
    return {
        "implications": [
            "project managers should budget mitigation and restoration as core capital costs",
            "small projects can be approved quickly when cumulative service loss stays below local thresholds",
            "large linear infrastructure needs corridor alternatives and offsets before permitting",
            "benefit-cost ratios should be reported both before and after ecosystem-service accounting",
            "regional planners need cumulative impact ledgers because individually small projects can combine into significant degradation",
        ]
    }


def build_time_update_model() -> dict[str, Any]:
    return {
        "update_interval_years": 3,
        "change_triggers": [
            "new satellite land-cover baseline",
            "observed water quality or air quality deterioration",
            "species or habitat threshold crossed",
            "carbon price or restoration cost changes",
        ],
        "time_rule": "update service values, degradation sensitivities, and recovery periods whenever monitoring changes the expected residual loss by more than 10 percent",
    }


def write_frontier(project_df: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(9.0, 5.0))
    x = range(len(project_df))
    ax.bar([i - 0.18 for i in x], project_df["traditional_npv_musd"], width=0.36, label="traditional NPV")
    ax.bar([i + 0.18 for i in x], project_df["true_npv_after_services_musd"], width=0.36, label="after services")
    ax.set_xticks(list(x))
    ax.set_xticklabels(project_df["project"], rotation=25, ha="right")
    ax.set_ylabel("NPV (million USD)")
    ax.set_title("Environmental Degradation Cost Accounting")
    ax.axhline(0, color="#444444", linewidth=0.8)
    ax.grid(axis="y", alpha=0.22)
    ax.legend()
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "environmental_cost_frontier.png", dpi=180)
    plt.close(fig)


def build_result(
    valuation_model: dict[str, Any],
    project_cost_benefit: dict[str, Any],
    model_effectiveness: dict[str, Any],
    planner_implications: dict[str, Any],
    time_update_model: dict[str, Any],
) -> dict[str, Any]:
    return {
        "problem_id": "2019-E",
        "title": "What is the Cost of Environmental Degradation?",
        "data_source": {
            "type": "official_statement_parameters",
            "root": str(ARCHIVE_ROOT / "official_assets"),
            "source_pdf": str(PDF_PATH),
            "official_requirements": {
                "ecosystem_service_valuation": True,
                "land_use_cost_benefit": True,
                "varying_project_sizes": True,
                "model_effectiveness": True,
                "planner_manager_implications": True,
                "model_changes_over_time": True,
            },
            "parameters": {
                "ecosystem_services": ECOSYSTEM_SERVICES,
                "land_use_projects": LAND_USE_PROJECTS,
                "discount_rate": DISCOUNT_RATE,
                "evaluation_years": EVALUATION_YEARS,
                "source_note": "Official PDF statement categories only; monetary values, sensitivities, and project rows are explicit deterministic modeling inputs for audit and replacement.",
            },
        },
        "valuation_model": valuation_model,
        "project_cost_benefit": project_cost_benefit,
        "model_effectiveness": model_effectiveness,
        "planner_implications": planner_implications,
        "time_update_model": time_update_model,
        "assumption_audit": {
            "truthfulness_note": "This workflow uses official statement parameters and transparent deterministic valuation scenarios; it does not use random placeholder data.",
            "model_limits": [
                "COMAP did not provide a land-cover table, project cost ledger, or local ecosystem measurements.",
                "Dollar values are transparent planning inputs inspired by the service categories named in the statement, not observed project accounts.",
                "A full paper should replace them with local data.gov ecosystem data, satellite land cover, restoration bids, and monitoring records.",
            ],
        },
    }


def build_report(result: dict[str, Any]) -> None:
    lines = [
        "# 2019 ICM-E What is the Cost of Environmental Degradation?",
        "",
        "## Data Source",
        f"- Official PDF asset: `{result['data_source']['source_pdf']}`.",
        "- No numeric COMAP attachment is supplied; this workflow uses official statement categories and explicit deterministic valuation inputs.",
        "",
        "## Model Summary",
        f"- Ecosystem services valued: {len(result['valuation_model']['service_rows'])}.",
        f"- Project rows: {len(result['project_cost_benefit']['project_rows'])}.",
        f"- Projects flagged for redesign: {result['model_effectiveness']['projects_flagged_for_redesign']}.",
        "",
        "## Planner Implications",
        *[f"- {item}" for item in result["planner_implications"]["implications"]],
        "",
        "## Output Files",
        "- `ecosystem_service_values.csv`",
        "- `project_true_costs.csv`",
        "- `environmental_cost_frontier.png`",
    ]
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ensure_pdf_exists()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    service_df, valuation_model = build_valuation_model()
    project_df, project_cost_benefit = build_project_cost_benefit(service_df)
    model_effectiveness = build_model_effectiveness(project_df)
    planner_implications = build_planner_implications()
    time_update_model = build_time_update_model()
    write_frontier(project_df)
    result = build_result(valuation_model, project_cost_benefit, model_effectiveness, planner_implications, time_update_model)
    result["artifacts"] = {
        "service_values": str(ARTIFACT_DIR / "ecosystem_service_values.csv"),
        "project_true_costs": str(ARTIFACT_DIR / "project_true_costs.csv"),
        "frontier": str(ARTIFACT_DIR / "environmental_cost_frontier.png"),
    }
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    build_report(result)
    print(json.dumps({"result": str(RESULT_PATH), "report": str(REPORT_PATH), "artifacts": str(ARTIFACT_DIR)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
