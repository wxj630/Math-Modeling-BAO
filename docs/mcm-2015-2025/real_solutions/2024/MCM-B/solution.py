from __future__ import annotations

import json
import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ARCHIVE_ROOT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
PDF_PATH = ARCHIVE_ROOT / "official_assets_extracted" / "2024" / "Searching for Submersibles.pdf"
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"

HOURS = list(range(0, 25, 2))
SEARCH_DETECTION_REALISM_FACTOR = 0.16

SCENARIO_ASSUMPTIONS = {
    "purpose": "deterministic rescue-planning example for the official PDF-only problem; not observed incident data",
    "deployment_area": "Ionian Sea tourist wreck-search site near a host ship",
    "initial_fix_error_km": 0.18,
    "submersible_speed_kmh_before_failure": 3.0,
    "time_since_last_fix_hours": 0.5,
    "surface_current_kmh": 1.15,
    "deep_current_kmh": 0.35,
    "current_direction_degrees": 58.0,
    "current_uncertainty_kmh": 0.24,
    "cross_current_uncertainty_kmh": 0.14,
    "depth_state_ambiguity_km": 0.55,
    "seafloor_terrain_uncertainty_km": 0.35,
    "neutral_buoyancy_share": 0.55,
    "seafloor_share": 0.45,
    "acoustic_range_km": 4.0,
}

SEARCH_ASSETS = [
    {
        "asset": "shipboard USBL acoustic locator",
        "availability": "must be aboard host ship",
        "maintenance": "medium: calibration before tourist dives",
        "readiness_hours": 0.25,
        "usage_cost_index": 2.0,
        "coverage_km2_per_hour": 7.5,
        "quality": 0.72,
        "role": "quickly interrogate emergency pingers and reduce horizontal uncertainty",
    },
    {
        "asset": "drop transponder/LBL beacons",
        "availability": "portable kit aboard host ship",
        "maintenance": "low-to-medium: battery and timing checks",
        "readiness_hours": 0.8,
        "usage_cost_index": 2.8,
        "coverage_km2_per_hour": 4.2,
        "quality": 0.80,
        "role": "create a local acoustic baseline around the predicted ellipse",
    },
    {
        "asset": "side-scan sonar towfish",
        "availability": "host ship or nearby contracted survey vessel",
        "maintenance": "medium: tow cable, fish, and winch inspection",
        "readiness_hours": 1.2,
        "usage_cost_index": 3.3,
        "coverage_km2_per_hour": 5.8,
        "quality": 0.68,
        "role": "scan seafloor-likely sectors when the submersible has lost propulsion",
    },
    {
        "asset": "inspection-class ROV",
        "availability": "host ship if tourist operation is approved",
        "maintenance": "high: tether, thrusters, cameras, manipulator",
        "readiness_hours": 1.5,
        "usage_cost_index": 4.2,
        "coverage_km2_per_hour": 1.4,
        "quality": 0.92,
        "role": "confirm contact and attach lift, air, or communication line",
    },
    {
        "asset": "AUV with multibeam sonar",
        "availability": "rescue vessel or prearranged regional contractor",
        "maintenance": "high: mission planning, batteries, recovery crew",
        "readiness_hours": 5.0,
        "usage_cost_index": 5.0,
        "coverage_km2_per_hour": 10.5,
        "quality": 0.75,
        "role": "expand search when the first host-ship pattern fails",
    },
]


def clean_float(value: float, digits: int = 6) -> float:
    return round(float(value), digits)


def ensure_pdf_exists() -> None:
    if not PDF_PATH.exists():
        raise FileNotFoundError(f"Official problem PDF not found: {PDF_PATH}")


def drift_center(hour: float) -> tuple[float, float]:
    direction = math.radians(SCENARIO_ASSUMPTIONS["current_direction_degrees"])
    mixed_current = (
        SCENARIO_ASSUMPTIONS["neutral_buoyancy_share"] * SCENARIO_ASSUMPTIONS["deep_current_kmh"]
        + SCENARIO_ASSUMPTIONS["seafloor_share"] * 0.12
    )
    east = mixed_current * hour * math.sin(direction)
    north = mixed_current * hour * math.cos(direction)
    return east, north


def uncertainty_axes(hour: float) -> tuple[float, float]:
    initial = SCENARIO_ASSUMPTIONS["initial_fix_error_km"]
    dead_reckoning = SCENARIO_ASSUMPTIONS["submersible_speed_kmh_before_failure"] * SCENARIO_ASSUMPTIONS["time_since_last_fix_hours"]
    along = math.sqrt(
        initial**2
        + (0.55 * dead_reckoning) ** 2
        + (SCENARIO_ASSUMPTIONS["current_uncertainty_kmh"] * hour) ** 2
        + SCENARIO_ASSUMPTIONS["depth_state_ambiguity_km"] ** 2
    )
    cross = math.sqrt(
        initial**2
        + (0.25 * dead_reckoning) ** 2
        + (SCENARIO_ASSUMPTIONS["cross_current_uncertainty_kmh"] * hour) ** 2
        + SCENARIO_ASSUMPTIONS["seafloor_terrain_uncertainty_km"] ** 2
    )
    return along, cross


def build_position_uncertainty() -> pd.DataFrame:
    rows = []
    for hour in HOURS:
        east, north = drift_center(hour)
        major, minor = uncertainty_axes(hour)
        area = math.pi * major * minor
        rows.append(
            {
                "hour_after_loss": hour,
                "center_east_km": clean_float(east, 4),
                "center_north_km": clean_float(north, 4),
                "major_axis_km": clean_float(major, 4),
                "minor_axis_km": clean_float(minor, 4),
                "position_uncertainty_area_km2": clean_float(area, 4),
                "dominant_uncertainty": "current drift + depth-state ambiguity",
            }
        )
    df = pd.DataFrame(rows)
    df.to_csv(ARTIFACT_DIR / "position_uncertainty.csv", index=False)
    return df


def build_equipment_tradeoffs() -> pd.DataFrame:
    df = pd.DataFrame(SEARCH_ASSETS)
    df["readiness_penalty"] = df["readiness_hours"] / df["readiness_hours"].max()
    df["cost_penalty"] = df["usage_cost_index"] / df["usage_cost_index"].max()
    df["search_value_score"] = (
        0.42 * df["quality"]
        + 0.36 * df["coverage_km2_per_hour"] / df["coverage_km2_per_hour"].max()
        - 0.12 * df["readiness_penalty"]
        - 0.10 * df["cost_penalty"]
    ).round(4)
    df.to_csv(ARTIFACT_DIR / "equipment_tradeoffs.csv", index=False)
    return df


def deployment_points(position_df: pd.DataFrame) -> list[dict[str, object]]:
    row12 = position_df[position_df["hour_after_loss"] == 12].iloc[0]
    cx = float(row12["center_east_km"])
    cy = float(row12["center_north_km"])
    major = float(row12["major_axis_km"])
    minor = float(row12["minor_axis_km"])
    direction = math.radians(SCENARIO_ASSUMPTIONS["current_direction_degrees"])
    along = np.array([math.sin(direction), math.cos(direction)])
    cross = np.array([math.cos(direction), -math.sin(direction)])
    center = np.array([cx, cy])
    points = [
        ("P0 predicted center", center, "deploy USBL and first drop beacon"),
        ("P1 down-current ellipse focus", center + 0.62 * major * along, "start creeping-line sonar along drift axis"),
        ("P2 up-current ellipse focus", center - 0.42 * major * along, "backtrack possible powerless descent path"),
        ("P3 cross-current high-uncertainty edge", center + 0.78 * minor * cross, "cover terrain and density-current ambiguity"),
        ("P4 opposite cross-current edge", center - 0.78 * minor * cross, "complete LBL bracket and close acoustic geometry"),
    ]
    return [
        {
            "point": name,
            "east_km": clean_float(float(vec[0]), 3),
            "north_km": clean_float(float(vec[1]), 3),
            "purpose": purpose,
        }
        for name, vec, purpose in points
    ]


def probability_after_search(area_km2: float, asset_rows: list[dict[str, object]], hours_available: float) -> tuple[float, float]:
    remaining = max(0.0, hours_available)
    cumulative_effective_area = 0.0
    for asset in asset_rows:
        ready = float(asset["readiness_hours"])
        if remaining <= ready:
            continue
        work_hours = min(remaining - ready, 6.0)
        cumulative_effective_area += work_hours * float(asset["coverage_km2_per_hour"]) * float(asset["quality"]) * SEARCH_DETECTION_REALISM_FACTOR
        remaining -= work_hours
    probability = 1.0 - math.exp(-cumulative_effective_area / max(area_km2, 0.1))
    return min(0.995, probability), cumulative_effective_area


def build_search_plan(position_df: pd.DataFrame, equipment_df: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, object]]:
    selected_assets = [
        equipment_df[equipment_df["asset"] == "shipboard USBL acoustic locator"].iloc[0].to_dict(),
        equipment_df[equipment_df["asset"] == "drop transponder/LBL beacons"].iloc[0].to_dict(),
        equipment_df[equipment_df["asset"] == "side-scan sonar towfish"].iloc[0].to_dict(),
        equipment_df[equipment_df["asset"] == "inspection-class ROV"].iloc[0].to_dict(),
        equipment_df[equipment_df["asset"] == "AUV with multibeam sonar"].iloc[0].to_dict(),
    ]
    rows = []
    cumulative_hazard = 0.0
    previous_effective_area = 0.0
    for hour in [4, 8, 12, 16, 20, 24]:
        area = float(np.interp(hour, position_df["hour_after_loss"], position_df["position_uncertainty_area_km2"]))
        _, effective_area = probability_after_search(area, selected_assets, hour)
        incremental_effective_area = max(0.0, effective_area - previous_effective_area)
        cumulative_hazard += incremental_effective_area / max(area, 0.1)
        probability = min(0.995, 1.0 - math.exp(-cumulative_hazard))
        previous_effective_area = effective_area
        rows.append(
            {
                "hour_after_loss": hour,
                "uncertainty_area_km2": clean_float(area, 4),
                "cumulative_effective_swept_area_km2": clean_float(effective_area, 4),
                "cumulative_detection_hazard": clean_float(cumulative_hazard, 4),
                "probability_found": clean_float(probability, 4),
                "posterior_not_found": clean_float(1.0 - probability, 4),
            }
        )
    df = pd.DataFrame(rows)
    df.to_csv(ARTIFACT_DIR / "search_probability.csv", index=False)
    points = deployment_points(position_df)
    summary = {
        "model": "Bayesian-style survival update with deterministic swept-area coverage over the official location-model uncertainty ellipse",
        "search_probability": {
            "probability_found_by_12h": clean_float(float(df[df["hour_after_loss"] == 12]["probability_found"].iloc[0]), 4),
            "probability_found_by_24h": clean_float(float(df[df["hour_after_loss"] == 24]["probability_found"].iloc[0]), 4),
            "formula": "P_found(t)=1-exp(-sum_over_intervals(incremental_effective_swept_area/current_uncertainty_area))",
            "detection_realism_factor": SEARCH_DETECTION_REALISM_FACTOR,
            "detection_realism_note": "discounts nominal sensor sweep area for deep-water 3D ambiguity, acoustic multipath, terrain shadowing, and contact-confirmation delay",
        },
        "deployment_points": points,
        "search_pattern": [
            "0-2 h: interrogate acoustic pingers from the host ship and deploy two LBL beacons around P0/P1",
            "2-8 h: run creeping-line side-scan sonar along the drift-axis ellipse from P1 to P2",
            "8-16 h: use ROV to inspect acoustic/sonar contacts and seafloor terrain traps",
            "16-24 h: add AUV expanding-square search around remaining posterior mass if no confirmed contact",
        ],
    }
    write_search_plot(position_df, df, points)
    return df, summary


def write_search_plot(position_df: pd.DataFrame, probability_df: pd.DataFrame, points: list[dict[str, object]]) -> None:
    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(11.0, 4.8))
    theta = np.linspace(0.0, 2.0 * math.pi, 240)
    for hour in [4, 12, 24]:
        row = position_df[position_df["hour_after_loss"] == hour].iloc[0]
        x = float(row["center_east_km"]) + float(row["major_axis_km"]) * np.cos(theta)
        y = float(row["center_north_km"]) + float(row["minor_axis_km"]) * np.sin(theta)
        ax0.plot(x, y, label=f"{hour} h ellipse")
    for point in points:
        ax0.scatter(point["east_km"], point["north_km"], s=36)
        ax0.text(point["east_km"], point["north_km"], point["point"].split()[0], fontsize=8)
    ax0.set_title("Deterministic Search Ellipses")
    ax0.set_xlabel("East of last fix (km)")
    ax0.set_ylabel("North of last fix (km)")
    ax0.grid(alpha=0.25)
    ax0.legend(fontsize=8)

    ax1.plot(probability_df["hour_after_loss"], probability_df["probability_found"], marker="o", color="#2f6f73")
    ax1.set_ylim(0.0, 1.0)
    ax1.set_title("Probability of Location vs Time")
    ax1.set_xlabel("Hours after communication loss")
    ax1.set_ylabel("Probability found")
    ax1.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "search_plan.png", dpi=180)
    plt.close(fig)


def build_location_model(position_df: pd.DataFrame) -> dict[str, object]:
    row12 = position_df[position_df["hour_after_loss"] == 12].iloc[0].to_dict()
    row24 = position_df[position_df["hour_after_loss"] == 24].iloc[0].to_dict()
    return {
        "model": "current-driven dead-reckoning ellipse with two vertical states: seafloor-resting and neutral-buoyancy drifting",
        "scenario_assumptions": SCENARIO_ASSUMPTIONS,
        "position_uncertainty": {
            "area_km2_after_12h": row12["position_uncertainty_area_km2"],
            "area_km2_after_24h": row24["position_uncertainty_area_km2"],
            "center_after_12h_km": [row12["center_east_km"], row12["center_north_km"]],
            "dominant_uncertainties": [
                "unknown vertical state: seafloor versus neutral buoyancy",
                "current magnitude and direction",
                "time since last accurate fix",
                "seafloor terrain trapping and density layers",
            ],
        },
        "telemetry_to_reduce_uncertainty": [
            {
                "signal": "acoustic pinger range/bearing packet",
                "equipment": "coded acoustic modem and emergency pinger",
                "uncertainty_reduced": "horizontal range and bearing from host ship",
            },
            {
                "signal": "depth and pressure time series",
                "equipment": "pressure sensor with logged acoustic burst",
                "uncertainty_reduced": "distinguishes seafloor contact from neutral-buoyancy drift",
            },
            {
                "signal": "inertial dead-reckoning summary",
                "equipment": "IMU, compass, Doppler velocity log where available",
                "uncertainty_reduced": "motion after last GPS/USBL fix",
            },
            {
                "signal": "battery, ballast, and propulsion health flags",
                "equipment": "fault monitor tied to acoustic status messages",
                "uncertainty_reduced": "likely mobility, ascent ability, and rescue urgency",
            },
            {
                "signal": "local current and temperature-density observations",
                "equipment": "compact current/CTD package",
                "uncertainty_reduced": "drift model and density-layer uncertainty",
            },
        ],
    }


def build_equipment_recommendations(equipment_df: pd.DataFrame) -> dict[str, object]:
    host = equipment_df.sort_values("search_value_score", ascending=False).head(4)
    rescue = [
        {
            "asset": "work-class ROV with lift/umbilical tools",
            "reason": "needed for confirmed deep contact, intervention, and connection to lifting or life-support systems",
        },
        {
            "asset": "dynamic-positioning rescue vessel",
            "reason": "keeps the rescue platform over the contact while operating tethered tools",
        },
        {
            "asset": "medical decompression and survivor reception team",
            "reason": "turns a location success into safe recovery and post-rescue care",
        },
    ]
    return {
        "model": "multi-criteria equipment scoring over coverage, detection quality, readiness, usage cost, and maintenance burden",
        "host_ship_equipment": host[
            ["asset", "availability", "maintenance", "readiness_hours", "usage_cost_index", "coverage_km2_per_hour", "quality", "search_value_score", "role"]
        ].to_dict(orient="records"),
        "rescue_vessel_equipment": rescue,
        "recommendation": "The host ship should carry acoustic localization, drop beacons, a side-scan option, and an inspection ROV; heavier lift and intervention assets can be pre-contracted for rescue-vessel arrival.",
    }


def build_extrapolation() -> dict[str, object]:
    return {
        "caribbean_adjustments": {
            "current_uncertainty_multiplier": 1.35,
            "terrain_adjustment": "replace Ionian seafloor-wreck bathymetry with reef wall, trench, and strong surface-current layers",
            "communications_adjustment": "predefine tourist-route LBL boxes because warm shallow shelves may create more multipath and recreational vessel noise",
            "environmental_data_needed": ["regional current forecast", "reef/trench bathymetry", "shipping density", "hurricane-season operating rule"],
        },
        "multi_submersible": {
            "coordination_rule": "assign each submersible a unique acoustic code, maintain non-overlapping safety corridors, and partition the search posterior into Voronoi sectors around last confirmed fixes",
            "model_change": "state vector becomes one ellipse per submersible plus a collision/communication interference constraint matrix",
            "search_allocation": "prioritize sectors by expected lives saved per hour: posterior probability mass divided by deployment time and resource conflicts",
        },
    }


def build_result(position_df: pd.DataFrame, equipment_df: pd.DataFrame, probability_df: pd.DataFrame, search_plan: dict[str, object]) -> dict[str, object]:
    return {
        "problem_id": "2024-B",
        "title": "Searching for Submersibles",
        "data_source": {
            "type": "official_statement_parameters",
            "root": str(ARCHIVE_ROOT / "official_assets_extracted"),
            "source_pdf": str(PDF_PATH),
            "official_requirements": {
                "loss_of_communication": True,
                "possible_loss_of_propulsion": True,
                "predict_location_over_time": True,
                "seafloor_or_neutral_buoyancy": True,
                "currents_densities_and_geography": True,
                "prepare_search_equipment": True,
                "probability_of_finding_as_function_of_time": True,
                "caribbean_and_multiple_submersibles": True,
                "memo_to_greek_government": True,
            },
            "parameters": SCENARIO_ASSUMPTIONS,
        },
        "location_model": build_location_model(position_df),
        "equipment_recommendations": build_equipment_recommendations(equipment_df),
        "search_plan": search_plan,
        "extrapolation": build_extrapolation(),
        "government_memo": (
            "Memo to the Greek government: MCMS approval should require an auditable lost-submersible plan with periodic acoustic "
            "telemetry, a host-ship localization kit, preplanned deployment points, a probability-updated search log, and a rescue-vessel "
            "mobilization trigger when the 12-hour posterior still leaves substantial uncertainty."
        ),
        "artifact_preview": {
            "position_rows": position_df.head(4).to_dict(orient="records"),
            "equipment_rows": equipment_df.sort_values("search_value_score", ascending=False).head(3).to_dict(orient="records"),
            "search_probability_rows": probability_df.to_dict(orient="records"),
        },
    }


def build_report(result: dict[str, object]) -> None:
    lines = [
        "# 2024 MCM-B Searching for Submersibles",
        "",
        "## 数据真实性",
        f"- 官方来源：`{result['data_source']['source_pdf']}`。",
        "- 本题无 COMAP 数值附件；脚本只使用官方 PDF 任务约束和显式救援预案情景，不使用随机占位数据。",
        "- `scenario_assumptions` 是可替换的确定性预案参数，不是声称采集到的真实事故观测。",
        "",
        "## 每问建模与结果",
        "### Q1 Locate",
        f"- 模型：{result['location_model']['model']}。",
        f"- 12 小时不确定区域：{result['location_model']['position_uncertainty']['area_km2_after_12h']} km^2。",
        f"- 24 小时不确定区域：{result['location_model']['position_uncertainty']['area_km2_after_24h']} km^2。",
        "- 减小不确定性的遥测：",
    ]
    lines.extend([f"- {item['signal']}：{item['uncertainty_reduced']}。" for item in result["location_model"]["telemetry_to_reduce_uncertainty"]])
    lines.extend([
        "",
        "### Q2 Prepare",
        f"- 模型：{result['equipment_recommendations']['model']}。",
        f"- 推荐：{result['equipment_recommendations']['recommendation']}",
        "",
        "### Q3 Search",
        f"- 模型：{result['search_plan']['model']}。",
        f"- 24 小时发现概率：{result['search_plan']['search_probability']['probability_found_by_24h']}。",
        "- 初始部署点：",
    ])
    lines.extend([f"- {point['point']}：east={point['east_km']} km, north={point['north_km']} km，{point['purpose']}。" for point in result["search_plan"]["deployment_points"]])
    lines.extend([
        "",
        "### Q4 Extrapolate",
        f"- 加勒比海洋流不确定性倍数：{result['extrapolation']['caribbean_adjustments']['current_uncertainty_multiplier']}。",
        f"- 多潜水器协调规则：{result['extrapolation']['multi_submersible']['coordination_rule']}。",
        "",
        "## 给监管方备忘录核心句",
        result["government_memo"],
        "",
        "## 输出产物",
        "- `position_uncertainty.csv`：随时间扩张的位置不确定性椭圆。",
        "- `equipment_tradeoffs.csv`：主船与救援装备的覆盖、成本、维护和准备度权衡。",
        "- `search_probability.csv`：随时间累计搜索后的发现概率。",
        "- `search_plan.png`：搜索椭圆、部署点和发现概率曲线。",
    ])
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ensure_pdf_exists()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    position_df = build_position_uncertainty()
    equipment_df = build_equipment_tradeoffs()
    probability_df, search_plan = build_search_plan(position_df, equipment_df)
    result = build_result(position_df, equipment_df, probability_df, search_plan)
    result["artifacts"] = {
        "position_uncertainty": str(ARTIFACT_DIR / "position_uncertainty.csv"),
        "equipment_tradeoffs": str(ARTIFACT_DIR / "equipment_tradeoffs.csv"),
        "search_probability": str(ARTIFACT_DIR / "search_probability.csv"),
        "search_plan": str(ARTIFACT_DIR / "search_plan.png"),
    }
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    build_report(result)
    print(json.dumps({"result": str(RESULT_PATH), "report": str(REPORT_PATH), "artifacts": str(ARTIFACT_DIR)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
