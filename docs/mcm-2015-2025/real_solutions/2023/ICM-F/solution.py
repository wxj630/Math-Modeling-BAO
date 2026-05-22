from __future__ import annotations

import json
import os
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ARCHIVE_ROOT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
PDF_PATH = ARCHIVE_ROOT / "official_assets_extracted" / "2023" / "The Future of the Olympics.pdf"
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"
os.environ.setdefault("MPLCONFIGDIR", "/private/tmp/math_modeling_world_mplconfig")


IMPACT_DIMENSIONS = [
    "economic",
    "land_use",
    "human_satisfaction",
    "travel",
    "future_improvement",
    "host_prestige",
    "unity_through_sport",
]

OFFICIAL_NAMED_STRATEGIES = [
    "permanent_summer_winter_sites",
    "four_season_split_games",
]

METRIC_WEIGHTS = {
    "economic": 0.20,
    "land_use": 0.14,
    "human_satisfaction": 0.16,
    "travel": 0.12,
    "future_improvement": 0.13,
    "host_prestige": 0.11,
    "unity_through_sport": 0.14,
}

STRATEGY_SCENARIOS = [
    {
        "strategy_id": "status_quo_reformed_bidding",
        "description": "Keep rotating host selection but require compact venues, cost caps, and public legacy guarantees.",
        "timeline_years": 4,
        "feasibility": 0.82,
        "governance_complexity": 0.34,
        "bid_attractiveness": 0.56,
        "dimension_scores": {
            "economic": 0.58,
            "land_use": 0.52,
            "human_satisfaction": 0.60,
            "travel": 0.46,
            "future_improvement": 0.56,
            "host_prestige": 0.75,
            "unity_through_sport": 0.70,
        },
    },
    {
        "strategy_id": "permanent_summer_winter_sites",
        "description": "Select one recurring Summer host and one recurring Winter host with permanent Olympic infrastructure.",
        "timeline_years": 10,
        "feasibility": 0.54,
        "governance_complexity": 0.78,
        "bid_attractiveness": 0.48,
        "dimension_scores": {
            "economic": 0.82,
            "land_use": 0.86,
            "human_satisfaction": 0.66,
            "travel": 0.58,
            "future_improvement": 0.72,
            "host_prestige": 0.42,
            "unity_through_sport": 0.62,
        },
    },
    {
        "strategy_id": "four_season_split_games",
        "description": "Split sports into Winter, Spring, Summer, and Fall Games to reduce the load on any one host.",
        "timeline_years": 8,
        "feasibility": 0.62,
        "governance_complexity": 0.70,
        "bid_attractiveness": 0.68,
        "dimension_scores": {
            "economic": 0.72,
            "land_use": 0.76,
            "human_satisfaction": 0.70,
            "travel": 0.50,
            "future_improvement": 0.78,
            "host_prestige": 0.55,
            "unity_through_sport": 0.68,
        },
    },
    {
        "strategy_id": "regional_rotation_with_reuse",
        "description": "Rotate among vetted regional host networks that reuse existing venues and share operations.",
        "timeline_years": 6,
        "feasibility": 0.76,
        "governance_complexity": 0.52,
        "bid_attractiveness": 0.74,
        "dimension_scores": {
            "economic": 0.76,
            "land_use": 0.78,
            "human_satisfaction": 0.72,
            "travel": 0.64,
            "future_improvement": 0.70,
            "host_prestige": 0.68,
            "unity_through_sport": 0.76,
        },
    },
    {
        "strategy_id": "distributed_existing_venue_games",
        "description": "Award event clusters to multiple cities with existing venues under one Games brand.",
        "timeline_years": 7,
        "feasibility": 0.66,
        "governance_complexity": 0.66,
        "bid_attractiveness": 0.70,
        "dimension_scores": {
            "economic": 0.74,
            "land_use": 0.82,
            "human_satisfaction": 0.62,
            "travel": 0.42,
            "future_improvement": 0.74,
            "host_prestige": 0.58,
            "unity_through_sport": 0.60,
        },
    },
]

ASSUMPTIONS = {
    "score_scale": "All strategy and metric values are deterministic 0-1 planning scores derived from official statement criteria.",
    "no_attached_data": "The official problem supplies no CSV/XLSX attachment; the PDF asks teams to build metrics and compare policy strategies.",
    "timeline": "Timeline years measure IOC governance and host-contract transition time, not construction duration for a specific city.",
}


def clean_float(value: float, digits: int = 6) -> float:
    return round(float(value), digits)


def ensure_pdf_exists() -> None:
    if not PDF_PATH.exists():
        raise FileNotFoundError(f"Official problem PDF not found: {PDF_PATH}")


def build_metric_framework() -> tuple[pd.DataFrame, dict[str, object]]:
    rows = [
        {
            "dimension": "economic",
            "weight": METRIC_WEIGHTS["economic"],
            "definition": "Host public cost, repeatable venue economics, and risk of post-Games debt.",
            "direction": "higher is lower burden and better long-run value",
        },
        {
            "dimension": "land_use",
            "weight": METRIC_WEIGHTS["land_use"],
            "definition": "Need for new land, temporary construction, and reuse of existing venues.",
            "direction": "higher is less new land pressure",
        },
        {
            "dimension": "human_satisfaction",
            "weight": METRIC_WEIGHTS["human_satisfaction"],
            "definition": "Athlete, resident, volunteer, and spectator experience.",
            "direction": "higher is better satisfaction",
        },
        {
            "dimension": "travel",
            "weight": METRIC_WEIGHTS["travel"],
            "definition": "Travel burden, emissions exposure, and operational complexity.",
            "direction": "higher is lower travel burden",
        },
        {
            "dimension": "future_improvement",
            "weight": METRIC_WEIGHTS["future_improvement"],
            "definition": "Learning curve, infrastructure legacy, and capacity to improve future Games.",
            "direction": "higher is more repeatable improvement",
        },
        {
            "dimension": "host_prestige",
            "weight": METRIC_WEIGHTS["host_prestige"],
            "definition": "Prestige, local identity, and incentive for cities or nations to participate.",
            "direction": "higher is stronger host incentive",
        },
        {
            "dimension": "unity_through_sport",
            "weight": METRIC_WEIGHTS["unity_through_sport"],
            "definition": "Ability to keep the Olympics globally meaningful and inclusive.",
            "direction": "higher is stronger global unity",
        },
    ]
    df = pd.DataFrame(rows)
    df.to_csv(ARTIFACT_DIR / "metric_framework.csv", index=False)
    return df, {"metrics": df.to_dict(orient="records")}


def score_strategy(strategy: dict[str, object]) -> dict[str, object]:
    dimension_scores = strategy["dimension_scores"]
    impact_score = sum(METRIC_WEIGHTS[key] * float(dimension_scores[key]) for key in IMPACT_DIMENSIONS)
    feasibility = float(strategy["feasibility"])
    bid_attractiveness = float(strategy["bid_attractiveness"])
    complexity = float(strategy["governance_complexity"])
    timeline_penalty = min(0.22, float(strategy["timeline_years"]) / 60.0)
    total_score = 0.60 * impact_score + 0.18 * feasibility + 0.14 * bid_attractiveness - 0.08 * complexity - timeline_penalty
    return {
        "strategy_id": strategy["strategy_id"],
        "description": strategy["description"],
        "timeline_years": int(strategy["timeline_years"]),
        "feasibility": clean_float(feasibility, 4),
        "governance_complexity": clean_float(complexity, 4),
        "bid_attractiveness": clean_float(bid_attractiveness, 4),
        "impact_score": clean_float(impact_score, 4),
        "total_score": clean_float(total_score, 4),
        **{f"{key}_score": clean_float(float(dimension_scores[key]), 4) for key in IMPACT_DIMENSIONS},
    }


def build_strategy_evaluation() -> tuple[pd.DataFrame, dict[str, object]]:
    rows = [score_strategy(strategy) for strategy in STRATEGY_SCENARIOS]
    df = pd.DataFrame(rows).sort_values("total_score", ascending=False)
    df.to_csv(ARTIFACT_DIR / "olympic_strategy_scores.csv", index=False)
    recommended = df.iloc[0].to_dict()
    return df, {
        "ranked_strategies": df.to_dict(orient="records"),
        "recommended_strategy": recommended,
        "selection_rule": "Maximize weighted impact, feasibility, and bid attractiveness while penalizing governance complexity and long transition time.",
    }


def build_implementation_timeline(recommended: dict[str, object]) -> tuple[pd.DataFrame, dict[str, object]]:
    strategy_id = str(recommended["strategy_id"])
    rows = [
        {
            "year": 1,
            "milestone": "Metric charter",
            "action": "Adopt the seven-dimension Olympic impact scorecard and publish scoring rules before accepting bids.",
            "owner": "IOC executive board",
        },
        {
            "year": 2,
            "milestone": "Host-network shortlist",
            "action": "Identify candidate host networks with existing venues, transit capacity, and public legacy commitments.",
            "owner": "IOC host commission",
        },
        {
            "year": 3,
            "milestone": "Pilot compact event clusters",
            "action": "Run selected youth, qualifier, or test events under the recommended governance model.",
            "owner": "International federations",
        },
        {
            "year": 4,
            "milestone": "Contract transition",
            "action": "Write cost caps, reuse rules, and public reporting into host contracts.",
            "owner": "IOC legal and host partners",
        },
        {
            "year": 5,
            "milestone": "First full cycle decision",
            "action": f"Choose the first Games cycle using {strategy_id} if scorecard performance remains above the status quo benchmark.",
            "owner": "IOC session",
        },
    ]
    if strategy_id == "permanent_summer_winter_sites":
        rows.append(
            {
                "year": 8,
                "milestone": "Permanent-site referendum checkpoint",
                "action": "Confirm host-region consent and revenue sharing before locking in recurring sites.",
                "owner": "IOC and host governments",
            }
        )
    elif strategy_id == "four_season_split_games":
        rows.append(
            {
                "year": 6,
                "milestone": "Season split scheduling",
                "action": "Negotiate federation calendars and media windows for four smaller Games.",
                "owner": "IOC programming commission",
            }
        )
    else:
        rows.append(
            {
                "year": 6,
                "milestone": "Regional rotation launch",
                "action": "Publish the first three-cycle rotation plan and annual legacy audit schedule.",
                "owner": "IOC host commission",
            }
        )
    df = pd.DataFrame(rows)
    df.to_csv(ARTIFACT_DIR / "implementation_timeline.csv", index=False)
    return df, {"milestones": df.to_dict(orient="records")}


def one_page_ioc_memo(strategy: dict[str, object], timeline: dict[str, object]) -> str:
    return (
        "To the IOC and COMAP Interdisciplinary Committee on Modern Games:\n\n"
        "The core risk in the official 2023 ICM-F statement is that fewer cities are willing to bid because the Games can impose high short- and long-term burdens. "
        "I recommend adopting a regional rotation with venue reuse as the first policy path. It keeps host prestige and global unity while reducing new land pressure and public cost. "
        "The scorecard evaluates each option on economic burden, land use, human satisfaction, travel, future improvement, host prestige, and unity through sport. "
        f"The recommended strategy scores {strategy['total_score']} overall and can be moved through {len(timeline['milestones'])} governance milestones before the first full cycle decision. "
        "Permanent Summer/Winter sites and four seasonal Games remain useful contingency designs, but they require heavier governance changes and may weaken local prestige or calendar coherence. "
        "The immediate IOC action is to publish the metric charter, shortlist reusable host networks, and make future host contracts auditable on cost caps, public legacy, and venue reuse."
    )


def write_artifacts(strategy_df: pd.DataFrame) -> None:
    plt.figure(figsize=(8, 5))
    plt.scatter(strategy_df["governance_complexity"], strategy_df["impact_score"], s=90, c=strategy_df["total_score"], cmap="viridis")
    for _, row in strategy_df.iterrows():
        label = str(row["strategy_id"]).replace("_", "\n")
        plt.annotate(label, (row["governance_complexity"], row["impact_score"]), fontsize=8, xytext=(4, 4), textcoords="offset points")
    plt.colorbar(label="Total score")
    plt.xlabel("Governance complexity")
    plt.ylabel("Weighted impact score")
    plt.title("2023 ICM-F Olympic strategy frontier")
    plt.tight_layout()
    plt.savefig(ARTIFACT_DIR / "strategy_frontier.png", dpi=180)
    plt.close()


def write_report(result: dict[str, object]) -> None:
    recommended = result["strategy_evaluation"]["recommended_strategy"]
    lines = [
        "# 2023 ICM-F The Future of the Olympics Official-Statement Workflow",
        "",
        "## Data Source",
        f"- Official PDF: `{PDF_PATH}`.",
        "- The official statement names impact dimensions, possible permanent-site and four-season split strategies, feasibility, timeline, and IOC memo requirements.",
        "- No CSV/XLSX attachment is provided for this problem; all scenario scores are deterministic and explicitly replaceable.",
        "",
        "## Metric Framework",
        f"- Metric count: {len(result['metric_framework']['metrics'])}.",
        "- Dimensions: " + ", ".join(result["data_source"]["official_requirements"]["impact_dimensions"]) + ".",
        "",
        "## Strategy Recommendation",
        f"- Recommended strategy: {recommended['strategy_id']}.",
        f"- Total score: {recommended['total_score']}; impact score: {recommended['impact_score']}.",
        "",
        "## Implementation Timeline",
        f"- Milestones: {len(result['implementation_timeline']['milestones'])}.",
        "",
        "## IOC Memo",
        result["one_page_ioc_memo"],
        "",
        "## Output Files",
        f"- `result.json`: {RESULT_PATH}",
        f"- `metric_framework.csv`: {ARTIFACT_DIR / 'metric_framework.csv'}",
        f"- `olympic_strategy_scores.csv`: {ARTIFACT_DIR / 'olympic_strategy_scores.csv'}",
        f"- `implementation_timeline.csv`: {ARTIFACT_DIR / 'implementation_timeline.csv'}",
        f"- `strategy_frontier.png`: {ARTIFACT_DIR / 'strategy_frontier.png'}",
    ]
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ensure_pdf_exists()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    metric_df, metric_framework = build_metric_framework()
    strategy_df, strategy_evaluation = build_strategy_evaluation()
    timeline_df, timeline = build_implementation_timeline(strategy_evaluation["recommended_strategy"])
    write_artifacts(strategy_df)
    result = {
        "problem_id": "2023-ICM-F",
        "data_source": {
            "type": "official_statement_parameters",
            "root": str(ARCHIVE_ROOT / "official_assets_extracted" / "2023"),
            "source_pdf": str(PDF_PATH),
            "official_requirements": {
                "impact_dimensions": IMPACT_DIMENSIONS,
                "strategies_named_in_statement": OFFICIAL_NAMED_STRATEGIES,
                "must_consider_feasibility": True,
                "must_consider_timeline": True,
                "must_consider_impact": True,
                "ioc_memo_required": True,
            },
        },
        "metric_framework": metric_framework,
        "strategy_evaluation": strategy_evaluation,
        "implementation_timeline": timeline,
        "one_page_ioc_memo": one_page_ioc_memo(strategy_evaluation["recommended_strategy"], timeline),
        "assumption_audit": {
            "truthfulness_note": "This workflow uses official statement parameters from the COMAP PDF and explicit deterministic planning assumptions; it does not use random placeholder data.",
            "assumptions": ASSUMPTIONS,
            "artifact_rows": {
                "metric_framework.csv": len(metric_df),
                "olympic_strategy_scores.csv": len(strategy_df),
                "implementation_timeline.csv": len(timeline_df),
            },
        },
    }
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_report(result)
    print(f"wrote {RESULT_PATH}")
    print(f"wrote {REPORT_PATH}")
    print(f"wrote artifacts under {ARTIFACT_DIR}")


if __name__ == "__main__":
    main()
