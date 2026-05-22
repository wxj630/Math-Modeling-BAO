from __future__ import annotations

import json
import os
from pathlib import Path

import pandas as pd


ARCHIVE_ROOT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
PDF_PATH = ARCHIVE_ROOT / "official_assets_extracted" / "2016" / "Are we heading towards a thirsty planet.pdf"
DATA_PATH = ARCHIVE_ROOT / "official_assets_extracted" / "2016" / "Problem Data- Are we heading towards a thirsty planet" / "world_bank_jordan_water_indicators.csv"
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"
os.environ.setdefault("MPLCONFIGDIR", str(ARTIFACT_DIR / ".matplotlib"))

import matplotlib.pyplot as plt


SELECTED_REGION = "Jordan"
FORECAST_HORIZON_YEARS = 15
WATER_USE_GROWS_TWICE_POPULATION_RATE = 2.0
UN_WATER_SCARCITY_PEOPLE = 1_600_000_000

INDICATORS = {
    "SP.POP.TOTL": "Population, total",
    "ER.H2O.FWTL.ZS": "Annual freshwater withdrawals, total (% of internal resources)",
    "ER.H2O.FWAG.ZS": "Annual freshwater withdrawals, agriculture (% of total freshwater withdrawal)",
    "ER.H2O.FWIN.ZS": "Annual freshwater withdrawals, industry (% of total freshwater withdrawal)",
    "ER.H2O.FWDM.ZS": "Annual freshwater withdrawals, domestic (% of total freshwater withdrawal)",
    "SH.H2O.BASW.ZS": "People using at least basic drinking water services",
    "SH.STA.BASS.ZS": "People using at least basic sanitation services",
    "NY.GDP.PCAP.KD": "GDP per capita, constant 2015 US$",
}

INTERVENTIONS = [
    {
        "program": "agricultural_efficiency",
        "annual_cost_musd": 120,
        "withdrawal_reduction_pct_points": 2.4,
        "quality_gain_pct_points": 0.2,
        "neighbor_ecosystem_note": "lower irrigation withdrawals leave more water in shared basins and reduce salinity pressure",
    },
    {
        "program": "wastewater_reuse_and_sanitation",
        "annual_cost_musd": 95,
        "withdrawal_reduction_pct_points": 1.1,
        "quality_gain_pct_points": 0.9,
        "neighbor_ecosystem_note": "treated reuse reduces downstream pollution but requires careful brine/sludge management",
    },
    {
        "program": "leakage_reduction_and_metering",
        "annual_cost_musd": 85,
        "withdrawal_reduction_pct_points": 1.5,
        "quality_gain_pct_points": 0.3,
        "neighbor_ecosystem_note": "demand management lowers pressure on regional aquifers without shifting scarcity elsewhere",
    },
    {
        "program": "desalination_and_renewable_energy",
        "annual_cost_musd": 220,
        "withdrawal_reduction_pct_points": 1.7,
        "quality_gain_pct_points": 0.4,
        "neighbor_ecosystem_note": "adds supply but has coastal brine and energy tradeoffs; pair with renewable power",
    },
    {
        "program": "rainwater_harvesting_and_aquifer_recharge",
        "annual_cost_musd": 70,
        "withdrawal_reduction_pct_points": 0.8,
        "quality_gain_pct_points": 0.2,
        "neighbor_ecosystem_note": "small decentralized gains improve drought resilience and reduce flash-flood losses",
    },
]

ASSUMPTIONS = {
    "region_choice_note": "Jordan is selected as a heavily overloaded water-scarce region; the water stress indicator is observed in World Bank data.",
    "baseline_model": "stress index = freshwater withdrawals as percent of internal renewable resources divided by 100; values above 1 mean withdrawals exceed internal resources.",
    "no_intervention_demand_growth": "future stress grows with recent population trend multiplied by the problem statement claim that water use has grown at twice the population rate.",
    "intervention_effect_note": "intervention effects are transparent planning assumptions applied to observed baseline indicators, not historical causal estimates.",
}


def clean_float(value: float, digits: int = 6) -> float:
    return round(float(value), digits)


def load_panel() -> pd.DataFrame:
    df = pd.read_csv(DATA_PATH)
    df["year"] = pd.to_numeric(df["year"], errors="coerce").astype("Int64")
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    df = df.dropna(subset=["year"])
    return df[df["indicator_id"].isin(INDICATORS)].copy()


def latest(panel: pd.DataFrame, indicator_id: str) -> dict[str, object]:
    rows = panel[(panel["indicator_id"] == indicator_id) & panel["value"].notna()].sort_values("year")
    row = rows.iloc[-1]
    return {
        "indicator_id": indicator_id,
        "indicator_name": INDICATORS[indicator_id],
        "year": int(row["year"]),
        "value": clean_float(row["value"], 6),
        "api_url": str(row.get("api_url", "")),
        "lastupdated": str(row.get("lastupdated", "")),
    }


def slope(panel: pd.DataFrame, indicator_id: str, periods: int = 10) -> float:
    rows = panel[(panel["indicator_id"] == indicator_id) & panel["value"].notna()].sort_values("year").tail(periods)
    if len(rows) < 2:
        return 0.0
    first = rows.iloc[0]
    last = rows.iloc[-1]
    return float((last["value"] - first["value"]) / max(1, int(last["year"] - first["year"])))


def water_scarcity_model(panel: pd.DataFrame) -> dict[str, object]:
    indicators = {indicator: latest(panel, indicator) for indicator in INDICATORS}
    stress_pct = float(indicators["ER.H2O.FWTL.ZS"]["value"])
    stress_index = stress_pct / 100.0
    quality_penalty = max(0.0, (100.0 - float(indicators["SH.STA.BASS.ZS"]["value"])) / 100.0)
    access_gap = max(0.0, (100.0 - float(indicators["SH.H2O.BASW.ZS"]["value"])) / 100.0)
    economic_capacity = min(1.0, float(indicators["NY.GDP.PCAP.KD"]["value"]) / 12_000.0)
    scarcity_score = stress_index + 0.6 * quality_penalty + 0.4 * access_gap - 0.25 * economic_capacity
    status = "critical" if scarcity_score >= 1.0 else "stressed" if scarcity_score >= 0.6 else "manageable"
    components = [
        {"component": "physical_stress", "value": clean_float(stress_index), "interpretation": "withdrawals/internal renewable resources"},
        {"component": "sanitation_quality_gap", "value": clean_float(quality_penalty), "interpretation": "economic scarcity proxy through sanitation service gap"},
        {"component": "basic_water_access_gap", "value": clean_float(access_gap), "interpretation": "clean water access gap"},
        {"component": "economic_capacity_offset", "value": clean_float(economic_capacity), "interpretation": "GDP/capita ability to fund infrastructure"},
    ]
    return {
        "definition": "A region is critical when withdrawals exceed internal renewable resources after adjusting for service gaps and economic capacity.",
        "selected_region": SELECTED_REGION,
        "baseline_year": max(item["year"] for item in indicators.values()),
        "baseline_stress_percent_internal_resources": clean_float(stress_pct, 3),
        "baseline_stress_index": clean_float(stress_index, 6),
        "scarcity_score": clean_float(scarcity_score, 6),
        "scarcity_status": status,
        "indicator_latest": indicators,
        "components": components,
        "drivers": {
            "physical_scarcity": "freshwater withdrawals exceed internal renewable resources",
            "economic_scarcity": "near-universal basic water access hides infrastructure leakage, sanitation, cost, and reliability gaps",
            "sector_driver": "agriculture remains the largest withdrawal share in the cached World Bank observations",
        },
    }


def population_growth_rate(panel: pd.DataFrame) -> float:
    pop = panel[(panel["indicator_id"] == "SP.POP.TOTL") & panel["value"].notna()].sort_values("year").tail(10)
    first = float(pop.iloc[0]["value"])
    last = float(pop.iloc[-1]["value"])
    years = max(1, int(pop.iloc[-1]["year"] - pop.iloc[0]["year"]))
    return (last / first) ** (1 / years) - 1


def forecast_rows(base_index: float, annual_growth: float, annual_reduction_pct_points: float = 0.0) -> list[dict[str, object]]:
    rows = []
    for year in range(0, FORECAST_HORIZON_YEARS + 1):
        raw_pct = base_index * 100.0 * ((1 + annual_growth) ** year)
        adjusted_pct = max(0.0, raw_pct - annual_reduction_pct_points * year)
        stress_index = adjusted_pct / 100.0
        rows.append(
            {
                "year_after_start": year,
                "freshwater_withdrawal_pct_internal_resources": clean_float(adjusted_pct, 3),
                "stress_index": clean_float(stress_index, 6),
                "status": "critical" if stress_index >= 1.0 else "stressed" if stress_index >= 0.6 else "manageable",
            }
        )
    return rows


def no_intervention_forecast(panel: pd.DataFrame, model: dict[str, object]) -> dict[str, object]:
    pop_growth = population_growth_rate(panel)
    water_growth = pop_growth * WATER_USE_GROWS_TWICE_POPULATION_RATE
    rows = forecast_rows(float(model["baseline_stress_index"]), water_growth)
    critical_year = next((row["year_after_start"] for row in rows if row["stress_index"] >= 1.5), None)
    return {
        "horizon_years": FORECAST_HORIZON_YEARS,
        "recent_population_growth_rate": clean_float(pop_growth, 6),
        "water_use_growth_rate_assumption": clean_float(water_growth, 6),
        "critical_threshold_index": 1.5,
        "first_year_crossing_critical_threshold": critical_year,
        "stress_index_after_15_years": rows[-1]["stress_index"],
        "rows": rows,
        "citizen_impact": "Without intervention, higher stress implies more intermittent supply, higher water prices, more agricultural constraints, and greater health risk during drought periods.",
    }


def intervention_plan() -> dict[str, object]:
    rows = []
    for item in INTERVENTIONS:
        total_cost = item["annual_cost_musd"] * FORECAST_HORIZON_YEARS
        gain = item["withdrawal_reduction_pct_points"] + 0.5 * item["quality_gain_pct_points"]
        rows.append(
            {
                "program": item["program"],
                "annual_cost_musd": item["annual_cost_musd"],
                "fifteen_year_cost_musd": total_cost,
                "annual_withdrawal_reduction_pct_points": item["withdrawal_reduction_pct_points"],
                "annual_quality_gain_pct_points": item["quality_gain_pct_points"],
                "efficiency_score_per_billion_usd": clean_float(gain / (total_cost / 1000.0), 6),
                "neighbor_ecosystem_note": item["neighbor_ecosystem_note"],
            }
        )
    rows = sorted(rows, key=lambda row: row["efficiency_score_per_billion_usd"], reverse=True)
    return {
        "selected_region": SELECTED_REGION,
        "horizon_years": FORECAST_HORIZON_YEARS,
        "strategy": "combine demand reduction, reuse, leakage control, new non-conventional supply, and watershed recharge; avoid relying on one megaproject",
        "programs": rows,
        "strengths": ["addresses both physical and economic scarcity", "prioritizes agriculture and leakage before expensive new supply", "explicitly tracks ecosystem spillovers"],
        "weaknesses": ["requires governance capacity and pricing reform", "desalination can shift environmental burden to energy/brine", "national World Bank indicators hide local inequity"],
    }


def intervention_forecast(base_forecast: dict[str, object], plan: dict[str, object]) -> dict[str, object]:
    annual_reduction = sum(float(row["annual_withdrawal_reduction_pct_points"]) for row in plan["programs"])
    rows = forecast_rows(base_forecast["rows"][0]["stress_index"], base_forecast["water_use_growth_rate_assumption"], annual_reduction_pct_points=annual_reduction)
    return {
        "horizon_years": FORECAST_HORIZON_YEARS,
        "annual_reduction_pct_points": clean_float(annual_reduction, 3),
        "stress_index_after_15_years": rows[-1]["stress_index"],
        "stress_reduction_vs_no_intervention": clean_float(base_forecast["stress_index_after_15_years"] - rows[-1]["stress_index"], 6),
        "rows": rows,
        "can_become_less_susceptible": rows[-1]["stress_index"] < base_forecast["stress_index_after_15_years"],
        "will_water_be_critical_without_intervention": base_forecast["stress_index_after_15_years"] >= 1.5,
    }


def write_artifacts(panel: pd.DataFrame, model: dict[str, object], no_plan: dict[str, object], plan: dict[str, object], with_plan: dict[str, object]) -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    panel.to_csv(ARTIFACT_DIR / "world_bank_water_panel.csv", index=False, encoding="utf-8-sig")
    pd.DataFrame(model["components"]).to_csv(ARTIFACT_DIR / "water_scarcity_components.csv", index=False, encoding="utf-8-sig")
    pd.DataFrame(plan["programs"]).to_csv(ARTIFACT_DIR / "intervention_plan.csv", index=False, encoding="utf-8-sig")
    forecast = pd.DataFrame(no_plan["rows"]).rename(columns={"stress_index": "no_intervention_stress_index"})
    with_df = pd.DataFrame(with_plan["rows"])[["year_after_start", "stress_index"]].rename(columns={"stress_index": "intervention_stress_index"})
    forecast = forecast.merge(with_df, on="year_after_start", how="left")
    forecast.to_csv(ARTIFACT_DIR / "water_forecast.csv", index=False, encoding="utf-8-sig")

    fig, ax = plt.subplots(figsize=(8.5, 5))
    ax.plot(forecast["year_after_start"], forecast["no_intervention_stress_index"], marker="o", label="no intervention", color="#b44b32")
    ax.plot(forecast["year_after_start"], forecast["intervention_stress_index"], marker="o", label="with intervention", color="#2f6f73")
    ax.axhline(1.0, color="#444444", linestyle="--", label="withdrawals = internal resources")
    ax.axhline(1.5, color="#7a4b9a", linestyle=":", label="critical threshold")
    ax.set_title("2016 ICM-E Jordan Water Stress Projection")
    ax.set_xlabel("Years after start")
    ax.set_ylabel("Water stress index")
    ax.grid(alpha=0.25)
    ax.legend()
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "water_stress_projection.png", dpi=180)
    plt.close(fig)


def write_report(result: dict[str, object]) -> None:
    model = result["water_scarcity_model"]
    no_plan = result["no_intervention_forecast"]
    with_plan = result["intervention_forecast"]
    lines = [
        "# 2016 ICM-E Are we heading towards a thirsty planet? 官方 PDF + World Bank 实验报告",
        "",
        "## 数据来源",
        f"- 官方 PDF：`{PDF_PATH}`。",
        f"- World Bank 缓存数据：`{DATA_PATH}`。",
        f"- 选定地区：{SELECTED_REGION}，用 World Bank 观测到的 freshwater withdrawals/internal resources 指标体现水资源严重超载。",
        "",
        "## Q1 清洁水供给能力模型",
        f"- 基线年份：{model['baseline_year']}。",
        f"- 基线 stress index：{model['baseline_stress_index']}。",
        f"- 稀缺状态：{model['scarcity_status']}。",
        "",
        "## Q2 缺水原因",
        "- 物理稀缺：总取水量超过内部可再生淡水资源。",
        "- 经济稀缺：基础服务覆盖率高但管理、漏损、成本和水质风险仍会限制可靠供水。",
        "",
        "## Q3 15 年无干预预测",
        f"- 15 年后 stress index：{no_plan['stress_index_after_15_years']}。",
        f"- 居民影响：{no_plan['citizen_impact']}",
        "",
        "## Q4 干预计划",
        f"- 项目数：{len(result['intervention_plan']['programs'])}。",
        f"- 策略：{result['intervention_plan']['strategy']}",
        "",
        "## Q5 有干预预测",
        f"- 15 年后 stress index：{with_plan['stress_index_after_15_years']}。",
        f"- 相对无干预降低：{with_plan['stress_reduction_vs_no_intervention']}。",
        f"- 是否降低易受缺水影响：{with_plan['can_become_less_susceptible']}。",
        "",
        "## Q6 模型优缺点",
        "- 优点：观测指标可追溯，区分物理稀缺和经济稀缺，能比较干预路径。",
        "- 局限：World Bank 年度国家级指标不能替代流域/月度水文数据；干预效果是规划假设，不是因果估计。",
        "",
        "## 输出文件",
        f"- `result.json`：{RESULT_PATH}",
        f"- `world_bank_water_panel.csv`：{ARTIFACT_DIR / 'world_bank_water_panel.csv'}",
        f"- `water_scarcity_components.csv`：{ARTIFACT_DIR / 'water_scarcity_components.csv'}",
        f"- `intervention_plan.csv`：{ARTIFACT_DIR / 'intervention_plan.csv'}",
        f"- `water_forecast.csv`：{ARTIFACT_DIR / 'water_forecast.csv'}",
        f"- `water_stress_projection.png`：{ARTIFACT_DIR / 'water_stress_projection.png'}",
    ]
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    if not PDF_PATH.exists():
        raise FileNotFoundError(f"Missing official PDF: {PDF_PATH}")
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Missing cached World Bank CSV: {DATA_PATH}")
    panel = load_panel()
    model = water_scarcity_model(panel)
    no_plan = no_intervention_forecast(panel, model)
    plan = intervention_plan()
    with_plan = intervention_forecast(no_plan, plan)
    result = {
        "problem_id": "2016-E",
        "data_source": {
            "type": "official_pdf_and_world_bank_csv",
            "root": str(DATA_PATH.parent),
            "source_pdf": str(PDF_PATH),
            "selected_region": SELECTED_REGION,
            "rows": {DATA_PATH.name: int(len(panel))},
            "indicators": INDICATORS,
            "official_problem_parameters": {
                "un_water_scarcity_people": UN_WATER_SCARCITY_PEOPLE,
                "water_use_growth_vs_population_rate": WATER_USE_GROWS_TWICE_POPULATION_RATE,
                "forecast_horizon_years": FORECAST_HORIZON_YEARS,
                "scarcity_types": ["physical scarcity", "economic scarcity"],
            },
        },
        "water_scarcity_model": model,
        "no_intervention_forecast": no_plan,
        "intervention_plan": plan,
        "intervention_forecast": with_plan,
        "assumption_audit": {
            "truthfulness_note": "COMAP supplied the PDF task statement and named water-resource data sources; this workflow uses cached World Bank observations for Jordan plus explicit planning assumptions for interventions.",
            "assumptions": ASSUMPTIONS,
        },
    }
    write_artifacts(panel, model, no_plan, plan, with_plan)
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_report(result)
    print(json.dumps({"result": str(RESULT_PATH), "report": str(REPORT_PATH), "artifacts": str(ARTIFACT_DIR)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
