from __future__ import annotations

import json
import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ARCHIVE_ROOT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
PDF_PATH = ARCHIVE_ROOT / "official_assets_extracted" / "2025" / "2025_MCM_Problem_B.pdf"
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"

# Official statement parameters from 2025 MCM Problem B.
JUNEAU_POPULATION = 30_000
ANNUAL_CRUISE_PASSENGERS_2023 = 1_600_000
BUSIEST_DAY_VISITORS = 20_000
BUSIEST_DAY_SHIPS = 7
TOURISM_REVENUE_USD_2023 = 375_000_000
GLACIER_RECESSION_FOOTBALL_FIELDS_SINCE_2007 = 8
GLACIER_RECESSION_START_YEAR = 2007
REFERENCE_YEAR = 2023

# Modeling assumptions are deterministic and visible in result.json; they are not generated data.
SEASON_DAYS = 153
BASELINE_DAILY_CAP = BUSIEST_DAY_VISITORS
BASELINE_VISITOR_FEE = 0.0
BASELINE_CONSERVATION_SHARE = 0.25
FEE_ELASTICITY_PER_USD = 0.0024
CAP_COMPLIANCE = 0.96
BASE_EXTERNAL_COST_PER_VISITOR = 58.0
BASE_CROWDING_COST_PER_EXCESS_VISITOR = 18.0
BASE_CARBON_COST_PER_VISITOR = 22.0
BASE_RESIDENT_ACCEPTANCE = 0.58
BASE_ATTRACTION_HEALTH = 0.67


def clean_float(value: float, digits: int = 6) -> float:
    return round(float(value), digits)


def official_parameters() -> dict[str, object]:
    return {
        "juneau_population": JUNEAU_POPULATION,
        "annual_cruise_passengers_2023": ANNUAL_CRUISE_PASSENGERS_2023,
        "busiest_day_visitors": BUSIEST_DAY_VISITORS,
        "busiest_day_ships": BUSIEST_DAY_SHIPS,
        "tourism_revenue_usd_2023": TOURISM_REVENUE_USD_2023,
        "glacier_recession_football_fields_since_2007": GLACIER_RECESSION_FOOTBALL_FIELDS_SINCE_2007,
        "glacier_recession_start_year": GLACIER_RECESSION_START_YEAR,
        "reference_year": REFERENCE_YEAR,
    }


def scenario_assumptions() -> dict[str, object]:
    return {
        "season_days": SEASON_DAYS,
        "fee_elasticity_per_usd": FEE_ELASTICITY_PER_USD,
        "cap_compliance": CAP_COMPLIANCE,
        "base_external_cost_per_visitor_usd": BASE_EXTERNAL_COST_PER_VISITOR,
        "base_crowding_cost_per_excess_visitor_usd": BASE_CROWDING_COST_PER_EXCESS_VISITOR,
        "base_carbon_cost_per_visitor_usd": BASE_CARBON_COST_PER_VISITOR,
        "base_resident_acceptance_index": BASE_RESIDENT_ACCEPTANCE,
        "base_attraction_health_index": BASE_ATTRACTION_HEALTH,
        "conservation_feedback": "additional fee revenue is split into conservation/infrastructure/community spending; conservation improves attraction health, infrastructure reduces hidden cost, community spending improves acceptance",
    }


def evaluate_policy(daily_cap: int, visitor_fee_usd: float, conservation_share: float) -> dict[str, float]:
    revenue_per_visitor = TOURISM_REVENUE_USD_2023 / ANNUAL_CRUISE_PASSENGERS_2023
    demand_after_fee = ANNUAL_CRUISE_PASSENGERS_2023 * max(0.70, 1.0 - FEE_ELASTICITY_PER_USD * visitor_fee_usd)
    cap_limited_visitors = min(demand_after_fee, daily_cap * SEASON_DAYS * CAP_COMPLIANCE)
    visitor_ratio = cap_limited_visitors / ANNUAL_CRUISE_PASSENGERS_2023
    fee_revenue = cap_limited_visitors * visitor_fee_usd
    tourism_business_revenue = cap_limited_visitors * revenue_per_visitor
    total_revenue = tourism_business_revenue + fee_revenue

    infrastructure_share = 0.45 * (1.0 - conservation_share)
    community_share = 1.0 - conservation_share - infrastructure_share
    conservation_spend = fee_revenue * conservation_share
    infrastructure_spend = fee_revenue * infrastructure_share
    community_spend = fee_revenue * community_share

    peak_pressure = daily_cap / BUSIEST_DAY_VISITORS
    crowding_cost = max(0.0, daily_cap - JUNEAU_POPULATION * 0.35) * BASE_CROWDING_COST_PER_EXCESS_VISITOR * SEASON_DAYS / 1_000_000
    infrastructure_relief = 1.0 - min(0.35, infrastructure_spend / 90_000_000)
    hidden_cost = cap_limited_visitors * (BASE_EXTERNAL_COST_PER_VISITOR + BASE_CARBON_COST_PER_VISITOR) * infrastructure_relief + crowding_cost * 1_000_000

    glacier_recession_rate_fields_per_year = GLACIER_RECESSION_FOOTBALL_FIELDS_SINCE_2007 / (REFERENCE_YEAR - GLACIER_RECESSION_START_YEAR)
    conservation_relief = min(0.30, conservation_spend / 80_000_000)
    projected_glacier_pressure = glacier_recession_rate_fields_per_year * (0.65 + 0.35 * visitor_ratio) * (1.0 - conservation_relief)
    attraction_health = min(1.0, BASE_ATTRACTION_HEALTH + conservation_relief - 0.10 * max(0, peak_pressure - 0.70))
    resident_acceptance = min(1.0, BASE_RESIDENT_ACCEPTANCE + min(0.20, community_spend / 40_000_000) - 0.25 * max(0, peak_pressure - 0.70))
    economic_index = min(1.25, total_revenue / TOURISM_REVENUE_USD_2023)
    environment_index = max(0.0, attraction_health - projected_glacier_pressure / 2.0)
    resident_index = max(0.0, resident_acceptance)
    net_benefit = total_revenue - hidden_cost
    sustainability_score = 0.42 * economic_index + 0.34 * environment_index + 0.24 * resident_index

    return {
        "daily_cap": float(daily_cap),
        "visitor_fee_usd": float(visitor_fee_usd),
        "conservation_share": float(conservation_share),
        "annual_visitors": float(cap_limited_visitors),
        "business_revenue_usd": float(tourism_business_revenue),
        "fee_revenue_usd": float(fee_revenue),
        "total_revenue_usd": float(total_revenue),
        "hidden_cost_usd": float(hidden_cost),
        "net_benefit_usd": float(net_benefit),
        "conservation_spend_usd": float(conservation_spend),
        "infrastructure_spend_usd": float(infrastructure_spend),
        "community_spend_usd": float(community_spend),
        "projected_glacier_recession_fields_per_year": float(projected_glacier_pressure),
        "economic_index": float(economic_index),
        "environment_index": float(environment_index),
        "resident_acceptance_index": float(resident_index),
        "sustainability_score": float(sustainability_score),
    }


def build_policy_grid() -> pd.DataFrame:
    rows = []
    for daily_cap in range(10_000, 20_001, 500):
        for visitor_fee in range(0, 51, 5):
            for conservation_share in np.round(np.linspace(0.20, 0.60, 9), 2):
                rows.append(evaluate_policy(daily_cap, float(visitor_fee), float(conservation_share)))
    return pd.DataFrame(rows)


def summarize_policy(row: pd.Series) -> dict[str, object]:
    keys = [
        "daily_cap",
        "visitor_fee_usd",
        "conservation_share",
        "annual_visitors",
        "business_revenue_usd",
        "fee_revenue_usd",
        "total_revenue_usd",
        "hidden_cost_usd",
        "net_benefit_usd",
        "conservation_spend_usd",
        "infrastructure_spend_usd",
        "community_spend_usd",
        "projected_glacier_recession_fields_per_year",
        "economic_index",
        "environment_index",
        "resident_acceptance_index",
        "sustainability_score",
    ]
    out = {}
    for key in keys:
        value = row[key]
        if key in {"daily_cap"}:
            out[key] = int(round(value))
        elif key in {"annual_visitors"}:
            out[key] = int(round(value))
        elif key.endswith("usd"):
            out[key] = clean_float(value, 2)
        else:
            out[key] = clean_float(value)
    out["visitors_per_resident"] = clean_float(out["annual_visitors"] / JUNEAU_POPULATION, 3)
    return out


def sustainability_analysis(grid: pd.DataFrame) -> dict[str, object]:
    baseline = summarize_policy(pd.Series(evaluate_policy(BASELINE_DAILY_CAP, BASELINE_VISITOR_FEE, BASELINE_CONSERVATION_SHARE)))
    feasible = grid[
        (grid["annual_visitors"] >= 0.72 * ANNUAL_CRUISE_PASSENGERS_2023)
        & (grid["resident_acceptance_index"] >= 0.55)
        & (grid["environment_index"] >= 0.45)
        & (grid["total_revenue_usd"] >= 0.80 * TOURISM_REVENUE_USD_2023)
    ].copy()
    if feasible.empty:
        feasible = grid.copy()
    optimal = feasible.sort_values(["sustainability_score", "net_benefit_usd"], ascending=False).iloc[0]
    frontier = grid.sort_values("sustainability_score", ascending=False).head(12)
    return {
        "objective": "maximize weighted sustainability score subject to minimum revenue, resident acceptance, attraction health, and feasible visitor volume",
        "baseline": baseline,
        "optimal_policy": summarize_policy(optimal),
        "frontier_policies": [summarize_policy(row) for _, row in frontier.iterrows()],
        "expenditure_plan": {
            "conservation": "fund glacier trail protection, visitor dispersal to whale watching/rain forest sites, and ecological monitoring",
            "infrastructure": "water, waste, dock scheduling, shuttle electrification, and queue management",
            "community": "resident dividend/community grants, seasonal worker housing mitigation, and visitor behavior enforcement",
        },
    }


def sensitivity_analysis(grid: pd.DataFrame) -> dict[str, object]:
    variables = ["daily_cap", "visitor_fee_usd", "conservation_share", "annual_visitors", "fee_revenue_usd", "hidden_cost_usd"]
    rows = []
    for var in variables:
        corr = grid[[var, "sustainability_score"]].corr().iloc[0, 1]
        q_low = grid[var].quantile(0.1)
        q_high = grid[var].quantile(0.9)
        low_score = grid.loc[(grid[var] - q_low).abs().idxmin(), "sustainability_score"]
        high_score = grid.loc[(grid[var] - q_high).abs().idxmin(), "sustainability_score"]
        rows.append(
            {
                "factor": var,
                "correlation_with_score": clean_float(corr),
                "score_change_from_p10_to_p90": clean_float(high_score - low_score),
                "interpretation": sensitivity_interpretation(var, corr),
            }
        )
    rows = sorted(rows, key=lambda item: abs(item["correlation_with_score"]), reverse=True)
    return {
        "method": "correlation and 10th-to-90th percentile score shift over deterministic policy grid",
        "top_factors": rows,
    }


def sensitivity_interpretation(var: str, corr: float) -> str:
    direction = "raises" if corr > 0 else "reduces"
    descriptions = {
        "daily_cap": "daily crowding pressure and maximum seasonal volume",
        "visitor_fee_usd": "added revenue and price response",
        "conservation_share": "fee allocation toward attraction health",
        "annual_visitors": "volume after cap and fee response",
        "fee_revenue_usd": "funds available for mitigation",
        "hidden_cost_usd": "infrastructure, crowding, and carbon burden",
    }
    return f"{descriptions[var]} {direction} the score in this grid."


def destination_adaptation(optimal: dict[str, object]) -> dict[str, object]:
    barcelona_population = 1_620_000
    visitor_pressure_ratio = optimal["annual_visitors"] / JUNEAU_POPULATION
    scaled_district_visitors = int(round(visitor_pressure_ratio * 180_000))
    return {
        "destination": "Barcelona overtourism district",
        "reason_for_choice": "It has concentrated visitor pressure, resident crowding complaints, and a need to redirect tourists to less saturated attractions; the same model structure applies with different constraints.",
        "adapted_constraints": {
            "resident_population_reference": barcelona_population,
            "district_level_planning_population": 180_000,
            "recommended_annual_visitor_target_for_district": scaled_district_visitors,
            "key_changed_weight": "resident acceptance receives higher weight than glacier/attraction health; cultural-site crowding replaces glacier recession.",
        },
        "policy_transfer": [
            "replace cruise daily cap with timed-entry caps at saturated districts",
            "replace glacier conservation fund with cultural-site maintenance and transit dispersal fund",
            "use fees to promote under-visited neighborhoods through transit passes and bundled tickets",
        ],
    }


def tourism_board_memo(analysis: dict[str, object], sensitivity: dict[str, object], adaptation: dict[str, object]) -> str:
    opt = analysis["optimal_policy"]
    base = analysis["baseline"]
    top = sensitivity["top_factors"][0]
    return (
        "To the Juneau Tourism Board:\n\n"
        "Using the official problem-statement values for Juneau, the baseline is 1.6 million annual cruise passengers, "
        "about 53 visitors per resident, and busiest days near 20,000 visitors. The model recommends keeping tourism economically viable "
        f"while lowering peak pressure: daily cap {opt['daily_cap']}, visitor fee ${opt['visitor_fee_usd']}, and conservation share {opt['conservation_share']}. "
        f"This policy produces about {opt['annual_visitors']:,} annual visitors, total revenue ${opt['total_revenue_usd']:,.0f}, "
        f"and a sustainability score of {opt['sustainability_score']}, compared with the baseline score {base['sustainability_score']}. "
        f"The most influential factor in the grid is {top['factor']}, so enforcement of caps and fee-funded mitigation should receive the most attention.\n\n"
        "Spend new fee revenue on glacier and trail conservation, water/waste/dock infrastructure, electric shuttles, and community programs. "
        "The same framework can be transferred to other overtourism locations such as Barcelona by replacing glacier health with cultural-site crowding "
        "and using timed-entry plus visitor dispersal.\n\n"
        "Recommendation: adopt a moderate cap-fee package, publish transparent annual indicators, and reserve enough fee revenue for visible resident benefits."
    )


def write_artifacts(grid: pd.DataFrame, result: dict[str, object]) -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    grid.to_csv(ARTIFACT_DIR / "policy_grid.csv", index=False, encoding="utf-8-sig")
    pd.DataFrame(result["sensitivity_analysis"]["top_factors"]).to_csv(ARTIFACT_DIR / "sensitivity.csv", index=False, encoding="utf-8-sig")
    pd.DataFrame(result["sustainability_model"]["frontier_policies"]).to_csv(
        ARTIFACT_DIR / "frontier_policies.csv", index=False, encoding="utf-8-sig"
    )

    fig, ax = plt.subplots(figsize=(8.5, 5.2))
    scatter = ax.scatter(
        grid["annual_visitors"] / 1_000_000,
        grid["total_revenue_usd"] / 1_000_000,
        c=grid["sustainability_score"],
        cmap="viridis",
        s=22,
        alpha=0.72,
    )
    opt = result["sustainability_model"]["optimal_policy"]
    ax.scatter([opt["annual_visitors"] / 1_000_000], [opt["total_revenue_usd"] / 1_000_000], color="#d62828", s=90, label="recommended policy")
    ax.set_title("Juneau tourism policy frontier")
    ax.set_xlabel("Annual visitors (millions)")
    ax.set_ylabel("Total tourism + fee revenue (million USD)")
    ax.grid(alpha=0.25)
    ax.legend(loc="best")
    fig.colorbar(scatter, ax=ax, label="Sustainability score")
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "tourism_policy_frontier.png", dpi=180)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(8, 4.8))
    sens = pd.DataFrame(result["sensitivity_analysis"]["top_factors"])
    ax.barh(sens["factor"], sens["correlation_with_score"], color="#3a6ea5")
    ax.axvline(0, color="black", linewidth=1)
    ax.set_title("Sensitivity of sustainability score")
    ax.set_xlabel("Correlation with score")
    ax.grid(axis="x", alpha=0.25)
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "sensitivity_tornado.png", dpi=180)
    plt.close(fig)


def write_report(result: dict[str, object]) -> None:
    opt = result["sustainability_model"]["optimal_policy"]
    base = result["sustainability_model"]["baseline"]
    lines = [
        "# 2025 MCM-B Sustainable Tourism 题面参数实验报告",
        "",
        "## 数据来源",
        f"- 官方 PDF：`{result['data_source']['source_pdf']}`。",
        "- 本题没有独立 CSV/XLSX 附件；模型只使用题面给出的朱诺人口、游客量、峰值游客、收入和冰川退缩参数，并把其他参数作为显式假设。",
        "",
        "## Q1 朱诺可持续旅游模型",
        f"- 基线游客/居民比：{base['annual_visitors'] / JUNEAU_POPULATION:.2f}。",
        f"- 推荐日上限：{opt['daily_cap']}，游客费：{opt['visitor_fee_usd']} USD，保护支出比例：{opt['conservation_share']}。",
        f"- 推荐方案年度游客：{opt['annual_visitors']}；总收入：{opt['total_revenue_usd']} USD；可持续得分：{opt['sustainability_score']}。",
        "",
        "## 敏感性分析",
        "| factor | correlation_with_score | score_change_p10_p90 | interpretation |",
        "|---|---:|---:|---|",
    ]
    for row in result["sensitivity_analysis"]["top_factors"]:
        lines.append(f"| {row['factor']} | {row['correlation_with_score']} | {row['score_change_from_p10_to_p90']} | {row['interpretation']} |")
    lines.extend(
        [
            "",
            "## Q2 迁移到其他过度旅游目的地",
            f"- 目的地：{result['destination_adaptation']['destination']}。",
            f"- 迁移原因：{result['destination_adaptation']['reason_for_choice']}。",
            "- 政策迁移：" + "; ".join(result['destination_adaptation']['policy_transfer']),
            "",
            "## Q3 给朱诺旅游委员会备忘录",
            result["tourism_board_memo"],
            "",
            "## 输出文件",
            f"- `result.json`：{RESULT_PATH}",
            f"- `policy_grid.csv`：{ARTIFACT_DIR / 'policy_grid.csv'}",
            f"- `frontier_policies.csv`：{ARTIFACT_DIR / 'frontier_policies.csv'}",
            f"- `sensitivity.csv`：{ARTIFACT_DIR / 'sensitivity.csv'}",
            f"- `tourism_policy_frontier.png`：{ARTIFACT_DIR / 'tourism_policy_frontier.png'}",
        ]
    )
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    if not PDF_PATH.exists():
        raise FileNotFoundError(f"missing official statement PDF: {PDF_PATH}")
    grid = build_policy_grid()
    sustainability = sustainability_analysis(grid)
    sensitivity = sensitivity_analysis(grid)
    adaptation = destination_adaptation(sustainability["optimal_policy"])
    memo = tourism_board_memo(sustainability, sensitivity, adaptation)
    result = {
        "problem_id": "2025-B",
        "data_source": {
            "type": "official_statement_parameters",
            "root": str(PDF_PATH.parent),
            "source_pdf": str(PDF_PATH),
            "parameters": official_parameters(),
            "assumptions": scenario_assumptions(),
        },
        "model_features": [
            "daily_cap",
            "visitor_fee_usd",
            "conservation_share",
            "annual_visitors",
            "total_revenue_usd",
            "hidden_cost_usd",
            "environment_index",
            "resident_acceptance_index",
        ],
        "sustainability_model": sustainability,
        "sensitivity_analysis": sensitivity,
        "destination_adaptation": adaptation,
        "tourism_board_memo": memo,
    }
    write_artifacts(grid, result)
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_report(result)
    print(f"wrote {RESULT_PATH}")
    print(f"wrote {REPORT_PATH}")
    print(f"wrote artifacts under {ARTIFACT_DIR}")


if __name__ == "__main__":
    main()
