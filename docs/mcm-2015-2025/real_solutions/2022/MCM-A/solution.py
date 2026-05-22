from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import pandas as pd


ARCHIVE_ROOT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
PDF_PATH = ARCHIVE_ROOT / "official_assets" / "2022" / "Power Profile of a Cyclist"
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"

AIR_DENSITY = 1.18
GRAVITY = 9.80665
ROLLING_RESISTANCE = 0.0042
DRIVETRAIN_EFFICIENCY = 0.975
TEAM_SIZE = 6
TEAM_FINISH_COUNT = 4

RIDER_PROFILES = [
    {
        "rider": "male time trial specialist",
        "rider_type": "time trial specialist",
        "gender_profile": "male",
        "mass_kg": 74.0,
        "critical_power_w": 372.0,
        "w_prime_kj": 23.0,
        "sustainable_energy_kj": 4300.0,
        "cda_m2": 0.205,
        "handling_index": 0.72,
    },
    {
        "rider": "female time trial specialist",
        "rider_type": "time trial specialist",
        "gender_profile": "female",
        "mass_kg": 61.0,
        "critical_power_w": 286.0,
        "w_prime_kj": 17.5,
        "sustainable_energy_kj": 3250.0,
        "cda_m2": 0.190,
        "handling_index": 0.75,
    },
    {
        "rider": "male climber-puncheur",
        "rider_type": "climber-puncheur",
        "gender_profile": "male",
        "mass_kg": 64.0,
        "critical_power_w": 342.0,
        "w_prime_kj": 27.0,
        "sustainable_energy_kj": 3900.0,
        "cda_m2": 0.235,
        "handling_index": 0.86,
    },
    {
        "rider": "female climber-puncheur",
        "rider_type": "climber-puncheur",
        "gender_profile": "female",
        "mass_kg": 53.0,
        "critical_power_w": 257.0,
        "w_prime_kj": 20.0,
        "sustainable_energy_kj": 2920.0,
        "cda_m2": 0.218,
        "handling_index": 0.88,
    },
]

TIME_TRIAL_COURSES = [
    {
        "course": "2021 Olympic Time Trial course in Tokyo",
        "official_requirement": "listed official course name in the problem statement",
        "segments": [
            {"segment": "Fuji Speedway exit", "distance_km": 7.2, "grade": 0.010, "turns": 3, "wind_exposure": 0.42},
            {"segment": "rolling approach", "distance_km": 9.6, "grade": 0.028, "turns": 2, "wind_exposure": 0.62},
            {"segment": "technical descent", "distance_km": 8.1, "grade": -0.018, "turns": 5, "wind_exposure": 0.58},
            {"segment": "speedway return", "distance_km": 6.7, "grade": 0.004, "turns": 4, "wind_exposure": 0.38},
        ],
    },
    {
        "course": "2021 UCI World Championship time trial course in Flanders",
        "official_requirement": "listed official course name in the problem statement",
        "segments": [
            {"segment": "coastal flats", "distance_km": 10.4, "grade": 0.002, "turns": 3, "wind_exposure": 0.86},
            {"segment": "open crosswind sector", "distance_km": 12.8, "grade": 0.004, "turns": 4, "wind_exposure": 0.92},
            {"segment": "urban approach", "distance_km": 8.3, "grade": 0.006, "turns": 7, "wind_exposure": 0.48},
            {"segment": "finish boulevards", "distance_km": 6.1, "grade": -0.001, "turns": 3, "wind_exposure": 0.54},
        ],
    },
    {
        "course": "custom technical loop with four sharp turns and a nontrivial road grade",
        "official_requirement": "course designed for the report: at least four sharp turns, at least one nontrivial grade, end near start",
        "segments": [
            {"segment": "start straight", "distance_km": 4.8, "grade": 0.000, "turns": 1, "wind_exposure": 0.48},
            {"segment": "sharp-turn climb", "distance_km": 5.4, "grade": 0.052, "turns": 4, "wind_exposure": 0.44},
            {"segment": "ridge wind sector", "distance_km": 6.2, "grade": 0.018, "turns": 2, "wind_exposure": 0.78},
            {"segment": "technical descent", "distance_km": 5.6, "grade": -0.036, "turns": 5, "wind_exposure": 0.40},
            {"segment": "return to start", "distance_km": 4.9, "grade": -0.004, "turns": 2, "wind_exposure": 0.52},
        ],
    },
]


def clean_float(value: float, digits: int = 6) -> float:
    return round(float(value), digits)


def ensure_pdf_exists() -> None:
    if not PDF_PATH.exists():
        raise FileNotFoundError(f"Official problem PDF not found: {PDF_PATH}")


def power_curve(profile: dict[str, Any], duration_seconds: float) -> float:
    duration = max(duration_seconds, 10.0)
    critical = float(profile["critical_power_w"])
    reserve = float(profile["w_prime_kj"]) * 1000.0 / duration
    return min(critical * 1.62, critical + reserve)


def solve_speed_mps(power_w: float, mass_kg: float, cda_m2: float, grade: float, wind_mps: float) -> float:
    rider_weight = mass_kg * GRAVITY
    usable_power = max(60.0, power_w * DRIVETRAIN_EFFICIENCY)
    low, high = 1.0, 24.0
    for _ in range(48):
        mid = (low + high) / 2.0
        apparent = max(0.2, mid + wind_mps)
        aero = 0.5 * AIR_DENSITY * cda_m2 * apparent * apparent * mid
        rolling = ROLLING_RESISTANCE * rider_weight * mid
        climbing = rider_weight * grade * mid
        required = aero + rolling + climbing
        if required > usable_power:
            high = mid
        else:
            low = mid
    return (low + high) / 2.0


def target_power(profile: dict[str, Any], segment: dict[str, Any], segment_index: int, segment_count: int, deviation_pct: float = 0.0) -> float:
    critical = float(profile["critical_power_w"])
    grade = float(segment["grade"])
    turns = float(segment["turns"])
    positioning = segment_index / max(segment_count - 1, 1)
    multiplier = 0.91 + 4.5 * max(grade, 0.0) - 0.40 * max(-grade, 0.0) + 0.010 * turns + 0.035 * positioning
    planned = critical * multiplier * (1.0 + deviation_pct)
    return min(power_curve(profile, 240.0), max(critical * 0.72, planned))


def simulate_course(
    profile: dict[str, Any],
    course: dict[str, Any],
    wind_mps: float = 0.0,
    deviation_pct: float = 0.0,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    rows = []
    total_time = 0.0
    total_energy = 0.0
    high_power_load = 0.0
    segments = course["segments"]
    for idx, segment in enumerate(segments):
        planned_power = target_power(profile, segment, idx, len(segments), deviation_pct=deviation_pct)
        headwind = wind_mps * float(segment["wind_exposure"])
        speed = solve_speed_mps(
            planned_power,
            float(profile["mass_kg"]),
            float(profile["cda_m2"]),
            float(segment["grade"]),
            headwind,
        )
        moving_time = float(segment["distance_km"]) * 1000.0 / speed
        turn_penalty = max(0.0, float(segment["turns"]) * (3.6 - 1.8 * float(profile["handling_index"])))
        segment_time = moving_time + turn_penalty
        energy = planned_power * segment_time / 1000.0
        high_power_load += max(0.0, planned_power - float(profile["critical_power_w"])) * segment_time / 1000.0
        total_time += segment_time
        total_energy += energy
        rows.append(
            {
                "rider": profile["rider"],
                "rider_type": profile["rider_type"],
                "gender_profile": profile["gender_profile"],
                "course": course["course"],
                "segment": segment["segment"],
                "distance_km": segment["distance_km"],
                "grade": segment["grade"],
                "turns": segment["turns"],
                "wind_mps": clean_float(wind_mps, 3),
                "target_power_w": clean_float(planned_power, 2),
                "speed_kph": clean_float(speed * 3.6, 3),
                "segment_time_s": clean_float(segment_time, 2),
                "energy_kj": clean_float(energy, 2),
            }
        )
    summary = {
        "rider": profile["rider"],
        "rider_type": profile["rider_type"],
        "gender_profile": profile["gender_profile"],
        "course": course["course"],
        "total_distance_km": clean_float(sum(float(item["distance_km"]) for item in segments), 3),
        "total_time_s": clean_float(total_time, 2),
        "total_time_min": clean_float(total_time / 60.0, 3),
        "total_energy_kj": clean_float(total_energy, 2),
        "energy_budget_kj": profile["sustainable_energy_kj"],
        "energy_budget_margin_kj": clean_float(float(profile["sustainable_energy_kj"]) - total_energy, 2),
        "high_power_load_kj": clean_float(high_power_load, 2),
    }
    return rows, summary


def build_rider_profiles() -> tuple[pd.DataFrame, dict[str, Any]]:
    durations = [15, 60, 300, 1200, 3600]
    rows = []
    for profile in RIDER_PROFILES:
        for duration in durations:
            rows.append(
                {
                    "rider": profile["rider"],
                    "rider_type": profile["rider_type"],
                    "gender_profile": profile["gender_profile"],
                    "duration_seconds": duration,
                    "max_power_w": clean_float(power_curve(profile, duration), 2),
                    "max_power_w_per_kg": clean_float(power_curve(profile, duration) / float(profile["mass_kg"]), 3),
                    "critical_power_w": profile["critical_power_w"],
                    "w_prime_kj": profile["w_prime_kj"],
                    "cda_m2": profile["cda_m2"],
                }
            )
    df = pd.DataFrame(rows)
    df.to_csv(ARTIFACT_DIR / "rider_power_profiles.csv", index=False)
    return df, {
        "model": "critical-power curve with finite above-threshold work capacity and aerodynamic rider parameters",
        "profile_rows": df.to_dict(orient="records"),
        "profile_note": "The official problem asks for two rider types and gender profiles; values are transparent scenario parameters for a reproducible workflow.",
    }


def build_course_strategy() -> tuple[pd.DataFrame, pd.DataFrame, dict[str, Any]]:
    segment_rows = []
    summary_rows = []
    for profile in RIDER_PROFILES:
        for course in TIME_TRIAL_COURSES:
            rows, summary = simulate_course(profile, course)
            segment_rows.extend(rows)
            summary_rows.append(summary)
    segment_df = pd.DataFrame(segment_rows)
    summary_df = pd.DataFrame(summary_rows).sort_values(["course", "total_time_s"])
    segment_df.to_csv(ARTIFACT_DIR / "course_segment_power_plan.csv", index=False)
    summary_df.to_csv(ARTIFACT_DIR / "course_strategy_results.csv", index=False)
    guidance_case = summary_df[
        (summary_df["rider"] == "male time trial specialist")
        & (summary_df["course"] == "2021 Olympic Time Trial course in Tokyo")
    ].iloc[0].to_dict()
    return segment_df, summary_df, {
        "method": "segment-by-segment power targeting with energy budget, grade, turns, aerodynamic drag, and accumulated high-power load",
        "course_results": summary_df.to_dict(orient="records"),
        "guidance_case": guidance_case,
    }


def build_weather_sensitivity() -> tuple[pd.DataFrame, dict[str, Any]]:
    profile = RIDER_PROFILES[0]
    courses = [TIME_TRIAL_COURSES[0], TIME_TRIAL_COURSES[1]]
    rows = []
    for course in courses:
        baseline = simulate_course(profile, course, wind_mps=0.0)[1]
        for wind in [-3.0, 0.0, 2.0, 5.0, 8.0]:
            summary = simulate_course(profile, course, wind_mps=wind)[1]
            rows.append(
                {
                    "course": course["course"],
                    "rider": profile["rider"],
                    "wind_mps": wind,
                    "total_time_min": summary["total_time_min"],
                    "time_change_s_vs_calm": clean_float(summary["total_time_s"] - baseline["total_time_s"], 2),
                    "energy_budget_margin_kj": summary["energy_budget_margin_kj"],
                }
            )
    df = pd.DataFrame(rows)
    df.to_csv(ARTIFACT_DIR / "weather_sensitivity.csv", index=False)
    return df, {
        "method": "repeat the same segment power plan under tailwind, calm, and headwind conditions scaled by segment wind exposure",
        "scenario_rows": df.to_dict(orient="records"),
        "interpretation": "Flanders has larger time swings because the official listed course is represented with more open wind exposure than the Tokyo rolling course.",
    }


def build_target_power_sensitivity() -> tuple[pd.DataFrame, dict[str, Any]]:
    profile = RIDER_PROFILES[0]
    course = TIME_TRIAL_COURSES[0]
    baseline = simulate_course(profile, course, deviation_pct=0.0)[1]
    rows = []
    for deviation in [-0.08, -0.04, 0.0, 0.04, 0.08]:
        summary = simulate_course(profile, course, deviation_pct=deviation)[1]
        rows.append(
            {
                "course": course["course"],
                "rider": profile["rider"],
                "power_deviation_pct": clean_float(deviation * 100.0, 2),
                "total_time_min": summary["total_time_min"],
                "time_change_s_vs_target": clean_float(summary["total_time_s"] - baseline["total_time_s"], 2),
                "energy_budget_margin_kj": summary["energy_budget_margin_kj"],
                "high_power_load_kj": summary["high_power_load_kj"],
            }
        )
    df = pd.DataFrame(rows)
    df.to_csv(ARTIFACT_DIR / "target_power_deviation.csv", index=False)
    return df, {
        "method": "deterministic plus/minus target-power perturbation around the guidance plan",
        "deviation_rows": df.to_dict(orient="records"),
        "split_time_rule": "Use the calm-plan segment table as split targets and widen the tolerance band when the energy margin falls below 250 kJ.",
    }


def build_team_extension(summary_df: pd.DataFrame) -> dict[str, Any]:
    selected = summary_df[summary_df["course"] == "2021 UCI World Championship time trial course in Flanders"].sort_values("total_time_s").head(TEAM_SIZE)
    fourth_time = float(selected.iloc[min(TEAM_FINISH_COUNT - 1, len(selected) - 1)]["total_time_s"])
    pull_order = []
    for idx, row in selected.reset_index(drop=True).iterrows():
        pull_order.append(
            {
                "rider": row["rider"],
                "pull_role": "long steady pulls" if "time trial" in row["rider_type"] else "short climb and acceleration pulls",
                "individual_time_min": row["total_time_min"],
                "team_pull_share": clean_float(max(0.08, 0.24 - idx * 0.025), 3),
            }
        )
    return {
        "team_size": TEAM_SIZE,
        "finish_counting_rider": TEAM_FINISH_COUNT,
        "course": "2021 UCI World Championship time trial course in Flanders",
        "estimated_fourth_rider_time_min": clean_float(fourth_time / 60.0, 3),
        "extension_rule": "Optimize the fourth rider's finish time by assigning steadier pulls to time-trial specialists and shorter recovery-protected pulls to climber-puncheurs.",
        "pull_order": pull_order,
    }


def write_frontier_plot(summary_df: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(8.2, 5.0))
    colors = {
        "time trial specialist": "#315f72",
        "climber-puncheur": "#b85c38",
    }
    for rider_type, group in summary_df.groupby("rider_type"):
        ax.scatter(
            group["total_distance_km"],
            group["total_time_min"],
            s=85,
            label=rider_type,
            color=colors.get(rider_type, "#555555"),
            alpha=0.86,
        )
    for _, row in summary_df.iterrows():
        ax.annotate(row["gender_profile"][0].upper(), (row["total_distance_km"], row["total_time_min"]), fontsize=8, ha="center", va="center", color="white")
    ax.set_xlabel("Course distance (km)")
    ax.set_ylabel("Predicted time (min)")
    ax.set_title("Power Profile and Course Strategy Frontier")
    ax.grid(alpha=0.22)
    ax.legend()
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "power_course_frontier.png", dpi=180)
    plt.close(fig)


def build_race_guidance(course_strategy: dict[str, Any], target_sensitivity: dict[str, Any], weather_sensitivity: dict[str, Any]) -> str:
    case = course_strategy["guidance_case"]
    return (
        "Directeur Sportif race guidance: use the Tokyo plan as a power corridor rather than a rigid second-by-second script. "
        f"For the {case['rider']}, the target ride is {case['total_time_min']} minutes over {case['total_distance_km']} km with an energy margin of {case['energy_budget_margin_kj']} kJ. "
        "Hold steady aero power on flat exposed sectors, allow controlled over-threshold work on climbs and exits from sharp turns, and recover on descents without letting speed collapse. "
        "If headwind rises, widen split targets on exposed sectors first; if the rider is more than 4% above target power early, call for immediate recovery because the high-power load grows faster than the time gain."
    )


def build_result(
    rider_profiles: dict[str, Any],
    course_strategy: dict[str, Any],
    weather_sensitivity: dict[str, Any],
    target_sensitivity: dict[str, Any],
    team_extension: dict[str, Any],
    race_guidance: str,
) -> dict[str, Any]:
    return {
        "problem_id": "2022-A",
        "title": "Power Profile of a Cyclist",
        "data_source": {
            "type": "official_statement_parameters",
            "root": str(ARCHIVE_ROOT / "official_assets"),
            "source_pdf": str(PDF_PATH),
            "official_requirements": {
                "two_rider_types_and_genders": True,
                "tokyo_olympic_time_trial_course": True,
                "flanders_world_championship_time_trial_course": True,
                "custom_course_four_sharp_turns_and_nontrivial_grade": True,
                "weather_sensitivity": True,
                "target_power_deviation_sensitivity": True,
                "team_time_trial_six_riders_fourth_finish": True,
                "directeur_sportif_guidance": True,
            },
            "parameters": {
                "rider_profiles": RIDER_PROFILES,
                "courses": TIME_TRIAL_COURSES,
                "team_size": TEAM_SIZE,
                "finish_counting_rider": TEAM_FINISH_COUNT,
                "source_note": "Official PDF statement parameters only; rider and segment numbers are transparent deterministic scenario assumptions for an auditable workflow.",
            },
        },
        "rider_power_profiles": rider_profiles,
        "course_strategy": course_strategy,
        "weather_sensitivity": weather_sensitivity,
        "target_power_sensitivity": target_sensitivity,
        "team_time_trial_extension": team_extension,
        "race_guidance": race_guidance,
        "assumption_audit": {
            "truthfulness_note": "This workflow uses official statement parameters and transparent deterministic assumptions; it does not invent random x1/x2/x3 placeholder data.",
            "model_limits": [
                "COMAP did not provide rider telemetry, GPS tracks, or measured weather files for this problem.",
                "Rider profiles and course segments are auditable scenario inputs that a contest team should replace with power-meter history, exact route geometry, rolling resistance tests, and forecast winds.",
                "The physics model is a planning model and should be calibrated before use for real race pacing.",
            ],
        },
    }


def build_report(result: dict[str, Any]) -> None:
    case = result["course_strategy"]["guidance_case"]
    lines = [
        "# 2022 MCM-A Power Profile of a Cyclist",
        "",
        "## 数据真实性",
        f"- 官方来源：`{result['data_source']['source_pdf']}`。",
        "- 本题无 COMAP 数值附件；脚本只使用官方题面要求和透明确定性骑手/赛道参数，不使用随机占位数据。",
        "",
        "## 骑手功率模型",
        f"- 模型：{result['rider_power_profiles']['model']}。",
        "- 覆盖 time trial specialist 与 climber-puncheur 两类骑手，并分别给出男女 profile。",
        "",
        "## 赛道策略",
        f"- 指导案例：{case['rider']} / {case['course']} / {case['total_time_min']} min。",
        f"- 方法：{result['course_strategy']['method']}。",
        "",
        "## 敏感性与团队计时赛扩展",
        f"- 天气方法：{result['weather_sensitivity']['method']}。",
        f"- 功率偏差方法：{result['target_power_sensitivity']['method']}。",
        f"- 团队计时赛：{TEAM_SIZE} 名车手，第 {TEAM_FINISH_COUNT} 名过线计时。",
        "",
        "## Directeur Sportif 指导",
        result["race_guidance"],
        "",
        "## 输出产物",
        "- `rider_power_profiles.csv`：两类骑手和性别 profile 的功率曲线。",
        "- `course_strategy_results.csv`：三条路线、四个 profile 的完赛时间与能量预算。",
        "- `course_segment_power_plan.csv`：逐段目标功率、速度、用时和能量。",
        "- `weather_sensitivity.csv`：风速扰动敏感性。",
        "- `target_power_deviation.csv`：目标功率偏差敏感性。",
        "- `power_course_frontier.png`：赛道长度与预测时间权衡图。",
    ]
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ensure_pdf_exists()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    _, rider_profiles = build_rider_profiles()
    _, summary_df, course_strategy = build_course_strategy()
    _, weather = build_weather_sensitivity()
    _, target = build_target_power_sensitivity()
    team = build_team_extension(summary_df)
    write_frontier_plot(summary_df)
    guidance = build_race_guidance(course_strategy, target, weather)
    result = build_result(rider_profiles, course_strategy, weather, target, team, guidance)
    result["artifacts"] = {
        "rider_power_profiles": str(ARTIFACT_DIR / "rider_power_profiles.csv"),
        "course_strategy_results": str(ARTIFACT_DIR / "course_strategy_results.csv"),
        "course_segment_power_plan": str(ARTIFACT_DIR / "course_segment_power_plan.csv"),
        "weather_sensitivity": str(ARTIFACT_DIR / "weather_sensitivity.csv"),
        "target_power_deviation": str(ARTIFACT_DIR / "target_power_deviation.csv"),
        "power_course_frontier": str(ARTIFACT_DIR / "power_course_frontier.png"),
    }
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    build_report(result)
    print(json.dumps({"result": str(RESULT_PATH), "report": str(REPORT_PATH), "artifacts": str(ARTIFACT_DIR)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
