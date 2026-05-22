# 2024-B q01：失联潜水器位置预测与不确定性

## 题目原问
Locate - Develop a model(s) that predicts the location of the submersible over time. What are the uncertainties associated with these predictions? What information can the submersible periodically send to the host ship to decrease these uncertainties prior to an incident? What kinds of equipment would the submersible need to do so?

## 适合模型
官方 PDF 题面约束 + 失去通信/推进情景 + 洋流漂移-中性浮力/海底双状态位置椭圆 + 遥测信息对不确定性的削减清单。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted`。
- 行数/记录数：{'official_parameters': 15}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 潜水器位置预测模型
- 模型：current-driven dead-reckoning ellipse with two vertical states: seafloor-resting and neutral-buoyancy drifting。
- 12 小时不确定区域：16.9261 km^2。
- 24 小时不确定区域：62.5273 km^2。
- 12 小时预测中心：[2.5085, 1.5675] km。

#### 主要不确定性
- unknown vertical state: seafloor versus neutral buoyancy
- current magnitude and direction
- time since last accurate fix
- seafloor terrain trapping and density layers

#### 降低不确定性的遥测

| signal | equipment | uncertainty_reduced |
|---|---|---|
| acoustic pinger range/bearing packet | coded acoustic modem and emergency pinger | horizontal range and bearing from host ship |
| depth and pressure time series | pressure sensor with logged acoustic burst | distinguishes seafloor contact from neutral-buoyancy drift |
| inertial dead-reckoning summary | IMU, compass, Doppler velocity log where available | motion after last GPS/USBL fix |
| battery, ballast, and propulsion health flags | fault monitor tied to acoustic status messages | likely mobility, ascent ability, and rescue urgency |
| local current and temperature-density observations | compact current/CTD package | drift model and density-layer uncertainty |

## 模型限制
- 这是可复现的官方题面参数搜索救援实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中的任务约束和显式确定性预案参数。
- 洋流、装备覆盖率和准备时间是可替换的场景参数，不是事故观测数据；正式论文应接入作业海区实时流场、测深、声学设备规格和演练记录校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2024/B/q01/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2024/B/q01/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2024/B/q01/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2024/B/q01`
