from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import pandas as pd


ARCHIVE_ROOT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
PDF_PATH = ARCHIVE_ROOT / "official_assets" / "2021" / "Re-Optimizing Food Systems"
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"

TRANSITION_YEARS = 15
GLOBAL_HUNGER_MILLIONS = 821
FOOD_SYSTEM_GHG_SHARE = 0.29
FOOD_SYSTEM_BIODIVERSITY_LOSS_SHARE = 0.80
FOOD_SYSTEM_DEFORESTATION_SHARE = 0.80
FOOD_SYSTEM_FRESHWATER_SHARE = 0.70

FOOD_SYSTEM_PRIORITIES = {
    "current_efficiency_profit": {
        "efficiency": 0.34,
        "profitability": 0.30,
        "sustainability": 0.16,
        "equity": 0.12,
        "nutrition_resilience": 0.08,
    },
    "equity_sustainability_balanced": {
        "efficiency": 0.16,
        "profitability": 0.12,
        "sustainability": 0.30,
        "equity": 0.28,
        "nutrition_resilience": 0.14,
    },
    "regional_resilience": {
        "efficiency": 0.18,
        "profitability": 0.16,
        "sustainability": 0.22,
        "equity": 0.20,
        "nutrition_resilience": 0.24,
    },
    "profit_with_guardrails": {
        "efficiency": 0.26,
        "profitability": 0.24,
        "sustainability": 0.22,
        "equity": 0.18,
        "nutrition_resilience": 0.10,
    },
}

COUNTRY_CASES = [
    {
        "country": "United States",
        "development_group": "developed",
        "efficiency": 0.82,
        "profitability": 0.78,
        "sustainability": 0.42,
        "equity": 0.46,
        "nutrition_resilience": 0.70,
        "governance_capacity": 0.84,
        "local_production_capacity": 0.58,
        "environmental_pressure": 0.76,
        "food_insecurity_rate": 0.11,
    },
    {
        "country": "Germany",
        "development_group": "developed",
        "efficiency": 0.74,
        "profitability": 0.66,
        "sustainability": 0.62,
        "equity": 0.68,
        "nutrition_resilience": 0.78,
        "governance_capacity": 0.86,
        "local_production_capacity": 0.62,
        "environmental_pressure": 0.55,
        "food_insecurity_rate": 0.05,
    },
    {
        "country": "India",
        "development_group": "developing",
        "efficiency": 0.56,
        "profitability": 0.48,
        "sustainability": 0.38,
        "equity": 0.44,
        "nutrition_resilience": 0.54,
        "governance_capacity": 0.58,
        "local_production_capacity": 0.72,
        "environmental_pressure": 0.68,
        "food_insecurity_rate": 0.18,
    },
    {
        "country": "Kenya",
        "development_group": "developing",
        "efficiency": 0.44,
        "profitability": 0.36,
        "sustainability": 0.48,
        "equity": 0.42,
        "nutrition_resilience": 0.46,
        "governance_capacity": 0.52,
        "local_production_capacity": 0.66,
        "environmental_pressure": 0.52,
        "food_insecurity_rate": 0.25,
    },
]

INTERVENTIONS = [
    {
        "intervention": "regional procurement and shorter supply loops",
        "primary_dimension": "efficiency",
        "sustainability_gain": 0.10,
        "equity_gain": 0.07,
        "profitability_cost": 0.04,
        "first_benefit_year": 3,
    },
    {
        "intervention": "regenerative production and water stewardship",
        "primary_dimension": "sustainability",
        "sustainability_gain": 0.18,
        "equity_gain": 0.05,
        "profitability_cost": 0.07,
        "first_benefit_year": 5,
    },
    {
        "intervention": "nutritious access vouchers and school meals",
        "primary_dimension": "nutrition_resilience",
        "sustainability_gain": 0.04,
        "equity_gain": 0.16,
        "profitability_cost": 0.05,
        "first_benefit_year": 2,
    },
    {
        "intervention": "transparent waste reduction and storage upgrades",
        "primary_dimension": "efficiency",
        "sustainability_gain": 0.09,
        "equity_gain": 0.08,
        "profitability_cost": 0.02,
        "first_benefit_year": 2,
    },
    {
        "intervention": "small producer market access and risk sharing",
        "primary_dimension": "equity",
        "sustainability_gain": 0.07,
        "equity_gain": 0.15,
        "profitability_cost": 0.06,
        "first_benefit_year": 4,
    },
]


def clean_float(value: float, digits: int = 6) -> float:
    return round(float(value), digits)


def ensure_pdf_exists() -> None:
    if not PDF_PATH.exists():
        raise FileNotFoundError(f"Official problem PDF not found: {PDF_PATH}")


def score_case(case: dict[str, Any], weights: dict[str, float]) -> float:
    return sum(float(case[dimension]) * weight for dimension, weight in weights.items())


def build_priority_model() -> tuple[pd.DataFrame, dict[str, Any]]:
    rows = []
    for priority_name, weights in FOOD_SYSTEM_PRIORITIES.items():
        case_scores = [score_case(case, weights) for case in COUNTRY_CASES]
        sustainability_weight = weights["sustainability"]
        equity_weight = weights["equity"]
        current_penalty = 0.16 * FOOD_SYSTEM_GHG_SHARE + 0.05 * FOOD_SYSTEM_FRESHWATER_SHARE
        objective_score = sum(case_scores) / len(case_scores) + 0.22 * sustainability_weight + 0.20 * equity_weight - current_penalty
        rows.append(
            {
                "priority": priority_name,
                "mean_country_score": clean_float(sum(case_scores) / len(case_scores), 4),
                "sustainability_weight": sustainability_weight,
                "equity_weight": equity_weight,
                "profitability_weight": weights["profitability"],
                "objective_score": clean_float(objective_score, 4),
            }
        )
    df = pd.DataFrame(rows).sort_values("objective_score", ascending=False)
    df.to_csv(ARTIFACT_DIR / "food_system_priority_scores.csv", index=False)
    recommended = df.iloc[0].to_dict()
    return df, {
        "method": "weighted food-system health score over efficiency, profitability, sustainability, equity, and nutrition resilience",
        "priority_rows": df.to_dict(orient="records"),
        "current_system": df[df["priority"] == "current_efficiency_profit"].iloc[0].to_dict(),
        "recommended_priority": recommended,
    }


def build_country_applications(recommended_priority: str) -> tuple[pd.DataFrame, dict[str, Any]]:
    current_weights = FOOD_SYSTEM_PRIORITIES["current_efficiency_profit"]
    target_weights = FOOD_SYSTEM_PRIORITIES[recommended_priority]
    rows = []
    for case in COUNTRY_CASES:
        current_score = score_case(case, current_weights)
        target_score = score_case(case, target_weights)
        sustainability_gap = max(0.0, 0.78 - float(case["sustainability"]))
        equity_gap = max(0.0, 0.76 - float(case["equity"]))
        implementation_years = 5 + round(TRANSITION_YEARS * (0.45 * sustainability_gap + 0.35 * equity_gap + 0.20 * (1.0 - float(case["governance_capacity"]))))
        rows.append(
            {
                "country": case["country"],
                "development_group": case["development_group"],
                "current_priority_score": clean_float(current_score, 4),
                "target_priority_score": clean_float(target_score, 4),
                "score_delta": clean_float(target_score - current_score, 4),
                "food_insecurity_rate": case["food_insecurity_rate"],
                "environmental_pressure": case["environmental_pressure"],
                "recommended_implementation_years": min(TRANSITION_YEARS, max(4, implementation_years)),
                "main_gap": "equity" if equity_gap >= sustainability_gap else "sustainability",
            }
        )
    df = pd.DataFrame(rows).sort_values(["development_group", "score_delta"], ascending=[True, False])
    df.to_csv(ARTIFACT_DIR / "country_food_system_applications.csv", index=False)
    return df, {
        "method": "apply the same priority score to developed and developing country cases requested by the official statement",
        "country_rows": df.to_dict(orient="records"),
        "developed_case_count": int((df["development_group"] == "developed").sum()),
        "developing_case_count": int((df["development_group"] == "developing").sum()),
    }


def build_transition_plan(country_df: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, Any]]:
    rows = []
    baseline_equity = float(country_df["target_priority_score"].mean())
    for year in range(1, TRANSITION_YEARS + 1):
        phase = "diagnose and pilot" if year <= 3 else "scale and finance" if year <= 9 else "institutionalize"
        adoption = year / TRANSITION_YEARS
        rows.append(
            {
                "year": year,
                "phase": phase,
                "regional_procurement_share": clean_float(0.20 + 0.42 * adoption, 4),
                "waste_reduction_share": clean_float(0.04 + 0.28 * adoption, 4),
                "nutrition_access_coverage": clean_float(0.18 + 0.52 * adoption, 4),
                "regenerative_area_share": clean_float(0.08 + 0.36 * adoption, 4),
                "projected_food_system_score": clean_float(baseline_equity - 0.10 + 0.10 * adoption, 4),
            }
        )
    df = pd.DataFrame(rows)
    df.to_csv(ARTIFACT_DIR / "food_system_transition_plan.csv", index=False)
    return df, {
        "years_to_implement": TRANSITION_YEARS,
        "timeline_rows": df.to_dict(orient="records"),
        "implementation_logic": "early pilots protect affordability; years 4-9 scale procurement, storage, water, and producer risk sharing; years 10-15 lock in measurement and finance rules",
    }


def build_benefit_cost_analysis() -> tuple[pd.DataFrame, dict[str, Any]]:
    rows = []
    for item in INTERVENTIONS:
        benefit_index = item["sustainability_gain"] * (FOOD_SYSTEM_GHG_SHARE + FOOD_SYSTEM_FRESHWATER_SHARE) + item["equity_gain"] * GLOBAL_HUNGER_MILLIONS / 1000.0
        rows.append(
            {
                **item,
                "estimated_benefit_index": clean_float(benefit_index, 4),
                "net_priority_gain": clean_float(item["sustainability_gain"] + item["equity_gain"] - item["profitability_cost"], 4),
                "developed_country_fit": clean_float(0.50 + item["sustainability_gain"] - 0.25 * item["profitability_cost"], 4),
                "developing_country_fit": clean_float(0.48 + item["equity_gain"] + 0.35 * (1.0 / item["first_benefit_year"]), 4),
            }
        )
    df = pd.DataFrame(rows).sort_values("net_priority_gain", ascending=False)
    df.to_csv(ARTIFACT_DIR / "food_system_benefit_cost.csv", index=False)
    return df, {
        "method": "transparent intervention benefit-cost scoring by timing, equity gain, sustainability gain, and profitability cost",
        "benefit_cost_rows": df.to_dict(orient="records"),
        "timing_note": "nutrition access and waste/storage upgrades pay off earliest; regenerative production and producer risk sharing require longer implementation but improve durability",
    }


def write_frontier(priority_df: pd.DataFrame, country_df: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(8.0, 5.0))
    ax.scatter(priority_df["equity_weight"], priority_df["sustainability_weight"], s=140, c=priority_df["objective_score"], cmap="viridis")
    for _, row in priority_df.iterrows():
        ax.annotate(str(row["priority"]).replace("_", "\n"), (row["equity_weight"], row["sustainability_weight"]), fontsize=8, xytext=(5, 5), textcoords="offset points")
    ax.set_xlabel("Equity priority weight")
    ax.set_ylabel("Sustainability priority weight")
    ax.set_title("Food System Priority Frontier")
    ax.grid(alpha=0.22)
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "food_system_priority_frontier.png", dpi=180)
    plt.close(fig)

    country_df.plot.bar(x="country", y=["current_priority_score", "target_priority_score"], figsize=(8.5, 5.0))
    plt.ylabel("Priority score")
    plt.title("Country Food System Score Under Current and Re-Optimized Priorities")
    plt.tight_layout()
    plt.savefig(ARTIFACT_DIR / "country_food_system_scores.png", dpi=180)
    plt.close()


def build_result(priority_model: dict[str, Any], country_applications: dict[str, Any], transition_plan: dict[str, Any], benefit_cost_analysis: dict[str, Any]) -> dict[str, Any]:
    return {
        "problem_id": "2021-E",
        "title": "Re-Optimizing Food Systems",
        "data_source": {
            "type": "official_statement_parameters",
            "root": str(ARCHIVE_ROOT / "official_assets"),
            "source_pdf": str(PDF_PATH),
            "official_requirements": {
                "optimize_efficiency_profitability_sustainability_equity": True,
                "developed_and_developing_country_applications": True,
                "benefits_and_costs_over_time": True,
                "scalability_and_adaptability": True,
                "twenty_five_page_limit": True,
            },
            "parameters": {
                "global_hunger_millions": GLOBAL_HUNGER_MILLIONS,
                "food_system_ghg_share": FOOD_SYSTEM_GHG_SHARE,
                "food_system_biodiversity_loss_share": FOOD_SYSTEM_BIODIVERSITY_LOSS_SHARE,
                "food_system_deforestation_share": FOOD_SYSTEM_DEFORESTATION_SHARE,
                "food_system_freshwater_share": FOOD_SYSTEM_FRESHWATER_SHARE,
                "transition_years": TRANSITION_YEARS,
                "source_note": "Official PDF statement parameters only; country and policy rows are deterministic planning inputs for audit and replacement.",
            },
        },
        "priority_model": priority_model,
        "country_applications": country_applications,
        "transition_plan": transition_plan,
        "benefit_cost_analysis": benefit_cost_analysis,
        "scalability_adaptability": {
            "scalable_to_larger_systems": "Use the same weighted score with subnational or global rows; adjust intervention capacity and governance constraints.",
            "adaptable_to_other_regions": "Replace country case scores with local food access, water, emissions, producer income, and nutrition measurements.",
            "minimum_data_needed": ["food access", "nutritional adequacy", "supply loss", "producer margin", "water use", "emissions", "governance capacity"],
        },
        "committee_memo": (
            "Memo to the International Comestibles Management Committee: re-optimization should move the food system away from a narrow efficiency-profit objective toward a balanced equity and sustainability target. "
            "The model keeps efficiency visible, but adds nutrition resilience, producer access, water stewardship, and environmental footprint to the objective. "
            "Developed countries can move first through procurement, waste reduction, and regenerative incentives; developing countries need risk sharing, storage, and nutrition access policies so the transition does not reduce affordability."
        ),
        "assumption_audit": {
            "truthfulness_note": "This workflow uses official statement parameters and transparent deterministic planning scenarios; it does not invent placeholder x1/x2/x3 data.",
            "model_limits": [
                "COMAP did not provide country food-system workbooks for this problem.",
                "Country scores are auditable planning inputs that should be replaced by FAO, World Bank, national nutrition, emissions, and water records in a full contest paper.",
                "Weights are policy choices; a final paper should test stakeholder alternatives and uncertainty bands.",
            ],
        },
    }


def build_report(result: dict[str, Any]) -> None:
    recommendation = result["priority_model"]["recommended_priority"]["priority"]
    lines = [
        "# 2021 ICM-E Re-Optimizing Food Systems",
        "",
        "## Data Source",
        f"- Official PDF asset: `{result['data_source']['source_pdf']}`.",
        "- No COMAP numeric attachment is supplied; this workflow uses official statement parameters and explicit deterministic planning inputs.",
        "",
        "## Model Summary",
        f"- Recommended priority: `{recommendation}`.",
        f"- Country applications: {len(result['country_applications']['country_rows'])} developed/developing cases.",
        f"- Transition horizon: {result['transition_plan']['years_to_implement']} years.",
        "",
        "## Committee Memo",
        result["committee_memo"],
        "",
        "## Output Files",
        "- `food_system_priority_scores.csv`: objective score for each priority setting.",
        "- `country_food_system_applications.csv`: developed and developing country applications.",
        "- `food_system_transition_plan.csv`: implementation timeline.",
        "- `food_system_benefit_cost.csv`: benefits, costs, and timing by intervention.",
        "- `food_system_priority_frontier.png`: equity-sustainability frontier.",
    ]
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ensure_pdf_exists()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    priority_df, priority_model = build_priority_model()
    country_df, country_applications = build_country_applications(str(priority_model["recommended_priority"]["priority"]))
    transition_df, transition_plan = build_transition_plan(country_df)
    benefit_df, benefit_cost_analysis = build_benefit_cost_analysis()
    write_frontier(priority_df, country_df)
    result = build_result(priority_model, country_applications, transition_plan, benefit_cost_analysis)
    result["artifacts"] = {
        "food_system_priority_scores": str(ARTIFACT_DIR / "food_system_priority_scores.csv"),
        "country_food_system_applications": str(ARTIFACT_DIR / "country_food_system_applications.csv"),
        "food_system_transition_plan": str(ARTIFACT_DIR / "food_system_transition_plan.csv"),
        "food_system_benefit_cost": str(ARTIFACT_DIR / "food_system_benefit_cost.csv"),
        "food_system_priority_frontier": str(ARTIFACT_DIR / "food_system_priority_frontier.png"),
        "country_food_system_scores": str(ARTIFACT_DIR / "country_food_system_scores.png"),
        "transition_rows": len(transition_df),
        "benefit_cost_rows": len(benefit_df),
    }
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    build_report(result)
    print(json.dumps({"result": str(RESULT_PATH), "report": str(REPORT_PATH), "artifacts": str(ARTIFACT_DIR)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
