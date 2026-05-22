# 2016-F q05：Canada、China、United States 区域扩展

## 题目原问
Also consider the inclusion of other refugee destinations such as Canada, China, and the United States. Does your model work for these regions as well?

## 适合模型
把题面要求的 Canada、China、United States 纳入 extension feasibility，保留网络流/容量结构，但重新校准距离、法律准入、资源 readiness 和长期融合能力。对应模型：模型迁移、区域适配、多指标可行性评分。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2016`。
- 行数/记录数：{'official_problem_parameters': 7}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 六条路线容量约束流动模型
- 方法：capacity-constrained deterministic route allocation over the six official travel routes, with explicit emergency overflow when stated crisis scale exceeds temporary route capacity
- 总分配人数：715000。
- 临时容量合计：670000。
- 应急溢出安置人数：45000。

| route | entry_point | allocated_refugees | share_of_total | safety_score | accessibility_score | estimated_processing_days | capacity_binding | emergency_overflow_refugees |
|---|---|---|---|---|---|---|---|---|
| West Mediterranean | Spain | 55000 | 0.07692 | 0.58 | 0.5 | 26.19 | True | 0 |
| Central Mediterranean | Italy | 86000 | 0.12028 | 0.28 | 0.48 | 29.66 | True | 0 |
| Eastern Mediterranean | Greece/Turkey | 329000 | 0.46014 | 0.62 | 0.82 | 40.12 | True | 45000 |
| West Balkans | Hungary/Serbia | 162000 | 0.22657 | 0.5 | 0.68 | 35.22 | True | 0 |
| Eastern Borders | Eastern EU border | 48000 | 0.06713 | 0.54 | 0.36 | 35.56 | True | 0 |
| Albania to Greece | Albania/Greece | 35000 | 0.04895 | 0.6 | 0.42 | 30.43 | True | 0 |

### Canada、China、United States 区域扩展
- 模型是否可迁移：True。
- 说明：The network-flow/resource-capacity structure transfers, but distance, legal access, air/sea transport, and long-run integration parameters must be recalibrated.

| destination | distance_penalty | integration_capacity | legal_access | resource_readiness | model_feasibility_score |
|---|---|---|---|---|---|
| United States | 0.5 | 95000 | 0.62 | 0.78 | 0.6128 |
| Canada | 0.42 | 65000 | 0.74 | 0.82 | 0.5624 |
| China | 0.55 | 80000 | 0.42 | 0.7 | 0.4746 |

## 模型限制
- 这是可复现的官方题面参数难民政策实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中 715,000+ 申请、Hungary 1,450/100k、32% 批准率、六条路线、最热门/最危险路线、NGO、外生事件和 10 倍扩展等约束。
- 路线安全、可达性、临时容量、日处理能力、资源包和 NGO 增益是显式规划假设，不是边境观测数据；正式论文应补充 UNHCR/IOM/FRONTEX 路线流量、死亡风险、接收容量、庇护审批、公共卫生和本地融合数据校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2016/F/q05/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2016/F/q05/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2016/F/q05/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2016/F/q05`
