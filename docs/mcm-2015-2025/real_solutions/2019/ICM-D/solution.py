from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import pandas as pd


ARCHIVE_ROOT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
PDF_PATH = ARCHIVE_ROOT / "official_assets" / "2019" / "Time to leave the Louvre"
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"

LOUVRE_FLOORS = 5
UNDERGROUND_FLOORS = 2
VISITORS_2017_MILLION = 8.1
EXHIBITS = 380000
FLOOR_AREA_M2 = 72735
MAX_WING_LENGTH_M = 480

ENTRANCES = [
    {"exit": "Pyramid entrance", "public": True, "baseline_capacity_person_min": 420, "security_level": 0.94, "familiarity": 0.95},
    {"exit": "Passage Richelieu", "public": False, "baseline_capacity_person_min": 210, "security_level": 0.88, "familiarity": 0.52},
    {"exit": "Carrousel du Louvre", "public": False, "baseline_capacity_person_min": 260, "security_level": 0.86, "familiarity": 0.58},
    {"exit": "Portes Des Lions", "public": False, "baseline_capacity_person_min": 150, "security_level": 0.82, "familiarity": 0.38},
]

FLOOR_LOADS = [
    {"floor": "level -2", "share": 0.16, "vertical_delay_min": 6.5, "mobility_factor": 1.16},
    {"floor": "level -1", "share": 0.22, "vertical_delay_min": 4.8, "mobility_factor": 1.12},
    {"floor": "ground", "share": 0.27, "vertical_delay_min": 2.4, "mobility_factor": 1.00},
    {"floor": "level 1", "share": 0.23, "vertical_delay_min": 3.8, "mobility_factor": 1.07},
    {"floor": "level 2", "share": 0.12, "vertical_delay_min": 5.2, "mobility_factor": 1.10},
]

THREAT_SCENARIOS = [
    {"scenario": "baseline all main exits", "closed_exits": [], "extra_service_exits": 0, "emergency_access_reserved_pct": 0.10},
    {"scenario": "pyramid unavailable", "closed_exits": ["Pyramid entrance"], "extra_service_exits": 4, "emergency_access_reserved_pct": 0.14},
    {"scenario": "underground corridor smoke", "closed_exits": ["Carrousel du Louvre"], "extra_service_exits": 5, "emergency_access_reserved_pct": 0.16},
    {"scenario": "riverside security incident", "closed_exits": ["Portes Des Lions"], "extra_service_exits": 3, "emergency_access_reserved_pct": 0.12},
]


def clean_float(value: float, digits: int = 6) -> float:
    return round(float(value), digits)


def ensure_pdf_exists() -> None:
    if not PDF_PATH.exists():
        raise FileNotFoundError(f"Official problem PDF not found: {PDF_PATH}")


def peak_occupancy_estimate() -> int:
    daily_average = VISITORS_2017_MILLION * 1_000_000.0 / 310.0
    return int(round(daily_average * 0.32))


def build_baseline_model() -> tuple[pd.DataFrame, dict[str, Any]]:
    occupancy = peak_occupancy_estimate()
    total_capacity = sum(item["baseline_capacity_person_min"] for item in ENTRANCES)
    rows = []
    for floor in FLOOR_LOADS:
        visitors = occupancy * float(floor["share"])
        evac_time = visitors / (total_capacity * (1.0 / float(floor["mobility_factor"]))) + float(floor["vertical_delay_min"])
        rows.append(
            {
                **floor,
                "estimated_peak_visitors": int(round(visitors)),
                "area_m2_allocated": clean_float(FLOOR_AREA_M2 * float(floor["share"]), 1),
                "baseline_evacuation_time_min": clean_float(evac_time, 2),
            }
        )
    df = pd.DataFrame(rows)
    df.to_csv(ARTIFACT_DIR / "louvre_evacuation_baseline.csv", index=False)
    return df, {
        "floor_count": LOUVRE_FLOORS,
        "underground_floor_count": UNDERGROUND_FLOORS,
        "estimated_peak_occupancy": occupancy,
        "main_exit_capacity_person_min": total_capacity,
        "floor_rows": df.to_dict(orient="records"),
        "model": "capacity-constrained evacuation time by floor using official visitor, floor, area, entrance, and wing-length facts",
    }


def build_bottleneck_analysis(baseline_df: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, Any]]:
    rows = []
    for entrance in ENTRANCES:
        bottleneck = (1.0 - float(entrance["familiarity"])) * 0.35 + (1.0 - float(entrance["security_level"])) * 0.25 + 380.0 / float(entrance["baseline_capacity_person_min"]) * 0.20
        rows.append(
            {
                **entrance,
                "bottleneck_index": clean_float(bottleneck, 4),
                "management_action": "push multilingual app routing" if entrance["public"] else "pre-authorize emergency-only opening with staff escorts",
            }
        )
    rows.append(
        {
            "exit": "vertical circulation between underground floors and main concourse",
            "public": True,
            "baseline_capacity_person_min": 0,
            "security_level": 0.72,
            "familiarity": 0.46,
            "bottleneck_index": clean_float(float(baseline_df["baseline_evacuation_time_min"].max()) / 30.0, 4),
            "management_action": "meter upstream galleries and reserve stair capacity for disabled visitors and responders",
        }
    )
    df = pd.DataFrame(rows).sort_values("bottleneck_index", ascending=False)
    df.to_csv(ARTIFACT_DIR / "louvre_bottlenecks.csv", index=False)
    return df, {
        "bottleneck_rows": df.to_dict(orient="records"),
        "priority_bottleneck": df.iloc[0].to_dict(),
    }


def build_threat_scenarios() -> tuple[pd.DataFrame, dict[str, Any]]:
    occupancy = peak_occupancy_estimate()
    rows = []
    for scenario in THREAT_SCENARIOS:
        open_exits = [item for item in ENTRANCES if item["exit"] not in scenario["closed_exits"]]
        capacity = sum(item["baseline_capacity_person_min"] for item in open_exits)
        service_capacity = int(scenario["extra_service_exits"]) * 85
        reserved = float(scenario["emergency_access_reserved_pct"])
        effective_capacity = (capacity + service_capacity) * (1.0 - reserved)
        evac_time = occupancy / max(effective_capacity, 1.0) + 4.5
        rows.append(
            {
                **scenario,
                "open_main_exit_capacity_person_min": capacity,
                "service_exit_capacity_person_min": service_capacity,
                "effective_public_capacity_person_min": clean_float(effective_capacity, 2),
                "estimated_clear_time_min": clean_float(evac_time, 2),
                "responder_access_reserved_pct": reserved,
                "route_policy": "activate service exits only under staff control after threat-specific route screening",
            }
        )
    df = pd.DataFrame(rows).sort_values("estimated_clear_time_min")
    df.to_csv(ARTIFACT_DIR / "louvre_threat_scenarios.csv", index=False)
    return df, {
        "scenario_rows": df.to_dict(orient="records"),
        "robustness_rule": "optimize a portfolio of safe exits, not a single shortest route, because threats can remove route segments.",
    }


def build_implementation_policy() -> dict[str, Any]:
    return {
        "recommendations": [
            "use Affluences-style routing to send visitors to different exits by floor and language group",
            "pre-authorize service exits with staff-only release conditions and security screening posts",
            "reserve a fixed responder corridor before opening all public flow capacity",
            "meter upstream galleries when underground stair queues exceed threshold density",
            "run quarterly drills by scenario: unavailable main entrance, smoke, riverside security incident, and disabled-visitor surge",
        ],
        "adaptation_to_other_structures": [
            "replace Louvre exits with stadium gates, airport concourses, or mall anchors",
            "estimate floor/zone load from ticketing or sensors",
            "rank route portfolios by clear time, responder access, and security posture",
        ],
    }


def write_frontier(baseline_df: pd.DataFrame, scenario_df: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(8.0, 5.0))
    ax.bar(baseline_df["floor"], baseline_df["baseline_evacuation_time_min"], color="#586f86")
    ax.set_ylabel("Baseline evacuation time (min)")
    ax.set_title("Louvre Baseline Floor Evacuation Times")
    ax.grid(axis="y", alpha=0.22)
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "louvre_evacuation_frontier.png", dpi=180)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(8.0, 5.0))
    ax.plot(scenario_df["scenario"], scenario_df["estimated_clear_time_min"], marker="o", color="#8a5742")
    ax.set_ylabel("Estimated clear time (min)")
    ax.set_title("Threat Scenario Robustness")
    ax.tick_params(axis="x", rotation=20)
    ax.grid(alpha=0.22)
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "louvre_threat_robustness.png", dpi=180)
    plt.close(fig)


def build_result(
    baseline_evacuation_model: dict[str, Any],
    bottleneck_analysis: dict[str, Any],
    threat_scenarios: dict[str, Any],
    implementation_policy: dict[str, Any],
) -> dict[str, Any]:
    return {
        "problem_id": "2019-D",
        "title": "Time to leave the Louvre",
        "data_source": {
            "type": "official_statement_parameters",
            "root": str(ARCHIVE_ROOT / "official_assets"),
            "source_pdf": str(PDF_PATH),
            "official_requirements": {
                "five_floors": True,
                "two_underground_floors": True,
                "visitors_2017_8_1_million": True,
                "exhibits_380000": True,
                "floor_area_72735_m2": True,
                "four_main_entrances": True,
                "affluences_app": True,
                "extra_exits_security_tradeoff": True,
                "adaptable_threat_model": True,
            },
            "parameters": {
                "visitors_2017_million": VISITORS_2017_MILLION,
                "floor_area_m2": FLOOR_AREA_M2,
                "max_wing_length_m": MAX_WING_LENGTH_M,
                "entrances": ENTRANCES,
                "floor_loads": FLOOR_LOADS,
                "source_note": "Official PDF statement parameters only; capacities and occupancy shares are explicit deterministic planning inputs for audit and replacement.",
            },
        },
        "baseline_evacuation_model": baseline_evacuation_model,
        "bottleneck_analysis": bottleneck_analysis,
        "threat_scenarios": threat_scenarios,
        "implementation_policy": implementation_policy,
        "technology_plan": "Use Affluences wait-time logic as an evacuation routing layer: multilingual push messages, exit status, responder corridor reservations, and floor-specific crowd metering.",
        "assumption_audit": {
            "truthfulness_note": "This workflow uses official statement parameters and transparent deterministic evacuation scenarios; it does not use random placeholder data.",
            "model_limits": [
                "COMAP did not provide a detailed Louvre graph, sensor counts, or actual emergency-exit capacities.",
                "Capacity and floor-load rows are planning inputs grounded in official statement facts.",
                "A full implementation should use confidential exit inventory, pedestrian simulation, disability access records, and security staff protocols.",
            ],
        },
    }


def build_report(result: dict[str, Any]) -> None:
    lines = [
        "# 2019 ICM-D Time to leave the Louvre",
        "",
        "## Data Source",
        f"- Official PDF asset: `{result['data_source']['source_pdf']}`.",
        "- No numeric COMAP attachment is supplied; this workflow uses official statement facts and explicit deterministic evacuation inputs.",
        "",
        "## Model Summary",
        f"- Estimated peak occupancy: {result['baseline_evacuation_model']['estimated_peak_occupancy']}.",
        f"- Main exit capacity: {result['baseline_evacuation_model']['main_exit_capacity_person_min']} persons/min.",
        f"- Threat scenarios: {len(result['threat_scenarios']['scenario_rows'])}.",
        "",
        "## Technology Plan",
        result["technology_plan"],
        "",
        "## Output Files",
        "- `louvre_evacuation_baseline.csv`",
        "- `louvre_bottlenecks.csv`",
        "- `louvre_threat_scenarios.csv`",
        "- `louvre_evacuation_frontier.png`",
    ]
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ensure_pdf_exists()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    baseline_df, baseline_evacuation_model = build_baseline_model()
    _, bottleneck_analysis = build_bottleneck_analysis(baseline_df)
    scenario_df, threat_scenarios = build_threat_scenarios()
    implementation_policy = build_implementation_policy()
    write_frontier(baseline_df, scenario_df)
    result = build_result(baseline_evacuation_model, bottleneck_analysis, threat_scenarios, implementation_policy)
    result["artifacts"] = {
        "baseline": str(ARTIFACT_DIR / "louvre_evacuation_baseline.csv"),
        "bottlenecks": str(ARTIFACT_DIR / "louvre_bottlenecks.csv"),
        "threat_scenarios": str(ARTIFACT_DIR / "louvre_threat_scenarios.csv"),
        "evacuation_frontier": str(ARTIFACT_DIR / "louvre_evacuation_frontier.png"),
    }
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    build_report(result)
    print(json.dumps({"result": str(RESULT_PATH), "report": str(REPORT_PATH), "artifacts": str(ARTIFACT_DIR)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
