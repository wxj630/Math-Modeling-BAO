# 2024-D q06：给 IJC 的一页备忘录

## 题目原问
Provide a one-page memo to IJC leadership communicating key model features and why they should select the model.

## 适合模型
把目标带控制器、官方历史数据、两坝出流约束、2017 高风险月份和 Lake Ontario 权衡浓缩为 IJC 决策备忘录。

## 数据与真实性
- 数据类型：official_comap_xlsx。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2024/Data- Great Lakes Water Problem/2024_Problem_D_Great_Lakes.xlsx`。
- 行数/记录数：{'records': 2548, 'level_records': 1380, 'flow_records': 1168}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 分月最优水位目标
- 方法：monthly historical median with interquartile operating band

| lake | annual_target_mean_m | mean_operating_band_width_m | seasonal_target_min_m | seasonal_target_max_m |
|---|---|---|---|---|
| Lake Erie | 174.203333 | 0.424583 | 174.02 | 174.36 |
| Lake Michigan and Lake Huron | 176.1375 | 0.669167 | 175.96 | 176.33 |
| Lake Ontario | 74.818333 | 0.2325 | 74.51 | 75.13 |
| Lake St. Clair | 174.986667 | 0.494167 | 174.85 | 175.15 |
| Lake Superior | 183.293333 | 0.381667 | 183.11 | 183.44 |

### 控制算法
- 规则：monthly median flow plus 900 cms per meter above target, clipped to historical 10th-90th percentile by month

| lake | control_flow | mean_abs_level_deviation_m | mean_abs_recommended_change_cms | max_recommended_change_cms |
|---|---|---|---|---|
| Lake Ontario | St. Lawrence River | 0.152681 | 136.499176 | 702.0 |
| Lake Superior | St. Mary's River | 0.186775 | 159.972069 | 449.218411 |

### Lake Ontario 专项
- 记录数：276。
- 高水位月份：71，低水位月份：71。
- 平均绝对偏离：0.152681 m。
- 与连接河流流量相关：{'Niagara River': 0.745267, 'Ottawa River': 0.396294, 'St. Lawrence River': 0.629777}。

#### Stakeholder factors

- shoreline flood risk when levels exceed the monthly high operating band
- navigation draft risk when levels fall below the monthly low operating band
- hydropower and downstream flow constraints at Moses-Saunders
- ecosystem and wetland exposure to prolonged high or low deviations
- Ottawa River inflow contribution to downstream Montreal/St. Lawrence flooding context

#### 最高成本月份

| date | level_m | target_m | deviation_m | cost_total |
|---|---|---|---|---|
| 2019-06-01 | 75.91 | 75.13 | 0.78 | 2.79 |
| 2019-07-01 | 75.8 | 75.09 | 0.71 | 2.63 |
| 2017-05-01 | 75.8 | 75.1 | 0.7 | 2.425 |
| 2017-06-01 | 75.81 | 75.13 | 0.68 | 2.39 |
| 2017-07-01 | 75.69 | 75.09 | 0.6 | 2.19 |
| 2019-08-01 | 75.53 | 74.95 | 0.58 | 2.05 |
| 2019-05-01 | 75.7 | 75.1 | 0.6 | 2.025 |
| 2019-11-01 | 75.04 | 74.51 | 0.53 | 1.82 |

### IJC 备忘录
IJC should select a transparent monthly target-band controller: it uses official historical lake levels to define stakeholder operating bands, then adjusts the two controllable outflows toward those bands while clipping releases to historical monthly 10th-90th percentile flow ranges. The model is auditable, shows where 2017 levels were costly, and highlights Lake Ontario months where Moses-Saunders decisions should balance shoreline flooding, navigation drafts, hydropower, wetlands, and downstream Ottawa/St. Lawrence flood context.

## 模型限制
- 这是可复现的官方数据基线实验，适合做论文骨架和结果表，不应把随机森林相关性解释为严格因果。
- 对异常国家/代表队名称、教练履历、项目规则变化等，需要在竞赛论文中追加人工核验和敏感性分析。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2024/D/q06/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2024/D/q06/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2024/D/q06/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2024/D/q06`
