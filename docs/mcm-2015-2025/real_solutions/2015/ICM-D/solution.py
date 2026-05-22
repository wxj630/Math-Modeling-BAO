from __future__ import annotations

import json
import os
from pathlib import Path

import pandas as pd


ARCHIVE_ROOT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
PDF_PATH = ARCHIVE_ROOT / "official_assets_extracted" / "2015" / "Is it sustainable.pdf"
DATA_PATH = ARCHIVE_ROOT / "official_assets_extracted" / "2015" / "Problem Data- Is it sustainable" / "world_bank_nepal_indicators.csv"
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"
os.environ.setdefault("MPLCONFIGDIR", str(ARTIFACT_DIR / ".matplotlib"))

import matplotlib.pyplot as plt


PLANNING_HORIZON_YEARS = 20
UN_LDC_LIST_SIZE = 48
SELECTED_COUNTRY = "Nepal"
REFERENCE_WORLD_POPULATION_2050 = 9_000_000_000

INDICATORS = {
    "SP.POP.TOTL": "Population, total",
    "NY.GDP.PCAP.KD": "GDP per capita, constant 2015 US$",
    "SI.POV.DDAY": "Poverty headcount ratio at $2.15/day",
    "SH.H2O.BASW.ZS": "People using at least basic drinking water services",
    "EG.ELC.ACCS.ZS": "Access to electricity",
    "AG.LND.FRST.ZS": "Forest area",
    "SH.STA.BASS.ZS": "People using at least basic sanitation services",
}

COMPONENTS = {
    "water_access": {"indicator": "SH.H2O.BASW.ZS", "weight": 0.17, "direction": "higher_is_better"},
    "sanitation_access": {"indicator": "SH.STA.BASS.ZS", "weight": 0.15, "direction": "higher_is_better"},
    "energy_access": {"indicator": "EG.ELC.ACCS.ZS", "weight": 0.15, "direction": "higher_is_better"},
    "livelihood": {"indicator": "NY.GDP.PCAP.KD", "weight": 0.16, "direction": "higher_is_better", "normalizer": 3000.0},
    "poverty_reduction": {"indicator": "SI.POV.DDAY", "weight": 0.17, "direction": "lower_is_better"},
    "environment_health": {"indicator": "AG.LND.FRST.ZS", "weight": 0.12, "direction": "higher_is_better"},
    "population_pressure": {"indicator": "SP.POP.TOTL", "weight": 0.08, "direction": "lower_growth_is_better"},
}

PROGRAMS = [
    {
        "program": "clean_water_and_sanitation",
        "annual_cost_billion_usd": 0.18,
        "component_delta_per_year": {"water_access": 0.004, "sanitation_access": 0.008, "poverty_reduction": 0.001},
        "description": "rural water systems, sanitation extension, and maintenance training",
    },
    {
        "program": "distributed_clean_energy",
        "annual_cost_billion_usd": 0.14,
        "component_delta_per_year": {"energy_access": 0.004, "livelihood": 0.004, "environment_health": 0.001},
        "description": "micro-hydro, solar mini-grids, clean cooking, and resilient local maintenance",
    },
    {
        "program": "climate_resilient_agriculture",
        "annual_cost_billion_usd": 0.16,
        "component_delta_per_year": {"poverty_reduction": 0.004, "livelihood": 0.003, "environment_health": 0.002},
        "description": "terrace stabilization, irrigation efficiency, seed resilience, and farmer cooperatives",
    },
    {
        "program": "education_and_livelihoods",
        "annual_cost_billion_usd": 0.20,
        "component_delta_per_year": {"livelihood": 0.006, "poverty_reduction": 0.003, "population_pressure": 0.001},
        "description": "technical training, women-focused entrepreneurship, and local value-chain support",
    },
    {
        "program": "forest_and_disaster_risk_management",
        "annual_cost_billion_usd": 0.10,
        "component_delta_per_year": {"environment_health": 0.004, "poverty_reduction": 0.001, "population_pressure": 0.001},
        "description": "community forestry, slope risk monitoring, disaster preparedness, and watershed protection",
    },
]

ASSUMPTIONS = {
    "country_choice_note": "Nepal is used as one LDC example to instantiate the required 20-year plan; the numeric observations are cached from World Bank API responses.",
    "score_range": "All component scores are clipped to [0, 1]. Percent indicators are divided by 100; GDP per capita is divided by 3000 constant 2015 US dollars and clipped at 1.",
    "program_delta_note": "Program effects are transparent planning assumptions applied to observed baseline indicators, not historical estimates of causal impact.",
    "population_pressure_note": "Population pressure score rewards a lower 20-year extrapolated population growth ratio, capped by a 1.6 stress reference.",
}


def clean_float(value: float, digits: int = 6) -> float:
    return round(float(value), digits)


def load_panel() -> pd.DataFrame:
    df = pd.read_csv(DATA_PATH)
    df["year"] = pd.to_numeric(df["year"], errors="coerce").astype("Int64")
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    df = df.dropna(subset=["year"])
    return df[df["indicator_id"].isin(INDICATORS)].copy()


def latest_values(panel: pd.DataFrame) -> dict[str, dict[str, object]]:
    latest = {}
    for indicator_id, group in panel.dropna(subset=["value"]).groupby("indicator_id"):
        row = group.sort_values("year").iloc[-1]
        latest[indicator_id] = {
            "indicator_name": row["indicator_name"],
            "year": int(row["year"]),
            "value": clean_float(row["value"], 6),
            "lastupdated": str(row.get("lastupdated", "")),
            "api_url": str(row.get("api_url", "")),
        }
    return latest


def trend_per_year(panel: pd.DataFrame, indicator_id: str, years: int = 10) -> float:
    rows = panel[(panel["indicator_id"] == indicator_id) & panel["value"].notna()].sort_values("year")
    if len(rows) < 2:
        return 0.0
    recent = rows.tail(years)
    first = recent.iloc[0]
    last = recent.iloc[-1]
    year_gap = max(1, int(last["year"] - first["year"]))
    return float((last["value"] - first["value"]) / year_gap)


def component_score(component: str, latest: dict[str, dict[str, object]], panel: pd.DataFrame) -> dict[str, object]:
    spec = COMPONENTS[component]
    indicator_id = spec["indicator"]
    value = float(latest[indicator_id]["value"])
    if spec["direction"] == "higher_is_better":
        if "normalizer" in spec:
            score = value / float(spec["normalizer"])
        else:
            score = value / 100.0
    elif spec["direction"] == "lower_is_better":
        score = 1.0 - value / 100.0
    else:
        pop_rows = panel[(panel["indicator_id"] == indicator_id) & panel["value"].notna()].sort_values("year")
        first = pop_rows.tail(20).iloc[0]
        last = pop_rows.tail(20).iloc[-1]
        growth_ratio = float(last["value"] / first["value"])
        score = 1.0 - min(1.0, max(0.0, (growth_ratio - 1.0) / 0.6))
    score = max(0.0, min(1.0, score))
    return {
        "component": component,
        "indicator_id": indicator_id,
        "indicator_name": INDICATORS[indicator_id],
        "latest_year": latest[indicator_id]["year"],
        "latest_value": value,
        "weight": spec["weight"],
        "score": clean_float(score),
        "weighted_score": clean_float(score * spec["weight"]),
        "trend_per_year_raw": clean_float(trend_per_year(panel, indicator_id), 6),
    }


def sustainability_index(panel: pd.DataFrame) -> dict[str, object]:
    latest = latest_values(panel)
    components = [component_score(component, latest, panel) for component in COMPONENTS]
    total = sum(item["weighted_score"] for item in components)
    baseline_year = int(max(item["latest_year"] for item in components))
    status = "sustainable" if total >= 0.70 else "transitional" if total >= 0.50 else "unsustainable"
    return {
        "definition": "Weighted country sustainability score over needs and limits: water, sanitation, energy, livelihoods, poverty, environment, and population pressure.",
        "baseline_year": baseline_year,
        "baseline_score": clean_float(total),
        "status_rule": "score >= 0.70 sustainable; 0.50-0.70 transitional; <0.50 unsustainable",
        "baseline_status": status,
        "components": components,
    }


def build_plan(index: dict[str, object]) -> dict[str, object]:
    rows = []
    baseline_components = {item["component"]: float(item["score"]) for item in index["components"]}
    for program in PROGRAMS:
        score_gain = 0.0
        for component, delta in program["component_delta_per_year"].items():
            weight = COMPONENTS[component]["weight"]
            remaining_room = max(0.0, 1.0 - baseline_components[component])
            realized_delta = min(remaining_room, delta * PLANNING_HORIZON_YEARS)
            score_gain += realized_delta * weight
        total_cost = program["annual_cost_billion_usd"] * PLANNING_HORIZON_YEARS
        rows.append(
            {
                "program": program["program"],
                "annual_cost_billion_usd": clean_float(program["annual_cost_billion_usd"], 3),
                "twenty_year_cost_billion_usd": clean_float(total_cost, 3),
                "estimated_score_gain": clean_float(score_gain),
                "score_gain_per_billion_usd": clean_float(score_gain / total_cost if total_cost else 0.0),
                "description": program["description"],
            }
        )
    rows = sorted(rows, key=lambda item: item["score_gain_per_billion_usd"], reverse=True)
    return {
        "selected_country": SELECTED_COUNTRY,
        "horizon_years": PLANNING_HORIZON_YEARS,
        "strategy": "Prioritize infrastructure that jointly improves basic needs and ecological limits, then rank programs by score gain per billion USD.",
        "programs": rows,
    }


def evaluate_plan(index: dict[str, object], plan: dict[str, object]) -> dict[str, object]:
    component_scores = {item["component"]: float(item["score"]) for item in index["components"]}
    for program in PROGRAMS:
        for component, delta in program["component_delta_per_year"].items():
            component_scores[component] = min(1.0, component_scores[component] + delta * PLANNING_HORIZON_YEARS)
    rows = []
    score_after = 0.0
    for component, score in component_scores.items():
        weighted = score * COMPONENTS[component]["weight"]
        score_after += weighted
        rows.append({"component": component, "score_after_20_years": clean_float(score), "weighted_score_after": clean_float(weighted)})
    return {
        "baseline_score": index["baseline_score"],
        "score_after_20_years": clean_float(score_after),
        "score_gain": clean_float(score_after - float(index["baseline_score"])),
        "status_after_20_years": "sustainable" if score_after >= 0.70 else "transitional" if score_after >= 0.50 else "unsustainable",
        "component_projection": rows,
        "evaluation_note": "Projection applies transparent program-effect assumptions to cached World Bank baseline indicators; it is a planning experiment, not a causal forecast.",
    }


def bang_for_buck(plan: dict[str, object]) -> dict[str, object]:
    top = plan["programs"][0]
    return {
        "ranking_method": "estimated 20-year sustainability score gain per billion USD",
        "top_program": top,
        "program_ranking": plan["programs"],
    }


def write_artifacts(panel: pd.DataFrame, index: dict[str, object], plan: dict[str, object], evaluation: dict[str, object], efficiency: dict[str, object]) -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    panel.to_csv(ARTIFACT_DIR / "world_bank_indicator_panel.csv", index=False, encoding="utf-8-sig")
    pd.DataFrame(index["components"]).to_csv(ARTIFACT_DIR / "sustainability_index_components.csv", index=False, encoding="utf-8-sig")
    pd.DataFrame(plan["programs"]).to_csv(ARTIFACT_DIR / "development_plan.csv", index=False, encoding="utf-8-sig")
    pd.DataFrame(efficiency["program_ranking"]).to_csv(ARTIFACT_DIR / "policy_efficiency.csv", index=False, encoding="utf-8-sig")

    years = list(range(0, PLANNING_HORIZON_YEARS + 1))
    scores = [index["baseline_score"] + evaluation["score_gain"] * year / PLANNING_HORIZON_YEARS for year in years]
    fig, ax = plt.subplots(figsize=(8, 4.8))
    ax.plot(years, scores, marker="o", color="#2f6f73")
    ax.axhline(0.70, linestyle="--", color="#9a6b1f", label="sustainable threshold")
    ax.set_title("2015 ICM-D Nepal Sustainability Projection")
    ax.set_xlabel("Years after plan starts")
    ax.set_ylabel("Sustainability score")
    ax.set_ylim(0, 1)
    ax.grid(alpha=0.25)
    ax.legend()
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "sustainability_projection.png", dpi=180)
    plt.close(fig)


def write_report(result: dict[str, object]) -> None:
    index = result["sustainability_index"]
    plan = result["development_plan"]
    evaluation = result["plan_evaluation"]
    top = result["bang_for_buck"]["top_program"]
    lines = [
        "# 2015 ICM-D Is it sustainable? 官方 PDF + World Bank 实验报告",
        "",
        "## 数据来源",
        f"- COMAP 官方 PDF：`{PDF_PATH}`。",
        f"- World Bank 缓存数据：`{DATA_PATH}`。",
        f"- 选定 LDC 示例：{SELECTED_COUNTRY}。题面要求从 48 个 LDC 中选择一个国家；本实验选择 Nepal，并只把缓存 World Bank API 指标作为观测值。",
        "- 没有观测到的指标不补造；项目影响系数在 `assumption_audit` 中标为规划假设。",
        "",
        "## Q1 国家可持续性模型",
        f"- 基线年份：{index['baseline_year']}。",
        f"- 基线得分：{index['baseline_score']}，状态：{index['baseline_status']}。",
        "- 指标维度：清洁水、卫生设施、能源、收入/生计、贫困、森林环境、人口压力。",
        "",
        "## Q2 20 年可持续发展计划",
        f"- 规划期：{plan['horizon_years']} 年。",
        f"- 项目数：{len(plan['programs'])}。",
        f"- 效率最高项目：{top['program']}，单位预算增益：{top['score_gain_per_billion_usd']}。",
        "",
        "## Q3 计划影响评估",
        f"- 20 年后得分：{evaluation['score_after_20_years']}。",
        f"- 得分增益：{evaluation['score_gain']}。",
        f"- 20 年后状态：{evaluation['status_after_20_years']}。",
        "",
        "## Q4 模型优缺点",
        "- 优点：指标透明、数据可追溯、项目效率可排序，适合 ICM 对不同干预做初筛。",
        "- 局限：World Bank 年度指标粒度较粗，项目效应不是因果估计；正式论文应补充本地项目成本、气候灾害、治理稳定性和微观贫困数据。",
        "",
        "## 输出文件",
        f"- `result.json`：{RESULT_PATH}",
        f"- `world_bank_indicator_panel.csv`：{ARTIFACT_DIR / 'world_bank_indicator_panel.csv'}",
        f"- `sustainability_index_components.csv`：{ARTIFACT_DIR / 'sustainability_index_components.csv'}",
        f"- `development_plan.csv`：{ARTIFACT_DIR / 'development_plan.csv'}",
        f"- `policy_efficiency.csv`：{ARTIFACT_DIR / 'policy_efficiency.csv'}",
        f"- `sustainability_projection.png`：{ARTIFACT_DIR / 'sustainability_projection.png'}",
    ]
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    if not PDF_PATH.exists():
        raise FileNotFoundError(f"Missing official PDF: {PDF_PATH}")
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Missing cached World Bank CSV: {DATA_PATH}")
    panel = load_panel()
    index = sustainability_index(panel)
    plan = build_plan(index)
    evaluation = evaluate_plan(index, plan)
    efficiency = bang_for_buck(plan)
    result = {
        "problem_id": "2015-D",
        "data_source": {
            "type": "official_pdf_and_world_bank_csv",
            "root": str(DATA_PATH.parent),
            "source_pdf": str(PDF_PATH),
            "selected_country": SELECTED_COUNTRY,
            "rows": {DATA_PATH.name: int(len(panel))},
            "indicators": INDICATORS,
            "official_problem_parameters": {
                "ldc_list_size": UN_LDC_LIST_SIZE,
                "planning_horizon_years": PLANNING_HORIZON_YEARS,
                "reference_world_population_2050": REFERENCE_WORLD_POPULATION_2050,
                "pillars_from_statement": ["poverty and vulnerability", "economic development", "ecosystem health"],
            },
        },
        "sustainability_index": index,
        "development_plan": plan,
        "plan_evaluation": evaluation,
        "bang_for_buck": efficiency,
        "assumption_audit": {
            "truthfulness_note": "COMAP supplied the PDF task statement and pointed teams to World Bank Data; this workflow uses cached World Bank API observations for Nepal plus explicit planning assumptions for intervention effects.",
            "assumptions": ASSUMPTIONS,
        },
    }
    write_artifacts(panel, index, plan, evaluation, efficiency)
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_report(result)
    print(json.dumps({"result": str(RESULT_PATH), "report": str(REPORT_PATH), "artifacts": str(ARTIFACT_DIR)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
