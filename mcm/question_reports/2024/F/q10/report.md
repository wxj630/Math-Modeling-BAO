# 2024-F q10：情境化敏感性和一页客户备忘录

## 题目原问
Also, based on a contextualized sensitivity analysis, are there conditions or events that may disproportionately aid or harm the project's ability to reach its goal? Submit a 1-page memo with key points for your client.

## 适合模型
列出数据共享、平台合作、社区伙伴、路线转移、腐败泄露和经济冲击等敏感事件，并输出面向客户的一页 memo。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted`。
- 行数/记录数：{'official_parameters': 5}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 达成目标概率
- 目标：at least 20% cumulative reduction from the no-project five-year trajectory。
- 基础概率：0.64。
- 达标概率：0.69。

### 情境化敏感性分析
- 方法：one-at-a-time contextual event adjustments around the base probability of meeting the 20% reduction goal。

#### 有利条件

| condition | effect_on_goal_probability | adjusted_probability |
|---|---|---|
| high customs data-sharing compliance | 0.13 | 0.77 |
| platform API cooperation and rapid takedown | 0.1 | 0.74 |
| stable source-country community partners | 0.08 | 0.72 |

#### 不利条件

| condition | effect_on_goal_probability | adjusted_probability |
|---|---|---|
| trafficker route displacement to unobserved corridors | -0.14 | 0.5 |
| corruption or leak of targeting rules | -0.12 | 0.52 |
| economic shock increasing poaching recruitment | -0.09 | 0.55 |

### 给客户的一页备忘录
Memo to the World Customs Organization coordinated customs task force: adopt this 5-year corridor disruption project because illegal wildlife trade is valued up to 26.5 billion USD per year and is the fourth largest illegal trade. The program uses customs risk scoring, shared intelligence, platform takedowns, financial-flow screening, and community incentives to produce a measurable 33.83% reduction versus the no-project trajectory by year 5.

### 敏感性分析
- 方法：one-at-a-time contextual event adjustments around the base probability of meeting the 20% reduction goal。

无可展示记录。

## 模型限制
- 这是可复现的官方题面参数非法野生动物贸易项目设计实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中 26.5B USD/year、第四大非法贸易和 5 年项目要求。
- 客户评分、干预减幅、预算和达标概率是显式确定性项目情景，不是执法数据库观测；正式论文应补充 seizure records、CITES/UNODC 路线资料、平台下架数据和地方伙伴调研校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2024/F/q10/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2024/F/q10/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2024/F/q10/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2024/F/q10`
