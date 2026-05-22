# 2023-D q01：17 个 SDG 的关系网络

## 题目原问
Create a network of the relationships between the 17 SDGs.

## 适合模型
官方 PDF 给出的 17 个 SDG 节点 + 透明确定性有向加权边，构造 SDG 影响网络；对应教程模型：复杂网络与图论模型。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025`。
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

## 模型限制
- 这是可复现的官方题面参数 SDG 网络实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中 17 个 SDGs、网络关系、10 年优先级、达成一个目标后的网络、危机冲击和组织迁移等题面约束。
- 边权、直接需求指数、危机乘数和新增目标情景是显式确定性建模假设，不是 UN 指标数据库观测；正式论文应补充 UN SDG indicator panel、国家分组、资金约束和专家打分校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2023/D/q01/solution.py`

## 输出
- `mcm/question_results/2023/D/q01/result.json`
- `mcm/question_reports/2023/D/q01/report.md`
- `mcm/question_artifacts/2023/D/q01`
