# 2015-C q07：20 页报告与执行摘要

## 题目原问
Write a 20-page report introducing your organizational model, its functions, and the issues the manager asked you to consider. A one-page executive summary does not count toward the page limit.

## 适合模型
把官方题面参数、网络模型、流失动态、两年预算、25%/35% 情景、中层 30% 冲击和团队科学路线图整理为 HR 经理可读报告。对应模型：实验报告、执行摘要、政策备忘录、模型限制说明。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2015/Managing Human Capital in Organizations.pdf`。
- 行数/记录数：{'official_parameters': 11}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 两年招聘与培训预算
- 方法：replace projected attrition and recover the 15% vacancy gap over two years; costs are reported in units of sigma as requested by the statement
- 招聘成本：57.189 sigma。
- 培训成本：43.454 sigma。
- 总预算：100.643 sigma。

| level | two_year_total_hires | two_year_recruiting_sigma | two_year_training_sigma | two_year_budget_sigma |
|---|---|---|---|---|
| senior_manager_executive | 3.54 | 4.248 | 1.77 | 6.018 |
| junior_manager_administrator | 13.2 | 9.24 | 7.92 | 17.16 |
| experienced_supervisor_branch | 16.5 | 9.9 | 3.3 | 13.2 |
| inexperienced_supervisor_division | 15.65 | 9.39 | 4.695 | 14.085 |
| experienced_staff | 46.42 | 13.926 | 4.642 | 18.568 |
| inexperienced_staff | 68.4 | 6.84 | 20.52 | 27.36 |
| administrative_clerk | 12.15 | 3.645 | 0.607 | 4.252 |

### 25%/35% 流失率情景
- 方法：compare annual attrition load with active recruiting throughput adjusted for administrative readiness

| annual_turnover_rate | annual_leavers_at_full_positions | estimated_hiring_capacity_per_year | end_of_year_fill_rate | sustains_80pct_fill |
|---|---|---|---|---|
| 0.18 | 66.6 | 108.37 | 0.9629 | True |
| 0.25 | 92.5 | 108.37 | 0.8929 | True |
| 0.35 | 129.5 | 108.37 | 0.7929 | False |

#### 间接影响

- middle-layer vacancies increase coordination delay between executives and staff
- HR capacity is consumed by replacement hiring instead of quality screening
- training load rises while informal knowledge transfer falls

### 中层 30% 流失与内部晋升
- 情景：30% attrition among junior managers and experienced supervisors, other attrition left at statement 18% baseline for broader planning context
- 无外部招聘中层填补率：0.595。
- 仅内部晋升中层填补率：0.7603。
- 解释：Internal promotion cushions the management gap, but it transfers vacancies to supervisors and experienced staff, so HR health still deteriorates without external recruiting.

| level | baseline_filled | after_30pct_middle_attrition_no_external | after_internal_promotions_only |
|---|---|---|---|
| senior_manager_executive | 8.5 | 8.5 | 8.5 |
| junior_manager_administrator | 17.0 | 11.9 | 17.0 |
| experienced_supervisor_branch | 21.25 | 14.88 | 17.21 |
| inexperienced_supervisor_division | 21.25 | 21.25 | 21.25 |
| experienced_staff | 93.5 | 93.5 | 86.06 |
| inexperienced_staff | 127.5 | 127.5 | 127.5 |
| administrative_clerk | 25.5 | 25.5 | 25.5 |

### Executive summary
To the ICM HR Manager:

The official statement describes 370 positions, 314.5 currently filled positions, and an annual attrition rate of 18%. I modeled ICM as a multilayer human-capital network linking hierarchy, work units, attrition influence, and training/recruiting capacity. The most fragile layers are junior managers and supervisors: they are central enough to transmit knowledge and dissatisfaction, but the statement says middle turnover is unusually high.

For the next two years, the aggregate recruiting-plus-training budget is 100.643 sigma units. Under the explicit throughput assumptions, ICM can sustain 80% fill at 25% annual turnover: True; at 35%: False. The 35% case overloads HR and creates indirect costs through weak screening, manager vacancies, and lost informal knowledge.

If 30% of junior managers and experienced supervisors leave, internal promotions recover part of the gap (0.7603 middle-layer fill), but they drain experienced supervisors and staff. Recommendation: stabilize middle managers first, reserve recruiting capacity for critical roles, and build a multiplex employee network so HR can monitor influence, trust, information flow, and training dependencies before departures cascade.

## 模型限制
- 这是可复现的官方题面参数人力资本网络实验；COMAP 没有提供员工级 CSV/XLSX 附件，因此只使用 PDF 中 370 个岗位、85% 填补率、18% 年流失率、8%-10% 主动招聘范围和岗位层级表。
- 流失影响权重、招聘吞吐折减和内部晋升池比例是显式确定性假设，不是员工观测数据；正式论文应补充员工级组织图、绩效评价、离职历史、招聘流水和匿名关系网络校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2015/C/q07/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2015/C/q07/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2015/C/q07/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2015/C/q07`
