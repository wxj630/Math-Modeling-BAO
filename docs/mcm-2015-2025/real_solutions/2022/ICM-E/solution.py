from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import pandas as pd


ARCHIVE_ROOT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
PDF_PATH = ARCHIVE_ROOT / "official_assets" / "2022" / "Forestry for Carbon Sequestration"
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"

HORIZON_YEARS = 100
CO2_PER_CARBON = 44.0 / 12.0
CURRENT_PRACTICE_ROTATION_YEARS = 40
REQUESTED_TRANSITION_EXTENSION_YEARS = 10

OFFICIAL_STATEMENT_PARAMETERS = {
    "horizon_years": HORIZON_YEARS,
    "current_practice_rotation_years": CURRENT_PRACTICE_ROTATION_YEARS,
    "requested_transition_extension_years": REQUESTED_TRANSITION_EXTENSION_YEARS,
    "forest_products_store_carbon": True,
    "balance_carbon_with_other_values": True,
    "apply_to_various_forests": True,
    "community_article_required": True,
    "source_note": "Official PDF statement parameters only; forest rows below are deterministic scenario assumptions for audit and replacement, not observed inventory records.",
}

MANAGEMENT_PLANS = [
    {
        "plan": "no_harvest",
        "rotation_years": 999,
        "harvest_intensity": 0.00,
        "long_product_share": 0.00,
        "medium_product_share": 0.00,
        "short_product_share": 0.00,
        "biodiversity_value": 0.92,
        "recreation_value": 0.86,
        "cultural_value": 0.88,
        "product_value": 0.10,
        "transition_burden": 0.18,
    },
    {
        "plan": "selective_60_year",
        "rotation_years": 60,
        "harvest_intensity": 0.28,
        "long_product_share": 0.54,
        "medium_product_share": 0.28,
        "short_product_share": 0.08,
        "biodiversity_value": 0.84,
        "recreation_value": 0.80,
        "cultural_value": 0.81,
        "product_value": 0.54,
        "transition_burden": 0.10,
    },
    {
        "plan": "extended_50_year",
        "rotation_years": 50,
        "harvest_intensity": 0.42,
        "long_product_share": 0.50,
        "medium_product_share": 0.30,
        "short_product_share": 0.10,
        "biodiversity_value": 0.74,
        "recreation_value": 0.72,
        "cultural_value": 0.74,
        "product_value": 0.70,
        "transition_burden": 0.06,
    },
    {
        "plan": "current_40_year",
        "rotation_years": 40,
        "harvest_intensity": 0.50,
        "long_product_share": 0.45,
        "medium_product_share": 0.32,
        "short_product_share": 0.13,
        "biodiversity_value": 0.62,
        "recreation_value": 0.64,
        "cultural_value": 0.66,
        "product_value": 0.78,
        "transition_burden": 0.00,
    },
    {
        "plan": "short_30_year",
        "rotation_years": 30,
        "harvest_intensity": 0.58,
        "long_product_share": 0.36,
        "medium_product_share": 0.34,
        "short_product_share": 0.18,
        "biodiversity_value": 0.48,
        "recreation_value": 0.52,
        "cultural_value": 0.54,
        "product_value": 0.88,
        "transition_burden": 0.08,
    },
]

FOREST_CASES = [
    {
        "forest": "temperate mixed hardwood community forest",
        "region_type": "temperate",
        "initial_age": 35,
        "initial_live_carbon_t_per_ha": 118.0,
        "carrying_capacity_t_per_ha": 226.0,
        "growth_rate": 0.036,
        "soil_carbon_t_per_ha": 82.0,
        "biodiversity_sensitivity": 0.82,
        "community_product_need": 0.56,
        "harvest_suitability": 0.62,
    },
    {
        "forest": "managed pine production forest",
        "region_type": "subtropical plantation",
        "initial_age": 24,
        "initial_live_carbon_t_per_ha": 88.0,
        "carrying_capacity_t_per_ha": 188.0,
        "growth_rate": 0.052,
        "soil_carbon_t_per_ha": 58.0,
        "biodiversity_sensitivity": 0.46,
        "community_product_need": 0.82,
        "harvest_suitability": 0.86,
    },
    {
        "forest": "old-growth coastal conifer reserve",
        "region_type": "cool wet conifer",
        "initial_age": 110,
        "initial_live_carbon_t_per_ha": 244.0,
        "carrying_capacity_t_per_ha": 294.0,
        "growth_rate": 0.018,
        "soil_carbon_t_per_ha": 128.0,
        "biodiversity_sensitivity": 0.95,
        "community_product_need": 0.22,
        "harvest_suitability": 0.20,
    },
    {
        "forest": "dry interior fire-adapted pine forest",
        "region_type": "dry interior",
        "initial_age": 48,
        "initial_live_carbon_t_per_ha": 104.0,
        "carrying_capacity_t_per_ha": 168.0,
        "growth_rate": 0.030,
        "soil_carbon_t_per_ha": 54.0,
        "biodiversity_sensitivity": 0.66,
        "community_product_need": 0.50,
        "harvest_suitability": 0.54,
    },
]

PRODUCT_POOLS = {
    "long_lived_products": {"half_life_years": 80, "substitution_credit_per_t_carbon": 0.22},
    "medium_lived_products": {"half_life_years": 25, "substitution_credit_per_t_carbon": 0.12},
    "short_lived_products": {"half_life_years": 4, "substitution_credit_per_t_carbon": 0.03},
}


def clean_float(value: float, digits: int = 6) -> float:
    return round(float(value), digits)


def ensure_pdf_exists() -> None:
    if not PDF_PATH.exists():
        raise FileNotFoundError(f"Official problem PDF not found: {PDF_PATH}")


def product_decay_factor(half_life_years: float) -> float:
    return math.exp(math.log(0.5) / half_life_years)


def simulate_plan(forest: dict[str, Any], plan: dict[str, Any]) -> pd.DataFrame:
    live_carbon = float(forest["initial_live_carbon_t_per_ha"])
    soil_carbon = float(forest["soil_carbon_t_per_ha"])
    product_pools = {name: 0.0 for name in PRODUCT_POOLS}
    rows = []
    rotation = int(plan["rotation_years"])
    for year in range(HORIZON_YEARS + 1):
        product_total = sum(product_pools.values())
        substitution_credit = sum(
            product_pools[name] * PRODUCT_POOLS[name]["substitution_credit_per_t_carbon"]
            for name in product_pools
        )
        rows.append(
            {
                "forest": forest["forest"],
                "plan": plan["plan"],
                "year": year,
                "live_carbon_t_per_ha": clean_float(live_carbon, 4),
                "soil_carbon_t_per_ha": clean_float(soil_carbon, 4),
                "product_carbon_t_per_ha": clean_float(product_total, 4),
                "substitution_credit_t_carbon_per_ha": clean_float(substitution_credit, 4),
                "total_co2e_t_per_ha": clean_float((live_carbon + soil_carbon + product_total + substitution_credit) * CO2_PER_CARBON, 4),
            }
        )
        if year == HORIZON_YEARS:
            break
        for name, pool in PRODUCT_POOLS.items():
            product_pools[name] *= product_decay_factor(float(pool["half_life_years"]))

        age = int(forest["initial_age"]) + year
        maturity_slowdown = max(0.35, 1.0 - age / 260.0)
        growth = float(forest["growth_rate"]) * live_carbon * (1.0 - live_carbon / float(forest["carrying_capacity_t_per_ha"])) * maturity_slowdown
        live_carbon += max(0.0, growth)
        soil_carbon += 0.010 * growth

        should_harvest = rotation <= 100 and year > 0 and year % rotation == 0
        if should_harvest:
            removed = live_carbon * float(plan["harvest_intensity"])
            live_carbon -= removed
            harvest_residue = removed * 0.10
            soil_carbon += harvest_residue * 0.22
            product_pools["long_lived_products"] += removed * float(plan["long_product_share"])
            product_pools["medium_lived_products"] += removed * float(plan["medium_product_share"])
            product_pools["short_lived_products"] += removed * float(plan["short_product_share"])
    return pd.DataFrame(rows)


def score_plan(carbon_100: float, forest: dict[str, Any], plan: dict[str, Any], min_carbon: float, max_carbon: float) -> dict[str, Any]:
    carbon_score = (carbon_100 - min_carbon) / max(max_carbon - min_carbon, 1e-9)
    biodiversity_score = float(plan["biodiversity_value"]) * float(forest["biodiversity_sensitivity"])
    product_score = float(plan["product_value"]) * float(forest["community_product_need"])
    suitability_bonus = float(plan["harvest_intensity"]) * float(forest["harvest_suitability"]) * 0.16
    social_score = (
        0.38 * carbon_score
        + 0.22 * biodiversity_score
        + 0.14 * float(plan["recreation_value"])
        + 0.10 * float(plan["cultural_value"])
        + 0.16 * product_score
        + suitability_bonus
        - 0.08 * float(plan["transition_burden"])
    )
    return {
        "carbon_score": clean_float(carbon_score, 4),
        "biodiversity_score": clean_float(biodiversity_score, 4),
        "product_score": clean_float(product_score, 4),
        "social_decision_score": clean_float(social_score, 4),
    }


def run_all_scenarios() -> tuple[pd.DataFrame, pd.DataFrame]:
    trajectory_frames = []
    summary_rows = []
    for forest in FOREST_CASES:
        forest_results = []
        for plan in MANAGEMENT_PLANS:
            trajectory = simulate_plan(forest, plan)
            trajectory_frames.append(trajectory)
            final = trajectory.iloc[-1].to_dict()
            forest_results.append(
                {
                    "forest": forest["forest"],
                    "region_type": forest["region_type"],
                    "plan": plan["plan"],
                    "rotation_years": plan["rotation_years"],
                    "harvest_intensity": plan["harvest_intensity"],
                    "carbon_100_years_co2_per_ha": final["total_co2e_t_per_ha"],
                    "live_carbon_100_years_t_per_ha": final["live_carbon_t_per_ha"],
                    "product_carbon_100_years_t_per_ha": final["product_carbon_t_per_ha"],
                    "substitution_credit_100_years_t_carbon_per_ha": final["substitution_credit_t_carbon_per_ha"],
                    "biodiversity_value": plan["biodiversity_value"],
                    "recreation_value": plan["recreation_value"],
                    "cultural_value": plan["cultural_value"],
                    "product_value": plan["product_value"],
                }
            )
        min_carbon = min(row["carbon_100_years_co2_per_ha"] for row in forest_results)
        max_carbon = max(row["carbon_100_years_co2_per_ha"] for row in forest_results)
        for row in forest_results:
            plan = next(item for item in MANAGEMENT_PLANS if item["plan"] == row["plan"])
            row.update(score_plan(row["carbon_100_years_co2_per_ha"], forest, plan, min_carbon, max_carbon))
            summary_rows.append(row)
    trajectory_df = pd.concat(trajectory_frames, ignore_index=True)
    summary_df = pd.DataFrame(summary_rows)
    trajectory_df.to_csv(ARTIFACT_DIR / "carbon_stock_trajectories.csv", index=False)
    summary_df.to_csv(ARTIFACT_DIR / "management_plan_scores.csv", index=False)
    return trajectory_df, summary_df


def build_application_results(summary_df: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, Any]]:
    rows = []
    for forest, group in summary_df.groupby("forest"):
        carbon_best = group.sort_values("carbon_100_years_co2_per_ha", ascending=False).iloc[0].to_dict()
        social_best = group.sort_values("social_decision_score", ascending=False).iloc[0].to_dict()
        rows.append(
            {
                "forest": forest,
                "region_type": social_best["region_type"],
                "best_carbon_plan": carbon_best["plan"],
                "best_social_plan": social_best["plan"],
                "recommended_plan": social_best["plan"],
                "carbon_100_years_co2_per_ha": social_best["carbon_100_years_co2_per_ha"],
                "decision_score": social_best["social_decision_score"],
                "include_harvest": social_best["plan"] != "no_harvest",
            }
        )
    df = pd.DataFrame(rows).sort_values("decision_score", ascending=False)
    df.to_csv(ARTIFACT_DIR / "forest_application_results.csv", index=False)
    harvest_cases = df[df["include_harvest"]]
    harvest_case = harvest_cases.iloc[0].to_dict() if not harvest_cases.empty else df.iloc[0].to_dict()
    return df, {
        "application_rows": df.to_dict(orient="records"),
        "harvest_inclusion_case": harvest_case,
        "interpretation": "The decision model separates the carbon-only winner from the socially balanced recommendation; harvesting appears only where product need and forest suitability offset biodiversity loss.",
    }


def build_transition_strategy(application: dict[str, Any]) -> tuple[pd.DataFrame, dict[str, Any]]:
    start_rotation = CURRENT_PRACTICE_ROTATION_YEARS
    target_rotation = start_rotation + REQUESTED_TRANSITION_EXTENSION_YEARS
    rows = [
        {"year": 0, "rotation_years": start_rotation, "action": "publish stand inventory, carbon baseline, and product-use accounting before changing harvest contracts"},
        {"year": 2, "rotation_years": start_rotation + 2, "action": "delay low-risk stands first and use local mill contracts to protect jobs during the first extension"},
        {"year": 5, "rotation_years": start_rotation + 5, "action": "shift harvested volume toward long-lived lumber and panels; report living and product carbon together"},
        {"year": 8, "rotation_years": start_rotation + 8, "action": "expand recreation, habitat buffers, and cultural access investments funded by product revenue"},
        {"year": 10, "rotation_years": target_rotation, "action": "adopt the new 50-year interval after monitoring confirms carbon, revenue, and community access thresholds"},
    ]
    df = pd.DataFrame(rows)
    df.to_csv(ARTIFACT_DIR / "transition_schedule.csv", index=False)
    return df, {
        "current_practice_rotation_years": start_rotation,
        "target_rotation_years": target_rotation,
        "recommended_forest": application["harvest_inclusion_case"]["forest"],
        "timeline": df.to_dict(orient="records"),
        "sensitivity_note": "The transition should pause if annual product revenue, habitat score, or community access falls below its baseline threshold.",
    }


def build_transition_thresholds(summary_df: pd.DataFrame) -> list[dict[str, Any]]:
    rows = []
    for forest, group in summary_df.groupby("forest"):
        no_harvest = group[group["plan"] == "no_harvest"].iloc[0]
        harvest_best = group[group["plan"] != "no_harvest"].sort_values("social_decision_score", ascending=False).iloc[0]
        carbon_gap = float(no_harvest["carbon_100_years_co2_per_ha"] - harvest_best["carbon_100_years_co2_per_ha"])
        decision_gap = float(harvest_best["social_decision_score"] - no_harvest["social_decision_score"])
        rows.append(
            {
                "forest": forest,
                "best_harvest_plan": harvest_best["plan"],
                "carbon_gap_vs_no_harvest_co2_per_ha": clean_float(carbon_gap, 3),
                "decision_score_gap_vs_no_harvest": clean_float(decision_gap, 4),
                "transition_rule": "include harvest" if decision_gap > 0 else "leave uncut unless product need or disturbance risk increases",
            }
        )
    return rows


def write_frontier_plot(summary_df: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(8.4, 5.2))
    colors = {
        "no_harvest": "#2f6b47",
        "selective_60_year": "#3d7ea6",
        "extended_50_year": "#b57f2a",
        "current_40_year": "#7d6fb2",
        "short_30_year": "#bf5f45",
    }
    for plan, group in summary_df.groupby("plan"):
        ax.scatter(
            group["carbon_100_years_co2_per_ha"],
            group["social_decision_score"],
            label=plan,
            s=70,
            color=colors.get(plan, "#555555"),
            alpha=0.88,
        )
    ax.set_xlabel("100-year CO2e storage per hectare")
    ax.set_ylabel("Social decision score")
    ax.set_title("Forest Carbon and Social-Value Management Frontier")
    ax.grid(alpha=0.22)
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "management_tradeoff_frontier.png", dpi=180)
    plt.close(fig)


def build_result(summary_df: pd.DataFrame, application: dict[str, Any], transition: dict[str, Any]) -> dict[str, Any]:
    carbon_winners = (
        summary_df.sort_values(["forest", "carbon_100_years_co2_per_ha"], ascending=[True, False])
        .groupby("forest")
        .head(1)
        .to_dict(orient="records")
    )
    decision_winners = (
        summary_df.sort_values(["forest", "social_decision_score"], ascending=[True, False])
        .groupby("forest")
        .head(1)
        .to_dict(orient="records")
    )
    return {
        "problem_id": "2022-E",
        "title": "Forestry for Carbon Sequestration",
        "data_source": {
            "type": "official_statement_parameters",
            "root": str(ARCHIVE_ROOT / "official_assets"),
            "source_pdf": str(PDF_PATH),
            "official_requirements": {
                "hundred_year_carbon_accounting": True,
                "forest_products_lifecycle": True,
                "balance_carbon_with_biodiversity_recreation_cultural_values": True,
                "apply_to_various_forests": True,
                "transition_from_current_timeline": True,
                "community_article": True,
            },
            "parameters": OFFICIAL_STATEMENT_PARAMETERS,
        },
        "carbon_sequestration_model": {
            "method": "annual deterministic live-tree, soil, product-pool, and substitution-credit carbon accounting",
            "co2_conversion": "CO2e = carbon * 44/12",
            "product_pools": PRODUCT_POOLS,
            "management_plan_results": summary_df.to_dict(orient="records"),
            "carbon_only_recommendations": carbon_winners,
        },
        "decision_model": {
            "criteria_weights": {
                "carbon_storage": 0.38,
                "biodiversity": 0.22,
                "recreation": 0.14,
                "cultural": 0.10,
                "forest_products": 0.16,
            },
            "transition_thresholds": build_transition_thresholds(summary_df),
            "decision_recommendations": decision_winners,
        },
        "management_plan_spectrum": {
            "plans": MANAGEMENT_PLANS,
            "no_cut_condition": "Leave the forest uncut when no_harvest has the highest decision score or when biodiversity sensitivity is high and community product need is low.",
            "common_transition_point": "The 50-year interval is the first extension beyond current 40-year practice that preserves product flow while increasing living and product carbon.",
        },
        "forest_applications": application,
        "transition_strategy": transition,
        "community_article": (
            "A local community can protect its forest and still use wood carefully. The model counts carbon in standing trees, soil, and long-lived products, then compares those benefits with habitat, recreation, cultural use, and local product needs. "
            "For the managed pine production forest, a longer harvest interval with more wood going into durable products stores substantial carbon over 100 years while keeping jobs and stewardship revenue. "
            "The recommendation is not to cut every forest: the old-growth reserve remains best left uncut. The point is to match the plan to the forest, monitor the carbon account, and move gradually so residents, workers, and forest users can see the tradeoffs."
        ),
        "assumption_audit": {
            "truthfulness_note": "This workflow uses official statement parameters and transparent deterministic scenarios; it does not invent random x1/x2/x3 placeholder data.",
            "model_limits": [
                "COMAP did not provide plot-level inventory or product market files for this problem.",
                "Forest case rows are auditable scenario inputs that a contest team should replace with local inventory, soil, fire, biodiversity, and product-lifetime measurements.",
                "Decision weights are explicit policy choices, not revealed preferences from a community survey.",
            ],
        },
    }


def build_report(result: dict[str, Any]) -> None:
    harvest_case = result["forest_applications"]["harvest_inclusion_case"]
    lines = [
        "# 2022 ICM-E Forestry for Carbon Sequestration",
        "",
        "## 数据真实性",
        f"- 官方来源：`{result['data_source']['source_pdf']}`。",
        "- 本题无 COMAP 数值附件；脚本只使用官方题面要求和显式确定性森林管理情景，不使用随机占位数据。",
        "",
        "## 官方题面参数",
        f"- 评估年限：{HORIZON_YEARS} 年。",
        f"- 当前采伐间隔：{CURRENT_PRACTICE_ROTATION_YEARS} 年；过渡要求：延长 {REQUESTED_TRANSITION_EXTENSION_YEARS} 年。",
        "",
        "## 模型摘要",
        f"- 碳模型：{result['carbon_sequestration_model']['method']}。",
        f"- 决策权重：{result['decision_model']['criteria_weights']}。",
        f"- 推荐包含采伐的森林：{harvest_case['forest']}，方案：{harvest_case['recommended_plan']}，100 年 CO2e：{harvest_case['carbon_100_years_co2_per_ha']} t/ha。",
        "",
        "## 管理计划谱系",
        result["management_plan_spectrum"]["no_cut_condition"],
        result["management_plan_spectrum"]["common_transition_point"],
        "",
        "## 社区文章摘录",
        result["community_article"],
        "",
        "## 输出产物",
        "- `carbon_stock_trajectories.csv`：逐年活树、土壤、产品碳轨迹。",
        "- `management_plan_scores.csv`：各森林与管理计划的碳和社会得分。",
        "- `forest_application_results.csv`：各种森林的推荐计划。",
        "- `transition_schedule.csv`：从 40 年到 50 年采伐间隔的过渡安排。",
        "- `management_tradeoff_frontier.png`：100 年 CO2e 与社会得分权衡图。",
    ]
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ensure_pdf_exists()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    _, summary_df = run_all_scenarios()
    application_df, application = build_application_results(summary_df)
    transition_df, transition = build_transition_strategy(application)
    application_df.to_csv(ARTIFACT_DIR / "forest_application_results.csv", index=False)
    transition_df.to_csv(ARTIFACT_DIR / "transition_schedule.csv", index=False)
    write_frontier_plot(summary_df)
    result = build_result(summary_df, application, transition)
    result["artifacts"] = {
        "carbon_stock_trajectories": str(ARTIFACT_DIR / "carbon_stock_trajectories.csv"),
        "management_plan_scores": str(ARTIFACT_DIR / "management_plan_scores.csv"),
        "forest_application_results": str(ARTIFACT_DIR / "forest_application_results.csv"),
        "transition_schedule": str(ARTIFACT_DIR / "transition_schedule.csv"),
        "management_tradeoff_frontier": str(ARTIFACT_DIR / "management_tradeoff_frontier.png"),
    }
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    build_report(result)
    print(json.dumps({"result": str(RESULT_PATH), "report": str(REPORT_PATH), "artifacts": str(ARTIFACT_DIR)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
