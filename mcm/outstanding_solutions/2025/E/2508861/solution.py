from __future__ import annotations

import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(REPO_ROOT))

from mcm.outstanding_solutions.paper_guided_reproduction import run


CONFIG = {
    "problem_id": "2025-E",
    "code": "E",
    "real_solution_key": "ICM-E",
    "paper_id": "2508861",
    "paper_title": "Symphony of Eco-Agriculture: A New Music of Harmonious Coexistence",
    "paper_source_ocr": "Outstanding_Solutions/MCM/OCR-results/E/2508861/2508861.md",
    "paper_source_pdf": "Outstanding_Solutions/MCM/PDF-2025/E/2508861.pdf",
    "selected_model": "FATE 生态系统动力学 + COMAP 有机农业转型规划",
    "scope": "用当前 ICM-E real solution 的森林转农田食物网、月度动力系统、情景仿真和有机转型建议，对齐 2508861 的生态农业获奖论文主线。",
    "narrative": "2508861 围绕森林转农田后的生态系统稳定性、农药/除草剂干预、物种回归和有机农业过渡建立动力学模型。当前计算核已经构造作物、野生植物、害虫、益虫、蝙蝠、鸟类、土壤健康和化学投入的食物网，按月模拟多种管理情景，并输出生态稳定性、净收益和转型建议，因此可以作为该论文的可验证复现底座。",
    "paper_methods": ["食物网状态变量", "季节性差分方程", "化学控制与自然过程耦合", "有机农业情景前沿", "给农户的政策建议"],
    "repo_kernel": ["food web interaction edges", "monthly deterministic dynamics", "chemical-removal and bat habitat scenarios", "organic transition tradeoff frontier", "farmer-facing letter"],
    "experiment_fields": [
        {"key": "food_web_node_count", "label": "食物网节点数", "path": ["food_web_model", "nodes"], "transform": "count"},
        {"key": "months_simulated", "label": "仿真月数", "path": ["seasonal_dynamics", "months"]},
        {"key": "baseline_stability_score", "label": "化学基线生态稳定性", "path": ["natural_processes", "newly_cleared_baseline", "ecosystem_stability_score"]},
        {"key": "recommended_transition", "label": "推荐有机转型策略", "path": ["organic_scenarios", "recommended_transition"]},
        {"key": "top_scenario", "label": "综合评分最高情景", "path": ["organic_scenarios", "scenario_rankings", 0, "scenario"]},
        {"key": "top_scenario_sustainability", "label": "最高情景可持续性得分", "path": ["organic_scenarios", "scenario_rankings", 0, "sustainability_score"]},
    ],
    "difference_from_advanced": "把 advanced 的食物网仿真和有机情景比较组织为 2508861 的生态农业动力系统，突出自然过程、农业决策、物种回归和农户建议之间的递进关系。",
    "limitations": ["当前复现采用透明参数化的差分系统；原论文中的 FATE/COMAP 细节、参数校准和更复杂稳定性分析可在后续扩展。"],
}


if __name__ == "__main__":
    run(CONFIG, Path(__file__).resolve().parent)
