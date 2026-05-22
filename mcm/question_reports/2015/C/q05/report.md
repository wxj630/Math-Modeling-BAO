# 2015-C q05：中层 30% 流失、无外部招聘与内部晋升情景

## 题目原问
Simulate the effect of 30% of both junior managers and experienced supervisors leaving, with no external recruiting and with only qualified employees promoted over the next two years. Explain the effect on organizational HR health.

## 适合模型
对 junior managers 和 experienced supervisors 施加官方要求的 30% 流失冲击，比较无外部招聘与资深主管/初级主管/资深员工内部晋升链；晋升池比例为显式假设。对应模型：晋升链仿真、岗位替补模型、瓶颈分析。

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

## 模型限制
- 这是可复现的官方题面参数人力资本网络实验；COMAP 没有提供员工级 CSV/XLSX 附件，因此只使用 PDF 中 370 个岗位、85% 填补率、18% 年流失率、8%-10% 主动招聘范围和岗位层级表。
- 流失影响权重、招聘吞吐折减和内部晋升池比例是显式确定性假设，不是员工观测数据；正式论文应补充员工级组织图、绩效评价、离职历史、招聘流水和匿名关系网络校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2015/C/q05/solution.py`

## 输出
- `mcm/question_results/2015/C/q05/result.json`
- `mcm/question_reports/2015/C/q05/report.md`
- `mcm/question_artifacts/2015/C/q05`
