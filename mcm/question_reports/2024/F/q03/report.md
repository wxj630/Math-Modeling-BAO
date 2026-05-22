# 2024-F q03：文献和分析如何支持项目选择

## 题目原问
What research, from published literature and from your own analyses, supports the selection of your proposed project?

## 适合模型
用官方 26.5B USD/year 与第四大非法贸易约束，加上复杂系统网络和干预证据说明 targeted corridor disruption 比泛化宣传更适合客户。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted`。
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

## 模型限制
- 这是可复现的官方题面参数非法野生动物贸易项目设计实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中 26.5B USD/year、第四大非法贸易和 5 年项目要求。
- 客户评分、干预减幅、预算和达标概率是显式确定性项目情景，不是执法数据库观测；正式论文应补充 seizure records、CITES/UNODC 路线资料、平台下架数据和地方伙伴调研校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2024/F/q03/solution.py`

## 输出
- `mcm/question_results/2024/F/q03/result.json`
- `mcm/question_reports/2024/F/q03/report.md`
- `mcm/question_artifacts/2024/F/q03`
