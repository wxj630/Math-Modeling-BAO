from __future__ import annotations

import itertools
import json
import os
from pathlib import Path

import pandas as pd


ARCHIVE_ROOT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
PDF_PATH = ARCHIVE_ROOT / "official_assets_extracted" / "2016" / "Space Junk.pdf"
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"
os.environ.setdefault("MPLCONFIGDIR", str(ARTIFACT_DIR / ".matplotlib"))

import matplotlib.pyplot as plt


TRACKED_DEBRIS_COUNT = 500_000
REFERENCE_COLLISION_YEAR = 2009
REFERENCE_COLLISION = "Kosmos-2251 / Iridium-33"
EVALUATION_HORIZON_YEARS = 10
DISCOUNT_RATE = 0.08

ALTERNATIVES = [
    {
        "option": "space_based_water_jets",
        "category": "active_removal",
        "capex_musd": 420.0,
        "annual_opex_musd": 55.0,
        "annual_revenue_musd": 105.0,
        "debris_removed_per_year": 1800,
        "risk_reduction_per_1000_removed": 0.0018,
        "technical_risk": 0.46,
        "regulatory_risk": 0.32,
        "scalability": 0.48,
        "statement_link": "small space-based water jets targeting debris",
    },
    {
        "option": "high_energy_lasers",
        "category": "active_removal_or_deflection",
        "capex_musd": 260.0,
        "annual_opex_musd": 38.0,
        "annual_revenue_musd": 92.0,
        "debris_removed_per_year": 2400,
        "risk_reduction_per_1000_removed": 0.0015,
        "technical_risk": 0.38,
        "regulatory_risk": 0.44,
        "scalability": 0.62,
        "statement_link": "high energy lasers targeting specific debris",
    },
    {
        "option": "sweeper_satellites",
        "category": "active_removal",
        "capex_musd": 780.0,
        "annual_opex_musd": 95.0,
        "annual_revenue_musd": 135.0,
        "debris_removed_per_year": 5200,
        "risk_reduction_per_1000_removed": 0.0012,
        "technical_risk": 0.58,
        "regulatory_risk": 0.36,
        "scalability": 0.54,
        "statement_link": "large satellites designed to sweep up debris",
    },
    {
        "option": "laser_tracking_subscription",
        "category": "collision_avoidance_service",
        "capex_musd": 85.0,
        "annual_opex_musd": 18.0,
        "annual_revenue_musd": 72.0,
        "debris_removed_per_year": 0,
        "risk_reduction_per_1000_removed": 0.0,
        "technical_risk": 0.18,
        "regulatory_risk": 0.12,
        "scalability": 0.82,
        "statement_link": "innovative alternative for avoiding collisions if removal is not commercially viable",
    },
]

ASSUMPTIONS = {
    "market_note": "Private-firm revenue is a transparent scenario variable for service contracts with satellite operators and insurers; it is not observed COMAP data.",
    "risk_score_definition": "risk_score = 0.55 technical risk + 0.45 regulatory risk, lower is better",
    "benefit_definition": "collision risk reduction proxy combines tracked-debris removal and collision-avoidance service value over a 10-year horizon",
    "commercial_rule": "commercial opportunity is attractive if NPV is positive and risk-adjusted score exceeds 0.05",
    "combination_synergy": "hybrid active removal plus avoidance gets a small revenue/risk-reduction synergy but also integration cost",
}


def clean_float(value: float, digits: int = 6) -> float:
    return round(float(value), digits)


def npv(capex: float, annual_net: float, years: int = EVALUATION_HORIZON_YEARS) -> float:
    present = sum(annual_net / ((1 + DISCOUNT_RATE) ** year) for year in range(1, years + 1))
    return present - capex


def score_option(option: dict[str, object], debris_multiplier: float = 1.0, revenue_multiplier: float = 1.0) -> dict[str, object]:
    annual_revenue = float(option["annual_revenue_musd"]) * revenue_multiplier
    annual_opex = float(option["annual_opex_musd"])
    removed = float(option["debris_removed_per_year"]) * debris_multiplier
    ten_year_removed = removed * EVALUATION_HORIZON_YEARS
    risk_reduction = min(0.75, ten_year_removed / 1000.0 * float(option["risk_reduction_per_1000_removed"]))
    if option["category"] == "collision_avoidance_service":
        risk_reduction = 0.16 * revenue_multiplier
    risk_score = 0.55 * float(option["technical_risk"]) + 0.45 * float(option["regulatory_risk"])
    value = npv(float(option["capex_musd"]), annual_revenue - annual_opex)
    risk_adjusted_score = value / 1000.0 + 0.8 * risk_reduction + 0.25 * float(option["scalability"]) - 0.45 * risk_score
    return {
        "option": option["option"],
        "category": option["category"],
        "capex_musd": clean_float(option["capex_musd"], 3),
        "annual_opex_musd": clean_float(option["annual_opex_musd"], 3),
        "annual_revenue_musd": clean_float(annual_revenue, 3),
        "ten_year_debris_removed": int(round(ten_year_removed)),
        "ten_year_collision_risk_reduction_proxy": clean_float(risk_reduction, 5),
        "risk_score": clean_float(risk_score, 5),
        "npv_musd": clean_float(value, 3),
        "risk_adjusted_score": clean_float(risk_adjusted_score, 6),
        "commercially_attractive": bool(value > 0 and risk_adjusted_score > 0.05),
        "statement_link": option["statement_link"],
    }


def alternative_assessment() -> dict[str, object]:
    rows = [score_option(option) for option in ALTERNATIVES]
    return {
        "method": "deterministic private-firm screening over cost, revenue, risk, scalability, and 10-year debris-risk reduction proxy",
        "alternatives": sorted(rows, key=lambda row: row["risk_adjusted_score"], reverse=True),
    }


def combine_options(options: list[dict[str, object]]) -> dict[str, object]:
    names = [str(option["option"]) for option in options]
    capex = sum(float(option["capex_musd"]) for option in options) * (1.0 + 0.06 * (len(options) - 1))
    annual_opex = sum(float(option["annual_opex_musd"]) for option in options) * (1.0 + 0.04 * (len(options) - 1))
    annual_revenue = sum(float(option["annual_revenue_musd"]) for option in options) * (1.0 + 0.05 * (len(options) - 1))
    removed = sum(float(option["debris_removed_per_year"]) for option in options) * (1.0 + 0.08 * max(0, len(options) - 1))
    risk_reduction = min(0.82, sum(score_option(option)["ten_year_collision_risk_reduction_proxy"] for option in options) * (1.0 + 0.10 * (len(options) - 1)))
    technical = sum(float(option["technical_risk"]) for option in options) / len(options)
    regulatory = sum(float(option["regulatory_risk"]) for option in options) / len(options) + 0.03 * (len(options) - 1)
    scalability = max(float(option["scalability"]) for option in options)
    risk_score = 0.55 * technical + 0.45 * regulatory
    value = npv(capex, annual_revenue - annual_opex)
    risk_adjusted_score = value / 1000.0 + 0.8 * risk_reduction + 0.25 * scalability - 0.45 * risk_score
    return {
        "combination": "+".join(names),
        "option_count": len(options),
        "capex_musd": clean_float(capex, 3),
        "annual_opex_musd": clean_float(annual_opex, 3),
        "annual_revenue_musd": clean_float(annual_revenue, 3),
        "ten_year_debris_removed": int(round(removed * EVALUATION_HORIZON_YEARS)),
        "ten_year_collision_risk_reduction_proxy": clean_float(risk_reduction, 5),
        "risk_score": clean_float(risk_score, 5),
        "npv_musd": clean_float(value, 3),
        "risk_adjusted_score": clean_float(risk_adjusted_score, 6),
        "commercially_attractive": bool(value > 0 and risk_adjusted_score > 0.05),
    }


def combination_assessment() -> dict[str, object]:
    combos = []
    for size in [2, 3]:
        for options in itertools.combinations(ALTERNATIVES, size):
            combos.append(combine_options(list(options)))
    combos = sorted(combos, key=lambda row: row["risk_adjusted_score"], reverse=True)
    return {
        "method": "evaluate pair and triple combinations with transparent integration cost and synergy assumptions",
        "combinations": combos,
    }


def what_if_scenarios() -> dict[str, object]:
    rows = []
    scenario_defs = [
        ("baseline", 1.0, 1.0),
        ("tracked_debris_doubles", 2.0, 1.15),
        ("insurance_market_weak", 1.0, 0.72),
        ("regulators_support_lasers", 1.1, 1.05),
        ("launch_cost_drop_active_removal", 1.35, 1.0),
    ]
    for scenario, debris_multiplier, revenue_multiplier in scenario_defs:
        scored = [score_option(option, debris_multiplier=debris_multiplier, revenue_multiplier=revenue_multiplier) for option in ALTERNATIVES]
        best = sorted(scored, key=lambda row: row["risk_adjusted_score"], reverse=True)[0]
        rows.append(
            {
                "scenario": scenario,
                "debris_multiplier": debris_multiplier,
                "revenue_multiplier": revenue_multiplier,
                "best_option": best["option"],
                "best_npv_musd": best["npv_musd"],
                "best_risk_adjusted_score": best["risk_adjusted_score"],
                "commercially_attractive": best["commercially_attractive"],
            }
        )
    return {
        "method": "deterministic what-if stress tests over debris load and service-market revenue",
        "rows": rows,
    }


def commercial_opportunity(alternatives: dict[str, object], combinations: dict[str, object]) -> dict[str, object]:
    candidates = alternatives["alternatives"] + combinations["combinations"]
    best = sorted(candidates, key=lambda row: row["risk_adjusted_score"], reverse=True)[0]
    if best["commercially_attractive"] and "laser_tracking_subscription" in str(best.get("option", best.get("combination", ""))):
        action = "laser_tracking_subscription"
    elif best["commercially_attractive"]:
        action = "hybrid_laser_and_avoidance"
    else:
        action = "no_removal_collision_avoidance"
    return {
        "recommended_action": action,
        "best_candidate": best,
        "interpretation": "A full debris-removal business is capital intensive; the most attractive private opportunity is a staged service model that sells collision avoidance and selectively adds laser deflection/removal when contracts support it.",
    }


def executive_summary(opportunity: dict[str, object], scenarios: dict[str, object]) -> str:
    best = opportunity["best_candidate"]
    name = best.get("option", best.get("combination"))
    return (
        "Executive summary for policy makers and media analysts:\n\n"
        f"The official problem states that more than {TRACKED_DEBRIS_COUNT:,} pieces of debris are tracked and that the 2009 {REFERENCE_COLLISION} collision made the risk visible. "
        "A private company should not begin with an expensive sweeper-satellite-only business. In this screening model, the best near-term commercial option is "
        f"{name}, with NPV {best['npv_musd']} million USD and risk-adjusted score {best['risk_adjusted_score']}. "
        "The recommended strategy is staged: sell tracking/avoidance subscriptions first, then add laser deflection for high-value debris when regulation and customer contracts are in place. "
        "If revenue weakens, collision-avoidance services remain the least risky fallback; if tracked debris grows faster, hybrid laser-plus-avoidance becomes more attractive."
    )


def write_artifacts(alternatives: dict[str, object], combinations: dict[str, object], scenarios: dict[str, object]) -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(alternatives["alternatives"]).to_csv(ARTIFACT_DIR / "alternative_scores.csv", index=False, encoding="utf-8-sig")
    pd.DataFrame(combinations["combinations"]).to_csv(ARTIFACT_DIR / "combination_scores.csv", index=False, encoding="utf-8-sig")
    pd.DataFrame(scenarios["rows"]).to_csv(ARTIFACT_DIR / "what_if_scenarios.csv", index=False, encoding="utf-8-sig")

    alt = pd.DataFrame(alternatives["alternatives"])
    fig, ax = plt.subplots(figsize=(8.5, 5))
    ax.scatter(alt["risk_score"], alt["npv_musd"], s=(alt["ten_year_collision_risk_reduction_proxy"] + 0.05) * 950, color="#2f6f73", alpha=0.75)
    for _, row in alt.iterrows():
        ax.annotate(row["option"].replace("_", "\n"), (row["risk_score"], row["npv_musd"]), fontsize=8, xytext=(4, 4), textcoords="offset points")
    ax.axhline(0, color="#444444", linestyle="--")
    ax.set_xlabel("Risk score (lower is better)")
    ax.set_ylabel("10-year NPV (million USD)")
    ax.set_title("2016 MCM-B Space Junk Commercial Frontier")
    ax.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "debris_strategy_frontier.png", dpi=180)
    plt.close(fig)


def write_report(result: dict[str, object]) -> None:
    best = result["commercial_opportunity"]["best_candidate"]
    lines = [
        "# 2016 MCM-B Space Junk 题面参数实验报告",
        "",
        "## 数据来源",
        f"- 官方 PDF：`{PDF_PATH}`。",
        f"- 官方题面参数：tracked debris > {TRACKED_DEBRIS_COUNT:,}；2009 年 {REFERENCE_COLLISION} collision；候选方案包括 space-based water jets、high energy lasers、sweeper satellites，以及不可行时的 collision avoidance。",
        "- 本题没有独立 CSV/XLSX 附件；商业收入、成本、风险和协同效应均为显式可替换情景假设。",
        "",
        "## Q1 时间相关商业机会模型",
        f"- 最佳候选：{best.get('option', best.get('combination'))}。",
        f"- 10 年 NPV：{best['npv_musd']} million USD。",
        f"- 风险调整得分：{best['risk_adjusted_score']}。",
        "",
        "## Q2 成本、风险、收益比较",
        "- 输出 `alternative_scores.csv` 比较 capex、opex、revenue、10 年移除数量、风险得分和 NPV。",
        "",
        "## Q3 组合方案与 what-if 情景",
        "- 输出 `combination_scores.csv` 和 `what_if_scenarios.csv`，比较组合协同与市场变化。",
        "",
        "## Q4 商业建议与执行摘要",
        f"- 推荐动作：{result['commercial_opportunity']['recommended_action']}。",
        result["executive_summary"],
        "",
        "## 输出文件",
        f"- `result.json`：{RESULT_PATH}",
        f"- `alternative_scores.csv`：{ARTIFACT_DIR / 'alternative_scores.csv'}",
        f"- `combination_scores.csv`：{ARTIFACT_DIR / 'combination_scores.csv'}",
        f"- `what_if_scenarios.csv`：{ARTIFACT_DIR / 'what_if_scenarios.csv'}",
        f"- `debris_strategy_frontier.png`：{ARTIFACT_DIR / 'debris_strategy_frontier.png'}",
    ]
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    if not PDF_PATH.exists():
        raise FileNotFoundError(f"Missing official PDF: {PDF_PATH}")
    alternatives = alternative_assessment()
    combinations = combination_assessment()
    scenarios = what_if_scenarios()
    opportunity = commercial_opportunity(alternatives, combinations)
    result = {
        "problem_id": "2016-B",
        "data_source": {
            "type": "official_statement_parameters",
            "root": str(PDF_PATH),
            "source_pdf": str(PDF_PATH),
            "official_problem_parameters": {
                "tracked_debris_count": TRACKED_DEBRIS_COUNT,
                "reference_collision_year": REFERENCE_COLLISION_YEAR,
                "reference_collision": REFERENCE_COLLISION,
                "candidate_methods_named_in_statement": ["space-based water jets", "high energy lasers", "large sweeper satellites"],
                "report_requirement": "two-page executive summary for high-level policy makers and news media analysts",
            },
            "assumptions": ASSUMPTIONS,
        },
        "alternative_assessment": alternatives,
        "combination_assessment": combinations,
        "what_if_scenarios": scenarios,
        "commercial_opportunity": opportunity,
        "executive_summary": executive_summary(opportunity, scenarios),
        "assumption_audit": {
            "truthfulness_note": "This workflow uses official statement constraints and explicit deterministic business assumptions; it does not claim observed space-debris business data.",
            "replaceable_assumptions": ASSUMPTIONS,
        },
    }
    write_artifacts(alternatives, combinations, scenarios)
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_report(result)
    print(json.dumps({"result": str(RESULT_PATH), "report": str(REPORT_PATH), "artifacts": str(ARTIFACT_DIR)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
