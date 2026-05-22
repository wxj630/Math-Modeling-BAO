# 2023-D q02：网络结构驱动的 UN 优先级和 10 年计划

## 题目原问
Use the individual SDGs, as well as the structure of your network, to set priorities that can most efficiently move the work of the UN forward. How did you evaluate the effectiveness of each priority? What could be reasonable to achieve in the next 10 years if your priorities are initiated?

## 适合模型
PageRank、介数中心性、出边强度、入边支持和直接需求指数综合评价，生成 17 个目标排序和 10 年 first-wave priority portfolio。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025`。
- 行数/记录数：{'official_parameters': 5}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### SDG 关系网络
- 模型：directed weighted SDG influence network based on official 17-goal list and transparent scenario edges。
- 节点数：17。
- 边数：45。
- 负向权衡边数：1。

#### 节点

| sdg | name | category |
|---|---|---|
| 1 | No Poverty | social |
| 2 | Zero Hunger | social |
| 3 | Good Health and Well-being | social |
| 4 | Quality Education | social |
| 5 | Gender Equality | social |
| 6 | Clean Water and Sanitation | environment |
| 7 | Affordable and Clean Energy | infrastructure |
| 8 | Decent Work and Economic Growth | economic |
| 9 | Industry, Innovation and Infrastructure | infrastructure |
| 10 | Reduced Inequality | social |
| 11 | Sustainable Cities and Communities | infrastructure |
| 12 | Responsible Consumption and Production | environment |
| 13 | Climate Action | environment |
| 14 | Life Below Water | environment |
| 15 | Life on Land | environment |
| 16 | Peace and Justice Strong Institutions | governance |
| 17 | Partnerships to achieve the Goal | governance |

#### 关系边样本

| source_sdg | target_sdg | weight | sign | relationship |
|---|---|---|---|---|
| 1 | 2 | 0.72 | positive | poverty reduction improves food security |
| 1 | 3 | 0.66 | positive | income access improves health |
| 1 | 4 | 0.6 | positive | poverty reduction keeps children in school |
| 1 | 8 | 0.63 | positive | poverty and decent work reinforce each other |
| 1 | 10 | 0.74 | positive | poverty reduction reduces inequality |
| 2 | 3 | 0.69 | positive | nutrition improves health |
| 2 | 6 | 0.54 | positive | water quality supports food systems |
| 2 | 12 | 0.5 | positive | sustainable consumption affects food systems |
| 2 | 15 | 0.55 | positive | land ecosystems support agriculture |
| 3 | 4 | 0.58 | positive | health improves learning |
| 3 | 5 | 0.47 | positive | health access affects gender outcomes |
| 3 | 6 | 0.61 | positive | clean water reduces disease |
| 3 | 11 | 0.45 | positive | urban design affects health |
| 4 | 5 | 0.7 | positive | education promotes gender equality |

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

## 模型限制
- 这是可复现的官方题面参数 SDG 网络实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中 17 个 SDGs、网络关系、10 年优先级、达成一个目标后的网络、危机冲击和组织迁移等题面约束。
- 边权、直接需求指数、危机乘数和新增目标情景是显式确定性建模假设，不是 UN 指标数据库观测；正式论文应补充 UN SDG indicator panel、国家分组、资金约束和专家打分校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2023/D/q02/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2023/D/q02/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2023/D/q02/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2023/D/q02`
