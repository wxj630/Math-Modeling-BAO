# 2023-B q01：保护区内不同区域的政策和管理策略

## 题目原问
Consider and recommend specific policies and management strategies for different areas within the current preserve that will protect wildlife and other natural resources while also balancing the interests of the people who live in the area. These policies and strategies should help mitigate the impacts of lost opportunities experienced by the people who live near the preserve, as well as minimize negative interactions between animals and the people attracted to the preserve.

## 适合模型
官方 PDF 题面 + Maasai Mara 分区多指标评价：wildlife value、habitat fragility、resident pressure、conflict exposure、tourism value；对应教程模型：综合评价与权重决策、空间分区。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025`。
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

## 模型限制
- 这是可复现的官方题面参数保护区管理实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中 Maasai Mara、Wildlife Conservation and Management Act 2013、2020 修订、分区管理、社区利益、人兽冲突和两页委员会报告等题面约束。
- 分区评分、政策收益、冲突变化率、社区收益份额和 20 年投影系数是显式确定性情景参数，不是 Maasai Mara 实地监测数据；正式论文应补充保护区 GIS、野生动物迁徙、冲突事件、旅游收入、社区调查和治理预算数据校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2023/B/q01/solution.py`

## 输出
- `mcm/question_results/2023/B/q01/result.json`
- `mcm/question_reports/2023/B/q01/report.md`
- `mcm/question_artifacts/2023/B/q01`
