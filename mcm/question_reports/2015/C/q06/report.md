# 2015-C q06：团队科学与多层组织网络扩展

## 题目原问
Summarize the potential use of team science and multilayer networks to realize the HR manager's vision of connecting the human capital network to information flow, trust, influence, and friendship layers.

## 适合模型
把人力资本网络扩展为信息流、信任、影响力、友谊和培训依赖的 multiplex 网络，用跨层中心性识别关键员工和关键岗位。对应模型：团队科学、多层网络、multiplex centrality、组织网络分析。

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

### 团队科学与多层网络扩展
- Represent each work unit as a team layer with formal reporting edges and informal collaboration edges.
- Track trust, information flow, influence, and friendship as separate layers sharing the same employee nodes.
- Use multiplex centrality to find employees whose departure would damage several layers at once.
- 推荐网络层：information_flow, trust, influence, friendship, training_dependency。
- 典型模型：multilayer network, Markov workforce transition, queue/capacity model for recruiting, multi-criteria HR health index。

## 模型限制
- 这是可复现的官方题面参数人力资本网络实验；COMAP 没有提供员工级 CSV/XLSX 附件，因此只使用 PDF 中 370 个岗位、85% 填补率、18% 年流失率、8%-10% 主动招聘范围和岗位层级表。
- 流失影响权重、招聘吞吐折减和内部晋升池比例是显式确定性假设，不是员工观测数据；正式论文应补充员工级组织图、绩效评价、离职历史、招聘流水和匿名关系网络校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2015/C/q06/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2015/C/q06/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2015/C/q06/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2015/C/q06`
