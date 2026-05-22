from __future__ import annotations

import json
import math
import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/private/tmp/matplotlib-cache")

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, balanced_accuracy_score
from sklearn.tree import DecisionTreeClassifier


ARCHIVE_ROOT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
DATA_ROOT = ARCHIVE_ROOT / "official_assets_extracted" / "2020" / "Problem Data- Teaming Strategies" / "2020_Problem_D_DATA"
PDF_PATH = ARCHIVE_ROOT / "official_assets_extracted" / "2020" / "Teaming Strategies.pdf"
MATCHES_PATH = DATA_ROOT / "matches.csv"
PASSING_PATH = DATA_ROOT / "passingevents.csv"
FULL_EVENTS_PATH = DATA_ROOT / "fullevents.csv"
README_PATH = DATA_ROOT / "README.txt"
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"
REQUIRED_ARTIFACTS = [
    ARTIFACT_DIR / "match_teamwork_features.csv",
    ARTIFACT_DIR / "passing_network_edges.csv",
    ARTIFACT_DIR / "player_centrality.csv",
    ARTIFACT_DIR / "teamwork_feature_importance.csv",
    ARTIFACT_DIR / "passing_network_top_edges.png",
]

FEATURE_COLUMNS = [
    "passes",
    "pass_advantage",
    "players_involved",
    "network_density",
    "network_reciprocity",
    "weighted_clustering",
    "pass_type_entropy",
    "top_pair_share",
    "contribution_gini",
    "average_pass_length",
    "forward_pass_share",
    "attacking_third_share",
    "shot_count",
    "duel_count",
    "foul_count",
    "home_side",
]


def clean_float(value: object, digits: int = 6) -> float | None:
    if value is None:
        return None
    value = float(value)
    if math.isnan(value) or math.isinf(value):
        return None
    return round(value, digits)


def read_official_data() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    missing = [str(path) for path in [PDF_PATH, MATCHES_PATH, PASSING_PATH, FULL_EVENTS_PATH, README_PATH] if not path.exists()]
    if missing:
        raise FileNotFoundError("missing official COMAP Teaming Strategies assets: " + ", ".join(missing))
    matches = pd.read_csv(MATCHES_PATH)
    passing = pd.read_csv(PASSING_PATH)
    full_events = pd.read_csv(FULL_EVENTS_PATH)
    return matches, passing, full_events


def player_position(player_id: object) -> str:
    text = str(player_id)
    if "_" not in text:
        return ""
    suffix = text.rsplit("_", 1)[-1]
    return suffix[:1]


def shannon_entropy(values: pd.Series) -> float:
    shares = values.dropna().value_counts(normalize=True)
    if shares.empty:
        return 0.0
    return float(-(shares * np.log(shares)).sum())


def gini(values: pd.Series | np.ndarray | list[float]) -> float:
    array = np.sort(np.asarray(values, dtype=float))
    if len(array) == 0 or array.sum() == 0:
        return 0.0
    n = len(array)
    return float((2 * np.arange(1, n + 1).dot(array)) / (n * array.sum()) - (n + 1) / n)


def weighted_pass_graph(passes: pd.DataFrame) -> nx.DiGraph:
    graph = nx.DiGraph()
    edge_counts = passes.groupby(["OriginPlayerID", "DestinationPlayerID"]).size()
    for (origin, destination), weight in edge_counts.items():
        graph.add_edge(str(origin), str(destination), weight=int(weight))
    return graph


def pass_network_tables(passing: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, dict[str, object]]:
    huskies = passing[passing["TeamID"] == "Huskies"].copy()
    graph = weighted_pass_graph(huskies)
    edge_rows = []
    for origin, destination, data in graph.edges(data=True):
        edge_rows.append(
            {
                "origin": origin,
                "destination": destination,
                "origin_position": player_position(origin),
                "destination_position": player_position(destination),
                "pass_count": int(data["weight"]),
            }
        )
    edge_table = pd.DataFrame(edge_rows).sort_values("pass_count", ascending=False)

    weighted_in = dict(graph.in_degree(weight="weight"))
    weighted_out = dict(graph.out_degree(weight="weight"))
    pagerank = nx.pagerank(graph, weight="weight")
    betweenness = nx.betweenness_centrality(graph, weight=None, normalized=True)
    centrality_rows = []
    for player in sorted(graph.nodes()):
        centrality_rows.append(
            {
                "player": player,
                "position": player_position(player),
                "weighted_out_degree": int(weighted_out.get(player, 0)),
                "weighted_in_degree": int(weighted_in.get(player, 0)),
                "pagerank": clean_float(pagerank.get(player, 0.0)),
                "betweenness": clean_float(betweenness.get(player, 0.0)),
                "teamwork_centrality": clean_float(
                    0.45 * pagerank.get(player, 0.0)
                    + 0.35 * (weighted_out.get(player, 0) / max(1, huskies.shape[0]))
                    + 0.20 * betweenness.get(player, 0.0)
                ),
            }
        )
    centrality = pd.DataFrame(centrality_rows).sort_values("teamwork_centrality", ascending=False)

    undirected = graph.to_undirected()
    summary = {
        "huskies_player_count": int(graph.number_of_nodes()),
        "huskies_pass_count": int(len(huskies)),
        "directed_edge_count": int(graph.number_of_edges()),
        "season_network_density": clean_float(nx.density(graph)),
        "season_network_reciprocity": clean_float(nx.overall_reciprocity(graph) or 0),
        "season_weighted_clustering": clean_float(nx.average_clustering(undirected, weight="weight")),
        "season_triangles": int(sum(nx.triangles(undirected).values()) // 3),
        "top_pass_pairs": edge_table.head(12).to_dict(orient="records"),
        "top_central_players": centrality.head(10).to_dict(orient="records"),
    }
    return edge_table, centrality, summary


def match_teamwork_features(matches: pd.DataFrame, passing: pd.DataFrame, full_events: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for _, match in matches.sort_values("MatchID").iterrows():
        match_id = int(match["MatchID"])
        husky_passes = passing[(passing["MatchID"] == match_id) & (passing["TeamID"] == "Huskies")].copy()
        opponent_passes = passing[(passing["MatchID"] == match_id) & (passing["TeamID"] != "Huskies")].copy()
        husky_events = full_events[(full_events["MatchID"] == match_id) & (full_events["TeamID"] == "Huskies")].copy()

        graph = weighted_pass_graph(husky_passes)
        undirected = graph.to_undirected()
        edge_counts = husky_passes.groupby(["OriginPlayerID", "DestinationPlayerID"]).size()
        pass_lengths = np.hypot(
            husky_passes["EventDestination_x"] - husky_passes["EventOrigin_x"],
            husky_passes["EventDestination_y"] - husky_passes["EventOrigin_y"],
        )
        origin_positions = husky_passes["OriginPlayerID"].map(player_position)
        pass_count = int(len(husky_passes))
        row = {
            "MatchID": match_id,
            "OpponentID": str(match["OpponentID"]),
            "Outcome": str(match["Outcome"]),
            "team_success_non_loss": int(str(match["Outcome"]) != "loss"),
            "OwnScore": int(match["OwnScore"]),
            "OpponentScore": int(match["OpponentScore"]),
            "goal_diff": int(match["OwnScore"]) - int(match["OpponentScore"]),
            "Side": str(match["Side"]),
            "CoachID": str(match["CoachID"]),
            "passes": pass_count,
            "opponent_passes": int(len(opponent_passes)),
            "pass_advantage": int(pass_count - len(opponent_passes)),
            "players_involved": int(graph.number_of_nodes()),
            "network_density": clean_float(nx.density(graph) if graph.number_of_nodes() > 1 else 0),
            "network_reciprocity": clean_float(nx.overall_reciprocity(graph) or 0),
            "weighted_clustering": clean_float(nx.average_clustering(undirected, weight="weight") if graph.number_of_nodes() > 1 else 0),
            "triadic_configurations": int(sum(nx.triangles(undirected).values()) // 3) if graph.number_of_nodes() > 2 else 0,
            "pass_type_entropy": clean_float(shannon_entropy(husky_passes["EventSubType"])),
            "top_pair_share": clean_float(edge_counts.max() / pass_count if pass_count else 0),
            "contribution_gini": clean_float(gini(husky_passes["OriginPlayerID"].value_counts().values)),
            "average_pass_length": clean_float(pass_lengths.mean() if pass_count else 0),
            "forward_pass_share": clean_float((husky_passes["EventDestination_x"] > husky_passes["EventOrigin_x"]).mean() if pass_count else 0),
            "attacking_third_share": clean_float((husky_passes["EventDestination_x"] >= 66).mean() if pass_count else 0),
            "shot_count": int((husky_events["EventType"] == "Shot").sum()),
            "duel_count": int((husky_events["EventType"] == "Duel").sum()),
            "foul_count": int((husky_events["EventType"] == "Foul").sum()),
            "home_side": int(str(match["Side"]) == "home"),
            "origin_defense_share": clean_float((origin_positions == "D").mean() if pass_count else 0),
            "origin_midfield_share": clean_float((origin_positions == "M").mean() if pass_count else 0),
            "origin_forward_share": clean_float((origin_positions == "F").mean() if pass_count else 0),
            "origin_goalkeeper_share": clean_float((origin_positions == "G").mean() if pass_count else 0),
        }
        rows.append(row)
    return pd.DataFrame(rows)


def formation_patterns(features: pd.DataFrame) -> dict[str, object]:
    by_outcome = (
        features.groupby("Outcome")
        .agg(
            matches=("MatchID", "count"),
            avg_passes=("passes", "mean"),
            avg_density=("network_density", "mean"),
            avg_reciprocity=("network_reciprocity", "mean"),
            avg_triads=("triadic_configurations", "mean"),
            avg_forward_share=("origin_forward_share", "mean"),
            avg_midfield_share=("origin_midfield_share", "mean"),
            avg_attacking_third=("attacking_third_share", "mean"),
            avg_goal_diff=("goal_diff", "mean"),
        )
        .reset_index()
    )
    for column in by_outcome.columns:
        if column != "Outcome":
            by_outcome[column] = by_outcome[column].map(lambda value: clean_float(value, 4))
    return {
        "by_outcome": by_outcome.to_dict(orient="records"),
        "scales_modeled": [
            "micro: repeated dyadic pass pairs and top-pair concentration",
            "meso: triadic configurations, weighted clustering, and position-share formations",
            "macro: season-level directed passing network density and reciprocity",
            "temporal: match-by-match features ordered across all 38 official matches",
        ],
        "time_scale_note": "MatchPeriod contains 1H/2H values; this workflow aggregates full-match features and keeps half-level fields available for minute-level extensions.",
    }


def teamwork_model(features: pd.DataFrame) -> tuple[dict[str, object], pd.DataFrame]:
    train = features[features["MatchID"] <= 30].copy()
    holdout = features[features["MatchID"] > 30].copy()
    model = DecisionTreeClassifier(max_depth=2, min_samples_leaf=3)
    model.fit(train[FEATURE_COLUMNS], train["team_success_non_loss"])
    pred = model.predict(holdout[FEATURE_COLUMNS])
    accuracy = accuracy_score(holdout["team_success_non_loss"], pred)
    balanced = balanced_accuracy_score(holdout["team_success_non_loss"], pred)
    importances = pd.DataFrame({"feature": FEATURE_COLUMNS, "importance": model.feature_importances_}).sort_values(
        "importance", ascending=False
    )
    holdout_rows = holdout[["MatchID", "Outcome", "team_success_non_loss"]].copy()
    holdout_rows["predicted_success_non_loss"] = pred.astype(int)
    return (
        {
            "target": "team_success_non_loss",
            "target_definition": "1 for win or tie, 0 for loss; model inputs exclude goals and final score.",
            "model": "deterministic DecisionTreeClassifier(max_depth=2, min_samples_leaf=3)",
            "train_matches": int(len(train)),
            "holdout_matches": int(len(holdout)),
            "accuracy": clean_float(accuracy),
            "balanced_accuracy": clean_float(balanced),
            "holdout_predictions": holdout_rows.to_dict(orient="records"),
            "top_feature_importance": importances.head(8).to_dict(orient="records"),
            "feature_columns": FEATURE_COLUMNS,
        },
        importances,
    )


def strategy_recommendations(features: pd.DataFrame, network: dict[str, object]) -> dict[str, object]:
    wins = features[features["Outcome"] == "win"]
    losses = features[features["Outcome"] == "loss"]
    win_means = wins[FEATURE_COLUMNS].mean(numeric_only=True)
    loss_means = losses[FEATURE_COLUMNS].mean(numeric_only=True)
    gaps = (win_means - loss_means).sort_values(ascending=False)
    actions = [
        {
            "action": "Keep the passing network reciprocal rather than hub-only.",
            "evidence": f"Season reciprocity is {network['season_network_reciprocity']}; wins have reciprocity {clean_float(wins['network_reciprocity'].mean(), 4)} versus losses {clean_float(losses['network_reciprocity'].mean(), 4)}.",
            "model_family": "directed graph reciprocity and weighted centrality",
        },
        {
            "action": "Use midfield-forward triangles as the default attacking build-up pattern.",
            "evidence": f"Wins average {clean_float(wins['triadic_configurations'].mean(), 2)} triadic configurations versus {clean_float(losses['triadic_configurations'].mean(), 2)} in losses.",
            "model_family": "triadic network motifs and formation shares",
        },
        {
            "action": "Protect pass diversity instead of relying on one repeated dyad.",
            "evidence": f"The best positive feature gap is {gaps.index[0]} = {clean_float(gaps.iloc[0], 4)}.",
            "model_family": "entropy, concentration, and contribution-distribution indicators",
        },
        {
            "action": "Monitor match-by-match teamwork features after tactical changes.",
            "evidence": "The holdout model uses only network/event indicators and predicts non-loss outcomes on the last 8 official matches.",
            "model_family": "interpretable classification with temporal holdout",
        },
    ]
    return {"feature_gaps_win_minus_loss": {key: clean_float(value, 5) for key, value in gaps.to_dict().items()}, "actions": actions}


def write_artifacts(edge_table: pd.DataFrame, centrality: pd.DataFrame, features: pd.DataFrame, importances: pd.DataFrame) -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    edge_table.to_csv(ARTIFACT_DIR / "passing_network_edges.csv", index=False)
    centrality.to_csv(ARTIFACT_DIR / "player_centrality.csv", index=False)
    features.to_csv(ARTIFACT_DIR / "match_teamwork_features.csv", index=False)
    importances.to_csv(ARTIFACT_DIR / "teamwork_feature_importance.csv", index=False)

    top_edges = edge_table.head(12).copy()
    labels = [f"{row.origin}->{row.destination}" for row in top_edges.itertuples()]
    plt.figure(figsize=(10, 5))
    plt.barh(labels[::-1], top_edges["pass_count"].iloc[::-1], color="#2f6f73")
    plt.xlabel("official pass count")
    plt.title("2020 ICM-D Huskies top directed passing edges")
    plt.tight_layout()
    plt.savefig(ARTIFACT_DIR / "passing_network_top_edges.png", dpi=180)
    plt.close()

    top_features = importances.head(8)
    plt.figure(figsize=(8, 4.8))
    plt.barh(top_features["feature"].iloc[::-1], top_features["importance"].iloc[::-1], color="#b46a33")
    plt.xlabel("decision-tree importance")
    plt.title("Teamwork success model feature importance")
    plt.tight_layout()
    plt.savefig(ARTIFACT_DIR / "teamwork_feature_importance.png", dpi=180)
    plt.close()


def write_report(result: dict[str, object]) -> None:
    lines = [
        "# 2020 ICM-D Teaming Strategies：官方足球事件数据实验报告",
        "",
        "## 数据真实性",
        "",
        f"- 官方题面：`{result['data_source']['source_pdf']}`。",
        f"- 官方附件目录：`{result['data_source']['root']}`。",
        f"- 行数：`{result['data_source']['rows']}`。",
        "- 本解法只读取 COMAP 官方 CSV 和 README，不生成随机 `x1/x2/x3` 数据。",
        "",
        "## 每问建模与求解",
        "",
        "### q01 传球网络、二元/三元结构与多尺度指标",
        "",
        "- 模型：有向加权图、PageRank、介数中心性、互惠率、加权聚类和三角形 motif。",
        f"- Huskies 球员节点数：{result['passing_network']['huskies_player_count']}；传球数：{result['passing_network']['huskies_pass_count']}；有向边：{result['passing_network']['directed_edge_count']}。",
        f"- 赛季网络密度：{result['passing_network']['season_network_density']}；互惠率：{result['passing_network']['season_network_reciprocity']}。",
        "",
        "### q02 团队表现指标与团队协作模型",
        "",
        "- 模型：传球熵、贡献 Gini、前向传球比例、进攻三区比例、shot/duel/foul 事件计数和解释型决策树。",
        f"- 目标变量：{result['teamwork_model']['target_definition']}",
        f"- 时间留出：前 {result['teamwork_model']['train_matches']} 场训练，后 {result['teamwork_model']['holdout_matches']} 场检验。",
        f"- 留出准确率：{result['teamwork_model']['accuracy']}；balanced accuracy：{result['teamwork_model']['balanced_accuracy']}。",
        "",
        "### q03 给 Huskies 教练的结构策略建议",
        "",
    ]
    for action in result["strategy_recommendations"]["actions"]:
        lines.append(f"- {action['action']} 证据：{action['evidence']}")
    lines.extend(
        [
            "",
            "### q04 对一般团队协作的推广",
            "",
            result["generalization_memo"],
            "",
            "## 给教练的备忘录",
            "",
            result["coach_memo"],
            "",
            "## 产物",
            "",
            "- `artifacts/match_teamwork_features.csv`：38 场比赛逐场团队协作指标。",
            "- `artifacts/passing_network_edges.csv`：赛季有向传球边表。",
            "- `artifacts/player_centrality.csv`：球员中心性和位置角色。",
            "- `artifacts/teamwork_feature_importance.csv`：模型特征重要性。",
            "- `artifacts/passing_network_top_edges.png`：Top 传球边图。",
        ]
    )
    REPORT_PATH.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def outputs_current() -> bool:
    outputs = [RESULT_PATH, REPORT_PATH, *REQUIRED_ARTIFACTS]
    if not all(path.exists() for path in outputs):
        return False
    source_mtime = Path(__file__).stat().st_mtime
    input_mtime = max(path.stat().st_mtime for path in [PDF_PATH, MATCHES_PATH, PASSING_PATH, FULL_EVENTS_PATH, README_PATH])
    required_mtime = max(source_mtime, input_mtime)
    return all(path.stat().st_mtime >= required_mtime for path in outputs)


def main() -> None:
    if outputs_current():
        print(json.dumps({"cached": True, "result": str(RESULT_PATH), "report": str(REPORT_PATH)}, ensure_ascii=False, indent=2))
        return

    matches, passing, full_events = read_official_data()
    edge_table, centrality, network = pass_network_tables(passing)
    features = match_teamwork_features(matches, passing, full_events)
    model_result, importances = teamwork_model(features)
    patterns = formation_patterns(features)
    recommendations = strategy_recommendations(features, network)
    write_artifacts(edge_table, centrality, features, importances)

    result = {
        "data_source": {
            "type": "official_comap_csv",
            "root": str(DATA_ROOT),
            "source_pdf": str(PDF_PATH),
            "readme": str(README_PATH),
            "rows": {
                "matches.csv": int(len(matches)),
                "passingevents.csv": int(len(passing)),
                "fullevents.csv": int(len(full_events)),
            },
            "official_scope": "38 Huskies matches, 23,429 official pass rows, and 59,271 official event rows from COMAP 2020 ICM-D.",
        },
        "passing_network": network,
        "formation_patterns": patterns,
        "teamwork_model": model_result,
        "strategy_recommendations": recommendations,
        "coach_memo": (
            "To the Huskies coach: use the season passing network as a tactical dashboard. "
            "The official data show that coordination should be managed as a graph, not as isolated player totals: "
            "track reciprocal passing links, midfield-forward triads, pass-type diversity, and whether one dyad is carrying too much of the build-up. "
            "For next season, rehearse possessions that keep at least three stable passing outlets around the ball, protect the midfield bridge players, "
            "and review the teamwork feature table after every match rather than waiting for final league results."
        ),
        "generalization_memo": (
            "The soccer result generalizes to interdisciplinary teams by replacing players with specialists and passes with task handoffs. "
            "Successful interdisciplinary teams should have reciprocal information flow, redundant triads that prevent single-point failure, "
            "enough diversity of interaction types to adapt under pressure, and a monitoring routine that compares current teamwork indicators with past successful patterns."
        ),
    }
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_report(result)
    print(json.dumps({"result": str(RESULT_PATH), "report": str(REPORT_PATH), "artifacts": str(ARTIFACT_DIR)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
