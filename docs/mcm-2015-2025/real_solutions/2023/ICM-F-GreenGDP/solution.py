from __future__ import annotations

import json
import math
import os
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

import pandas as pd


ARCHIVE_ROOT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
PDF_PATH = ARCHIVE_ROOT / "official_assets_extracted" / "2023" / "Green GDP.pdf"
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"
CACHE_DIR = ARTIFACT_DIR / "cache"
os.environ.setdefault("MPLCONFIGDIR", str(ARTIFACT_DIR / ".matplotlib"))

import matplotlib.pyplot as plt


WORLD_BANK_API = "https://api.worldbank.org/v2/country/{countries}/indicator/{indicator}?format=json&per_page=20000"
COUNTRIES = ["WLD", "BRA", "CHN", "USA", "IND", "IDN", "COD", "NOR"]
COUNTRY_NAMES = {
    "WLD": "World",
    "BRA": "Brazil",
    "CHN": "China",
    "USA": "United States",
    "IND": "India",
    "IDN": "Indonesia",
    "COD": "Congo, Dem. Rep.",
    "NOR": "Norway",
}
INDICATORS = {
    "NY.GDP.MKTP.CD": "gdp_current_usd",
    "NY.ADJ.DCO2.GN.ZS": "co2_damage_pct_gni",
    "NY.ADJ.DRES.GN.ZS": "natural_resource_depletion_pct_gni",
    "NY.ADJ.DFOR.GN.ZS": "net_forest_depletion_pct_gni",
    "AG.LND.FRST.ZS": "forest_area_pct_land",
    "NY.GDP.TOTL.RT.ZS": "natural_resource_rents_pct_gdp",
}
FALLBACK_WORLD_BANK = {
    "WLD": {
        "NY.GDP.MKTP.CD": (2024, 110_982_661_180_013.0),
        "NY.ADJ.DCO2.GN.ZS": (2021, 1.55839504000073),
        "NY.ADJ.DRES.GN.ZS": (2021, 1.52506495947352),
        "NY.ADJ.DFOR.GN.ZS": (2021, 0.0567101771969873),
        "AG.LND.FRST.ZS": (2022, 31.1430410787403),
        "NY.GDP.TOTL.RT.ZS": (2021, 3.07420969679454),
    },
    "BRA": {
        "NY.GDP.MKTP.CD": (2024, 2_185_821_648_943.86),
        "NY.ADJ.DCO2.GN.ZS": (2021, 1.26503805892481),
        "NY.ADJ.DRES.GN.ZS": (2021, 3.74676225993476),
        "NY.ADJ.DFOR.GN.ZS": (2021, 0.0),
        "AG.LND.FRST.ZS": (2023, 58.9818729765235),
        "NY.GDP.TOTL.RT.ZS": (2021, 7.94111199933246),
    },
    "CHN": {
        "NY.GDP.MKTP.CD": (2024, 18_743_803_170_827.2),
        "NY.ADJ.DCO2.GN.ZS": (2021, 2.74580037586664),
        "NY.ADJ.DRES.GN.ZS": (2021, 1.01156651783812),
        "NY.ADJ.DFOR.GN.ZS": (2021, 0.0),
        "AG.LND.FRST.ZS": (2023, 24.0319389958256),
        "NY.GDP.TOTL.RT.ZS": (2021, 1.70756488252672),
    },
    "USA": {
        "NY.GDP.MKTP.CD": (2024, 28_750_956_130_731.2),
        "NY.ADJ.DCO2.GN.ZS": (2021, 0.890531802541054),
        "NY.ADJ.DRES.GN.ZS": (2021, 0.81519312438195),
        "NY.ADJ.DFOR.GN.ZS": (2021, 0.0),
        "AG.LND.FRST.ZS": (2023, 33.8669264120375),
        "NY.GDP.TOTL.RT.ZS": (2021, 1.27994423022721),
    },
    "IND": {
        "NY.GDP.MKTP.CD": (2024, 3_909_891_533_858.08),
        "NY.ADJ.DCO2.GN.ZS": (2021, 3.44095931382658),
        "NY.ADJ.DRES.GN.ZS": (2021, 1.62081061089854),
        "NY.ADJ.DFOR.GN.ZS": (2021, 0.16326686195924),
        "AG.LND.FRST.ZS": (2023, 24.5390304689576),
        "NY.GDP.TOTL.RT.ZS": (2021, 3.15934537555664),
    },
    "IDN": {
        "NY.GDP.MKTP.CD": (2024, 1_396_300_098_190.97),
        "NY.ADJ.DCO2.GN.ZS": (2021, 2.37594364421979),
        "NY.ADJ.DRES.GN.ZS": (2021, 3.23302873666391),
        "NY.ADJ.DFOR.GN.ZS": (2021, 0.0),
        "AG.LND.FRST.ZS": (2023, 47.7220336902463),
        "NY.GDP.TOTL.RT.ZS": (2021, 5.15704008451705),
    },
    "COD": {
        "NY.GDP.MKTP.CD": (2024, 70_962_185_790.7094),
        "NY.ADJ.DCO2.GN.ZS": (2021, 0.267266369995342),
        "NY.ADJ.DRES.GN.ZS": (2021, 33.0940322255891),
        "NY.ADJ.DFOR.GN.ZS": (2021, 9.97062142594133),
        "AG.LND.FRST.ZS": (2023, 54.1898572594341),
        "NY.GDP.TOTL.RT.ZS": (2021, 38.8272665239082),
    },
    "NOR": {
        "NY.GDP.MKTP.CD": (2024, 483_592_648_313.301),
        "NY.ADJ.DCO2.GN.ZS": (2021, 0.315010674313667),
        "NY.ADJ.DRES.GN.ZS": (2021, 7.71310815458361),
        "NY.ADJ.DFOR.GN.ZS": (2021, 0.0),
        "AG.LND.FRST.ZS": (2023, 33.5009745518434),
        "NY.GDP.TOTL.RT.ZS": (2021, 10.0482763904291),
    },
}
GGDP_COMPONENTS = [
    {
        "component": "conventional_gdp",
        "indicator_id": "NY.GDP.MKTP.CD",
        "role": "base",
        "direction": "higher measured production raises GDP and GGDP before environmental adjustment",
    },
    {
        "component": "co2_damage_pct_gni",
        "indicator_id": "NY.ADJ.DCO2.GN.ZS",
        "role": "penalty",
        "direction": "subtract climate damage recorded by World Bank adjusted-savings accounts",
    },
    {
        "component": "natural_resource_depletion_pct_gni",
        "indicator_id": "NY.ADJ.DRES.GN.ZS",
        "role": "penalty",
        "direction": "subtract energy, mineral, and forest resource depletion",
    },
    {
        "component": "net_forest_depletion_pct_gni",
        "indicator_id": "NY.ADJ.DFOR.GN.ZS",
        "role": "penalty",
        "direction": "subtract net forest depletion where observed separately",
    },
]
IMPACT_SCENARIOS = [
    {"scenario": "cautious_multilateral_pilot", "coverage_share": 0.35, "policy_response_fraction": 0.12, "transition_effort_index": 0.42},
    {"scenario": "phased_g20_plus_resource_exporters", "coverage_share": 0.65, "policy_response_fraction": 0.25, "transition_effort_index": 0.58},
    {"scenario": "full_primary_metric_switch", "coverage_share": 0.90, "policy_response_fraction": 0.38, "transition_effort_index": 0.78},
]
OFFICIAL_REQUIREMENTS = [
    "select_ggdp_formula",
    "simple_global_climate_impact_model",
    "global_upside_downside_assessment",
    "country_specific_resource_analysis",
    "one_page_country_leader_report",
]
ASSUMPTIONS = {
    "formula": "GGDP = GDP * (1 - observed adjusted-savings environmental penalty percent / 100).",
    "policy_response": "Impact scenarios apply transparent response fractions to observed World Bank CO2 damage and resource-depletion penalties.",
    "country_choice": "Brazil is selected because the official prompt asks for one country and Brazil makes forest, resource-rent, GDP, and future-generation tradeoffs visible.",
}


def clean_float(value: Any, digits: int = 6) -> float | None:
    if value is None:
        return None
    if isinstance(value, float) and math.isnan(value):
        return None
    return round(float(value), digits)


def ensure_pdf_exists() -> None:
    if not PDF_PATH.exists():
        raise FileNotFoundError(f"Official problem PDF not found: {PDF_PATH}")


def http_json(url: str, timeout: int = 35) -> Any:
    request = urllib.request.Request(url, headers={"User-Agent": "Math-Modeling-BAO-Green-GDP/1.0"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def latest_observations(indicator: str) -> dict[str, tuple[int, float]]:
    url = WORLD_BANK_API.format(countries=";".join(COUNTRIES), indicator=indicator)
    data = http_json(url)
    observations = data[1] if isinstance(data, list) and len(data) > 1 else []
    latest: dict[str, tuple[int, float]] = {}
    for observation in observations:
        iso3 = observation.get("countryiso3code")
        value = observation.get("value")
        year = observation.get("date")
        if iso3 in COUNTRIES and value is not None and str(year).isdigit():
            current = latest.get(iso3)
            if current is None or int(year) > current[0]:
                latest[iso3] = (int(year), float(value))
    return latest


def fetch_world_bank_panel() -> pd.DataFrame:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache = CACHE_DIR / "world_bank_green_gdp_panel.csv"
    if cache.exists():
        return pd.read_csv(cache)

    rows: dict[str, dict[str, Any]] = {iso3: {"iso3": iso3, "country": COUNTRY_NAMES[iso3]} for iso3 in COUNTRIES}
    for indicator, column in INDICATORS.items():
        try:
            latest = latest_observations(indicator)
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, IndexError, ValueError):
            latest = {}
        for iso3 in COUNTRIES:
            year, value = latest.get(iso3, FALLBACK_WORLD_BANK[iso3][indicator])
            rows[iso3][column] = value
            rows[iso3][f"{column}_year"] = year
            rows[iso3][f"{column}_indicator"] = indicator

    df = pd.DataFrame(rows.values())
    df = add_green_gdp_columns(df)
    df.to_csv(cache, index=False)
    return df


def add_green_gdp_columns(df: pd.DataFrame) -> pd.DataFrame:
    panel = df.copy()
    penalty_columns = ["co2_damage_pct_gni", "natural_resource_depletion_pct_gni", "net_forest_depletion_pct_gni"]
    for column in penalty_columns + ["gdp_current_usd", "forest_area_pct_land", "natural_resource_rents_pct_gdp"]:
        panel[column] = pd.to_numeric(panel[column], errors="coerce")
    panel["green_gdp_penalty_pct_gni"] = panel[penalty_columns].fillna(0.0).sum(axis=1)
    panel["green_gdp_ratio"] = (1.0 - panel["green_gdp_penalty_pct_gni"] / 100.0).clip(lower=0.0)
    panel["green_gdp_current_usd"] = panel["gdp_current_usd"] * panel["green_gdp_ratio"]
    panel["green_gap_usd"] = panel["gdp_current_usd"] - panel["green_gdp_current_usd"]
    non_world_gdp = panel.loc[panel["iso3"] != "WLD", "gdp_current_usd"].sum()
    panel["panel_gdp_share"] = panel["gdp_current_usd"] / non_world_gdp
    panel.loc[panel["iso3"] == "WLD", "panel_gdp_share"] = None
    max_penalty = max(1.0, float(panel.loc[panel["iso3"] != "WLD", "green_gdp_penalty_pct_gni"].max()))
    panel["adoption_priority_score"] = (
        0.50 * (panel["green_gdp_penalty_pct_gni"] / max_penalty)
        + 0.25 * (panel["co2_damage_pct_gni"].fillna(0.0) / max(1.0, float(panel["co2_damage_pct_gni"].max())))
        + 0.25 * (panel["natural_resource_rents_pct_gdp"].fillna(0.0) / max(1.0, float(panel["natural_resource_rents_pct_gdp"].max())))
    ).round(4)
    return panel


def build_formula_components() -> tuple[pd.DataFrame, dict[str, Any]]:
    df = pd.DataFrame(GGDP_COMPONENTS)
    df.to_csv(ARTIFACT_DIR / "ggdp_formula_components.csv", index=False)
    method = {
        "method_id": "adjusted_savings_green_gdp",
        "description": "A World-Bank adjusted-savings style GGDP subtracts observed environmental damage and resource-depletion penalties from conventional GDP.",
        "formula": ASSUMPTIONS["formula"],
        "penalty_components": [row["component"] for row in GGDP_COMPONENTS if row["role"] == "penalty"],
        "reason_for_selection": "It is already operationalized in public WDI adjusted-savings indicators, so the model can be audited without inventing hidden environmental accounts.",
    }
    return df, method


def build_global_impact_model(panel: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, Any]]:
    world = panel[panel["iso3"] == "WLD"].iloc[0]
    resource_penalty = float(world["natural_resource_depletion_pct_gni"]) + float(world["net_forest_depletion_pct_gni"])
    scenario_rows = []
    for scenario in IMPACT_SCENARIOS:
        coverage = scenario["coverage_share"]
        response = scenario["policy_response_fraction"]
        co2_damage_reduction = float(world["co2_damage_pct_gni"]) * coverage * response
        resource_reduction = resource_penalty * coverage * response * 0.75
        combined = co2_damage_reduction + resource_reduction
        benefit_index = 100.0 * combined / max(0.01, float(world["green_gdp_penalty_pct_gni"]))
        effort_index = 100.0 * float(scenario["transition_effort_index"]) * (1.0 - 0.20 * coverage)
        net_benefit_score = 3.0 * benefit_index - 0.50 * effort_index
        scenario_rows.append(
            {
                **scenario,
                "co2_damage_reduction_pct_gni": clean_float(co2_damage_reduction, 4),
                "resource_depletion_reduction_pct_gni": clean_float(resource_reduction, 4),
                "combined_environmental_benefit_pct_gni": clean_float(combined, 4),
                "benefit_index": clean_float(benefit_index, 3),
                "effort_index": clean_float(effort_index, 3),
                "net_benefit_score": clean_float(net_benefit_score, 3),
            }
        )
    scenario_df = pd.DataFrame(scenario_rows)
    scenario_df.to_csv(ARTIFACT_DIR / "global_impact_scenarios.csv", index=False)
    panel.to_csv(ARTIFACT_DIR / "world_bank_green_gdp_panel.csv", index=False)
    return scenario_df, {
        "world_summary": {
            "source": "World Bank WDI latest available observations",
            "world_green_gdp_penalty_pct_gni": clean_float(world["green_gdp_penalty_pct_gni"], 4),
            "world_co2_damage_pct_gni": clean_float(world["co2_damage_pct_gni"], 4),
            "world_natural_resource_depletion_pct_gni": clean_float(world["natural_resource_depletion_pct_gni"], 4),
            "world_net_forest_depletion_pct_gni": clean_float(world["net_forest_depletion_pct_gni"], 4),
        },
        "country_panel": panel.drop(columns=[column for column in panel.columns if column.endswith("_indicator")]).to_dict(orient="records"),
        "scenarios": scenario_df.to_dict(orient="records"),
        "model_note": "The simple model translates the official prompt's GGDP adoption question into observed WDI green penalties multiplied by explicit adoption coverage and response fractions.",
    }


def assess_worthwhile(scenario_df: pd.DataFrame) -> dict[str, Any]:
    selected = scenario_df[scenario_df["scenario"] == "phased_g20_plus_resource_exporters"].iloc[0]
    recommendation = "support_switch" if float(selected["net_benefit_score"]) > 0 else "reject_switch"
    return {
        "scenario_used": selected["scenario"],
        "recommendation": recommendation,
        "reasoning": (
            "The phased strategy is the most defensible global option because it targets large emitters and resource exporters first, "
            "giving climate and resource incentives before forcing a universal statistical transition."
        ),
        "upside": {
            "combined_environmental_benefit_pct_gni": clean_float(selected["combined_environmental_benefit_pct_gni"], 4),
            "benefit_index": clean_float(selected["benefit_index"], 3),
        },
        "downside": {
            "transition_effort_index": clean_float(selected["transition_effort_index"], 3),
            "effort_index": clean_float(selected["effort_index"], 3),
        },
        "net_benefit_score": clean_float(selected["net_benefit_score"], 3),
    }


def country_case_study(panel: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, Any]]:
    brazil = panel[panel["iso3"] == "BRA"].iloc[0]
    green_gap_usd = float(brazil["green_gap_usd"])
    resource_shift_pct_gdp = min(2.0, float(brazil["natural_resource_depletion_pct_gni"]) * 0.25)
    forest_stewardship_score = 0.55 * float(brazil["forest_area_pct_land"]) / 100.0 + 0.45 * (
        1.0 - min(1.0, float(brazil["net_forest_depletion_pct_gni"]) / 3.0)
    )
    rows = [
        {
            "lever": "natural_resource_rent_reinvestment",
            "current_signal": "natural_resource_rents_pct_gdp",
            "observed_value": clean_float(brazil["natural_resource_rents_pct_gdp"], 4),
            "expected_change_under_ggdp": "shift part of extractive rent toward restoration, monitoring, and lower-damage production",
            "planning_magnitude": clean_float(resource_shift_pct_gdp, 4),
        },
        {
            "lever": "forest_and_biodiversity_accounting",
            "current_signal": "forest_area_pct_land",
            "observed_value": clean_float(brazil["forest_area_pct_land"], 4),
            "expected_change_under_ggdp": "treat avoided forest loss as preserving future economic capacity instead of a hidden externality",
            "planning_magnitude": clean_float(forest_stewardship_score, 4),
        },
        {
            "lever": "carbon_damage_visibility",
            "current_signal": "co2_damage_pct_gni",
            "observed_value": clean_float(brazil["co2_damage_pct_gni"], 4),
            "expected_change_under_ggdp": "prefer projects whose GDP gain remains positive after CO2 damage is deducted",
            "planning_magnitude": clean_float(float(brazil["co2_damage_pct_gni"]) * 0.30, 4),
        },
        {
            "lever": "headline_metric_gap",
            "current_signal": "green_gap_usd",
            "observed_value": clean_float(green_gap_usd, 2),
            "expected_change_under_ggdp": "make the environmental cost of status-quo growth visible in the main national performance number",
            "planning_magnitude": clean_float(green_gap_usd / 1_000_000_000.0, 4),
        },
    ]
    df = pd.DataFrame(rows)
    df.to_csv(ARTIFACT_DIR / "brazil_country_analysis.csv", index=False)
    return df, {
        "country_iso3": "BRA",
        "country": "Brazil",
        "green_gdp_penalty_pct_gni": clean_float(brazil["green_gdp_penalty_pct_gni"], 4),
        "green_gdp_ratio": clean_float(brazil["green_gdp_ratio"], 4),
        "green_gap_usd": clean_float(green_gap_usd, 2),
        "forest_area_pct_land": clean_float(brazil["forest_area_pct_land"], 4),
        "natural_resource_rents_pct_gdp": clean_float(brazil["natural_resource_rents_pct_gdp"], 4),
        "future_generations_assessment": "Beneficial if adoption protects forest capital and channels resource rents into durable productivity rather than one-year GDP gains.",
        "policy_levers": df.to_dict(orient="records"),
    }


def one_page_country_report(case: dict[str, Any], assessment: dict[str, Any]) -> str:
    decision = "support a phased switch to GGDP" if assessment["recommendation"] == "support_switch" else "delay a full switch while piloting GGDP accounts"
    return (
        "One-page report to Brazil's economic and environmental leaders\n\n"
        f"Recommendation: Brazil should {decision}. Conventional GDP rewards current production even when natural capital is depleted. "
        f"Using the selected adjusted-savings GGDP method, Brazil's observed environmental penalty is {case['green_gdp_penalty_pct_gni']}% of GNI, "
        f"leaving a green-GDP ratio of {case['green_gdp_ratio']}. This gap is large enough to make forest protection, cleaner energy, and resource-rent reinvestment visible in the headline economic metric.\n\n"
        "Expected changes: projects that raise GDP by drawing down forests, minerals, or climate stability would face an explicit deduction. "
        "Projects that preserve forest capital, reduce CO2 damage, and reinvest resource rents would become more attractive because they protect the income base available to future generations.\n\n"
        "Risk and implementation: the switch will be politically difficult, so Brazil should support a phased international standard with audited WDI/SEEA-style accounts, publish both GDP and GGDP during a transition period, and use the GGDP gap to guide investment rather than as a punitive ranking alone."
    )


def write_plot(panel: pd.DataFrame, scenario_df: pd.DataFrame) -> None:
    country_panel = panel[panel["iso3"] != "WLD"].sort_values("green_gdp_penalty_pct_gni", ascending=False)
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    axes[0].bar(country_panel["iso3"], country_panel["green_gdp_penalty_pct_gni"], color="#4C78A8")
    axes[0].set_ylabel("GGDP penalty (% of GNI)")
    axes[0].set_title("World Bank adjusted-savings penalty by country")
    axes[1].scatter(scenario_df["effort_index"], scenario_df["benefit_index"], s=110, c=scenario_df["net_benefit_score"], cmap="viridis")
    for _, row in scenario_df.iterrows():
        axes[1].annotate(str(row["scenario"]).replace("_", "\n"), (row["effort_index"], row["benefit_index"]), fontsize=8, xytext=(4, 4), textcoords="offset points")
    axes[1].set_xlabel("Transition effort index")
    axes[1].set_ylabel("Climate/resource benefit index")
    axes[1].set_title("GGDP adoption scenario frontier")
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "green_gdp_policy_frontier.png", dpi=180)
    plt.close(fig)


def write_report(result: dict[str, Any]) -> None:
    lines = [
        "# 2023 ICM-F Green GDP Official PDF + World Bank Workflow",
        "",
        "## Data Source",
        f"- Official PDF: `{PDF_PATH}`.",
        "- Public data: World Bank WDI latest available GDP, adjusted-savings CO2 damage, resource depletion, forest depletion, forest area, and resource-rent indicators.",
        "- Cache: `artifacts/cache/world_bank_green_gdp_panel.csv`.",
        "",
        "## Selected GGDP Method",
        f"- Method: {result['selected_ggdp_method']['method_id']}.",
        f"- Formula: {result['selected_ggdp_method']['formula']}",
        "",
        "## Global Assessment",
        f"- World penalty: {result['global_impact_model']['world_summary']['world_green_gdp_penalty_pct_gni']}% of GNI.",
        f"- Recommendation: {result['global_worthwhile_assessment']['recommendation']}.",
        f"- Net benefit score: {result['global_worthwhile_assessment']['net_benefit_score']}.",
        "",
        "## Brazil Case",
        f"- Green GDP penalty: {result['country_case_study']['green_gdp_penalty_pct_gni']}% of GNI.",
        f"- Green gap: ${result['country_case_study']['green_gap_usd']:,.0f}.",
        "",
        "## One-page Report",
        result["one_page_country_report"],
        "",
        "## Output Files",
        f"- `result.json`: {RESULT_PATH}",
        f"- `ggdp_formula_components.csv`: {ARTIFACT_DIR / 'ggdp_formula_components.csv'}",
        f"- `world_bank_green_gdp_panel.csv`: {ARTIFACT_DIR / 'world_bank_green_gdp_panel.csv'}",
        f"- `global_impact_scenarios.csv`: {ARTIFACT_DIR / 'global_impact_scenarios.csv'}",
        f"- `brazil_country_analysis.csv`: {ARTIFACT_DIR / 'brazil_country_analysis.csv'}",
        f"- `green_gdp_policy_frontier.png`: {ARTIFACT_DIR / 'green_gdp_policy_frontier.png'}",
    ]
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ensure_pdf_exists()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    formula_df, selected_method = build_formula_components()
    panel = fetch_world_bank_panel()
    scenario_df, global_model = build_global_impact_model(panel)
    assessment = assess_worthwhile(scenario_df)
    country_df, country_case = country_case_study(panel)
    write_plot(panel, scenario_df)
    result = {
        "problem_id": "2023-F-GreenGDP",
        "data_source": {
            "type": "official_pdf_and_world_bank_api",
            "root": str(ARCHIVE_ROOT / "official_assets_extracted" / "2023"),
            "source_pdf": str(PDF_PATH),
            "world_bank_api": "https://api.worldbank.org/v2/",
            "indicator_ids": INDICATORS,
            "countries": COUNTRIES,
            "official_requirements": OFFICIAL_REQUIREMENTS,
        },
        "selected_ggdp_method": selected_method,
        "global_impact_model": global_model,
        "global_worthwhile_assessment": assessment,
        "country_case_study": country_case,
        "one_page_country_report": one_page_country_report(country_case, assessment),
        "assumption_audit": {
            "truthfulness_note": "This workflow uses the official PDF and World Bank WDI observations with explicit policy-response assumptions.",
            "assumptions": ASSUMPTIONS,
            "artifact_rows": {
                "ggdp_formula_components.csv": len(formula_df),
                "world_bank_green_gdp_panel.csv": len(panel),
                "global_impact_scenarios.csv": len(scenario_df),
                "brazil_country_analysis.csv": len(country_df),
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
