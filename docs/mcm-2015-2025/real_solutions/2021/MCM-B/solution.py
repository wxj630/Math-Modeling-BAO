from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import pandas as pd


ARCHIVE_ROOT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
PDF_PATH = ARCHIVE_ROOT / "official_assets" / "2021" / "Fighting Wildfires"
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"

DRONE_COST_AUD = 10000
HANDHELD_RANGE_FLAT_KM = 5
HANDHELD_RANGE_URBAN_KM = 2
REPEATER_RANGE_KM = 20
REPEATER_POWER_W = 10
REPEATER_WEIGHT_KG = 1.3

WILEE_DRONE = {
    "flight_range_km": 30,
    "max_speed_m_s": 20,
    "max_flight_time_hr": 2.50,
    "recharge_time_hr": 1.75,
    "auxiliary_battery_swap": True,
}

FIRE_EVENT_CLASSES = [
    {"event_class": "small grass/brush fire", "area_km2": 18, "annual_frequency": 18, "terrain_complexity": 0.34, "frontline_teams": 5},
    {"event_class": "medium forest interface fire", "area_km2": 85, "annual_frequency": 8, "terrain_complexity": 0.58, "frontline_teams": 12},
    {"event_class": "large eastern Victoria bushfire", "area_km2": 420, "annual_frequency": 3, "terrain_complexity": 0.78, "frontline_teams": 28},
    {"event_class": "extreme campaign fire", "area_km2": 1200, "annual_frequency": 0.8, "terrain_complexity": 0.92, "frontline_teams": 60},
]

TERRAINS = [
    {"terrain": "coastal plain", "area_km2": 120, "terrain_complexity": 0.30, "eoc_distance_km": 16},
    {"terrain": "rolling forest", "area_km2": 260, "terrain_complexity": 0.55, "eoc_distance_km": 24},
    {"terrain": "Mt. Bogong alpine terrain", "area_km2": 420, "terrain_complexity": 0.88, "eoc_distance_km": 36},
]


def clean_float(value: float, digits: int = 6) -> float:
    return round(float(value), digits)


def ensure_pdf_exists() -> None:
    if not PDF_PATH.exists():
        raise FileNotFoundError(f"Official problem PDF not found: {PDF_PATH}")


def drones_available_per_day() -> float:
    cycle = WILEE_DRONE["max_flight_time_hr"] + WILEE_DRONE["recharge_time_hr"]
    return 24.0 * WILEE_DRONE["max_flight_time_hr"] / cycle


def event_need(event: dict[str, Any]) -> dict[str, float]:
    radius = math.sqrt(float(event["area_km2"]) / math.pi)
    ssa_need = max(1.0, float(event["area_km2"]) / 90.0 + 0.10 * float(event["frontline_teams"]))
    repeater_need = max(1.0, radius / (REPEATER_RANGE_KM * (1.0 - 0.42 * float(event["terrain_complexity"]))))
    safety_weight = 1.0 + 0.55 * float(event["terrain_complexity"]) + 0.012 * float(event["frontline_teams"])
    return {"ssa_need": ssa_need, "repeater_need": repeater_need, "safety_weight": safety_weight}


def evaluate_mix(ssa_drones: int, repeater_drones: int, event_frequency_multiplier: float = 1.0) -> dict[str, Any]:
    availability = drones_available_per_day()
    capability_score = 0.0
    weighted_events = 0.0
    for event in FIRE_EVENT_CLASSES:
        need = event_need(event)
        ssa_service = min(1.0, ssa_drones * availability / max(need["ssa_need"] * 8.0, 1e-9))
        repeater_service = min(1.0, repeater_drones * availability / max(need["repeater_need"] * 8.0, 1e-9))
        mission_score = 0.46 * ssa_service + 0.40 * repeater_service + 0.14 * min(ssa_service, repeater_service)
        weight = float(event["annual_frequency"]) * event_frequency_multiplier * need["safety_weight"]
        capability_score += mission_score * weight
        weighted_events += weight
    capability_score /= max(weighted_events, 1e-9)
    cost_aud = (ssa_drones + repeater_drones) * DRONE_COST_AUD
    economics_penalty = min(0.22, cost_aud / 1_000_000.0 * 0.10)
    objective = capability_score - economics_penalty
    return {
        "ssa_drones": ssa_drones,
        "repeater_drones": repeater_drones,
        "total_drones": ssa_drones + repeater_drones,
        "purchase_cost_aud": cost_aud,
        "capability_safety_score": clean_float(capability_score, 4),
        "economics_penalty": clean_float(economics_penalty, 4),
        "objective_score": clean_float(objective, 4),
    }


def build_drone_mix_model() -> tuple[pd.DataFrame, dict[str, Any]]:
    rows = []
    for ssa in range(2, 19):
        for repeater in range(2, 19):
            rows.append(evaluate_mix(ssa, repeater))
    df = pd.DataFrame(rows).sort_values("objective_score", ascending=False)
    df.to_csv(ARTIFACT_DIR / "drone_mix_optimization.csv", index=False)
    recommended = df.iloc[0].to_dict()
    event_rows = []
    for event in FIRE_EVENT_CLASSES:
        need = event_need(event)
        event_rows.append(
            {
                **event,
                "estimated_ssa_need": clean_float(need["ssa_need"], 3),
                "estimated_repeater_need": clean_float(need["repeater_need"], 3),
                "safety_weight": clean_float(need["safety_weight"], 3),
            }
        )
    return df, {
        "method": "grid search over SSA and radio-repeater drone counts balancing capability, safety, mission need, topography, fire size/frequency, and economics",
        "recommended_mix": recommended,
        "event_need_rows": event_rows,
        "top_candidate_rows": df.head(12).to_dict(orient="records"),
    }


def build_decade_projection(recommended: dict[str, Any]) -> tuple[pd.DataFrame, dict[str, Any]]:
    rows = []
    base_cost = float(recommended["purchase_cost_aud"])
    for year in range(1, 11):
        extreme_multiplier = 1.0 + 0.055 * (year - 1)
        evaluated = evaluate_mix(int(recommended["ssa_drones"]), int(recommended["repeater_drones"]), event_frequency_multiplier=extreme_multiplier)
        added_repeater = 0
        added_ssa = 0
        if evaluated["capability_safety_score"] < 0.82:
            added_repeater = math.ceil((0.82 - evaluated["capability_safety_score"]) * 12)
            added_ssa = math.ceil((0.82 - evaluated["capability_safety_score"]) * 9)
        rows.append(
            {
                "year": year,
                "extreme_fire_likelihood_multiplier": clean_float(extreme_multiplier, 3),
                "added_ssa_drones": added_ssa,
                "added_repeater_drones": added_repeater,
                "cumulative_equipment_cost_aud": clean_float(base_cost + (added_ssa + added_repeater) * DRONE_COST_AUD, 2),
                "capability_safety_score_before_purchase": evaluated["capability_safety_score"],
            }
        )
    df = pd.DataFrame(rows)
    df.to_csv(ARTIFACT_DIR / "decade_cost_projection.csv", index=False)
    return df, {
        "method": "increase extreme-event likelihood each year while drone unit cost remains constant, then add equipment if capability drops below the target band",
        "projection_rows": df.to_dict(orient="records"),
    }


def build_repeater_locations() -> tuple[pd.DataFrame, dict[str, Any]]:
    rows = []
    for terrain in TERRAINS:
        effective_range = REPEATER_RANGE_KM * (1.0 - 0.38 * float(terrain["terrain_complexity"]))
        coverage_area = math.pi * effective_range**2
        required = max(1, math.ceil(float(terrain["area_km2"]) / max(coverage_area * 0.72, 1e-9)))
        eoc_chain = max(0, math.ceil(float(terrain["eoc_distance_km"]) / max(effective_range, 1e-9)) - 1)
        rows.append(
            {
                **terrain,
                "effective_repeater_range_km": clean_float(effective_range, 3),
                "coverage_area_per_drone_km2": clean_float(coverage_area, 2),
                "coverage_repeaters_required": required,
                "eoc_relay_chain_repeaters": eoc_chain,
                "recommended_hover_pattern": "ridge line chain" if terrain["terrain_complexity"] > 0.75 else "triangular perimeter with one EOC-facing relay",
            }
        )
    df = pd.DataFrame(rows)
    df.to_csv(ARTIFACT_DIR / "repeater_location_plan.csv", index=False)
    return df, {
        "method": "terrain-adjusted coverage radius and EOC relay-chain count using the official 20 km repeater range",
        "terrain_rows": df.to_dict(orient="records"),
    }


def build_budget_request(recommended: dict[str, Any], decade_projection: dict[str, Any]) -> tuple[pd.DataFrame, str]:
    rows = [
        {"item": "SSA drones", "count": int(recommended["ssa_drones"]), "unit_cost_aud": DRONE_COST_AUD, "justification": "thermal/video situational awareness and wearable telemetry monitoring"},
        {"item": "radio repeater drones", "count": int(recommended["repeater_drones"]), "unit_cost_aud": DRONE_COST_AUD, "justification": "20 km VHF/UHF relay coverage for forward teams and EOC"},
        {"item": "training and spares reserve", "count": 1, "unit_cost_aud": clean_float(0.18 * float(recommended["purchase_cost_aud"]), 2), "justification": "battery rotations, auxiliary payload swaps, operators, and field maintenance"},
    ]
    df = pd.DataFrame(rows)
    df["line_total_aud"] = df["count"] * df["unit_cost_aud"]
    df.to_csv(ARTIFACT_DIR / "annotated_budget_request.csv", index=False)
    total = clean_float(float(df["line_total_aud"].sum()), 2)
    request = (
        "Annotated Budget Request to the Victoria State Government: CFA Rapid Bushfire Response requests "
        f"AUD {total} for an initial drone division. The request purchases {int(recommended['ssa_drones'])} SSA drones and "
        f"{int(recommended['repeater_drones'])} radio-repeater drones at the official AUD {DRONE_COST_AUD} unit cost, plus a training and spares reserve. "
        "The mix balances surveillance, communications, topography, event size, event frequency, firefighter safety, and economics. "
        "A decade projection is included because increasing extreme fire likelihood can require extra equipment even when drone unit cost stays constant."
    )
    return df, request


def write_frontier(mix_df: pd.DataFrame) -> None:
    best_by_total = mix_df.sort_values("objective_score", ascending=False).groupby("total_drones").head(1).sort_values("total_drones")
    fig, ax = plt.subplots(figsize=(8.0, 5.0))
    ax.plot(best_by_total["purchase_cost_aud"], best_by_total["capability_safety_score"], marker="o", color="#355c7d")
    ax.set_xlabel("Purchase cost (AUD)")
    ax.set_ylabel("Capability and safety score")
    ax.set_title("Rapid Bushfire Response Drone Budget Frontier")
    ax.grid(alpha=0.22)
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "wildfire_budget_frontier.png", dpi=180)
    plt.close(fig)


def build_result(drone_mix: dict[str, Any], decade_projection: dict[str, Any], repeater_locations: dict[str, Any], budget_request: str) -> dict[str, Any]:
    return {
        "problem_id": "2021-B",
        "title": "Fighting Wildfires",
        "data_source": {
            "type": "official_statement_parameters",
            "root": str(ARCHIVE_ROOT / "official_assets"),
            "source_pdf": str(PDF_PATH),
            "official_requirements": {
                "ssa_and_repeater_drone_mix": True,
                "balance_capability_safety_economics": True,
                "fire_size_frequency_parameters": True,
                "decade_extreme_fire_likelihood": True,
                "radio_repeater_locations_by_terrain": True,
                "annotated_budget_request": True,
            },
            "parameters": {
                "drone_cost_aud": DRONE_COST_AUD,
                "handheld_range_flat_km": HANDHELD_RANGE_FLAT_KM,
                "handheld_range_urban_km": HANDHELD_RANGE_URBAN_KM,
                "repeater_range_km": REPEATER_RANGE_KM,
                "repeater_power_w": REPEATER_POWER_W,
                "repeater_weight_kg": REPEATER_WEIGHT_KG,
                "wilee_drone": WILEE_DRONE,
                "source_note": "Official PDF statement parameters only; fire-event rows and terrain rows are deterministic planning scenarios.",
            },
        },
        "drone_mix_model": drone_mix,
        "decade_projection": decade_projection,
        "repeater_location_model": repeater_locations,
        "budget_request": budget_request,
        "assumption_audit": {
            "truthfulness_note": "This workflow uses official statement parameters and deterministic planning scenarios; it does not invent random x1/x2/x3 placeholder data.",
            "model_limits": [
                "COMAP did not provide geospatial fire perimeters, topography rasters, or CFA incident logs.",
                "Fire classes and terrain rows are transparent planning scenarios calibrated to the official drone/radio constraints.",
                "A deployment-ready model should add GIS line-of-sight, crew rosters, wind, smoke, and aircraft deconfliction rules.",
            ],
        },
    }


def build_report(result: dict[str, Any]) -> None:
    mix = result["drone_mix_model"]["recommended_mix"]
    lines = [
        "# 2021 MCM-B Fighting Wildfires",
        "",
        "## 数据真实性",
        f"- 官方来源：`{result['data_source']['source_pdf']}`。",
        "- 本题无 COMAP 数值附件；脚本只使用官方题面中的无人机、无线电和任务参数，以及显式确定性火场情景。",
        "",
        "## 推荐装备组合",
        f"- SSA drones：{mix['ssa_drones']}；Radio repeater drones：{mix['repeater_drones']}；cost：{mix['purchase_cost_aud']} AUD。",
        f"- 方法：{result['drone_mix_model']['method']}。",
        "",
        "## 十年投影与中继布点",
        f"- 十年投影：{result['decade_projection']['method']}。",
        f"- 布点模型：{result['repeater_location_model']['method']}。",
        "",
        "## 预算请求摘录",
        result["budget_request"],
        "",
        "## 输出产物",
        "- `drone_mix_optimization.csv`：SSA/Repeater 组合搜索。",
        "- `decade_cost_projection.csv`：极端火灾概率变化下的十年成本。",
        "- `repeater_location_plan.csv`：地形调整的中继无人机布点。",
        "- `annotated_budget_request.csv`：预算条目与注释。",
        "- `wildfire_budget_frontier.png`：预算-能力安全前沿图。",
    ]
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ensure_pdf_exists()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    mix_df, drone_mix = build_drone_mix_model()
    _, decade = build_decade_projection(drone_mix["recommended_mix"])
    _, repeater = build_repeater_locations()
    _, budget = build_budget_request(drone_mix["recommended_mix"], decade)
    write_frontier(mix_df)
    result = build_result(drone_mix, decade, repeater, budget)
    result["artifacts"] = {
        "drone_mix_optimization": str(ARTIFACT_DIR / "drone_mix_optimization.csv"),
        "decade_cost_projection": str(ARTIFACT_DIR / "decade_cost_projection.csv"),
        "repeater_location_plan": str(ARTIFACT_DIR / "repeater_location_plan.csv"),
        "annotated_budget_request": str(ARTIFACT_DIR / "annotated_budget_request.csv"),
        "wildfire_budget_frontier": str(ARTIFACT_DIR / "wildfire_budget_frontier.png"),
    }
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    build_report(result)
    print(json.dumps({"result": str(RESULT_PATH), "report": str(REPORT_PATH), "artifacts": str(ARTIFACT_DIR)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
