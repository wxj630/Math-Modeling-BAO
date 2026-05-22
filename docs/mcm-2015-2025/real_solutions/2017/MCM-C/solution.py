"""2017 MCM-C Cooperate and Navigate real-data workflow.

The workflow reads the official COMAP traffic workbook. It does not create
synthetic x1/x2/x3 data; scenario values are transparent policy parameters
from the problem setting and traffic-flow assumptions documented below.
"""

from __future__ import annotations

import json
import math
import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/private/tmp/matplotlib-cache")
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd


REPO_ROOT = Path(__file__).resolve().parents[5]
ARCHIVE_ROOT = REPO_ROOT / "docs" / "mcm-2015-2025"
DATA_ROOT = ARCHIVE_ROOT / "official_assets_extracted" / "2017" / "Problem Data- Cooperate and Navigate"
PDF_PATH = ARCHIVE_ROOT / "official_assets_extracted" / "2017" / "Cooperate and Navigate.pdf"
WORKBOOK_PATH = DATA_ROOT / "2017_MCM_Problem_C_Data.xlsx"
OUT_ROOT = ARCHIVE_ROOT / "real_solutions" / "2017" / "MCM-C"
ARTIFACT_DIR = OUT_ROOT / "artifacts"

PEAK_HOUR_DAILY_SHARE = 0.08
SPEED_LIMIT_MPH = 60
HUMAN_CAPACITY_PER_LANE_VPH = 2000
AV_LANE_CAPACITY_PER_LANE_VPH = 3600
ADOPTION_SHARES = [0.10, 0.50, 0.90]


def require_assets() -> None:
    missing = [str(path) for path in [PDF_PATH, WORKBOOK_PATH] if not path.exists()]
    if missing:
        raise FileNotFoundError("missing official COMAP Cooperate and Navigate assets: " + ", ".join(missing))


def clean_segments(raw: pd.DataFrame) -> pd.DataFrame:
    rename = {
        "Route_ID": "route_id",
        "startMilepost": "start_milepost",
        "endMilepost": "end_milepost",
        "Average daily traffic counts Year_2015": "adt_2015",
        "RteType (IS= Interstate, SR= State Route)": "route_type",
        "Number of Lanes DECR MP direction ": "lanes_decreasing",
        "Number of Lanes INCR MP direction": "lanes_increasing",
        "Comments": "comments",
    }
    df = raw.rename(columns=rename)[list(rename.values())].copy()
    df["segment_length_mi"] = (df["end_milepost"] - df["start_milepost"]).abs()
    df["avg_lanes_per_direction"] = (df["lanes_decreasing"] + df["lanes_increasing"]) / 2.0
    df["peak_hour_volume_total"] = df["adt_2015"] * PEAK_HOUR_DAILY_SHARE
    df["peak_hour_volume_per_direction"] = df["peak_hour_volume_total"] / 2.0
    df["baseline_capacity_per_direction"] = df["avg_lanes_per_direction"] * HUMAN_CAPACITY_PER_LANE_VPH
    df["baseline_vc_ratio"] = df["peak_hour_volume_per_direction"] / df["baseline_capacity_per_direction"]
    df["route_label"] = df["route_id"].map(lambda value: f"I-{int(value)}" if int(value) in {5, 90, 405} else f"SR-{int(value)}")
    return df.sort_values(["route_id", "start_milepost"]).reset_index(drop=True)


def capacity_multiplier(av_share: float) -> float:
    # AV-AV cooperation grows quadratically; mixed traffic has a smaller coordination gain.
    return 1.0 + 1.20 * av_share**2 + 0.25 * av_share * (1.0 - av_share)


def speed_from_vc(vc_ratio: pd.Series | float) -> pd.Series | float:
    return SPEED_LIMIT_MPH / (1.0 + 0.15 * (vc_ratio**4))


def scenario_for_share(segments: pd.DataFrame, av_share: float) -> tuple[dict[str, float], pd.DataFrame]:
    modeled = segments.copy()
    modeled["av_share"] = av_share
    modeled["capacity_multiplier"] = capacity_multiplier(av_share)
    modeled["mixed_capacity_per_direction"] = modeled["baseline_capacity_per_direction"] * modeled["capacity_multiplier"]
    modeled["mixed_vc_ratio"] = modeled["peak_hour_volume_per_direction"] / modeled["mixed_capacity_per_direction"]
    modeled["mixed_speed_mph"] = speed_from_vc(modeled["mixed_vc_ratio"])
    modeled["baseline_speed_mph"] = speed_from_vc(modeled["baseline_vc_ratio"])
    modeled["baseline_vehicle_hours"] = modeled["peak_hour_volume_per_direction"] * modeled["segment_length_mi"] / modeled["baseline_speed_mph"]
    modeled["mixed_vehicle_hours"] = modeled["peak_hour_volume_per_direction"] * modeled["segment_length_mi"] / modeled["mixed_speed_mph"]
    modeled["vehicle_hours_saved"] = modeled["baseline_vehicle_hours"] - modeled["mixed_vehicle_hours"]
    weighted_len = modeled["segment_length_mi"].sum()
    summary = {
        "av_share": round(av_share, 2),
        "capacity_multiplier": round(capacity_multiplier(av_share), 6),
        "mean_vc_ratio": round(float((modeled["mixed_vc_ratio"] * modeled["segment_length_mi"]).sum() / weighted_len), 6),
        "congested_segment_share_vc_gt_1": round(float((modeled["mixed_vc_ratio"] > 1.0).mean()), 6),
        "total_peak_vehicle_hours": round(float(modeled["mixed_vehicle_hours"].sum()), 6),
        "vehicle_hours_saved_vs_baseline": round(float(modeled["vehicle_hours_saved"].sum()), 6),
        "median_speed_mph": round(float(modeled["mixed_speed_mph"].median()), 6),
    }
    return summary, modeled


def route_summary(segments: pd.DataFrame) -> list[dict[str, float]]:
    rows = []
    for route_id, group in segments.groupby("route_id"):
        rows.append(
            {
                "route_id": int(route_id),
                "route_label": group["route_label"].iloc[0],
                "segments": int(len(group)),
                "miles": round(float(group["segment_length_mi"].sum()), 3),
                "weighted_adt_2015": round(float((group["adt_2015"] * group["segment_length_mi"]).sum() / group["segment_length_mi"].sum()), 3),
                "max_adt_2015": int(group["adt_2015"].max()),
                "median_lanes_per_direction": round(float(group["avg_lanes_per_direction"].median()), 3),
                "baseline_congested_segments": int((group["baseline_vc_ratio"] > 1.0).sum()),
            }
        )
    return sorted(rows, key=lambda row: row["route_id"])


def adoption_scenarios(segments: pd.DataFrame) -> tuple[list[dict[str, float]], pd.DataFrame]:
    rows = []
    profile_frames = []
    for share in [0.0] + ADOPTION_SHARES:
        summary, modeled = scenario_for_share(segments, share)
        rows.append(summary)
        profile_frames.append(modeled[["route_id", "start_milepost", "end_milepost", "av_share", "mixed_vc_ratio", "mixed_speed_mph", "vehicle_hours_saved"]])
    return rows, pd.concat(profile_frames, ignore_index=True)


def tipping_point(segments: pd.DataFrame) -> dict[str, float | str | None]:
    baseline_summary, _ = scenario_for_share(segments, 0.0)
    target = baseline_summary["total_peak_vehicle_hours"] * 0.90
    for i in range(0, 101):
        share = i / 100
        summary, _ = scenario_for_share(segments, share)
        if summary["total_peak_vehicle_hours"] <= target:
            return {
                "criterion": "first AV share where total peak vehicle-hours are at least 10% below the all-human baseline",
                "av_share": round(share, 2),
                "baseline_peak_vehicle_hours": baseline_summary["total_peak_vehicle_hours"],
                "target_peak_vehicle_hours": round(target, 6),
                "achieved_peak_vehicle_hours": summary["total_peak_vehicle_hours"],
            }
    return {
        "criterion": "first AV share where total peak vehicle-hours are at least 10% below the all-human baseline",
        "av_share": None,
        "baseline_peak_vehicle_hours": baseline_summary["total_peak_vehicle_hours"],
        "target_peak_vehicle_hours": round(target, 6),
        "achieved_peak_vehicle_hours": None,
    }


def dedicated_lane_analysis(segments: pd.DataFrame) -> tuple[dict[str, object], pd.DataFrame]:
    candidates = []
    for _, row in segments.iterrows():
        lanes = float(row["avg_lanes_per_direction"])
        if lanes < 3:
            continue
        for share in [0.5, 0.9]:
            total_volume = float(row["peak_hour_volume_per_direction"])
            av_volume = total_volume * share
            human_volume = total_volume * (1.0 - share)
            mixed_summary, mixed_detail = scenario_for_share(pd.DataFrame([row]), share)
            av_lanes = 1.0
            human_lanes = max(lanes - av_lanes, 1.0)
            av_vc = av_volume / (av_lanes * AV_LANE_CAPACITY_PER_LANE_VPH) if av_volume else 0.0
            human_vc = human_volume / (human_lanes * HUMAN_CAPACITY_PER_LANE_VPH) if human_volume else 0.0
            dedicated_vh = av_volume * float(row["segment_length_mi"]) / speed_from_vc(av_vc) + human_volume * float(row["segment_length_mi"]) / speed_from_vc(human_vc)
            mixed_vh = float(mixed_detail["mixed_vehicle_hours"].iloc[0])
            savings = mixed_vh - dedicated_vh
            if savings > 0:
                candidates.append(
                    {
                        "route_id": int(row["route_id"]),
                        "start_milepost": round(float(row["start_milepost"]), 3),
                        "end_milepost": round(float(row["end_milepost"]), 3),
                        "av_share": share,
                        "avg_lanes_per_direction": round(lanes, 3),
                        "adt_2015": int(row["adt_2015"]),
                        "mixed_vehicle_hours": round(mixed_vh, 6),
                        "dedicated_lane_vehicle_hours": round(dedicated_vh, 6),
                        "vehicle_hours_saved_vs_mixed": round(float(savings), 6),
                        "policy": "pilot one AV-only lane where lanes>=3 and modeled peak-hour vehicle-hours improve",
                    }
                )
    candidates_df = pd.DataFrame(candidates)
    if not candidates_df.empty:
        candidates_df = candidates_df.sort_values("vehicle_hours_saved_vs_mixed", ascending=False).reset_index(drop=True)
    policy = {
        "rule": "Do not reserve scarce two-lane facilities. Pilot one AV-only lane only on >=3 lane-per-direction segments when AV demand is at least 50% and modeled vehicle-hours beat mixed traffic.",
        "candidate_count": int(len(candidates_df)),
        "candidate_segments": candidates_df.head(12).to_dict(orient="records") if not candidates_df.empty else [],
    }
    return policy, candidates_df


def write_plot(segments: pd.DataFrame) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(11, 7), sharey=True)
    axes = axes.flatten()
    for ax, (route_id, group) in zip(axes, segments.groupby("route_id")):
        ax.plot(group["start_milepost"], group["baseline_vc_ratio"], marker="o", linewidth=1.4)
        ax.axhline(1.0, color="firebrick", linestyle="--", linewidth=1)
        ax.set_title(f"Route {int(route_id)}")
        ax.set_xlabel("start milepost")
        ax.set_ylabel("baseline V/C")
        ax.grid(alpha=0.25)
    fig.suptitle("2017 MCM-C official route congestion profiles")
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "route_congestion_profiles.png", dpi=180)
    plt.close(fig)


def build_report(result: dict) -> str:
    top_routes = result["network_profile"]["route_summary"]
    scenario_rows = result["adoption_scenarios"]["scenario_rows"]
    lines = [
        "# 2017 MCM-C Cooperate and Navigate：官方交通 workbook 实验报告",
        "",
        "## 数据来源",
        f"- 官方题面：`{PDF_PATH}`。",
        f"- 官方 workbook：`{WORKBOOK_PATH}`。",
        f"- `parsed mile posts` 行数：{result['data_source']['rows']['parsed mile posts']}。",
        f"- `definitions` 行数：{result['data_source']['rows']['definitions']}。",
        "- 本实验不使用随机生成的 x1/x2/x3 数据；10%、50%、90% 是题目要求讨论的自动驾驶渗透率情景。",
        "",
        "## 路网画像",
        "| route | miles | weighted ADT | max ADT | baseline congested segments |",
        "|---|---:|---:|---:|---:|",
    ]
    for row in top_routes:
        lines.append(f"| {row['route_label']} | {row['miles']} | {row['weighted_adt_2015']} | {row['max_adt_2015']} | {row['baseline_congested_segments']} |")
    lines.extend([
        "",
        "## 自动驾驶渗透率情景",
        "| AV share | capacity multiplier | congested share | peak vehicle-hours | saved vs baseline | median speed |",
        "|---:|---:|---:|---:|---:|---:|",
    ])
    for row in scenario_rows:
        lines.append(
            f"| {row['av_share']} | {row['capacity_multiplier']} | {row['congested_segment_share_vc_gt_1']} | {row['total_peak_vehicle_hours']} | {row['vehicle_hours_saved_vs_baseline']} | {row['median_speed_mph']} |"
        )
    lines.extend([
        "",
        "## 临界点与专用车道",
        f"- 临界点定义：{result['tipping_point']['criterion']}。",
        f"- 临界 AV share：{result['tipping_point']['av_share']}。",
        f"- 专用车道规则：{result['dedicated_lane_policy']['rule']}",
        f"- 候选路段数：{result['dedicated_lane_policy']['candidate_count']}。",
        "",
        "## 给州长的建议摘要",
        result["governor_letter"],
        "",
        "## 产物",
        "- `clean_traffic_segments.csv`",
        "- `adoption_scenario_summary.csv`",
        "- `adoption_segment_profiles.csv`",
        "- `dedicated_lane_candidates.csv`",
        "- `route_congestion_profiles.png`",
    ])
    return "\n".join(lines) + "\n"


def main() -> None:
    require_assets()
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    raw = pd.read_excel(WORKBOOK_PATH, sheet_name="parsed mile posts")
    definitions = pd.read_excel(WORKBOOK_PATH, sheet_name="definitions")
    segments = clean_segments(raw)
    routes = route_summary(segments)
    scenario_rows, scenario_profiles = adoption_scenarios(segments)
    tipping = tipping_point(segments)
    dedicated_policy, dedicated_candidates = dedicated_lane_analysis(segments)

    segments.to_csv(ARTIFACT_DIR / "clean_traffic_segments.csv", index=False)
    pd.DataFrame(scenario_rows).to_csv(ARTIFACT_DIR / "adoption_scenario_summary.csv", index=False)
    scenario_profiles.to_csv(ARTIFACT_DIR / "adoption_segment_profiles.csv", index=False)
    dedicated_candidates.to_csv(ARTIFACT_DIR / "dedicated_lane_candidates.csv", index=False)
    write_plot(segments)

    result = {
        "data_source": {
            "type": "official_comap_xlsx",
            "root": str(DATA_ROOT),
            "source_pdf": str(PDF_PATH),
            "workbook": str(WORKBOOK_PATH),
            "rows": {
                "parsed mile posts": int(len(raw)),
                "definitions": int(len(definitions)),
            },
            "route_ids": [int(value) for value in sorted(segments["route_id"].unique())],
        },
        "official_problem_parameters": {
            "peak_hour_daily_share": PEAK_HOUR_DAILY_SHARE,
            "speed_limit_mph": SPEED_LIMIT_MPH,
            "adoption_shares_required": ADOPTION_SHARES,
            "human_capacity_per_lane_vph_assumption": HUMAN_CAPACITY_PER_LANE_VPH,
            "av_lane_capacity_per_lane_vph_assumption": AV_LANE_CAPACITY_PER_LANE_VPH,
            "assumption_note": "Capacity and peak-hour conversion are explicit traffic-flow assumptions applied to the official COMAP segment workbook, not observed fields in the workbook.",
        },
        "network_profile": {
            "segment_count": int(len(segments)),
            "total_directional_miles": round(float(segments["segment_length_mi"].sum()), 3),
            "route_summary": routes,
            "most_congested_segments": segments.sort_values("baseline_vc_ratio", ascending=False)
            .head(10)[["route_id", "start_milepost", "end_milepost", "adt_2015", "avg_lanes_per_direction", "baseline_vc_ratio"]]
            .round(6)
            .to_dict(orient="records"),
        },
        "adoption_scenarios": {
            "model": "BPR speed model with deterministic AV capacity multiplier: 1 + 1.20*p^2 + 0.25*p*(1-p).",
            "scenario_rows": scenario_rows,
        },
        "tipping_point": tipping,
        "dedicated_lane_policy": dedicated_policy,
        "governor_letter": (
            "To the Governor: the official 2017 MCM-C traffic workbook shows that the I-5/I-90/I-405/SR-520 corridor has many "
            "segments near or above a volume-capacity ratio of one under a simple peak-hour model. At 10% automated vehicles, the benefit is "
            "modest and should be handled in mixed traffic. Around the modeled tipping point, cooperative vehicles begin reducing total peak "
            "vehicle-hours materially. Dedicated AV lanes should therefore be piloted only on high-volume corridors with at least three lanes per "
            "direction and at least 50% AV demand; otherwise, taking a lane away from human drivers can make congestion worse."
        ),
    }
    (OUT_ROOT / "result.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    (OUT_ROOT / "report.md").write_text(build_report(result), encoding="utf-8")
    print(json.dumps({"result": str(OUT_ROOT / "result.json"), "artifacts": str(ARTIFACT_DIR)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
