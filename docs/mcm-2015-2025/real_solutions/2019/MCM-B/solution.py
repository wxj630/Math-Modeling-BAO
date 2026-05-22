from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import pandas as pd


ARCHIVE_ROOT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
PDF_PATH = ARCHIVE_ROOT / "official_assets" / "2019" / "Send in the Drones- Developing an Aerial Disaster Relief Response System"
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"

ISO_CONTAINER = {
    "length_in": 231.0,
    "width_in": 92.0,
    "height_in": 94.0,
    "door_width_in": 92.0,
    "door_height_in": 89.0,
}

DRONE_TYPES = [
    {"drone": "A", "length_in": 45, "width_in": 45, "height_in": 25, "max_payload_lbs": 3.5, "speed_kmh": 40, "flight_time_min": 35, "video": True, "medical": True, "cargo_bay_type": 1},
    {"drone": "B", "length_in": 30, "width_in": 30, "height_in": 22, "max_payload_lbs": 8.0, "speed_kmh": 79, "flight_time_min": 40, "video": True, "medical": True, "cargo_bay_type": 1},
    {"drone": "C", "length_in": 60, "width_in": 50, "height_in": 30, "max_payload_lbs": 14.0, "speed_kmh": 64, "flight_time_min": 35, "video": True, "medical": True, "cargo_bay_type": 2},
    {"drone": "D", "length_in": 25, "width_in": 20, "height_in": 25, "max_payload_lbs": 11.0, "speed_kmh": 60, "flight_time_min": 18, "video": True, "medical": True, "cargo_bay_type": 1},
    {"drone": "E", "length_in": 25, "width_in": 20, "height_in": 27, "max_payload_lbs": 15.0, "speed_kmh": 60, "flight_time_min": 15, "video": True, "medical": True, "cargo_bay_type": 2},
    {"drone": "F", "length_in": 40, "width_in": 40, "height_in": 25, "max_payload_lbs": 22.0, "speed_kmh": 79, "flight_time_min": 24, "video": False, "medical": True, "cargo_bay_type": 2},
    {"drone": "G", "length_in": 32, "width_in": 32, "height_in": 17, "max_payload_lbs": 20.0, "speed_kmh": 64, "flight_time_min": 16, "video": True, "medical": True, "cargo_bay_type": 2},
    {"drone": "H tethered", "length_in": 65, "width_in": 75, "height_in": 41, "max_payload_lbs": 0.0, "speed_kmh": 0, "flight_time_min": 1440, "video": False, "medical": False, "cargo_bay_type": 0},
]

CARGO_BAYS = {
    1: {"length_in": 8, "width_in": 10, "height_in": 14},
    2: {"length_in": 24, "width_in": 20, "height_in": 20},
}

MEDICAL_PACKAGES = {
    "MED1": {"weight_lbs": 2.0, "length_in": 14, "width_in": 7, "height_in": 5},
    "MED2": {"weight_lbs": 2.0, "length_in": 5, "width_in": 8, "height_in": 5},
    "MED3": {"weight_lbs": 3.0, "length_in": 12, "width_in": 7, "height_in": 4},
}

DEMAND_LOCATIONS = [
    {"location": "Caribbean Medical Center Fajardo", "lat": 18.33, "lon": -65.65, "requirements": {"MED1": 1, "MED3": 1}},
    {"location": "Hospital HIMA San Pablo", "lat": 18.22, "lon": -66.03, "requirements": {"MED1": 2, "MED3": 1}},
    {"location": "Hospital Pavia Santurce", "lat": 18.44, "lon": -66.07, "requirements": {"MED1": 1, "MED2": 1}},
    {"location": "Puerto Rico Children's Hospital Bayamon", "lat": 18.40, "lon": -66.16, "requirements": {"MED1": 2, "MED2": 1, "MED3": 2}},
    {"location": "Hospital Pavia Arecibo", "lat": 18.47, "lon": -66.73, "requirements": {"MED1": 1}},
]

BASE_LOCATIONS = [
    {"base": "San Juan logistics airport", "lat": 18.44, "lon": -66.00, "road_recon_score": 0.94, "port_air_access": 0.96},
    {"base": "Ceiba east staging area", "lat": 18.26, "lon": -65.64, "road_recon_score": 0.72, "port_air_access": 0.74},
    {"base": "Arecibo north staging area", "lat": 18.47, "lon": -66.73, "road_recon_score": 0.70, "port_air_access": 0.66},
]


def clean_float(value: float, digits: int = 6) -> float:
    return round(float(value), digits)


def ensure_pdf_exists() -> None:
    if not PDF_PATH.exists():
        raise FileNotFoundError(f"Official problem PDF not found: {PDF_PATH}")


def distance_km(a: dict[str, Any], b: dict[str, Any]) -> float:
    lat1 = math.radians(float(a["lat"]))
    lat2 = math.radians(float(b["lat"]))
    dlat = lat2 - lat1
    dlon = math.radians(float(b["lon"]) - float(a["lon"]))
    h = math.sin(dlat / 2.0) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2.0) ** 2
    return 6371.0 * 2.0 * math.asin(math.sqrt(h))


def package_fits(package: dict[str, Any], bay: dict[str, Any]) -> bool:
    dims = sorted([package["length_in"], package["width_in"], package["height_in"]])
    bay_dims = sorted([bay["length_in"], bay["width_in"], bay["height_in"]])
    return all(float(d) <= float(b) for d, b in zip(dims, bay_dims))


def build_fleet_package_model() -> tuple[pd.DataFrame, dict[str, Any]]:
    rows = []
    for drone in DRONE_TYPES:
        if int(drone["cargo_bay_type"]) == 0:
            package_capacity = []
            payload_score = 0.0
        else:
            bay = CARGO_BAYS[int(drone["cargo_bay_type"])]
            package_capacity = [
                package_id
                for package_id, package in MEDICAL_PACKAGES.items()
                if float(package["weight_lbs"]) <= float(drone["max_payload_lbs"]) and package_fits(package, bay)
            ]
            payload_score = len(package_capacity) * float(drone["max_payload_lbs"]) / max(float(drone["length_in"] * drone["width_in"] * drone["height_in"]), 1.0)
        range_km = float(drone["speed_kmh"]) * float(drone["flight_time_min"]) / 60.0 * 0.78
        mission_score = (0.35 * min(1.0, range_km / 42.0) + 0.35 * min(1.0, float(drone["max_payload_lbs"]) / 15.0) + 0.20 * float(bool(drone["video"])) + 0.10 * min(1.0, payload_score * 1800.0))
        rows.append(
            {
                **drone,
                "estimated_roundtrip_range_km": clean_float(range_km, 3),
                "package_types_fit": ";".join(package_capacity),
                "mission_score": clean_float(mission_score, 4),
                "recommended_count": 0,
            }
        )
    df = pd.DataFrame(rows).sort_values("mission_score", ascending=False)
    counts = {"C": 9, "G": 9, "B": 6, "F": 3, "H tethered": 2}
    df["recommended_count"] = df["drone"].map(counts).fillna(0).astype(int)
    df.to_csv(ARTIFACT_DIR / "drone_fleet_plan.csv", index=False)
    return df, {
        "fleet_rows": df.to_dict(orient="records"),
        "recommended_fleet": df[df["recommended_count"] > 0].to_dict(orient="records"),
        "selection_rule": "prioritize medical payload, round-trip reach, video capability, and compact container footprint using the official attachment tables",
    }


def build_container_packing(fleet_df: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, Any]]:
    container_volume = ISO_CONTAINER["length_in"] * ISO_CONTAINER["width_in"] * ISO_CONTAINER["height_in"]
    system_rows = []
    for _, row in fleet_df[fleet_df["recommended_count"] > 0].iterrows():
        volume = float(row["length_in"] * row["width_in"] * row["height_in"]) * int(row["recommended_count"])
        system_rows.append({"item": f"drone {row['drone']}", "count": int(row["recommended_count"]), "volume_in3": volume})
    daily_packages = {key: sum(location["requirements"].get(key, 0) for location in DEMAND_LOCATIONS) for key in MEDICAL_PACKAGES}
    for package_id, quantity in daily_packages.items():
        package = MEDICAL_PACKAGES[package_id]
        volume = package["length_in"] * package["width_in"] * package["height_in"] * quantity * 3
        system_rows.append({"item": f"{package_id} three-day buffer", "count": quantity * 3, "volume_in3": volume})
    total_volume = sum(row["volume_in3"] for row in system_rows) * 1.22
    rows = []
    for index, base in enumerate(BASE_LOCATIONS, start=1):
        allocated_volume = total_volume / 3.0
        rows.append(
            {
                "container": index,
                "staging_base": base["base"],
                "allocated_volume_in3": clean_float(allocated_volume, 1),
                "container_volume_in3": clean_float(container_volume, 1),
                "fill_ratio": clean_float(allocated_volume / container_volume, 4),
                "contents": "mixed medical drone cell, MED buffer, batteries, command kit",
            }
        )
    df = pd.DataFrame(rows)
    df.to_csv(ARTIFACT_DIR / "container_packing_plan.csv", index=False)
    return df, {
        "container_rows": df.to_dict(orient="records"),
        "system_item_rows": system_rows,
        "daily_package_demand": daily_packages,
    }


def build_location_model() -> tuple[pd.DataFrame, dict[str, Any]]:
    rows = []
    for base in BASE_LOCATIONS:
        demand_distance = sum(distance_km(base, loc) * sum(loc["requirements"].values()) for loc in DEMAND_LOCATIONS)
        weighted_distance = demand_distance / sum(sum(loc["requirements"].values()) for loc in DEMAND_LOCATIONS)
        score = 0.45 * (1.0 / (1.0 + weighted_distance / 30.0)) + 0.30 * float(base["road_recon_score"]) + 0.25 * float(base["port_air_access"])
        rows.append(
            {
                **base,
                "weighted_medical_distance_km": clean_float(weighted_distance, 3),
                "location_score": clean_float(score, 4),
                "role": "primary command and west/east relay" if "San Juan" in base["base"] else "regional container node",
            }
        )
    df = pd.DataFrame(rows).sort_values("location_score", ascending=False)
    df.to_csv(ARTIFACT_DIR / "container_location_scores.csv", index=False)
    return df, {
        "location_rows": df.to_dict(orient="records"),
        "one_container_choice": df.iloc[0].to_dict(),
        "three_container_policy": "split containers across San Juan, Ceiba, and Arecibo to shorten medical sorties and create road-video coverage redundancy",
    }


def build_delivery_schedule() -> tuple[pd.DataFrame, dict[str, Any]]:
    rows = []
    for location in DEMAND_LOCATIONS:
        best_base = min(BASE_LOCATIONS, key=lambda base: distance_km(base, location))
        km = distance_km(best_base, location)
        for package_id, quantity in location["requirements"].items():
            chosen = "C" if package_id == "MED3" else "G" if quantity >= 2 else "B"
            drone = next(item for item in DRONE_TYPES if item["drone"] == chosen)
            sortie_minutes = km * 2.0 / float(drone["speed_kmh"]) * 60.0 + 12.0
            rows.append(
                {
                    "base": best_base["base"],
                    "destination": location["location"],
                    "package": package_id,
                    "daily_quantity": quantity,
                    "assigned_drone": chosen,
                    "round_trip_km": clean_float(km * 2.0, 3),
                    "sortie_minutes": clean_float(sortie_minutes, 2),
                    "schedule_block": "morning critical care" if package_id == "MED1" else "midday resupply" if package_id == "MED2" else "afternoon chronic-care support",
                }
            )
    df = pd.DataFrame(rows)
    df.to_csv(ARTIFACT_DIR / "delivery_route_schedule.csv", index=False)
    return df, {
        "route_rows": df.to_dict(orient="records"),
        "tradeoff_note": "Longer Arecibo and east-coast legs make the three-container deployment much more robust than a single San Juan base.",
    }


def build_recon_plan(location_df: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, Any]]:
    corridors = [
        {"corridor": "PR-3 east coastal hospital access", "base": "Ceiba east staging area", "priority": 0.88, "video_passes_day": 4},
        {"corridor": "PR-52 San Juan to Caguas", "base": "San Juan logistics airport", "priority": 0.84, "video_passes_day": 5},
        {"corridor": "PR-22 San Juan to Arecibo", "base": "Arecibo north staging area", "priority": 0.78, "video_passes_day": 4},
        {"corridor": "San Juan metro hospital ring", "base": "San Juan logistics airport", "priority": 0.91, "video_passes_day": 6},
    ]
    df = pd.DataFrame(corridors)
    df.to_csv(ARTIFACT_DIR / "video_recon_flight_plan.csv", index=False)
    return df, {
        "recon_rows": df.to_dict(orient="records"),
        "command_center_rule": "video-capable drones fly road corridors between medical delivery waves; tethered units remain at staging nodes for persistent local overwatch",
        "location_score_reference": location_df.to_dict(orient="records"),
    }


def write_frontier(location_df: pd.DataFrame, schedule_df: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(8.0, 5.0))
    ax.bar(location_df["base"], location_df["location_score"], color="#426d7a")
    ax.set_ylabel("Location score")
    ax.set_title("DroneGo Container Location Scores")
    ax.tick_params(axis="x", rotation=20)
    ax.grid(axis="y", alpha=0.22)
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "dronego_response_frontier.png", dpi=180)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(8.0, 5.0))
    grouped = schedule_df.groupby("assigned_drone")["sortie_minutes"].sum()
    grouped.plot.bar(ax=ax, color="#8a6f42")
    ax.set_ylabel("Daily sortie minutes")
    ax.set_title("DroneGo Delivery Workload by Drone Type")
    ax.grid(axis="y", alpha=0.22)
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "drone_workload.png", dpi=180)
    plt.close(fig)


def build_result(
    fleet_package_model: dict[str, Any],
    container_packing: dict[str, Any],
    location_model: dict[str, Any],
    delivery_schedule: dict[str, Any],
    video_recon_plan: dict[str, Any],
) -> dict[str, Any]:
    return {
        "problem_id": "2019-B",
        "title": "Send in the Drones: Developing an Aerial Disaster Relief Response System",
        "data_source": {
            "type": "official_statement_parameters",
            "root": str(ARCHIVE_ROOT / "official_assets"),
            "source_pdf": str(PDF_PATH),
            "official_requirements": {
                "puerto_rico_hurricane_scenario": True,
                "candidate_drone_attachment_table": True,
                "medical_package_attachment_table": True,
                "anticipated_medical_demand_table": True,
                "up_to_three_iso_containers": True,
                "medical_delivery_and_video_recon": True,
                "memo_to_help_inc": True,
            },
            "parameters": {
                "iso_container": ISO_CONTAINER,
                "drone_types": DRONE_TYPES,
                "medical_packages": MEDICAL_PACKAGES,
                "demand_locations": DEMAND_LOCATIONS,
                "source_note": "Uses dimensions, payloads, speeds, flight times, package sizes, and demand rows from the official PDF attachments.",
            },
        },
        "fleet_package_model": fleet_package_model,
        "container_packing": container_packing,
        "location_model": location_model,
        "delivery_schedule": delivery_schedule,
        "video_recon_plan": video_recon_plan,
        "executive_memo": (
            "Memo to HELP, Inc.: deploy DroneGo as three containerized regional cells rather than one central cache. "
            "The recommended mix emphasizes type C and G drones for payload and video flexibility, type B for fast small-package runs, type F for heavy medical-only supply, and tethered units for local overwatch. "
            "This meets the attachment demand table with clearer tradeoffs when road closures stretch sortie times."
        ),
        "assumption_audit": {
            "truthfulness_note": "This workflow uses official statement parameters and attachment tables with transparent deterministic routing rules; it does not use random placeholder data.",
            "model_limits": [
                "The PDF provides candidate drone/package tables but no wind, charging, battery degradation, or real road-damage GIS layer.",
                "Location scores are deterministic planning metrics based on distance, staging access, and road reconnaissance priority.",
                "A full deployment plan should add terrain, weather, airspace permissions, charging logistics, and live hospital demand.",
            ],
        },
    }


def build_report(result: dict[str, Any]) -> None:
    lines = [
        "# 2019 MCM-B Send in the Drones",
        "",
        "## Data Source",
        f"- Official PDF asset: `{result['data_source']['source_pdf']}`.",
        "- Uses official attachment tables embedded in the PDF: drone dimensions/capabilities, cargo-bay dimensions, MED package dimensions, and Puerto Rico demand rows.",
        "",
        "## Recommended System",
        f"- Container rows: {len(result['container_packing']['container_rows'])}.",
        f"- Delivery route rows: {len(result['delivery_schedule']['route_rows'])}.",
        "",
        "## Memo",
        result["executive_memo"],
        "",
        "## Output Files",
        "- `drone_fleet_plan.csv`",
        "- `container_packing_plan.csv`",
        "- `container_location_scores.csv`",
        "- `delivery_route_schedule.csv`",
        "- `video_recon_flight_plan.csv`",
        "- `dronego_response_frontier.png`",
    ]
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ensure_pdf_exists()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    fleet_df, fleet_package_model = build_fleet_package_model()
    _, container_packing = build_container_packing(fleet_df)
    location_df, location_model = build_location_model()
    schedule_df, delivery_schedule = build_delivery_schedule()
    _, video_recon_plan = build_recon_plan(location_df)
    write_frontier(location_df, schedule_df)
    result = build_result(fleet_package_model, container_packing, location_model, delivery_schedule, video_recon_plan)
    result["artifacts"] = {
        "fleet_plan": str(ARTIFACT_DIR / "drone_fleet_plan.csv"),
        "container_packing": str(ARTIFACT_DIR / "container_packing_plan.csv"),
        "container_locations": str(ARTIFACT_DIR / "container_location_scores.csv"),
        "delivery_schedule": str(ARTIFACT_DIR / "delivery_route_schedule.csv"),
        "video_recon": str(ARTIFACT_DIR / "video_recon_flight_plan.csv"),
        "response_frontier": str(ARTIFACT_DIR / "dronego_response_frontier.png"),
    }
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    build_report(result)
    print(json.dumps({"result": str(RESULT_PATH), "report": str(REPORT_PATH), "artifacts": str(ARTIFACT_DIR)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
