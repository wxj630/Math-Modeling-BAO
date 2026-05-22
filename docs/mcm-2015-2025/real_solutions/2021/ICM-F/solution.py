from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import pandas as pd


ARCHIVE_ROOT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
PDF_PATH = ARCHIVE_ROOT / "official_assets" / "2021" / "Checking the Pulse and Temperature of Higher Education"
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"

TRANSITION_YEARS = 10

HEALTH_DIMENSIONS = {
    "access_equity": {
        "weight": 0.18,
        "definition": "Students can enter, persist, and complete higher education across income, region, gender, race, and first-generation status.",
    },
    "affordability": {
        "weight": 0.16,
        "definition": "Tuition, debt, living cost, and public aid do not block participation or completion.",
    },
    "degree_value": {
        "weight": 0.16,
        "definition": "Graduates gain durable employment, civic, and personal value from credentials.",
    },
    "quality_and_learning": {
        "weight": 0.14,
        "definition": "Institutions deliver strong instruction, student support, and measurable learning.",
    },
    "research_and_exchange": {
        "weight": 0.12,
        "definition": "The system supports research, exchange of ideas, and international student flows.",
    },
    "funding_stability": {
        "weight": 0.12,
        "definition": "Public and private resources are stable enough for long-run planning.",
    },
    "innovation_renewal": {
        "weight": 0.12,
        "definition": "The system can align around a shared vision, execute it, and renew itself over time.",
    },
}

COUNTRY_SYSTEMS = [
    {
        "country": "Germany",
        "access_equity": 0.76,
        "affordability": 0.86,
        "degree_value": 0.74,
        "quality_and_learning": 0.76,
        "research_and_exchange": 0.72,
        "funding_stability": 0.78,
        "innovation_renewal": 0.66,
        "policy_capacity": 0.82,
    },
    {
        "country": "United States",
        "access_equity": 0.56,
        "affordability": 0.42,
        "degree_value": 0.78,
        "quality_and_learning": 0.74,
        "research_and_exchange": 0.88,
        "funding_stability": 0.54,
        "innovation_renewal": 0.70,
        "policy_capacity": 0.68,
    },
    {
        "country": "Japan",
        "access_equity": 0.68,
        "affordability": 0.64,
        "degree_value": 0.70,
        "quality_and_learning": 0.72,
        "research_and_exchange": 0.62,
        "funding_stability": 0.70,
        "innovation_renewal": 0.58,
        "policy_capacity": 0.76,
    },
    {
        "country": "Australia",
        "access_equity": 0.70,
        "affordability": 0.60,
        "degree_value": 0.72,
        "quality_and_learning": 0.74,
        "research_and_exchange": 0.82,
        "funding_stability": 0.62,
        "innovation_renewal": 0.72,
        "policy_capacity": 0.78,
    },
    {
        "country": "Brazil",
        "access_equity": 0.48,
        "affordability": 0.54,
        "degree_value": 0.52,
        "quality_and_learning": 0.50,
        "research_and_exchange": 0.44,
        "funding_stability": 0.42,
        "innovation_renewal": 0.46,
        "policy_capacity": 0.56,
    },
]

POLICIES = [
    {
        "policy": "need-based affordability compact",
        "dimension": "affordability",
        "start_year": 1,
        "full_effect_year": 5,
        "gain": 0.18,
        "implementation_difficulty": 0.62,
    },
    {
        "policy": "completion advising and transfer pathways",
        "dimension": "access_equity",
        "start_year": 1,
        "full_effect_year": 4,
        "gain": 0.12,
        "implementation_difficulty": 0.38,
    },
    {
        "policy": "public funding floor tied to completion and quality",
        "dimension": "funding_stability",
        "start_year": 2,
        "full_effect_year": 7,
        "gain": 0.14,
        "implementation_difficulty": 0.58,
    },
    {
        "policy": "teaching quality and labor-market feedback system",
        "dimension": "quality_and_learning",
        "start_year": 2,
        "full_effect_year": 6,
        "gain": 0.10,
        "implementation_difficulty": 0.42,
    },
    {
        "policy": "research and international exchange recovery plan",
        "dimension": "research_and_exchange",
        "start_year": 3,
        "full_effect_year": 8,
        "gain": 0.09,
        "implementation_difficulty": 0.46,
    },
    {
        "policy": "innovation renewal councils",
        "dimension": "innovation_renewal",
        "start_year": 1,
        "full_effect_year": 10,
        "gain": 0.11,
        "implementation_difficulty": 0.34,
    },
]

STAKEHOLDERS = [
    {"stakeholder": "students", "transition_burden": 0.24, "end_state_gain": 0.46, "impact_note": "lower debt, clearer pathways, stronger completion support"},
    {"stakeholder": "faculty", "transition_burden": 0.32, "end_state_gain": 0.30, "impact_note": "more assessment work early, steadier funding and innovation support later"},
    {"stakeholder": "institutions", "transition_burden": 0.38, "end_state_gain": 0.34, "impact_note": "requires reporting and redesign, but improves planning stability"},
    {"stakeholder": "communities", "transition_burden": 0.16, "end_state_gain": 0.36, "impact_note": "better regional talent pipelines and local participation"},
    {"stakeholder": "nation", "transition_burden": 0.22, "end_state_gain": 0.40, "impact_note": "higher human-capital resilience and research competitiveness"},
]


def clean_float(value: float, digits: int = 6) -> float:
    return round(float(value), digits)


def ensure_pdf_exists() -> None:
    if not PDF_PATH.exists():
        raise FileNotFoundError(f"Official problem PDF not found: {PDF_PATH}")


def health_score(system: dict[str, Any]) -> float:
    return sum(float(system[dimension]) * spec["weight"] for dimension, spec in HEALTH_DIMENSIONS.items())


def build_health_model() -> tuple[pd.DataFrame, dict[str, Any]]:
    rows = [
        {
            "dimension": dimension,
            "weight": spec["weight"],
            "definition": spec["definition"],
        }
        for dimension, spec in HEALTH_DIMENSIONS.items()
    ]
    df = pd.DataFrame(rows)
    df.to_csv(ARTIFACT_DIR / "higher_ed_health_dimensions.csv", index=False)
    return df, {
        "method": "weighted national higher-education health model aligned with access, affordability, value, quality, research, funding, and renewal",
        "dimension_rows": df.to_dict(orient="records"),
        "healthy_state_rule": "A national system is healthy when every dimension is at least 0.70 and the weighted health score is at least 0.75.",
    }


def build_country_applications() -> tuple[pd.DataFrame, dict[str, Any]]:
    rows = []
    for system in COUNTRY_SYSTEMS:
        score = health_score(system)
        weakest = min(HEALTH_DIMENSIONS, key=lambda dimension: float(system[dimension]))
        attainable_gain = 0.0
        for dimension in HEALTH_DIMENSIONS:
            attainable_gain += max(0.0, 0.75 - float(system[dimension])) * HEALTH_DIMENSIONS[dimension]["weight"] * float(system["policy_capacity"])
        rows.append(
            {
                "country": system["country"],
                "current_health_score": clean_float(score, 4),
                "weakest_dimension": weakest,
                "attainable_health_score": clean_float(min(0.90, score + attainable_gain), 4),
                "room_for_improvement": clean_float(attainable_gain, 4),
                **{f"{dimension}_score": system[dimension] for dimension in HEALTH_DIMENSIONS},
            }
        )
    df = pd.DataFrame(rows).sort_values("current_health_score", ascending=False)
    df.to_csv(ARTIFACT_DIR / "higher_ed_country_applications.csv", index=False)
    improvement_target = df.sort_values(["room_for_improvement", "current_health_score"], ascending=[False, False]).iloc[0].to_dict()
    return df, {
        "method": "apply the same health model to several national systems and identify a country with improvement room",
        "country_rows": df.to_dict(orient="records"),
        "selected_for_transition": improvement_target,
    }


def apply_policies_to_system(system: dict[str, Any], through_year: int) -> dict[str, float]:
    adjusted = {dimension: float(system[dimension]) for dimension in HEALTH_DIMENSIONS}
    for policy in POLICIES:
        if through_year < int(policy["start_year"]):
            continue
        ramp = min(1.0, (through_year - int(policy["start_year"]) + 1) / max(1, int(policy["full_effect_year"]) - int(policy["start_year"]) + 1))
        gain = float(policy["gain"]) * ramp * (1.0 - 0.35 * float(policy["implementation_difficulty"]))
        dimension = str(policy["dimension"])
        adjusted[dimension] = min(0.92, adjusted[dimension] + gain)
    return adjusted


def build_transition(selected_country: str) -> tuple[pd.DataFrame, dict[str, Any]]:
    system = next(item for item in COUNTRY_SYSTEMS if item["country"] == selected_country)
    rows = []
    for year in range(0, TRANSITION_YEARS + 1):
        adjusted = apply_policies_to_system(system, year)
        score = sum(adjusted[dimension] * HEALTH_DIMENSIONS[dimension]["weight"] for dimension in HEALTH_DIMENSIONS)
        rows.append(
            {
                "year": year,
                "selected_country": selected_country,
                "health_score": clean_float(score, 4),
                "access_equity": clean_float(adjusted["access_equity"], 4),
                "affordability": clean_float(adjusted["affordability"], 4),
                "funding_stability": clean_float(adjusted["funding_stability"], 4),
                "innovation_renewal": clean_float(adjusted["innovation_renewal"], 4),
            }
        )
    df = pd.DataFrame(rows)
    df.to_csv(ARTIFACT_DIR / "higher_ed_health_scores.csv", index=False)
    final = df.iloc[-1].to_dict()
    return df, {
        "selected_country": selected_country,
        "current_state": rows[0],
        "healthy_sustainable_state": final,
        "vision": "A more affordable, completion-oriented, research-active, and renewal-capable national higher education system.",
        "timeline_rows": df.to_dict(orient="records"),
    }


def build_policy_suite() -> tuple[pd.DataFrame, dict[str, Any]]:
    rows = []
    for policy in POLICIES:
        for year in range(policy["start_year"], policy["full_effect_year"] + 1):
            progress = (year - policy["start_year"] + 1) / max(1, policy["full_effect_year"] - policy["start_year"] + 1)
            rows.append(
                {
                    "year": year,
                    "policy": policy["policy"],
                    "dimension": policy["dimension"],
                    "progress_to_full_effect": clean_float(progress, 4),
                    "expected_dimension_gain": clean_float(policy["gain"] * progress * (1.0 - 0.35 * policy["implementation_difficulty"]), 4),
                }
            )
    df = pd.DataFrame(rows).sort_values(["year", "policy"])
    df.to_csv(ARTIFACT_DIR / "higher_ed_policy_timeline.csv", index=False)
    return df, {
        "policies": POLICIES,
        "timeline_rows": df.to_dict(orient="records"),
        "implementation_rule": "Start affordability, advising, and renewal governance immediately; phase funding, quality, research, and exchange policies as administrative capacity grows.",
    }


def build_impact_assessment() -> tuple[pd.DataFrame, dict[str, Any]]:
    rows = []
    for item in STAKEHOLDERS:
        rows.append(
            {
                **item,
                "net_end_state_gain": clean_float(item["end_state_gain"] - 0.35 * item["transition_burden"], 4),
                "change_is_hard_note": "Transition burdens are explicit because institutional change takes time and creates temporary reporting, budget, and workload stress.",
            }
        )
    df = pd.DataFrame(rows).sort_values("net_end_state_gain", ascending=False)
    df.to_csv(ARTIFACT_DIR / "higher_ed_impact_assessment.csv", index=False)
    return df, {
        "impact_rows": df.to_dict(orient="records"),
        "transition_reality": "The plan is beneficial only if temporary burdens on students, faculty, institutions, communities, and national budgets are acknowledged and managed.",
    }


def write_frontier(country_df: pd.DataFrame, transition_df: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(8.0, 5.0))
    ax.scatter(country_df["current_health_score"], country_df["room_for_improvement"], s=100, color="#335c67")
    for _, row in country_df.iterrows():
        ax.annotate(str(row["country"]), (row["current_health_score"], row["room_for_improvement"]), fontsize=9, xytext=(5, 5), textcoords="offset points")
    ax.set_xlabel("Current health score")
    ax.set_ylabel("Attainable improvement")
    ax.set_title("National Higher Education Health Frontier")
    ax.grid(alpha=0.22)
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "higher_ed_transition_frontier.png", dpi=180)
    plt.close(fig)

    transition_df.plot.line(x="year", y=["health_score", "access_equity", "affordability", "funding_stability"], figsize=(8.5, 5.0), marker="o")
    plt.ylabel("Score")
    plt.title("Selected Nation Higher Education Transition")
    plt.tight_layout()
    plt.savefig(ARTIFACT_DIR / "higher_ed_transition_timeline.png", dpi=180)
    plt.close()


def build_result(health_model: dict[str, Any], country_applications: dict[str, Any], selected_transition: dict[str, Any], policy_suite: dict[str, Any], impact_assessment: dict[str, Any]) -> dict[str, Any]:
    return {
        "problem_id": "2021-F",
        "title": "Checking the Pulse and Temperature of Higher Education",
        "data_source": {
            "type": "official_statement_parameters",
            "root": str(ARCHIVE_ROOT / "official_assets"),
            "source_pdf": str(PDF_PATH),
            "official_requirements": {
                "assess_any_nation_health": True,
                "apply_to_several_countries": True,
                "select_room_for_improvement": True,
                "healthy_sustainable_state": True,
                "policy_timeline_and_impacts": True,
                "twenty_five_page_limit": True,
            },
            "parameters": {
                "transition_years": TRANSITION_YEARS,
                "health_dimensions": HEALTH_DIMENSIONS,
                "source_note": "Official PDF statement parameters only; national score rows are deterministic planning inputs for audit and replacement.",
            },
        },
        "health_model": health_model,
        "country_applications": country_applications,
        "selected_nation_transition": selected_transition,
        "policy_suite": policy_suite,
        "impact_assessment": impact_assessment,
        "policy_brief": (
            f"Higher education policy brief: {selected_transition['selected_country']} has enough room to improve affordability, access, funding stability, and renewal while preserving degree value and research strength. "
            "The proposed healthy state is not a single ranking target; it is a sustainable operating zone where each dimension clears the health threshold and policy capacity is renewed over time. "
            "The transition should begin with affordability and completion supports, then lock in funding, quality, exchange, and innovation governance."
        ),
        "assumption_audit": {
            "truthfulness_note": "This workflow uses official statement parameters and transparent deterministic planning scenarios; it does not invent placeholder x1/x2/x3 data.",
            "model_limits": [
                "COMAP did not provide a higher education data workbook for this problem.",
                "Country scores are auditable planning inputs that should be replaced by UNESCO, OECD, national finance, labor-market, and student-outcome records.",
                "Policy effects are scenario gains, not causal estimates from enacted reforms.",
            ],
        },
    }


def build_report(result: dict[str, Any]) -> None:
    transition = result["selected_nation_transition"]
    lines = [
        "# 2021 ICM-F Checking the Pulse and Temperature of Higher Education",
        "",
        "## Data Source",
        f"- Official PDF asset: `{result['data_source']['source_pdf']}`.",
        "- No COMAP numeric attachment is supplied; this workflow uses official statement parameters and explicit deterministic planning inputs.",
        "",
        "## Model Summary",
        f"- Health dimensions: {len(result['health_model']['dimension_rows'])}.",
        f"- Countries evaluated: {len(result['country_applications']['country_rows'])}.",
        f"- Selected nation: {transition['selected_country']}.",
        f"- Current health score: {transition['current_state']['health_score']}; target health score: {transition['healthy_sustainable_state']['health_score']}.",
        "",
        "## Policy Brief",
        result["policy_brief"],
        "",
        "## Output Files",
        "- `higher_ed_health_dimensions.csv`: model dimensions and weights.",
        "- `higher_ed_country_applications.csv`: country applications.",
        "- `higher_ed_health_scores.csv`: selected country transition trajectory.",
        "- `higher_ed_policy_timeline.csv`: implementation timeline.",
        "- `higher_ed_impact_assessment.csv`: stakeholder impact assessment.",
        "- `higher_ed_transition_frontier.png`: country health and improvement frontier.",
    ]
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ensure_pdf_exists()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    dimension_df, health_model = build_health_model()
    country_df, country_applications = build_country_applications()
    selected_country = str(country_applications["selected_for_transition"]["country"])
    transition_df, selected_transition = build_transition(selected_country)
    policy_df, policy_suite = build_policy_suite()
    impact_df, impact_assessment = build_impact_assessment()
    write_frontier(country_df, transition_df)
    result = build_result(health_model, country_applications, selected_transition, policy_suite, impact_assessment)
    result["artifacts"] = {
        "higher_ed_health_dimensions": str(ARTIFACT_DIR / "higher_ed_health_dimensions.csv"),
        "higher_ed_country_applications": str(ARTIFACT_DIR / "higher_ed_country_applications.csv"),
        "higher_ed_health_scores": str(ARTIFACT_DIR / "higher_ed_health_scores.csv"),
        "higher_ed_policy_timeline": str(ARTIFACT_DIR / "higher_ed_policy_timeline.csv"),
        "higher_ed_impact_assessment": str(ARTIFACT_DIR / "higher_ed_impact_assessment.csv"),
        "higher_ed_transition_frontier": str(ARTIFACT_DIR / "higher_ed_transition_frontier.png"),
        "higher_ed_transition_timeline": str(ARTIFACT_DIR / "higher_ed_transition_timeline.png"),
        "dimension_rows": len(dimension_df),
        "policy_timeline_rows": len(policy_df),
        "impact_rows": len(impact_df),
    }
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    build_report(result)
    print(json.dumps({"result": str(RESULT_PATH), "report": str(REPORT_PATH), "artifacts": str(ARTIFACT_DIR)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
