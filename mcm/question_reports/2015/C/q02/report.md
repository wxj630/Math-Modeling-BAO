# 2015-C q02：组织流失动态过程与生产率影响

## 题目原问
Use your model to identify dynamic processes within the human capital network. Describe and incorporate dynamic processes involved in organizational churn and the effect of churn on organizational productivity.

## 适合模型
把官方 18% 年流失率和中层高流失描述转化为确定性层级流失风险，叠加网络影响、职业阻塞和 salary-sigma 加权生产率损失；所有非题面系数写入 assumption_audit。对应模型：Markov 人员流动、网络影响扩散、生产率损失函数。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted/2015/Managing Human Capital in Organizations.pdf`。
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

### 流失动态与生产率影响
- influence contagion: departures connected to a level raise dissatisfaction pressure in adjacent levels
- middle-layer career blockage: junior managers and supervisors receive an extra dissatisfaction component
- productivity loss: leavers remove salary-weighted knowledge and coordination capacity before replacements mature

#### Dynamic risk rows

| level | baseline_attrition_rate | dynamic_attrition_risk | expected_annual_leavers | productivity_loss_sigma |
|---|---|---|---|---|
| senior_manager_executive | 0.12 | 0.148 | 1.26 | 10.064 |
| junior_manager_administrator | 0.3 | 0.3516 | 5.98 | 21.042 |
| experienced_supervisor_branch | 0.3 | 0.35 | 7.44 | 12.196 |
| inexperienced_supervisor_division | 0.28 | 0.3272 | 6.95 | 7.508 |
| experienced_staff | 0.16 | 0.1734 | 16.22 | 7.784 |
| inexperienced_staff | 0.18 | 0.1898 | 24.2 | 7.623 |
| administrative_clerk | 0.15 | 0.157 | 4.0 | 0.901 |

## 模型限制
- 这是可复现的官方题面参数人力资本网络实验；COMAP 没有提供员工级 CSV/XLSX 附件，因此只使用 PDF 中 370 个岗位、85% 填补率、18% 年流失率、8%-10% 主动招聘范围和岗位层级表。
- 流失影响权重、招聘吞吐折减和内部晋升池比例是显式确定性假设，不是员工观测数据；正式论文应补充员工级组织图、绩效评价、离职历史、招聘流水和匿名关系网络校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2015/C/q02/solution.py`

## 输出
- `mcm/question_results/2015/C/q02/result.json`
- `mcm/question_reports/2015/C/q02/report.md`
- `mcm/question_artifacts/2015/C/q02`
