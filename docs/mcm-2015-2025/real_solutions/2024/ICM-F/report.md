# 2024 ICM-F Reducing Illegal Wildlife Trade

## 数据真实性
- 官方来源：`docs/mcm-2015-2025/official_assets_extracted/2024/Reducing Illegal Wildlife Trade.pdf`。
- 本题无 COMAP 数值附件；脚本只使用官方 PDF 中的 26.5B USD/year、第四大非法贸易和 5 年项目要求。
- 客户评分、干预效果、成本和敏感性是显式确定性项目情景，不是声称拥有真实执法数据库。

## 官方题面参数
- 非法野生动物贸易最高估计：26.5 billion USD/year。
- 项目周期：5 年。
- 第四大全球非法贸易：True。

## 每问结果
### Q1-Q2 客户与现实行动能力
- 选择客户：World Customs Organization coordinated customs task force。
- 理由：highest fit because customs coordination has authority over border chokepoints and access to shipment-risk metadata。

### Q3-Q4 项目适配和数据驱动说服
- 项目名：Targeted Corridor Disruption and Demand-Platform Friction Program。
- 5 年末相对无项目路径降低：33.83%。
- 无项目第 5 年贸易额：31.4737 billion USD。
- 项目第 5 年贸易额：20.8262 billion USD。

### Q5 额外资源和权力
- 5 年新增预算：160.395 million USD。
- customs data-sharing memorandum across high-risk ports
- legal authority for risk-scored inspections and controlled deliveries
- platform takedown escalation channel
- financial intelligence liaison for wildlife-product typologies
- audited community reward and microgrant mechanism

### Q6-Q8 项目后果、可测量影响和分析方法
- 方法：compound no-project growth path compared with deterministic yearly intervention reductions under implementation maturity。
- 年度影响：
- Year 1：project=26.6609B，reduction=2.795%。
- Year 2：project=26.1991B，reduction=7.709%。
- Year 3：project=25.0463B，reduction=14.754%。
- Year 4：project=23.2169B，reduction=23.652%。
- Year 5：project=20.8262B，reduction=33.83%。

### Q9-Q10 达成目标概率与敏感性
- 目标：at least 20% cumulative reduction from the no-project five-year trajectory。
- 达标概率：0.69。
- 有利条件：
- high customs data-sharing compliance：0.77。
- platform API cooperation and rapid takedown：0.74。
- stable source-country community partners：0.72。
- 不利条件：
- trafficker route displacement to unobserved corridors：0.5。
- corruption or leak of targeting rules：0.52。
- economic shock increasing poaching recruitment：0.55。

## 给客户一页备忘录核心
Memo to the World Customs Organization coordinated customs task force: adopt this 5-year corridor disruption project because illegal wildlife trade is valued up to 26.5 billion USD per year and is the fourth largest illegal trade. The program uses customs risk scoring, shared intelligence, platform takedowns, financial-flow screening, and community incentives to produce a measurable 33.83% reduction versus the no-project trajectory by year 5.

## 输出产物
- `client_project_scores.csv`：客户选择多指标评分。
- `resource_plan.csv`：项目资源和额外权力需求。
- `intervention_impact_projection.csv`：5 年影响预测。
- `sensitivity_analysis.csv`：情景敏感性。
- `complex_system_edges.csv`：复杂系统影响网络。
- `wildlife_trade_project_frontier.png`：客户选择和项目影响图。
