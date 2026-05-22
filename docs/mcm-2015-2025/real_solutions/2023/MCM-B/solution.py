from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ARCHIVE_ROOT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
PDF_PATH = ARCHIVE_ROOT / "official_assets_extracted" / "2023" / "Reimagining Maasai Mara.pdf"
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"

WILDLIFE_ACT_YEAR = 2013
MANAGEMENT_AMENDMENT_YEAR = 2020
PROJECTION_YEARS = 20

OFFICIAL_STATEMENT_PARAMETERS = {
    "wildlife_act_year": WILDLIFE_ACT_YEAR,
    "management_amendment_year": MANAGEMENT_AMENDMENT_YEAR,
    "focus_preserve": "Maasai Mara",
    "requirements": [
        "recommend policies and management strategies for different areas within the current preserve",
        "protect wildlife and natural resources while balancing interests of local residents",
        "mitigate lost opportunities for people near the preserve",
        "minimize negative interactions between animals and people attracted to the preserve",
        "rank and compare outcomes from the methodology",
        "predict long-term trends and discuss transfer to other wildlife management areas",
        "provide a two-page non-technical report for the Kenyan Tourism and Wildlife Committee",
    ],
    "source_note": "Official PDF statement parameters only; zone scores and policy coefficients are deterministic scenario assumptions, not observed Maasai Mara field data.",
}

ZONES = [
    {
        "zone": "core migration corridor",
        "wildlife_value": 0.96,
        "tourism_value": 0.84,
        "resident_pressure": 0.36,
        "conflict_exposure": 0.58,
        "habitat_fragility": 0.91,
        "recommended_policy": "strict habitat protection with community revenue sharing",
    },
    {
        "zone": "riverine habitat and watering points",
        "wildlife_value": 0.90,
        "tourism_value": 0.72,
        "resident_pressure": 0.42,
        "conflict_exposure": 0.66,
        "habitat_fragility": 0.87,
        "recommended_policy": "seasonal access zoning and riparian buffer enforcement",
    },
    {
        "zone": "community conservancy interface",
        "wildlife_value": 0.72,
        "tourism_value": 0.62,
        "resident_pressure": 0.86,
        "conflict_exposure": 0.82,
        "habitat_fragility": 0.63,
        "recommended_policy": "co-managed conservancy with livestock compensation and grazing calendar",
    },
    {
        "zone": "tourism lodge cluster",
        "wildlife_value": 0.64,
        "tourism_value": 0.91,
        "resident_pressure": 0.51,
        "conflict_exposure": 0.54,
        "habitat_fragility": 0.59,
        "recommended_policy": "visitor caps, concession fees, waste-water standards, local hiring quota",
    },
    {
        "zone": "settlement and agriculture edge",
        "wildlife_value": 0.48,
        "tourism_value": 0.35,
        "resident_pressure": 0.93,
        "conflict_exposure": 0.88,
        "habitat_fragility": 0.52,
        "recommended_policy": "fencing hotspots, predator-proof bomas, crop protection and benefit payments",
    },
    {
        "zone": "restoration buffer outside current boundary",
        "wildlife_value": 0.69,
        "tourism_value": 0.50,
        "resident_pressure": 0.74,
        "conflict_exposure": 0.70,
        "habitat_fragility": 0.76,
        "recommended_policy": "voluntary easements, grassland restoration and rotational grazing contracts",
    },
]

POLICY_PACKAGES = [
    {
        "policy": "baseline enforcement only",
        "wildlife_protection_gain": 0.04,
        "resident_benefit_gain": 0.02,
        "conflict_reduction": 0.03,
        "tourism_revenue_gain": 0.03,
        "governance_feasibility": 0.80,
        "implementation_cost_index": 0.18,
    },
    {
        "policy": "strict core zoning plus visitor caps",
        "wildlife_protection_gain": 0.22,
        "resident_benefit_gain": 0.09,
        "conflict_reduction": 0.15,
        "tourism_revenue_gain": 0.10,
        "governance_feasibility": 0.64,
        "implementation_cost_index": 0.42,
    },
    {
        "policy": "community conservancy revenue sharing",
        "wildlife_protection_gain": 0.18,
        "resident_benefit_gain": 0.31,
        "conflict_reduction": 0.23,
        "tourism_revenue_gain": 0.18,
        "governance_feasibility": 0.77,
        "implementation_cost_index": 0.49,
    },
    {
        "policy": "compensation and predator-proof livestock program",
        "wildlife_protection_gain": 0.11,
        "resident_benefit_gain": 0.26,
        "conflict_reduction": 0.34,
        "tourism_revenue_gain": 0.07,
        "governance_feasibility": 0.73,
        "implementation_cost_index": 0.38,
    },
    {
        "policy": "restoration buffer and voluntary easements",
        "wildlife_protection_gain": 0.25,
        "resident_benefit_gain": 0.22,
        "conflict_reduction": 0.28,
        "tourism_revenue_gain": 0.13,
        "governance_feasibility": 0.67,
        "implementation_cost_index": 0.55,
    },
    {
        "policy": "integrated mosaic plan",
        "wildlife_protection_gain": 0.30,
        "resident_benefit_gain": 0.33,
        "conflict_reduction": 0.35,
        "tourism_revenue_gain": 0.21,
        "governance_feasibility": 0.70,
        "implementation_cost_index": 0.62,
    },
]


def clean_float(value: float, digits: int = 6) -> float:
    return round(float(value), digits)


def ensure_pdf_exists() -> None:
    if not PDF_PATH.exists():
        raise FileNotFoundError(f"Official problem PDF not found: {PDF_PATH}")


def build_zone_scores() -> tuple[pd.DataFrame, dict[str, object]]:
    rows = []
    for zone in ZONES:
        conservation_priority = 0.38 * zone["wildlife_value"] + 0.28 * zone["habitat_fragility"] + 0.18 * zone["conflict_exposure"] + 0.16 * zone["tourism_value"]
        community_priority = 0.42 * zone["resident_pressure"] + 0.28 * zone["conflict_exposure"] + 0.18 * (1.0 - zone["tourism_value"]) + 0.12 * zone["wildlife_value"]
        balance_need = abs(conservation_priority - community_priority)
        rows.append(
            {
                **zone,
                "conservation_priority": clean_float(conservation_priority, 4),
                "community_priority": clean_float(community_priority, 4),
                "balance_need": clean_float(balance_need, 4),
                "management_intensity": "high" if max(conservation_priority, community_priority) >= 0.72 else "medium",
            }
        )
    df = pd.DataFrame(rows).sort_values(["management_intensity", "conservation_priority"], ascending=[True, False])
    df.to_csv(ARTIFACT_DIR / "policy_zone_scores.csv", index=False)
    return df, {
        "model": "zone-level multi-criteria scoring for wildlife value, habitat fragility, resident pressure, conflict exposure, and tourism value",
        "zones": df.to_dict(orient="records"),
        "policy_principle": "Use stricter protection in high wildlife/high fragility zones and co-management/compensation in high resident-pressure interfaces.",
    }


def evaluate_policies(zone_df: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, object]]:
    rows = []
    mean_conflict = float(zone_df["conflict_exposure"].mean())
    mean_resident_pressure = float(zone_df["resident_pressure"].mean())
    for package in POLICY_PACKAGES:
        ecological_score = 0.58 * package["wildlife_protection_gain"] + 0.24 * package["conflict_reduction"] + 0.18 * mean_conflict
        resident_score = 0.56 * package["resident_benefit_gain"] + 0.24 * package["conflict_reduction"] + 0.20 * mean_resident_pressure
        economic_score = 0.58 * package["tourism_revenue_gain"] + 0.24 * package["resident_benefit_gain"] + 0.18 * package["governance_feasibility"]
        cost_penalty = 0.30 * package["implementation_cost_index"] + 0.10 * (1.0 - package["governance_feasibility"])
        composite = 0.36 * ecological_score + 0.32 * resident_score + 0.22 * economic_score + 0.10 * package["governance_feasibility"] - cost_penalty
        rows.append(
            {
                **package,
                "ecological_score": clean_float(ecological_score, 4),
                "resident_score": clean_float(resident_score, 4),
                "economic_score": clean_float(economic_score, 4),
                "composite_score": clean_float(composite, 4),
            }
        )
    df = pd.DataFrame(rows).sort_values("composite_score", ascending=False)
    df.to_csv(ARTIFACT_DIR / "policy_package_ranking.csv", index=False)
    return df, {
        "methodology": "weighted multi-objective evaluation balancing ecological protection, local opportunity costs, conflict reduction, tourism revenue, feasibility, and cost",
        "ranked_policies": df.to_dict(orient="records"),
        "best_policy": df.iloc[0].to_dict(),
        "weights": {
            "ecology": 0.36,
            "resident_interest": 0.32,
            "economic_impact": 0.22,
            "governance_feasibility": 0.10,
            "cost_penalty": "0.30 * cost + 0.10 * infeasibility",
        },
    }


def project_interactions(policy_df: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, object]]:
    best = policy_df.iloc[0].to_dict()
    baseline_conflict = 1.00
    baseline_wildlife = 1.00
    conflict = baseline_conflict
    wildlife = baseline_wildlife
    rows = []
    annual_learning = 0.018
    displacement_pressure = 0.010
    for year in range(1, PROJECTION_YEARS + 1):
        maturity = min(1.0, 0.35 + 0.045 * year)
        conflict *= 1.0 - best["conflict_reduction"] * maturity * 0.18 + displacement_pressure
        wildlife *= 1.0 + best["wildlife_protection_gain"] * maturity * 0.08 - 0.015 * conflict
        resident_acceptance = min(1.0, 0.48 + best["resident_benefit_gain"] * maturity + annual_learning * year)
        rows.append(
            {
                "year": year,
                "policy": best["policy"],
                "conflict_index": clean_float(conflict, 4),
                "wildlife_population_index": clean_float(wildlife, 4),
                "resident_acceptance_index": clean_float(resident_acceptance, 4),
                "implementation_maturity": clean_float(maturity, 4),
            }
        )
    df = pd.DataFrame(rows)
    df.to_csv(ARTIFACT_DIR / "human_wildlife_interaction_projection.csv", index=False)
    return df, {
        "model": "discrete annual projection for conflict, wildlife index, and resident acceptance under the highest-ranked policy package",
        "selected_policy": best["policy"],
        "interaction_projection": df.to_dict(orient="records"),
        "certainty_note": "Certainty is highest for direction-of-change comparisons across policies and lower for numeric year-20 levels because coefficients are scenario assumptions.",
    }


def project_economics(policy_df: pd.DataFrame, interaction_df: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, object]]:
    best = policy_df.iloc[0].to_dict()
    rows = []
    tourism_revenue_index = 1.00
    community_share = 0.14
    local_opportunity_cost = 0.26
    for year, interaction in interaction_df.iterrows():
        maturity = float(interaction["implementation_maturity"])
        tourism_revenue_index *= 1.0 + best["tourism_revenue_gain"] * 0.045 * maturity
        community_share = min(0.38, community_share + best["resident_benefit_gain"] * 0.010)
        local_opportunity_cost *= 1.0 - best["resident_benefit_gain"] * 0.030 - best["conflict_reduction"] * 0.020
        rows.append(
            {
                "year": int(interaction["year"]),
                "tourism_revenue_index": clean_float(tourism_revenue_index, 4),
                "community_revenue_share": clean_float(community_share, 4),
                "community_revenue_index": clean_float(tourism_revenue_index * community_share, 4),
                "local_opportunity_cost_index": clean_float(local_opportunity_cost, 4),
                "net_community_benefit_index": clean_float(tourism_revenue_index * community_share - local_opportunity_cost, 4),
            }
        )
    df = pd.DataFrame(rows)
    df.to_csv(ARTIFACT_DIR / "community_revenue_projection.csv", index=False)
    return df, {
        "model": "tourism revenue and community benefit projection with revenue sharing and reduced local opportunity costs",
        "community_revenue_projection": df.to_dict(orient="records"),
        "year20_net_community_benefit_index": clean_float(float(df.iloc[-1]["net_community_benefit_index"]), 4),
        "economic_interpretation": "The policy is valuable only if a visible share of tourism and conservation finance reaches households bearing wildlife opportunity costs.",
    }


def build_long_term_outcomes(interaction_df: pd.DataFrame, economics_df: pd.DataFrame) -> dict[str, object]:
    year20 = interaction_df.iloc[-1]
    econ20 = economics_df.iloc[-1]
    outcome_score = 0.35 * float(year20["wildlife_population_index"]) + 0.30 * (1.0 - float(year20["conflict_index"])) + 0.25 * float(year20["resident_acceptance_index"]) + 0.10 * max(0.0, float(econ20["net_community_benefit_index"]))
    return {
        "projection_years": PROJECTION_YEARS,
        "year20_conflict_index": clean_float(float(year20["conflict_index"]), 4),
        "year20_wildlife_population_index": clean_float(float(year20["wildlife_population_index"]), 4),
        "year20_resident_acceptance_index": clean_float(float(year20["resident_acceptance_index"]), 4),
        "year20_net_community_benefit_index": clean_float(float(econ20["net_community_benefit_index"]), 4),
        "long_term_outcome_score": clean_float(outcome_score, 4),
        "risk_register": [
            "elite capture of revenue-sharing funds",
            "displacement of conflict to zones outside the current preserve boundary",
            "tourism volatility from drought, disease, or security shocks",
            "weak enforcement of grazing calendars and riparian buffers",
        ],
        "monitoring_indicators": [
            "conflict incidents per zone per season",
            "wildlife corridor use and calf recruitment",
            "household compensation processing time",
            "community revenue share and local hiring percentage",
            "vegetation cover in restoration buffers",
        ],
    }


def build_transferability() -> dict[str, object]:
    return {
        "target_area_type": "other wildlife management areas with boundary communities and tourism value",
        "adaptation_steps": [
            "replace zone scores with local wildlife corridors, water points, settlements, tourism assets, and conflict hotspots",
            "recalibrate resident pressure and opportunity-cost weights through community consultation",
            "test policy packages against the local legal framework and enforcement capacity",
            "run the same 20-year conflict/wildlife/community-benefit projection under local drought and tourism volatility scenarios",
            "publish a dashboard that separates ecological, resident, economic, and governance outcomes",
        ],
        "limits": "The framework transfers as a decision process, not as fixed numerical scores; local field data must replace the scenario coefficients.",
    }


def create_frontier_plot(policy_df: pd.DataFrame, interaction_df: pd.DataFrame, economics_df: pd.DataFrame) -> None:
    plt.figure(figsize=(8, 5))
    plt.scatter(policy_df["resident_score"], policy_df["ecological_score"], s=(policy_df["composite_score"] + 0.1) * 420, alpha=0.75)
    for _, row in policy_df.iterrows():
        plt.annotate(row["policy"].split()[0], (row["resident_score"], row["ecological_score"]), fontsize=8)
    plt.xlabel("Resident interest score")
    plt.ylabel("Ecological score")
    plt.title("Maasai Mara policy tradeoff frontier")
    plt.tight_layout()
    plt.savefig(ARTIFACT_DIR / "maasai_mara_policy_frontier.png", dpi=180)
    plt.close()

    combined = interaction_df.merge(economics_df, on="year")
    combined.to_csv(ARTIFACT_DIR / "long_term_outcome_projection.csv", index=False)


def write_report(result: dict[str, object]) -> None:
    best = result["policy_evaluation"]["best_policy"]
    long_term = result["long_term_outcomes"]
    lines = [
        "# 2023 MCM-B Reimagining Maasai Mara",
        "",
        "## Official Statement Basis",
        "- Source: `Reimagining Maasai Mara.pdf`.",
        f"- Official references include Kenya's Wildlife Conservation and Management Act, {WILDLIFE_ACT_YEAR}, and later governance amendments in {MANAGEMENT_AMENDMENT_YEAR}.",
        "- No COMAP numeric data attachment is provided; zone weights and projection coefficients are deterministic scenario assumptions, not field observations.",
        "",
        "## Model",
        "- Zone model: multi-criteria evaluation over wildlife value, habitat fragility, resident pressure, conflict exposure, and tourism value.",
        "- Policy model: weighted ecological/resident/economic/feasibility score with implementation cost penalty.",
        "- Projection model: annual discrete dynamics for conflict, wildlife index, resident acceptance, tourism revenue, and community benefit.",
        "- Tutorial model references: comprehensive evaluation, graph/spatial zoning, optimization, and dynamic systems from `/Users/wuxiaojun/code/My-Agent/intro-mathmodel`.",
        "",
        "## Results",
        f"- Highest-ranked policy: {best['policy']} with composite score {best['composite_score']}.",
        f"- Year-20 conflict index: {long_term['year20_conflict_index']}.",
        f"- Year-20 wildlife index: {long_term['year20_wildlife_population_index']}.",
        f"- Year-20 resident acceptance index: {long_term['year20_resident_acceptance_index']}.",
        "",
        "## Committee Report",
        str(result["committee_report"]),
    ]
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ensure_pdf_exists()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    zone_df, zoning_policy_model = build_zone_scores()
    policy_df, policy_evaluation = evaluate_policies(zone_df)
    interaction_df, interaction_model = project_interactions(policy_df)
    economics_df, economic_impact_model = project_economics(policy_df, interaction_df)
    long_term_outcomes = build_long_term_outcomes(interaction_df, economics_df)
    transferability = build_transferability()
    create_frontier_plot(policy_df, interaction_df, economics_df)
    result = {
        "problem_id": "2023-B",
        "title": "Reimagining Maasai Mara",
        "data_source": {
            "type": "official_statement_parameters",
            "root": str(ARCHIVE_ROOT),
            "source_pdf": str(PDF_PATH),
            "parameters": OFFICIAL_STATEMENT_PARAMETERS,
            "scenario_assumption_note": "All zone scores, policy gains, costs, and projections are deterministic assumptions for a reproducible policy experiment; they are not observed Maasai Mara field measurements.",
        },
        "zoning_policy_model": zoning_policy_model,
        "policy_evaluation": policy_evaluation,
        "interaction_model": interaction_model,
        "economic_impact_model": economic_impact_model,
        "long_term_outcomes": long_term_outcomes,
        "transferability": transferability,
        "committee_report": "To the Kenyan Tourism and Wildlife Committee: adopt an integrated mosaic plan for the Maasai Mara that keeps strict protection in core wildlife corridors, shares tourism revenue through community conservancies, funds compensation and predator-proof livestock measures at settlement edges, and restores buffer lands through voluntary easements. This approach protects wildlife and natural resources while directly addressing the lost opportunities and human-wildlife conflict borne by neighboring residents.",
    }
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_report(result)
    print(f"wrote {RESULT_PATH}")
    print(f"wrote {REPORT_PATH}")
    print(f"wrote artifacts under {ARTIFACT_DIR}")


if __name__ == "__main__":
    main()
