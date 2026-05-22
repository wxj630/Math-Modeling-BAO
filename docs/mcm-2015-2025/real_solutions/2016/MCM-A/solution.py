from __future__ import annotations

import json
import os
from pathlib import Path

import numpy as np
import pandas as pd


ARCHIVE_ROOT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
PDF_PATH = ARCHIVE_ROOT / "official_assets_extracted" / "2016" / "A Hot Bath.pdf"
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"
os.environ.setdefault("MPLCONFIGDIR", str(ARTIFACT_DIR / ".matplotlib"))

import matplotlib.pyplot as plt


TARGET_TEMPERATURE_C = 40.0
HOT_WATER_TEMPERATURE_C = 48.0
ROOM_TEMPERATURE_C = 22.0
PERSON_SKIN_TEMPERATURE_C = 34.0
BATH_DURATION_MIN = 40
TIME_STEP_MIN = 0.5
GRID_CELLS = 18

BASE_TUB = {
    "name": "baseline_rectangular_tub",
    "length_m": 1.55,
    "width_m": 0.72,
    "water_depth_m": 0.42,
    "water_volume_l": 250.0,
    "surface_area_m2": 1.12,
    "wall_area_m2": 2.3,
}
PERSON = {
    "displaced_volume_l": 70.0,
    "immersed_surface_area_m2": 1.15,
    "thermal_contact_factor": 0.52,
}

ASSUMPTIONS = {
    "model_type": "deterministic 1D finite-volume bathtub temperature model with faucet at one end and overflow removal from the other end",
    "ambient_heat_loss_per_min": 0.010,
    "wall_heat_loss_per_min": 0.004,
    "person_heat_exchange_per_min": 0.006,
    "base_mixing_per_min": 0.18,
    "motion_mixing_multiplier": {"still": 0.75, "gentle_motion": 1.0, "active_stirring": 1.45},
    "overflow_rule": "when hot water is added at constant trickle, the same volume leaves through overflow; this is counted as wasted water",
    "truthfulness": "The PDF gives qualitative constraints but no measured tub/person temperatures; numeric coefficients are explicit scenario assumptions, not observed data.",
}


def clean_float(value: float, digits: int = 6) -> float:
    return round(float(value), digits)


def simulate_strategy(
    flow_l_per_min: float,
    motion: str = "gentle_motion",
    tub: dict[str, float | str] | None = None,
    bubble_factor: float = 1.0,
) -> dict[str, object]:
    tub = tub or BASE_TUB
    steps = int(BATH_DURATION_MIN / TIME_STEP_MIN)
    cells = GRID_CELLS
    water_volume_l = float(tub["water_volume_l"]) - PERSON["displaced_volume_l"]
    cell_volume_l = water_volume_l / cells
    temps = np.full(cells, TARGET_TEMPERATURE_C, dtype=float)
    profile_rows = []

    ambient_loss = ASSUMPTIONS["ambient_heat_loss_per_min"] * float(tub["surface_area_m2"]) / BASE_TUB["surface_area_m2"] / bubble_factor
    wall_loss = ASSUMPTIONS["wall_heat_loss_per_min"] * float(tub["wall_area_m2"]) / BASE_TUB["wall_area_m2"]
    person_exchange = ASSUMPTIONS["person_heat_exchange_per_min"] * PERSON["thermal_contact_factor"]
    mixing = ASSUMPTIONS["base_mixing_per_min"] * ASSUMPTIONS["motion_mixing_multiplier"][motion]
    hot_fraction = min(0.45, flow_l_per_min * TIME_STEP_MIN / cell_volume_l)

    for step in range(steps + 1):
        minute = step * TIME_STEP_MIN
        if step % 4 == 0 or step == steps:
            profile_rows.append(
                {
                    "minute": clean_float(minute, 2),
                    "near_faucet_c": clean_float(temps[0], 4),
                    "middle_c": clean_float(temps[cells // 2], 4),
                    "overflow_end_c": clean_float(temps[-1], 4),
                    "mean_c": clean_float(float(temps.mean()), 4),
                    "spatial_range_c": clean_float(float(temps.max() - temps.min()), 4),
                }
            )
        if step == steps:
            break
        exchange = np.zeros_like(temps)
        exchange[1:-1] = temps[:-2] - 2 * temps[1:-1] + temps[2:]
        exchange[0] = temps[1] - temps[0]
        exchange[-1] = temps[-2] - temps[-1]
        temps = temps + mixing * TIME_STEP_MIN * exchange
        temps -= (ambient_loss + wall_loss) * TIME_STEP_MIN * (temps - ROOM_TEMPERATURE_C)
        temps -= person_exchange * TIME_STEP_MIN * (temps - PERSON_SKIN_TEMPERATURE_C)
        if flow_l_per_min > 0:
            shifted = np.empty_like(temps)
            shifted[0] = (1 - hot_fraction) * temps[0] + hot_fraction * HOT_WATER_TEMPERATURE_C
            shifted[1:] = (1 - hot_fraction) * temps[1:] + hot_fraction * temps[:-1]
            temps = shifted

    profile = pd.DataFrame(profile_rows)
    mean_abs_error = float((profile["mean_c"] - TARGET_TEMPERATURE_C).abs().mean())
    spatial_penalty = float(profile["spatial_range_c"].mean())
    wasted_liters = flow_l_per_min * BATH_DURATION_MIN
    comfort_score = 1.0 / (1.0 + mean_abs_error + 0.8 * spatial_penalty + 0.015 * wasted_liters)
    return {
        "flow_l_per_min": clean_float(flow_l_per_min, 3),
        "motion": motion,
        "bubble_factor": clean_float(bubble_factor, 3),
        "mean_abs_error_c": clean_float(mean_abs_error, 4),
        "mean_spatial_range_c": clean_float(spatial_penalty, 4),
        "final_mean_c": clean_float(float(temps.mean()), 4),
        "final_spatial_range_c": clean_float(float(temps.max() - temps.min()), 4),
        "wasted_liters": clean_float(wasted_liters, 2),
        "comfort_score": clean_float(comfort_score, 6),
        "profile_rows": profile_rows,
    }


def thermal_strategy() -> dict[str, object]:
    rows = []
    for flow in np.arange(0.0, 2.51, 0.25):
        for motion in ["still", "gentle_motion", "active_stirring"]:
            result = simulate_strategy(float(flow), motion=motion)
            rows.append({key: result[key] for key in ["flow_l_per_min", "motion", "mean_abs_error_c", "mean_spatial_range_c", "final_mean_c", "wasted_liters", "comfort_score"]})
    grid = pd.DataFrame(rows)
    feasible = grid[(grid["final_mean_c"] >= 35.5) & (grid["wasted_liters"] < 80)].copy()
    if feasible.empty:
        feasible = grid.copy()
    best = feasible.sort_values(["comfort_score", "wasted_liters"], ascending=[False, True]).iloc[0].to_dict()
    return {
        "objective": "keep mean bath temperature close to initial target, reduce spatial unevenness, and penalize overflow waste",
        "recommended_strategy": {key: clean_float(value) if isinstance(value, (float, np.floating)) else value for key, value in best.items()},
        "strategy_rows": rows,
        "recommended_profile": simulate_strategy(float(best["flow_l_per_min"]), motion=str(best["motion"]))["profile_rows"],
    }


def shape_person_motion_sensitivity(best_flow: float) -> dict[str, object]:
    tubs = [
        {**BASE_TUB, "name": "short_deep_tub", "length_m": 1.30, "width_m": 0.70, "water_depth_m": 0.52, "water_volume_l": 250.0, "surface_area_m2": 0.91, "wall_area_m2": 2.6},
        BASE_TUB,
        {**BASE_TUB, "name": "long_shallow_tub", "length_m": 1.80, "width_m": 0.78, "water_depth_m": 0.34, "water_volume_l": 250.0, "surface_area_m2": 1.40, "wall_area_m2": 2.1},
    ]
    shape_rows = []
    for tub in tubs:
        result = simulate_strategy(best_flow, motion="gentle_motion", tub=tub)
        shape_rows.append(
            {
                "shape": tub["name"],
                "surface_area_m2": tub["surface_area_m2"],
                "water_depth_m": tub["water_depth_m"],
                "mean_abs_error_c": result["mean_abs_error_c"],
                "mean_spatial_range_c": result["mean_spatial_range_c"],
                "comfort_score": result["comfort_score"],
            }
        )
    motion_rows = []
    for motion in ["still", "gentle_motion", "active_stirring"]:
        result = simulate_strategy(best_flow, motion=motion)
        motion_rows.append({"motion": motion, "mean_abs_error_c": result["mean_abs_error_c"], "mean_spatial_range_c": result["mean_spatial_range_c"], "comfort_score": result["comfort_score"]})
    return {
        "shape_rows": shape_rows,
        "motion_rows": motion_rows,
        "person_effect_note": "A larger or cooler bather increases displacement and heat exchange, so the same trickle requires stronger mixing or slightly higher flow; the scenario uses the visible person assumptions in data_source.",
    }


def bubble_bath_effect(best_flow: float) -> dict[str, object]:
    rows = []
    for factor, label in [(1.0, "no_bubbles"), (1.15, "thin_bubble_layer"), (1.35, "moderate_bubble_layer"), (1.60, "thick_bubble_layer")]:
        result = simulate_strategy(best_flow, motion="gentle_motion", bubble_factor=factor)
        rows.append(
            {
                "bubble_case": label,
                "surface_heat_loss_reduction_factor": clean_float(factor, 2),
                "mean_abs_error_c": result["mean_abs_error_c"],
                "mean_spatial_range_c": result["mean_spatial_range_c"],
                "final_mean_c": result["final_mean_c"],
                "comfort_score": result["comfort_score"],
            }
        )
    return {
        "interpretation": "Bubble bath suppresses surface heat loss but can also suppress natural surface mixing; this experiment isolates the insulating effect and keeps motion fixed.",
        "rows": rows,
    }


def user_explanation(strategy: dict[str, object], sensitivity: dict[str, object], bubble: dict[str, object]) -> str:
    best = strategy["recommended_strategy"]
    return (
        "For a simple bathtub, the practical strategy is a small continuous trickle of hot water plus gentle motion. "
        f"In the baseline scenario the model selects about {best['flow_l_per_min']} L/min with {best['motion']}, wasting about {best['wasted_liters']} L over a 40 minute bath. "
        "Hot water enters near the faucet, cooler water leaves near the overflow, and heat is constantly lost to air, tub walls, and the bather, so perfectly uniform temperature is physically difficult. "
        "Gentle stirring matters because it reduces hot and cold spots without requiring a much larger overflow. Bubble bath helps by insulating the surface, but it should not replace mixing."
    )


def write_artifacts(strategy: dict[str, object], sensitivity: dict[str, object], bubble: dict[str, object]) -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(strategy["strategy_rows"]).to_csv(ARTIFACT_DIR / "temperature_strategy_grid.csv", index=False, encoding="utf-8-sig")
    pd.DataFrame(sensitivity["shape_rows"]).to_csv(ARTIFACT_DIR / "tub_shape_sensitivity.csv", index=False, encoding="utf-8-sig")
    pd.DataFrame(bubble["rows"]).to_csv(ARTIFACT_DIR / "bubble_bath_sensitivity.csv", index=False, encoding="utf-8-sig")
    profile = pd.DataFrame(strategy["recommended_profile"])
    profile.to_csv(ARTIFACT_DIR / "recommended_temperature_profile.csv", index=False, encoding="utf-8-sig")

    fig, ax = plt.subplots(figsize=(8.5, 5))
    ax.plot(profile["minute"], profile["near_faucet_c"], label="near faucet", color="#b44b32")
    ax.plot(profile["minute"], profile["middle_c"], label="middle", color="#2f6f73")
    ax.plot(profile["minute"], profile["overflow_end_c"], label="overflow end", color="#2d5f9a")
    ax.axhline(TARGET_TEMPERATURE_C, color="#444444", linestyle="--", label="target")
    ax.set_title("2016 MCM-A Hot Bath Temperature Profile")
    ax.set_xlabel("Minute")
    ax.set_ylabel("Temperature (C)")
    ax.grid(alpha=0.25)
    ax.legend()
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "temperature_profiles.png", dpi=180)
    plt.close(fig)


def write_report(result: dict[str, object]) -> None:
    best = result["thermal_strategy"]["recommended_strategy"]
    lines = [
        "# 2016 MCM-A A Hot Bath 题面参数实验报告",
        "",
        "## 数据来源",
        f"- 官方 PDF：`{PDF_PATH}`。",
        "- 本题没有独立 CSV/XLSX 附件；模型只使用题面的物理约束：单水龙头、简单浴缸、无循环加热、热水恒定细流、满水后溢流排出。",
        "- 浴缸尺寸、热损失、人体体积/温度、泡泡浴隔热系数都是显式可替换假设。",
        "",
        "## Q1 温度空间-时间模型与最优策略",
        f"- 推荐流量：{best['flow_l_per_min']} L/min。",
        f"- 推荐动作：{best['motion']}。",
        f"- 40 分钟溢流水量：{best['wasted_liters']} L。",
        f"- 平均温度误差：{best['mean_abs_error_c']} C；平均空间温差：{best['mean_spatial_range_c']} C。",
        "",
        "## Q2 形状、人体和动作敏感性",
        "- 长浅浴缸表面积更大，散热和空间不均匀更明显。",
        "- 人体增加排水体积并与水换热，较冷或较大体型需要更多热水或动作混合。",
        "- 主动搅动降低空间温差，但现实中舒适性和安全性限制其强度。",
        "",
        "## Q3 泡泡浴影响",
        f"- 解释：{result['bubble_bath_effect']['interpretation']}",
        "",
        "## Q4 给浴缸用户的一页说明",
        result["user_explanation"],
        "",
        "## 输出文件",
        f"- `result.json`：{RESULT_PATH}",
        f"- `temperature_strategy_grid.csv`：{ARTIFACT_DIR / 'temperature_strategy_grid.csv'}",
        f"- `tub_shape_sensitivity.csv`：{ARTIFACT_DIR / 'tub_shape_sensitivity.csv'}",
        f"- `bubble_bath_sensitivity.csv`：{ARTIFACT_DIR / 'bubble_bath_sensitivity.csv'}",
        f"- `temperature_profiles.png`：{ARTIFACT_DIR / 'temperature_profiles.png'}",
    ]
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    if not PDF_PATH.exists():
        raise FileNotFoundError(f"Missing official PDF: {PDF_PATH}")
    strategy = thermal_strategy()
    best_flow = float(strategy["recommended_strategy"]["flow_l_per_min"])
    sensitivity = shape_person_motion_sensitivity(best_flow)
    bubble = bubble_bath_effect(best_flow)
    result = {
        "problem_id": "2016-A",
        "data_source": {
            "type": "official_statement_parameters",
            "root": str(PDF_PATH),
            "source_pdf": str(PDF_PATH),
            "official_constraints": [
                "single faucet fills hot water",
                "simple bathtub without heater or circulating jets",
                "constant trickle of hot water reheats the bath",
                "overflow drain removes excess water at capacity",
                "model must account for space and time temperature variation",
                "bubble bath may affect model results",
            ],
            "assumptions": {"tub": BASE_TUB, "person": PERSON, **ASSUMPTIONS},
        },
        "thermal_strategy": strategy,
        "shape_person_motion_sensitivity": sensitivity,
        "bubble_bath_effect": bubble,
        "user_explanation": user_explanation(strategy, sensitivity, bubble),
        "assumption_audit": {
            "truthfulness_note": "This workflow uses official statement constraints and explicit deterministic physics assumptions; it does not claim measured bath sensor data.",
            "replaceable_assumptions": {"tub": BASE_TUB, "person": PERSON, **ASSUMPTIONS},
        },
    }
    write_artifacts(strategy, sensitivity, bubble)
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_report(result)
    print(json.dumps({"result": str(RESULT_PATH), "report": str(REPORT_PATH), "artifacts": str(ARTIFACT_DIR)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
