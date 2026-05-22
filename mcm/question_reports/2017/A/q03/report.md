# 2017-A q03：多坝系统正常水文周期调度策略

## 题目原问
Include a strategy for modulating the water flow through the new multiple dam system that provides a reasonable balance between safety and costs under known or predicted normal water cycles.

## 适合模型
把 normal wet-season 和 normal dry-season 转成 flow_index 区间，制定上游蓄水、中游错峰、下游生态脉冲和低流量补给规则。对应模型：水库群调度、规则曲线、系统动力学、风险-成本权衡。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2017`。
- 行数/记录数：{'official_problem_parameters': 5}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 10-20 座小坝系统设计
- Kariba reference index：100.0。
- 推荐小坝数量：15。
- 推荐系统 water management index：103.110093。
- 说明：Use a distributed 15-dam system: enough redundancy to match Kariba-level management while avoiding the coordination penalty of 18-20 dams.

#### 坝址计划

| dam_id | river_coordinate_0_100 | segment | local_storage_share_pct | primary_role |
|---|---|---|---|---|
| D01 | 6.0 | upstream_lake_control | 7.2 | replace Kariba storage and regulate lake-level transitions |
| D02 | 12.29 | upstream_lake_control | 7.2 | replace Kariba storage and regulate lake-level transitions |
| D03 | 18.57 | upstream_lake_control | 7.2 | replace Kariba storage and regulate lake-level transitions |
| D04 | 24.86 | upstream_lake_control | 7.2 | replace Kariba storage and regulate lake-level transitions |
| D05 | 31.14 | mid_river_flood_buffer | 7.2 | attenuate flood peaks and distribute release timing |
| D06 | 37.43 | mid_river_flood_buffer | 7.2 | attenuate flood peaks and distribute release timing |
| D07 | 43.71 | mid_river_flood_buffer | 7.2 | attenuate flood peaks and distribute release timing |
| D08 | 50.0 | mid_river_flood_buffer | 7.2 | attenuate flood peaks and distribute release timing |
| D09 | 56.29 | downstream_power_and_irrigation | 6.133 | support low-flow releases for users |
| D10 | 62.57 | downstream_power_and_irrigation | 6.133 | support low-flow releases for users |
| D11 | 68.86 | downstream_power_and_irrigation | 6.133 | support low-flow releases for users |
| D12 | 75.14 | downstream_power_and_irrigation | 6.133 | support low-flow releases for users |
| D13 | 81.43 | delta_ecology_protection | 6.133 | limit extreme exposure in sensitive downstream reaches |
| D14 | 87.71 | delta_ecology_protection | 6.133 | limit extreme exposure in sensitive downstream reaches |
| D15 | 94.0 | delta_ecology_protection | 6.133 | limit extreme exposure in sensitive downstream reaches |

### 多坝系统水流调度策略
- 协调原则：Operate the dam chain as staggered buffers rather than independent reservoirs.

| condition | trigger_flow_index | release_rule | safety_cost_tradeoff |
|---|---|---|---|
| normal wet-season inflow | 60-85 | store first 30% of surplus upstream, pass 50% through mid-river buffers, reserve 20% for downstream ecological pulse | moderate storage with low emergency spill risk |
| normal dry-season inflow | 35-60 | coordinate weekly low-flow support from downstream and mid-river dams while preserving upstream reserve | protect water users while limiting turbine and ecology stress |
| flood emergency | >85 | pre-release upstream dams, stagger mid-river gates by 8-12 hours, cap downstream rise rate | higher short-term spill cost to avoid synchronized flood peak |
| prolonged low-water emergency | <35 for 30 days | shift to drought rationing, suspend noncritical hydropower peaking, protect drinking water and ecological minimum flow | economic generation loss accepted to preserve health and minimum river function |

## 模型限制
- 这是可复现的官方题面参数 Zambezi River 水库群规划实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中三种选项、10-20 座小坝、同等或更高水量管理能力、正常/极端流量和暴露限制等要求。
- 成本、坝址坐标、容量、流量指数和暴露天数是显式工程规划假设，不是实测水文或施工数据；正式论文应补充 Zambezi 历史径流、Kariba 库容曲线、生态影响、地形地质、移民和工程造价数据校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2017/A/q03/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2017/A/q03/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2017/A/q03/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2017/A/q03`
