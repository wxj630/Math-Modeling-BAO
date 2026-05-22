# 2024-D q03：2017 年控制效果与两坝出流敏感性

## 题目原问
Understand sensitivity of the control algorithms for the outflow of the two control dams. Given 2017 data, would the controls improve recorded water levels?

## 适合模型
用官方月度流量和下一月水位变化做经验响应拟合，并对 2017 年实际水位 stakeholder cost 与建议控制幅度进行评估。

## 数据与真实性
- 数据类型：official_comap_xlsx。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2024/Data- Great Lakes Water Problem/2024_Problem_D_Great_Lakes.xlsx`。
- 行数/记录数：{'records': 2548, 'level_records': 1380, 'flow_records': 1168}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 2017 年评价
- 实际 stakeholder cost：51.325。
- 平均建议控制幅度：295.631961 cms。
- 解释：The policy is evaluated as an advisory release rule, not a full hydraulic simulator; it flags months where controlled outflow should move toward historical operating bands.

#### 2017 最高成本月份

| lake | date | level_m | target_m | deviation_m | cost_total |
|---|---|---|---|---|---|
| Lake Ontario | 2017-05-01 | 75.8 | 75.1 | 0.7 | 2.425 |
| Lake Ontario | 2017-06-01 | 75.81 | 75.13 | 0.68 | 2.39 |
| Lake Ontario | 2017-07-01 | 75.69 | 75.09 | 0.6 | 2.19 |
| Lake Ontario | 2017-08-01 | 75.43 | 74.95 | 0.48 | 1.65 |
| Lake Michigan and Lake Huron | 2017-11-01 | 176.85 | 176.07 | 0.78 | 1.62 |
| Lake Michigan and Lake Huron | 2017-12-01 | 176.79 | 176.05 | 0.74 | 1.49 |
| Lake St. Clair | 2017-11-01 | 175.44 | 174.85 | 0.59 | 1.415 |
| Lake Michigan and Lake Huron | 2017-10-01 | 176.87 | 176.14 | 0.73 | 1.405 |
| Lake Michigan and Lake Huron | 2017-08-01 | 177.0 | 176.32 | 0.68 | 1.265 |
| Lake Michigan and Lake Huron | 2017-09-01 | 176.93 | 176.24 | 0.69 | 1.245 |

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
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2024/D/q03/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2024/D/q03/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2024/D/q03/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2024/D/q03`
