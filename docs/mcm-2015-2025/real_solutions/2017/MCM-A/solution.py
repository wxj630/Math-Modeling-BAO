from __future__ import annotations

import json
import math
import os
from pathlib import Path

import pandas as pd


ARCHIVE_ROOT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
PDF_PATH = ARCHIVE_ROOT / "official_assets_extracted" / "2017" / "Managing The Zambezi River.pdf"
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"
os.environ.setdefault("MPLCONFIGDIR", "/private/tmp/math_modeling_world_mplconfig")

import matplotlib.pyplot as plt


SMALL_DAM_MIN_COUNT = 10
SMALL_DAM_MAX_COUNT = 20
KARIBA_REFERENCE_WATER_MANAGEMENT_INDEX = 100.0
OPTION_1 = "Repairing the existing Kariba Dam"
OPTION_2 = "Rebuilding the existing Kariba Dam"
OPTION_3 = "Removing Kariba Dam and replacing it with 10 to 20 smaller dams"

ASSUMPTIONS = {
    "cost_units": "All costs are normalized planning cost units because the official statement provides no engineering bill of quantities.",
    "river_axis": "The Zambezi reach is represented by a normalized 0-100 river coordinate from upstream Lake Kariba control to downstream exposed communities.",
    "dam_capacity": "Each small dam contributes storage, flood attenuation, low-flow release, and redundancy; values are deterministic scenario assumptions.",
    "water_management_index": "Composite index = 0.35 storage + 0.30 flood attenuation + 0.20 low-flow support + 0.15 redundancy.",
    "exposure_limits": "Maximum exposure durations are planning rules for protecting river segments under flood or low-flow extremes.",
}


def clean_float(value: float, digits: int = 6) -> float:
    return round(float(value), digits)


def option_assessment() -> dict[str, object]:
    rows = [
        {
            "option": "Option 1",
            "description": OPTION_1,
            "normalized_cost": 42.0,
            "implementation_years": 4,
            "construction_disruption": 0.28,
            "safety_improvement": 0.48,
            "water_management_flexibility": 0.34,
            "main_benefit": "lowest near-term cost and fastest reduction of urgent maintenance risk",
            "main_risk": "keeps single-point failure and limited operational flexibility",
        },
        {
            "option": "Option 2",
            "description": OPTION_2,
            "normalized_cost": 96.0,
            "implementation_years": 8,
            "construction_disruption": 0.66,
            "safety_improvement": 0.82,
            "water_management_flexibility": 0.58,
            "main_benefit": "major safety reset while preserving Lake Kariba operating concept",
            "main_risk": "high cost and long construction exposure",
        },
        {
            "option": "Option 3",
            "description": OPTION_3,
            "normalized_cost": 118.0,
            "implementation_years": 11,
            "construction_disruption": 0.78,
            "safety_improvement": 0.88,
            "water_management_flexibility": 0.91,
            "main_benefit": "distributed redundancy and more flexible flood/low-flow control",
            "main_risk": "complex siting, ecological exposure, and coordination across many dams",
        },
    ]
    for row in rows:
        row["benefit_score"] = clean_float(0.45 * row["safety_improvement"] + 0.35 * row["water_management_flexibility"] - 0.20 * row["construction_disruption"])
        row["benefit_cost_ratio"] = clean_float(row["benefit_score"] / row["normalized_cost"] * 100)
    return {
        "options": rows,
        "brief_recommendation": "Option 1 is a near-term risk bridge, but Option 3 is the strategic option if ZRA can manage multi-site construction and ecological constraints.",
    }


def evaluate_dam_count(count: int) -> dict[str, object]:
    storage = min(118.0, 6.0 * count + 13.0 * math.log(count))
    flood = min(122.0, 4.4 * count + 2.8 * count ** 0.78)
    low_flow = min(112.0, 3.9 * count + 16.0 * math.log(count))
    redundancy = min(120.0, 35.0 + 4.2 * count)
    coordination_penalty = max(0.0, (count - 16) * 1.8)
    index = 0.35 * storage + 0.30 * flood + 0.20 * low_flow + 0.15 * redundancy - coordination_penalty
    cost = 18.0 + 5.4 * count + 0.22 * count * count
    safety_cost_balance = index - 0.42 * cost
    return {
        "dam_count": count,
        "storage_index": clean_float(storage),
        "flood_attenuation_index": clean_float(flood),
        "low_flow_support_index": clean_float(low_flow),
        "redundancy_index": clean_float(redundancy),
        "water_management_index": clean_float(index),
        "normalized_cost": clean_float(cost),
        "safety_cost_balance": clean_float(safety_cost_balance),
        "meets_kariba_reference": bool(index >= KARIBA_REFERENCE_WATER_MANAGEMENT_INDEX),
    }


def dam_placement_plan(recommended_count: int) -> list[dict[str, object]]:
    rows = []
    for dam_id in range(1, recommended_count + 1):
        coordinate = 6.0 + (88.0 / (recommended_count - 1)) * (dam_id - 1)
        if coordinate < 25:
            segment = "upstream_lake_control"
        elif coordinate < 55:
            segment = "mid_river_flood_buffer"
        elif coordinate < 78:
            segment = "downstream_power_and_irrigation"
        else:
            segment = "delta_ecology_protection"
        local_storage = 100.0 / recommended_count * (1.08 if segment in {"upstream_lake_control", "mid_river_flood_buffer"} else 0.92)
        rows.append(
            {
                "dam_id": f"D{dam_id:02d}",
                "river_coordinate_0_100": clean_float(coordinate, 2),
                "segment": segment,
                "local_storage_share_pct": clean_float(local_storage, 3),
                "primary_role": {
                    "upstream_lake_control": "replace Kariba storage and regulate lake-level transitions",
                    "mid_river_flood_buffer": "attenuate flood peaks and distribute release timing",
                    "downstream_power_and_irrigation": "support low-flow releases for users",
                    "delta_ecology_protection": "limit extreme exposure in sensitive downstream reaches",
                }[segment],
            }
        )
    return rows


def small_dam_system() -> dict[str, object]:
    frontier = [evaluate_dam_count(count) for count in range(SMALL_DAM_MIN_COUNT, SMALL_DAM_MAX_COUNT + 1)]
    feasible = [row for row in frontier if row["meets_kariba_reference"]]
    recommended = max(feasible or frontier, key=lambda row: row["safety_cost_balance"])
    placements = dam_placement_plan(int(recommended["dam_count"]))
    return {
        "kariba_reference_index": KARIBA_REFERENCE_WATER_MANAGEMENT_INDEX,
        "frontier": frontier,
        "recommended_dam_count": int(recommended["dam_count"]),
        "recommended_system": recommended,
        "placements": placements,
        "recommendation": "Use a distributed 15-dam system: enough redundancy to match Kariba-level management while avoiding the coordination penalty of 18-20 dams.",
    }


def flow_modulation_strategy(system: dict[str, object]) -> dict[str, object]:
    rules = [
        {
            "condition": "normal wet-season inflow",
            "trigger_flow_index": "60-85",
            "release_rule": "store first 30% of surplus upstream, pass 50% through mid-river buffers, reserve 20% for downstream ecological pulse",
            "safety_cost_tradeoff": "moderate storage with low emergency spill risk",
        },
        {
            "condition": "normal dry-season inflow",
            "trigger_flow_index": "35-60",
            "release_rule": "coordinate weekly low-flow support from downstream and mid-river dams while preserving upstream reserve",
            "safety_cost_tradeoff": "protect water users while limiting turbine and ecology stress",
        },
        {
            "condition": "flood emergency",
            "trigger_flow_index": ">85",
            "release_rule": "pre-release upstream dams, stagger mid-river gates by 8-12 hours, cap downstream rise rate",
            "safety_cost_tradeoff": "higher short-term spill cost to avoid synchronized flood peak",
        },
        {
            "condition": "prolonged low-water emergency",
            "trigger_flow_index": "<35 for 30 days",
            "release_rule": "shift to drought rationing, suspend noncritical hydropower peaking, protect drinking water and ecological minimum flow",
            "safety_cost_tradeoff": "economic generation loss accepted to preserve health and minimum river function",
        },
    ]
    return {
        "recommended_dam_count": system["recommended_dam_count"],
        "rules": rules,
        "coordination_principle": "Operate the dam chain as staggered buffers rather than independent reservoirs.",
    }


def extreme_flow_guidance() -> dict[str, object]:
    scenarios = [
        {"scenario": "maximum_expected_discharge", "flow_index": 100, "action": "open upstream pre-release gates and enforce downstream rise-rate cap", "zra_guidance": "activate flood command center and evacuate exposed low banks"},
        {"scenario": "high_flood", "flow_index": 88, "action": "stagger mid-river releases and maximize flood-buffer storage", "zra_guidance": "reduce synchronized peaks across adjacent segments"},
        {"scenario": "low_flow", "flow_index": 28, "action": "ration hydropower peaking and release ecological minimum flow", "zra_guidance": "prioritize drinking water, sanitation, and critical irrigation"},
        {"scenario": "minimum_expected_discharge", "flow_index": 12, "action": "enter emergency drought rule curve and suspend discretionary releases", "zra_guidance": "protect health and ecosystem refuges until inflow recovers"},
    ]
    return {"scenarios": scenarios}


def exposure_restrictions() -> dict[str, object]:
    segments = [
        {"segment": "upstream_lake_margin", "max_flood_exposure_days": 10, "max_low_water_exposure_days": 45, "reason": "slope stability and shoreline settlement risk"},
        {"segment": "mid_river_farmland", "max_flood_exposure_days": 6, "max_low_water_exposure_days": 35, "reason": "crop and soil damage"},
        {"segment": "urban_low_banks", "max_flood_exposure_days": 3, "max_low_water_exposure_days": 30, "reason": "public safety and sanitation"},
        {"segment": "hydropower_intake_reaches", "max_flood_exposure_days": 7, "max_low_water_exposure_days": 21, "reason": "turbine intake reliability"},
        {"segment": "delta_wetlands", "max_flood_exposure_days": 14, "max_low_water_exposure_days": 25, "reason": "ecological stress and salinity intrusion"},
    ]
    return {"segments": segments}


def brief_report(options: dict[str, object], system: dict[str, object]) -> str:
    best_option = max(options["options"], key=lambda row: row["benefit_score"])
    return (
        "Brief assessment for ZRA management:\n\n"
        f"ZRA asked for a two-page comparison of repairing Kariba, rebuilding Kariba, and replacing Kariba with 10-20 smaller dams. "
        f"Repair is the lowest-cost bridge, rebuild is the single-dam safety reset, and Option 3 provides the highest flexibility. "
        f"In this transparent scoring model, {best_option['option']} has the highest benefit score, while the detailed Option 3 design recommends "
        f"{system['recommended_dam_count']} smaller dams with water management index {system['recommended_system']['water_management_index']}. "
        "Because the official statement does not provide engineering cost or hydrology tables, all costs and capacities are normalized planning assumptions."
    )


def write_artifacts(options: dict[str, object], system: dict[str, object], strategy: dict[str, object], extreme: dict[str, object], exposure: dict[str, object]) -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(options["options"]).to_csv(ARTIFACT_DIR / "option_assessment.csv", index=False, encoding="utf-8-sig")
    pd.DataFrame(system["frontier"]).to_csv(ARTIFACT_DIR / "dam_count_frontier.csv", index=False, encoding="utf-8-sig")
    pd.DataFrame(system["placements"]).to_csv(ARTIFACT_DIR / "dam_placement_plan.csv", index=False, encoding="utf-8-sig")
    pd.DataFrame(strategy["rules"]).to_csv(ARTIFACT_DIR / "flow_modulation_policy.csv", index=False, encoding="utf-8-sig")
    pd.DataFrame(extreme["scenarios"]).to_csv(ARTIFACT_DIR / "extreme_flow_guidance.csv", index=False, encoding="utf-8-sig")
    pd.DataFrame(exposure["segments"]).to_csv(ARTIFACT_DIR / "exposure_restrictions.csv", index=False, encoding="utf-8-sig")

    frontier = pd.DataFrame(system["frontier"])
    fig, ax1 = plt.subplots(figsize=(8.8, 5.2))
    ax1.plot(frontier["dam_count"], frontier["water_management_index"], marker="o", color="#23645d", label="water management")
    ax1.axhline(KARIBA_REFERENCE_WATER_MANAGEMENT_INDEX, color="#555555", linestyle="--", label="Kariba reference")
    ax1.set_xlabel("Number of smaller dams")
    ax1.set_ylabel("Water management index")
    ax2 = ax1.twinx()
    ax2.plot(frontier["dam_count"], frontier["normalized_cost"], marker="s", color="#b45f3c", label="cost")
    ax2.set_ylabel("Normalized cost")
    ax1.set_title("2017 MCM-A Zambezi Small-Dam System Frontier")
    lines = ax1.get_lines() + ax2.get_lines()
    labels = [line.get_label() for line in lines]
    ax1.legend(lines, labels, loc="lower right")
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "dam_system_frontier.png", dpi=180)
    plt.close(fig)


def write_report(result: dict[str, object]) -> None:
    rec = result["small_dam_system"]["recommended_system"]
    lines = [
        "# 2017 MCM-A Managing The Zambezi River 题面参数实验报告",
        "",
        "## 数据来源",
        f"- 官方 PDF：`{PDF_PATH}`。",
        "- 官方题面参数：三种方案；Option 3 必须移除 Kariba 并用 10-20 座较小水坝替代；新系统需具有与 Kariba 相同或更高的总体水量管理能力。",
        "- 本题没有独立 CSV/XLSX 附件；成本、坝址坐标、容量和流量指数都是显式可替换规划假设。",
        "",
        "## Requirement 1 三方案简短评估",
        result["brief_assessment_report"],
        "",
        "## Requirement 2 Option 3 详细设计",
        f"- 推荐小坝数量：{result['small_dam_system']['recommended_dam_count']}。",
        f"- 水量管理指数：{rec['water_management_index']}，Kariba reference：{result['small_dam_system']['kariba_reference_index']}。",
        f"- 安全-成本平衡：{rec['safety_cost_balance']}。",
        "",
        "## 调度策略",
        f"- 原则：{result['flow_modulation_strategy']['coordination_principle']}。",
        "",
        "## 极端流量与暴露限制",
        f"- 极端情景数：{len(result['extreme_flow_guidance']['scenarios'])}。",
        f"- 暴露限制河段数：{len(result['exposure_restrictions']['segments'])}。",
        "",
        "## 输出文件",
        f"- `result.json`：{RESULT_PATH}",
        f"- `option_assessment.csv`：{ARTIFACT_DIR / 'option_assessment.csv'}",
        f"- `dam_placement_plan.csv`：{ARTIFACT_DIR / 'dam_placement_plan.csv'}",
        f"- `flow_modulation_policy.csv`：{ARTIFACT_DIR / 'flow_modulation_policy.csv'}",
        f"- `extreme_flow_guidance.csv`：{ARTIFACT_DIR / 'extreme_flow_guidance.csv'}",
        f"- `exposure_restrictions.csv`：{ARTIFACT_DIR / 'exposure_restrictions.csv'}",
        f"- `dam_system_frontier.png`：{ARTIFACT_DIR / 'dam_system_frontier.png'}",
    ]
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    if not PDF_PATH.exists():
        raise FileNotFoundError(f"Missing official PDF: {PDF_PATH}")
    options = option_assessment()
    system = small_dam_system()
    strategy = flow_modulation_strategy(system)
    extreme = extreme_flow_guidance()
    exposure = exposure_restrictions()
    result = {
        "problem_id": "2017-A",
        "data_source": {
            "type": "official_statement_parameters",
            "root": str(PDF_PATH.parent),
            "source_pdf": str(PDF_PATH),
            "official_problem_parameters": {
                "options": [OPTION_1, OPTION_2, OPTION_3],
                "small_dam_count_range": [SMALL_DAM_MIN_COUNT, SMALL_DAM_MAX_COUNT],
                "same_or_greater_water_management_required": True,
                "brief_assessment_required_pages": "1-2",
                "main_solution_page_limit": 20,
            },
            "assumptions": ASSUMPTIONS,
        },
        "option_assessment": options,
        "small_dam_system": system,
        "flow_modulation_strategy": strategy,
        "extreme_flow_guidance": extreme,
        "exposure_restrictions": exposure,
        "brief_assessment_report": brief_report(options, system),
        "assumption_audit": {
            "truthfulness_note": "This workflow uses official statement parameters and explicit deterministic assumptions; it does not claim normalized costs or dam coordinates are observed engineering data.",
            "replaceable_assumptions": ASSUMPTIONS,
        },
    }
    write_artifacts(options, system, strategy, extreme, exposure)
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_report(result)
    print(json.dumps({"result": str(RESULT_PATH), "report": str(REPORT_PATH), "artifacts": str(ARTIFACT_DIR)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
