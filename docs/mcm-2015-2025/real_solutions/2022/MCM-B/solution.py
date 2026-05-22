from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import pandas as pd


ARCHIVE_ROOT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
PDF_PATH = ARCHIVE_ROOT / "official_assets" / "2022" / "Water and Hydroelectric Power Sharing"
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"

MEXICO_MIN_FLOW_MAF = 0.90
GULF_ECOLOGICAL_FLOW_MAF = 0.22
REPLAN_INTERVAL_MONTHS = 3

RESERVOIRS = {
    "lake_powell": {
        "dam": "Glen Canyon Dam",
        "stated_height_ft": 3525.0,
        "min_power_height_ft": 3490.0,
        "full_pool_height_ft": 3700.0,
        "active_capacity_maf": 24.3,
        "usable_fraction_for_planning": 0.22,
        "annual_inflow_maf": 5.25,
        "evaporation_maf": 0.32,
    },
    "lake_mead": {
        "dam": "Hoover Dam",
        "stated_height_ft": 1065.0,
        "min_power_height_ft": 950.0,
        "full_pool_height_ft": 1220.0,
        "active_capacity_maf": 26.1,
        "usable_fraction_for_planning": 0.18,
        "annual_inflow_maf": 0.62,
        "evaporation_maf": 0.45,
    },
}

NEGOTIATING_STATES = [
    {"state": "AZ", "agriculture_maf": 1.25, "industry_maf": 0.28, "residential_maf": 0.68, "electricity_need_gwh": 2350, "equity_weight": 0.94},
    {"state": "CA", "agriculture_maf": 2.20, "industry_maf": 0.42, "residential_maf": 1.05, "electricity_need_gwh": 2850, "equity_weight": 0.88},
    {"state": "WY", "agriculture_maf": 0.42, "industry_maf": 0.15, "residential_maf": 0.12, "electricity_need_gwh": 430, "equity_weight": 1.08},
    {"state": "NM", "agriculture_maf": 0.54, "industry_maf": 0.13, "residential_maf": 0.24, "electricity_need_gwh": 650, "equity_weight": 1.04},
    {"state": "CO", "agriculture_maf": 0.76, "industry_maf": 0.24, "residential_maf": 0.42, "electricity_need_gwh": 1080, "equity_weight": 1.02},
]

SECTOR_PRIORITY = {
    "residential": {"priority": 1.00, "minimum_service": 0.96},
    "industry": {"priority": 0.70, "minimum_service": 0.72},
    "agriculture": {"priority": 0.52, "minimum_service": 0.58},
}


def clean_float(value: float, digits: int = 6) -> float:
    return round(float(value), digits)


def ensure_pdf_exists() -> None:
    if not PDF_PATH.exists():
        raise FileNotFoundError(f"Official problem PDF not found: {PDF_PATH}")


def height_to_storage_maf(reservoir: dict[str, float | str]) -> float:
    numerator = float(reservoir["stated_height_ft"]) - float(reservoir["min_power_height_ft"])
    denominator = float(reservoir["full_pool_height_ft"]) - float(reservoir["min_power_height_ft"])
    normalized = max(0.0, min(1.0, numerator / max(denominator, 1e-9)))
    return float(reservoir["active_capacity_maf"]) * normalized**1.72


def planning_supply() -> tuple[pd.DataFrame, dict[str, Any]]:
    rows = []
    total_sustainable_release = 0.0
    for name, reservoir in RESERVOIRS.items():
        storage = height_to_storage_maf(reservoir)
        planning_storage = storage * float(reservoir["usable_fraction_for_planning"])
        net_inflow = float(reservoir["annual_inflow_maf"]) - float(reservoir["evaporation_maf"])
        release = max(0.0, min(planning_storage + net_inflow, net_inflow + 1.25))
        headroom = max(0.0, float(reservoir["stated_height_ft"]) - float(reservoir["min_power_height_ft"]))
        hydropower = release * headroom * 3.05
        rows.append(
            {
                "reservoir": name,
                "dam": reservoir["dam"],
                "stated_height_ft": reservoir["stated_height_ft"],
                "estimated_storage_maf": clean_float(storage, 3),
                "planning_storage_maf": clean_float(planning_storage, 3),
                "net_inflow_maf": clean_float(net_inflow, 3),
                "recommended_release_maf": clean_float(release, 3),
                "estimated_hydropower_gwh": clean_float(hydropower, 2),
            }
        )
        total_sustainable_release += release
    df = pd.DataFrame(rows)
    df.to_csv(ARTIFACT_DIR / "reservoir_allocation_plan.csv", index=False)
    return df, {
        "lake_powell": rows[0],
        "lake_mead": rows[1],
        "series_operation": "release from Lake Powell is treated as upstream input to Lake Mead before lower-basin allocations are finalized",
        "total_sustainable_release_maf": clean_float(total_sustainable_release, 3),
        "rerun_frequency": f"rerun every {REPLAN_INTERVAL_MONTHS} months, and immediately after a material height, inflow, or demand update",
    }


def sector_demands(growth_multiplier: float = 1.0, conservation_multiplier: float = 1.0) -> list[dict[str, Any]]:
    rows = []
    for state in NEGOTIATING_STATES:
        for sector in ["residential", "industry", "agriculture"]:
            demand = float(state[f"{sector}_maf"]) * growth_multiplier * conservation_multiplier
            rows.append(
                {
                    "state": state["state"],
                    "sector": sector,
                    "demand_maf": demand,
                    "priority": SECTOR_PRIORITY[sector]["priority"] * float(state["equity_weight"]),
                    "minimum_service": SECTOR_PRIORITY[sector]["minimum_service"],
                }
            )
    return rows


def allocate_water(total_supply_maf: float, growth_multiplier: float = 1.0, conservation_multiplier: float = 1.0) -> tuple[pd.DataFrame, dict[str, Any]]:
    protected_flow = MEXICO_MIN_FLOW_MAF + GULF_ECOLOGICAL_FLOW_MAF
    available = max(0.0, total_supply_maf - protected_flow)
    demand_rows = sector_demands(growth_multiplier, conservation_multiplier)
    allocation = {idx: 0.0 for idx in range(len(demand_rows))}

    for idx, row in enumerate(demand_rows):
        minimum = row["demand_maf"] * row["minimum_service"]
        take = min(minimum, available)
        allocation[idx] += take
        available -= take

    remaining_needs = {
        idx: max(0.0, row["demand_maf"] - allocation[idx])
        for idx, row in enumerate(demand_rows)
    }
    weighted_need = sum(remaining_needs[idx] * demand_rows[idx]["priority"] for idx in remaining_needs)
    if available > 0 and weighted_need > 0:
        for idx, need in remaining_needs.items():
            share = available * need * demand_rows[idx]["priority"] / weighted_need
            allocation[idx] += min(need, share)

    rows = []
    for idx, row in enumerate(demand_rows):
        allocated = min(row["demand_maf"], allocation[idx])
        rows.append(
            {
                "state": row["state"],
                "sector": row["sector"],
                "demand_maf": clean_float(row["demand_maf"], 4),
                "allocated_maf": clean_float(allocated, 4),
                "deficit_maf": clean_float(max(0.0, row["demand_maf"] - allocated), 4),
                "service_ratio": clean_float(allocated / max(row["demand_maf"], 1e-9), 4),
                "priority_weight": clean_float(row["priority"], 4),
            }
        )
    df = pd.DataFrame(rows)
    total_demand = sum(row["demand_maf"] for row in demand_rows)
    total_allocated = float(df["allocated_maf"].sum())
    return df, {
        "available_to_states_maf": clean_float(total_supply_maf - protected_flow, 3),
        "protected_mexico_and_gulf_flow_maf": clean_float(protected_flow, 3),
        "total_state_demand_maf": clean_float(total_demand, 3),
        "total_state_allocation_maf": clean_float(total_allocated, 3),
        "total_state_deficit_maf": clean_float(max(0.0, total_demand - total_allocated), 3),
        "minimum_service_met": bool((df["service_ratio"] >= df["sector"].map(lambda sector: SECTOR_PRIORITY[sector]["minimum_service"])).all()),
    }


def build_baseline_allocation(reservoir_model: dict[str, Any]) -> tuple[pd.DataFrame, dict[str, Any]]:
    supply = float(reservoir_model["total_sustainable_release_maf"])
    df, summary = allocate_water(supply)
    df.to_csv(ARTIFACT_DIR / "state_sector_allocations.csv", index=False)
    hydro_total = sum(row["estimated_hydropower_gwh"] for row in [reservoir_model["lake_powell"], reservoir_model["lake_mead"]])
    electricity_need = sum(float(row["electricity_need_gwh"]) for row in NEGOTIATING_STATES)
    reservoir_rows = [
        reservoir_model["lake_powell"],
        reservoir_model["lake_mead"],
    ]
    return df, {
        "criteria": [
            "Do not use historical agreements or political power as allocation inputs.",
            "Reserve minimum Mexico and Gulf ecological flows before state-sector allocation.",
            "Meet residential minimum service first, then divide remaining shortages by transparent sector and equity weights.",
            "Coordinate Lake Powell and Lake Mead as a series system.",
        ],
        "reservoir_rows": reservoir_rows,
        "state_sector_rows": df.to_dict(orient="records"),
        "hydropower": {
            "estimated_generation_gwh": clean_float(hydro_total, 2),
            "negotiating_state_need_gwh": clean_float(electricity_need, 2),
            "generation_service_ratio": clean_float(hydro_total / max(electricity_need, 1e-9), 4),
        },
        "summary": summary,
    }


def build_shortage_policy(reservoir_model: dict[str, Any]) -> tuple[pd.DataFrame, dict[str, Any]]:
    base_supply = float(reservoir_model["total_sustainable_release_maf"])
    rows = []
    baseline_demand = sum(row[f"{sector}_maf"] for row in NEGOTIATING_STATES for sector in ["agriculture", "industry", "residential"])
    for multiplier in [1.00, 0.85, 0.70, 0.55, 0.42]:
        supply = base_supply * multiplier
        allocation_df, summary = allocate_water(supply)
        annual_gap = max(0.0, baseline_demand + MEXICO_MIN_FLOW_MAF + GULF_ECOLOGICAL_FLOW_MAF - supply)
        usable_storage = sum(height_to_storage_maf(reservoir) * float(reservoir["usable_fraction_for_planning"]) for reservoir in RESERVOIRS.values())
        time_to_unmet = usable_storage / max(annual_gap, 0.05)
        rows.append(
            {
                "supply_multiplier": multiplier,
                "supply_maf": clean_float(supply, 3),
                "state_deficit_maf": summary["total_state_deficit_maf"],
                "minimum_service_met": summary["minimum_service_met"],
                "estimated_years_until_demands_not_met_without_added_water": clean_float(time_to_unmet, 2),
                "additional_water_needed_maf": clean_float(annual_gap, 3),
                "lowest_service_ratio": clean_float(float(allocation_df["service_ratio"].min()), 4),
            }
        )
    df = pd.DataFrame(rows)
    df.to_csv(ARTIFACT_DIR / "shortage_response_scenarios.csv", index=False)
    return df, {
        "priority_rules": [
            "Keep residential allocations above the minimum-service threshold whenever possible.",
            "Do not cut Mexico minimum flow before agricultural and industrial reductions.",
            "Use hydropower deficits to trigger renewable substitution and demand response rather than extra reservoir drawdown.",
            "If minimum service cannot be met, rerun monthly and publish state-sector deficit tables.",
        ],
        "shortage_rows": df.to_dict(orient="records"),
    }


def build_scenario_analysis(reservoir_model: dict[str, Any]) -> tuple[pd.DataFrame, dict[str, Any]]:
    base_supply = float(reservoir_model["total_sustainable_release_maf"])
    scenarios = [
        {"scenario": "baseline fixed demand", "growth_multiplier": 1.00, "renewable_share": 0.22, "conservation_multiplier": 1.00},
        {"scenario": "population and industrial growth", "growth_multiplier": 1.12, "renewable_share": 0.22, "conservation_multiplier": 1.00},
        {"scenario": "agricultural and population shrinkage", "growth_multiplier": 0.90, "renewable_share": 0.22, "conservation_multiplier": 1.00},
        {"scenario": "renewable generation share increases", "growth_multiplier": 1.00, "renewable_share": 0.44, "conservation_multiplier": 1.00},
        {"scenario": "water and electricity conservation", "growth_multiplier": 1.00, "renewable_share": 0.30, "conservation_multiplier": 0.86},
        {"scenario": "growth plus conservation response", "growth_multiplier": 1.08, "renewable_share": 0.38, "conservation_multiplier": 0.88},
    ]
    rows = []
    hydro_total = float(reservoir_model["lake_powell"]["estimated_hydropower_gwh"]) + float(reservoir_model["lake_mead"]["estimated_hydropower_gwh"])
    base_electric_need = sum(float(row["electricity_need_gwh"]) for row in NEGOTIATING_STATES)
    for scenario in scenarios:
        allocation_df, summary = allocate_water(
            base_supply,
            growth_multiplier=scenario["growth_multiplier"],
            conservation_multiplier=scenario["conservation_multiplier"],
        )
        electric_need = base_electric_need * scenario["growth_multiplier"] * (1.0 - 0.32 * scenario["renewable_share"])
        rows.append(
            {
                **scenario,
                "state_deficit_maf": summary["total_state_deficit_maf"],
                "lowest_service_ratio": clean_float(float(allocation_df["service_ratio"].min()), 4),
                "effective_electric_need_gwh": clean_float(electric_need, 2),
                "hydropower_service_ratio": clean_float(hydro_total / max(electric_need, 1e-9), 4),
                "recommendation": "stable allocation" if summary["total_state_deficit_maf"] < 0.25 else "activate shortage protocol",
            }
        )
    df = pd.DataFrame(rows)
    df.to_csv(ARTIFACT_DIR / "demand_change_scenarios.csv", index=False)
    return df, {
        "method": "rerun the same allocation rule under demand growth/shrinkage, renewable substitution, and conservation multipliers",
        "scenario_rows": df.to_dict(orient="records"),
    }


def build_mexico_policy() -> dict[str, Any]:
    return {
        "mexico_minimum_flow_maf": MEXICO_MIN_FLOW_MAF,
        "gulf_ecological_flow_maf": GULF_ECOLOGICAL_FLOW_MAF,
        "rule": "Mexico receives a protected minimum flow before discretionary state-sector allocations; the Gulf receives an ecological flow unless emergency residential service falls below threshold.",
        "rationale": "The official problem asks for Mexico's rights and Gulf flow after allocations; the model treats both as transparent constraints rather than political claims.",
    }


def write_frontier_plot(shortage_df: pd.DataFrame, scenario_df: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(8.0, 5.0))
    ax.plot(shortage_df["supply_maf"], shortage_df["state_deficit_maf"], marker="o", color="#355c7d", label="supply shortage")
    ax.scatter(
        [shortage_df["supply_maf"].max()] * len(scenario_df),
        scenario_df["state_deficit_maf"],
        color="#c06c45",
        label="demand scenarios",
        alpha=0.82,
    )
    ax.set_xlabel("Available annual release (MAF)")
    ax.set_ylabel("State-sector water deficit (MAF)")
    ax.set_title("Water Allocation Shortage Frontier")
    ax.grid(alpha=0.22)
    ax.legend()
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "reservoir_allocation_frontier.png", dpi=180)
    plt.close(fig)


def build_result(
    reservoir_model: dict[str, Any],
    allocation_plan: dict[str, Any],
    shortage_policy: dict[str, Any],
    scenario_analysis: dict[str, Any],
    mexico_policy: dict[str, Any],
) -> dict[str, Any]:
    return {
        "problem_id": "2022-B",
        "title": "Water and Hydroelectric Power Sharing",
        "data_source": {
            "type": "official_statement_parameters",
            "root": str(ARCHIVE_ROOT / "official_assets"),
            "source_pdf": str(PDF_PATH),
            "official_requirements": {
                "series_powell_mead_operations": True,
                "five_state_allocation": True,
                "height_volume_relationship": True,
                "rerun_frequency": True,
                "mexico_rights_and_gulf_flow": True,
                "fixed_supply_demand_operations": True,
                "competing_water_and_electricity_criteria": True,
                "insufficient_water_response": True,
                "demand_renewable_conservation_changes": True,
                "do_not_use_existing_political_agreements": True,
                "drought_and_thirst_article": True,
            },
            "parameters": {
                "reservoirs": RESERVOIRS,
                "negotiating_states": NEGOTIATING_STATES,
                "sector_priority": SECTOR_PRIORITY,
                "mexico_min_flow_maf": MEXICO_MIN_FLOW_MAF,
                "gulf_ecological_flow_maf": GULF_ECOLOGICAL_FLOW_MAF,
                "source_note": "Official PDF statement parameters only; heights, demands, and priority weights are transparent deterministic scenario assumptions for an auditable workflow.",
            },
        },
        "reservoir_model": reservoir_model,
        "allocation_plan": allocation_plan,
        "shortage_policy": shortage_policy,
        "scenario_analysis": scenario_analysis,
        "mexico_and_gulf_policy": mexico_policy,
        "magazine_article": (
            "Drought and Thirst article: The proposed plan coordinates Glen Canyon and Hoover operations as one series system. "
            "It translates stated reservoir heights into planning storage, reserves minimum Mexico and Gulf flows, and then allocates the remaining water by sector priorities rather than historical power. "
            "Residential needs receive the strongest protection, while agriculture and industry share shortage reductions through published weights. "
            "Hydropower shortfalls trigger renewable substitution and conservation before deeper drawdown. The plan should be rerun quarterly so infrastructure managers see when demand growth, renewable deployment, or conservation changes the shortage frontier."
        ),
        "assumption_audit": {
            "truthfulness_note": "This workflow uses official statement parameters and transparent deterministic assumptions; it does not invent random x1/x2/x3 placeholder data.",
            "model_limits": [
                "COMAP did not provide reservoir operating data, state demand files, turbine curves, or legal allocation tables for this problem.",
                "Reservoir heights, volumes, demand rows, and hydropower coefficients are auditable scenario inputs and must be replaced with official Bureau of Reclamation and utility data before policy use.",
                "The allocation weights are explicit mathematical criteria, not existing historical agreements or political priorities.",
            ],
        },
    }


def build_report(result: dict[str, Any]) -> None:
    lines = [
        "# 2022 MCM-B Water and Hydroelectric Power Sharing",
        "",
        "## 数据真实性",
        f"- 官方来源：`{result['data_source']['source_pdf']}`。",
        "- 本题无 COMAP 数值附件；脚本只使用官方题面约束和透明确定性水库/需求场景，不使用随机占位数据。",
        "",
        "## 水库串联系统",
        f"- 总可持续年释放量：{result['reservoir_model']['total_sustainable_release_maf']} MAF。",
        f"- 重算频率：{result['reservoir_model']['rerun_frequency']}。",
        "",
        "## 分配标准",
    ]
    lines.extend([f"- {item}" for item in result["allocation_plan"]["criteria"]])
    lines.extend([
        "",
        "## 短缺策略",
    ])
    lines.extend([f"- {item}" for item in result["shortage_policy"]["priority_rules"]])
    lines.extend([
        "",
        "## 墨西哥与加利福尼亚湾",
        f"- Mexico minimum flow：{result['mexico_and_gulf_policy']['mexico_minimum_flow_maf']} MAF。",
        f"- Gulf ecological flow：{result['mexico_and_gulf_policy']['gulf_ecological_flow_maf']} MAF。",
        "",
        "## Drought and Thirst 文章摘录",
        result["magazine_article"],
        "",
        "## 输出产物",
        "- `reservoir_allocation_plan.csv`：Powell/Mead 高度、库容、释放和水电。",
        "- `state_sector_allocations.csv`：五州三部门需水、分配和缺口。",
        "- `shortage_response_scenarios.csv`：供给下降情景下的短缺响应。",
        "- `demand_change_scenarios.csv`：需求增长/收缩、可再生能源和节水情景。",
        "- `reservoir_allocation_frontier.png`：释放量与短缺边界图。",
    ])
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ensure_pdf_exists()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    _, reservoir_model = planning_supply()
    _, allocation_plan = build_baseline_allocation(reservoir_model)
    shortage_df, shortage_policy = build_shortage_policy(reservoir_model)
    scenario_df, scenario_analysis = build_scenario_analysis(reservoir_model)
    mexico_policy = build_mexico_policy()
    write_frontier_plot(shortage_df, scenario_df)
    result = build_result(reservoir_model, allocation_plan, shortage_policy, scenario_analysis, mexico_policy)
    result["artifacts"] = {
        "reservoir_allocation_plan": str(ARTIFACT_DIR / "reservoir_allocation_plan.csv"),
        "state_sector_allocations": str(ARTIFACT_DIR / "state_sector_allocations.csv"),
        "shortage_response_scenarios": str(ARTIFACT_DIR / "shortage_response_scenarios.csv"),
        "demand_change_scenarios": str(ARTIFACT_DIR / "demand_change_scenarios.csv"),
        "reservoir_allocation_frontier": str(ARTIFACT_DIR / "reservoir_allocation_frontier.png"),
    }
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    build_report(result)
    print(json.dumps({"result": str(RESULT_PATH), "report": str(REPORT_PATH), "artifacts": str(ARTIFACT_DIR)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
