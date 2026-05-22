from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd


ARCHIVE_ROOT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
PDF_PATH = ARCHIVE_ROOT / "official_assets_extracted" / "2023" / "Prioritizing the UN Sustainability Goals.pdf"
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"

SDG_COUNT = 17
TEN_YEAR_HORIZON = 10

SDGS = [
    (1, "No Poverty", "social"),
    (2, "Zero Hunger", "social"),
    (3, "Good Health and Well-being", "social"),
    (4, "Quality Education", "social"),
    (5, "Gender Equality", "social"),
    (6, "Clean Water and Sanitation", "environment"),
    (7, "Affordable and Clean Energy", "infrastructure"),
    (8, "Decent Work and Economic Growth", "economic"),
    (9, "Industry, Innovation and Infrastructure", "infrastructure"),
    (10, "Reduced Inequality", "social"),
    (11, "Sustainable Cities and Communities", "infrastructure"),
    (12, "Responsible Consumption and Production", "environment"),
    (13, "Climate Action", "environment"),
    (14, "Life Below Water", "environment"),
    (15, "Life on Land", "environment"),
    (16, "Peace and Justice Strong Institutions", "governance"),
    (17, "Partnerships to achieve the Goal", "governance"),
]

OFFICIAL_STATEMENT_PARAMETERS = {
    "sdg_count": SDG_COUNT,
    "ten_year_horizon": TEN_YEAR_HORIZON,
    "source_reference": "Transforming Our World: The 2030 Agenda for Sustainable Development, UN General Assembly, A/RES/70/1, 2015",
    "requirements": [
        "create a network of relationships between the 17 SDGs",
        "use individual SDGs and network structure to set priorities",
        "evaluate priority effectiveness and 10-year achievability",
        "analyze resulting network if one SDG is achieved",
        "discuss whether other goals should be proposed",
        "analyze technology, pandemics, climate change, regional wars, refugees, or other crises",
        "explain how the network approach helps other organizations set priorities",
    ],
    "source_note": "Official PDF statement parameters only; edge weights and crisis multipliers are deterministic scenario assumptions, not observed UN indicator data.",
}

BASE_EDGES = [
    (1, 2, 0.72, "poverty reduction improves food security"),
    (1, 3, 0.66, "income access improves health"),
    (1, 4, 0.60, "poverty reduction keeps children in school"),
    (1, 8, 0.63, "poverty and decent work reinforce each other"),
    (1, 10, 0.74, "poverty reduction reduces inequality"),
    (2, 3, 0.69, "nutrition improves health"),
    (2, 6, 0.54, "water quality supports food systems"),
    (2, 12, 0.50, "sustainable consumption affects food systems"),
    (2, 15, 0.55, "land ecosystems support agriculture"),
    (3, 4, 0.58, "health improves learning"),
    (3, 5, 0.47, "health access affects gender outcomes"),
    (3, 6, 0.61, "clean water reduces disease"),
    (3, 11, 0.45, "urban design affects health"),
    (4, 5, 0.70, "education promotes gender equality"),
    (4, 8, 0.62, "skills support employment"),
    (4, 9, 0.48, "education supports innovation"),
    (4, 16, 0.42, "education supports institutions"),
    (5, 8, 0.52, "gender equality expands labor participation"),
    (5, 10, 0.66, "gender equity reduces inequality"),
    (6, 11, 0.55, "water and sanitation support cities"),
    (6, 14, 0.52, "water treatment protects oceans"),
    (6, 15, 0.46, "water systems support terrestrial ecosystems"),
    (7, 8, 0.59, "energy access supports economic activity"),
    (7, 9, 0.67, "energy and infrastructure co-develop"),
    (7, 12, 0.50, "clean energy supports responsible production"),
    (7, 13, 0.71, "clean energy mitigates climate change"),
    (8, 9, 0.56, "economic growth supports infrastructure"),
    (8, 10, 0.44, "inclusive growth reduces inequality"),
    (8, 12, -0.32, "growth can increase resource pressure without safeguards"),
    (9, 11, 0.58, "infrastructure supports sustainable cities"),
    (9, 13, 0.38, "innovation can support climate mitigation"),
    (10, 11, 0.49, "reduced inequality improves urban inclusion"),
    (10, 16, 0.53, "less inequality supports stable institutions"),
    (11, 12, 0.51, "cities drive consumption systems"),
    (11, 13, 0.46, "urban resilience supports climate action"),
    (12, 13, 0.57, "responsible production reduces emissions"),
    (12, 14, 0.62, "waste reduction protects oceans"),
    (12, 15, 0.60, "resource stewardship protects land"),
    (13, 14, 0.64, "climate action protects oceans"),
    (13, 15, 0.66, "climate action protects land"),
    (14, 15, 0.37, "ecosystem protection has cross-biome spillovers"),
    (16, 17, 0.76, "institutions enable partnerships"),
    (17, 1, 0.50, "partnerships finance poverty programs"),
    (17, 6, 0.46, "partnerships support water projects"),
    (17, 13, 0.52, "partnerships coordinate climate action"),
]

CRISES = [
    {"crisis": "technological advances", "targets": [4, 7, 8, 9, 17], "effect": 0.16, "risk": "digital divide can widen inequality"},
    {"crisis": "global pandemic", "targets": [1, 2, 3, 4, 8, 10], "effect": -0.20, "risk": "health shock disrupts education and work"},
    {"crisis": "climate change", "targets": [2, 6, 11, 13, 14, 15], "effect": -0.24, "risk": "ecosystem and water stress cascades"},
    {"crisis": "regional wars", "targets": [1, 2, 3, 8, 16, 17], "effect": -0.22, "risk": "institutions and partnerships are strained"},
    {"crisis": "refugee movements", "targets": [1, 3, 4, 10, 11, 16], "effect": -0.14, "risk": "service demand rises in destination communities"},
]


def clean_float(value: float, digits: int = 6) -> float:
    return round(float(value), digits)


def ensure_pdf_exists() -> None:
    if not PDF_PATH.exists():
        raise FileNotFoundError(f"Official problem PDF not found: {PDF_PATH}")


def build_graph() -> tuple[nx.DiGraph, pd.DataFrame, dict[str, object]]:
    graph = nx.DiGraph()
    for number, name, category in SDGS:
        graph.add_node(number, name=f"SDG {number}: {name}", category=category)
    rows = []
    for source, target, weight, rationale in BASE_EDGES:
        graph.add_edge(source, target, weight=weight, rationale=rationale)
        rows.append({"source_sdg": source, "target_sdg": target, "weight": weight, "relationship": rationale, "sign": "positive" if weight >= 0 else "negative"})
    edge_df = pd.DataFrame(rows)
    edge_df.to_csv(ARTIFACT_DIR / "sdg_network_edges.csv", index=False)
    plt.figure(figsize=(9, 7))
    pos = nx.spring_layout(graph, seed=17, weight="weight")
    colors = ["#4C78A8" if graph.nodes[n]["category"] == "social" else "#59A14F" if graph.nodes[n]["category"] == "environment" else "#F28E2B" if graph.nodes[n]["category"] == "infrastructure" else "#B07AA1" if graph.nodes[n]["category"] == "governance" else "#E15759" for n in graph.nodes]
    nx.draw_networkx_nodes(graph, pos, node_color=colors, node_size=720, alpha=0.9)
    nx.draw_networkx_labels(graph, pos, labels={n: str(n) for n in graph.nodes}, font_size=9, font_color="white")
    positive = [(u, v) for u, v, d in graph.edges(data=True) if d["weight"] >= 0]
    negative = [(u, v) for u, v, d in graph.edges(data=True) if d["weight"] < 0]
    nx.draw_networkx_edges(graph, pos, edgelist=positive, alpha=0.33, arrowsize=10, edge_color="#555555")
    nx.draw_networkx_edges(graph, pos, edgelist=negative, alpha=0.75, arrowsize=12, edge_color="#D62728", style="dashed")
    plt.title("Official 17-SDG relationship network scenario")
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(ARTIFACT_DIR / "sdg_priority_network.png", dpi=180)
    plt.close()
    return graph, edge_df, {
        "model": "directed weighted SDG influence network based on official 17-goal list and transparent scenario edges",
        "nodes": [{"sdg": number, "name": name, "category": category} for number, name, category in SDGS],
        "sdg_network_edges": edge_df.to_dict(orient="records"),
        "negative_tradeoff_count": int((edge_df["weight"] < 0).sum()),
    }


def build_priorities(graph: nx.DiGraph) -> dict[str, object]:
    pagerank = nx.pagerank(graph, weight="weight")
    betweenness = nx.betweenness_centrality(graph, weight="weight", normalized=True)
    out_strength = {n: sum(abs(d["weight"]) for _, _, d in graph.out_edges(n, data=True)) for n in graph.nodes}
    incoming_support = {n: sum(max(0.0, d["weight"]) for _, _, d in graph.in_edges(n, data=True)) for n in graph.nodes}
    rows = []
    for number, name, category in SDGS:
        direct_need = 0.64 if category == "social" else 0.58 if category == "environment" else 0.54 if category == "governance" else 0.50
        leverage = 0.34 * pagerank[number] / max(pagerank.values()) + 0.28 * betweenness[number] / max(betweenness.values() or [1]) + 0.24 * out_strength[number] / max(out_strength.values()) + 0.14 * incoming_support[number] / max(incoming_support.values())
        priority_score = 0.55 * leverage + 0.45 * direct_need
        rows.append({"sdg": number, "name": name, "category": category, "pagerank": clean_float(pagerank[number], 5), "betweenness": clean_float(betweenness[number], 5), "out_strength": clean_float(out_strength[number], 4), "direct_need_index": direct_need, "priority_score": clean_float(priority_score, 4)})
    ranking = pd.DataFrame(rows).sort_values("priority_score", ascending=False)
    ranking.to_csv(ARTIFACT_DIR / "priority_ranking.csv", index=False)
    top = ranking.head(5).to_dict(orient="records")
    ten_year_gain = sum(row["priority_score"] for row in top) / len(top) * 0.42
    return {
        "method": "priority = 55% network leverage + 45% direct human/environment need",
        "priority_ranking": ranking.to_dict(orient="records"),
        "ten_year_plan": {
            "years": TEN_YEAR_HORIZON,
            "first_wave_priorities": [row["sdg"] for row in top],
            "expected_network_progress_gain": clean_float(ten_year_gain, 4),
            "evaluation_metric": "weighted reachable influence from funded priority goals, discounted by governance feasibility",
        },
    }


def build_achieved_goal_scenario(graph: nx.DiGraph, priority_model: dict[str, object]) -> dict[str, object]:
    achieved_goal = 1
    scenario = graph.copy()
    for successor in list(scenario.successors(achieved_goal)):
        scenario[achieved_goal][successor]["weight"] *= 0.55
    for predecessor in list(scenario.predecessors(achieved_goal)):
        scenario[predecessor][achieved_goal]["weight"] *= 0.35
    scenario.add_node(18, name="SDG 18: Digital Public Trust and Resilience", category="governance")
    scenario.add_edge(18, 4, weight=0.45, rationale="digital trust improves education access")
    scenario.add_edge(18, 9, weight=0.52, rationale="trusted digital systems support innovation")
    scenario.add_edge(18, 16, weight=0.49, rationale="digital public trust supports institutions")
    pr = nx.pagerank(scenario, weight="weight")
    rows = []
    for node, value in sorted(pr.items(), key=lambda item: item[1], reverse=True):
        rows.append({"sdg": node, "name": scenario.nodes[node]["name"], "post_achievement_pagerank": clean_float(value, 5)})
    df = pd.DataFrame(rows)
    df.to_csv(ARTIFACT_DIR / "achieved_goal_network_priorities.csv", index=False)
    return {
        "achieved_goal": achieved_goal,
        "scenario": "SDG 1 No Poverty achieved, so poverty-centered incoming dependencies fall and downstream support becomes maintenance rather than emergency relief.",
        "resulting_network_priorities": rows[:10],
        "proposed_new_goal": {"sdg": 18, "name": "Digital Public Trust and Resilience", "reason": "Technology and crisis governance appear repeatedly in the official prompt but are not represented as a standalone SDG."},
    }


def build_crisis_impacts(priority_model: dict[str, object]) -> dict[str, object]:
    top_scores = {row["sdg"]: row["priority_score"] for row in priority_model["priority_ranking"]}
    rows = []
    for crisis in CRISES:
        exposed_priority = sum(top_scores[sdg] for sdg in crisis["targets"] if sdg in top_scores)
        severity = abs(crisis["effect"]) * exposed_priority / len(crisis["targets"])
        response_goals = sorted(crisis["targets"], key=lambda sdg: top_scores.get(sdg, 0), reverse=True)[:3]
        rows.append({"crisis": crisis["crisis"], "affected_sdgs": ",".join(str(s) for s in crisis["targets"]), "effect_direction": "positive" if crisis["effect"] > 0 else "negative", "network_severity_index": clean_float(severity, 4), "priority_response_sdgs": ",".join(str(s) for s in response_goals), "risk": crisis["risk"]})
    df = pd.DataFrame(rows).sort_values("network_severity_index", ascending=False)
    df.to_csv(ARTIFACT_DIR / "crisis_impact_matrix.csv", index=False)
    return {
        "method": "overlay official crisis categories onto priority-weighted SDG network exposure",
        "crisis_impact_matrix": df.to_dict(orient="records"),
        "network_perspective": "Crises matter most when they hit bridge goals such as health, education, institutions, partnerships, climate, and inequality at the same time.",
    }


def build_organization_transfer() -> dict[str, object]:
    return {
        "model": "goal-network portfolio prioritization",
        "adaptation_steps": [
            "list organizational goals as nodes and define positive or negative dependencies as weighted edges",
            "score each goal using centrality, direct mission need, feasibility, and risk exposure",
            "fund a small first-wave portfolio of bridge goals instead of isolated high-visibility goals",
            "rerun the network after a goal is achieved or after a crisis changes edge weights",
            "publish tradeoff edges so stakeholders can see where progress on one objective may slow another",
        ],
        "use_cases": ["corporate ESG portfolio", "public health agency strategy", "university sustainability plan", "NGO grant allocation"],
    }


def write_report(result: dict[str, object]) -> None:
    top = result["priority_model"]["priority_ranking"][:5]
    lines = [
        "# 2023 ICM-D Prioritizing the UN Sustainability Goals",
        "",
        "## Official Statement Basis",
        "- Source: `Prioritizing the UN Sustainability Goals.pdf`.",
        "- Official statement lists 17 Sustainable Development Goals and asks for a relationship network, priorities, 10-year achievability, achieved-goal network changes, crisis impacts, and transfer to other organizations.",
        "- No COMAP numeric attachment is provided; edge weights and crisis multipliers are deterministic scenario assumptions.",
        "",
        "## Model",
        "- Directed weighted network over the 17 official SDGs.",
        "- Priority score combines PageRank, betweenness, outgoing influence, incoming support, and direct need.",
        "- Tutorial model references: complex networks/graph theory, comprehensive evaluation, and scenario sensitivity from `/Users/wuxiaojun/code/My-Agent/intro-mathmodel`.",
        "",
        "## Top Priorities",
    ]
    for row in top:
        lines.append(f"- SDG {row['sdg']} {row['name']}: priority score {row['priority_score']}.")
    lines.extend([
        "",
        "## Crisis Interpretation",
        result["crisis_impact_model"]["network_perspective"],
        "",
        "## Organization Transfer",
    ])
    lines.extend([f"- {item}" for item in result["organization_transfer"]["adaptation_steps"]])
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ensure_pdf_exists()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    graph, edge_df, sdg_network_model = build_graph()
    priority_model = build_priorities(graph)
    achieved_goal_scenario = build_achieved_goal_scenario(graph, priority_model)
    crisis_impact_model = build_crisis_impacts(priority_model)
    organization_transfer = build_organization_transfer()
    result = {
        "problem_id": "2023-D",
        "title": "Prioritizing the UN Sustainability Goals",
        "data_source": {
            "type": "official_statement_parameters",
            "root": str(ARCHIVE_ROOT),
            "source_pdf": str(PDF_PATH),
            "parameters": OFFICIAL_STATEMENT_PARAMETERS,
            "scenario_assumption_note": "All network edges, edge weights, direct-need indices, and crisis multipliers are transparent deterministic assumptions for a reproducible network experiment; they are not observed UN indicator data.",
        },
        "sdg_network_model": sdg_network_model,
        "priority_model": priority_model,
        "achieved_goal_scenario": achieved_goal_scenario,
        "crisis_impact_model": crisis_impact_model,
        "organization_transfer": organization_transfer,
    }
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_report(result)
    print(f"wrote {RESULT_PATH}")
    print(f"wrote {REPORT_PATH}")
    print(f"wrote artifacts under {ARTIFACT_DIR}")


if __name__ == "__main__":
    main()
