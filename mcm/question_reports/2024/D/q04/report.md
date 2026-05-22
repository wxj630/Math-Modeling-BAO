# 2024-D q04：环境条件变化敏感性

## 题目原问
How sensitive is the algorithm to environmental changes such as precipitation, snowpack, and ice jams?

## 适合模型
用偏离分月目标带的高水位/月低水位月数、平均 stakeholder cost 和最大偏离量作为环境冲击敏感性指标。

## 数据与真实性
- 数据类型：official_comap_xlsx。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2024/Data- Great Lakes Water Problem/2024_Problem_D_Great_Lakes.xlsx`。
- 行数/记录数：{'records': 2548, 'level_records': 1380, 'flow_records': 1168}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 两坝出流敏感性

| lake | control_flow | rows | rmse_m | standardized_outflow_sensitivity | interpretation |
|---|---|---|---|---|---|
| Lake Superior | St. Mary's River | 168 | 0.066173 | -0.005175 | negative means larger outflow tends to lower next-month lake level |
| Lake Ontario | St. Lawrence River | 109 | 0.136944 | -0.122293 | negative means larger outflow tends to lower next-month lake level |

### 环境条件敏感性

| lake | mean_monthly_cost | high_water_months | low_water_months | max_abs_deviation_m |
|---|---|---|---|---|
| Lake Michigan and Lake Huron | 0.624493 | 70 | 70 | 1.28 |
| Lake St. Clair | 0.522971 | 71 | 67 | 0.94 |
| Lake Erie | 0.453043 | 72 | 68 | 0.83 |
| Lake Ontario | 0.321993 | 71 | 71 | 0.78 |
| Lake Superior | 0.308841 | 71 | 71 | 0.53 |

## 模型限制
- 这是可复现的官方数据基线实验，适合做论文骨架和结果表，不应把随机森林相关性解释为严格因果。
- 对异常国家/代表队名称、教练履历、项目规则变化等，需要在竞赛论文中追加人工核验和敏感性分析。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2024/D/q04/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2024/D/q04/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2024/D/q04/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2024/D/q04`
