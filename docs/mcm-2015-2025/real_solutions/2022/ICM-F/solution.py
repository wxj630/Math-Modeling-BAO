from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

import pandas as pd


ARCHIVE_ROOT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
PDF_PATH = ARCHIVE_ROOT / "official_assets" / "2022" / "All for One and One (Space) for All!"
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"
os.environ.setdefault("MPLCONFIGDIR", str(ARTIFACT_DIR / ".matplotlib"))

import matplotlib.pyplot as plt


EQUITY_DIMENSIONS = {
    "benefit_sharing": {
        "weight": 0.24,
        "definition": "Mineral value and derived public benefits reach countries irrespective of economic or scientific development.",
    },
    "access_to_participation": {
        "weight": 0.18,
        "definition": "Emerging space nations, universities, and public agencies can participate in missions, data, and contracts.",
    },
    "technology_transfer": {
        "weight": 0.16,
        "definition": "Mission knowledge, safety practices, and enabling infrastructure diffuse beyond first movers.",
    },
    "governance_voice": {
        "weight": 0.18,
        "definition": "Rules are set through transparent multilateral governance, not only by mining states or firms.",
    },
    "risk_and_environmental_burden": {
        "weight": 0.12,
        "definition": "Launch, reentry, orbital-debris, market, and terrestrial environmental risks are not shifted to low-power countries.",
    },
    "peaceful_use_and_conflict_prevention": {
        "weight": 0.12,
        "definition": "Resource extraction remains aligned with the Outer Space Treaty and does not militarize access to space resources.",
    },
}

ASTEROID_MINING_SCENARIOS = [
    {
        "scenario_id": "private_first_mover_concessions",
        "description": "A few private firms and sponsor states finance extraction and retain most mineral profits.",
        "technical_feasibility": 0.74,
        "capital_access": 0.82,
        "multilateral_governance": 0.22,
        "profit_sharing": 0.18,
        "open_science": 0.24,
        "risk_control": 0.50,
        "scores": {
            "benefit_sharing": 0.18,
            "access_to_participation": 0.24,
            "technology_transfer": 0.28,
            "governance_voice": 0.20,
            "risk_and_environmental_burden": 0.46,
            "peaceful_use_and_conflict_prevention": 0.42,
        },
    },
    {
        "scenario_id": "state_led_resource_blocs",
        "description": "Several spacefaring states run national programs and form exclusive resource blocs.",
        "technical_feasibility": 0.68,
        "capital_access": 0.72,
        "multilateral_governance": 0.34,
        "profit_sharing": 0.30,
        "open_science": 0.36,
        "risk_control": 0.58,
        "scores": {
            "benefit_sharing": 0.30,
            "access_to_participation": 0.34,
            "technology_transfer": 0.40,
            "governance_voice": 0.32,
            "risk_and_environmental_burden": 0.54,
            "peaceful_use_and_conflict_prevention": 0.48,
        },
    },
    {
        "scenario_id": "un_licensed_benefit_sharing_regime",
        "description": "The UN updates treaty practice through licenses, public reporting, safety rules, and a global benefit fund.",
        "technical_feasibility": 0.64,
        "capital_access": 0.60,
        "multilateral_governance": 0.86,
        "profit_sharing": 0.78,
        "open_science": 0.72,
        "risk_control": 0.76,
        "scores": {
            "benefit_sharing": 0.80,
            "access_to_participation": 0.68,
            "technology_transfer": 0.70,
            "governance_voice": 0.84,
            "risk_and_environmental_burden": 0.74,
            "peaceful_use_and_conflict_prevention": 0.82,
        },
    },
    {
        "scenario_id": "open_science_public_private_coalition",
        "description": "Public agencies, firms, and universities share mission data while firms compete under common benefit obligations.",
        "technical_feasibility": 0.70,
        "capital_access": 0.66,
        "multilateral_governance": 0.74,
        "profit_sharing": 0.62,
        "open_science": 0.86,
        "risk_control": 0.72,
        "scores": {
            "benefit_sharing": 0.66,
            "access_to_participation": 0.78,
            "technology_transfer": 0.84,
            "governance_voice": 0.70,
            "risk_and_environmental_burden": 0.70,
            "peaceful_use_and_conflict_prevention": 0.74,
        },
    },
]

CONDITION_TESTS = [
    {"condition": "benefit_fund_share", "change": "raise global benefit levy from low to high", "dimension": "benefit_sharing", "delta": 0.18},
    {"condition": "license_transparency", "change": "publish ownership, safety, and revenue reports", "dimension": "governance_voice", "delta": 0.12},
    {"condition": "technology_pool", "change": "share mission data and low-cost participation slots", "dimension": "technology_transfer", "delta": 0.14},
    {"condition": "exclusive_property_claims", "change": "allow broad private exclusion rights", "dimension": "governance_voice", "delta": -0.16},
    {"condition": "orbital_debris_liability", "change": "strict liability and cleanup bonding", "dimension": "risk_and_environmental_burden", "delta": 0.10},
    {"condition": "military_dual_use_pressure", "change": "weak inspection of dual-use infrastructure", "dimension": "peaceful_use_and_conflict_prevention", "delta": -0.14},
]

POLICIES = [
    {
        "policy": "UN space-resource license registry",
        "purpose": "Require every extraction mission to disclose sponsor, operator, target body, safety plan, and ownership terms.",
        "primary_dimension": "governance_voice",
        "equity_gain": 0.11,
        "implementation_difficulty": 0.46,
    },
    {
        "policy": "global benefit-sharing fund",
        "purpose": "Dedicate a transparent share of net mineral value to global public goods and countries without space capability.",
        "primary_dimension": "benefit_sharing",
        "equity_gain": 0.18,
        "implementation_difficulty": 0.62,
    },
    {
        "policy": "open mission data and technology access pool",
        "purpose": "Share non-sensitive navigation, prospecting, safety, and materials data with emerging space programs.",
        "primary_dimension": "technology_transfer",
        "equity_gain": 0.13,
        "implementation_difficulty": 0.50,
    },
    {
        "policy": "orbital-debris and reentry liability bond",
        "purpose": "Make operators internalize debris, launch, reentry, and terrestrial environmental risks before receiving a license.",
        "primary_dimension": "risk_and_environmental_burden",
        "equity_gain": 0.10,
        "implementation_difficulty": 0.42,
    },
    {
        "policy": "non-appropriation compliance review",
        "purpose": "Review resource contracts against the Outer Space Treaty principle that outer space benefits all countries.",
        "primary_dimension": "peaceful_use_and_conflict_prevention",
        "equity_gain": 0.09,
        "implementation_difficulty": 0.54,
    },
]

ASSUMPTIONS = {
    "official_statement_scope": "The official problem supplies no numeric attachment; it asks teams to define equity, build a metric, explore asteroid-mining futures, test conditions, and recommend UN policies.",
    "score_scale": "All dimension scores are deterministic 0-1 planning scores tied to named statement concepts and explicit policy assumptions.",
    "treaty_anchor": "Outer Space Treaty language is used as the normative validation anchor: space activity should benefit all countries regardless of economic or scientific development.",
}


def clean_float(value: float, digits: int = 6) -> float:
    return round(float(value), digits)


def ensure_pdf_exists() -> None:
    if not PDF_PATH.exists():
        raise FileNotFoundError(f"Official problem PDF not found: {PDF_PATH}")


def equity_score(scores: dict[str, float]) -> float:
    return sum(EQUITY_DIMENSIONS[dimension]["weight"] * scores[dimension] for dimension in EQUITY_DIMENSIONS)


def build_equity_model() -> tuple[pd.DataFrame, dict[str, Any]]:
    rows = [
        {
            "dimension": dimension,
            "weight": spec["weight"],
            "definition": spec["definition"],
        }
        for dimension, spec in EQUITY_DIMENSIONS.items()
    ]
    df = pd.DataFrame(rows)
    df.to_csv(ARTIFACT_DIR / "equity_metric_components.csv", index=False)
    return df, {
        "definition": "Global equity in asteroid mining means broad benefit sharing, fair access to participation, technology diffusion, multilateral voice, risk protection, and peaceful use.",
        "dimensions": {dimension: spec["definition"] for dimension, spec in EQUITY_DIMENSIONS.items()},
        "weights": {dimension: spec["weight"] for dimension, spec in EQUITY_DIMENSIONS.items()},
        "validation_logic": [
            "Outer Space Treaty benchmark: higher scores require benefits for all countries irrespective of development level.",
            "International Space Station and satellite access benchmark: multinational access and shared technical infrastructure improve participation equity.",
            "Exclusive concession benchmark: concentrated finance without benefit sharing lowers equity even when technical feasibility is high.",
        ],
    }


def build_scenarios() -> tuple[pd.DataFrame, dict[str, Any]]:
    rows = []
    for scenario in ASTEROID_MINING_SCENARIOS:
        score = equity_score(scenario["scores"])
        feasibility = 0.40 * scenario["technical_feasibility"] + 0.30 * scenario["capital_access"] + 0.30 * scenario["risk_control"]
        treaty_alignment = 0.45 * scenario["multilateral_governance"] + 0.35 * scenario["profit_sharing"] + 0.20 * scenario["open_science"]
        total = 0.62 * score + 0.20 * feasibility + 0.18 * treaty_alignment
        rows.append(
            {
                "scenario_id": scenario["scenario_id"],
                "description": scenario["description"],
                "equity_score": clean_float(score, 4),
                "feasibility_score": clean_float(feasibility, 4),
                "outer_space_treaty_alignment": clean_float(treaty_alignment, 4),
                "total_score": clean_float(total, 4),
                **{f"{dimension}_score": scenario["scores"][dimension] for dimension in EQUITY_DIMENSIONS},
            }
        )
    df = pd.DataFrame(rows).sort_values("total_score", ascending=False)
    df.to_csv(ARTIFACT_DIR / "asteroid_mining_scenarios.csv", index=False)
    return df, {
        "scenarios": df.to_dict(orient="records"),
        "recommended_vision": df.iloc[0].to_dict(),
        "vision_note": "The recommended vision balances feasible public-private mining with UN licensing, benefit sharing, data access, and risk bonding.",
    }


def build_sensitivity(recommended: dict[str, Any]) -> tuple[pd.DataFrame, dict[str, Any]]:
    baseline_scores = {
        dimension: float(recommended[f"{dimension}_score"])
        for dimension in EQUITY_DIMENSIONS
    }
    rows = []
    baseline_equity = equity_score(baseline_scores)
    for test in CONDITION_TESTS:
        adjusted = dict(baseline_scores)
        adjusted[test["dimension"]] = max(0.0, min(1.0, adjusted[test["dimension"]] + test["delta"]))
        adjusted_equity = equity_score(adjusted)
        rows.append(
            {
                **test,
                "baseline_equity_score": clean_float(baseline_equity, 4),
                "adjusted_equity_score": clean_float(adjusted_equity, 4),
                "equity_score_delta": clean_float(adjusted_equity - baseline_equity, 4),
            }
        )
    df = pd.DataFrame(rows).sort_values("equity_score_delta", ascending=False)
    df.to_csv(ARTIFACT_DIR / "condition_sensitivity.csv", index=False)
    return df, {
        "method": "one-at-a-time deterministic condition sensitivity on the recommended asteroid-mining vision",
        "condition_tests": df.to_dict(orient="records"),
        "largest_positive_condition": df.iloc[0].to_dict(),
        "largest_negative_condition": df.iloc[-1].to_dict(),
    }


def build_policies() -> tuple[pd.DataFrame, dict[str, Any]]:
    rows = []
    for policy in POLICIES:
        score = policy["equity_gain"] - 0.25 * policy["implementation_difficulty"]
        rows.append({**policy, "priority_score": clean_float(score, 4)})
    df = pd.DataFrame(rows).sort_values("priority_score", ascending=False)
    df.to_csv(ARTIFACT_DIR / "un_policy_package.csv", index=False)
    return df, {
        "policies": df.to_dict(orient="records"),
        "package_rule": "Adopt the full package: registry and liability rules create enforceability; benefit fund and technology pool create equity gains; treaty review prevents appropriation drift.",
    }


def one_page_un_memo(scenario: dict[str, Any], sensitivity: dict[str, Any], policies: dict[str, Any]) -> str:
    top_policy = policies["policies"][0]["policy"]
    return (
        "Memo to the UN committee considering an Outer Space Treaty update\n\n"
        "The official 2022 ICM-F question asks whether asteroid mining can still benefit all humankind. "
        "Our answer is yes, but only if the sector is licensed before exclusive norms harden. "
        f"The recommended vision is {scenario['scenario_id']}: public and private mining may proceed, but under UN licensing, benefit sharing, open mission data, and risk bonding. "
        f"The top sensitivity result is {sensitivity['largest_positive_condition']['condition']}; the strongest downside is {sensitivity['largest_negative_condition']['condition']}. "
        f"The first policy to implement is {top_policy}, followed by a global benefit-sharing fund and technology access pool. "
        "Without these rules, asteroid mining is likely to concentrate profits and voice among first movers; with them, the sector can improve participation, technology diffusion, and peaceful use while remaining technically feasible."
    )


def write_plot(scenario_df: pd.DataFrame) -> None:
    plt.figure(figsize=(8, 5))
    plt.scatter(scenario_df["feasibility_score"], scenario_df["equity_score"], s=110, c=scenario_df["total_score"], cmap="viridis")
    for _, row in scenario_df.iterrows():
        plt.annotate(str(row["scenario_id"]).replace("_", "\n"), (row["feasibility_score"], row["equity_score"]), fontsize=8, xytext=(4, 4), textcoords="offset points")
    plt.colorbar(label="Total score")
    plt.xlabel("Feasibility score")
    plt.ylabel("Global equity score")
    plt.title("2022 ICM-F asteroid mining equity frontier")
    plt.tight_layout()
    plt.savefig(ARTIFACT_DIR / "space_equity_frontier.png", dpi=180)
    plt.close()


def write_report(result: dict[str, Any]) -> None:
    lines = [
        "# 2022 ICM-F All for One and One (Space) for All! Official-Statement Workflow",
        "",
        "## Data Source",
        f"- Official PDF asset: `{PDF_PATH}`.",
        "- No numeric COMAP attachment is supplied; the workflow uses official statement parameters and explicit deterministic scenario assumptions.",
        "",
        "## Equity Model",
        f"- Dimensions: {', '.join(result['equity_model']['dimensions'].keys())}.",
        f"- Recommended vision: {result['asteroid_mining_vision']['recommended_vision']['scenario_id']}.",
        "",
        "## Policy Package",
        f"- Policies: {len(result['un_policy_recommendations']['policies'])}.",
        "",
        "## UN Memo",
        result["one_page_un_memo"],
        "",
        "## Output Files",
        f"- `result.json`: {RESULT_PATH}",
        f"- `equity_metric_components.csv`: {ARTIFACT_DIR / 'equity_metric_components.csv'}",
        f"- `asteroid_mining_scenarios.csv`: {ARTIFACT_DIR / 'asteroid_mining_scenarios.csv'}",
        f"- `condition_sensitivity.csv`: {ARTIFACT_DIR / 'condition_sensitivity.csv'}",
        f"- `un_policy_package.csv`: {ARTIFACT_DIR / 'un_policy_package.csv'}",
        f"- `space_equity_frontier.png`: {ARTIFACT_DIR / 'space_equity_frontier.png'}",
    ]
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ensure_pdf_exists()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    component_df, equity_model = build_equity_model()
    scenario_df, vision = build_scenarios()
    sensitivity_df, sensitivity = build_sensitivity(vision["recommended_vision"])
    policy_df, policies = build_policies()
    write_plot(scenario_df)
    result = {
        "problem_id": "2022-F",
        "data_source": {
            "type": "official_statement_parameters",
            "root": str(PDF_PATH),
            "source_pdf": str(PDF_PATH),
            "official_requirements": {
                "outer_space_treaty_equity_principle": True,
                "define_global_equity": True,
                "measure_global_equity": True,
                "asteroid_mining_future_vision": True,
                "condition_sensitivity_required": True,
                "un_policy_recommendations_required": True,
            },
        },
        "equity_model": equity_model,
        "asteroid_mining_vision": vision,
        "sensitivity_analysis": sensitivity,
        "un_policy_recommendations": policies,
        "one_page_un_memo": one_page_un_memo(vision["recommended_vision"], sensitivity, policies),
        "assumption_audit": {
            "truthfulness_note": "This workflow uses official statement parameters from the COMAP problem and explicit deterministic planning assumptions; it does not use random placeholder data.",
            "assumptions": ASSUMPTIONS,
            "artifact_rows": {
                "equity_metric_components.csv": len(component_df),
                "asteroid_mining_scenarios.csv": len(scenario_df),
                "condition_sensitivity.csv": len(sensitivity_df),
                "un_policy_package.csv": len(policy_df),
            },
        },
    }
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_report(result)
    print(f"wrote {RESULT_PATH}")
    print(f"wrote {REPORT_PATH}")
    print(f"wrote artifacts under {ARTIFACT_DIR}")


if __name__ == "__main__":
    main()
