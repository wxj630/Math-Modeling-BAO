from __future__ import annotations

import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(REPO_ROOT))

from cumcm.outstanding_solutions.paper_guided_reproduction import run


CONFIG = {
    "problem_id": "2025-E",
    "code": "E",
    "paper_id": "E030",
    "paper_title": "基于姿态识别的AI辅助智能体测研究",
    "paper_source_ocr": "Outstanding_Solutions/CUMCM/OCR-results/E030/E030.md",
    "paper_source_pdf": "Outstanding_Solutions/CUMCM/PDF-2025/E030.pdf",
    "selected_model": "关键点插补/平滑 + 起跳落地检测 + 相关性分析 + 成绩预测建议",
    "scope": "用当前 2025-E advanced 的关键点几何、FFT 信号特征、成绩预测和训练建议结果，对齐 E030 的 AI 辅助立定跳远体测框架。",
    "narrative": "E030 的主线是先对人体关键点序列做插补、平滑和尺度统一，再识别起跳/落地时刻、提取滞空阶段动作特征，并结合体质数据分析成绩影响因素，最后给出运动者 11 的成绩预测和训练建议。当前 advanced 已按四个问题输出关键点几何拟合、信号特征、预测和建议结果，可作为该获奖论文的整题复现入口。",
    "paper_methods": ["人体关键点序列预处理", "起跳/落地事件检测", "滞空阶段运动学描述", "Spearman 相关与多元线性回归", "个体化训练建议"],
    "difference_from_advanced": "把逐问 advanced 的姿态/信号结果组织成 E030 的 AI 体测模型链，强调从动作识别到影响因素、成绩预测和训练建议的递进闭环。",
    "limitations": ["当前复现聚合已有 advanced 结果；E030 中的关键点缺失插补、Savitzky-Golay 平滑和完整回归系数可在后续单独重写。"],
}


if __name__ == "__main__":
    run(CONFIG, Path(__file__).resolve().parent)
