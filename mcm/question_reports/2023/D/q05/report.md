# 2023-D q05：网络方法迁移到其他公司和组织

## 题目原问
Discuss how your network approach may help other companies and organizations set priorities of their goals.

## 适合模型
把 SDG 网络方法抽象成目标节点、依赖边、中心性、直接需求、风险覆盖和达成后重算，用于 ESG、公共卫生、高校和 NGO 目标组合决策。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025`。
- 行数/记录数：{'official_parameters': 5}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### UN 优先级与 10 年计划
- 方法：priority = 55% network leverage + 45% direct human/environment need。
- 10 年 first-wave priorities：[1, 17, 10, 15, 13]。
- 预期网络进展增益：0.2285。
- 评价指标：weighted reachable influence from funded priority goals, discounted by governance feasibility。

#### 优先级排序

| sdg | name | category | pagerank | betweenness | out_strength | priority_score |
|---|---|---|---|---|---|---|
| 1 | No Poverty | social | 0.03465 | 0.15417 | 3.35 | 0.5962 |
| 17 | Partnerships to achieve the Goal | governance | 0.06004 | 0.19167 | 1.48 | 0.5429 |
| 10 | Reduced Inequality | social | 0.06337 | 0.10417 | 1.02 | 0.5346 |
| 15 | Life on Land | environment | 0.17171 | 0.0 | 0.0 | 0.525 |
| 13 | Climate Action | environment | 0.10951 | 0.01667 | 1.3 | 0.5219 |
| 4 | Quality Education | social | 0.02953 | 0.06667 | 2.22 | 0.4956 |
| 3 | Good Health and Well-being | social | 0.02932 | 0.0625 | 2.11 | 0.4927 |
| 16 | Peace and Justice Strong Institutions | governance | 0.05015 | 0.16667 | 0.76 | 0.4892 |
| 12 | Responsible Consumption and Production | environment | 0.04811 | 0.06667 | 1.79 | 0.4815 |
| 8 | Decent Work and Economic Growth | economic | 0.04506 | 0.1 | 1.32 | 0.4753 |
| 11 | Sustainable Cities and Communities | infrastructure | 0.09241 | 0.0375 | 0.97 | 0.4544 |
| 6 | Clean Water and Sanitation | environment | 0.04525 | 0.04167 | 1.53 | 0.451 |
| 2 | Zero Hunger | social | 0.02374 | 0.00417 | 2.28 | 0.428 |
| 14 | Life Below Water | environment | 0.09047 | 0.0 | 0.37 | 0.426 |
| 5 | Gender Equality | social | 0.03088 | 0.01667 | 1.18 | 0.4156 |
| 9 | Industry, Innovation and Infrastructure | infrastructure | 0.05839 | 0.0125 | 0.96 | 0.3863 |
| 7 | Affordable and Clean Energy | infrastructure | 0.01741 | 0.0 | 2.47 | 0.3413 |

### 危机冲击矩阵
- 方法：overlay official crisis categories onto priority-weighted SDG network exposure。
- 网络视角：Crises matter most when they hit bridge goals such as health, education, institutions, partnerships, climate, and inequality at the same time.。

| crisis | affected_sdgs | effect_direction | network_severity_index | priority_response_sdgs | risk |
|---|---|---|---|---|---|
| climate change | 2,6,11,13,14,15 | negative | 0.1123 | 15,13,11 | ecosystem and water stress cascades |
| regional wars | 1,2,3,8,16,17 | negative | 0.1109 | 1,17,3 | institutions and partnerships are strained |
| global pandemic | 1,2,3,4,8,10 | negative | 0.1007 | 1,10,4 | health shock disrupts education and work |
| technological advances | 4,7,8,9,17 | positive | 0.0717 | 17,4,8 | digital divide can widen inequality |
| refugee movements | 1,3,4,10,11,16 | negative | 0.0715 | 1,10,4 | service demand rises in destination communities |

### 迁移到公司和组织目标管理
- 模型：goal-network portfolio prioritization。

#### 迁移步骤

- list organizational goals as nodes and define positive or negative dependencies as weighted edges
- score each goal using centrality, direct mission need, feasibility, and risk exposure
- fund a small first-wave portfolio of bridge goals instead of isolated high-visibility goals
- rerun the network after a goal is achieved or after a crisis changes edge weights
- publish tradeoff edges so stakeholders can see where progress on one objective may slow another

#### 使用场景

- corporate ESG portfolio
- public health agency strategy
- university sustainability plan
- NGO grant allocation

## 模型限制
- 这是可复现的官方题面参数 SDG 网络实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中 17 个 SDGs、网络关系、10 年优先级、达成一个目标后的网络、危机冲击和组织迁移等题面约束。
- 边权、直接需求指数、危机乘数和新增目标情景是显式确定性建模假设，不是 UN 指标数据库观测；正式论文应补充 UN SDG indicator panel、国家分组、资金约束和专家打分校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2023/D/q05/solution.py`

## 输出
- `mcm/question_results/2023/D/q05/result.json`
- `mcm/question_reports/2023/D/q05/report.md`
- `mcm/question_artifacts/2023/D/q05`
