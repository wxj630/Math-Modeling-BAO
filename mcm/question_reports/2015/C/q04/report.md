# 2015-C q04：25% 与 35% 年流失率下的 80% 填补率可持续性

## 题目原问
Can ICM maintain its 80% filled positions if annual turnover for all positions increases to 25%? What about 35%? What are the costs of these higher turnover rates? What indirect effects might high turnover cause?

## 适合模型
把题面 8%-10% 主动招聘范围转成可审计招聘吞吐量，比较 18%、25%、35% 年流失下的离职负荷、第一年填补率和间接成本。对应模型：稳态容量约束、人员库存模型、敏感性分析。

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

## 模型限制
- 这是可复现的官方题面参数人力资本网络实验；COMAP 没有提供员工级 CSV/XLSX 附件，因此只使用 PDF 中 370 个岗位、85% 填补率、18% 年流失率、8%-10% 主动招聘范围和岗位层级表。
- 流失影响权重、招聘吞吐折减和内部晋升池比例是显式确定性假设，不是员工观测数据；正式论文应补充员工级组织图、绩效评价、离职历史、招聘流水和匿名关系网络校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2015/C/q04/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2015/C/q04/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2015/C/q04/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2015/C/q04`
