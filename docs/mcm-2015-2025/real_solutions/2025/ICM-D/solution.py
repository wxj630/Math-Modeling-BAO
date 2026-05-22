from __future__ import annotations

import ast
import json
import math
import re
from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd
from scipy.spatial import cKDTree


ARCHIVE_ROOT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
DATA_DIR = ARCHIVE_ROOT / "official_assets_extracted" / "2025" / "2025_Problem_D_Data.zip" / "2025_Problem_D_Data"
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"

FILES = {
    "edges_drive.csv": DATA_DIR / "edges_drive.csv",
    "nodes_drive.csv": DATA_DIR / "nodes_drive.csv",
    "Bus_Stops.csv": DATA_DIR / "Bus_Stops.csv",
    "Bus_Routes.csv": DATA_DIR / "Bus_Routes.csv",
    "MDOT_SHA_Annual_Average_Daily_Traffic_Baltimore.csv": DATA_DIR / "MDOT_SHA_Annual_Average_Daily_Traffic_Baltimore.csv",
    "DataDictionary.csv": DATA_DIR / "DataDictionary.csv",
}

KEY_BRIDGE_BBOX = {
    "min_x": -76.52,
    "max_x": -76.45,
    "min_y": 39.225,
    "max_y": 39.252,
}


def clean_float(value: object, digits: int = 6) -> float | None:
    value = float(value)
    if math.isnan(value) or math.isinf(value):
        return None
    return round(value, digits)


def parse_linestring_points(geometry: object) -> list[tuple[float, float]]:
    nums = [float(x) for x in re.findall(r"-?\d+\.\d+", str(geometry))]
    return list(zip(nums[0::2], nums[1::2]))


def parse_node_set(value: object) -> list[int]:
    return [int(x) for x in re.findall(r"\d+", str(value))]


def read_official_data() -> dict[str, pd.DataFrame]:
    missing = [str(path) for path in FILES.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing official COMAP Baltimore files: " + ", ".join(missing))
    return {
        name: pd.read_csv(path, encoding_errors="ignore", low_memory=False)
        for name, path in FILES.items()
    }


def build_drive_graph(edges: pd.DataFrame) -> nx.DiGraph:
    graph = nx.DiGraph()
    for row in edges[["u", "v", "length", "highway", "name", "bridge", "ref"]].itertuples(index=False):
        try:
            u = int(row.u)
            v = int(row.v)
            length = float(row.length)
        except (TypeError, ValueError):
            continue
        if graph.has_edge(u, v):
            if length < graph[u][v]["length"]:
                graph[u][v].update(length=length, highway=str(row.highway), name=str(row.name), bridge=str(row.bridge), ref=str(row.ref))
        else:
            graph.add_edge(u, v, length=length, highway=str(row.highway), name=str(row.name), bridge=str(row.bridge), ref=str(row.ref))
    return graph


def enrich_edges(edges: pd.DataFrame) -> pd.DataFrame:
    out = edges.copy()
    centroids = []
    for geom in out["geometry"]:
        points = parse_linestring_points(geom)
        if points:
            xs = [p[0] for p in points]
            ys = [p[1] for p in points]
            centroids.append((sum(xs) / len(xs), sum(ys) / len(ys), min(xs), max(xs), min(ys), max(ys)))
        else:
            centroids.append((np.nan, np.nan, np.nan, np.nan, np.nan, np.nan))
    out[["cx", "cy", "min_x", "max_x", "min_y", "max_y"]] = pd.DataFrame(centroids, index=out.index)
    return out


def identify_key_bridge_edges(edges: pd.DataFrame) -> pd.DataFrame:
    enriched = enrich_edges(edges)
    mask = (
        enriched["name"].astype(str).str.contains("Baltimore Beltway", case=False, na=False)
        & enriched["ref"].astype(str).str.contains("I 695", case=False, na=False)
        & enriched["cx"].between(KEY_BRIDGE_BBOX["min_x"], KEY_BRIDGE_BBOX["max_x"])
        & enriched["cy"].between(KEY_BRIDGE_BBOX["min_y"], KEY_BRIDGE_BBOX["max_y"])
    )
    selected = enriched[mask].copy()
    if selected.empty:
        selected = enriched[
            enriched["name"].astype(str).str.contains("Baltimore Beltway", case=False, na=False)
            & enriched["ref"].astype(str).str.contains("I 695", case=False, na=False)
            & enriched["cy"].between(39.22, 39.27)
        ].copy()
    return selected


def nearest_nodes(nodes: pd.DataFrame, points: list[tuple[float, float]]) -> list[int]:
    coords = nodes[["x", "y"]].astype(float).to_numpy()
    tree = cKDTree(coords)
    _, idx = tree.query(np.array(points), k=1)
    return [int(nodes.iloc[int(i)]["osmid"]) for i in np.atleast_1d(idx)]


def route_impact(graph: nx.DiGraph, collapse_graph: nx.DiGraph, nodes: pd.DataFrame, stops: pd.DataFrame) -> dict[str, object]:
    key_points = [
        ("Key Bridge west approach", -76.5068, 39.2321),
        ("Key Bridge east approach", -76.4555, 39.2462),
        ("Downtown/Inner Harbor", -76.6122, 39.2867),
        ("Port/Curtis Bay", -76.5885, 39.2220),
        ("Dundalk/East Baltimore", -76.5200, 39.2600),
        ("I-95 Southwest Gateway", -76.6810, 39.2570),
        ("Mondawmin Transit Hub", -76.6530, 39.3181),
        ("Rogers Avenue Metro", -76.6916, 39.3446),
    ]
    nearest = dict(zip([p[0] for p in key_points], nearest_nodes(nodes, [(p[1], p[2]) for p in key_points])))
    od_pairs = [
        ("Key Bridge west-east approaches", "Key Bridge west approach", "Key Bridge east approach"),
        ("Port to Dundalk", "Port/Curtis Bay", "Dundalk/East Baltimore"),
        ("Southwest Gateway to Dundalk", "I-95 Southwest Gateway", "Dundalk/East Baltimore"),
        ("Downtown to Port", "Downtown/Inner Harbor", "Port/Curtis Bay"),
        ("Mondawmin to Port jobs", "Mondawmin Transit Hub", "Port/Curtis Bay"),
        ("Rogers Ave to Inner Harbor", "Rogers Avenue Metro", "Downtown/Inner Harbor"),
    ]
    rows = []
    for label, a, b in od_pairs:
        source = nearest[a]
        target = nearest[b]
        try:
            baseline = nx.shortest_path_length(graph, source, target, weight="length")
        except nx.NetworkXNoPath:
            baseline = math.nan
        try:
            collapsed = nx.shortest_path_length(collapse_graph, source, target, weight="length")
        except nx.NetworkXNoPath:
            collapsed = math.nan
        change = collapsed - baseline if not (math.isnan(baseline) or math.isnan(collapsed)) else math.nan
        rows.append(
            {
                "od_pair": label,
                "from": a,
                "to": b,
                "status_after_removal": "disconnected" if math.isnan(collapsed) else "connected",
                "baseline_km": clean_float(baseline / 1000, 3) if not math.isnan(baseline) else None,
                "collapse_km": clean_float(collapsed / 1000, 3) if not math.isnan(collapsed) else None,
                "extra_km": clean_float(change / 1000, 3) if not math.isnan(change) else None,
                "extra_pct": clean_float(change / baseline * 100, 2) if baseline and not math.isnan(change) else None,
            }
        )
    return {
        "anchor_nodes": nearest,
        "od_impacts": rows,
        "mean_extra_km": clean_float(np.nanmean([r["extra_km"] for r in rows if r["extra_km"] is not None]), 3),
        "max_extra_pct": clean_float(max([r["extra_pct"] for r in rows if r["extra_pct"] is not None]), 2),
        "disconnected_od_count": int(sum(1 for row in rows if row["status_after_removal"] == "disconnected")),
    }


def traffic_edge_scores(traffic: pd.DataFrame, graph: nx.DiGraph) -> list[dict[str, object]]:
    rows = []
    for _, row in traffic.iterrows():
        starts = parse_node_set(row.get("node start"))
        ends = parse_node_set(row.get("node(s) end"))
        volume = pd.to_numeric(row.get("AADT (Current)"), errors="coerce")
        lanes = pd.to_numeric(row.get("Number of Lanes"), errors="coerce")
        if not starts or not ends or pd.isna(volume):
            continue
        length = 0.0
        matched = False
        for u in starts:
            for v in ends:
                if graph.has_edge(u, v):
                    length += graph[u][v]["length"]
                    matched = True
        rows.append(
            {
                "road_name": str(row.get("Road Name", "")),
                "station_id": str(row.get("Station ID", "")),
                "aadt_current": int(volume),
                "lanes": int(lanes) if not pd.isna(lanes) else None,
                "aadt_per_lane": clean_float(volume / lanes, 2) if lanes and lanes > 0 else None,
                "functional_class": str(row.get("Functional Class", "")),
                "matched_drive_edge": bool(matched),
                "matched_length_m": clean_float(length, 2),
            }
        )
    return sorted(rows, key=lambda item: item["aadt_current"], reverse=True)[:15]


def bus_stop_project(stops: pd.DataFrame, nodes: pd.DataFrame) -> dict[str, object]:
    stop_data = stops.copy()
    stop_data["needs_shelter"] = stop_data["Shelter"].astype(str).str.lower().eq("no")
    candidates = stop_data[stop_data["needs_shelter"]].sort_values("Rider_Tota", ascending=False).head(15).copy()
    stop_nodes = nearest_nodes(nodes, list(zip(candidates["X"].astype(float), candidates["Y"].astype(float))))
    candidates["nearest_drive_node"] = stop_nodes
    top = []
    for _, row in candidates.head(10).iterrows():
        routes = [item.strip() for item in str(row["Routes_Ser"]).split(",") if item.strip()]
        top.append(
            {
                "stop_name": str(row["stop_name"]),
                "riders_total": int(row["Rider_Tota"]),
                "rider_on": int(row["Rider_On"]),
                "rider_off": int(row["Rider_Off"]),
                "route_count": len(set(routes)),
                "routes": ",".join(sorted(set(routes))[:8]),
                "nearest_drive_node": int(row["nearest_drive_node"]),
                "x": clean_float(row["X"], 6),
                "y": clean_float(row["Y"], 6),
            }
        )
    all_riders = float(stop_data["Rider_Tota"].sum())
    no_shelter_riders = float(stop_data.loc[stop_data["needs_shelter"], "Rider_Tota"].sum())
    top10_riders = float(candidates.head(10)["Rider_Tota"].sum())
    return {
        "total_stops": int(len(stop_data)),
        "no_shelter_stops": int(stop_data["needs_shelter"].sum()),
        "riders_at_no_shelter_share": clean_float(no_shelter_riders / all_riders, 4),
        "top10_no_shelter_riders": int(top10_riders),
        "top10_no_shelter_share_all_riders": clean_float(top10_riders / all_riders, 4),
        "recommended_project": "Install shelters, lighting, ADA boarding pads, and bus-priority curb management at the highest-ridership unsheltered stops.",
        "priority_stops": top,
    }


def safety_priorities(stops: pd.DataFrame, traffic: pd.DataFrame) -> dict[str, object]:
    top_stops = stops.sort_values("Rider_Tota", ascending=False).head(20)
    high_traffic = traffic.copy()
    high_traffic["AADT (Current)"] = pd.to_numeric(high_traffic["AADT (Current)"], errors="coerce")
    high_traffic["Number of Lanes"] = pd.to_numeric(high_traffic["Number of Lanes"], errors="coerce")
    high_traffic["aadt_per_lane"] = high_traffic["AADT (Current)"] / high_traffic["Number of Lanes"].replace(0, np.nan)
    road_rows = []
    for _, row in high_traffic.sort_values("aadt_per_lane", ascending=False).head(12).iterrows():
        road_rows.append(
            {
                "road_name": str(row["Road Name"]),
                "station_id": str(row["Station ID"]),
                "aadt_current": int(row["AADT (Current)"]) if not pd.isna(row["AADT (Current)"]) else None,
                "lanes": int(row["Number of Lanes"]) if not pd.isna(row["Number of Lanes"]) else None,
                "aadt_per_lane": clean_float(row["aadt_per_lane"], 2) if not pd.isna(row["aadt_per_lane"]) else None,
                "functional_class": str(row["Functional Class"]),
            }
        )
    stop_rows = [
        {
            "stop_name": str(row["stop_name"]),
            "riders_total": int(row["Rider_Tota"]),
            "shelter": str(row["Shelter"]),
            "routes": str(row["Routes_Ser"]),
        }
        for _, row in top_stops.iterrows()
    ]
    return {
        "safety_strategy": "Prioritize pedestrian refuge, protected crossings, lighting, speed management, and bus-stop hardening where high-ridership stops overlap high traffic exposure.",
        "high_exposure_roads": road_rows,
        "high_ridership_stops": stop_rows[:12],
    }


def stakeholder_project_summary(route: dict[str, object], bus: dict[str, object], traffic_scores: list[dict[str, object]]) -> dict[str, object]:
    disconnected = [row for row in route["od_impacts"] if row["status_after_removal"] == "disconnected"]
    worst = max(route["od_impacts"], key=lambda row: row["extra_pct"] if row["extra_pct"] is not None else -1)
    bridge_benefit = (
        f"Restores direct connectivity for {disconnected[0]['od_pair']} under the removal scenario."
        if disconnected
        else f"Restores network redundancy; worst sampled OD pair adds {worst['extra_km']} km ({worst['extra_pct']}%) under bridge removal."
    )
    return {
        "recommended_projects": [
            {
                "project": "Rebuild and harden the Francis Scott Key / I-695 harbor crossing corridor.",
                "primary_benefit": bridge_benefit,
                "resident_benefit": "Improves access between port-adjacent jobs, east/south neighborhoods, and regional highways.",
                "other_stakeholders": "Port freight, commuters, emergency services, and pass-through traffic gain reliability; construction staging creates short-run delays.",
                "disruption": "Major capital cost, detours, construction noise, and possible induced traffic unless paired with transit and safety improvements.",
            },
            {
                "project": bus["recommended_project"],
                "primary_benefit": f"Targets {bus['top10_no_shelter_riders']} boardings/alightings at the top 10 unsheltered high-ridership stops.",
                "resident_benefit": "Benefits bus-dependent residents directly through weather protection, safer waiting areas, and more reliable boarding.",
                "other_stakeholders": "Transit agency operations improve, nearby businesses may gain foot traffic, drivers may face curb-management changes.",
                "disruption": "Temporary sidewalk work, curb reallocation, and potential parking/loading conflicts near priority stops.",
            },
        ],
        "top_traffic_segments": traffic_scores[:8],
    }


def write_artifacts(result: dict[str, object]) -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(result["bridge_impact"]["od_impacts"]).to_csv(ARTIFACT_DIR / "bridge_od_impacts.csv", index=False, encoding="utf-8-sig")
    pd.DataFrame(result["bus_project"]["priority_stops"]).to_csv(ARTIFACT_DIR / "priority_bus_stops.csv", index=False, encoding="utf-8-sig")
    pd.DataFrame(result["safety_priorities"]["high_exposure_roads"]).to_csv(ARTIFACT_DIR / "high_exposure_roads.csv", index=False, encoding="utf-8-sig")

    stops = pd.DataFrame(result["bus_project"]["priority_stops"])
    if not stops.empty:
        plt.figure(figsize=(9, 5))
        plt.barh(stops["stop_name"].head(10)[::-1], stops["riders_total"].head(10)[::-1], color="#355c7d")
        plt.xlabel("Rider total")
        plt.title("Highest-ridership unsheltered bus stops")
        plt.tight_layout()
        plt.savefig(ARTIFACT_DIR / "priority_bus_stops.png", dpi=180)
        plt.close()

    impacts = pd.DataFrame(result["bridge_impact"]["od_impacts"])
    if not impacts.empty:
        plt.figure(figsize=(8, 4.6))
        plt.bar(impacts["od_pair"], impacts["extra_km"].fillna(0), color="#9c3d54")
        plt.xticks(rotation=35, ha="right")
        plt.ylabel("Extra km after bridge removal")
        plt.title("Sample OD network impact of I-695 harbor crossing removal")
        plt.tight_layout()
        plt.savefig(ARTIFACT_DIR / "bridge_od_impacts.png", dpi=180)
        plt.close()


def write_report(result: dict[str, object]) -> None:
    lines = [
        "# 2025 ICM-D A Roadmap to a Better City 真实数据解法",
        "",
        "## 数据来源",
        "- 使用 COMAP 官方 `2025_Problem_D_Data.zip` 解压出的路网、公交站、公交线路和 AADT 交通量 CSV。",
        "- 没有使用随机生成交通流或虚构站点。",
        "",
        "## 网络模型",
        f"- 驾车路网节点：{result['network_summary']['drive_nodes']}，边：{result['network_summary']['drive_edges']}。",
        f"- 公交站：{result['data_source']['rows']['Bus_Stops.csv']}，公交线路：{result['data_source']['rows']['Bus_Routes.csv']}。",
        f"- AADT 交通量记录：{result['data_source']['rows']['MDOT_SHA_Annual_Average_Daily_Traffic_Baltimore.csv']}。",
        "",
        "## Q1 桥梁坍塌/重建影响",
        f"- 识别 I-695/Baltimore Beltway 港口桥梁走廊边数：{result['bridge_impact']['removed_edge_count']}。",
        f"- 样本 OD 平均额外距离：{result['bridge_impact']['mean_extra_km']} km，最大额外比例：{result['bridge_impact']['max_extra_pct']}%，断连 OD 数：{result['bridge_impact']['disconnected_od_count']}。",
        "",
        "| OD | status | baseline km | collapse km | extra km | extra % |",
        "|---|---|---:|---:|---:|---:|",
    ]
    for row in result["bridge_impact"]["od_impacts"]:
        lines.append(f"| {row['od_pair']} | {row['status_after_removal']} | {row['baseline_km']} | {row['collapse_km']} | {row['extra_km']} | {row['extra_pct']} |")
    lines.extend([
        "",
        "## Q2 公交/步行项目",
        f"- 推荐项目：{result['bus_project']['recommended_project']}",
        f"- 无候车亭站点：{result['bus_project']['no_shelter_stops']} / {result['bus_project']['total_stops']}。",
        f"- 前 10 个高客流无候车亭站点覆盖客流：{result['bus_project']['top10_no_shelter_riders']}。",
        "",
        "| stop | riders | routes | nearest node |",
        "|---|---:|---:|---:|",
    ])
    for row in result["bus_project"]["priority_stops"][:10]:
        lines.append(f"| {row['stop_name']} | {row['riders_total']} | {row['route_count']} | {row['nearest_drive_node']} |")
    lines.extend([
        "",
        "## Q3-Q5 推荐项目、收益、利益相关者与扰动",
    ])
    for item in result["project_recommendations"]["recommended_projects"]:
        lines.extend([
            f"### {item['project']}",
            f"- 主要收益：{item['primary_benefit']}",
            f"- 居民收益：{item['resident_benefit']}",
            f"- 其他利益相关者：{item['other_stakeholders']}",
            f"- 扰动：{item['disruption']}",
        ])
    lines.extend([
        "",
        "## Q6 安全策略",
        f"- {result['safety_priorities']['safety_strategy']}",
        "",
        "| road | AADT | lanes | AADT/lane | class |",
        "|---|---:|---:|---:|---|",
    ])
    for row in result["safety_priorities"]["high_exposure_roads"][:10]:
        lines.append(f"| {row['road_name']} | {row['aadt_current']} | {row['lanes']} | {row['aadt_per_lane']} | {row['functional_class']} |")
    lines.extend([
        "",
        "## Q7 给市长的一页备忘录摘要",
        result["mayor_memo"],
        "",
        "## 输出文件",
        "- `result.json`：结构化结果。",
        "- `artifacts/bridge_od_impacts.csv/png`：桥梁走廊移除 OD 影响。",
        "- `artifacts/priority_bus_stops.csv/png`：公交站项目优先级。",
        "- `artifacts/high_exposure_roads.csv`：高安全暴露道路。",
    ])
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    data = read_official_data()
    edges = data["edges_drive.csv"]
    nodes = data["nodes_drive.csv"]
    stops = data["Bus_Stops.csv"]
    routes = data["Bus_Routes.csv"]
    traffic = data["MDOT_SHA_Annual_Average_Daily_Traffic_Baltimore.csv"]

    graph = build_drive_graph(edges)
    key_edges = identify_key_bridge_edges(edges)
    collapse_graph = graph.copy()
    collapse_graph.remove_edges_from([(int(row.u), int(row.v)) for row in key_edges.itertuples(index=False) if collapse_graph.has_edge(int(row.u), int(row.v))])

    bridge = route_impact(graph, collapse_graph, nodes, stops)
    bridge["removed_edge_count"] = int(len(key_edges))
    bridge["removed_total_km"] = clean_float(pd.to_numeric(key_edges["length"], errors="coerce").sum() / 1000, 3)
    bus = bus_stop_project(stops, nodes)
    traffic_scores = traffic_edge_scores(traffic, graph)
    safety = safety_priorities(stops, traffic)
    recommendations = stakeholder_project_summary(bridge, bus, traffic_scores)
    mayor_memo = (
        "Mayor, the model recommends a paired program: rebuild and harden the I-695 harbor crossing to restore regional freight/emergency redundancy, "
        "while immediately funding bus-stop safety upgrades at the highest-ridership unsheltered stops. The bridge project protects port access and regional reliability but causes construction disruption; "
        "the transit project directly helps daily residents at modest scale, with curb and sidewalk tradeoffs. Safety benefits are strongest if both projects include lighting, refuge crossings, speed management, and bus-priority curb design."
    )

    result: dict[str, object] = {
        "problem": "2025 ICM-D A Roadmap to a Better City",
        "data_source": {
            "type": "official_comap_csv",
            "root": str(DATA_DIR),
            "rows": {name: int(len(df)) for name, df in data.items()},
        },
        "network_summary": {
            "drive_nodes": int(graph.number_of_nodes()),
            "drive_edges": int(graph.number_of_edges()),
            "largest_weak_component_nodes": int(len(max(nx.weakly_connected_components(graph), key=len))),
            "bus_routes": int(len(routes)),
            "bus_stops": int(len(stops)),
        },
        "bridge_impact": bridge,
        "bus_project": bus,
        "project_recommendations": recommendations,
        "safety_priorities": safety,
        "mayor_memo": mayor_memo,
    }
    ROOT.mkdir(parents=True, exist_ok=True)
    write_artifacts(result)
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_report(result)
    print(json.dumps({"result": str(RESULT_PATH), "report": str(REPORT_PATH)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
