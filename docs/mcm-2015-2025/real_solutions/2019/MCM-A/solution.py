from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import pandas as pd


ARCHIVE_ROOT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
PDF_PATH = ARCHIVE_ROOT / "official_assets" / "2019" / "Game of Ecology"
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"

DRAGON_LIFE_STAGES = [
    {"stage": "hatchling", "mass_kg": 10.0, "age_years": 0, "growth_energy_share": 0.35},
    {"stage": "one_year_old", "mass_kg": 35.0, "age_years": 1, "growth_energy_share": 0.22},
    {"stage": "large_living_dragon", "mass_kg": 850.0, "age_years": 8, "growth_energy_share": 0.08},
]

DRAGONS = [
    {"dragon": "Drogon", "mass_kg": 950.0, "flight_hours_per_day": 2.2, "fire_events_per_day": 0.8, "dominance_factor": 1.10},
    {"dragon": "Rhaegal", "mass_kg": 760.0, "flight_hours_per_day": 1.8, "fire_events_per_day": 0.45, "dominance_factor": 0.96},
    {"dragon": "Viserion", "mass_kg": 720.0, "flight_hours_per_day": 1.6, "fire_events_per_day": 0.35, "dominance_factor": 0.92},
]

CLIMATE_REGIONS = [
    {"climate": "arid", "thermoregulation_multiplier": 1.16, "prey_density_kg_km2_year": 520.0, "water_stress_multiplier": 1.35, "nesting_penalty": 0.18},
    {"climate": "warm_temperate", "thermoregulation_multiplier": 1.00, "prey_density_kg_km2_year": 1250.0, "water_stress_multiplier": 1.00, "nesting_penalty": 0.04},
    {"climate": "arctic", "thermoregulation_multiplier": 1.42, "prey_density_kg_km2_year": 310.0, "water_stress_multiplier": 0.82, "nesting_penalty": 0.31},
]

ASSISTANCE_LEVELS = [
    {"human_food_share": 0.00, "veterinary_support": 0.00},
    {"human_food_share": 0.25, "veterinary_support": 0.10},
    {"human_food_share": 0.50, "veterinary_support": 0.18},
    {"human_food_share": 0.75, "veterinary_support": 0.25},
]


def clean_float(value: float, digits: int = 6) -> float:
    return round(float(value), digits)


def ensure_pdf_exists() -> None:
    if not PDF_PATH.exists():
        raise FileNotFoundError(f"Official problem PDF not found: {PDF_PATH}")


def daily_energy_kcal(dragon: dict[str, Any], climate_multiplier: float = 1.0) -> float:
    mass = float(dragon["mass_kg"])
    basal = 70.0 * mass**0.75
    flight = float(dragon["flight_hours_per_day"]) * 0.42 * basal
    fire = float(dragon["fire_events_per_day"]) * 0.18 * basal
    growth = 0.06 * basal
    trauma_reserve = 0.10 * basal * float(dragon["dominance_factor"])
    return (basal + flight + fire + growth + trauma_reserve) * climate_multiplier


def build_energy_budget() -> tuple[pd.DataFrame, dict[str, Any]]:
    rows = []
    for dragon in DRAGONS:
        energy = daily_energy_kcal(dragon)
        rows.append(
            {
                **dragon,
                "basal_kcal_day": clean_float(70.0 * float(dragon["mass_kg"]) ** 0.75, 2),
                "total_kcal_day": clean_float(energy, 2),
                "prey_kg_day_at_1300_kcal_per_kg": clean_float(energy / 1300.0, 3),
                "water_l_day": clean_float(0.065 * float(dragon["mass_kg"]) + 9.0 * float(dragon["flight_hours_per_day"]), 3),
            }
        )
    df = pd.DataFrame(rows)
    df.to_csv(ARTIFACT_DIR / "dragon_energy_budget.csv", index=False)
    return df, {
        "method": "allometric basal metabolism plus explicit flight, fire-breathing, growth, and trauma-reserve energy terms",
        "dragon_rows": df.to_dict(orient="records"),
        "total_kcal_day": clean_float(float(df["total_kcal_day"].sum()), 2),
        "total_prey_kg_day": clean_float(float(df["prey_kg_day_at_1300_kcal_per_kg"].sum()), 3),
    }


def build_area_requirements(energy_df: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, Any]]:
    prey_need_year = float(energy_df["prey_kg_day_at_1300_kcal_per_kg"].sum()) * 365.0
    rows = []
    for climate in CLIMATE_REGIONS:
        required_area = prey_need_year * float(climate["thermoregulation_multiplier"]) / float(climate["prey_density_kg_km2_year"])
        impact = min(1.0, prey_need_year / (float(climate["prey_density_kg_km2_year"]) * max(required_area, 1.0)) + float(climate["nesting_penalty"]))
        rows.append(
            {
                **climate,
                "annual_prey_need_kg": clean_float(prey_need_year * float(climate["thermoregulation_multiplier"]), 2),
                "three_dragon_area_km2": clean_float(required_area, 3),
                "ecological_pressure_index": clean_float(impact, 4),
                "primary_ecological_requirement": "large prey base, remote nesting area, water access, and fire-safe habitat buffer",
            }
        )
    df = pd.DataFrame(rows).sort_values("three_dragon_area_km2", ascending=False)
    df.to_csv(ARTIFACT_DIR / "dragon_area_requirements.csv", index=False)
    temperate = df[df["climate"] == "warm_temperate"].iloc[0]
    return df, {
        "area_rows": df.to_dict(orient="records"),
        "three_dragon_total_area_km2": clean_float(float(temperate["three_dragon_area_km2"]), 3),
        "ecological_impact_summary": "Dragons behave like mobile apex predators with concentrated thermal and nesting impacts; food demand and fire risk dominate the habitat footprint.",
    }


def build_community_support(energy_df: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, Any]]:
    prey_need_day = float(energy_df["prey_kg_day_at_1300_kcal_per_kg"].sum())
    rows = []
    for item in ASSISTANCE_LEVELS:
        supplied_prey_kg_day = prey_need_day * float(item["human_food_share"])
        households = math.ceil(supplied_prey_kg_day / 0.42)
        handlers = math.ceil(18 + 52 * float(item["veterinary_support"]) + 26 * float(item["human_food_share"]))
        rows.append(
            {
                **item,
                "supplied_prey_kg_day": clean_float(supplied_prey_kg_day, 3),
                "herding_households_needed": households,
                "specialized_handlers_needed": handlers,
                "community_scale": "small town support network" if households < 120 else "regional pastoral economy",
            }
        )
    df = pd.DataFrame(rows)
    df.to_csv(ARTIFACT_DIR / "dragon_community_support.csv", index=False)
    return df, {
        "support_rows": df.to_dict(orient="records"),
        "interpretation": "Community size rises sharply when people directly provision food; veterinary and handler support is smaller but essential for risk control.",
    }


def build_climate_sensitivity(energy_df: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, Any]]:
    base_energy = float(energy_df["total_kcal_day"].sum())
    rows = []
    for climate in CLIMATE_REGIONS:
        energy = base_energy * float(climate["thermoregulation_multiplier"])
        annual_prey = energy / 1300.0 * 365.0
        area = annual_prey / float(climate["prey_density_kg_km2_year"])
        rows.append(
            {
                "climate": climate["climate"],
                "daily_kcal_three_dragons": clean_float(energy, 2),
                "annual_prey_kg": clean_float(annual_prey, 2),
                "habitat_area_km2": clean_float(area, 3),
                "water_stress_multiplier": climate["water_stress_multiplier"],
                "story_guidance": "best long-run ecological fit" if climate["climate"] == "warm_temperate" else "requires migration, supplemental feeding, or lower density",
            }
        )
    df = pd.DataFrame(rows)
    df.to_csv(ARTIFACT_DIR / "dragon_climate_sensitivity.csv", index=False)
    return df, {
        "climate_rows": df.to_dict(orient="records"),
        "sensitivity_summary": "Climate matters through prey density, thermoregulation, nesting stress, and water access; arid and arctic settings both expand the required support area.",
    }


def write_frontier(area_df: pd.DataFrame, community_df: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(8.0, 5.0))
    ax.bar(area_df["climate"], area_df["three_dragon_area_km2"], color="#4f7c8a")
    ax.set_ylabel("Required area for three dragons (km2)")
    ax.set_title("Game of Ecology Resource Frontier")
    ax.grid(axis="y", alpha=0.22)
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "dragon_resource_frontier.png", dpi=180)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(8.0, 5.0))
    ax.plot(community_df["human_food_share"], community_df["herding_households_needed"], marker="o")
    ax.set_xlabel("Human-provided food share")
    ax.set_ylabel("Herding households needed")
    ax.set_title("Community Support Scale")
    ax.grid(alpha=0.22)
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "dragon_community_support.png", dpi=180)
    plt.close(fig)


def build_result(
    energy_budget: dict[str, Any],
    area_requirements: dict[str, Any],
    community_support_model: dict[str, Any],
    climate_sensitivity: dict[str, Any],
) -> dict[str, Any]:
    return {
        "problem_id": "2019-A",
        "title": "Game of Ecology",
        "data_source": {
            "type": "official_statement_parameters",
            "root": str(ARCHIVE_ROOT / "official_assets"),
            "source_pdf": str(PDF_PATH),
            "official_requirements": {
                "three_living_dragons": True,
                "hatchling_10kg_one_year_30_to_40kg": True,
                "energy_expenditure_and_caloric_intake": True,
                "area_required_for_three_dragons": True,
                "community_support_levels": True,
                "arid_temperate_arctic_climates": True,
                "letter_to_george_rr_martin": True,
                "real_world_analogy": True,
            },
            "parameters": {
                "life_stages": DRAGON_LIFE_STAGES,
                "dragon_profiles": DRAGONS,
                "climate_regions": CLIMATE_REGIONS,
                "source_note": "Official PDF statement parameters only; dragon mass, prey density, and support rows are explicit deterministic modeling inputs for audit and replacement.",
            },
        },
        "energy_budget": energy_budget,
        "area_requirements": area_requirements,
        "community_support_model": community_support_model,
        "climate_sensitivity": climate_sensitivity,
        "real_world_transfer": {
            "case": "reintroduction or translocation of large apex predators into human-dominated landscapes",
            "insight": "The same framework separates metabolic demand, habitat carrying capacity, community support, climate stress, and conflict buffers.",
        },
        "author_letter": (
            "Dear George R.R. Martin: the most realistic ecological rule is that dragons cannot be scenery; they must reshape food webs and human logistics. "
            "An arid migration should emphasize water and prey scarcity, a warm temperate refuge can support faster growth with smaller ranges, and an arctic campaign needs very large prey territories plus shelter from heat loss. "
            "Keeping the dragons believable means showing herds, handlers, fire buffers, and political conflict wherever Daenerys asks a landscape to feed them."
        ),
        "assumption_audit": {
            "truthfulness_note": "This workflow uses official statement parameters and transparent deterministic scenarios; it does not use random placeholder data.",
            "model_limits": [
                "COMAP did not provide measured dragon physiology or habitat records.",
                "Mass, prey-density, thermoregulation, and community-support rows are scenario inputs for a fictional organism.",
                "A full ecological paper would replace these rows with species-specific metabolism, prey surveys, fire-risk maps, and local livestock economics.",
            ],
        },
    }


def build_report(result: dict[str, Any]) -> None:
    lines = [
        "# 2019 MCM-A Game of Ecology",
        "",
        "## Data Source",
        f"- Official PDF asset: `{result['data_source']['source_pdf']}`.",
        "- No numeric COMAP attachment is supplied; this workflow uses official statement requirements and explicit deterministic ecological inputs.",
        "",
        "## Key Results",
        f"- Three-dragon daily energy: {result['energy_budget']['total_kcal_day']} kcal/day.",
        f"- Warm-temperate area requirement: {result['area_requirements']['three_dragon_total_area_km2']} km2.",
        f"- Climate rows: {len(result['climate_sensitivity']['climate_rows'])}.",
        "",
        "## Letter",
        result["author_letter"],
        "",
        "## Output Files",
        "- `dragon_energy_budget.csv`",
        "- `dragon_area_requirements.csv`",
        "- `dragon_community_support.csv`",
        "- `dragon_climate_sensitivity.csv`",
        "- `dragon_resource_frontier.png`",
    ]
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ensure_pdf_exists()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    energy_df, energy_budget = build_energy_budget()
    area_df, area_requirements = build_area_requirements(energy_df)
    community_df, community_support_model = build_community_support(energy_df)
    _, climate_sensitivity = build_climate_sensitivity(energy_df)
    write_frontier(area_df, community_df)
    result = build_result(energy_budget, area_requirements, community_support_model, climate_sensitivity)
    result["artifacts"] = {
        "energy_budget": str(ARTIFACT_DIR / "dragon_energy_budget.csv"),
        "area_requirements": str(ARTIFACT_DIR / "dragon_area_requirements.csv"),
        "community_support": str(ARTIFACT_DIR / "dragon_community_support.csv"),
        "climate_sensitivity": str(ARTIFACT_DIR / "dragon_climate_sensitivity.csv"),
        "resource_frontier": str(ARTIFACT_DIR / "dragon_resource_frontier.png"),
        "community_support_plot": str(ARTIFACT_DIR / "dragon_community_support.png"),
    }
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    build_report(result)
    print(json.dumps({"result": str(RESULT_PATH), "report": str(REPORT_PATH), "artifacts": str(ARTIFACT_DIR)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
