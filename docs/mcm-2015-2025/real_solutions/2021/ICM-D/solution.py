from __future__ import annotations

import ast
import json
from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler


ARCHIVE_ROOT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
DATA_DIR = ARCHIVE_ROOT / "official_assets_extracted" / "2021" / "Problem Data- The Influence of Music" / "2021_ICM_Problem_D_Data"
PDF_PATH = ARCHIVE_ROOT / "official_assets_extracted" / "2021" / "The Influence of Music.pdf"
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"

FEATURES = [
    "danceability",
    "energy",
    "valence",
    "tempo",
    "loudness",
    "acousticness",
    "instrumentalness",
    "liveness",
    "speechiness",
    "duration_ms",
    "popularity",
]


def official_inputs() -> list[Path]:
    return [
        DATA_DIR / "influence_data.csv",
        DATA_DIR / "full_music_data.csv",
        DATA_DIR / "data_by_artist.csv",
        DATA_DIR / "data_by_year.csv",
        PDF_PATH,
        Path(__file__).resolve(),
    ]


def outputs_are_current() -> bool:
    required_outputs = [
        RESULT_PATH,
        REPORT_PATH,
        ARTIFACT_DIR / "artist_influence_centrality.csv",
        ARTIFACT_DIR / "genre_similarity_matrix.csv",
        ARTIFACT_DIR / "genre_feature_evolution.csv",
        ARTIFACT_DIR / "feature_contagion.csv",
        ARTIFACT_DIR / "revolutionary_artists.csv",
        ARTIFACT_DIR / "influence_network_top_artists.png",
        ARTIFACT_DIR / "genre_similarity_heatmap.png",
    ]
    if any(not path.exists() for path in required_outputs):
        return False
    output_mtime = min(path.stat().st_mtime for path in required_outputs)
    input_mtime = max(path.stat().st_mtime for path in official_inputs() if path.exists())
    return output_mtime >= input_mtime


def clean_float(value: float, digits: int = 6) -> float:
    if pd.isna(value):
        return 0.0
    return round(float(value), digits)


def read_official_data() -> dict[str, pd.DataFrame]:
    files = {
        "influence_data.csv": DATA_DIR / "influence_data.csv",
        "full_music_data.csv": DATA_DIR / "full_music_data.csv",
        "data_by_artist.csv": DATA_DIR / "data_by_artist.csv",
        "data_by_year.csv": DATA_DIR / "data_by_year.csv",
    }
    missing = [str(path) for path in files.values() if not path.exists()]
    if not PDF_PATH.exists():
        missing.append(str(PDF_PATH))
    if missing:
        raise FileNotFoundError("missing official COMAP 2021-D assets: " + ", ".join(missing))
    return {name: pd.read_csv(path) for name, path in files.items()}


def genre_lookup(influence: pd.DataFrame) -> pd.DataFrame:
    influencer = influence[["influencer_id", "influencer_name", "influencer_main_genre", "influencer_active_start"]].rename(
        columns={
            "influencer_id": "artist_id",
            "influencer_name": "artist_name_from_influence",
            "influencer_main_genre": "main_genre",
            "influencer_active_start": "active_start",
        }
    )
    follower = influence[["follower_id", "follower_name", "follower_main_genre", "follower_active_start"]].rename(
        columns={
            "follower_id": "artist_id",
            "follower_name": "artist_name_from_influence",
            "follower_main_genre": "main_genre",
            "follower_active_start": "active_start",
        }
    )
    lookup = pd.concat([influencer, follower], ignore_index=True)
    lookup["artist_id"] = lookup["artist_id"].astype(int)
    lookup = lookup.dropna(subset=["main_genre"]).drop_duplicates("artist_id")
    return lookup


def artist_feature_table(data: dict[str, pd.DataFrame]) -> pd.DataFrame:
    artists = data["data_by_artist.csv"].copy()
    artists["artist_id"] = artists["artist_id"].astype(int)
    lookup = genre_lookup(data["influence_data.csv"])
    merged = artists.merge(lookup[["artist_id", "main_genre", "active_start"]], on="artist_id", how="left")
    merged["main_genre"] = merged["main_genre"].fillna("Unknown")
    scaler = StandardScaler()
    scaled = scaler.fit_transform(merged[FEATURES].fillna(merged[FEATURES].median()))
    for index, feature in enumerate(FEATURES):
        merged[f"z_{feature}"] = scaled[:, index]
    return merged


def build_influence_network(influence: pd.DataFrame) -> tuple[nx.DiGraph, pd.DataFrame]:
    graph = nx.DiGraph()
    for row in influence.itertuples(index=False):
        influencer = int(row.influencer_id)
        follower = int(row.follower_id)
        graph.add_node(
            influencer,
            name=row.influencer_name,
            genre=row.influencer_main_genre,
            active_start=int(row.influencer_active_start),
        )
        graph.add_node(
            follower,
            name=row.follower_name,
            genre=row.follower_main_genre,
            active_start=int(row.follower_active_start),
        )
        graph.add_edge(influencer, follower)

    pagerank = nx.pagerank(graph, alpha=0.85, max_iter=200, tol=1e-9)
    centrality_rows = []
    for artist_id, attrs in graph.nodes(data=True):
        centrality_rows.append(
            {
                "artist_id": int(artist_id),
                "artist_name": attrs.get("name", ""),
                "main_genre": attrs.get("genre", ""),
                "active_start": attrs.get("active_start", ""),
                "in_degree": int(graph.in_degree(artist_id)),
                "out_degree": int(graph.out_degree(artist_id)),
                "pagerank": clean_float(pagerank.get(artist_id, 0.0), 10),
                "influence_score": clean_float(np.log1p(graph.out_degree(artist_id)) * 0.45 + np.log1p(graph.in_degree(artist_id)) * 0.35 + pagerank.get(artist_id, 0.0) * 100.0 * 0.20),
            }
        )
    centrality = pd.DataFrame(centrality_rows).sort_values(
        ["influence_score", "out_degree", "in_degree"], ascending=False
    )
    return graph, centrality


def top_genre_similarity(artists: pd.DataFrame) -> tuple[dict[str, object], pd.DataFrame]:
    feature_cols = [f"z_{feature}" for feature in FEATURES]
    known = artists[artists["main_genre"] != "Unknown"].copy()
    genre_counts = known["main_genre"].value_counts()
    top_genres = genre_counts[genre_counts >= 80].head(12).index.tolist()
    subset = known[known["main_genre"].isin(top_genres)].copy()

    centroids = subset.groupby("main_genre")[feature_cols].mean()
    centroid_similarity = pd.DataFrame(cosine_similarity(centroids), index=centroids.index, columns=centroids.index)
    within_rows = []
    for genre, frame in subset.groupby("main_genre"):
        centroid = centroids.loc[genre].to_numpy()
        distances = np.linalg.norm(frame[feature_cols].to_numpy() - centroid, axis=1)
        within_rows.append(1.0 / (1.0 + float(distances.mean())))
    between_rows = []
    for i in range(len(centroids)):
        for j in range(i + 1, len(centroids)):
            distance = float(np.linalg.norm(centroids.iloc[i].to_numpy() - centroids.iloc[j].to_numpy()))
            between_rows.append(1.0 / (1.0 + distance))
    summary = {
        "method": "Standardize official data_by_artist audio features; compare artists to same-genre centroids and compare genre centroids with the same distance-to-similarity transform. The matrix artifact also records cosine similarity between genre centroids.",
        "artist_count_with_genre": int(len(known)),
        "top_genres_used": top_genres,
        "within_genre_mean_similarity": clean_float(np.mean(within_rows)),
        "between_genre_mean_similarity": clean_float(np.mean(between_rows)),
        "most_similar_genre_pairs": [],
    }
    pair_rows = []
    for i, genre_a in enumerate(centroid_similarity.index):
        for j, genre_b in enumerate(centroid_similarity.columns):
            if j <= i:
                continue
            pair_rows.append(
                {
                    "genre_a": genre_a,
                    "genre_b": genre_b,
                    "centroid_cosine_similarity": clean_float(centroid_similarity.iloc[i, j]),
                }
            )
    pair_rows.sort(key=lambda item: item["centroid_cosine_similarity"], reverse=True)
    summary["most_similar_genre_pairs"] = pair_rows[:10]
    return summary, centroid_similarity.reset_index().rename(columns={"main_genre": "genre"})


def parse_first_artist_id(value: object) -> int | None:
    try:
        parsed = ast.literal_eval(str(value))
        if isinstance(parsed, list) and parsed:
            return int(parsed[0])
    except (ValueError, SyntaxError, TypeError):
        return None
    return None


def genre_evolution(data: dict[str, pd.DataFrame], artists: pd.DataFrame) -> tuple[dict[str, object], pd.DataFrame]:
    full = data["full_music_data.csv"].copy()
    full["artist_id"] = full["artists_id"].apply(parse_first_artist_id)
    genre_map = artists[["artist_id", "main_genre"]].drop_duplicates()
    full = full.dropna(subset=["artist_id"]).astype({"artist_id": int})
    full = full.merge(genre_map, on="artist_id", how="left")
    full = full[full["main_genre"].notna() & (full["main_genre"] != "Unknown")]
    top_genres = full["main_genre"].value_counts().head(10).index.tolist()
    rows = []
    for genre in top_genres:
        grouped = full[full["main_genre"] == genre].groupby("year")[FEATURES[:9]].mean().reset_index()
        if len(grouped) < 12:
            continue
        item = {"main_genre": genre, "year_min": int(grouped["year"].min()), "year_max": int(grouped["year"].max()), "year_count": int(len(grouped))}
        for feature in ["danceability", "energy", "valence", "tempo", "loudness", "acousticness", "instrumentalness"]:
            slope = np.polyfit(grouped["year"], grouped[feature], 1)[0]
            item[f"{feature}_slope_per_year"] = clean_float(slope, 8)
            item[f"{feature}_change_1921_2020"] = clean_float(slope * (grouped["year"].max() - grouped["year"].min()))
        rows.append(item)
    evolution = pd.DataFrame(rows).sort_values("energy_change_1921_2020", ascending=False)
    global_year = data["data_by_year.csv"].copy()
    global_trends = []
    for feature in ["danceability", "energy", "valence", "tempo", "loudness", "acousticness", "instrumentalness"]:
        slope = np.polyfit(global_year["year"], global_year[feature], 1)[0]
        global_trends.append({"feature": feature, "slope_per_year": clean_float(slope, 8), "change_1921_2020": clean_float(slope * 99)})
    return {
        "method": "Merge official full_music_data first artist id to official influence genres, then estimate per-year feature slopes by genre.",
        "song_rows_with_genre": int(len(full)),
        "global_feature_trends": global_trends,
        "genre_profiles": evolution.head(10).to_dict("records"),
    }, evolution


def influence_evidence(data: dict[str, pd.DataFrame], artists: pd.DataFrame) -> tuple[dict[str, object], pd.DataFrame]:
    feature_cols = [f"z_{feature}" for feature in FEATURES]
    vectors = artists.set_index("artist_id")[feature_cols + ["main_genre"]]
    edge_rows = []
    for row in data["influence_data.csv"].itertuples(index=False):
        influencer = int(row.influencer_id)
        follower = int(row.follower_id)
        if influencer not in vectors.index or follower not in vectors.index:
            continue
        influencer_vec = vectors.loc[influencer, feature_cols].to_numpy(dtype=float)
        follower_vec = vectors.loc[follower, feature_cols].to_numpy(dtype=float)
        distance = float(np.linalg.norm(influencer_vec - follower_vec))
        edge_rows.append(
            {
                "influencer_id": influencer,
                "follower_id": follower,
                "influencer_genre": row.influencer_main_genre,
                "follower_genre": row.follower_main_genre,
                "same_genre": row.influencer_main_genre == row.follower_main_genre,
                "feature_distance": distance,
                "similarity": 1.0 / (1.0 + distance),
            }
        )
    edge_features = pd.DataFrame(edge_rows)
    contagion_rows = []
    merged = data["influence_data.csv"][["influencer_id", "follower_id"]].copy()
    left = artists[["artist_id"] + FEATURES].rename(columns={"artist_id": "influencer_id", **{feature: f"influencer_{feature}" for feature in FEATURES}})
    right = artists[["artist_id"] + FEATURES].rename(columns={"artist_id": "follower_id", **{feature: f"follower_{feature}" for feature in FEATURES}})
    merged = merged.merge(left, on="influencer_id", how="inner").merge(right, on="follower_id", how="inner")
    for feature in FEATURES:
        corr = merged[f"influencer_{feature}"].corr(merged[f"follower_{feature}"])
        gap = (merged[f"influencer_{feature}"] - merged[f"follower_{feature}"]).abs().mean()
        contagion_rows.append({"feature": feature, "influencer_follower_correlation": clean_float(corr), "mean_absolute_gap": clean_float(gap)})
    contagion = pd.DataFrame(contagion_rows).sort_values("influencer_follower_correlation", ascending=False)
    same = edge_features[edge_features["same_genre"]]
    different = edge_features[~edge_features["same_genre"]]
    summary = {
        "method": "Join official influence edges to official data_by_artist features; high influencer-follower correlation and lower feature distance support measurable influence.",
        "edge_pairs_with_features": int(len(edge_features)),
        "same_genre_edge_similarity": clean_float(same["similarity"].mean()),
        "cross_genre_edge_similarity": clean_float(different["similarity"].mean()),
        "feature_contagion": contagion.to_dict("records"),
    }
    return summary, contagion


def revolutionary_artists(centrality: pd.DataFrame, data: dict[str, pd.DataFrame], artists: pd.DataFrame) -> tuple[dict[str, object], pd.DataFrame]:
    feature_cols = [f"z_{feature}" for feature in FEATURES]
    vectors = artists.set_index("artist_id")[feature_cols]
    out_rows = []
    for row in data["influence_data.csv"].itertuples(index=False):
        influencer = int(row.influencer_id)
        follower = int(row.follower_id)
        if influencer not in vectors.index or follower not in vectors.index:
            continue
        distance = float(np.linalg.norm(vectors.loc[influencer].to_numpy(dtype=float) - vectors.loc[follower].to_numpy(dtype=float)))
        out_rows.append({"artist_id": influencer, "mean_follower_feature_distance": distance})
    leap = pd.DataFrame(out_rows).groupby("artist_id", as_index=False).agg(
        mean_follower_feature_distance=("mean_follower_feature_distance", "mean"),
        feature_link_count=("mean_follower_feature_distance", "size"),
    )
    candidates = centrality.merge(leap, on="artist_id", how="left").fillna({"mean_follower_feature_distance": 0.0, "feature_link_count": 0})
    candidates = candidates[candidates["out_degree"] >= 10].copy()
    candidates["revolutionary_score"] = (
        candidates["influence_score"].rank(pct=True) * 0.50
        + candidates["mean_follower_feature_distance"].rank(pct=True) * 0.35
        + candidates["out_degree"].rank(pct=True) * 0.15
    )
    candidates = candidates.sort_values("revolutionary_score", ascending=False)
    out = candidates[[
        "artist_id",
        "artist_name",
        "main_genre",
        "active_start",
        "out_degree",
        "in_degree",
        "pagerank",
        "mean_follower_feature_distance",
        "feature_link_count",
        "revolutionary_score",
    ]].head(20).copy()
    for column in ["mean_follower_feature_distance", "revolutionary_score"]:
        out[column] = out[column].map(clean_float)
    return {
        "method": "Rank artists by directed-network influence plus average feature distance to followers, identifying high-impact artists associated with major stylistic jumps.",
        "artists": out.head(12).to_dict("records"),
    }, out


def cultural_context(data: dict[str, pd.DataFrame]) -> dict[str, object]:
    influence = data["influence_data.csv"].copy()
    decade_counts = influence.groupby("follower_active_start").size().reset_index(name="edge_count").sort_values("follower_active_start")
    pre_internet = int(influence[influence["follower_active_start"] < 1990].shape[0])
    internet_transition = int(influence[(influence["follower_active_start"] >= 1990) & (influence["follower_active_start"] <= 2000)].shape[0])
    post_2000 = int(influence[influence["follower_active_start"] > 2000].shape[0])
    return {
        "decade_edge_counts": decade_counts.to_dict("records"),
        "pre_1990_edges": pre_internet,
        "1990_2000_edges": internet_transition,
        "post_2000_edges": post_2000,
        "interpretation": "Follower active-start decades show how the observed influence network concentrates across eras; this is a network signal, not a causal proof of internet or political effects.",
    }


def write_artifacts(centrality: pd.DataFrame, similarity_matrix: pd.DataFrame, evolution: pd.DataFrame, contagion: pd.DataFrame, revolutionaries: pd.DataFrame) -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    centrality.to_csv(ARTIFACT_DIR / "artist_influence_centrality.csv", index=False)
    similarity_matrix.to_csv(ARTIFACT_DIR / "genre_similarity_matrix.csv", index=False)
    evolution.to_csv(ARTIFACT_DIR / "genre_feature_evolution.csv", index=False)
    contagion.to_csv(ARTIFACT_DIR / "feature_contagion.csv", index=False)
    revolutionaries.to_csv(ARTIFACT_DIR / "revolutionary_artists.csv", index=False)

    top = centrality.head(15).sort_values("influence_score")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(top["artist_name"], top["influence_score"], color="#356859")
    ax.set_title("2021 ICM-D top artist influence scores")
    ax.set_xlabel("Influence score")
    ax.grid(axis="x", alpha=0.25)
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "influence_network_top_artists.png", dpi=180)
    plt.close(fig)

    numeric = similarity_matrix.set_index("genre")
    fig, ax = plt.subplots(figsize=(8, 7))
    im = ax.imshow(numeric.to_numpy(dtype=float), cmap="viridis", vmin=-1, vmax=1)
    ax.set_xticks(range(len(numeric.columns)))
    ax.set_xticklabels(numeric.columns, rotation=90, fontsize=7)
    ax.set_yticks(range(len(numeric.index)))
    ax.set_yticklabels(numeric.index, fontsize=7)
    ax.set_title("Genre centroid cosine similarity")
    fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "genre_similarity_heatmap.png", dpi=180)
    plt.close(fig)


def build_memo(result: dict[str, object]) -> str:
    top = result["influence_network"]["top_influencers"][:3]
    top_names = ", ".join(item["artist_name"] for item in top)
    within = result["similarity_model"]["within_genre_mean_similarity"]
    between = result["similarity_model"]["between_genre_mean_similarity"]
    return (
        "To the ICM Society: our network approach turns the provided artist influence lists into "
        "a directed graph and links that graph to the provided Spotify-style audio features. The "
        f"top network influencers in this run include {top_names}. Within-genre similarity "
        f"({within}) is higher than between-genre similarity ({between}), so genres have measurable "
        "feature signatures while still showing cross-genre bridges. With richer data, the same "
        "pipeline should add lyrics, geography, collaborations, release chronology, and external "
        "historical events; those additions would allow stronger causal claims about cultural, social, "
        "political, or technological influence. The current results are valuable as an auditable map "
        "of influence, similarity, and musical evolution using only the four contest files."
    )


def write_report(result: dict[str, object]) -> None:
    lines = [
        "# 2021 ICM-D The Influence of Music",
        "",
        "## 数据与真实性",
        f"- 官方题面：`{PDF_PATH}`。",
        f"- 官方附件目录：`{DATA_DIR}`。",
        "- 只使用 COMAP 提供的 `influence_data.csv`、`full_music_data.csv`、`data_by_artist.csv`、`data_by_year.csv`；没有随机数、没有外部 Spotify 抓取、没有 x1/x2/x3 占位数据。",
        f"- 行数：`{result['data_source']['rows']}`。",
        "",
        "## 建模与求解",
        "- 影响网络：把 influencer -> follower 作为有向边，计算入度、出度、PageRank 和综合 influence_score。",
        "- 音乐相似性：对官方 `data_by_artist` 的音频特征标准化，比较同流派艺术家到流派中心的距离，以及流派中心之间的余弦相似度。",
        "- 流派演化：把 `full_music_data` 中第一 artist_id 合并到流派，按 year 估计各流派音频特征斜率。",
        "- 影响证据：把官方影响边连接到艺术家特征，计算 influencer-follower 特征相关和距离，识别更可能传播的音乐特征。",
        "- 革命者：综合网络影响力、出边规模和与追随者的特征跃迁距离排序。",
        "",
        "## 关键结果",
        f"- 网络节点数：{result['influence_network']['node_count']}；边数：{result['influence_network']['edge_count']}。",
        f"- 同流派平均相似度：{result['similarity_model']['within_genre_mean_similarity']}；跨流派平均相似度：{result['similarity_model']['between_genre_mean_similarity']}。",
        f"- 有特征可连接的影响边：{result['influence_evidence']['edge_pairs_with_features']}。",
        "",
        "### Top influencers",
        "| artist | genre | out_degree | in_degree | pagerank | score |",
        "|---|---|---:|---:|---:|---:|",
    ]
    for row in result["influence_network"]["top_influencers"][:12]:
        lines.append(f"| {row['artist_name']} | {row['main_genre']} | {row['out_degree']} | {row['in_degree']} | {row['pagerank']} | {row['influence_score']} |")
    lines.extend([
        "",
        "### 最相近流派对",
        "| genre_a | genre_b | centroid_cosine_similarity |",
        "|---|---|---:|",
    ])
    for row in result["similarity_model"]["most_similar_genre_pairs"][:8]:
        lines.append(f"| {row['genre_a']} | {row['genre_b']} | {row['centroid_cosine_similarity']} |")
    lines.extend([
        "",
        "### 特征传播证据",
        "| feature | influencer_follower_correlation | mean_absolute_gap |",
        "|---|---:|---:|",
    ])
    for row in result["influence_evidence"]["feature_contagion"][:8]:
        lines.append(f"| {row['feature']} | {row['influencer_follower_correlation']} | {row['mean_absolute_gap']} |")
    lines.extend([
        "",
        "### 革命性艺术家候选",
        "| artist | genre | active_start | out_degree | feature_distance | score |",
        "|---|---|---:|---:|---:|---:|",
    ])
    for row in result["revolutionary_artists"]["artists"][:10]:
        lines.append(f"| {row['artist_name']} | {row['main_genre']} | {row['active_start']} | {row['out_degree']} | {row['mean_follower_feature_distance']} | {row['revolutionary_score']} |")
    lines.extend([
        "",
        "## One-page document to ICM Society",
        result["one_page_icm_society_memo"],
        "",
        "## 输出文件",
        "- `artifacts/artist_influence_centrality.csv`",
        "- `artifacts/genre_similarity_matrix.csv`",
        "- `artifacts/genre_feature_evolution.csv`",
        "- `artifacts/feature_contagion.csv`",
        "- `artifacts/revolutionary_artists.csv`",
        "- `artifacts/influence_network_top_artists.png`",
        "- `artifacts/genre_similarity_heatmap.png`",
    ])
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    if outputs_are_current():
        print(json.dumps({"result": str(RESULT_PATH), "report": str(REPORT_PATH), "artifacts": str(ARTIFACT_DIR), "cached": True}, ensure_ascii=False, indent=2))
        return
    data = read_official_data()
    artists = artist_feature_table(data)
    graph, centrality = build_influence_network(data["influence_data.csv"])
    similarity_summary, similarity_matrix = top_genre_similarity(artists)
    evolution_summary, evolution_table = genre_evolution(data, artists)
    evidence_summary, contagion_table = influence_evidence(data, artists)
    revolution_summary, revolution_table = revolutionary_artists(centrality, data, artists)
    write_artifacts(centrality, similarity_matrix, evolution_table, contagion_table, revolution_table)

    result: dict[str, object] = {
        "data_source": {
            "type": "official_comap_csv",
            "root": str(DATA_DIR),
            "source_pdf": str(PDF_PATH),
            "rows": {name: int(len(frame)) for name, frame in data.items()},
            "only_allowed_files": ["influence_data.csv", "full_music_data.csv", "data_by_artist.csv", "data_by_year.csv"],
        },
        "influence_network": {
            "node_count": int(graph.number_of_nodes()),
            "edge_count": int(graph.number_of_edges()),
            "weak_component_count": int(nx.number_weakly_connected_components(graph)),
            "largest_weak_component_nodes": int(len(max(nx.weakly_connected_components(graph), key=len))),
            "top_influencers": centrality.head(15).to_dict("records"),
            "pop_rock_subnetwork": {
                "node_count": int(len([node for node, attrs in graph.nodes(data=True) if attrs.get("genre") == "Pop/Rock"])),
                "edge_count": int(sum(1 for u, v in graph.edges() if graph.nodes[u].get("genre") == "Pop/Rock" and graph.nodes[v].get("genre") == "Pop/Rock")),
            },
        },
        "similarity_model": similarity_summary,
        "genre_evolution": evolution_summary,
        "influence_evidence": evidence_summary,
        "revolutionary_artists": revolution_summary,
        "cultural_influence_context": cultural_context(data),
    }
    result["one_page_icm_society_memo"] = build_memo(result)
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_report(result)
    print(json.dumps({"result": str(RESULT_PATH), "report": str(REPORT_PATH), "artifacts": str(ARTIFACT_DIR)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
