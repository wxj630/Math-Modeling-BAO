# 2017-A q05：极端条件暴露区域与时长限制

## 题目原问
Include information addressing restrictions regarding locations and lengths of time that different areas of the Zambezi River should be exposed to the most detrimental effects of extreme conditions.

## 适合模型
把河道分成 upstream lake margin、mid-river farmland、urban low banks、hydropower intake reaches、delta wetlands，给出 flood/low-water 最大暴露天数和原因。对应模型：风险分区、暴露约束、韧性规划。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted/2017`。
- 行数/记录数：{'official_problem_parameters': 5}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 极端流量指导

| scenario | flow_index | action | zra_guidance |
|---|---|---|---|
| maximum_expected_discharge | 100 | open upstream pre-release gates and enforce downstream rise-rate cap | activate flood command center and evacuate exposed low banks |
| high_flood | 88 | stagger mid-river releases and maximize flood-buffer storage | reduce synchronized peaks across adjacent segments |
| low_flow | 28 | ration hydropower peaking and release ecological minimum flow | prioritize drinking water, sanitation, and critical irrigation |
| minimum_expected_discharge | 12 | enter emergency drought rule curve and suspend discretionary releases | protect health and ecosystem refuges until inflow recovers |

### 极端条件暴露限制

| segment | max_flood_exposure_days | max_low_water_exposure_days | reason |
|---|---|---|---|
| upstream_lake_margin | 10 | 45 | slope stability and shoreline settlement risk |
| mid_river_farmland | 6 | 35 | crop and soil damage |
| urban_low_banks | 3 | 30 | public safety and sanitation |
| hydropower_intake_reaches | 7 | 21 | turbine intake reliability |
| delta_wetlands | 14 | 25 | ecological stress and salinity intrusion |

## 模型限制
- 这是可复现的官方题面参数 Zambezi River 水库群规划实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中三种选项、10-20 座小坝、同等或更高水量管理能力、正常/极端流量和暴露限制等要求。
- 成本、坝址坐标、容量、流量指数和暴露天数是显式工程规划假设，不是实测水文或施工数据；正式论文应补充 Zambezi 历史径流、Kariba 库容曲线、生态影响、地形地质、移民和工程造价数据校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2017/A/q05/solution.py`

## 输出
- `mcm/question_results/2017/A/q05/result.json`
- `mcm/question_reports/2017/A/q05/report.md`
- `mcm/question_artifacts/2017/A/q05`
