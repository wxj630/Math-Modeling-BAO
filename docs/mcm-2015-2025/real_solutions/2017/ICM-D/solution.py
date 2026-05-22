"""2017 ICM-D Airport Security Checkpoint real-data workflow.

Reads the official COMAP TSA checkpoint workbook and builds deterministic queue
experiments. Scenario multipliers are explicitly labeled assumptions; no random
x1/x2/x3 data are generated.
"""

from __future__ import annotations

import json
import math
import os
from pathlib import Path
from typing import Iterable

os.environ.setdefault("MPLCONFIGDIR", "/private/tmp/matplotlib-cache")
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd


REPO_ROOT = Path(__file__).resolve().parents[5]
ARCHIVE_ROOT = REPO_ROOT / "docs" / "mcm-2015-2025"
DATA_ROOT = ARCHIVE_ROOT / "official_assets_extracted" / "2017" / "Problem Data- Airport Security Checkpoint"
PDF_PATH = ARCHIVE_ROOT / "official_assets_extracted" / "2017" / "Optimizing Passenger Throughput at an Airport Security Checkpoint.pdf"
WORKBOOK_PATH = DATA_ROOT / "2017_ICM_Problem_D_Data.xlsx"
OUT_ROOT = ARCHIVE_ROOT / "real_solutions" / "2017" / "ICM-D"
ARTIFACT_DIR = OUT_ROOT / "artifacts"

PRECHECK_SHARE_STATEMENT = 0.45
BASELINE_PRECHECK_LANES = 1
BASELINE_REGULAR_LANES = 3

COLUMN_MAP = {
    "precheck_arrival": "TSA Pre-Check Arrival Times",
    "regular_arrival": "Regular Pax Arrival Times",
    "id_1": "ID Check Process Time 1",
    "id_2": "ID Check Process Time 2",
    "mm_wave_exit": "Milimeter Wave Scan times",
    "xray_1_exit": "X-Ray Scan Time",
    "xray_2_exit": "X-Ray Scan Time.1",
    "property_time": "Time to get scanned property",
}


def require_assets() -> None:
    missing = [str(path) for path in [PDF_PATH, WORKBOOK_PATH] if not path.exists()]
    if missing:
        raise FileNotFoundError("missing official COMAP airport checkpoint assets: " + ", ".join(missing))


def to_seconds(value) -> float | None:
    if pd.isna(value):
        return None
    if isinstance(value, pd.Timedelta):
        return float(value.total_seconds())
    if hasattr(value, "hour") and hasattr(value, "minute") and hasattr(value, "second"):
        return float(value.hour * 3600 + value.minute * 60 + value.second + value.microsecond / 1_000_000)
    if isinstance(value, str):
        value = value.strip()
        if not value:
            return None
        parts = value.split(":")
        if len(parts) == 3:
            return float(parts[0]) * 3600 + float(parts[1]) * 60 + float(parts[2])
        if len(parts) == 2:
            return float(parts[0]) * 60 + float(parts[1])
    if isinstance(value, (int, float)):
        return float(value) * 24 * 3600 if 0 <= float(value) < 1 else float(value)
    return None


def seconds_from_column(df: pd.DataFrame, column: str) -> list[float]:
    values = [to_seconds(value) for value in df[column].tolist()]
    return [float(value) for value in values if value is not None and math.isfinite(value)]


def sorted_unique_nonnegative(values: Iterable[float]) -> list[float]:
    return sorted(value for value in values if value >= 0)


def positive_diffs(timestamps: list[float]) -> list[float]:
    stamps = sorted_unique_nonnegative(timestamps)
    diffs = [b - a for a, b in zip(stamps, stamps[1:]) if b > a]
    return diffs


def normalize_property_seconds(values: list[float]) -> list[float]:
    normalized = []
    for value in values:
        # The official workbook uses h:mm:ss formatting for entries that are plausibly seconds.
        normalized.append(value / 60.0 if value >= 600 else value)
    return normalized


def clean_samples(raw: pd.DataFrame) -> dict[str, list[float]]:
    precheck_arrivals = sorted_unique_nonnegative(seconds_from_column(raw, COLUMN_MAP["precheck_arrival"]))
    regular_arrivals = sorted_unique_nonnegative(seconds_from_column(raw, COLUMN_MAP["regular_arrival"]))
    id_times = seconds_from_column(raw, COLUMN_MAP["id_1"]) + seconds_from_column(raw, COLUMN_MAP["id_2"])
    mm_headways = positive_diffs(seconds_from_column(raw, COLUMN_MAP["mm_wave_exit"]))
    xray_headways = positive_diffs(seconds_from_column(raw, COLUMN_MAP["xray_1_exit"])) + positive_diffs(seconds_from_column(raw, COLUMN_MAP["xray_2_exit"]))
    property_times = normalize_property_seconds(seconds_from_column(raw, COLUMN_MAP["property_time"]))
    return {
        "precheck_arrivals": precheck_arrivals,
        "regular_arrivals": regular_arrivals,
        "id_times": id_times,
        "mm_wave_times": mm_headways,
        "xray_times": xray_headways,
        "property_times": property_times,
    }


def median(values: list[float]) -> float:
    series = pd.Series(values, dtype="float64")
    return float(series.median())


def percentile(values: list[float], q: float) -> float:
    series = pd.Series(values, dtype="float64")
    return float(series.quantile(q))


def cycle_value(values: list[float], index: int, multiplier: float = 1.0) -> float:
    if not values:
        raise ValueError("empty empirical process sample")
    return values[index % len(values)] * multiplier


def passenger_service_time(samples: dict[str, list[float]], index: int, passenger_type: str, multipliers: dict[str, float]) -> float:
    id_time = cycle_value(samples["id_times"], index, multipliers.get("id", 1.0))
    xray_time = cycle_value(samples["xray_times"], index, multipliers.get("xray", 1.0))
    mm_time = cycle_value(samples["mm_wave_times"], index, multipliers.get("mm_wave", 1.0))
    property_time = cycle_value(samples["property_times"], index, multipliers.get("property", 1.0))
    if passenger_type == "precheck":
        id_time *= multipliers.get("precheck_id_factor", 0.90)
        xray_time *= multipliers.get("precheck_xray_factor", 0.85)
        mm_time *= multipliers.get("precheck_mm_factor", 0.85)
        property_time *= multipliers.get("precheck_property_factor", 0.65)
    return id_time + max(xray_time, mm_time) + property_time


def simulate_queue(arrivals: list[float], service_times: list[float], servers: int) -> dict[str, object]:
    available = [0.0 for _ in range(servers)]
    rows = []
    for i, arrival in enumerate(arrivals):
        server_index = min(range(servers), key=lambda idx: available[idx])
        start = max(arrival, available[server_index])
        wait = start - arrival
        finish = start + service_times[i]
        available[server_index] = finish
        rows.append(
            {
                "passenger_index": i,
                "arrival_time_s": round(arrival, 6),
                "service_time_s": round(service_times[i], 6),
                "start_time_s": round(start, 6),
                "finish_time_s": round(finish, 6),
                "wait_time_s": round(wait, 6),
                "server": server_index,
            }
        )
    waits = [row["wait_time_s"] for row in rows]
    return {
        "servers": servers,
        "passenger_count": len(arrivals),
        "mean_wait_s": round(float(sum(waits) / len(waits)), 6) if waits else 0.0,
        "p90_wait_s": round(percentile(waits, 0.90), 6) if waits else 0.0,
        "max_wait_s": round(max(waits), 6) if waits else 0.0,
        "mean_service_s": round(float(sum(service_times) / len(service_times)), 6) if service_times else 0.0,
        "last_finish_s": round(max((row["finish_time_s"] for row in rows), default=0.0), 6),
        "rows": rows,
    }


def run_checkpoint(samples: dict[str, list[float]], precheck_lanes: int, regular_lanes: int, multipliers: dict[str, float]) -> dict[str, object]:
    pre_services = [passenger_service_time(samples, i, "precheck", multipliers) for i, _ in enumerate(samples["precheck_arrivals"])]
    reg_services = [passenger_service_time(samples, i, "regular", multipliers) for i, _ in enumerate(samples["regular_arrivals"])]
    pre = simulate_queue(samples["precheck_arrivals"], pre_services, precheck_lanes)
    reg = simulate_queue(samples["regular_arrivals"], reg_services, regular_lanes)
    combined_waits = [row["wait_time_s"] for row in pre["rows"]] + [row["wait_time_s"] for row in reg["rows"]]
    combined_finish = max(pre["last_finish_s"], reg["last_finish_s"])
    return {
        "precheck_lanes": precheck_lanes,
        "regular_lanes": regular_lanes,
        "precheck": {key: value for key, value in pre.items() if key != "rows"},
        "regular": {key: value for key, value in reg.items() if key != "rows"},
        "combined_mean_wait_s": round(float(sum(combined_waits) / len(combined_waits)), 6),
        "combined_p90_wait_s": round(percentile(combined_waits, 0.90), 6),
        "combined_max_wait_s": round(max(combined_waits), 6),
        "checkpoint_clear_time_s": round(float(combined_finish), 6),
        "rows": {"precheck": pre["rows"], "regular": reg["rows"]},
    }


def bottleneck_analysis(samples: dict[str, list[float]], baseline: dict[str, object]) -> dict[str, object]:
    stage_rows = [
        {"stage": "ID check", "median_s": round(median(samples["id_times"]), 6), "p90_s": round(percentile(samples["id_times"], 0.90), 6)},
        {"stage": "millimeter wave scanner headway", "median_s": round(median(samples["mm_wave_times"]), 6), "p90_s": round(percentile(samples["mm_wave_times"], 0.90), 6)},
        {"stage": "x-ray belt headway", "median_s": round(median(samples["xray_times"]), 6), "p90_s": round(percentile(samples["xray_times"], 0.90), 6)},
        {"stage": "property divest/reclaim", "median_s": round(median(samples["property_times"]), 6), "p90_s": round(percentile(samples["property_times"], 0.90), 6)},
    ]
    stage_rows.sort(key=lambda row: row["p90_s"], reverse=True)
    queue_rows = [
        {"queue": "precheck", "mean_wait_s": baseline["precheck"]["mean_wait_s"], "p90_wait_s": baseline["precheck"]["p90_wait_s"], "lanes": baseline["precheck_lanes"]},
        {"queue": "regular", "mean_wait_s": baseline["regular"]["mean_wait_s"], "p90_wait_s": baseline["regular"]["p90_wait_s"], "lanes": baseline["regular_lanes"]},
    ]
    return {
        "stage_service_summary": stage_rows,
        "queue_summary": queue_rows,
        "bottlenecks": [
            f"Highest p90 process time: {stage_rows[0]['stage']} ({stage_rows[0]['p90_s']} s).",
            f"Largest queue p90 wait: {max(queue_rows, key=lambda row: row['p90_wait_s'])['queue']} lane.",
        ],
    }


def modification_experiments(samples: dict[str, list[float]], baseline: dict[str, object]) -> dict[str, object]:
    scenarios = [
        {
            "name": "rebalance lanes to 2 PreCheck / 2 regular",
            "precheck_lanes": 2,
            "regular_lanes": 2,
            "multipliers": {},
            "rationale": "Problem statement says 45% are PreCheck but often only one PreCheck lane for every three regular lanes.",
        },
        {
            "name": "parallel divestment support and bin preparation",
            "precheck_lanes": 1,
            "regular_lanes": 3,
            "multipliers": {"property": 0.75, "xray": 0.90},
            "rationale": "Reduce Zone B/C property preparation variance without lowering security standards.",
        },
        {
            "name": "hybrid: 2 PreCheck lanes plus divestment support",
            "precheck_lanes": 2,
            "regular_lanes": 2,
            "multipliers": {"property": 0.75, "xray": 0.90},
            "rationale": "Combines lane balance with process support; included as a transparent upper-bound operational scenario.",
        },
    ]
    rows = []
    baseline_wait = baseline["combined_mean_wait_s"]
    baseline_p90 = baseline["combined_p90_wait_s"]
    for scenario in scenarios:
        result = run_checkpoint(samples, scenario["precheck_lanes"], scenario["regular_lanes"], scenario["multipliers"])
        rows.append(
            {
                "modification": scenario["name"],
                "precheck_lanes": scenario["precheck_lanes"],
                "regular_lanes": scenario["regular_lanes"],
                "combined_mean_wait_s": result["combined_mean_wait_s"],
                "combined_p90_wait_s": result["combined_p90_wait_s"],
                "mean_wait_change_vs_baseline_s": round(result["combined_mean_wait_s"] - baseline_wait, 6),
                "p90_wait_change_vs_baseline_s": round(result["combined_p90_wait_s"] - baseline_p90, 6),
                "checkpoint_clear_time_s": result["checkpoint_clear_time_s"],
                "rationale": scenario["rationale"],
            }
        )
    rows.sort(key=lambda row: (row["combined_p90_wait_s"], row["combined_mean_wait_s"]))
    return {"modifications": rows}


def cultural_sensitivity(samples: dict[str, list[float]]) -> dict[str, object]:
    styles = [
        {"style": "personal-space cautious", "property": 1.25, "id": 1.05, "description": "More spacing and slower divestment/reclaim behavior."},
        {"style": "collective-efficiency", "property": 0.85, "id": 0.95, "description": "Passengers coordinate bins and move when prompted."},
        {"style": "individual-fast but variable", "property": 0.95, "id": 1.00, "description": "Faster median but less orderly behavior; modeled here without random variance."},
    ]
    rows = []
    for style in styles:
        result = run_checkpoint(samples, BASELINE_PRECHECK_LANES, BASELINE_REGULAR_LANES, {"property": style["property"], "id": style["id"]})
        rows.append(
            {
                "traveler_style": style["style"],
                "property_multiplier": style["property"],
                "id_multiplier": style["id"],
                "combined_mean_wait_s": result["combined_mean_wait_s"],
                "combined_p90_wait_s": result["combined_p90_wait_s"],
                "description": style["description"],
            }
        )
    return {
        "method": "Deterministic one-at-a-time multipliers on official process samples; traveler styles are sensitivity scenarios, not observed cultures in the workbook.",
        "traveler_styles": rows,
    }


def write_artifacts(samples: dict[str, list[float]], baseline: dict[str, object], bottlenecks: dict[str, object], modifications: dict[str, object], cultural: dict[str, object]) -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    sample_rows = []
    for key, values in samples.items():
        for value in values:
            sample_rows.append({"sample_type": key, "seconds": round(value, 6)})
    pd.DataFrame(sample_rows).to_csv(ARTIFACT_DIR / "clean_checkpoint_samples.csv", index=False)
    pd.DataFrame(
        [
            {"queue": "precheck", **baseline["precheck"]},
            {"queue": "regular", **baseline["regular"]},
            {
                "queue": "combined",
                "servers": baseline["precheck_lanes"] + baseline["regular_lanes"],
                "passenger_count": baseline["precheck"]["passenger_count"] + baseline["regular"]["passenger_count"],
                "mean_wait_s": baseline["combined_mean_wait_s"],
                "p90_wait_s": baseline["combined_p90_wait_s"],
                "max_wait_s": baseline["combined_max_wait_s"],
                "mean_service_s": "",
                "last_finish_s": baseline["checkpoint_clear_time_s"],
            },
        ]
    ).to_csv(ARTIFACT_DIR / "baseline_queue_metrics.csv", index=False)
    pd.DataFrame(bottlenecks["stage_service_summary"]).to_csv(ARTIFACT_DIR / "stage_service_summary.csv", index=False)
    pd.DataFrame(modifications["modifications"]).to_csv(ARTIFACT_DIR / "modification_comparison.csv", index=False)
    pd.DataFrame(cultural["traveler_styles"]).to_csv(ARTIFACT_DIR / "cultural_sensitivity.csv", index=False)
    wait_rows = []
    for queue, rows in baseline["rows"].items():
        for row in rows:
            wait_rows.append({"queue": queue, "passenger_index": row["passenger_index"], "wait_time_s": row["wait_time_s"]})
    wait_df = pd.DataFrame(wait_rows)
    fig, ax = plt.subplots(figsize=(9, 5))
    for queue, group in wait_df.groupby("queue"):
        ax.plot(group["passenger_index"], group["wait_time_s"], marker="o", linewidth=1.2, label=queue)
    ax.set_title("2017 ICM-D baseline checkpoint wait times")
    ax.set_xlabel("passenger index in observed arrival stream")
    ax.set_ylabel("wait time (seconds)")
    ax.grid(alpha=0.25)
    ax.legend()
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "checkpoint_wait_times.png", dpi=180)
    plt.close(fig)


def build_report(result: dict) -> str:
    lines = [
        "# 2017 ICM-D Airport Security Checkpoint：官方 TSA workbook 实验报告",
        "",
        "## 数据来源",
        f"- 官方题面：`{PDF_PATH}`。",
        f"- 官方 workbook：`{WORKBOOK_PATH}`。",
        f"- Sheet1 行数：{result['data_source']['rows']['Sheet1']}。",
        f"- PreCheck 到达样本：{result['data_source']['arrival_counts']['precheck']}；Regular 到达样本：{result['data_source']['arrival_counts']['regular']}。",
        "- 本实验不使用随机生成的 x1/x2/x3；文化和流程改变是显式确定性敏感性情景。",
        "",
        "## 基线排队结果",
        f"- PreCheck lanes：{result['baseline_model']['precheck_lanes']}；regular lanes：{result['baseline_model']['regular_lanes']}。",
        f"- combined mean wait：{result['baseline_model']['combined_mean_wait_s']} s。",
        f"- combined p90 wait：{result['baseline_model']['combined_p90_wait_s']} s。",
        "",
        "## 瓶颈",
    ]
    lines.extend(f"- {item}" for item in result["bottleneck_analysis"]["bottlenecks"])
    lines.extend(["", "## 流程修改实验", "| modification | mean wait | p90 wait | p90 change | rationale |", "|---|---:|---:|---:|---|"])
    for row in result["modification_experiments"]["modifications"]:
        lines.append(f"| {row['modification']} | {row['combined_mean_wait_s']} | {row['combined_p90_wait_s']} | {row['p90_wait_change_vs_baseline_s']} | {row['rationale']} |")
    lines.extend(["", "## 文化/旅客风格敏感性", "| style | mean wait | p90 wait | description |", "|---|---:|---:|---|"])
    for row in result["cultural_sensitivity"]["traveler_styles"]:
        lines.append(f"| {row['traveler_style']} | {row['combined_mean_wait_s']} | {row['combined_p90_wait_s']} | {row['description']} |")
    lines.extend(["", "## 给安检管理者的建议", result["security_manager_memo"], ""])
    return "\n".join(lines)


def main() -> None:
    require_assets()
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    raw = pd.read_excel(WORKBOOK_PATH, sheet_name="Sheet1")
    samples = clean_samples(raw)
    baseline = run_checkpoint(samples, BASELINE_PRECHECK_LANES, BASELINE_REGULAR_LANES, {})
    bottlenecks = bottleneck_analysis(samples, baseline)
    modifications = modification_experiments(samples, baseline)
    cultural = cultural_sensitivity(samples)
    write_artifacts(samples, baseline, bottlenecks, modifications, cultural)
    result = {
        "data_source": {
            "type": "official_comap_xlsx",
            "root": str(DATA_ROOT),
            "source_pdf": str(PDF_PATH),
            "workbook": str(WORKBOOK_PATH),
            "rows": {"Sheet1": int(len(raw))},
            "arrival_counts": {"precheck": len(samples["precheck_arrivals"]), "regular": len(samples["regular_arrivals"])},
            "process_sample_counts": {key: len(value) for key, value in samples.items()},
        },
        "official_problem_parameters": {
            "precheck_share_statement": PRECHECK_SHARE_STATEMENT,
            "baseline_lane_ratio_statement": "often one Pre-Check lane open for every three regular lanes",
            "property_time_normalization_note": "Workbook property-time cells display large h:mm:ss values that are plausibly seconds entered under time formatting; values >=10 minutes are divided by 60 and labeled as a normalization assumption.",
        },
        "baseline_model": {key: value for key, value in baseline.items() if key != "rows"},
        "bottleneck_analysis": bottlenecks,
        "modification_experiments": modifications,
        "cultural_sensitivity": cultural,
        "security_manager_memo": (
            "To TSA security managers: the official checkpoint workbook points to Zone B/C preparation and scanner/x-ray headways as the most visible "
            "sources of high-tail service time. Keep the security standard fixed, but reduce variance by staffing divestment support, improving bin flow, "
            "and dynamically balancing PreCheck versus regular lanes when observed demand differs from the legacy one-to-three lane ratio. Cultural or traveler-style "
            "differences should be handled with clearer signs, parallel preparation space, and queue marshals rather than by lowering screening intensity."
        ),
    }
    (OUT_ROOT / "result.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    (OUT_ROOT / "report.md").write_text(build_report(result), encoding="utf-8")
    print(json.dumps({"result": str(OUT_ROOT / "result.json"), "artifacts": str(ARTIFACT_DIR)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
