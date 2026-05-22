# 2024-F q05：需要哪些额外权力和资源

## 题目原问
What additional powers and resources will your client need to carry out the project?

## 适合模型
把每项干预拆成启动成本、年成本、5 年成本和所需权限，形成资源与权力清单。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted`。
- 行数/记录数：{'official_parameters': 5}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

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

## 模型限制
- 这是可复现的官方题面参数非法野生动物贸易项目设计实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中 26.5B USD/year、第四大非法贸易和 5 年项目要求。
- 客户评分、干预减幅、预算和达标概率是显式确定性项目情景，不是执法数据库观测；正式论文应补充 seizure records、CITES/UNODC 路线资料、平台下架数据和地方伙伴调研校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2024/F/q05/solution.py`

## 输出
- `mcm/question_results/2024/F/q05/result.json`
- `mcm/question_reports/2024/F/q05/report.md`
- `mcm/question_artifacts/2024/F/q05`
