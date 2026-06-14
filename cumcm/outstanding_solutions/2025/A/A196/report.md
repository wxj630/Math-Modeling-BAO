# 2025-A Outstanding 复现：A196

## 复现对象
- 获奖论文：`A196`，多情形下无人机烟幕遮蔽策略的建模与优化研究
- OCR 来源：`Outstanding_Solutions/CUMCM/OCR-results/A196/A196.md`
- PDF 来源：`Outstanding_Solutions/CUMCM/PDF-2025/A196.pdf`
- 复现定位：用当前 2025-A advanced 的几何解析、优化搜索和逐问结果，对齐 A196 的运动学遮蔽判定与多情形投弹策略。

## 问题与建模
A196 的主线是先建立导弹、无人机、烟幕弹和云团中心的位置函数，再用布尔遮蔽判定计算有效遮蔽时长，随后从单机单弹扩展到单机多弹、多机单弹和多机多弹多目标优化。当前 advanced 已按五个问题输出几何解析和优化实验表，适合作为该获奖论文的可验证复现底座。

## 代码与实验
- `solution.py` 聚合当前 CUMCM advanced 的逐问 `result.json`、`report.md` 和 artifacts。
- 输出赛题级 `result.json`、`report.md`、`artifacts/question_result_summary.csv` 和逐问 artifact 副本。
- 这一步把逐问实验结果组织成获奖论文的整题模型链，后续可继续替换为更细的论文原算法。

## 逐问结果

| 小问 | Advanced 模型 | 实验摘要 |
|---|---|---|
| q01 | 几何解析与运动学参数方程 | method=least_squares_geometry_fit；center=2项；radius=4.28001；mean_squared_error=0.00344799 |
| q02 | 几何解析与运动学参数方程 | method=least_squares_geometry_fit；center=2项；radius=6.2946；mean_squared_error=0.00326825 |
| q03 | 规划优化与资源配置 | method=linear_programming；success=True；objective_max=36.1932；decision=6项 |
| q04 | 规划优化与资源配置 | method=linear_programming；success=True；objective_max=36.8528；decision=6项 |
| q05 | 规划优化与资源配置 | method=linear_programming；success=True；objective_max=32.4554；decision=6项 |

## 相对 Advanced 的优势
把逐问 advanced 的几何和优化结果组织成 A196 的整题模型链，突出单机单弹到多机多弹多目标的递进关系。

## 输出产物
- `q01/experiment_table`：`cumcm/outstanding_solutions/2025/A/A196/artifacts/q01/experiment_table.csv`
- `q02/experiment_table`：`cumcm/outstanding_solutions/2025/A/A196/artifacts/q02/experiment_table.csv`
- `q03/experiment_table`：`cumcm/outstanding_solutions/2025/A/A196/artifacts/q03/experiment_table.csv`
- `q04/experiment_table`：`cumcm/outstanding_solutions/2025/A/A196/artifacts/q04/experiment_table.csv`
- `q05/experiment_table`：`cumcm/outstanding_solutions/2025/A/A196/artifacts/q05/experiment_table.csv`
- `question_result_summary`：`cumcm/outstanding_solutions/2025/A/A196/artifacts/question_result_summary.csv`
