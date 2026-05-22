# 2024-D q05：Lake Ontario 专项利益相关者分析

## 题目原问
Focus extensive analysis only on stakeholders and factors influencing Lake Ontario, where water level management has drawn concern.

## 适合模型
对 Lake Ontario 分析高低水位月份、目标偏离、与 Niagara/Ottawa/St. Lawrence 流量相关性和最高 stakeholder cost 月份。

## 数据与真实性
- 数据类型：official_comap_xlsx。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted/2024/Data- Great Lakes Water Problem/2024_Problem_D_Great_Lakes.xlsx`。
- 行数/记录数：{'records': 2548, 'level_records': 1380, 'flow_records': 1168}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

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

## 模型限制
- 这是可复现的官方数据基线实验，适合做论文骨架和结果表，不应把随机森林相关性解释为严格因果。
- 对异常国家/代表队名称、教练履历、项目规则变化等，需要在竞赛论文中追加人工核验和敏感性分析。

## 运行方式
`.venv/bin/python mcm/question_solutions/2024/D/q05/solution.py`

## 输出
- `mcm/question_results/2024/D/q05/result.json`
- `mcm/question_reports/2024/D/q05/report.md`
- `mcm/question_artifacts/2024/D/q05`
