from __future__ import annotations

import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(REPO_ROOT))

from cumcm.outstanding_solutions.paper_guided_reproduction import run


CONFIG = {
    "problem_id": "2025-C",
    "code": "C",
    "paper_id": "C023",
    "paper_title": "基于混合效应模型的NIPT时点优化与胎儿异常判定",
    "paper_source_ocr": "Outstanding_Solutions/CUMCM/OCR-results/C023/C023.md",
    "paper_source_pdf": "Outstanding_Solutions/CUMCM/PDF-2025/C023.pdf",
    "selected_model": "logit 变换 + 线性混合效应模型 + 达标时间优化 + 异常判定",
    "scope": "用当前 2025-C advanced 的统计建模、风险分组和异常判定结果，对齐 C023 的混合效应 NIPT 检测时点优化框架。",
    "narrative": "C023 将胎儿 Y 染色体浓度做 logit 变换，用包含随机截距和随机斜率的线性混合效应模型处理重复测量和个体差异，再围绕 FF 达到 4% 的时间做 BMI 分组和风险最小化，最后扩展到女胎异常判定。当前 advanced 已覆盖相关性、分组时点、检测误差和异常判定四问。",
    "paper_methods": ["logit(FF) 响应变量", "GA/BMI 二次项", "随机截距与随机斜率 LMM", "最早达标时间优化", "女胎异常综合判定"],
    "difference_from_advanced": "把逐问 advanced 的统计与决策结果组织为 C023 的混合效应模型主线，强调个体差异、检测风险和异常判定的闭环。",
    "limitations": ["当前复现聚合已有 advanced 结果；REML/MLE 参数估计、似然比检验和 ICC 可在后续单独重写。"],
}


if __name__ == "__main__":
    run(CONFIG, Path(__file__).resolve().parent)
