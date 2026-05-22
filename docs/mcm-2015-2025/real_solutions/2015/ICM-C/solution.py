from __future__ import annotations

import json
import os
from pathlib import Path

import pandas as pd


ARCHIVE_ROOT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
PDF_PATH = ARCHIVE_ROOT / "official_assets_extracted" / "2015" / "Managing Human Capital in Organizations.pdf"
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"
os.environ.setdefault("MPLCONFIGDIR", str(ARTIFACT_DIR / ".matplotlib"))

import matplotlib.pyplot as plt

# Official statement parameters from 2015 ICM Problem C.
TOTAL_POSITIONS = 370
SEVEN_PERSON_DEPARTMENTS = 46
FOUR_PERSON_OFFICES = 12
CURRENT_FILL_RATE = 0.85
ACTIVE_RECRUITING_LOW_RATE = 0.08
ACTIVE_RECRUITING_HIGH_RATE = 0.10
BASE_ATTRITION_RATE = 0.18
MIDDLE_MANAGER_TURNOVER_MULTIPLIER = 2.0
MIDDLE_MANAGER_SHOCK_ATTRITION_RATE = 0.30
TARGET_MIN_FILL_RATE = 0.80
HORIZON_YEARS = 2

LEVELS = [
    {
        "level": "senior_manager_executive",
        "label": "Senior managers / executives",
        "recruit_time_months": 7,
        "recruit_cost_sigma": 1.2,
        "positions": 10,
        "salary_sigma": 8.0,
        "training_cost_sigma": 0.5,
        "baseline_attrition_rate": 0.12,
        "network_weight": 1.00,
    },
    {
        "level": "junior_manager_administrator",
        "label": "Junior managers / administrators",
        "recruit_time_months": 6,
        "recruit_cost_sigma": 0.7,
        "positions": 20,
        "salary_sigma": 4.0,
        "training_cost_sigma": 0.6,
        "baseline_attrition_rate": 0.30,
        "network_weight": 0.88,
    },
    {
        "level": "experienced_supervisor_branch",
        "label": "Experienced supervisors (branch)",
        "recruit_time_months": 5,
        "recruit_cost_sigma": 0.6,
        "positions": 25,
        "salary_sigma": 2.0,
        "training_cost_sigma": 0.2,
        "baseline_attrition_rate": 0.30,
        "network_weight": 0.82,
    },
    {
        "level": "inexperienced_supervisor_division",
        "label": "Inexperienced supervisors (division)",
        "recruit_time_months": 4,
        "recruit_cost_sigma": 0.6,
        "positions": 25,
        "salary_sigma": 1.5,
        "training_cost_sigma": 0.3,
        "baseline_attrition_rate": 0.28,
        "network_weight": 0.72,
    },
    {
        "level": "experienced_staff",
        "label": "Experienced staff",
        "recruit_time_months": 3,
        "recruit_cost_sigma": 0.3,
        "positions": 110,
        "salary_sigma": 1.0,
        "training_cost_sigma": 0.1,
        "baseline_attrition_rate": 0.16,
        "network_weight": 0.48,
    },
    {
        "level": "inexperienced_staff",
        "label": "Inexperienced staff",
        "recruit_time_months": 1,
        "recruit_cost_sigma": 0.1,
        "positions": 150,
        "salary_sigma": 0.9,
        "training_cost_sigma": 0.3,
        "baseline_attrition_rate": 0.18,
        "network_weight": 0.35,
    },
    {
        "level": "administrative_clerk",
        "label": "Administrative clerks",
        "recruit_time_months": 2,
        "recruit_cost_sigma": 0.3,
        "positions": 30,
        "salary_sigma": 0.9,
        "training_cost_sigma": 0.05,
        "baseline_attrition_rate": 0.15,
        "network_weight": 0.25,
    },
]

# Deterministic modeling assumptions. They are visible in result.json and report.md.
ASSUMPTIONS = {
    "active_recruiting_rate_used": 0.09,
    "recruiting_readiness_factor": 0.70,
    "attrition_contact_influence_weight": 0.35,
    "dissatisfaction_weight_for_middle_layers": 0.45,
    "promotion_training_extra_sigma": 0.20,
    "promotion_pool_share_experienced_staff_to_supervisor": 0.20,
    "promotion_pool_share_inexperienced_supervisor_to_experienced_supervisor": 0.35,
    "promotion_pool_share_experienced_supervisor_to_junior_manager": 0.25,
    "truthfulness": "Only official statement parameters are treated as inputs; coefficients above are scenario assumptions for an auditable aggregate model.",
}


def clean_float(value: float, digits: int = 6) -> float:
    return round(float(value), digits)


def level_table() -> pd.DataFrame:
    df = pd.DataFrame(LEVELS)
    df["filled_positions"] = df["positions"] * CURRENT_FILL_RATE
    df["vacant_positions"] = df["positions"] - df["filled_positions"]
    df["annual_attrition_people"] = df["filled_positions"] * df["baseline_attrition_rate"]
    df["annual_recruit_training_sigma"] = df["annual_attrition_people"] * (df["recruit_cost_sigma"] + df["training_cost_sigma"])
    df["two_year_vacancy_recovery_hires"] = df["vacant_positions"]
    df["two_year_total_hires"] = df["annual_attrition_people"] * HORIZON_YEARS + df["two_year_vacancy_recovery_hires"]
    df["two_year_budget_sigma"] = df["two_year_total_hires"] * (df["recruit_cost_sigma"] + df["training_cost_sigma"])
    df["knowledge_risk_score"] = df["baseline_attrition_rate"] * df["network_weight"] * df["salary_sigma"]
    return df


def official_parameters() -> dict[str, object]:
    return {
        "total_positions": TOTAL_POSITIONS,
        "seven_person_departments": SEVEN_PERSON_DEPARTMENTS,
        "four_person_offices": FOUR_PERSON_OFFICES,
        "current_fill_rate": CURRENT_FILL_RATE,
        "active_recruiting_low_rate": ACTIVE_RECRUITING_LOW_RATE,
        "active_recruiting_high_rate": ACTIVE_RECRUITING_HIGH_RATE,
        "base_attrition_rate": BASE_ATTRITION_RATE,
        "middle_manager_turnover_multiplier": MIDDLE_MANAGER_TURNOVER_MULTIPLIER,
        "middle_manager_shock_attrition_rate": MIDDLE_MANAGER_SHOCK_ATTRITION_RATE,
        "target_min_fill_rate": TARGET_MIN_FILL_RATE,
        "level_table_rows": [
            {
                "level": row["level"],
                "positions": row["positions"],
                "recruit_time_months": row["recruit_time_months"],
                "recruit_cost_sigma": row["recruit_cost_sigma"],
                "salary_sigma": row["salary_sigma"],
                "training_cost_sigma": row["training_cost_sigma"],
            }
            for row in LEVELS
        ],
    }


def workforce_network(df: pd.DataFrame) -> dict[str, object]:
    level_rows = []
    for _, row in df.iterrows():
        level_rows.append(
            {
                "level": row["level"],
                "label": row["label"],
                "positions": int(row["positions"]),
                "filled_positions": clean_float(row["filled_positions"], 2),
                "vacant_positions": clean_float(row["vacant_positions"], 2),
                "baseline_attrition_rate": clean_float(row["baseline_attrition_rate"], 3),
                "knowledge_risk_score": clean_float(row["knowledge_risk_score"], 4),
            }
        )
    return {
        "model": "aggregate multilayer human-capital network with hierarchy layer, work-unit layer, and attrition-influence layer",
        "organization_units": {
            "seven_person_departments": SEVEN_PERSON_DEPARTMENTS,
            "four_person_offices": FOUR_PERSON_OFFICES,
            "total_units": SEVEN_PERSON_DEPARTMENTS + FOUR_PERSON_OFFICES,
            "positions_reconciled": SEVEN_PERSON_DEPARTMENTS * 7 + FOUR_PERSON_OFFICES * 4,
        },
        "current_staffing": {
            "total_positions": TOTAL_POSITIONS,
            "filled_positions_at_85pct": clean_float(TOTAL_POSITIONS * CURRENT_FILL_RATE, 2),
            "vacancies_at_85pct": clean_float(TOTAL_POSITIONS * (1 - CURRENT_FILL_RATE), 2),
            "active_recruiting_range_positions": [
                clean_float(TOTAL_POSITIONS * ACTIVE_RECRUITING_LOW_RATE, 2),
                clean_float(TOTAL_POSITIONS * ACTIVE_RECRUITING_HIGH_RATE, 2),
            ],
        },
        "level_rows": level_rows,
        "highest_knowledge_risk_levels": sorted(level_rows, key=lambda item: item["knowledge_risk_score"], reverse=True)[:3],
    }


def attrition_dynamics(df: pd.DataFrame) -> dict[str, object]:
    rows = []
    for _, row in df.iterrows():
        contact_component = row["network_weight"] * ASSUMPTIONS["attrition_contact_influence_weight"]
        middle_penalty = ASSUMPTIONS["dissatisfaction_weight_for_middle_layers"] if "supervisor" in row["level"] or "junior_manager" in row["level"] else 0.0
        dynamic_risk = min(0.75, row["baseline_attrition_rate"] + 0.08 * contact_component + 0.06 * middle_penalty)
        productivity_loss_sigma = row["filled_positions"] * dynamic_risk * row["salary_sigma"] * row["network_weight"]
        rows.append(
            {
                "level": row["level"],
                "baseline_attrition_rate": clean_float(row["baseline_attrition_rate"], 3),
                "dynamic_attrition_risk": clean_float(dynamic_risk, 4),
                "expected_annual_leavers": clean_float(row["filled_positions"] * dynamic_risk, 2),
                "productivity_loss_sigma": clean_float(productivity_loss_sigma, 3),
            }
        )
    return {
        "processes": [
            "influence contagion: departures connected to a level raise dissatisfaction pressure in adjacent levels",
            "middle-layer career blockage: junior managers and supervisors receive an extra dissatisfaction component",
            "productivity loss: leavers remove salary-weighted knowledge and coordination capacity before replacements mature",
        ],
        "risk_rows": rows,
        "top_dynamic_risk_levels": sorted(rows, key=lambda item: item["productivity_loss_sigma"], reverse=True)[:3],
    }


def budget_forecast(df: pd.DataFrame) -> dict[str, object]:
    rows = []
    for _, row in df.iterrows():
        rows.append(
            {
                "level": row["level"],
                "positions": int(row["positions"]),
                "annual_attrition_people": clean_float(row["annual_attrition_people"], 2),
                "two_year_total_hires": clean_float(row["two_year_total_hires"], 2),
                "two_year_recruiting_sigma": clean_float(row["two_year_total_hires"] * row["recruit_cost_sigma"], 3),
                "two_year_training_sigma": clean_float(row["two_year_total_hires"] * row["training_cost_sigma"], 3),
                "two_year_budget_sigma": clean_float(row["two_year_budget_sigma"], 3),
            }
        )
    return {
        "horizon_years": HORIZON_YEARS,
        "method": "replace projected attrition and recover the 15% vacancy gap over two years; costs are reported in units of sigma as requested by the statement",
        "rows": rows,
        "total_two_year_recruiting_sigma": clean_float(sum(row["two_year_recruiting_sigma"] for row in rows), 3),
        "total_two_year_training_sigma": clean_float(sum(row["two_year_training_sigma"] for row in rows), 3),
        "total_two_year_sigma": clean_float(sum(row["two_year_budget_sigma"] for row in rows), 3),
    }


def annual_hiring_capacity(df: pd.DataFrame) -> float:
    active_pipeline = TOTAL_POSITIONS * ASSUMPTIONS["active_recruiting_rate_used"]
    weighted_recruit_months = (df["positions"] * df["recruit_time_months"]).sum() / df["positions"].sum()
    return active_pipeline * (12.0 / weighted_recruit_months) * ASSUMPTIONS["recruiting_readiness_factor"]


def turnover_scenarios(df: pd.DataFrame) -> dict[str, object]:
    capacity = annual_hiring_capacity(df)
    rows = []
    can_sustain = {}
    for rate in [BASE_ATTRITION_RATE, 0.25, 0.35]:
        annual_leavers = TOTAL_POSITIONS * rate
        net_staff_change = capacity - annual_leavers
        end_fill_rate = min(1.0, (TOTAL_POSITIONS * CURRENT_FILL_RATE + net_staff_change) / TOTAL_POSITIONS)
        rows.append(
            {
                "annual_turnover_rate": clean_float(rate, 3),
                "annual_leavers_at_full_positions": clean_float(annual_leavers, 2),
                "estimated_hiring_capacity_per_year": clean_float(capacity, 2),
                "net_staff_change_first_year": clean_float(net_staff_change, 2),
                "end_of_year_fill_rate": clean_float(end_fill_rate, 4),
                "sustains_80pct_fill": bool(end_fill_rate >= TARGET_MIN_FILL_RATE),
            }
        )
        label = f"annual_turnover_{int(rate * 100)}pct"
        can_sustain[label] = bool(end_fill_rate >= TARGET_MIN_FILL_RATE)
    return {
        "method": "compare annual attrition load with active recruiting throughput adjusted for administrative readiness",
        "recruiting_capacity_assumptions": {
            "active_recruiting_rate_used": ASSUMPTIONS["active_recruiting_rate_used"],
            "recruiting_readiness_factor": ASSUMPTIONS["recruiting_readiness_factor"],
            "estimated_hiring_capacity_per_year": clean_float(capacity, 2),
        },
        "scenario_rows": rows,
        "can_sustain_80pct_fill": can_sustain,
        "indirect_effects_of_high_turnover": [
            "middle-layer vacancies increase coordination delay between executives and staff",
            "HR capacity is consumed by replacement hiring instead of quality screening",
            "training load rises while informal knowledge transfer falls",
        ],
    }


def promotion_shock_projection(df: pd.DataFrame) -> dict[str, object]:
    positions = {row["level"]: float(row["positions"] * CURRENT_FILL_RATE) for _, row in df.iterrows()}
    shock_levels = ["junior_manager_administrator", "experienced_supervisor_branch"]
    shock_losses = {level: positions[level] * MIDDLE_MANAGER_SHOCK_ATTRITION_RATE for level in shock_levels}

    no_external = positions.copy()
    for level, loss in shock_losses.items():
        no_external[level] -= loss

    promotions_only = no_external.copy()
    promote_exp_supervisor_to_junior = min(
        shock_losses["junior_manager_administrator"],
        positions["experienced_supervisor_branch"] * ASSUMPTIONS["promotion_pool_share_experienced_supervisor_to_junior_manager"],
    )
    promotions_only["junior_manager_administrator"] += promote_exp_supervisor_to_junior
    promotions_only["experienced_supervisor_branch"] -= promote_exp_supervisor_to_junior

    promote_inexp_supervisor_to_exp = min(
        shock_losses["experienced_supervisor_branch"] + promote_exp_supervisor_to_junior,
        positions["inexperienced_supervisor_division"] * ASSUMPTIONS["promotion_pool_share_inexperienced_supervisor_to_experienced_supervisor"],
    )
    promotions_only["experienced_supervisor_branch"] += promote_inexp_supervisor_to_exp
    promotions_only["inexperienced_supervisor_division"] -= promote_inexp_supervisor_to_exp

    promote_staff_to_supervisor = min(
        promote_inexp_supervisor_to_exp,
        positions["experienced_staff"] * ASSUMPTIONS["promotion_pool_share_experienced_staff_to_supervisor"],
    )
    promotions_only["inexperienced_supervisor_division"] += promote_staff_to_supervisor
    promotions_only["experienced_staff"] -= promote_staff_to_supervisor

    rows = []
    for level in positions:
        rows.append(
            {
                "level": level,
                "baseline_filled": clean_float(positions[level], 2),
                "after_30pct_middle_attrition_no_external": clean_float(no_external[level], 2),
                "after_internal_promotions_only": clean_float(promotions_only[level], 2),
            }
        )
    return {
        "scenario": "30% attrition among junior managers and experienced supervisors, other attrition left at statement 18% baseline for broader planning context",
        "shock_losses": {key: clean_float(value, 2) for key, value in shock_losses.items()},
        "promotion_moves": {
            "experienced_supervisor_to_junior_manager": clean_float(promote_exp_supervisor_to_junior, 2),
            "inexperienced_supervisor_to_experienced_supervisor": clean_float(promote_inexp_supervisor_to_exp, 2),
            "experienced_staff_to_inexperienced_supervisor": clean_float(promote_staff_to_supervisor, 2),
        },
        "rows": rows,
        "health_impact": {
            "no_external_middle_layer_fill_rate": clean_float(sum(no_external[level] for level in shock_levels) / sum(row["positions"] for _, row in df[df["level"].isin(shock_levels)].iterrows()), 4),
            "promotions_only_middle_layer_fill_rate": clean_float(sum(promotions_only[level] for level in shock_levels) / sum(row["positions"] for _, row in df[df["level"].isin(shock_levels)].iterrows()), 4),
            "interpretation": "Internal promotion cushions the management gap, but it transfers vacancies to supervisors and experienced staff, so HR health still deteriorates without external recruiting.",
        },
    }


def team_science_extension() -> dict[str, object]:
    return {
        "team_science_summary": [
            "Represent each work unit as a team layer with formal reporting edges and informal collaboration edges.",
            "Track trust, information flow, influence, and friendship as separate layers sharing the same employee nodes.",
            "Use multiplex centrality to find employees whose departure would damage several layers at once.",
        ],
        "recommended_next_layers": ["information_flow", "trust", "influence", "friendship", "training_dependency"],
        "models": ["multilayer network", "Markov workforce transition", "queue/capacity model for recruiting", "multi-criteria HR health index"],
    }


def executive_report(workforce: dict[str, object], budget: dict[str, object], scenarios: dict[str, object], shock: dict[str, object]) -> str:
    current = workforce["current_staffing"]
    can25 = scenarios["can_sustain_80pct_fill"]["annual_turnover_25pct"]
    can35 = scenarios["can_sustain_80pct_fill"]["annual_turnover_35pct"]
    return (
        "To the ICM HR Manager:\n\n"
        f"The official statement describes {TOTAL_POSITIONS} positions, {current['filled_positions_at_85pct']} currently filled positions, "
        f"and an annual attrition rate of {BASE_ATTRITION_RATE:.0%}. I modeled ICM as a multilayer human-capital network linking hierarchy, "
        "work units, attrition influence, and training/recruiting capacity. The most fragile layers are junior managers and supervisors: "
        "they are central enough to transmit knowledge and dissatisfaction, but the statement says middle turnover is unusually high.\n\n"
        f"For the next two years, the aggregate recruiting-plus-training budget is {budget['total_two_year_sigma']} sigma units. "
        f"Under the explicit throughput assumptions, ICM can sustain 80% fill at 25% annual turnover: {can25}; at 35%: {can35}. "
        "The 35% case overloads HR and creates indirect costs through weak screening, manager vacancies, and lost informal knowledge.\n\n"
        f"If 30% of junior managers and experienced supervisors leave, internal promotions recover part of the gap "
        f"({shock['health_impact']['promotions_only_middle_layer_fill_rate']} middle-layer fill), but they drain experienced supervisors and staff. "
        "Recommendation: stabilize middle managers first, reserve recruiting capacity for critical roles, and build a multiplex employee network so HR can monitor influence, trust, information flow, and training dependencies before departures cascade."
    )


def write_artifacts(df: pd.DataFrame, budget: dict[str, object], scenarios: dict[str, object], shock: dict[str, object]) -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(ARTIFACT_DIR / "workforce_level_table.csv", index=False, encoding="utf-8-sig")
    pd.DataFrame(budget["rows"]).to_csv(ARTIFACT_DIR / "two_year_budget.csv", index=False, encoding="utf-8-sig")
    pd.DataFrame(scenarios["scenario_rows"]).to_csv(ARTIFACT_DIR / "turnover_scenarios.csv", index=False, encoding="utf-8-sig")
    pd.DataFrame(shock["rows"]).to_csv(ARTIFACT_DIR / "promotion_shock_projection.csv", index=False, encoding="utf-8-sig")

    fig, ax = plt.subplots(figsize=(9, 5))
    plot_df = df.sort_values("knowledge_risk_score", ascending=True)
    ax.barh(plot_df["label"], plot_df["knowledge_risk_score"], color="#2f6f73")
    ax.set_title("2015 ICM-C Human Capital Knowledge-Risk Score")
    ax.set_xlabel("attrition rate x network weight x salary sigma")
    ax.grid(axis="x", alpha=0.25)
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "human_capital_health.png", dpi=180)
    plt.close(fig)


def write_report(result: dict[str, object]) -> None:
    budget = result["budget_forecast"]
    scenarios = result["turnover_scenarios"]
    shock = result["middle_manager_shock"]
    lines = [
        "# 2015 ICM-C Managing Human Capital in Organizations 题面参数实验报告",
        "",
        "## 数据来源",
        f"- 官方 PDF：`{PDF_PATH}`。",
        "- 本题没有独立 CSV/XLSX 附件；模型只使用题面给出的组织规模、岗位层级、招聘时间、招聘成本、工资、培训成本、85% 填补率和 18% 流失率。",
        "- 其余系数均列入 `assumption_audit`，作为可替换的确定性情景假设，不当作观测数据。",
        "",
        "## Q1 人力资本网络模型",
        f"- 组织单元：{SEVEN_PERSON_DEPARTMENTS} 个 7 人部门 + {FOUR_PERSON_OFFICES} 个 4 人办公室 = {TOTAL_POSITIONS} 个岗位。",
        f"- 当前填补岗位：{result['workforce_network']['current_staffing']['filled_positions_at_85pct']}；空缺：{result['workforce_network']['current_staffing']['vacancies_at_85pct']}。",
        f"- 高知识风险层级：{', '.join(item['label'] for item in result['workforce_network']['highest_knowledge_risk_levels'])}。",
        "",
        "## Q2 流失动态与生产率影响",
        "- 动态过程：离职影响扩散、中层职业阻塞、知识/协调生产率损失。",
        f"- 最高生产率损失层级：{result['attrition_dynamics']['top_dynamic_risk_levels'][0]['level']}。",
        "",
        "## Q3 两年招聘与培训预算",
        f"- 两年总预算：{budget['total_two_year_sigma']} sigma。",
        f"- 招聘成本：{budget['total_two_year_recruiting_sigma']} sigma；培训成本：{budget['total_two_year_training_sigma']} sigma。",
        "",
        "## Q4 25%/35% 流失率情景",
        f"- 25% 年流失能否维持 80% 填补率：{scenarios['can_sustain_80pct_fill']['annual_turnover_25pct']}。",
        f"- 35% 年流失能否维持 80% 填补率：{scenarios['can_sustain_80pct_fill']['annual_turnover_35pct']}。",
        "- 间接影响：筛选质量下降、培训负荷上升、中层协调断裂。",
        "",
        "## Q5 中层 30% 流失冲击",
        f"- 冲击损失：{shock['shock_losses']}。",
        f"- 仅内部晋升后的中层填补率：{shock['health_impact']['promotions_only_middle_layer_fill_rate']}。",
        f"- 解释：{shock['health_impact']['interpretation']}",
        "",
        "## Q6 团队科学与多层网络",
        "- 建议把信息流、信任、影响力、友谊和培训依赖作为多层网络，使用 multiplex centrality 识别关键员工。",
        "",
        "## Q7 执行摘要",
        result["executive_report"],
        "",
        "## 输出文件",
        f"- `result.json`：{RESULT_PATH}",
        f"- `workforce_level_table.csv`：{ARTIFACT_DIR / 'workforce_level_table.csv'}",
        f"- `two_year_budget.csv`：{ARTIFACT_DIR / 'two_year_budget.csv'}",
        f"- `turnover_scenarios.csv`：{ARTIFACT_DIR / 'turnover_scenarios.csv'}",
        f"- `promotion_shock_projection.csv`：{ARTIFACT_DIR / 'promotion_shock_projection.csv'}",
        f"- `human_capital_health.png`：{ARTIFACT_DIR / 'human_capital_health.png'}",
    ]
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    if not PDF_PATH.exists():
        raise FileNotFoundError(f"Missing official PDF: {PDF_PATH}")
    df = level_table()
    workforce = workforce_network(df)
    dynamics = attrition_dynamics(df)
    budget = budget_forecast(df)
    scenarios = turnover_scenarios(df)
    shock = promotion_shock_projection(df)
    extension = team_science_extension()
    result = {
        "problem_id": "2015-C",
        "data_source": {
            "type": "official_statement_parameters",
            "root": str(PDF_PATH),
            "parameters": official_parameters(),
            "assumptions": ASSUMPTIONS,
        },
        "workforce_network": workforce,
        "attrition_dynamics": dynamics,
        "budget_forecast": budget,
        "turnover_scenarios": scenarios,
        "middle_manager_shock": shock,
        "team_science_extension": extension,
        "executive_report": executive_report(workforce, budget, scenarios, shock),
        "assumption_audit": {
            "truthfulness_note": "This workflow uses official statement parameters from the 2015 ICM-C PDF and explicit deterministic assumptions; it does not create hidden observed employee records.",
            "replaceable_assumptions": ASSUMPTIONS,
        },
    }
    write_artifacts(df, budget, scenarios, shock)
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_report(result)
    print(json.dumps({"result": str(RESULT_PATH), "report": str(REPORT_PATH), "artifacts": str(ARTIFACT_DIR)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
