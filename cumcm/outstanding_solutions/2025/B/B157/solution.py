from __future__ import annotations

import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(REPO_ROOT))

from cumcm.outstanding_solutions.paper_guided_reproduction import run


CONFIG = {
    "problem_id": "2025-B",
    "code": "B",
    "paper_id": "B157",
    "paper_title": "碳化硅外延层厚度的双光束和多光束干涉法测量研究",
    "paper_source_ocr": "Outstanding_Solutions/CUMCM/OCR-results/B157/B157.md",
    "paper_source_pdf": "Outstanding_Solutions/CUMCM/PDF-2025/B157.pdf",
    "selected_model": "Snell/Fresnel 干涉模型 + FFT 初值 + 非线性最小二乘 + 多光束修正",
    "scope": "用当前 2025-B advanced 的干涉模型、厚度反演和多光束讨论结果，对齐 B157 的双光束/多光束统一测厚框架。",
    "narrative": "B157 先从 Snell 定律和 Fresnel 反射系数推导双光束干涉，再用 Cauchy 色散、FFT 初值和非线性最小二乘反演厚度，最后讨论 Airy 多光束干涉对精度的影响。当前 advanced 覆盖模型推导、算法设计和多光束影响三个问题，可组织成完整测厚复现链。",
    "paper_methods": ["Snell 入射角修正", "Fresnel 反射与 Cauchy 色散", "FFT 周期初值", "非线性最小二乘联合拟合", "Airy 多光束修正"],
    "difference_from_advanced": "把逐问 advanced 的厚度公式、算法和多光束讨论统一成 B157 的物理反演模型链，并保留逐问实验摘要。",
    "limitations": ["当前复现使用已有 advanced 实验表；原论文中的残差正态性检验和双角联合全参拟合可后续细化。"],
}


if __name__ == "__main__":
    run(CONFIG, Path(__file__).resolve().parent)
