from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ARCHIVE_ROOT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
PDF_PATH = ARCHIVE_ROOT / "official_assets_extracted" / "2024" / "Resource Availability and Sex Ratios.pdf"
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"

LOW_FOOD_MALE_RATIO = 0.78
HIGH_FOOD_MALE_RATIO = 0.56
MONTHS = 240

SCENARIOS = {
    "low_food_adaptive": {"resource": 0.12, "adaptive": True, "harvest_pressure": 0.00},
    "medium_food_adaptive": {"resource": 0.50, "adaptive": True, "harvest_pressure": 0.00},
    "high_food_adaptive": {"resource": 0.90, "adaptive": True, "harvest_pressure": 0.00},
    "fixed_equal_ratio": {"resource": 0.50, "adaptive": False, "fixed_male_ratio": 0.50, "harvest_pressure": 0.00},
    "lamprey_reduced_control": {"resource": 0.50, "adaptive": True, "harvest_pressure": 0.38},
}


def clean_float(value: float, digits: int = 6) -> float:
    return round(float(value), digits)


def ensure_pdf_exists() -> None:
    if not PDF_PATH.exists():
        raise FileNotFoundError(f"Official problem PDF not found: {PDF_PATH}")


def sex_ratio_response(resource: float, adaptive: bool = True, fixed_male_ratio: float = 0.50) -> float:
    if not adaptive:
        return fixed_male_ratio
    clipped = min(1.0, max(0.0, resource))
    # Official endpoints: low food -> 78% male, high food -> 56% male.
    return LOW_FOOD_MALE_RATIO - (LOW_FOOD_MALE_RATIO - HIGH_FOOD_MALE_RATIO) * clipped


def mating_success(male_ratio: float) -> float:
    female_ratio = 1.0 - male_ratio
    # Pair formation is best near balanced ratios, but female scarcity is the limiting bottleneck under low food.
    return max(0.0, 4.0 * male_ratio * female_ratio)


def simulate_scenario(name: str, params: dict[str, float | bool]) -> pd.DataFrame:
    resource = float(params["resource"])
    adaptive = bool(params.get("adaptive", True))
    fixed = float(params.get("fixed_male_ratio", 0.50))
    harvest = float(params.get("harvest_pressure", 0.0))
    lamprey = 0.42
    host_fish = 0.78
    parasites = 0.24
    predators_food_web = 0.30
    rows = []
    for month in range(MONTHS + 1):
        seasonal_resource = min(1.0, max(0.0, resource + 0.10 * np.sin(2 * np.pi * month / 12.0)))
        male_ratio = sex_ratio_response(seasonal_resource, adaptive=adaptive, fixed_male_ratio=fixed)
        reproduction = 0.115 * mating_success(male_ratio) * lamprey * (1.0 - lamprey / 1.25)
        larval_survival = 0.025 + 0.070 * seasonal_resource
        parasitic_mortality = 0.075 * lamprey * host_fish
        lamprey_food_value = 0.035 * lamprey
        parasite_benefit = 0.050 * lamprey * parasites

        rows.append(
            {
                "scenario": name,
                "month": month,
                "resource_index": clean_float(seasonal_resource, 5),
                "male_ratio": clean_float(male_ratio, 5),
                "lamprey": clean_float(lamprey, 5),
                "host_fish": clean_float(host_fish, 5),
                "parasites": clean_float(parasites, 5),
                "predators_food_web": clean_float(predators_food_web, 5),
                "mating_success": clean_float(mating_success(male_ratio), 5),
            }
        )
        if month == MONTHS:
            break

        lamprey = min(1.4, max(0.02, lamprey + reproduction + larval_survival * lamprey - 0.050 * lamprey - harvest * 0.055 * lamprey))
        host_fish = min(1.4, max(0.05, host_fish + 0.060 * host_fish * (1 - host_fish / 1.15) - parasitic_mortality))
        parasites = min(1.2, max(0.02, parasites + parasite_benefit - 0.035 * parasites))
        predators_food_web = min(1.2, max(0.02, predators_food_web + lamprey_food_value - 0.025 * predators_food_web))
    return pd.DataFrame(rows)


def run_scenarios() -> tuple[pd.DataFrame, pd.DataFrame]:
    trajectories = [simulate_scenario(name, params) for name, params in SCENARIOS.items()]
    all_df = pd.concat(trajectories, ignore_index=True)
    summary_rows = []
    for name, df in all_df.groupby("scenario"):
        tail = df[df["month"] >= MONTHS - 59]
        stability = ecosystem_stability_score(tail)
        summary_rows.append(
            {
                "scenario": name,
                "mean_resource_index": clean_float(tail["resource_index"].mean(), 4),
                "mean_male_ratio": clean_float(tail["male_ratio"].mean(), 4),
                "mean_lamprey": clean_float(tail["lamprey"].mean(), 4),
                "mean_host_fish": clean_float(tail["host_fish"].mean(), 4),
                "mean_parasites": clean_float(tail["parasites"].mean(), 4),
                "mean_food_web_benefit": clean_float(tail["predators_food_web"].mean(), 4),
                "mean_mating_success": clean_float(tail["mating_success"].mean(), 4),
                **stability,
            }
        )
    return all_df, pd.DataFrame(summary_rows)


def ecosystem_stability_score(df: pd.DataFrame) -> dict[str, float]:
    state_cols = ["lamprey", "host_fish", "parasites", "predators_food_web"]
    means = df[state_cols].mean()
    volatility = df[state_cols].std().mean()
    host_damage = max(0.0, 0.82 - means["host_fish"])
    balance = 1.0 - float(np.std([means["lamprey"], means["host_fish"], means["parasites"], means["predators_food_web"]]))
    score = 0.42 * balance + 0.25 * means["host_fish"] + 0.18 * means["predators_food_web"] - 0.22 * host_damage - 0.20 * volatility
    return {
        "state_volatility": clean_float(volatility, 4),
        "host_damage_index": clean_float(host_damage, 4),
        "ecosystem_stability_score": clean_float(score, 4),
    }


def build_response_curve() -> pd.DataFrame:
    resources = np.round(np.linspace(0.0, 1.0, 21), 2)
    rows = []
    for resource in resources:
        male = sex_ratio_response(float(resource))
        rows.append(
            {
                "resource_index": float(resource),
                "male_ratio": clean_float(male, 4),
                "female_ratio": clean_float(1.0 - male, 4),
                "mating_success_index": clean_float(mating_success(male), 4),
            }
        )
    df = pd.DataFrame(rows)
    df.to_csv(ARTIFACT_DIR / "sex_ratio_response.csv", index=False)
    return df


def build_stability_surface() -> pd.DataFrame:
    rows = []
    for resource in np.linspace(0.0, 1.0, 11):
        for harvest in np.linspace(0.0, 0.5, 6):
            df = simulate_scenario("surface", {"resource": float(resource), "adaptive": True, "harvest_pressure": float(harvest)})
            tail = df[df["month"] >= MONTHS - 59]
            rows.append(
                {
                    "resource_index": clean_float(resource, 3),
                    "lamprey_reduction_pressure": clean_float(harvest, 3),
                    "mean_male_ratio": clean_float(tail["male_ratio"].mean(), 4),
                    "mean_lamprey": clean_float(tail["lamprey"].mean(), 4),
                    "mean_host_fish": clean_float(tail["host_fish"].mean(), 4),
                    **ecosystem_stability_score(tail),
                }
            )
    df = pd.DataFrame(rows)
    df.to_csv(ARTIFACT_DIR / "stability_surface.csv", index=False)
    return df


def public_rows(df: pd.DataFrame, n: int | None = None) -> list[dict[str, object]]:
    subset = df if n is None else df.head(n)
    return subset.to_dict(orient="records")


def scenario_public(row: dict[str, object]) -> dict[str, object]:
    out = dict(row)
    if "mean_male_ratio" in out:
        out["male_ratio"] = out["mean_male_ratio"]
    return out


def build_result(trajectory_df: pd.DataFrame, summary_df: pd.DataFrame, response_df: pd.DataFrame, stability_df: pd.DataFrame) -> dict[str, object]:
    low = summary_df[summary_df["scenario"] == "low_food_adaptive"].iloc[0].to_dict()
    high = summary_df[summary_df["scenario"] == "high_food_adaptive"].iloc[0].to_dict()
    adaptive_mid = summary_df[summary_df["scenario"] == "medium_food_adaptive"].iloc[0].to_dict()
    fixed_mid = summary_df[summary_df["scenario"] == "fixed_equal_ratio"].iloc[0].to_dict()
    reduced = summary_df[summary_df["scenario"] == "lamprey_reduced_control"].iloc[0].to_dict()
    return {
        "problem_id": "2024-A",
        "title": "Resource Availability and Sex Ratios",
        "data_source": {
            "type": "official_statement_parameters",
            "root": str(ARCHIVE_ROOT / "official_assets_extracted"),
            "source_pdf": str(PDF_PATH),
            "official_requirements": {
                "resource_dependent_lamprey_sex_ratio": True,
                "ecosystem_interactions": True,
                "advantages_and_disadvantages": True,
                "stability_and_other_species": True,
            },
            "parameters": {
                "low_food_male_ratio": LOW_FOOD_MALE_RATIO,
                "high_food_male_ratio": HIGH_FOOD_MALE_RATIO,
                "months_simulated": MONTHS,
                "source_statement": "low food male percentage can reach approximately 78%; high food male percentage observed approximately 56%",
            },
        },
        "sex_ratio_model": {
            "model": "linear adaptive response between the two official male-ratio endpoints, embedded in monthly ecosystem dynamics",
            "response_curve": public_rows(response_df),
            "formula": "male_ratio(resource)=0.78-(0.78-0.56)*resource_index",
        },
        "ecosystem_impact": {
            "model": "lamprey-host-parasite-food-web difference equations with resource-dependent sex ratio and lamprey reduction pressure",
            "scenario_comparison": public_rows(summary_df.sort_values("scenario")),
            "lamprey_reduction_effect": {
                "control_scenario": "lamprey_reduced_control",
                "mean_lamprey": reduced["mean_lamprey"],
                "mean_host_fish": reduced["mean_host_fish"],
                "ecosystem_stability_score": reduced["ecosystem_stability_score"],
                "interpretation": "reducing lampreys relieves host fish but also reduces lamprey food-web value and parasite habitat",
            },
        },
        "lamprey_population_tradeoffs": {
            "low_food": scenario_public(low),
            "high_food": scenario_public(high),
            "advantages": [
                "male-biased low-food cohorts preserve mating opportunities when larval resources are poor",
                "resource-sensitive sex ratios prevent overproduction of females when juvenile survival is low",
                "adaptive ratios can dampen population overshoot relative to a fixed sex ratio",
            ],
            "disadvantages": [
                "strong male bias lowers female availability and can bottleneck reproduction",
                "sex-ratio plasticity makes population forecasts more sensitive to resource measurement error",
                "host-fish damage can remain high if lamprey survival is also resource-supported",
            ],
        },
        "ecosystem_stability": {
            "adaptive_medium_food": adaptive_mid,
            "fixed_equal_ratio": fixed_mid,
            "adaptive_vs_fixed_stability_gain": clean_float(adaptive_mid["ecosystem_stability_score"] - fixed_mid["ecosystem_stability_score"], 4),
            "surface_best_cases": public_rows(stability_df.sort_values("ecosystem_stability_score", ascending=False).head(8)),
            "surface_worst_cases": public_rows(stability_df.sort_values("ecosystem_stability_score", ascending=True).head(8)),
        },
        "parasite_and_other_species_effects": {
            "beneficiaries": [
                {"species_group": "host fish", "condition": "benefits when lamprey reduction pressure lowers parasitic mortality"},
                {"species_group": "parasites of lampreys", "condition": "benefit when lamprey abundance remains moderate to high"},
                {"species_group": "predators / human harvest using lampreys as food", "condition": "benefit from sustained lamprey biomass"},
            ],
            "tradeoff": "variable sex ratios can indirectly help parasites and lamprey consumers by stabilizing lamprey persistence, but high lamprey density harms host fish",
        },
    }


def write_artifacts(trajectory_df: pd.DataFrame, summary_df: pd.DataFrame) -> None:
    trajectory_df.to_csv(ARTIFACT_DIR / "ecosystem_trajectories.csv", index=False)
    summary_df.to_csv(ARTIFACT_DIR / "scenario_summary.csv", index=False)
    fig, ax1 = plt.subplots(figsize=(8.2, 4.8))
    ordered = summary_df.sort_values("mean_resource_index")
    ax1.plot(ordered["mean_resource_index"], ordered["mean_male_ratio"], marker="o", label="male ratio", color="#315f72")
    ax1.set_xlabel("Resource index")
    ax1.set_ylabel("Male ratio")
    ax1.set_ylim(0.45, 0.85)
    ax1.grid(alpha=0.25)
    ax2 = ax1.twinx()
    ax2.plot(ordered["mean_resource_index"], ordered["ecosystem_stability_score"], marker="s", color="#c75b39", label="stability")
    ax2.set_ylabel("Ecosystem stability score")
    ax1.set_title("Lamprey Sex-Ratio Adaptation and Ecosystem Tradeoff")
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "lamprey_tradeoff_frontier.png", dpi=180)
    plt.close(fig)


def build_report(result: dict[str, object]) -> None:
    lines = [
        "# 2024 MCM-A Resource Availability and Sex Ratios",
        "",
        "## 数据真实性",
        f"- 官方来源：`{result['data_source']['source_pdf']}`。",
        "- 本题无 COMAP 数值附件；脚本只使用官方 PDF 中的性别比例端点和显式系统动力学假设，不使用随机占位数据。",
        "",
        "## 官方题面参数",
        f"- 低食物环境雄性比例：{LOW_FOOD_MALE_RATIO}。",
        f"- 高食物环境雄性比例：{HIGH_FOOD_MALE_RATIO}。",
        "",
        "## 每问结果",
        "### Q1 更大生态系统影响",
        f"- 模型：{result['ecosystem_impact']['model']}。",
        f"- 七鳃鳗减少情景解释：{result['ecosystem_impact']['lamprey_reduction_effect']['interpretation']}。",
        "",
        "### Q2 七鳃鳗种群优缺点",
        "- 优点：",
    ]
    lines.extend([f"- {item}" for item in result["lamprey_population_tradeoffs"]["advantages"]])
    lines.append("- 缺点：")
    lines.extend([f"- {item}" for item in result["lamprey_population_tradeoffs"]["disadvantages"]])
    lines.extend([
        "",
        "### Q3 生态系统稳定性",
        f"- 自适应 vs 固定性别比稳定性差值：{result['ecosystem_stability']['adaptive_vs_fixed_stability_gain']}。",
        "",
        "### Q4 对其他生物的优势",
        f"- 权衡：{result['parasite_and_other_species_effects']['tradeoff']}。",
        "",
        "## 输出产物",
        "- `sex_ratio_response.csv`：资源-雄性比例响应曲线。",
        "- `ecosystem_trajectories.csv`：月度生态状态轨迹。",
        "- `stability_surface.csv`：资源与七鳃鳗控制压力稳定性网格。",
        "- `lamprey_tradeoff_frontier.png`：性别比和稳定性权衡图。",
    ])
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ensure_pdf_exists()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    response_df = build_response_curve()
    stability_df = build_stability_surface()
    trajectory_df, summary_df = run_scenarios()
    write_artifacts(trajectory_df, summary_df)
    result = build_result(trajectory_df, summary_df, response_df, stability_df)
    result["artifacts"] = {
        "sex_ratio_response": str(ARTIFACT_DIR / "sex_ratio_response.csv"),
        "ecosystem_trajectories": str(ARTIFACT_DIR / "ecosystem_trajectories.csv"),
        "scenario_summary": str(ARTIFACT_DIR / "scenario_summary.csv"),
        "stability_surface": str(ARTIFACT_DIR / "stability_surface.csv"),
        "lamprey_tradeoff_frontier": str(ARTIFACT_DIR / "lamprey_tradeoff_frontier.png"),
    }
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    build_report(result)
    print(json.dumps({"result": str(RESULT_PATH), "report": str(REPORT_PATH), "artifacts": str(ARTIFACT_DIR)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
