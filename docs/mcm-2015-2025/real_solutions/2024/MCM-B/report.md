# 2024 MCM-B Searching for Submersibles

## 数据真实性
- 官方来源：`docs/mcm-2015-2025/official_assets_extracted/2024/Searching for Submersibles.pdf`。
- 本题无 COMAP 数值附件；脚本只使用官方 PDF 任务约束和显式救援预案情景，不使用随机占位数据。
- `scenario_assumptions` 是可替换的确定性预案参数，不是声称采集到的真实事故观测。

## 每问建模与结果
### Q1 Locate
- 模型：current-driven dead-reckoning ellipse with two vertical states: seafloor-resting and neutral-buoyancy drifting。
- 12 小时不确定区域：16.9261 km^2。
- 24 小时不确定区域：62.5273 km^2。
- 减小不确定性的遥测：
- acoustic pinger range/bearing packet：horizontal range and bearing from host ship。
- depth and pressure time series：distinguishes seafloor contact from neutral-buoyancy drift。
- inertial dead-reckoning summary：motion after last GPS/USBL fix。
- battery, ballast, and propulsion health flags：likely mobility, ascent ability, and rescue urgency。
- local current and temperature-density observations：drift model and density-layer uncertainty。

### Q2 Prepare
- 模型：multi-criteria equipment scoring over coverage, detection quality, readiness, usage cost, and maintenance burden。
- 推荐：The host ship should carry acoustic localization, drop beacons, a side-scan option, and an inspection ROV; heavier lift and intervention assets can be pre-contracted for rescue-vessel arrival.

### Q3 Search
- 模型：Bayesian-style survival update with deterministic swept-area coverage over the official location-model uncertainty ellipse。
- 24 小时发现概率：0.7812。
- 初始部署点：
- P0 predicted center：east=2.509 km, north=1.567 km，deploy USBL and first drop beacon。
- P1 down-current ellipse focus：east=4.113 km, north=2.57 km，start creeping-line sonar along drift axis。
- P2 up-current ellipse focus：east=1.422 km, north=0.888 km，backtrack possible powerless descent path。
- P3 cross-current high-uncertainty edge：east=3.238 km, north=0.399 km，cover terrain and density-current ambiguity。
- P4 opposite cross-current edge：east=1.779 km, north=2.736 km，complete LBL bracket and close acoustic geometry。

### Q4 Extrapolate
- 加勒比海洋流不确定性倍数：1.35。
- 多潜水器协调规则：assign each submersible a unique acoustic code, maintain non-overlapping safety corridors, and partition the search posterior into Voronoi sectors around last confirmed fixes。

## 给监管方备忘录核心句
Memo to the Greek government: MCMS approval should require an auditable lost-submersible plan with periodic acoustic telemetry, a host-ship localization kit, preplanned deployment points, a probability-updated search log, and a rescue-vessel mobilization trigger when the 12-hour posterior still leaves substantial uncertainty.

## 输出产物
- `position_uncertainty.csv`：随时间扩张的位置不确定性椭圆。
- `equipment_tradeoffs.csv`：主船与救援装备的覆盖、成本、维护和准备度权衡。
- `search_probability.csv`：随时间累计搜索后的发现概率。
- `search_plan.png`：搜索椭圆、部署点和发现概率曲线。
