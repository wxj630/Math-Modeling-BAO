from __future__ import annotations

import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(REPO_ROOT))

from mcm.outstanding_solutions.paper_guided_reproduction import run


CONFIG = {
    "problem_id": "2025-D",
    "code": "D",
    "real_solution_key": "ICM-D",
    "paper_id": "2507692",
    "paper_title": "Optimizing Baltimore Multi-Layer Traffic Network Model Based on Graph Theory & Clustering Algorithm",
    "paper_source_ocr": "Outstanding_Solutions/MCM/OCR-results/D/2507692/2507692.md",
    "paper_source_pdf": "Outstanding_Solutions/MCM/PDF-2025/D/2507692.pdf",
    "selected_model": "多层交通网络 + 图论指标 + 聚类改造优先级",
    "scope": "用当前 ICM-D real solution 的官方 Baltimore 路网、公交、OD 冲击和安全优先级结果，对齐 2507692 的多层交通网络优化论文主线。",
    "narrative": "2507692 将 Baltimore 交通系统抽象为道路、公交和关键桥梁的多层网络，先评估局部失效对 OD 连通性和绕行成本的影响，再结合站点客流、道路暴露和聚类分区给出建设优先级。当前计算核已读取官方 drive edges/nodes、bus stops/routes 和 AADT 表，并输出桥梁移除影响、无候车亭高客流站点和高暴露道路，适合作为该论文的可验证整题复现。",
    "paper_methods": ["多层交通网络建模", "OD 最短路冲击分析", "公交站点客流优先级", "道路暴露指标", "聚类/分区式改造建议"],
    "repo_kernel": ["official COMAP Baltimore CSV", "drive graph connectivity and shortest paths", "bridge removal OD impacts", "bus shelter priority ranking", "traffic exposure safety ranking"],
    "experiment_fields": [
        {"key": "drive_nodes", "label": "道路网络节点数", "path": ["network_summary", "drive_nodes"]},
        {"key": "drive_edges", "label": "道路网络边数", "path": ["network_summary", "drive_edges"]},
        {"key": "disconnected_od_count", "label": "桥梁移除后断连 OD 数", "path": ["bridge_impact", "disconnected_od_count"]},
        {"key": "no_shelter_stops", "label": "无候车亭站点数", "path": ["bus_project", "no_shelter_stops"]},
        {"key": "top10_no_shelter_riders", "label": "前 10 个无候车亭站点客流", "path": ["bus_project", "top10_no_shelter_riders"]},
        {"key": "recommended_project", "label": "首要改造建议", "path": ["project_recommendations", "recommended_projects", 0, "project"]},
    ],
    "difference_from_advanced": "把 advanced 的路网、公交和安全结果整理为 2507692 的多层网络优化框架，强调道路层、公交层和桥梁失效层之间的交互，以及从图论指标到建设建议的整题叙事。",
    "limitations": ["当前复现使用官方数据和可验证图指标；原论文中的完整聚类参数、社区划分图和多目标权重可在后续单独重写。"],
}


if __name__ == "__main__":
    run(CONFIG, Path(__file__).resolve().parent)
