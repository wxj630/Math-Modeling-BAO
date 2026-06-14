from __future__ import annotations

import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(REPO_ROOT))

from mcm.outstanding_solutions.paper_guided_reproduction import run


CONFIG = {
    "problem_id": "2025-F",
    "code": "F",
    "real_solution_key": "ICM-F",
    "paper_id": "2517199",
    "paper_title": "Data-Driven Policy Effectiveness Evaluation and Country Specific Characteristic Based Cybercrime Prediction",
    "paper_source_ocr": "Outstanding_Solutions/MCM/OCR-results/F/2517199/2517199.md",
    "paper_source_pdf": "Outstanding_Solutions/MCM/PDF-2025/F/2517199.pdf",
    "selected_model": "国家政策特征面板 + VCDB 事件分布 + 描述性有效性评估",
    "scope": "用当前 ICM-F real solution 的 VCDB 样本、国家政策特征矩阵、人口经济指标和领导人备忘录，对齐 2517199 的数据驱动网络犯罪政策评价主线。",
    "narrative": "2517199 将网络犯罪问题拆成国家层面的事件分布、政策成熟度、国家特征和政策有效性评价。当前计算核使用 VCDB 公开事件样本、VERIS/VCDB 语义、World Bank 指标和透明政策特征矩阵，输出国家事件分布、政策成熟度、描述性相关性和非技术备忘录；虽然题目有政策解释成分，但这些表格与图像可以直接验证，因此纳入本轮 outstanding 覆盖。",
    "paper_methods": ["国家级网络犯罪事件面板", "政策成熟度特征", "国家人口经济特征", "政策有效性描述性评估", "领导人备忘录"],
    "repo_kernel": ["VCDB validated incident sample", "policy feature matrix", "cyber country panel", "demographic correlations", "nontechnical leader memo"],
    "experiment_fields": [
        {"key": "records_used", "label": "VCDB 样本事件数", "path": ["cybercrime_distribution", "records_used"]},
        {"key": "country_count", "label": "覆盖国家数", "path": ["cybercrime_distribution", "country_count"]},
        {"key": "top_target_country", "label": "样本中事件最多国家", "path": ["cybercrime_distribution", "top_target_countries", 0, "country"]},
        {"key": "mature_policy_mean_incidents", "label": "成熟政策组平均事件数", "path": ["policy_effectiveness", "mature_policy_mean_incidents"]},
        {"key": "developing_policy_mean_incidents", "label": "发展中政策组平均事件数", "path": ["policy_effectiveness", "developing_policy_mean_incidents"]},
        {"key": "strongest_descriptive_association", "label": "最强描述性关联变量", "path": ["demographic_correlations", "strongest_descriptive_association", 0, "variable"]},
    ],
    "difference_from_advanced": "把 advanced 的政策矩阵、国家面板和相关性结果组织为 2517199 的数据驱动政策评价框架，明确把偏论述题中可计算、可复查的部分沉淀为表格和结果。",
    "limitations": ["VCDB 是公开报告样本而非全球犯罪普查；当前复现只做描述性评价，不把相关性解释为因果效果。"],
}


if __name__ == "__main__":
    run(CONFIG, Path(__file__).resolve().parent)
