# 2025-A q05：楼梯年龄与可靠性

## 题目原问
What is the age of the stairwell and how reliable is the estimate?

## 适合模型
在材料磨损系数和可能日均交通量上做确定性网格，输出与历史年龄先验重叠的年龄区间和可靠性等级。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted`。
- 行数/记录数：{'official_parameters': 3}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### Worked Example 假设
- 用途：deterministic calibration example showing how a filled measurement sheet is inverted; values are not official observations。
- 材料：medium limestone / sandstone-like tread material。
- 磨损系数：0.045 mm / 100k passages。
- 交通反演候选年龄：360 年。
- 几何：{'steps': 11, 'mean_tread_width_cm': 158.0, 'mean_tread_depth_cm': 32.0, 'mean_riser_height_cm': 16.5}。
- 这些数值是确定性演示参数，不是官方观测表。

### 年龄与可靠性
- 模型：deterministic uncertainty grid over material wear coefficient and plausible daily traffic。
- 年龄估计：340.3 年。
- 合理区间：[283.6, 397.0] 年。
- 可靠性：medium: age is identifiable only jointly with material wear rate and daily traffic prior。
- 合理网格数：2 / 30。

## 模型限制
- 这是可复现的官方题面参数和测量工作流实验，适合处理没有独立 CSV/XLSX 附件的 MCM 题；它不是随机造数，也不是虚构真实观测。
- `worked_example_assumptions` 只是展示考古队填完非破坏测量表后如何反演；正式论文应把现场测量值替换进模板，并对材料磨损系数做来源校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2025/A/q05/solution.py`

## 输出
- `mcm/question_results/2025/A/q05/result.json`
- `mcm/question_reports/2025/A/q05/report.md`
- `mcm/question_artifacts/2025/A/q05`
