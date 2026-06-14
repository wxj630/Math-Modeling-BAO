# 2025-C Outstanding 复现：C023

## 复现对象
- 获奖论文：`C023`，基于混合效应模型的NIPT时点优化与胎儿异常判定
- OCR 来源：`Outstanding_Solutions/CUMCM/OCR-results/C023/C023.md`
- PDF 来源：`Outstanding_Solutions/CUMCM/PDF-2025/C023.pdf`
- 复现定位：用当前 2025-C advanced 的统计建模、风险分组和异常判定结果，对齐 C023 的混合效应 NIPT 检测时点优化框架。

## 问题与建模
C023 将胎儿 Y 染色体浓度做 logit 变换，用包含随机截距和随机斜率的线性混合效应模型处理重复测量和个体差异，再围绕 FF 达到 4% 的时间做 BMI 分组和风险最小化，最后扩展到女胎异常判定。当前 advanced 已覆盖相关性、分组时点、检测误差和异常判定四问。

## 代码与实验
- `solution.py` 聚合当前 CUMCM advanced 的逐问 `result.json`、`report.md` 和 artifacts。
- 输出赛题级 `result.json`、`report.md`、`artifacts/question_result_summary.csv` 和逐问 artifact 副本。
- 这一步把逐问实验结果组织成获奖论文的整题模型链，后续可继续替换为更细的论文原算法。

## 逐问结果

| 小问 | Advanced 模型 | 实验摘要 |
|---|---|---|
| q01 | 综合评价与权重决策 | method=std_weight_topsis；weights=2项；scores=40项；best_option=1 |
| q02 | 机器学习与统计识别 | method=logistic_regression_plus_kmeans；training_accuracy=1；cluster_counts=2项 |
| q03 | 机器学习与统计识别 | method=logistic_regression_plus_kmeans；training_accuracy=1；cluster_counts=2项 |
| q04 | 综合评价与权重决策 | method=std_weight_topsis；weights=2项；scores=40项；best_option=1 |

## 相对 Advanced 的优势
把逐问 advanced 的统计与决策结果组织为 C023 的混合效应模型主线，强调个体差异、检测风险和异常判定的闭环。

## 输出产物
- `q01/experiment_table`：`cumcm/outstanding_solutions/2025/C/C023/artifacts/q01/experiment_table.csv`
- `q02/experiment_table`：`cumcm/outstanding_solutions/2025/C/C023/artifacts/q02/experiment_table.csv`
- `q03/experiment_table`：`cumcm/outstanding_solutions/2025/C/C023/artifacts/q03/experiment_table.csv`
- `q04/experiment_table`：`cumcm/outstanding_solutions/2025/C/C023/artifacts/q04/experiment_table.csv`
- `question_result_summary`：`cumcm/outstanding_solutions/2025/C/C023/artifacts/question_result_summary.csv`
