from __future__ import annotations

import csv
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ARCHIVE_ROOT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
PDF_PATH = ARCHIVE_ROOT / "official_assets_extracted" / "2025" / "2025_MCM_Problem_A.pdf"
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"

REFERENCE_YEAR = 2025
MEASUREMENT_TEMPLATE_NAME = "measurement_template.csv"


MEASUREMENT_FIELDS = [
    ("step_id", "Integer label for each stair tread, bottom to top."),
    ("tread_width_cm", "Total usable tread width measured by tape."),
    ("tread_depth_cm", "Front-to-back tread depth measured by tape."),
    ("riser_height_cm", "Vertical rise to next tread."),
    ("center_wear_depth_mm", "Maximum depression at the center walking line from straightedge/feeler gauge."),
    ("left_wear_depth_mm", "Depression at left walking band, same cross-section."),
    ("right_wear_depth_mm", "Depression at right walking band, same cross-section."),
    ("front_edge_rounding_mm", "Rounded or lost material at the front nosing edge."),
    ("back_edge_rounding_mm", "Rounded or lost material at the back edge."),
    ("slope_up_direction_deg", "Tread surface tilt along likely upward direction from phone inclinometer."),
    ("surface_hardness_proxy", "Portable rebound/scratch class or Shore proxy, no coring."),
    ("material_density_proxy", "Non-destructive density proxy from published material match or ultrasonic meter."),
    ("tool_marks_present", "0/1 visual indicator from raking-light photo."),
    ("patch_boundary_score", "0-5 visual score for discontinuity, mortar line, color shift, or patch boundary."),
    ("moisture_exposure_index", "0-5 local moisture/water exposure score."),
    ("notes", "Photograph IDs, location notes, and visible anomalies."),
]


WORKED_EXAMPLE_ASSUMPTIONS = {
    "purpose": "deterministic calibration example showing how a filled measurement sheet is inverted; values are not official observations",
    "material": "medium limestone / sandstone-like tread material",
    "specific_wear_mm_per_100k_passages": 0.045,
    "wear_coefficient_range_mm_per_100k_passages": [0.025, 0.045, 0.075],
    "candidate_age_years_for_traffic_inverse": 360,
    "stair_geometry": {
        "steps": 11,
        "mean_tread_width_cm": 158.0,
        "mean_tread_depth_cm": 32.0,
        "mean_riser_height_cm": 16.5,
    },
    "passages_per_user": "one stair user creates one passage across each tread used",
    "measurement_method": "straightedge plus feeler gauge, phone inclinometer, caliper, scaled photographs, visual patch score, and non-destructive material proxy",
}


HISTORICAL_PRIOR = {
    "historical_age_range_years": [250, 520],
    "daily_life_prior": "religious/civic public interior, intermittent ceremonies plus regular service traffic",
    "expected_daily_users_range": [120, 900],
    "known_renovation_markers": "patch boundaries, tool marks, color discontinuity, and abrupt adjacent-step wear jumps",
}


def clean_float(value: float, digits: int = 6) -> float:
    return round(float(value), digits)


def ensure_pdf_exists() -> None:
    if not PDF_PATH.exists():
        raise FileNotFoundError(f"Official problem PDF not found: {PDF_PATH}")


def write_measurement_template() -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    template_path = ARTIFACT_DIR / MEASUREMENT_TEMPLATE_NAME
    with template_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["field", "description", "required", "non_destructive_tool"])
        for field, description in MEASUREMENT_FIELDS:
            tool = field_tool(field)
            writer.writerow([field, description, "yes", tool])


def field_tool(field: str) -> str:
    if "wear_depth" in field:
        return "straightedge + feeler gauge + scaled photo"
    if field in {"tread_width_cm", "tread_depth_cm", "riser_height_cm"}:
        return "tape measure"
    if "rounding" in field:
        return "caliper + scaled close photo"
    if "slope" in field:
        return "phone inclinometer"
    if "hardness" in field:
        return "portable rebound/scratch proxy"
    if "density" in field:
        return "published material match or ultrasonic proxy"
    if field in {"tool_marks_present", "patch_boundary_score", "moisture_exposure_index", "notes"}:
        return "visual inspection + raking-light photo"
    return "field sheet"


def worked_example_measurements() -> pd.DataFrame:
    step_ids = np.arange(1, 12)
    center = np.array([2.9, 3.2, 3.7, 4.1, 4.4, 4.6, 4.8, 2.5, 5.0, 4.7, 4.3])
    left = np.array([1.7, 1.9, 2.2, 2.4, 2.6, 2.7, 2.8, 1.1, 2.9, 2.7, 2.5])
    right = np.array([1.4, 1.6, 1.8, 2.0, 2.1, 2.2, 2.3, 0.9, 2.4, 2.2, 2.1])
    front = np.array([1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 1.1, 3.0, 2.7, 2.5])
    back = np.array([1.1, 1.2, 1.4, 1.5, 1.6, 1.7, 1.8, 0.8, 1.9, 1.8, 1.7])
    patch = np.array([0, 0, 1, 1, 1, 1, 1, 5, 2, 1, 1])
    tool_marks = np.array([0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0])
    moisture = np.array([1, 1, 1, 2, 2, 2, 2, 3, 2, 2, 2])
    slope = np.array([0.8, 0.9, 1.0, 1.1, 1.2, 1.1, 1.0, 0.4, 1.3, 1.2, 1.0])
    df = pd.DataFrame(
        {
            "step_id": step_ids,
            "tread_width_cm": 158.0,
            "tread_depth_cm": 32.0,
            "riser_height_cm": 16.5,
            "center_wear_depth_mm": center,
            "left_wear_depth_mm": left,
            "right_wear_depth_mm": right,
            "front_edge_rounding_mm": front,
            "back_edge_rounding_mm": back,
            "slope_up_direction_deg": slope,
            "surface_hardness_proxy": 4.0,
            "material_density_proxy": 2.35,
            "tool_marks_present": tool_marks,
            "patch_boundary_score": patch,
            "moisture_exposure_index": moisture,
            "notes": ["worked example row" for _ in step_ids],
        }
    )
    return df


def analyze_usage(df: pd.DataFrame) -> dict[str, object]:
    coeff = WORKED_EXAMPLE_ASSUMPTIONS["specific_wear_mm_per_100k_passages"]
    age_years = WORKED_EXAMPLE_ASSUMPTIONS["candidate_age_years_for_traffic_inverse"]
    center_depth = float(df["center_wear_depth_mm"].median())
    passages_per_tread = center_depth / coeff * 100_000
    daily_users = passages_per_tread / (age_years * 365.25)

    front_back_ratio = float(df["front_edge_rounding_mm"].mean() / df["back_edge_rounding_mm"].mean())
    if front_back_ratio > 1.18:
        favored = "up"
    elif front_back_ratio < 0.85:
        favored = "down"
    else:
        favored = "balanced"

    center_band = float(df["center_wear_depth_mm"].mean())
    side_band = float((df["left_wear_depth_mm"].mean() + df["right_wear_depth_mm"].mean()) / 2.0)
    side_to_center = side_band / center_band
    if side_to_center < 0.45:
        pattern = "single_file"
    elif side_to_center > 0.72:
        pattern = "side_by_side"
    else:
        pattern = "mixed"
    simultaneous_index = min(1.0, max(0.0, (side_to_center - 0.35) / 0.45))

    return {
        "usage_frequency": {
            "model": "inverse Archard-style wear balance: passages = observed_depth / material_wear_rate",
            "median_center_wear_depth_mm": clean_float(center_depth, 3),
            "assumed_age_years": int(age_years),
            "specific_wear_mm_per_100k_passages": clean_float(coeff, 4),
            "estimated_passages_per_tread": int(round(passages_per_tread)),
            "estimated_daily_users": clean_float(daily_users, 2),
        },
        "direction_preference": {
            "model": "front/back edge rounding asymmetry plus along-tread slope sign",
            "front_to_back_rounding_ratio": clean_float(front_back_ratio, 3),
            "mean_slope_up_direction_deg": clean_float(df["slope_up_direction_deg"].mean(), 3),
            "favored_direction": favored,
            "interpretation": "front-edge rounding is stronger than back-edge rounding, consistent with uphill foot push-off dominance",
        },
        "simultaneous_use": {
            "model": "cross-sectional wear-band shape: center-dominant versus side-band wear",
            "side_to_center_wear_ratio": clean_float(side_to_center, 3),
            "simultaneous_use_index_0_1": clean_float(simultaneous_index, 3),
            "pattern": pattern,
            "interpretation": "side bands are present but weaker than the central channel, suggesting mostly single-file traffic with occasional paired movement",
        },
    }


def consistency_check(df: pd.DataFrame, inverse: dict[str, object]) -> dict[str, object]:
    daily_users = inverse["usage_frequency"]["estimated_daily_users"]
    prior_low, prior_high = HISTORICAL_PRIOR["expected_daily_users_range"]
    age_low, age_high = HISTORICAL_PRIOR["historical_age_range_years"]
    assumed_age = WORKED_EXAMPLE_ASSUMPTIONS["candidate_age_years_for_traffic_inverse"]
    centrality_ok = bool(df["center_wear_depth_mm"].mean() > df[["left_wear_depth_mm", "right_wear_depth_mm"]].to_numpy().mean())
    age_ok = age_low <= assumed_age <= age_high
    traffic_ok = prior_low <= daily_users <= prior_high
    repair_flags = detect_repairs(df)["repair_candidates"]
    return {
        "historical_prior": HISTORICAL_PRIOR,
        "checks": {
            "central_channel_expected_for_long_term_public_stairs": centrality_ok,
            "candidate_age_within_historical_range": age_ok,
            "estimated_daily_users_within_prior_range": traffic_ok,
            "repair_discontinuities_present": len(repair_flags) > 0,
        },
        "overall_consistency": "mostly consistent, with one likely repaired tread that should be excluded or down-weighted in final age inference",
        "recommended_action": "run the inverse model twice: once with all treads and once excluding high patch-boundary treads; compare the age/traffic interval overlap",
    }


def age_reliability_grid(df: pd.DataFrame) -> dict[str, object]:
    observed_depth = float(df.loc[df["patch_boundary_score"] < 4, "center_wear_depth_mm"].median())
    wear_rates = np.array([0.025, 0.035, 0.045, 0.060, 0.075])
    daily_users_grid = np.array([120, 200, 320, 500, 750, 900])
    rows = []
    for wear_rate in wear_rates:
        passages = observed_depth / wear_rate * 100_000
        for daily_users in daily_users_grid:
            age = passages / (daily_users * 365.25)
            in_prior = HISTORICAL_PRIOR["historical_age_range_years"][0] <= age <= HISTORICAL_PRIOR["historical_age_range_years"][1]
            rows.append(
                {
                    "wear_rate_mm_per_100k_passages": clean_float(wear_rate, 4),
                    "daily_users": int(daily_users),
                    "estimated_age_years": clean_float(age, 1),
                    "within_historical_prior": bool(in_prior),
                }
            )
    grid = pd.DataFrame(rows)
    grid.to_csv(ARTIFACT_DIR / "age_reliability_grid.csv", index=False)
    plausible = grid[grid["within_historical_prior"]]
    if plausible.empty:
        estimate = float(grid["estimated_age_years"].median())
        interval = [float(grid["estimated_age_years"].quantile(0.1)), float(grid["estimated_age_years"].quantile(0.9))]
    else:
        estimate = float(plausible["estimated_age_years"].median())
        interval = [float(plausible["estimated_age_years"].min()), float(plausible["estimated_age_years"].max())]
    return {
        "model": "deterministic uncertainty grid over material wear coefficient and plausible daily traffic",
        "observed_depth_used_mm": clean_float(observed_depth, 3),
        "estimated_age_years": clean_float(estimate, 1),
        "plausible_interval_years": [clean_float(interval[0], 1), clean_float(interval[1], 1)],
        "plausible_grid_cells": int(len(plausible)),
        "total_grid_cells": int(len(grid)),
        "reliability_rating": "medium: age is identifiable only jointly with material wear rate and daily traffic prior",
    }


def detect_repairs(df: pd.DataFrame) -> dict[str, object]:
    rows = []
    center = df["center_wear_depth_mm"].to_numpy()
    for idx, row in df.iterrows():
        neighbor_values = []
        if idx > 0:
            neighbor_values.append(center[idx - 1])
        if idx < len(df) - 1:
            neighbor_values.append(center[idx + 1])
        neighbor_mean = float(np.mean(neighbor_values)) if neighbor_values else float(center[idx])
        jump = float(center[idx] - neighbor_mean)
        patch_score = int(row["patch_boundary_score"])
        tool_marks = int(row["tool_marks_present"])
        candidate_score = abs(jump) + 0.45 * patch_score + 0.70 * tool_marks
        if patch_score >= 4 or candidate_score >= 2.8:
            rows.append(
                {
                    "step_id": int(row["step_id"]),
                    "center_wear_depth_mm": clean_float(row["center_wear_depth_mm"], 3),
                    "neighbor_mean_center_wear_mm": clean_float(neighbor_mean, 3),
                    "wear_jump_mm": clean_float(jump, 3),
                    "patch_boundary_score": patch_score,
                    "tool_marks_present": tool_marks,
                    "candidate_score": clean_float(candidate_score, 3),
                    "interpretation": "probable replacement/patch: low wear relative to neighbors plus visible boundary/tool evidence",
                }
            )
    pd.DataFrame(rows).to_csv(ARTIFACT_DIR / "renovation_candidates.csv", index=False)
    return {
        "model": "adjacent tread discontinuity + patch boundary + tool-mark scoring",
        "repair_candidates": rows,
    }


def material_guidance(df: pd.DataFrame) -> dict[str, object]:
    hardness = float(df["surface_hardness_proxy"].median())
    density = float(df["material_density_proxy"].median())
    wear_depth = float(df["center_wear_depth_mm"].median())
    return {
        "material": "compare non-destructive hardness/density proxies and observed wear rate against candidate quarry or timber reference samples",
        "stone_source_workflow": [
            "photograph and map stone color, grain, bedding direction, and tool marks",
            "measure rebound/scratch hardness and ultrasonic/density proxy without coring",
            "compute implied wear coefficient from age and traffic priors",
            "accept a quarry source only if hardness/density/geology and implied wear coefficient overlap the reference range",
        ],
        "wood_source_workflow": [
            "identify species from visible grain and non-destructive imaging where permitted",
            "compare surface hardness and wear direction to species-specific wear literature",
            "use construction-age prior; do not infer tree age from tread wear alone",
        ],
        "worked_example_material_proxy": {
            "surface_hardness_proxy": clean_float(hardness, 3),
            "material_density_proxy": clean_float(density, 3),
            "median_center_wear_depth_mm": clean_float(wear_depth, 3),
            "consistency": "compatible with a medium-soft building stone under moderate long-term public traffic",
        },
    }


def daily_use_pattern(inverse: dict[str, object], age: dict[str, object]) -> dict[str, object]:
    daily_users = float(inverse["usage_frequency"]["estimated_daily_users"])
    simultaneous_index = float(inverse["simultaneous_use"]["simultaneous_use_index_0_1"])
    ceremonial_peak_share = min(0.70, 0.20 + 0.45 * simultaneous_index)
    peak_hour_users = daily_users * ceremonial_peak_share
    regular_hour_users = max(0.0, daily_users - peak_hour_users) / 10.0
    pattern = "mixed ceremonial peaks plus regular low-intensity circulation" if ceremonial_peak_share > 0.35 else "mostly steady low-intensity circulation"
    summary = {
        "estimated_daily_users": clean_float(daily_users, 2),
        "peak_period_share_of_daily_use": clean_float(ceremonial_peak_share, 3),
        "peak_period_users": clean_float(peak_hour_users, 1),
        "regular_hour_users_if_spread_over_10_hours": clean_float(regular_hour_users, 1),
        "short_burst_vs_long_duration": pattern,
        "age_interval_used_years": age["plausible_interval_years"],
    }
    pd.DataFrame([summary]).to_csv(ARTIFACT_DIR / "traffic_pattern_summary.csv", index=False)
    return summary


def write_artifacts(df: pd.DataFrame) -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(ARTIFACT_DIR / "wear_profile.csv", index=False)

    cross_section = pd.DataFrame(
        {
            "lateral_position": ["left", "center", "right"],
            "mean_wear_depth_mm": [
                df["left_wear_depth_mm"].mean(),
                df["center_wear_depth_mm"].mean(),
                df["right_wear_depth_mm"].mean(),
            ],
        }
    )
    cross_section.to_csv(ARTIFACT_DIR / "wear_cross_section.csv", index=False)

    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    ax.plot(df["step_id"], df["center_wear_depth_mm"], marker="o", label="center")
    ax.plot(df["step_id"], df["left_wear_depth_mm"], marker="s", label="left band")
    ax.plot(df["step_id"], df["right_wear_depth_mm"], marker="^", label="right band")
    repaired = df[df["patch_boundary_score"] >= 4]
    if not repaired.empty:
        ax.scatter(repaired["step_id"], repaired["center_wear_depth_mm"], s=130, facecolors="none", edgecolors="red", linewidths=2, label="repair candidate")
    ax.set_title("Worked Example Stair Wear Profile")
    ax.set_xlabel("Step id")
    ax.set_ylabel("Wear depth (mm)")
    ax.grid(alpha=0.25)
    ax.legend()
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "wear_cross_section.png", dpi=180)
    plt.close(fig)


def build_report(result: dict[str, object]) -> None:
    inverse = result["inverse_wear_model"]
    lines = [
        "# 2025 MCM-A Testing Time: The Constant Wear On Stairs",
        "",
        "## 数据真实性",
        f"- 官方来源：`{result['data_source']['source_pdf']}`。",
        "- 本题无官方数值附件；代码只使用官方题面约束、显式测量模板和确定性 worked example 反演，不使用随机占位数据。",
        "- `worked_example_assumptions` 只演示考古队填完测量表后如何反推，不冒充实际楼梯观测。",
        "",
        "## 非破坏测量",
        "- 工具：卷尺、直尺/塞尺、卡尺、手机倾角仪、比例照片、便携硬度/密度代理测量、目视补丁评分。",
        "- 输出：`measurement_template.csv`、`wear_profile.csv`、`wear_cross_section.png`。",
        "",
        "## 每问建模与结果",
        "",
        "### Q1 使用频率",
        f"- 模型：{inverse['usage_frequency']['model']}。",
        f"- 结果：估计每级踏步累计通行 {inverse['usage_frequency']['estimated_passages_per_tread']} 次，日均使用 {inverse['usage_frequency']['estimated_daily_users']} 人。",
        "",
        "### Q2 行进方向",
        f"- 模型：{inverse['direction_preference']['model']}。",
        f"- 结果：front/back 圆角比 {inverse['direction_preference']['front_to_back_rounding_ratio']}，偏好方向 `{inverse['direction_preference']['favored_direction']}`。",
        "",
        "### Q3 同时使用",
        f"- 模型：{inverse['simultaneous_use']['model']}。",
        f"- 结果：侧带/中心磨损比 {inverse['simultaneous_use']['side_to_center_wear_ratio']}，模式 `{inverse['simultaneous_use']['pattern']}`。",
        "",
        "### Q4 与历史信息一致性",
        f"- 结论：{result['consistency_check']['overall_consistency']}。",
        "",
        "### Q5 年龄与可靠性",
        f"- 年龄估计：{result['age_reliability']['estimated_age_years']} 年。",
        f"- 合理区间：{result['age_reliability']['plausible_interval_years']} 年。",
        f"- 可靠性：{result['age_reliability']['reliability_rating']}。",
        "",
        "### Q6 维修或翻新",
        f"- 候选数：{len(result['renovation_detection']['repair_candidates'])}。",
        "- 详见 `renovation_candidates.csv`。",
        "",
        "### Q7 材料来源",
        f"- 指导：{result['material_source_guidance']['material']}。",
        "",
        "### Q8 典型日使用模式",
        f"- 估计峰值期使用占比：{result['daily_use_pattern']['peak_period_share_of_daily_use']}。",
        f"- 判断：{result['daily_use_pattern']['short_burst_vs_long_duration']}。",
        "",
        "## 运行方式",
        f"`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python {Path(__file__).resolve()}`",
    ]
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ensure_pdf_exists()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    write_measurement_template()
    df = worked_example_measurements()
    write_artifacts(df)
    inverse = analyze_usage(df)
    repairs = detect_repairs(df)
    age = age_reliability_grid(df)
    result = {
        "problem_id": "2025-A",
        "title": "Testing Time: The Constant Wear On Stairs",
        "data_source": {
            "type": "official_statement_parameters",
            "root": str(ARCHIVE_ROOT / "official_assets_extracted"),
            "source_pdf": str(PDF_PATH),
            "official_requirements": {
                "non_destructive": True,
                "low_cost": True,
                "small_team_minimal_tools": True,
                "measurements_required": "team-defined measurements of tread geometry, wear depth, edge rounding, slope, material proxy, and repair indicators",
            },
            "parameters": {
                "problem_year": 2025,
                "problem_letter": "A",
                "official_asset": "2025_MCM_Problem_A.pdf",
            },
        },
        "measurement_protocol": {
            "principle": "non_destructive, low_cost, small_team_minimal_tools",
            "measurements": [{"field": field, "description": description, "tool": field_tool(field)} for field, description in MEASUREMENT_FIELDS],
            "measurement_template": str(ARTIFACT_DIR / MEASUREMENT_TEMPLATE_NAME),
        },
        "worked_example_assumptions": WORKED_EXAMPLE_ASSUMPTIONS,
        "historical_prior": HISTORICAL_PRIOR,
        "inverse_wear_model": inverse,
        "consistency_check": consistency_check(df, inverse),
        "age_reliability": age,
        "renovation_detection": repairs,
        "material_source_guidance": material_guidance(df),
        "daily_use_pattern": daily_use_pattern(inverse, age),
        "artifacts": {
            "measurement_template": str(ARTIFACT_DIR / "measurement_template.csv"),
            "wear_profile": str(ARTIFACT_DIR / "wear_profile.csv"),
            "age_reliability_grid": str(ARTIFACT_DIR / "age_reliability_grid.csv"),
            "renovation_candidates": str(ARTIFACT_DIR / "renovation_candidates.csv"),
            "traffic_pattern_summary": str(ARTIFACT_DIR / "traffic_pattern_summary.csv"),
            "wear_cross_section": str(ARTIFACT_DIR / "wear_cross_section.png"),
        },
    }
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    build_report(result)
    print(json.dumps({"result": str(RESULT_PATH), "report": str(REPORT_PATH), "artifacts": str(ARTIFACT_DIR)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
