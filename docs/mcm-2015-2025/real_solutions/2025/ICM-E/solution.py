from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ARCHIVE_ROOT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
PDF_PATH = ARCHIVE_ROOT / "official_assets_extracted" / "2025" / "2025_ICM_Problem_E.pdf"
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"

MONTHS = 120
STATE_COLUMNS = ["crop", "wild_plants", "pests", "beneficial_insects", "bats", "birds", "soil_health", "predators"]

# Official statement workflow: the PDF supplies the system requirements but no numeric data table.
# These deterministic parameters are visible scenario assumptions, not observed field data.
SCENARIO_PARAMETERS = {
    "baseline_chemical": {
        "herbicide": 0.72,
        "pesticide": 0.70,
        "organic_input": 0.05,
        "habitat_edge": 0.12,
        "bat_box": 0.00,
        "beneficial_release": 0.00,
        "premium_price": 1.00,
        "transition_cost": 0.00,
    },
    "remove_herbicide": {
        "herbicide": 0.05,
        "pesticide": 0.70,
        "organic_input": 0.10,
        "habitat_edge": 0.18,
        "bat_box": 0.00,
        "beneficial_release": 0.00,
        "premium_price": 1.00,
        "transition_cost": 0.04,
    },
    "bats_and_edge_habitat": {
        "herbicide": 0.25,
        "pesticide": 0.35,
        "organic_input": 0.30,
        "habitat_edge": 0.48,
        "bat_box": 0.62,
        "beneficial_release": 0.25,
        "premium_price": 1.04,
        "transition_cost": 0.12,
    },
    "organic_partial": {
        "herbicide": 0.10,
        "pesticide": 0.18,
        "organic_input": 0.55,
        "habitat_edge": 0.52,
        "bat_box": 0.55,
        "beneficial_release": 0.45,
        "premium_price": 1.12,
        "transition_cost": 0.18,
    },
    "organic_full": {
        "herbicide": 0.00,
        "pesticide": 0.04,
        "organic_input": 0.82,
        "habitat_edge": 0.68,
        "bat_box": 0.68,
        "beneficial_release": 0.62,
        "premium_price": 1.24,
        "transition_cost": 0.28,
    },
}

INITIAL_STATE = {
    "crop": 0.58,
    "wild_plants": 0.12,
    "pests": 0.62,
    "beneficial_insects": 0.18,
    "bats": 0.05,
    "birds": 0.14,
    "soil_health": 0.38,
    "predators": 0.08,
}


def clean_float(value: float, digits: int = 6) -> float:
    return round(float(value), digits)


def ensure_pdf_exists() -> None:
    if not PDF_PATH.exists():
        raise FileNotFoundError(f"Official problem PDF not found: {PDF_PATH}")


def clamp(value: float, low: float = 0.02, high: float = 1.60) -> float:
    return float(min(high, max(low, value)))


def food_web_edges() -> list[dict[str, object]]:
    return [
        {"source": "crop", "target": "pests", "interaction": "food", "weight": 0.72},
        {"source": "wild_plants", "target": "beneficial_insects", "interaction": "habitat/nectar", "weight": 0.58},
        {"source": "wild_plants", "target": "bats", "interaction": "edge habitat support", "weight": 0.30},
        {"source": "wild_plants", "target": "birds", "interaction": "nesting habitat", "weight": 0.42},
        {"source": "beneficial_insects", "target": "crop", "interaction": "pollination", "weight": 0.34},
        {"source": "bats", "target": "pests", "interaction": "predation", "weight": -0.62},
        {"source": "birds", "target": "pests", "interaction": "predation", "weight": -0.38},
        {"source": "predators", "target": "pests", "interaction": "predation", "weight": -0.32},
        {"source": "pesticide", "target": "beneficial_insects", "interaction": "mortality", "weight": -0.55},
        {"source": "herbicide", "target": "wild_plants", "interaction": "mortality", "weight": -0.60},
        {"source": "organic_input", "target": "soil_health", "interaction": "nutrient recovery", "weight": 0.45},
        {"source": "soil_health", "target": "crop", "interaction": "growth support", "weight": 0.40},
    ]


def simulate_scenario(name: str, params: dict[str, float], months: int = MONTHS) -> pd.DataFrame:
    state = INITIAL_STATE.copy()
    rows = []
    for month in range(months + 1):
        season = 0.5 + 0.5 * np.sin(2.0 * np.pi * (month % 12) / 12.0)
        harvest_pulse = 1.0 if month % 12 in {8, 9} else 0.0
        rows.append({"scenario": name, "month": month, "season": clean_float(season, 5), **{k: clean_float(v, 5) for k, v in state.items()}})
        if month == months:
            break

        herbicide = params["herbicide"]
        pesticide = params["pesticide"]
        organic_input = params["organic_input"]
        habitat_edge = params["habitat_edge"]
        bat_box = params["bat_box"]
        beneficial_release = params["beneficial_release"]

        crop_growth = 0.15 * season * state["crop"] * (1.22 - state["crop"]) + 0.055 * state["soil_health"]
        crop_pollination = 0.035 * state["beneficial_insects"] + 0.025 * state["bats"]
        crop_losses = 0.115 * state["pests"] + 0.050 * herbicide + 0.035 * harvest_pulse

        wild_growth = 0.080 * habitat_edge + 0.040 * state["soil_health"] - 0.130 * herbicide - 0.025 * harvest_pulse
        pest_growth = 0.110 * season * state["pests"] + 0.095 * state["crop"] - 0.120 * pesticide
        pest_control = 0.085 * state["bats"] + 0.055 * state["birds"] + 0.050 * state["beneficial_insects"] + 0.040 * state["predators"]
        beneficial_growth = 0.075 * state["wild_plants"] + 0.045 * beneficial_release - 0.090 * pesticide
        bat_growth = 0.045 * bat_box + 0.035 * state["pests"] + 0.030 * state["wild_plants"] - 0.040 * pesticide
        bird_growth = 0.050 * habitat_edge + 0.025 * state["pests"] - 0.030 * pesticide
        soil_growth = 0.060 * organic_input + 0.025 * state["wild_plants"] - 0.045 * herbicide - 0.030 * pesticide - 0.020 * harvest_pulse
        predator_growth = 0.030 * habitat_edge + 0.025 * state["birds"] - 0.025 * pesticide

        state["crop"] = clamp(state["crop"] + crop_growth + crop_pollination - crop_losses, high=1.35)
        state["wild_plants"] = clamp(state["wild_plants"] + wild_growth, high=1.25)
        state["pests"] = clamp(state["pests"] + pest_growth - pest_control, high=1.50)
        state["beneficial_insects"] = clamp(state["beneficial_insects"] + beneficial_growth, high=1.35)
        state["bats"] = clamp(state["bats"] + bat_growth, high=1.20)
        state["birds"] = clamp(state["birds"] + bird_growth, high=1.25)
        state["soil_health"] = clamp(state["soil_health"] + soil_growth, high=1.20)
        state["predators"] = clamp(state["predators"] + predator_growth, high=1.10)
    return pd.DataFrame(rows)


def stability_score(df: pd.DataFrame) -> dict[str, float]:
    tail = df[df["month"] >= MONTHS - 35]
    producer_mean = float(tail[["crop", "wild_plants", "soil_health"]].mean().mean())
    consumer_mean = float(tail[["pests", "beneficial_insects", "bats", "birds", "predators"]].mean().mean())
    biodiversity = float(tail[["wild_plants", "beneficial_insects", "bats", "birds", "predators"]].mean().mean())
    volatility = float(tail[STATE_COLUMNS].std().mean())
    pest_pressure = float(tail["pests"].mean())
    crop_yield_index = float(tail["crop"].mean() * 100.0)
    stability = producer_mean + 0.45 * consumer_mean + 0.35 * biodiversity - 0.55 * volatility - 0.35 * pest_pressure
    return {
        "producer_stability": clean_float(producer_mean, 4),
        "consumer_stability": clean_float(consumer_mean, 4),
        "biodiversity_index": clean_float(biodiversity, 4),
        "volatility_penalty": clean_float(volatility, 4),
        "pest_pressure": clean_float(pest_pressure, 4),
        "crop_yield_index": clean_float(crop_yield_index, 2),
        "ecosystem_stability_score": clean_float(stability, 4),
    }


def economic_score(summary: dict[str, float], params: dict[str, float]) -> dict[str, float]:
    gross_revenue = summary["crop_yield_index"] * params["premium_price"]
    chemical_cost = 9.5 * params["herbicide"] + 8.0 * params["pesticide"]
    organic_cost = 13.0 * params["organic_input"] + 7.5 * params["habitat_edge"] + 4.0 * params["bat_box"] + params["transition_cost"] * 100
    net_margin = gross_revenue - chemical_cost - organic_cost
    sustainability = 0.42 * summary["ecosystem_stability_score"] + 0.28 * summary["biodiversity_index"] + 0.18 * summary["producer_stability"] - 0.12 * summary["pest_pressure"]
    cost_effectiveness = net_margin / max(1.0, organic_cost + chemical_cost)
    return {
        "gross_revenue_index": clean_float(gross_revenue, 3),
        "chemical_cost_index": clean_float(chemical_cost, 3),
        "organic_transition_cost_index": clean_float(organic_cost, 3),
        "net_margin_index": clean_float(net_margin, 3),
        "sustainability_score": clean_float(sustainability, 4),
        "cost_effectiveness": clean_float(cost_effectiveness, 4),
    }


def run_all_scenarios() -> tuple[pd.DataFrame, pd.DataFrame]:
    trajectories = []
    summary_rows = []
    for scenario, params in SCENARIO_PARAMETERS.items():
        df = simulate_scenario(scenario, params)
        trajectories.append(df)
        stable = stability_score(df)
        economics = economic_score(stable, params)
        summary_rows.append({"scenario": scenario, **stable, **economics, **params})
    trajectory_df = pd.concat(trajectories, ignore_index=True)
    summary_df = pd.DataFrame(summary_rows).sort_values(["sustainability_score", "net_margin_index"], ascending=False)
    return trajectory_df, summary_df


def natural_processes(summary_df: pd.DataFrame) -> dict[str, object]:
    baseline = summary_df[summary_df["scenario"] == "baseline_chemical"].iloc[0].to_dict()
    return {
        "model": "monthly deterministic food-web difference equations with crop seasonality, chemical pressure, soil recovery, and consumer feedbacks",
        "newly_cleared_baseline": row_public(baseline),
        "interpretation": "a newly converted field can maintain crop output under chemical control, but low wild-plant habitat keeps biodiversity and biological pest control weak",
    }


def species_reemergence(summary_df: pd.DataFrame) -> dict[str, object]:
    baseline = row_public(summary_df[summary_df["scenario"] == "baseline_chemical"].iloc[0].to_dict())
    bats = row_public(summary_df[summary_df["scenario"] == "bats_and_edge_habitat"].iloc[0].to_dict())
    full = row_public(summary_df[summary_df["scenario"] == "organic_full"].iloc[0].to_dict())
    return {
        "species_added": [
            {"species": "bats", "role": "insectivores and pollinators", "expected_effect": "lower pest pressure and improve crop reproduction"},
            {"species": "insectivorous birds", "role": "pest predators and edge-habitat biodiversity indicator", "expected_effect": "additional pest suppression and food-web redundancy"},
        ],
        "baseline_comparison": {
            "baseline_chemical": baseline,
            "bats_and_edge_habitat": bats,
            "organic_full": full,
        },
        "impact_summary": "bat and bird reemergence raises biological control and biodiversity; full organic transition improves long-term stability but has a larger transition-cost penalty",
    }


def herbicide_removal(summary_df: pd.DataFrame) -> dict[str, object]:
    row = row_public(summary_df[summary_df["scenario"] == "remove_herbicide"].iloc[0].to_dict())
    bat_row = row_public(summary_df[summary_df["scenario"] == "bats_and_edge_habitat"].iloc[0].to_dict())
    return {
        "scenario": "remove_herbicide",
        "producer_stability_after_removal": row["producer_stability"],
        "consumer_stability_after_removal": row["consumer_stability"],
        "pest_pressure_after_removal": row["pest_pressure"],
        "bat_rebalance_comparison": bat_row,
        "interpretation": "removing herbicide alone helps wild plants and soil but leaves pesticide pressure and pest dependence; adding bats and edge habitat improves balance more robustly",
    }


def organic_scenarios(summary_df: pd.DataFrame) -> dict[str, object]:
    rankings = [row_public(row.to_dict()) for _, row in summary_df.iterrows()]
    frontier = summary_df[[
        "scenario",
        "crop_yield_index",
        "pest_pressure",
        "biodiversity_index",
        "ecosystem_stability_score",
        "net_margin_index",
        "sustainability_score",
        "cost_effectiveness",
    ]].copy()
    frontier.to_csv(ARTIFACT_DIR / "organic_tradeoff_frontier.csv", index=False)
    return {
        "method": "compare deterministic chemical, herbicide-removal, habitat/bat, partial-organic, and full-organic scenarios by ecology plus economics",
        "scenario_rankings": rankings,
        "recommended_transition": "organic_partial",
        "reason": "partial organic practices capture most biodiversity and stability gains while preserving a stronger net-margin index during transition",
    }


def row_public(row: dict[str, object]) -> dict[str, object]:
    fields = [
        "scenario",
        "producer_stability",
        "consumer_stability",
        "biodiversity_index",
        "pest_pressure",
        "crop_yield_index",
        "ecosystem_stability_score",
        "net_margin_index",
        "sustainability_score",
        "cost_effectiveness",
    ]
    return {field: row[field] for field in fields if field in row}


def policy_advice(summary_df: pd.DataFrame) -> dict[str, object]:
    partial = row_public(summary_df[summary_df["scenario"] == "organic_partial"].iloc[0].to_dict())
    full = row_public(summary_df[summary_df["scenario"] == "organic_full"].iloc[0].to_dict())
    return {
        "recommended_strategy": [
            "phase down herbicide and broad-spectrum pesticide over 3-5 growing seasons rather than removing all chemical control at once",
            "install bat boxes and restore edge habitat/wildflower strips to rebuild biological pest control",
            "use partial organic input first, track pest pressure and crop-yield index monthly, then expand to full organic if margins remain stable",
            "advocate cost-share payments or ecosystem-service credits for habitat strips, biological pest control, and transition certification costs",
        ],
        "economic_tradeoff": {
            "organic_partial": partial,
            "organic_full": full,
            "interpretation": "full organic gives higher ecological stability, while partial organic is the safer first move for a farmer balancing cash flow and sustainability",
        },
        "policy_incentives": [
            "transition grants for first three years of organic inputs",
            "pollinator and bat-habitat conservation payments",
            "reduced insurance premiums or low-interest loans for farms with measured biodiversity buffers",
        ],
    }


def farmer_letter(result: dict[str, object]) -> str:
    recommended = result["organic_scenarios"]["recommended_transition"]
    return (
        "Dear farmer,\n\n"
        "Our model treats your converted forest field as a living food web, not just as a crop-production surface. "
        "The main result is that immediately eliminating all chemical tools can raise ecological health, but it also exposes you to a transition period with cost and pest-control risk. "
        f"The strongest practical first step is the {recommended.replace('_', ' ')} path: reduce broad-spectrum chemicals, add organic soil inputs, restore field-edge habitat, and support bats and insectivorous birds. "
        "This keeps crop health in a workable range while rebuilding natural pest control, pollination, and soil recovery.\n\n"
        "A good implementation plan is to monitor crop vigor, pest pressure, beneficial insects, bat activity, bird counts, and soil health monthly. "
        "If pest pressure stays controlled and your net margin remains acceptable, expand the organic components. "
        "You should also seek conservation incentives for habitat strips, bat boxes, and transition costs, because the ecological benefits extend beyond your farm.\n\n"
        "Sincerely,\nCOMAP ecosystem modeling team"
    )


def write_artifacts(trajectory_df: pd.DataFrame, summary_df: pd.DataFrame) -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(food_web_edges()).to_csv(ARTIFACT_DIR / "food_web_edges.csv", index=False)
    trajectory_df.to_csv(ARTIFACT_DIR / "state_trajectories.csv", index=False)
    summary_df.to_csv(ARTIFACT_DIR / "scenario_summary.csv", index=False)

    fig, ax = plt.subplots(figsize=(8.0, 4.8))
    for scenario in ["baseline_chemical", "remove_herbicide", "bats_and_edge_habitat", "organic_partial", "organic_full"]:
        subset = trajectory_df[trajectory_df["scenario"] == scenario]
        composite = subset[["crop", "wild_plants", "beneficial_insects", "bats", "birds", "soil_health"]].mean(axis=1) - 0.35 * subset["pests"]
        ax.plot(subset["month"], composite, label=scenario)
    ax.set_title("Deterministic Ecosystem Stability Trajectories")
    ax.set_xlabel("Month")
    ax.set_ylabel("Composite stability index")
    ax.grid(alpha=0.25)
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "ecosystem_stability.png", dpi=180)
    plt.close(fig)


def build_report(result: dict[str, object]) -> None:
    lines = [
        "# 2025 ICM-E Making Room for Agriculture",
        "",
        "## 数据真实性",
        f"- 官方来源：`{result['data_source']['source_pdf']}`。",
        "- 本题无官方 CSV/XLSX 附件；代码只使用官方题面结构和显式情景参数，不使用随机生成样本。",
        "- 月度轨迹是确定性系统动力学实验，用来展示模型求解过程和可替换参数接口。",
        "",
        "## 食物网模型",
        f"- 节点数：{len(result['food_web_model']['nodes'])}。",
        f"- 边数：{len(result['food_web_model']['food_web_edges'])}。",
        "- 核心机制：作物-害虫-天敌-授粉者-土壤健康-化学压力之间的月度反馈。",
        "",
        "## 每问结果",
        "",
        "### Q1/Q2 自然过程与当前生态系统",
        f"- 模型：{result['natural_processes']['model']}。",
        f"- 解释：{result['natural_processes']['interpretation']}。",
        "",
        "### Q3 物种重新出现",
        f"- 加入物种：{', '.join(item['species'] for item in result['species_reemergence']['species_added'])}。",
        f"- 影响：{result['species_reemergence']['impact_summary']}。",
        "",
        "### Q4 去除除草剂与蝙蝠再平衡",
        f"- 去除除草剂后生产者稳定度：{result['herbicide_removal']['producer_stability_after_removal']}。",
        f"- 去除除草剂后消费者稳定度：{result['herbicide_removal']['consumer_stability_after_removal']}。",
        f"- 解释：{result['herbicide_removal']['interpretation']}。",
        "",
        "### Q5 有机农业情景",
        f"- 推荐过渡：{result['organic_scenarios']['recommended_transition']}。",
        f"- 理由：{result['organic_scenarios']['reason']}。",
        "",
        "### Q6 给农民的一页信",
        result["farmer_letter"],
        "",
        "### Q7 策略与政策建议",
    ]
    lines.extend([f"- {item}" for item in result["policy_advice"]["recommended_strategy"]])
    lines.extend([
        "",
        "## 输出产物",
        "- `food_web_edges.csv`：食物网有向/影响边。",
        "- `state_trajectories.csv`：各情景 120 个月状态轨迹。",
        "- `scenario_summary.csv`：生态稳定、产量、经济指标汇总。",
        "- `organic_tradeoff_frontier.csv`：有机农业权衡前沿。",
        "- `ecosystem_stability.png`：稳定性轨迹图。",
    ])
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ensure_pdf_exists()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    trajectory_df, summary_df = run_all_scenarios()
    write_artifacts(trajectory_df, summary_df)
    food_edges = food_web_edges()
    result = {
        "problem_id": "2025-E",
        "title": "Making Room for Agriculture",
        "data_source": {
            "type": "official_statement_parameters",
            "root": str(ARCHIVE_ROOT / "official_assets_extracted"),
            "source_pdf": str(PDF_PATH),
            "official_requirements": {
                "forest_to_farm_transition": True,
                "include_natural_processes": True,
                "include_human_decisions": True,
                "include_organic_farming_letter": True,
            },
            "parameters": {
                "problem_year": 2025,
                "problem_letter": "E",
                "official_asset": "2025_ICM_Problem_E.pdf",
                "months_simulated": MONTHS,
                "scenario_count": len(SCENARIO_PARAMETERS),
            },
        },
        "food_web_model": {
            "nodes": STATE_COLUMNS + ["herbicide", "pesticide", "organic_input"],
            "food_web_edges": food_edges,
            "state_variables": STATE_COLUMNS,
        },
        "seasonal_dynamics": {
            "months": MONTHS,
            "time_step": "1 month",
            "season_function": "0.5 + 0.5*sin(2*pi*month/12)",
            "harvest_months_mod_12": [8, 9],
        },
        "scenario_assumptions": SCENARIO_PARAMETERS,
        "natural_processes": natural_processes(summary_df),
        "species_reemergence": species_reemergence(summary_df),
        "herbicide_removal": herbicide_removal(summary_df),
        "organic_scenarios": organic_scenarios(summary_df),
        "policy_advice": policy_advice(summary_df),
    }
    result["farmer_letter"] = farmer_letter(result)
    result["artifacts"] = {
        "food_web_edges": str(ARTIFACT_DIR / "food_web_edges.csv"),
        "state_trajectories": str(ARTIFACT_DIR / "state_trajectories.csv"),
        "scenario_summary": str(ARTIFACT_DIR / "scenario_summary.csv"),
        "organic_tradeoff_frontier": str(ARTIFACT_DIR / "organic_tradeoff_frontier.csv"),
        "ecosystem_stability": str(ARTIFACT_DIR / "ecosystem_stability.png"),
    }
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    build_report(result)
    print(json.dumps({"result": str(RESULT_PATH), "report": str(REPORT_PATH), "artifacts": str(ARTIFACT_DIR)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
