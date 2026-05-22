# 2025-A q03：并排或单列使用模式

## 题目原问
How many people used the stairs simultaneously? For example, did pairs of people climb the stairs side-by-side or did they travel single file?

## 适合模型
把横截面磨损剖面拆成中心带和左右侧带，使用侧带/中心磨损比估计 single-file、side-by-side 或 mixed 的同时使用模式。

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

### 磨损反演结果
#### 使用频率
- 模型：inverse Archard-style wear balance: passages = observed_depth / material_wear_rate。
- 中心磨损中位数：4.3 mm。
- 累计通行量：9555556。
- 日均使用人数：72.67。

#### 方向偏好
- 模型：front/back edge rounding asymmetry plus along-tread slope sign。
- 前/后缘圆角比：1.497。
- 偏好方向：up。

#### 同时使用
- 模型：cross-sectional wear-band shape: center-dominant versus side-band wear。
- 侧带/中心磨损比：0.526。
- 模式：mixed。

## 模型限制
- 这是可复现的官方题面参数和测量工作流实验，适合处理没有独立 CSV/XLSX 附件的 MCM 题；它不是随机造数，也不是虚构真实观测。
- `worked_example_assumptions` 只是展示考古队填完非破坏测量表后如何反演；正式论文应把现场测量值替换进模板，并对材料磨损系数做来源校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2025/A/q03/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2025/A/q03/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2025/A/q03/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2025/A/q03`
