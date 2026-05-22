# 2025-E q04：去除除草剂与蝙蝠再平衡

## 题目原问
Removal of herbicide. If the herbicide was removed, report on the stability of the ecosystem in terms of the producers and consumers. Bring the ecosystem back into balance by incorporating bats into the food web model. Identify another species that can provide benefits to bring the ecosystem back into balance and compare the impacts.

## 适合模型
比较 remove_herbicide 与 bats_and_edge_habitat 情景的生产者稳定性、消费者稳定性、害虫压力和蝙蝠/鸟类再平衡效果。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted`。
- 行数/记录数：{'official_parameters': 5}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 物种重新出现
- 影响摘要：bat and bird reemergence raises biological control and biodiversity; full organic transition improves long-term stability but has a larger transition-cost penalty。

#### 加入物种

| species | role | expected_effect |
|---|---|---|
| bats | insectivores and pollinators | lower pest pressure and improve crop reproduction |
| insectivorous birds | pest predators and edge-habitat biodiversity indicator | additional pest suppression and food-web redundancy |

### 去除除草剂与再平衡
- 生产者稳定性：0.542。
- 消费者稳定性：0.0645。
- 害虫压力：0.1694。
- 解释：removing herbicide alone helps wild plants and soil but leaves pesticide pressure and pest dependence; adding bats and edge habitat improves balance more robustly。

## 模型限制
- 这是可复现的官方题面参数生态系统实验，适合处理没有独立 CSV/XLSX 附件的 ICM 题；它不是随机造数，也不是声称拥有真实农场观测。
- 情景参数、经济指数和系统动力学系数是显式假设；正式论文应补充本地作物、害虫监测、土壤检测、投入成本和有机溢价数据进行校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2025/E/q04/solution.py`

## 输出
- `mcm/question_results/2025/E/q04/result.json`
- `mcm/question_reports/2025/E/q04/report.md`
- `mcm/question_artifacts/2025/E/q04`
