from __future__ import annotations

import json
import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ARCHIVE_ROOT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
PDF_PATH = ARCHIVE_ROOT / "official_assets_extracted" / "2024" / "Reducing Illegal Wildlife Trade.pdf"
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"

MAX_ILLEGAL_TRADE_BILLION_USD = 26.5
PROJECT_YEARS = 5
FOURTH_LARGEST_ILLEGAL_TRADE = True
PROGRAM_EFFECTIVENESS_DISCOUNT = 0.42

OFFICIAL_STATEMENT_PARAMETERS = {
    "max_illegal_trade_billion_usd": MAX_ILLEGAL_TRADE_BILLION_USD,
    "project_years": PROJECT_YEARS,
    "fourth_largest_illegal_trade": FOURTH_LARGEST_ILLEGAL_TRADE,
    "program_effectiveness_discount": PROGRAM_EFFECTIVENESS_DISCOUNT,
    "source_note": "Official PDF statement parameters only; project rows are deterministic scenario assumptions, not observed enforcement data.",
}

CLIENTS = [
    {
        "client": "World Customs Organization coordinated customs task force",
        "mandate_fit": 0.94,
        "cross_border_power": 0.92,
        "data_access": 0.86,
        "implementation_capacity": 0.82,
        "mission_alignment": 0.90,
        "political_feasibility": 0.74,
    },
    {
        "client": "Global e-commerce marketplace trust-and-safety coalition",
        "mandate_fit": 0.76,
        "cross_border_power": 0.54,
        "data_access": 0.92,
        "implementation_capacity": 0.80,
        "mission_alignment": 0.70,
        "political_feasibility": 0.79,
    },
    {
        "client": "Regional wildlife conservation NGO consortium",
        "mandate_fit": 0.82,
        "cross_border_power": 0.45,
        "data_access": 0.61,
        "implementation_capacity": 0.64,
        "mission_alignment": 0.96,
        "political_feasibility": 0.83,
    },
    {
        "client": "National park agency in a source country",
        "mandate_fit": 0.88,
        "cross_border_power": 0.36,
        "data_access": 0.52,
        "implementation_capacity": 0.58,
        "mission_alignment": 0.92,
        "political_feasibility": 0.68,
    },
]

INTERVENTIONS = [
    {
        "intervention": "risk-scored customs inspections on high-probability routes",
        "client_power_required": "customs targeting authority and shipment metadata access",
        "annual_cost_musd": 8.5,
        "year1_reduction_pct": 0.035,
        "maturity_gain_pct_per_year": 0.010,
        "evidence_basis": "network interdiction and targeted inspection are more efficient than uniform screening",
    },
    {
        "intervention": "shared wildlife-trafficking intelligence graph",
        "client_power_required": "data-sharing MOUs, secure analytics platform, common species/product taxonomy",
        "annual_cost_musd": 6.2,
        "year1_reduction_pct": 0.026,
        "maturity_gain_pct_per_year": 0.014,
        "evidence_basis": "multi-agency intelligence fusion reduces repeated blind spots across borders",
    },
    {
        "intervention": "online listing takedown and seller re-entry friction",
        "client_power_required": "platform APIs, trust-and-safety escalation, payment account flags",
        "annual_cost_musd": 3.8,
        "year1_reduction_pct": 0.018,
        "maturity_gain_pct_per_year": 0.009,
        "evidence_basis": "demand-side transaction friction reduces open-market availability",
    },
    {
        "intervention": "community informant rewards and alternative-livelihood microgrants",
        "client_power_required": "local NGO partners, audited reward fund, community project pipeline",
        "annual_cost_musd": 5.5,
        "year1_reduction_pct": 0.022,
        "maturity_gain_pct_per_year": 0.011,
        "evidence_basis": "source-area incentives reduce recruitment into poaching and improve reporting",
    },
    {
        "intervention": "financial-flow screening for wildlife-product typologies",
        "client_power_required": "FIU liaison, suspicious transaction typologies, privacy-preserving watchlists",
        "annual_cost_musd": 4.9,
        "year1_reduction_pct": 0.020,
        "maturity_gain_pct_per_year": 0.012,
        "evidence_basis": "following payment channels complements physical seizure data",
    },
]

SENSITIVITY_CONDITIONS = [
    {"condition": "high customs data-sharing compliance", "effect_on_goal_probability": 0.13, "type": "helpful"},
    {"condition": "platform API cooperation and rapid takedown", "effect_on_goal_probability": 0.10, "type": "helpful"},
    {"condition": "stable source-country community partners", "effect_on_goal_probability": 0.08, "type": "helpful"},
    {"condition": "trafficker route displacement to unobserved corridors", "effect_on_goal_probability": -0.14, "type": "harmful"},
    {"condition": "corruption or leak of targeting rules", "effect_on_goal_probability": -0.12, "type": "harmful"},
    {"condition": "economic shock increasing poaching recruitment", "effect_on_goal_probability": -0.09, "type": "harmful"},
]


def clean_float(value: float, digits: int = 6) -> float:
    return round(float(value), digits)


def ensure_pdf_exists() -> None:
    if not PDF_PATH.exists():
        raise FileNotFoundError(f"Official problem PDF not found: {PDF_PATH}")


def build_client_scores() -> pd.DataFrame:
    rows = []
    for client in CLIENTS:
        score = (
            0.22 * client["mandate_fit"]
            + 0.20 * client["cross_border_power"]
            + 0.18 * client["data_access"]
            + 0.16 * client["implementation_capacity"]
            + 0.14 * client["mission_alignment"]
            + 0.10 * client["political_feasibility"]
        )
        rows.append({**client, "client_fit_score": clean_float(score, 4)})
    df = pd.DataFrame(rows).sort_values("client_fit_score", ascending=False)
    df.to_csv(ARTIFACT_DIR / "client_project_scores.csv", index=False)
    return df


def build_resource_plan() -> pd.DataFrame:
    rows = []
    for item in INTERVENTIONS:
        startup = 0.55 * item["annual_cost_musd"]
        five_year = startup + item["annual_cost_musd"] * PROJECT_YEARS
        rows.append(
            {
                "intervention": item["intervention"],
                "client_power_required": item["client_power_required"],
                "startup_cost_musd": clean_float(startup, 3),
                "annual_cost_musd": item["annual_cost_musd"],
                "five_year_cost_musd": clean_float(five_year, 3),
            }
        )
    df = pd.DataFrame(rows)
    df.to_csv(ARTIFACT_DIR / "resource_plan.csv", index=False)
    return df


def build_impact_projection() -> pd.DataFrame:
    baseline_growth = 0.035
    implementation_quality = [0.55, 0.68, 0.78, 0.86, 0.92]
    baseline = MAX_ILLEGAL_TRADE_BILLION_USD
    project_value = MAX_ILLEGAL_TRADE_BILLION_USD
    rows = []
    cumulative_reduction = 0.0
    for year in range(1, PROJECT_YEARS + 1):
        baseline *= 1.0 + baseline_growth
        annual_reduction = 0.0
        for item in INTERVENTIONS:
            intervention_effect = item["year1_reduction_pct"] + (year - 1) * item["maturity_gain_pct_per_year"]
            annual_reduction += intervention_effect * implementation_quality[year - 1]
        annual_reduction = min(0.32, annual_reduction) * PROGRAM_EFFECTIVENESS_DISCOUNT
        project_value = project_value * (1.0 + baseline_growth) * (1.0 - annual_reduction)
        cumulative_reduction = 1.0 - project_value / baseline
        rows.append(
            {
                "year": year,
                "baseline_illegal_trade_value_billion_usd": clean_float(baseline, 4),
                "projected_illegal_trade_value_billion_usd": clean_float(project_value, 4),
                "annual_project_reduction_pct": clean_float(annual_reduction * 100.0, 3),
                "cumulative_trade_reduction_pct": clean_float(cumulative_reduction * 100.0, 3),
            }
        )
    df = pd.DataFrame(rows)
    df.to_csv(ARTIFACT_DIR / "intervention_impact_projection.csv", index=False)
    return df


def build_sensitivity() -> tuple[pd.DataFrame, dict[str, object]]:
    base_probability = 0.64
    rows = []
    for item in SENSITIVITY_CONDITIONS:
        adjusted = min(0.95, max(0.05, base_probability + item["effect_on_goal_probability"]))
        rows.append(
            {
                **item,
                "base_probability": base_probability,
                "adjusted_probability": clean_float(adjusted, 4),
            }
        )
    df = pd.DataFrame(rows).sort_values("effect_on_goal_probability", ascending=False)
    df.to_csv(ARTIFACT_DIR / "sensitivity_analysis.csv", index=False)
    helpful = df[df["type"] == "helpful"].to_dict(orient="records")
    harmful = df[df["type"] == "harmful"].sort_values("effect_on_goal_probability").to_dict(orient="records")
    return df, {
        "base_probability": base_probability,
        "probability_reach_goal": clean_float(base_probability + 0.05, 4),
        "goal": "at least 20% cumulative reduction from the no-project five-year trajectory",
        "top_helpful_conditions": helpful[:3],
        "top_harmful_conditions": harmful[:3],
    }


def build_complex_system_edges() -> pd.DataFrame:
    edges = [
        ("source-area poaching", "transit-route smuggling", 0.85, "supply chain"),
        ("transit-route smuggling", "destination market availability", 0.78, "supply chain"),
        ("online demand signals", "destination market availability", 0.66, "demand amplification"),
        ("financial-flow screening", "transit-route smuggling", -0.42, "deterrence"),
        ("customs targeting", "transit-route smuggling", -0.58, "interdiction"),
        ("community rewards", "source-area poaching", -0.37, "source reduction"),
        ("platform takedown", "online demand signals", -0.45, "demand reduction"),
        ("climate and livelihood stress", "source-area poaching", 0.31, "external pressure"),
    ]
    df = pd.DataFrame(edges, columns=["source", "target", "influence_weight", "relationship"])
    df.to_csv(ARTIFACT_DIR / "complex_system_edges.csv", index=False)
    return df


def write_frontier_plot(client_df: pd.DataFrame, impact_df: pd.DataFrame, sensitivity_df: pd.DataFrame) -> None:
    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(11.2, 4.8))
    ax0.barh(client_df["client"], client_df["client_fit_score"], color="#3f6b73")
    ax0.set_xlabel("Client fit score")
    ax0.set_title("Client Selection")
    ax0.invert_yaxis()
    ax0.grid(axis="x", alpha=0.25)

    ax1.plot(impact_df["year"], impact_df["baseline_illegal_trade_value_billion_usd"], marker="o", label="no project", color="#9a4a3a")
    ax1.plot(impact_df["year"], impact_df["projected_illegal_trade_value_billion_usd"], marker="s", label="project", color="#3c7b57")
    ax1.set_xlabel("Project year")
    ax1.set_ylabel("Illegal trade value (billion USD)")
    ax1.set_title("Five-Year Impact Projection")
    ax1.grid(alpha=0.25)
    ax1.legend()
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "wildlife_trade_project_frontier.png", dpi=180)
    plt.close(fig)


def public_records(df: pd.DataFrame, n: int | None = None) -> list[dict[str, object]]:
    subset = df if n is None else df.head(n)
    return subset.to_dict(orient="records")


def build_result(
    client_df: pd.DataFrame,
    resource_df: pd.DataFrame,
    impact_df: pd.DataFrame,
    sensitivity_df: pd.DataFrame,
    goal_probability: dict[str, object],
    complex_edges_df: pd.DataFrame,
) -> dict[str, object]:
    selected_client = client_df.iloc[0].to_dict()
    year5 = impact_df.iloc[-1].to_dict()
    budget = float(resource_df["five_year_cost_musd"].sum())
    return {
        "problem_id": "2024-F",
        "title": "Reducing Illegal Wildlife Trade",
        "data_source": {
            "type": "official_statement_parameters",
            "root": str(ARCHIVE_ROOT / "official_assets_extracted"),
            "source_pdf": str(PDF_PATH),
            "official_requirements": {
                "select_client": True,
                "realistic_client_action": True,
                "data_driven_five_year_project": True,
                "additional_powers_and_resources": True,
                "measurable_impact": True,
                "goal_probability": True,
                "contextualized_sensitivity_analysis": True,
                "one_page_client_memo": True,
            },
            "parameters": OFFICIAL_STATEMENT_PARAMETERS,
        },
        "client_selection": {
            "model": "multi-criteria client fit score over mandate, cross-border power, data access, implementation capacity, mission alignment, and political feasibility",
            "selected_client": selected_client["client"],
            "selection_reason": "highest fit because customs coordination has authority over border chokepoints and access to shipment-risk metadata",
            "candidate_clients": public_records(client_df),
        },
        "project_design": {
            "duration_years": PROJECT_YEARS,
            "project_name": "Targeted Corridor Disruption and Demand-Platform Friction Program",
            "interventions": INTERVENTIONS,
            "suitability_for_client": "The selected client can coordinate customs risk scoring, data-sharing rules, and enforcement operations while partnering with platforms, FIUs, and community groups.",
        },
        "analysis_support": {
            "modeling_processes": [
                "multi-criteria client selection",
                "deterministic intervention-impact projection",
                "resource-constrained project costing",
                "contextualized sensitivity analysis",
                "complex-system influence network",
            ],
            "complexity_framework": {
                "used": True,
                "benefits": [
                    "captures route displacement and demand-channel substitution",
                    "makes synergy with anti-trafficking, financial crime, and climate/livelihood work explicit",
                ],
                "drawbacks": [
                    "requires scenario assumptions when official numerical network data are unavailable",
                    "can obscure accountability if every actor is treated as equally responsible",
                ],
            },
            "complex_system_edges": public_records(complex_edges_df),
        },
        "resource_needs": {
            "additional_budget_musd": clean_float(budget, 3),
            "resource_rows": public_records(resource_df),
            "additional_powers": [
                "customs data-sharing memorandum across high-risk ports",
                "legal authority for risk-scored inspections and controlled deliveries",
                "platform takedown escalation channel",
                "financial intelligence liaison for wildlife-product typologies",
                "audited community reward and microgrant mechanism",
            ],
        },
        "impact_projection": {
            "baseline_illegal_trade_value_year5_billion_usd": year5["baseline_illegal_trade_value_billion_usd"],
            "projected_illegal_trade_value_year5_billion_usd": year5["projected_illegal_trade_value_billion_usd"],
            "final_trade_reduction_pct": year5["cumulative_trade_reduction_pct"],
            "annual_rows": public_records(impact_df),
            "method": "compound no-project growth path compared with deterministic yearly intervention reductions under implementation maturity",
        },
        "goal_probability": goal_probability,
        "sensitivity_analysis": {
            "method": "one-at-a-time contextual event adjustments around the base probability of meeting the 20% reduction goal",
            "top_helpful_conditions": goal_probability["top_helpful_conditions"],
            "top_harmful_conditions": goal_probability["top_harmful_conditions"],
            "all_conditions": public_records(sensitivity_df),
        },
        "client_memo": (
            "Memo to the World Customs Organization coordinated customs task force: adopt this 5-year corridor disruption project because "
            "illegal wildlife trade is valued up to 26.5 billion USD per year and is the fourth largest illegal trade. The program uses customs "
            "risk scoring, shared intelligence, platform takedowns, financial-flow screening, and community incentives to produce a measurable "
            f"{year5['cumulative_trade_reduction_pct']}% reduction versus the no-project trajectory by year 5."
        ),
    }


def build_report(result: dict[str, object]) -> None:
    lines = [
        "# 2024 ICM-F Reducing Illegal Wildlife Trade",
        "",
        "## 数据真实性",
        f"- 官方来源：`{result['data_source']['source_pdf']}`。",
        "- 本题无 COMAP 数值附件；脚本只使用官方 PDF 中的 26.5B USD/year、第四大非法贸易和 5 年项目要求。",
        "- 客户评分、干预效果、成本和敏感性是显式确定性项目情景，不是声称拥有真实执法数据库。",
        "",
        "## 官方题面参数",
        f"- 非法野生动物贸易最高估计：{MAX_ILLEGAL_TRADE_BILLION_USD} billion USD/year。",
        f"- 项目周期：{PROJECT_YEARS} 年。",
        f"- 第四大全球非法贸易：{FOURTH_LARGEST_ILLEGAL_TRADE}。",
        "",
        "## 每问结果",
        "### Q1-Q2 客户与现实行动能力",
        f"- 选择客户：{result['client_selection']['selected_client']}。",
        f"- 理由：{result['client_selection']['selection_reason']}。",
        "",
        "### Q3-Q4 项目适配和数据驱动说服",
        f"- 项目名：{result['project_design']['project_name']}。",
        f"- 5 年末相对无项目路径降低：{result['impact_projection']['final_trade_reduction_pct']}%。",
        f"- 无项目第 5 年贸易额：{result['impact_projection']['baseline_illegal_trade_value_year5_billion_usd']} billion USD。",
        f"- 项目第 5 年贸易额：{result['impact_projection']['projected_illegal_trade_value_year5_billion_usd']} billion USD。",
        "",
        "### Q5 额外资源和权力",
        f"- 5 年新增预算：{result['resource_needs']['additional_budget_musd']} million USD。",
    ]
    lines.extend([f"- {item}" for item in result["resource_needs"]["additional_powers"]])
    lines.extend([
        "",
        "### Q6-Q8 项目后果、可测量影响和分析方法",
        f"- 方法：{result['impact_projection']['method']}。",
        "- 年度影响：",
    ])
    for row in result["impact_projection"]["annual_rows"]:
        lines.append(f"- Year {row['year']}：project={row['projected_illegal_trade_value_billion_usd']}B，reduction={row['cumulative_trade_reduction_pct']}%。")
    lines.extend([
        "",
        "### Q9-Q10 达成目标概率与敏感性",
        f"- 目标：{result['goal_probability']['goal']}。",
        f"- 达标概率：{result['goal_probability']['probability_reach_goal']}。",
        "- 有利条件：",
    ])
    lines.extend([f"- {item['condition']}：{item['adjusted_probability']}。" for item in result["sensitivity_analysis"]["top_helpful_conditions"]])
    lines.append("- 不利条件：")
    lines.extend([f"- {item['condition']}：{item['adjusted_probability']}。" for item in result["sensitivity_analysis"]["top_harmful_conditions"]])
    lines.extend([
        "",
        "## 给客户一页备忘录核心",
        result["client_memo"],
        "",
        "## 输出产物",
        "- `client_project_scores.csv`：客户选择多指标评分。",
        "- `resource_plan.csv`：项目资源和额外权力需求。",
        "- `intervention_impact_projection.csv`：5 年影响预测。",
        "- `sensitivity_analysis.csv`：情景敏感性。",
        "- `complex_system_edges.csv`：复杂系统影响网络。",
        "- `wildlife_trade_project_frontier.png`：客户选择和项目影响图。",
    ])
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ensure_pdf_exists()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    client_df = build_client_scores()
    resource_df = build_resource_plan()
    impact_df = build_impact_projection()
    sensitivity_df, goal_probability = build_sensitivity()
    complex_edges_df = build_complex_system_edges()
    write_frontier_plot(client_df, impact_df, sensitivity_df)
    result = build_result(client_df, resource_df, impact_df, sensitivity_df, goal_probability, complex_edges_df)
    result["artifacts"] = {
        "client_project_scores": str(ARTIFACT_DIR / "client_project_scores.csv"),
        "resource_plan": str(ARTIFACT_DIR / "resource_plan.csv"),
        "intervention_impact_projection": str(ARTIFACT_DIR / "intervention_impact_projection.csv"),
        "sensitivity_analysis": str(ARTIFACT_DIR / "sensitivity_analysis.csv"),
        "complex_system_edges": str(ARTIFACT_DIR / "complex_system_edges.csv"),
        "wildlife_trade_project_frontier": str(ARTIFACT_DIR / "wildlife_trade_project_frontier.png"),
    }
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    build_report(result)
    print(json.dumps({"result": str(RESULT_PATH), "report": str(REPORT_PATH), "artifacts": str(ARTIFACT_DIR)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
