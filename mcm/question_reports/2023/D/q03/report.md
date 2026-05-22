# 2023-D q03：某一 SDG 达成后的网络结构和新增目标

## 题目原问
If one of the SDGs is achieved (for example, there is no poverty or no hunger), what would be the structure of the resulting network? How would this achievement impact your team's priorities? Are there other goals that should be included or proposed to the UN for inclusion?

## 适合模型
以 SDG 1 达成为情景，衰减其紧急依赖边，重算网络优先级，并提出 Digital Public Trust and Resilience 作为技术/危机治理补充目标。

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

### 达成一个 SDG 后的网络
- 达成目标：SDG 1。
- 情景：SDG 1 No Poverty achieved, so poverty-centered incoming dependencies fall and downstream support becomes maintenance rather than emergency relief.。
- 建议新增目标：SDG 18 Digital Public Trust and Resilience；原因：Technology and crisis governance appear repeatedly in the official prompt but are not represented as a standalone SDG.。

#### 达成后优先级

| sdg | name | post_achievement_pagerank |
|---|---|---|
| 15 | SDG 15: Life on Land | 0.17286 |
| 13 | SDG 13: Climate Action | 0.1132 |
| 14 | SDG 14: Life Below Water | 0.09142 |
| 11 | SDG 11: Sustainable Cities and Communities | 0.09054 |
| 17 | SDG 17: Partnerships to achieve the Goal | 0.06058 |
| 9 | SDG 9: Industry, Innovation and Infrastructure | 0.06037 |
| 10 | SDG 10: Reduced Inequality | 0.05828 |
| 16 | SDG 16: Peace and Justice Strong Institutions | 0.05186 |
| 6 | SDG 6: Clean Water and Sanitation | 0.04759 |
| 12 | SDG 12: Responsible Consumption and Production | 0.04687 |

## 模型限制
- 这是可复现的官方题面参数 SDG 网络实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中 17 个 SDGs、网络关系、10 年优先级、达成一个目标后的网络、危机冲击和组织迁移等题面约束。
- 边权、直接需求指数、危机乘数和新增目标情景是显式确定性建模假设，不是 UN 指标数据库观测；正式论文应补充 UN SDG indicator panel、国家分组、资金约束和专家打分校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2023/D/q03/solution.py`

## 输出
- `mcm/question_results/2023/D/q03/result.json`
- `mcm/question_reports/2023/D/q03/report.md`
- `mcm/question_artifacts/2023/D/q03`
