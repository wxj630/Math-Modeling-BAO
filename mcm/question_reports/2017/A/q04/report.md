# 2017-A q04：洪水与长期低水位极端流量指导

## 题目原问
Provide guidance for emergency water flow situations, including flooding and/or prolonged low water conditions, from maximum expected discharges to minimum expected discharges.

## 适合模型
建立 maximum expected discharge、high flood、low flow、minimum expected discharge 四类情景，分别给出预泄、错峰、限制下游上升率、干旱配给和生态最小流量。对应模型：应急调度、洪水控制、干旱管理、情景分析。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2017`。
- 行数/记录数：{'official_problem_parameters': 5}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 多坝系统水流调度策略
- 协调原则：Operate the dam chain as staggered buffers rather than independent reservoirs.

| condition | trigger_flow_index | release_rule | safety_cost_tradeoff |
|---|---|---|---|
| normal wet-season inflow | 60-85 | store first 30% of surplus upstream, pass 50% through mid-river buffers, reserve 20% for downstream ecological pulse | moderate storage with low emergency spill risk |
| normal dry-season inflow | 35-60 | coordinate weekly low-flow support from downstream and mid-river dams while preserving upstream reserve | protect water users while limiting turbine and ecology stress |
| flood emergency | >85 | pre-release upstream dams, stagger mid-river gates by 8-12 hours, cap downstream rise rate | higher short-term spill cost to avoid synchronized flood peak |
| prolonged low-water emergency | <35 for 30 days | shift to drought rationing, suspend noncritical hydropower peaking, protect drinking water and ecological minimum flow | economic generation loss accepted to preserve health and minimum river function |

### 极端流量指导

| scenario | flow_index | action | zra_guidance |
|---|---|---|---|
| maximum_expected_discharge | 100 | open upstream pre-release gates and enforce downstream rise-rate cap | activate flood command center and evacuate exposed low banks |
| high_flood | 88 | stagger mid-river releases and maximize flood-buffer storage | reduce synchronized peaks across adjacent segments |
| low_flow | 28 | ration hydropower peaking and release ecological minimum flow | prioritize drinking water, sanitation, and critical irrigation |
| minimum_expected_discharge | 12 | enter emergency drought rule curve and suspend discretionary releases | protect health and ecosystem refuges until inflow recovers |

## 模型限制
- 这是可复现的官方题面参数 Zambezi River 水库群规划实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中三种选项、10-20 座小坝、同等或更高水量管理能力、正常/极端流量和暴露限制等要求。
- 成本、坝址坐标、容量、流量指数和暴露天数是显式工程规划假设，不是实测水文或施工数据；正式论文应补充 Zambezi 历史径流、Kariba 库容曲线、生态影响、地形地质、移民和工程造价数据校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2017/A/q04/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2017/A/q04/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2017/A/q04/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2017/A/q04`
