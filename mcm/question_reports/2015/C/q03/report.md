# 2015-C q03：未来两年招聘与培训预算

## 题目原问
Use your model to analyze the organization's budget needs for talent management in sigma for the next two years of hiring and training.

## 适合模型
按官方每层招聘时间、招聘成本、人数、工资和年度培训成本，计算两年内替换预计离职人员并恢复 15% 空缺所需的招聘 sigma、培训 sigma 和总 sigma。对应模型：预算预测、招聘容量模型、培训成本模型。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2015/Managing Human Capital in Organizations.pdf`。
- 行数/记录数：{'official_parameters': 11}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### ICM 人力资本网络
- 组织单元：46 个 7 人部门 + 12 个 4 人办公室。
- 岗位核对：370 个岗位。
- 当前填补岗位：314.5；空缺：55.5。

#### Level risk table

| level | positions | filled_positions | baseline_attrition_rate | knowledge_risk_score |
|---|---|---|---|---|
| senior_manager_executive | 10 | 8.5 | 0.12 | 0.96 |
| junior_manager_administrator | 20 | 17.0 | 0.3 | 1.056 |
| experienced_supervisor_branch | 25 | 21.25 | 0.3 | 0.492 |
| inexperienced_supervisor_division | 25 | 21.25 | 0.28 | 0.3024 |
| experienced_staff | 110 | 93.5 | 0.16 | 0.0768 |
| inexperienced_staff | 150 | 127.5 | 0.18 | 0.0567 |
| administrative_clerk | 30 | 25.5 | 0.15 | 0.0338 |

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

## 模型限制
- 这是可复现的官方题面参数人力资本网络实验；COMAP 没有提供员工级 CSV/XLSX 附件，因此只使用 PDF 中 370 个岗位、85% 填补率、18% 年流失率、8%-10% 主动招聘范围和岗位层级表。
- 流失影响权重、招聘吞吐折减和内部晋升池比例是显式确定性假设，不是员工观测数据；正式论文应补充员工级组织图、绩效评价、离职历史、招聘流水和匿名关系网络校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2015/C/q03/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2015/C/q03/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2015/C/q03/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2015/C/q03`
