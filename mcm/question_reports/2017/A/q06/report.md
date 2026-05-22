# 2017-A q06：ZRA 摘要报告与推荐策略

## 题目原问
Submit a standard summary sheet, a 1-2 page brief assessment report, and the main solution for Requirement 2.

## 适合模型
把三方案决策矩阵、推荐小坝数量、坝址、正常/极端调度、暴露限制和模型局限整理为 ZRA 管理层可读报告。对应模型：工程政策报告、执行摘要、模型限制说明。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2017`。
- 行数/记录数：{'official_problem_parameters': 5}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### Kariba 三方案简短评估
- 管理建议：Option 1 is a near-term risk bridge, but Option 3 is the strategic option if ZRA can manage multi-site construction and ecological constraints.

| option | description | normalized_cost | implementation_years | construction_disruption | safety_improvement | water_management_flexibility | benefit_score | benefit_cost_ratio |
|---|---|---|---|---|---|---|---|---|
| Option 1 | Repairing the existing Kariba Dam | 42.0 | 4 | 0.28 | 0.48 | 0.34 | 0.279 | 0.664286 |
| Option 2 | Rebuilding the existing Kariba Dam | 96.0 | 8 | 0.66 | 0.82 | 0.58 | 0.44 | 0.458333 |
| Option 3 | Removing Kariba Dam and replacing it with 10 to 20 smaller dams | 118.0 | 11 | 0.78 | 0.88 | 0.91 | 0.5585 | 0.473305 |

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

### ZRA 管理层简报
Brief assessment for ZRA management:

ZRA asked for a two-page comparison of repairing Kariba, rebuilding Kariba, and replacing Kariba with 10-20 smaller dams. Repair is the lowest-cost bridge, rebuild is the single-dam safety reset, and Option 3 provides the highest flexibility. In this transparent scoring model, Option 3 has the highest benefit score, while the detailed Option 3 design recommends 15 smaller dams with water management index 103.110093. Because the official statement does not provide engineering cost or hydrology tables, all costs and capacities are normalized planning assumptions.

## 模型限制
- 这是可复现的官方题面参数 Zambezi River 水库群规划实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中三种选项、10-20 座小坝、同等或更高水量管理能力、正常/极端流量和暴露限制等要求。
- 成本、坝址坐标、容量、流量指数和暴露天数是显式工程规划假设，不是实测水文或施工数据；正式论文应补充 Zambezi 历史径流、Kariba 库容曲线、生态影响、地形地质、移民和工程造价数据校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2017/A/q06/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2017/A/q06/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2017/A/q06/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2017/A/q06`
