# 2024-E q06：识别需要保存保护的重要建筑

## 题目原问
As a community leader, how could you identify buildings in a community that should be preserved and protected due to their cultural, historical, economic, or community significance?

## 适合模型
构造文化、历史、经济和社区意义加权分，并乘以灾害暴露形成保护紧迫度，排除 Cape Hatteras Lighthouse 后选择 St. Augustine Lighthouse 做应用。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted`。
- 行数/记录数：{'official_parameters': 6}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

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

## 模型限制
- 这是可复现的官方题面参数保险与保护决策实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中 $1T、1000 起事件、115%、30-60%、57% 等宏观参数。
- 两个地区、建址和地标保护行是显式确定性演示情景，不是保险公司真实承保组合；正式论文应补充当地灾害频率、赔付率、建筑清单、工程造价和社区调查数据校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2024/E/q06/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2024/E/q06/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2024/E/q06/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2024/E/q06`
