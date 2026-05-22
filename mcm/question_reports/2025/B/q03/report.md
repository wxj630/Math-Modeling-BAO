# 2025-B q03：给朱诺旅游委员会的一页备忘录

## 题目原问
Write a one-page memo to the tourist council of Juneau outlining predictions, effects of measures, and advice on how to optimize outcomes.

## 适合模型
将最优政策、敏感性排序、收入支出反馈和迁移建议压缩为 Juneau Tourism Board 可执行备忘录。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2025`。
- 行数/记录数：{'official_parameters': 8}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 情境化敏感性分析
- 方法：correlation and 10th-to-90th percentile score shift over deterministic policy grid。

#### 有利条件

无可展示记录。

#### 不利条件

无可展示记录。

### 朱诺可持续旅游模型
- 目标：maximize weighted sustainability score subject to minimum revenue, resident acceptance, attraction health, and feasible visitor volume。

#### 基线

| annual_visitors | visitors_per_resident | total_revenue_usd | hidden_cost_usd | sustainability_score |
|---|---|---|---|---|
| 1600000 | 53.333 | 375000000.0 | 154163000.0 | 0.6738 |

#### 推荐政策

| daily_cap | visitor_fee_usd | conservation_share | annual_visitors | total_revenue_usd | resident_acceptance_index | environment_index | sustainability_score |
|---|---|---|---|---|---|---|---|
| 10000 | 50.0 | 0.35 | 1408000 | 400400000.0 | 0.78 | 0.80235 | 0.908447 |

#### 收入支出反馈

- conservation：fund glacier trail protection, visitor dispersal to whale watching/rain forest sites, and ecological monitoring
- infrastructure：water, waste, dock scheduling, shuttle electrification, and queue management
- community：resident dividend/community grants, seasonal worker housing mitigation, and visitor behavior enforcement

### 敏感性分析
- 方法：correlation and 10th-to-90th percentile score shift over deterministic policy grid。

| factor | correlation_with_score | score_change_from_p10_to_p90 | interpretation |
|---|---|---|---|
| fee_revenue_usd | 0.919311 | 0.112079 | funds available for mitigation raises the score in this grid. |
| visitor_fee_usd | 0.909965 | 0.142135 | added revenue and price response raises the score in this grid. |
| annual_visitors | -0.868509 | -0.112079 | volume after cap and fee response reduces the score in this grid. |
| hidden_cost_usd | -0.743621 | -0.20902 | infrastructure, crowding, and carbon burden reduces the score in this grid. |
| conservation_share | 0.227667 | 0.0 | fee allocation toward attraction health raises the score in this grid. |
| daily_cap | -0.117707 | -0.0235 | daily crowding pressure and maximum seasonal volume reduces the score in this grid. |

### Juneau Tourism Board 备忘录
To the Juneau Tourism Board:

Using the official problem-statement values for Juneau, the baseline is 1.6 million annual cruise passengers, about 53 visitors per resident, and busiest days near 20,000 visitors. The model recommends keeping tourism economically viable while lowering peak pressure: daily cap 10000, visitor fee $50.0, and conservation share 0.35. This policy produces about 1,408,000 annual visitors, total revenue $400,400,000, and a sustainability score of 0.908447, compared with the baseline score 0.6738. The most influential factor in the grid is fee_revenue_usd, so enforcement of caps and fee-funded mitigation should receive the most attention.

Spend new fee revenue on glacier and trail conservation, water/waste/dock infrastructure, electric shuttles, and community programs. The same framework can be transferred to other overtourism locations such as Barcelona by replacing glacier health with cultural-site crowding and using timed-entry plus visitor dispersal.

Recommendation: adopt a moderate cap-fee package, publish transparent annual indicators, and reserve enough fee revenue for visible resident benefits.

## 模型限制
- 这是可复现的官方题面参数实验，适合处理没有独立 CSV/XLSX 附件的 MCM 题；它不是随机造数，也不是外部数据回归。
- 价格弹性、隐性成本和支出反馈是显式建模假设，正式论文应通过城市公开预算、港口客流和居民调查进一步校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2025/B/q03/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2025/B/q03/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2025/B/q03/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2025/B/q03`
