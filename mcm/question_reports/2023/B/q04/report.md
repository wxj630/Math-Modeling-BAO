# 2023-B q04：给 Kenyan Tourism and Wildlife Committee 的非技术报告

## 题目原问
Finally, provide a two-page non-technical report for the Kenyan Tourism and Wildlife Committee discussing your proposed plan and its value for the preserve.

## 适合模型
把分区策略、政策排名、长期趋势、社区收益、风险和迁移价值压缩为 Kenyan Tourism and Wildlife Committee 可读的非技术报告。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025`。
- 行数/记录数：{'official_parameters': 5}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### Maasai Mara 分区政策模型
- 模型：zone-level multi-criteria scoring for wildlife value, habitat fragility, resident pressure, conflict exposure, and tourism value。
- 政策原则：Use stricter protection in high wildlife/high fragility zones and co-management/compensation in high resident-pressure interfaces.。

#### 分区评分

| zone | conservation_priority | community_priority | balance_need | management_intensity | recommended_policy |
|---|---|---|---|---|---|
| core migration corridor | 0.8584 | 0.4576 | 0.4008 | high | strict habitat protection with community revenue sharing |
| riverine habitat and watering points | 0.8196 | 0.5196 | 0.3 | high | seasonal access zoning and riparian buffer enforcement |
| community conservancy interface | 0.6968 | 0.7456 | 0.0488 | high | co-managed conservancy with livestock compensation and grazing calendar |
| settlement and agriculture edge | 0.5424 | 0.8116 | 0.2692 | high | fencing hotspots, predator-proof bomas, crop protection and benefit payments |
| restoration buffer outside current boundary | 0.681 | 0.6796 | 0.0014 | medium | voluntary easements, grassland restoration and rotational grazing contracts |
| tourism lodge cluster | 0.6512 | 0.4584 | 0.1928 | medium | visitor caps, concession fees, waste-water standards, local hiring quota |

### 政策与管理策略排名
- 方法：weighted multi-objective evaluation balancing ecological protection, local opportunity costs, conflict reduction, tourism revenue, feasibility, and cost。
- 最优政策：compensation and predator-proof livestock program；综合得分：0.1945。

#### 政策包排名

| policy | ecological_score | resident_score | economic_score | governance_feasibility | implementation_cost_index | composite_score |
|---|---|---|---|---|---|---|
| compensation and predator-proof livestock program | 0.2708 | 0.3545 | 0.2344 | 0.73 | 0.38 | 0.1945 |
| community conservancy revenue sharing | 0.285 | 0.3561 | 0.3174 | 0.77 | 0.49 | 0.1934 |
| integrated mosaic plan | 0.3834 | 0.3961 | 0.327 | 0.7 | 0.62 | 0.1907 |
| restoration buffer and voluntary easements | 0.3376 | 0.3177 | 0.2488 | 0.67 | 0.55 | 0.1469 |
| baseline enforcement only | 0.1558 | 0.1457 | 0.1662 | 0.8 | 0.18 | 0.1453 |
| strict core zoning plus visitor caps | 0.289 | 0.2137 | 0.1948 | 0.64 | 0.42 | 0.1173 |

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

### Kenyan Tourism and Wildlife Committee 非技术报告
To the Kenyan Tourism and Wildlife Committee: adopt an integrated mosaic plan for the Maasai Mara that keeps strict protection in core wildlife corridors, shares tourism revenue through community conservancies, funds compensation and predator-proof livestock measures at settlement edges, and restores buffer lands through voluntary easements. This approach protects wildlife and natural resources while directly addressing the lost opportunities and human-wildlife conflict borne by neighboring residents.

## 模型限制
- 这是可复现的官方题面参数保护区管理实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中 Maasai Mara、Wildlife Conservation and Management Act 2013、2020 修订、分区管理、社区利益、人兽冲突和两页委员会报告等题面约束。
- 分区评分、政策收益、冲突变化率、社区收益份额和 20 年投影系数是显式确定性情景参数，不是 Maasai Mara 实地监测数据；正式论文应补充保护区 GIS、野生动物迁徙、冲突事件、旅游收入、社区调查和治理预算数据校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2023/B/q04/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2023/B/q04/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2023/B/q04/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2023/B/q04`
