# 2021 MCM-B Fighting Wildfires

## 数据真实性
- 官方来源：`docs/mcm-2015-2025/official_assets/2021/Fighting Wildfires`。
- 本题无 COMAP 数值附件；脚本只使用官方题面中的无人机、无线电和任务参数，以及显式确定性火场情景。

## 推荐装备组合
- SSA drones：11.0；Radio repeater drones：2.0；cost：130000.0 AUD。
- 方法：grid search over SSA and radio-repeater drone counts balancing capability, safety, mission need, topography, fire size/frequency, and economics。

## 十年投影与中继布点
- 十年投影：increase extreme-event likelihood each year while drone unit cost remains constant, then add equipment if capability drops below the target band。
- 布点模型：terrain-adjusted coverage radius and EOC relay-chain count using the official 20 km repeater range。

## 预算请求摘录
Annotated Budget Request to the Victoria State Government: CFA Rapid Bushfire Response requests AUD 153400.0 for an initial drone division. The request purchases 11 SSA drones and 2 radio-repeater drones at the official AUD 10000 unit cost, plus a training and spares reserve. The mix balances surveillance, communications, topography, event size, event frequency, firefighter safety, and economics. A decade projection is included because increasing extreme fire likelihood can require extra equipment even when drone unit cost stays constant.

## 输出产物
- `drone_mix_optimization.csv`：SSA/Repeater 组合搜索。
- `decade_cost_projection.csv`：极端火灾概率变化下的十年成本。
- `repeater_location_plan.csv`：地形调整的中继无人机布点。
- `annotated_budget_request.csv`：预算条目与注释。
- `wildfire_budget_frontier.png`：预算-能力安全前沿图。
