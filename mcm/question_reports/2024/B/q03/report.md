# 2024-B q03：初始部署点、搜索路径与发现概率

## 题目原问
Search - Develop a model that will use information from your location model(s) to recommend initial points of deployment and search patterns for the equipment so as to minimize the time to location of a lost submersible. Determine the probability of finding the submersible as a function of time and accumulated search results.

## 适合模型
把位置椭圆转成部署点，按有效扫测面积累计更新发现概率 `1-exp(-swept_area/uncertainty_area)`，形成 24 小时搜索曲线。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted`。
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

### 搜索部署与发现概率
- 模型：Bayesian-style survival update with deterministic swept-area coverage over the official location-model uncertainty ellipse。
- 发现概率公式：`P_found(t)=1-exp(-sum_over_intervals(incremental_effective_swept_area/current_uncertainty_area))`。
- 12 小时发现概率：0.7489。
- 24 小时发现概率：0.7812。

#### 初始部署点

| point | east_km | north_km | purpose |
|---|---|---|---|
| P0 predicted center | 2.509 | 1.567 | deploy USBL and first drop beacon |
| P1 down-current ellipse focus | 4.113 | 2.57 | start creeping-line sonar along drift axis |
| P2 up-current ellipse focus | 1.422 | 0.888 | backtrack possible powerless descent path |
| P3 cross-current high-uncertainty edge | 3.238 | 0.399 | cover terrain and density-current ambiguity |
| P4 opposite cross-current edge | 1.779 | 2.736 | complete LBL bracket and close acoustic geometry |

#### 搜索模式

- 0-2 h: interrogate acoustic pingers from the host ship and deploy two LBL beacons around P0/P1
- 2-8 h: run creeping-line side-scan sonar along the drift-axis ellipse from P1 to P2
- 8-16 h: use ROV to inspect acoustic/sonar contacts and seafloor terrain traps
- 16-24 h: add AUV expanding-square search around remaining posterior mass if no confirmed contact

## 模型限制
- 这是可复现的官方题面参数搜索救援实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中的任务约束和显式确定性预案参数。
- 洋流、装备覆盖率和准备时间是可替换的场景参数，不是事故观测数据；正式论文应接入作业海区实时流场、测深、声学设备规格和演练记录校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2024/B/q03/solution.py`

## 输出
- `mcm/question_results/2024/B/q03/result.json`
- `mcm/question_reports/2024/B/q03/report.md`
- `mcm/question_artifacts/2024/B/q03`
