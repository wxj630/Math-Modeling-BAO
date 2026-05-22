# 2024-F q04：用数据驱动分析说服客户

## 题目原问
Using a data-driven analysis, how will you convince your client that this is a project they should undertake?

## 适合模型
比较无项目贸易额增长路径与 5 年项目干预路径，输出第 5 年降低比例和年度影响表。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted`。
- 行数/记录数：{'official_parameters': 5}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 客户选择
- 选择客户：World Customs Organization coordinated customs task force。
- 选择理由：highest fit because customs coordination has authority over border chokepoints and access to shipment-risk metadata。
- 模型：multi-criteria client fit score over mandate, cross-border power, data access, implementation capacity, mission alignment, and political feasibility。

#### 候选客户评分

| client | mandate_fit | cross_border_power | data_access | implementation_capacity | client_fit_score |
|---|---|---|---|---|---|
| World Customs Organization coordinated customs task force | 0.94 | 0.92 | 0.86 | 0.82 | 0.8768 |
| Global e-commerce marketplace trust-and-safety coalition | 0.76 | 0.54 | 0.92 | 0.8 | 0.7458 |
| Regional wildlife conservation NGO consortium | 0.82 | 0.45 | 0.61 | 0.64 | 0.7 |
| National park agency in a source country | 0.88 | 0.36 | 0.52 | 0.58 | 0.6488 |

### 五年项目设计
- 项目名：Targeted Corridor Disruption and Demand-Platform Friction Program。
- 项目周期：5 年。
- 适配性：The selected client can coordinate customs risk scoring, data-sharing rules, and enforcement operations while partnering with platforms, FIUs, and community groups.。

#### 干预组合

| intervention | annual_cost_musd | year1_reduction_pct | maturity_gain_pct_per_year |
|---|---|---|---|
| risk-scored customs inspections on high-probability routes | 8.5 | 0.035 | 0.01 |
| shared wildlife-trafficking intelligence graph | 6.2 | 0.026 | 0.014 |
| online listing takedown and seller re-entry friction | 3.8 | 0.018 | 0.009 |
| community informant rewards and alternative-livelihood microgrants | 5.5 | 0.022 | 0.011 |
| financial-flow screening for wildlife-product typologies | 4.9 | 0.02 | 0.012 |

### 五年影响预测
- 方法：compound no-project growth path compared with deterministic yearly intervention reductions under implementation maturity。
- 第 5 年无项目贸易额：31.4737 billion USD。
- 第 5 年项目贸易额：20.8262 billion USD。
- 第 5 年累计降低：33.83%。

| year | baseline_illegal_trade_value_billion_usd | projected_illegal_trade_value_billion_usd | cumulative_trade_reduction_pct |
|---|---|---|---|
| 1 | 27.4275 | 26.6609 | 2.795 |
| 2 | 28.3875 | 26.1991 | 7.709 |
| 3 | 29.381 | 25.0463 | 14.754 |
| 4 | 30.4094 | 23.2169 | 23.652 |
| 5 | 31.4737 | 20.8262 | 33.83 |

## 模型限制
- 这是可复现的官方题面参数非法野生动物贸易项目设计实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中 26.5B USD/year、第四大非法贸易和 5 年项目要求。
- 客户评分、干预减幅、预算和达标概率是显式确定性项目情景，不是执法数据库观测；正式论文应补充 seizure records、CITES/UNODC 路线资料、平台下架数据和地方伙伴调研校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2024/F/q04/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2024/F/q04/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2024/F/q04/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2024/F/q04`
