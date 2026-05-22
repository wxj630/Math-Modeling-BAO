# 2023-B q03：长期趋势、确定性与迁移到其他保护区

## 题目原问
Given your proposed plan, provide predictions about the long-term trends that will result from your recommendations. Analyze and provide estimates of the certainties and impacts of the possible long-term outcomes. You should also describe how your approach could be applied to other wildlife management areas.

## 适合模型
对最佳 integrated mosaic plan 做 20 年离散动态投影，输出 conflict index、wildlife index、resident acceptance、community benefit，并给出迁移步骤和风险登记。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025`。
- 行数/记录数：{'official_parameters': 5}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 人兽互动长期投影
- 模型：discrete annual projection for conflict, wildlife index, and resident acceptance under the highest-ranked policy package。
- 选定政策：compensation and predator-proof livestock program。
- 确定性说明：Certainty is highest for direction-of-change comparisons across policies and lower for numeric year-20 levels because coefficients are scenario assumptions.。

#### 20 年投影样本

| year | conflict_index | wildlife_population_index | resident_acceptance_index | implementation_maturity |
|---|---|---|---|---|
| 1 | 0.9858 | 0.9887 | 0.6007 | 0.395 |
| 2 | 0.9691 | 0.9781 | 0.6304 | 0.44 |
| 3 | 0.9501 | 0.9684 | 0.6601 | 0.485 |
| 4 | 0.9287 | 0.9594 | 0.6898 | 0.53 |
| 5 | 0.9054 | 0.9512 | 0.7195 | 0.575 |
| 16 | 0.5698 | 0.9145 | 1.0 | 1.0 |
| 17 | 0.5406 | 0.9151 | 1.0 | 1.0 |
| 18 | 0.513 | 0.9161 | 1.0 | 1.0 |
| 19 | 0.4867 | 0.9175 | 1.0 | 1.0 |
| 20 | 0.4618 | 0.9192 | 1.0 | 1.0 |

### 经济影响与社区收益
- 模型：tourism revenue and community benefit projection with revenue sharing and reduced local opportunity costs。
- 第 20 年净社区收益指数：0.0079。
- 解释：The policy is valuable only if a visible share of tourism and conservation finance reaches households bearing wildlife opportunity costs.。

#### 收益投影样本

| year | tourism_revenue_index | community_revenue_share | community_revenue_index | local_opportunity_cost_index | net_community_benefit_index |
|---|---|---|---|---|---|
| 1 | 1.0012 | 0.1426 | 0.1428 | 0.2562 | -0.1134 |
| 2 | 1.0026 | 0.1452 | 0.1456 | 0.2525 | -0.1069 |
| 3 | 1.0042 | 0.1478 | 0.1484 | 0.2488 | -0.1004 |
| 4 | 1.0058 | 0.1504 | 0.1513 | 0.2451 | -0.0939 |
| 5 | 1.0077 | 0.153 | 0.1542 | 0.2416 | -0.0874 |
| 16 | 1.0373 | 0.1816 | 0.1884 | 0.2055 | -0.0171 |
| 17 | 1.0405 | 0.1842 | 0.1917 | 0.2025 | -0.0108 |
| 18 | 1.0438 | 0.1868 | 0.195 | 0.1995 | -0.0045 |
| 19 | 1.0471 | 0.1894 | 0.1983 | 0.1966 | 0.0017 |
| 20 | 1.0504 | 0.192 | 0.2017 | 0.1937 | 0.0079 |

### 长期趋势与风险
- 投影年限：20。
- 第 20 年 conflict index：0.4618。
- 第 20 年 wildlife index：0.9192。
- 第 20 年 resident acceptance：1.0。
- 长期结果得分：0.734。

#### 风险登记

- elite capture of revenue-sharing funds
- displacement of conflict to zones outside the current preserve boundary
- tourism volatility from drought, disease, or security shocks
- weak enforcement of grazing calendars and riparian buffers

#### 监测指标

- conflict incidents per zone per season
- wildlife corridor use and calf recruitment
- household compensation processing time
- community revenue share and local hiring percentage
- vegetation cover in restoration buffers

### 迁移到其他保护区
- 适用对象：other wildlife management areas with boundary communities and tourism value。
- 限制：The framework transfers as a decision process, not as fixed numerical scores; local field data must replace the scenario coefficients.。

#### 迁移步骤

- replace zone scores with local wildlife corridors, water points, settlements, tourism assets, and conflict hotspots
- recalibrate resident pressure and opportunity-cost weights through community consultation
- test policy packages against the local legal framework and enforcement capacity
- run the same 20-year conflict/wildlife/community-benefit projection under local drought and tourism volatility scenarios
- publish a dashboard that separates ecological, resident, economic, and governance outcomes

## 模型限制
- 这是可复现的官方题面参数保护区管理实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中 Maasai Mara、Wildlife Conservation and Management Act 2013、2020 修订、分区管理、社区利益、人兽冲突和两页委员会报告等题面约束。
- 分区评分、政策收益、冲突变化率、社区收益份额和 20 年投影系数是显式确定性情景参数，不是 Maasai Mara 实地监测数据；正式论文应补充保护区 GIS、野生动物迁徙、冲突事件、旅游收入、社区调查和治理预算数据校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2023/B/q03/solution.py`

## 输出
- `mcm/question_results/2023/B/q03/result.json`
- `mcm/question_reports/2023/B/q03/report.md`
- `mcm/question_artifacts/2023/B/q03`
