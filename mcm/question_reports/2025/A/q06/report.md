# 2025-A q06：维修或翻新检测

## 题目原问
What repairs or renovations have been conducted?

## 适合模型
相邻踏步磨损跳变、patch boundary score 和 tool-mark 指标加权，输出可能替换/补丁踏步候选表。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted`。
- 行数/记录数：{'official_parameters': 3}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 非破坏测量方案
- 原则：non_destructive, low_cost, small_team_minimal_tools。
- 测量模板：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/real_solutions/2025/MCM-A/artifacts/measurement_template.csv`。

#### 推荐字段

| field | tool |
|---|---|
| step_id | field sheet |
| tread_width_cm | tape measure |
| tread_depth_cm | tape measure |
| riser_height_cm | tape measure |
| center_wear_depth_mm | straightedge + feeler gauge + scaled photo |
| left_wear_depth_mm | straightedge + feeler gauge + scaled photo |
| right_wear_depth_mm | straightedge + feeler gauge + scaled photo |
| front_edge_rounding_mm | caliper + scaled close photo |
| back_edge_rounding_mm | caliper + scaled close photo |
| slope_up_direction_deg | phone inclinometer |
| surface_hardness_proxy | portable rebound/scratch proxy |
| material_density_proxy | published material match or ultrasonic proxy |

### 维修或翻新检测
- 模型：adjacent tread discontinuity + patch boundary + tool-mark scoring。
- 候选数量：2。

| step_id | wear_jump_mm | patch_boundary_score | tool_marks_present | candidate_score |
|---|---|---|---|---|
| 8 | -2.4 | 5 | 1 | 5.35 |
| 9 | 1.4 | 2 | 1 | 3.0 |

## 模型限制
- 这是可复现的官方题面参数和测量工作流实验，适合处理没有独立 CSV/XLSX 附件的 MCM 题；它不是随机造数，也不是虚构真实观测。
- `worked_example_assumptions` 只是展示考古队填完非破坏测量表后如何反演；正式论文应把现场测量值替换进模板，并对材料磨损系数做来源校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2025/A/q06/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2025/A/q06/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2025/A/q06/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2025/A/q06`
