from __future__ import annotations

import json
import math
import os
from pathlib import Path

import pandas as pd


ARCHIVE_ROOT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
PDF_PATH = ARCHIVE_ROOT / "official_assets_extracted" / "2017" / "Merge After Toll.pdf"
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"
os.environ.setdefault("MPLCONFIGDIR", "/private/tmp/math_modeling_world_mplconfig")

import matplotlib.pyplot as plt


BASE_LANES = 3
BASE_TOLLBOOTHS = 8
OFFICIAL_B_GT_L = BASE_TOLLBOOTHS > BASE_LANES
LANE_WIDTH_M = 3.6
BASE_CAPACITY_PER_LANE_VPH = 1850.0
LIGHT_DEMAND_VPH = 2400.0
HEAVY_DEMAND_VPH = 6200.0

BOOTH_SERVICE_RATES = {
    "conventional": 300.0,
    "exact_change": 450.0,
    "electronic": 900.0,
}

BASE_TOLLBOOTH_MIX = {
    "conventional": 0.35,
    "exact_change": 0.25,
    "electronic": 0.40,
}

ASSUMPTIONS = {
    "geometry_units": "The official statement gives L lanes, B tollbooths, and a 3-lane/8-booth example, but no survey drawing; merge lengths are transparent planning dimensions.",
    "capacity_units": "Throughput uses standard passenger-car-per-hour planning rates so that the official objectives can be audited and replaced by local engineering values.",
    "safety_index": "Accident prevention is represented by conflict exposure, required lane changes, and speed management rather than crash history, because no crash data is attached.",
    "cost_index": "Land and construction cost are normalized by area and control complexity; the official statement only says land and road construction are expensive.",
}


def clean_float(value: float, digits: int = 6) -> float:
    return round(float(value), digits)


def weighted_booth_rate(mix: dict[str, float]) -> float:
    total = sum(mix.values())
    if not math.isclose(total, 1.0, rel_tol=1e-9):
        mix = {key: value / total for key, value in mix.items()}
    return sum(BOOTH_SERVICE_RATES[key] * mix.get(key, 0.0) for key in BOOTH_SERVICE_RATES)


def downstream_capacity(outgoing_lanes: int, autonomous_share: float = 0.0) -> float:
    headway_gain = 1.0 + 0.22 * autonomous_share
    return outgoing_lanes * BASE_CAPACITY_PER_LANE_VPH * headway_gain


def booth_capacity(egress_lanes: int, mix: dict[str, float]) -> float:
    return egress_lanes * weighted_booth_rate(mix)


def candidate_designs() -> list[dict[str, object]]:
    lane_drop = BASE_TOLLBOOTHS - BASE_LANES
    candidates = [
        {
            "design": "short_direct_taper",
            "egress_lanes": BASE_TOLLBOOTHS,
            "outgoing_lanes": BASE_LANES,
            "merge_length_m": 260.0,
            "control": "single fan-in taper",
            "speed_management": "advisory signs only",
            "conflict_multiplier": 1.34,
            "control_complexity": 0.15,
        },
        {
            "design": "staged_zipper_merge",
            "egress_lanes": BASE_TOLLBOOTHS,
            "outgoing_lanes": BASE_LANES,
            "merge_length_m": 420.0,
            "control": "two-stage zipper merge with lane assignment",
            "speed_management": "posted speed taper and lane-use signs",
            "conflict_multiplier": 0.72,
            "control_complexity": 0.35,
        },
        {
            "design": "collector_distributor_split",
            "egress_lanes": BASE_TOLLBOOTHS,
            "outgoing_lanes": BASE_LANES,
            "merge_length_m": 560.0,
            "control": "parallel collector lanes merge into three-lane trunk",
            "speed_management": "metered merge at final throat",
            "conflict_multiplier": 0.61,
            "control_complexity": 0.55,
        },
        {
            "design": "wide_plaza_metered_merge",
            "egress_lanes": BASE_TOLLBOOTHS,
            "outgoing_lanes": BASE_LANES,
            "merge_length_m": 700.0,
            "control": "long fan-in with signal-metered platoons",
            "speed_management": "active metering and variable signs",
            "conflict_multiplier": 0.54,
            "control_complexity": 0.78,
        },
    ]
    rows: list[dict[str, object]] = []
    for row in candidates:
        merge_length = float(row["merge_length_m"])
        width = BASE_TOLLBOOTHS * LANE_WIDTH_M
        conflict_index = row["conflict_multiplier"] * lane_drop / merge_length * 100
        area_index = merge_length * width / 1000
        cost_index = area_index + 12.0 * row["control_complexity"]
        safety_score = max(0.0, 100.0 - 18.0 * conflict_index)
        capacity = min(
            booth_capacity(BASE_TOLLBOOTHS, BASE_TOLLBOOTH_MIX),
            downstream_capacity(BASE_LANES, autonomous_share=0.10),
        )
        throughput_score = capacity / 60.0
        objective_score = 0.42 * safety_score + 0.38 * throughput_score - 0.42 * cost_index
        rows.append(
            {
                **row,
                "width_m": clean_float(width, 2),
                "lane_drop_count": lane_drop,
                "conflict_index": clean_float(conflict_index),
                "cost_index": clean_float(cost_index),
                "safety_score": clean_float(safety_score),
                "throughput_capacity_vph": clean_float(capacity),
                "objective_score": clean_float(objective_score),
            }
        )
    return rows


def merge_design() -> dict[str, object]:
    rows = candidate_designs()
    recommended = max(rows, key=lambda row: row["objective_score"])
    return {
        "official_condition": "B tollbooths fan in to L travel lanes with B > L.",
        "candidates": rows,
        "recommended_design": recommended,
        "recommendation": "Use a staged zipper merge: it removes five lanes over two controlled merge zones, keeps the 8-to-3 official example, and avoids the land cost of a very long metered plaza.",
    }


def estimate_performance(design: dict[str, object], demand_vph: float, label: str, autonomous_share: float = 0.10, mix: dict[str, float] | None = None) -> dict[str, object]:
    mix = mix or BASE_TOLLBOOTH_MIX
    toll_capacity = booth_capacity(int(design["egress_lanes"]), mix)
    road_capacity = downstream_capacity(int(design["outgoing_lanes"]), autonomous_share)
    conflict_penalty = 1.0 - min(0.18, float(design["conflict_index"]) / 100.0)
    merge_capacity = road_capacity * conflict_penalty
    throughput = min(demand_vph, toll_capacity, merge_capacity)
    delay_minutes = max(0.0, demand_vph - throughput) / max(throughput, 1.0) * 18.0
    utilization = throughput / min(toll_capacity, merge_capacity)
    return {
        "traffic_case": label,
        "demand_vph": clean_float(demand_vph),
        "throughput_vph": clean_float(throughput),
        "tollbooth_capacity_vph": clean_float(toll_capacity),
        "merge_capacity_vph": clean_float(merge_capacity),
        "utilization": clean_float(utilization),
        "mean_delay_minutes": clean_float(delay_minutes),
    }


def traffic_performance(design: dict[str, object]) -> dict[str, object]:
    light = estimate_performance(design, LIGHT_DEMAND_VPH, "light_traffic")
    heavy = estimate_performance(design, HEAVY_DEMAND_VPH, "heavy_traffic")
    return {
        "light_traffic": light,
        "heavy_traffic": heavy,
        "interpretation": "Light demand clears without queueing; heavy demand is limited by booth service and merge throat capacity, so throughput rises until the controlled bottleneck is reached.",
    }


def autonomous_vehicle_sensitivity(design: dict[str, object]) -> dict[str, object]:
    rows = []
    for share in [0.0, 0.10, 0.25, 0.40, 0.60, 0.80]:
        case = estimate_performance(design, HEAVY_DEMAND_VPH, "heavy_traffic", autonomous_share=share)
        recommended_length = max(260.0, float(design["merge_length_m"]) * (1.0 - 0.18 * share))
        rows.append(
            {
                "autonomous_vehicle_share": clean_float(share, 2),
                "throughput_vph": case["throughput_vph"],
                "mean_delay_minutes": case["mean_delay_minutes"],
                "recommended_merge_length_m": clean_float(recommended_length, 2),
                "policy": "allow shorter headways but keep lane assignment until autonomous share exceeds 60%" if share < 0.60 else "reserve a cooperative merge lane if vehicle-to-vehicle coordination is reliable",
            }
        )
    return {"rows": rows}


def tollbooth_mix_sensitivity(design: dict[str, object]) -> dict[str, object]:
    scenarios = [
        ("mostly_conventional", {"conventional": 0.70, "exact_change": 0.20, "electronic": 0.10}),
        ("balanced_mix", {"conventional": 0.35, "exact_change": 0.25, "electronic": 0.40}),
        ("electronic_priority", {"conventional": 0.20, "exact_change": 0.20, "electronic": 0.60}),
        ("transponder_dominant", {"conventional": 0.10, "exact_change": 0.10, "electronic": 0.80}),
    ]
    rows = []
    for name, mix in scenarios:
        case = estimate_performance(design, HEAVY_DEMAND_VPH, "heavy_traffic", mix=mix)
        rows.append(
            {
                "scenario": name,
                "conventional_share": clean_float(mix["conventional"], 2),
                "exact_change_share": clean_float(mix["exact_change"], 2),
                "electronic_share": clean_float(mix["electronic"], 2),
                "weighted_service_rate_vph_per_booth": clean_float(weighted_booth_rate(mix)),
                "throughput_vph": case["throughput_vph"],
                "mean_delay_minutes": case["mean_delay_minutes"],
                "design_effect": "booth service is the controlling bottleneck" if case["tollbooth_capacity_vph"] < case["merge_capacity_vph"] else "merge geometry is the controlling bottleneck",
            }
        )
    return {"rows": rows}


def turnpike_letter(design: dict[str, object], performance: dict[str, object]) -> str:
    return (
        "To the New Jersey Turnpike Authority:\n\n"
        "The official 2017 MCM-B statement asks for a toll-plaza fan-in design where B tollbooths merge to L highway lanes, with the example B=8 and L=3. "
        f"Our recommendation is a {design['design'].replace('_', ' ')} with {design['merge_length_m']} meters of controlled merge distance. "
        "The design uses lane assignment and a staged zipper merge to reduce side conflicts before vehicles enter the three-lane roadway. "
        f"Under light demand the modeled throughput is {performance['light_traffic']['throughput_vph']} vehicles per hour; under heavy demand it reaches "
        f"{performance['heavy_traffic']['throughput_vph']} vehicles per hour before booth service and merge capacity become binding. "
        "As electronic toll collection and cooperative autonomous vehicles increase, keep the same lane-count geometry but shorten the effective merge zone only after field verification of headway compliance. "
        "This is an auditable planning model, not a replacement for site survey, crash records, or a civil-engineering design review."
    )


def write_artifacts(design: dict[str, object], performance: dict[str, object], av: dict[str, object], mix: dict[str, object]) -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(design["candidates"]).to_csv(ARTIFACT_DIR / "merge_geometry.csv", index=False)
    pd.DataFrame([performance["light_traffic"], performance["heavy_traffic"]]).to_csv(ARTIFACT_DIR / "traffic_performance.csv", index=False)
    pd.DataFrame(av["rows"]).to_csv(ARTIFACT_DIR / "autonomous_vehicle_sensitivity.csv", index=False)
    pd.DataFrame(mix["rows"]).to_csv(ARTIFACT_DIR / "tollbooth_mix_sensitivity.csv", index=False)

    frontier = pd.DataFrame(design["candidates"])
    plt.figure(figsize=(7.2, 4.6))
    plt.scatter(frontier["cost_index"], frontier["throughput_capacity_vph"], s=80, c=frontier["safety_score"], cmap="viridis")
    for _, row in frontier.iterrows():
        plt.annotate(str(row["design"]).replace("_", "\n"), (row["cost_index"], row["throughput_capacity_vph"]), fontsize=8, xytext=(4, 4), textcoords="offset points")
    plt.colorbar(label="Safety score")
    plt.xlabel("Normalized land/control cost index")
    plt.ylabel("Capacity before demand cap (vehicles/hour)")
    plt.title("2017 MCM-B toll-plaza merge design frontier")
    plt.tight_layout()
    plt.savefig(ARTIFACT_DIR / "merge_design_frontier.png", dpi=180)
    plt.close()


def write_report(result: dict[str, object]) -> None:
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    design = result["merge_design"]["recommended_design"]
    lines = [
        "# 2017 MCM-B Merge After Toll 题面参数实验报告",
        "",
        "## 数据来源",
        f"- 官方 PDF：`{PDF_PATH}`。",
        "- 官方题面参数：每方向 L 条行驶车道、B 个 barrier tollbooth，且 B > L；题面示例为 L=3、B=8。",
        "- 本题没有独立 CSV/XLSX 附件；几何长度、容量、成本和安全权重均为显式可替换规划假设。",
        "",
        "## Q1 形状、尺寸与并道模式",
        f"- 推荐设计：{design['design']}。",
        f"- 收费亭出口车道：{design['egress_lanes']}；汇入行驶车道：{design['outgoing_lanes']}。",
        f"- 推荐并道长度：{design['merge_length_m']} m；冲突指数：{design['conflict_index']}。",
        "",
        "## Q2 轻/重交通性能",
        f"- 轻交通吞吐量：{result['traffic_performance']['light_traffic']['throughput_vph']} veh/h。",
        f"- 重交通吞吐量：{result['traffic_performance']['heavy_traffic']['throughput_vph']} veh/h。",
        "",
        "## Q3 自动驾驶车辆比例敏感性",
        f"- 扫描情景数：{len(result['autonomous_vehicle_sensitivity']['rows'])}。",
        "",
        "## Q4 收费亭类型比例敏感性",
        f"- 扫描情景数：{len(result['tollbooth_mix_sensitivity']['rows'])}。",
        "",
        "## New Jersey Turnpike Authority 信函",
        result["turnpike_authority_letter"],
        "",
        "## 输出文件",
        f"- `result.json`：{RESULT_PATH}",
        f"- `merge_geometry.csv`：{ARTIFACT_DIR / 'merge_geometry.csv'}",
        f"- `traffic_performance.csv`：{ARTIFACT_DIR / 'traffic_performance.csv'}",
        f"- `autonomous_vehicle_sensitivity.csv`：{ARTIFACT_DIR / 'autonomous_vehicle_sensitivity.csv'}",
        f"- `tollbooth_mix_sensitivity.csv`：{ARTIFACT_DIR / 'tollbooth_mix_sensitivity.csv'}",
        f"- `merge_design_frontier.png`：{ARTIFACT_DIR / 'merge_design_frontier.png'}",
    ]
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    if not PDF_PATH.exists():
        raise FileNotFoundError(PDF_PATH)
    design = merge_design()
    recommended = design["recommended_design"]
    performance = traffic_performance(recommended)
    av = autonomous_vehicle_sensitivity(recommended)
    mix = tollbooth_mix_sensitivity(recommended)
    result = {
        "problem_id": "2017-MCM-B",
        "data_source": {
            "type": "official_statement_parameters",
            "root": str(ARCHIVE_ROOT / "official_assets_extracted" / "2017"),
            "source_pdf": str(PDF_PATH),
            "official_problem_parameters": {
                "example_lanes": BASE_LANES,
                "example_tollbooths": BASE_TOLLBOOTHS,
                "condition": "BASE_TOLLBOOTHS > BASE_LANES",
                "condition_holds": OFFICIAL_B_GT_L,
                "objectives": ["accident prevention", "throughput", "land and road construction cost"],
                "traffic_cases": ["light traffic", "heavy traffic"],
                "booth_types": list(BOOTH_SERVICE_RATES),
            },
        },
        "merge_design": design,
        "traffic_performance": performance,
        "autonomous_vehicle_sensitivity": av,
        "tollbooth_mix_sensitivity": mix,
        "turnpike_authority_letter": turnpike_letter(recommended, performance),
        "assumption_audit": {
            "truthfulness_note": "This workflow uses official statement parameters from the COMAP PDF and explicit deterministic engineering assumptions; it does not use random placeholder data.",
            "assumptions": ASSUMPTIONS,
        },
    }
    RESULT_PATH.parent.mkdir(parents=True, exist_ok=True)
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_artifacts(design, performance, av, mix)
    write_report(result)
    print(f"wrote {RESULT_PATH}")
    print(f"wrote {REPORT_PATH}")
    print(f"wrote artifacts under {ARTIFACT_DIR}")


if __name__ == "__main__":
    main()
