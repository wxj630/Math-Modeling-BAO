from __future__ import annotations

import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(REPO_ROOT))

from cumcm.outstanding_solutions.paper_guided_reproduction import run


CONFIG = {
    "problem_id": "2025-D",
    "code": "D",
    "paper_id": "D037",
    "paper_title": "矿井突水水流漫延模型与逃生方案问题",
    "paper_source_ocr": "Outstanding_Solutions/CUMCM/OCR-results/D037/D037.md",
    "paper_source_pdf": "Outstanding_Solutions/CUMCM/PDF-2025/D037.pdf",
    "selected_model": "巷道图建模 + 水流漫延时间 + 动态 Dijkstra 逃生路径",
    "scope": "用当前 2025-D advanced 的图网络、水流传播和逃生路径结果，对齐 D037 的矿井突水动态漫延与实时逃生方案。",
    "narrative": "D037 将矿井巷道抽象为二维/三维图网络，先计算突水水流到达端点、铺满和充满时间，再把水位状态转化为动态边权，用实时 Dijkstra 设计矿工逃生路径；双突水点时再更新传播和逃生策略。当前 advanced 已覆盖四个小问的图网络和路径实验。",
    "paper_methods": ["二维/三维巷道图", "突水水流漫延时间", "BFS 平面/高度扩展", "实时动态 Dijkstra", "双突水点路径调整"],
    "difference_from_advanced": "把逐问 advanced 的水流和逃生结果组织为 D037 的动态网络主线，强调从单突水传播到双突水实时调整的递进。",
    "limitations": ["当前复现聚合已有 advanced 结果；D037 中铺水/封闭/断流三类模型的细节可后续逐段复写。"],
}


if __name__ == "__main__":
    run(CONFIG, Path(__file__).resolve().parent)
