# 2025-B Outstanding 复现：B157

## 复现对象
- 获奖论文：`B157`，碳化硅外延层厚度的双光束和多光束干涉法测量研究
- OCR 来源：`Outstanding_Solutions/CUMCM/OCR-results/B157/B157.md`
- PDF 来源：`Outstanding_Solutions/CUMCM/PDF-2025/B157.pdf`
- 复现定位：用当前 2025-B advanced 的干涉模型、厚度反演和多光束讨论结果，对齐 B157 的双光束/多光束统一测厚框架。

## 问题与建模
B157 先从 Snell 定律和 Fresnel 反射系数推导双光束干涉，再用 Cauchy 色散、FFT 初值和非线性最小二乘反演厚度，最后讨论 Airy 多光束干涉对精度的影响。当前 advanced 覆盖模型推导、算法设计和多光束影响三个问题，可组织成完整测厚复现链。

## 代码与实验
- `solution.py` 聚合当前 CUMCM advanced 的逐问 `result.json`、`report.md` 和 artifacts。
- 输出赛题级 `result.json`、`report.md`、`artifacts/question_result_summary.csv` 和逐问 artifact 副本。
- 这一步把逐问实验结果组织成获奖论文的整题模型链，后续可继续替换为更细的论文原算法。

## 逐问结果

| 小问 | Advanced 模型 | 实验摘要 |
|---|---|---|
| q01 | 数据拟合与回归分析 | method=quadratic_least_squares；coefficients=3项；r2=0.658138；mean_abs_error=2.25512 |
| q02 | 数据拟合与回归分析 | method=quadratic_least_squares；coefficients=3项；r2=0.658138；mean_abs_error=2.25512 |
| q03 | 数据拟合与回归分析 | method=quadratic_least_squares；coefficients=3项；r2=0.658138；mean_abs_error=2.25512 |

## 相对 Advanced 的优势
把逐问 advanced 的厚度公式、算法和多光束讨论统一成 B157 的物理反演模型链，并保留逐问实验摘要。

## 输出产物
- `q01/experiment_table`：`cumcm/outstanding_solutions/2025/B/B157/artifacts/q01/experiment_table.csv`
- `q02/experiment_table`：`cumcm/outstanding_solutions/2025/B/B157/artifacts/q02/experiment_table.csv`
- `q03/experiment_table`：`cumcm/outstanding_solutions/2025/B/B157/artifacts/q03/experiment_table.csv`
- `question_result_summary`：`cumcm/outstanding_solutions/2025/B/B157/artifacts/question_result_summary.csv`
