# 2024 ICM-D Great Lakes Water Problem 真实数据解法

## 数据来源
- 使用 COMAP 官方 `2024_Problem_D_Great_Lakes.xlsx` 的 11 个工作表。
- 将湖泊水位和连接河流流量整理为月度长表；未生成随机水位或流量。

## 数据规模
- 总有效月度记录：2548。
- 湖泊水位记录：1380；河流流量记录：1168。

## Q1 最优水位
- 以 2000-2023 历史月度中位数作为分月目标水位，以 25%-75% 分位数作为运行带。

| lake | target mean | band width | seasonal min | seasonal max |
|---|---:|---:|---:|---:|
| Lake Erie | 174.203333 | 0.424583 | 174.02 | 174.36 |
| Lake Michigan and Lake Huron | 176.1375 | 0.669167 | 175.96 | 176.33 |
| Lake Ontario | 74.818333 | 0.2325 | 74.51 | 75.13 |
| Lake St. Clair | 174.986667 | 0.494167 | 174.85 | 175.15 |
| Lake Superior | 183.293333 | 0.381667 | 183.11 | 183.44 |

## Q2 控制算法
- 规则：monthly median flow plus 900 cms per meter above target, clipped to historical 10th-90th percentile by month

| lake | control flow | mean abs level deviation | mean abs flow adjustment | max adjustment |
|---|---|---:|---:|---:|
| Lake Ontario | St. Lawrence River | 0.152681 | 136.499176 | 702.0 |
| Lake Superior | St. Mary's River | 0.186775 | 159.972069 | 449.218411 |

## Q3 2017 年控制评价和坝出流敏感性
- 2017 实际 stakeholder cost：51.325。
- 2017 平均建议控制幅度：295.631961 cms。

| lake | flow | rows | rmse | standardized sensitivity | interpretation |
|---|---|---:|---:|---:|---|
| Lake Superior | St. Mary's River | 168 | 0.066173 | -0.005175 | negative means larger outflow tends to lower next-month lake level |
| Lake Ontario | St. Lawrence River | 109 | 0.136944 | -0.122293 | negative means larger outflow tends to lower next-month lake level |

## Q4 环境条件敏感性
| lake | mean cost | high months | low months | max abs deviation |
|---|---:|---:|---:|---:|
| Lake Michigan and Lake Huron | 0.624493 | 70 | 70 | 1.28 |
| Lake St. Clair | 0.522971 | 71 | 67 | 0.94 |
| Lake Erie | 0.453043 | 72 | 68 | 0.83 |
| Lake Ontario | 0.321993 | 71 | 71 | 0.78 |
| Lake Superior | 0.308841 | 71 | 71 | 0.53 |

## Q5 Lake Ontario 专项
- 高水位月份：71；低水位月份：71。
- 平均绝对偏离：0.152681 m。
- 与 Niagara/Ottawa/St. Lawrence 流量相关：{'Niagara River': 0.745267, 'Ottawa River': 0.396294, 'St. Lawrence River': 0.629777}。

### Stakeholder factors
- shoreline flood risk when levels exceed the monthly high operating band
- navigation draft risk when levels fall below the monthly low operating band
- hydropower and downstream flow constraints at Moses-Saunders
- ecosystem and wetland exposure to prolonged high or low deviations
- Ottawa River inflow contribution to downstream Montreal/St. Lawrence flooding context

## IJC 一页备忘录摘要
IJC should select a transparent monthly target-band controller: it uses official historical lake levels to define stakeholder operating bands, then adjusts the two controllable outflows toward those bands while clipping releases to historical monthly 10th-90th percentile flow ranges. The model is auditable, shows where 2017 levels were costly, and highlights Lake Ontario months where Moses-Saunders decisions should balance shoreline flooding, navigation drafts, hydropower, wetlands, and downstream Ottawa/St. Lawrence flood context.

## 输出文件
- `artifacts/great_lakes_long_data.csv`：官方数据长表。
- `artifacts/monthly_level_targets.csv`：分月目标水位带。
- `artifacts/control_policy_releases.csv`：控制坝建议出流。
- `artifacts/dam_outflow_sensitivity.csv`：坝出流敏感性。
- `artifacts/lake_ontario_target_band.png`：Lake Ontario 水位与目标带。
