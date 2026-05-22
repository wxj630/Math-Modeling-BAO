from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ARCHIVE_ROOT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
PDF_PATH = ARCHIVE_ROOT / "official_assets_extracted" / "2023" / "Light Pollution.pdf"
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"

LOCATION_TYPES = ["protected_land", "rural", "suburban", "urban"]
RISK_SCALE = "0-100"

OFFICIAL_REQUIREMENTS = {
    "four_location_types": LOCATION_TYPES,
    "phenomena": ["light trespass", "over-illumination", "light clutter", "sky glow", "glare"],
    "concerns": ["human health", "safety", "wildlife migration", "plant maturation", "night sky visibility"],
    "intervention_count_required": 3,
    "promotion_flyer_required": True,
}

LOCATION_SCENARIOS = [
    {
        "location_type": "protected_land",
        "example_location": "dark-sky sensitive protected habitat",
        "development_level": 0.12,
        "population_pressure": 0.08,
        "biodiversity_sensitivity": 0.94,
        "geography_exposure": 0.36,
        "climate_clear_sky_factor": 0.74,
        "baseline_lighting_intensity": 0.18,
        "safety_need": 0.20,
    },
    {
        "location_type": "rural",
        "example_location": "low-density agricultural village",
        "development_level": 0.28,
        "population_pressure": 0.22,
        "biodiversity_sensitivity": 0.70,
        "geography_exposure": 0.44,
        "climate_clear_sky_factor": 0.66,
        "baseline_lighting_intensity": 0.32,
        "safety_need": 0.36,
    },
    {
        "location_type": "suburban",
        "example_location": "residential-commercial edge community",
        "development_level": 0.64,
        "population_pressure": 0.58,
        "biodiversity_sensitivity": 0.48,
        "geography_exposure": 0.55,
        "climate_clear_sky_factor": 0.54,
        "baseline_lighting_intensity": 0.66,
        "safety_need": 0.62,
    },
    {
        "location_type": "urban",
        "example_location": "dense mixed-use city district",
        "development_level": 0.92,
        "population_pressure": 0.88,
        "biodiversity_sensitivity": 0.30,
        "geography_exposure": 0.70,
        "climate_clear_sky_factor": 0.42,
        "baseline_lighting_intensity": 0.94,
        "safety_need": 0.86,
    },
]

INTERVENTIONS = [
    {
        "strategy": "shielded warm-spectrum fixtures",
        "specific_actions": "replace unshielded lamps, require full cutoff optics, shift to warmer color temperature",
        "sky_glow_reduction": 0.30,
        "trespass_reduction": 0.34,
        "clutter_reduction": 0.18,
        "safety_penalty": 0.02,
        "cost_index": 0.46,
        "implementation_feasibility": 0.82,
    },
    {
        "strategy": "adaptive dimming and curfew controls",
        "specific_actions": "dim after peak activity, use motion sensors, turn off decorative lighting overnight",
        "sky_glow_reduction": 0.38,
        "trespass_reduction": 0.26,
        "clutter_reduction": 0.24,
        "safety_penalty": 0.07,
        "cost_index": 0.36,
        "implementation_feasibility": 0.76,
    },
    {
        "strategy": "zoning ordinance and sign-lighting limits",
        "specific_actions": "set lumen caps by district, restrict upward signage, enforce lighting permits",
        "sky_glow_reduction": 0.27,
        "trespass_reduction": 0.22,
        "clutter_reduction": 0.42,
        "safety_penalty": 0.04,
        "cost_index": 0.24,
        "implementation_feasibility": 0.68,
    },
    {
        "strategy": "habitat buffer dark corridor",
        "specific_actions": "create no-light buffers near habitat, shield road edges, preserve migration corridors",
        "sky_glow_reduction": 0.24,
        "trespass_reduction": 0.40,
        "clutter_reduction": 0.18,
        "safety_penalty": 0.09,
        "cost_index": 0.52,
        "implementation_feasibility": 0.62,
    },
]


def clean_float(value: float, digits: int = 6) -> float:
    return round(float(value), digits)


def ensure_pdf_exists() -> None:
    if not PDF_PATH.exists():
        raise FileNotFoundError(f"Official problem PDF not found: {PDF_PATH}")


def risk_score(location: dict[str, float | str]) -> dict[str, float | str]:
    intensity = float(location["baseline_lighting_intensity"])
    development = float(location["development_level"])
    population = float(location["population_pressure"])
    biodiversity = float(location["biodiversity_sensitivity"])
    geography = float(location["geography_exposure"])
    climate = float(location["climate_clear_sky_factor"])
    safety_need = float(location["safety_need"])
    sky_glow = intensity * (0.55 * development + 0.30 * population + 0.15 * climate)
    ecological_exposure = intensity * (0.64 * biodiversity + 0.22 * geography + 0.14 * climate)
    human_health = intensity * (0.48 * population + 0.30 * development + 0.22 * (1.0 - safety_need))
    safety_glare = intensity * (0.42 * development + 0.38 * population + 0.20 * geography)
    night_sky_loss = intensity * (0.52 * climate + 0.30 * geography + 0.18 * development)
    total = 100.0 * (0.24 * sky_glow + 0.25 * ecological_exposure + 0.20 * human_health + 0.16 * safety_glare + 0.15 * night_sky_loss)
    return {
        **location,
        "sky_glow_component": clean_float(sky_glow, 4),
        "ecological_component": clean_float(ecological_exposure, 4),
        "human_health_component": clean_float(human_health, 4),
        "safety_glare_component": clean_float(safety_glare, 4),
        "night_sky_loss_component": clean_float(night_sky_loss, 4),
        "light_pollution_risk_score": clean_float(total, 2),
        "risk_level": "low" if total < 25 else "moderate" if total < 45 else "high" if total < 70 else "severe",
    }


def build_location_assessment() -> tuple[pd.DataFrame, dict[str, object]]:
    rows = [risk_score(location) for location in LOCATION_SCENARIOS]
    df = pd.DataFrame(rows)
    df.to_csv(ARTIFACT_DIR / "location_risk_scores.csv", index=False)
    return df, {
        "locations": df.to_dict(orient="records"),
        "interpretation": "The same lighting intensity can be high-risk in protected land because biodiversity sensitivity is high, while urban risk is driven by intensity, clutter, glare, and population exposure.",
    }


def build_interventions(location_df: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, object]]:
    rows = []
    for intervention in INTERVENTIONS:
        ecological_benefit = 0.34 * intervention["sky_glow_reduction"] + 0.38 * intervention["trespass_reduction"] + 0.28 * intervention["clutter_reduction"]
        human_benefit = 0.30 * intervention["sky_glow_reduction"] + 0.25 * intervention["trespass_reduction"] + 0.30 * intervention["clutter_reduction"] - 0.15 * intervention["safety_penalty"]
        total_value = 0.42 * ecological_benefit + 0.32 * human_benefit + 0.16 * intervention["implementation_feasibility"] - 0.10 * intervention["cost_index"]
        rows.append({**intervention, "ecological_benefit": clean_float(ecological_benefit, 4), "human_benefit": clean_float(human_benefit, 4), "strategy_value_score": clean_float(total_value, 4)})
    df = pd.DataFrame(rows).sort_values("strategy_value_score", ascending=False)
    df.to_csv(ARTIFACT_DIR / "intervention_strategy_scores.csv", index=False)
    return df, {
        "intervention_strategy_scores": df.to_dict(orient="records"),
        "general_impacts": [
            "Shielding and warm spectrum reduce sky glow and ecological disruption without a major safety penalty.",
            "Adaptive dimming gives the strongest nighttime intensity reduction but must protect pedestrian and traffic safety.",
            "Zoning and sign limits reduce clutter and over-illumination at low public cost but require enforcement capacity.",
        ],
    }


def apply_intervention(location: pd.Series, intervention: pd.Series) -> dict[str, object]:
    reduction = (
        0.30 * float(intervention["sky_glow_reduction"])
        + 0.28 * float(intervention["trespass_reduction"])
        + 0.22 * float(intervention["clutter_reduction"])
        - 0.10 * float(intervention["safety_penalty"])
        + 0.10 * float(intervention["implementation_feasibility"])
    )
    risk_before = float(location["light_pollution_risk_score"])
    risk_after = risk_before * max(0.30, 1.0 - reduction)
    return {
        "location_type": location["location_type"],
        "strategy": intervention["strategy"],
        "risk_before": clean_float(risk_before, 2),
        "risk_after": clean_float(risk_after, 2),
        "risk_reduction_points": clean_float(risk_before - risk_after, 2),
        "specific_actions": intervention["specific_actions"],
    }


def select_strategies(location_df: pd.DataFrame, intervention_df: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, object]]:
    selected_types = ["protected_land", "urban"]
    rows = []
    for location_type in selected_types:
        location = location_df[location_df["location_type"] == location_type].iloc[0]
        best = None
        for _, intervention in intervention_df.iterrows():
            candidate = apply_intervention(location, intervention)
            if best is None or candidate["risk_after"] < best["risk_after"]:
                best = candidate
        rows.append(best)
    df = pd.DataFrame(rows)
    df.to_csv(ARTIFACT_DIR / "selected_intervention_impacts.csv", index=False)
    plt.figure(figsize=(8, 5))
    plt.bar(location_df["location_type"], location_df["light_pollution_risk_score"], color="#4C78A8", label="baseline risk")
    for _, row in df.iterrows():
        x = list(location_df["location_type"]).index(row["location_type"])
        plt.scatter([x], [row["risk_after"]], color="#E15759", s=90, zorder=3, label="after selected intervention" if x == 0 else None)
    plt.ylabel("Light pollution risk score (0-100)")
    plt.title("Light pollution risk and selected mitigation impacts")
    plt.legend()
    plt.tight_layout()
    plt.savefig(ARTIFACT_DIR / "light_pollution_risk_frontier.png", dpi=180)
    plt.close()
    return df, {
        "selected_locations": df.to_dict(orient="records"),
        "selection_rule": "choose the strategy with the lowest post-intervention risk while including safety penalty and feasibility",
    }


def write_report(result: dict[str, object]) -> None:
    metric = result["risk_metric"]["light_pollution_risk_metric"]
    lines = [
        "# 2023 ICM-E Light Pollution",
        "",
        "## Official Statement Basis",
        "- Source: `Light Pollution.pdf`.",
        "- Official prompt requires a broadly applicable risk metric, four location types, three intervention strategies, two selected-location applications, and a one-page flyer.",
        "- No COMAP numeric attachment is provided; location profiles and intervention coefficients are deterministic scenario assumptions.",
        "",
        "## Metric",
        f"- Scale: {metric['scale']}.",
        f"- Formula: {metric['formula']}.",
        "- Tutorial model references: comprehensive evaluation, sensitivity analysis, and policy optimization from `/Users/wuxiaojun/code/My-Agent/intro-mathmodel`.",
        "",
        "## Flyer",
        result["promotion_flyer"],
    ]
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ensure_pdf_exists()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    location_df, location_assessment = build_location_assessment()
    intervention_df, intervention_model = build_interventions(location_df)
    selected_df, strategy_selection = select_strategies(location_df, intervention_df)
    result = {
        "problem_id": "2023-E",
        "title": "Light Pollution",
        "data_source": {
            "type": "official_statement_parameters",
            "root": str(ARCHIVE_ROOT),
            "source_pdf": str(PDF_PATH),
            "official_requirements": OFFICIAL_REQUIREMENTS,
            "scenario_assumption_note": "Location profiles, weights, intervention reductions, costs, and feasibility values are deterministic assumptions for reproducible experiments; they are not observed field measurements.",
        },
        "risk_metric": {
            "light_pollution_risk_metric": {
                "scale": RISK_SCALE,
                "formula": "100*(0.24*sky_glow + 0.25*ecological + 0.20*human_health + 0.16*safety_glare + 0.15*night_sky_loss)",
                "components": ["sky_glow", "ecological_exposure", "human_health", "safety_glare", "night_sky_loss"],
                "human_and_nonhuman_balance": "Ecological sensitivity and human exposure receive comparable total weight, matching the prompt's human and non-human concerns.",
            }
        },
        "location_assessment": location_assessment,
        "intervention_model": intervention_model,
        "strategy_selection": strategy_selection,
        "promotion_flyer": "Flyer: Protect the Night, Keep the Light. Use shielded warm lights, dim lights after peak hours, and cap sign lighting. This lowers sky glow, protects wildlife migration and plant cycles, improves sleep, and keeps necessary safety lighting where people need it.",
    }
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_report(result)
    print(f"wrote {RESULT_PATH}")
    print(f"wrote {REPORT_PATH}")
    print(f"wrote artifacts under {ARTIFACT_DIR}")


if __name__ == "__main__":
    main()
