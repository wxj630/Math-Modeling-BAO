# 2024-F q08：如何确定上述影响

## 题目原问
What analysis did you do to determine this?

## 适合模型
组合多指标客户选择、资源约束项目成本、干预影响投影、复杂系统影响网络和 one-at-a-time 敏感性分析。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted`。
- 行数/记录数：{'official_parameters': 5}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 分析支持与复杂系统框架
- 建模过程：
- multi-criteria client selection
- deterministic intervention-impact projection
- resource-constrained project costing
- contextualized sensitivity analysis
- complex-system influence network

- 使用复杂系统框架：True。
#### 复杂系统边

| source | target | influence_weight | relationship |
|---|---|---|---|
| source-area poaching | transit-route smuggling | 0.85 | supply chain |
| transit-route smuggling | destination market availability | 0.78 | supply chain |
| online demand signals | destination market availability | 0.66 | demand amplification |
| financial-flow screening | transit-route smuggling | -0.42 | deterrence |
| customs targeting | transit-route smuggling | -0.58 | interdiction |
| community rewards | source-area poaching | -0.37 | source reduction |
| platform takedown | online demand signals | -0.45 | demand reduction |
| climate and livelihood stress | source-area poaching | 0.31 | external pressure |

### 额外资源与权力需求
- 5 年新增预算：160.395 million USD。

#### 额外权力
- customs data-sharing memorandum across high-risk ports
- legal authority for risk-scored inspections and controlled deliveries
- platform takedown escalation channel
- financial intelligence liaison for wildlife-product typologies
- audited community reward and microgrant mechanism

#### 资源计划

| intervention | startup_cost_musd | annual_cost_musd | five_year_cost_musd |
|---|---|---|---|
| risk-scored customs inspections on high-probability routes | 4.675 | 8.5 | 47.175 |
| shared wildlife-trafficking intelligence graph | 3.41 | 6.2 | 34.41 |
| online listing takedown and seller re-entry friction | 2.09 | 3.8 | 21.09 |
| community informant rewards and alternative-livelihood microgrants | 3.025 | 5.5 | 30.525 |
| financial-flow screening for wildlife-product typologies | 2.695 | 4.9 | 27.195 |

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
`.venv/bin/python mcm/question_solutions/2024/F/q08/solution.py`

## 输出
- `mcm/question_results/2024/F/q08/result.json`
- `mcm/question_reports/2024/F/q08/report.md`
- `mcm/question_artifacts/2024/F/q08`
