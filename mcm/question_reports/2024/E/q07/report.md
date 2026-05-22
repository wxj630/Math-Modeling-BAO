# 2024-E q07：社区保护程度、计划、时间表与成本建议信

## 题目原问
Develop a preservation model for community leaders to use to determine the extent of measures they should take to preserve buildings in their community. Select a historic landmark - not Cape Hatteras Lighthouse - that is in a location that experiences extreme weather events. Apply your insurance and preservation models to assess the value of this landmark. Compose a one-page letter to the community recommending a plan, timeline, and cost proposal.

## 适合模型
用保护紧迫度和 benefit/cost ratio 给出分阶段保护计划、7 年时间表、成本建议和给社区的一页信。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted`。
- 行数/记录数：{'official_parameters': 6}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 建址与增长决策
- 模型：site build score combining hazard exposure, service viability, community need, and resilience cost。

| site | hazard_index | service_viability | resilience_cost | build_score | recommendation |
|---|---|---|---|---|---|
| elevated inland infill | 0.42 | 0.82 | 0.22 | 0.37 | build only after site-specific elevation, drainage, and insurance conditions |
| coastal low-lying expansion | 0.86 | 0.58 | 0.64 | 0.11 | avoid new construction or relocate growth inland |
| redeveloped floodplain with green buffers | 0.66 | 0.71 | 0.46 | 0.2655 | avoid new construction or relocate growth inland |
| wildland-urban edge subdivision | 0.74 | 0.63 | 0.53 | 0.1445 | avoid new construction or relocate growth inland |

### 社区历史建筑保护模型
- 选择地标：St. Augustine Lighthouse。
- 模型：weighted cultural, historical, economic, and community significance multiplied by exposure urgency and checked against benefit/cost ratio。

| building | significance_score | preservation_urgency | benefit_cost_ratio | recommended_action |
|---|---|---|---|---|
| St. Augustine Lighthouse | 0.858 | 0.592 | 2.757 | selective retrofit and archival/documentation plan |
| historic waterfront market | 0.7555 | 0.5817 | 4.154 | protect in place with phased hardening and emergency response covenant |
| old civic theater | 0.7625 | 0.4194 | 5.378 | selective retrofit and archival/documentation plan |
| redundant warehouse district | 0.414 | 0.2567 | 2.645 | selective retrofit and archival/documentation plan |

### 地标应用与保护计划
- 地标：St. Augustine Lighthouse。
- 成本建议：8.5 million USD。
- benefit/cost ratio：2.757。
- Phase 1：0-12 months: engineering survey, corrosion/wind inspection, emergency shutters, drainage maintenance, and visitor closure triggers。
- Phase 2：1-3 years: foundation drainage, roof and lantern-room hardening, floodproof utilities, and insurance inspection covenant。
- Phase 3：3-7 years: evaluate managed retreat only if erosion and storm-surge triggers exceed the conditional underwriting band。

### 给社区的一页信
Dear community members, our insurance and preservation models recommend protecting St. Augustine Lighthouse in place over the next seven years, beginning with inspections, floodproof utilities, roof and lantern-room hardening, and clear storm-closure triggers. The plan preserves a high-value cultural and tourism asset while keeping future insurance conditional on verified risk reduction.

## 模型限制
- 这是可复现的官方题面参数保险与保护决策实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中 $1T、1000 起事件、115%、30-60%、57% 等宏观参数。
- 两个地区、建址和地标保护行是显式确定性演示情景，不是保险公司真实承保组合；正式论文应补充当地灾害频率、赔付率、建筑清单、工程造价和社区调查数据校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2024/E/q07/solution.py`

## 输出
- `mcm/question_results/2024/E/q07/result.json`
- `mcm/question_reports/2024/E/q07/report.md`
- `mcm/question_artifacts/2024/E/q07`
