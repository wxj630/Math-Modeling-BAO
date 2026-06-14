from __future__ import annotations

import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(REPO_ROOT))

from cumcm.outstanding_solutions.paper_guided_reproduction import run


CONFIG = {
    "problem_id": "2025-A",
    "code": "A",
    "paper_id": "A196",
    "paper_title": "多情形下无人机烟幕遮蔽策略的建模与优化研究",
    "paper_source_ocr": "Outstanding_Solutions/CUMCM/OCR-results/A196/A196.md",
    "paper_source_pdf": "Outstanding_Solutions/CUMCM/PDF-2025/A196.pdf",
    "selected_model": "三维运动学 + 遮蔽判定 + 多情形投放优化",
    "scope": "用当前 2025-A advanced 的几何解析、优化搜索和逐问结果，对齐 A196 的运动学遮蔽判定与多情形投弹策略。",
    "narrative": "A196 的主线是先建立导弹、无人机、烟幕弹和云团中心的位置函数，再用布尔遮蔽判定计算有效遮蔽时长，随后从单机单弹扩展到单机多弹、多机单弹和多机多弹多目标优化。当前 advanced 已按五个问题输出几何解析和优化实验表，适合作为该获奖论文的可验证复现底座。",
    "paper_methods": ["三维运动学位置函数", "圆柱目标遮蔽判定", "二分查找/变步长搜索", "差分进化与分层任务分配"],
    "difference_from_advanced": "把逐问 advanced 的几何和优化结果组织成 A196 的整题模型链，突出单机单弹到多机多弹多目标的递进关系。",
    "limitations": ["当前复现聚合已有逐问结果；A196 中的精细二分证明和差分进化参数可在后续单独重写。"],
}


if __name__ == "__main__":
    run(CONFIG, Path(__file__).resolve().parent)
