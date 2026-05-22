# 2025-A q07：材料来源一致性指导

## 题目原问
Can the source of the material be determined? For example, if stone is used is the wear consistent with materials from a quarry the archaeologist believes is the original source or if wood was used is the wear consistent with the age and type of trees that are assumed to be used?

## 适合模型
给出石材/木材的非破坏材料代理测量流程：硬度、密度、纹理、工具痕和反推磨损系数必须与候选采石场或木材参考范围重叠。

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

### 材料来源判断
- 总原则：compare non-destructive hardness/density proxies and observed wear rate against candidate quarry or timber reference samples。

#### 石材流程

- photograph and map stone color, grain, bedding direction, and tool marks
- measure rebound/scratch hardness and ultrasonic/density proxy without coring
- compute implied wear coefficient from age and traffic priors
- accept a quarry source only if hardness/density/geology and implied wear coefficient overlap the reference range

#### 木材流程

- identify species from visible grain and non-destructive imaging where permitted
- compare surface hardness and wear direction to species-specific wear literature
- use construction-age prior; do not infer tree age from tread wear alone

## 模型限制
- 这是可复现的官方题面参数和测量工作流实验，适合处理没有独立 CSV/XLSX 附件的 MCM 题；它不是随机造数，也不是虚构真实观测。
- `worked_example_assumptions` 只是展示考古队填完非破坏测量表后如何反演；正式论文应把现场测量值替换进模板，并对材料磨损系数做来源校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2025/A/q07/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2025/A/q07/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2025/A/q07/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2025/A/q07`
