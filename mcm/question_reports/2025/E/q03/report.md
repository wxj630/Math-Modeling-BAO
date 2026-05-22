# 2025-E q03：边缘栖息地成熟与物种回归

## 题目原问
Incorporate the reemergence of species. Over time, the edge habitats begin to mature which brings back the species native to the area. As species return, the agricultural ecosystem changes due to the interactions of these species with the current environment. Incorporate two different species into the model to determine the impacts.

## 适合模型
显式加入蝙蝠和食虫鸟两类回归物种，量化生物控害、授粉、食物网冗余和稳定性变化。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted`。
- 行数/记录数：{'official_parameters': 5}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 农业生态食物网
- 状态变量：crop, wild_plants, pests, beneficial_insects, bats, birds, soil_health, predators
- 节点数：11。
- 食物网/影响边数：12。

#### 关键食物网边

| source | target | interaction | weight |
|---|---|---|---|
| crop | pests | food | 0.72 |
| wild_plants | beneficial_insects | habitat/nectar | 0.58 |
| wild_plants | bats | edge habitat support | 0.3 |
| wild_plants | birds | nesting habitat | 0.42 |
| beneficial_insects | crop | pollination | 0.34 |
| bats | pests | predation | -0.62 |
| birds | pests | predation | -0.38 |
| predators | pests | predation | -0.32 |
| pesticide | beneficial_insects | mortality | -0.55 |
| herbicide | wild_plants | mortality | -0.6 |
| organic_input | soil_health | nutrient recovery | 0.45 |
| soil_health | crop | growth support | 0.4 |

### 物种重新出现
- 影响摘要：bat and bird reemergence raises biological control and biodiversity; full organic transition improves long-term stability but has a larger transition-cost penalty。

#### 加入物种

| species | role | expected_effect |
|---|---|---|
| bats | insectivores and pollinators | lower pest pressure and improve crop reproduction |
| insectivorous birds | pest predators and edge-habitat biodiversity indicator | additional pest suppression and food-web redundancy |

## 模型限制
- 这是可复现的官方题面参数生态系统实验，适合处理没有独立 CSV/XLSX 附件的 ICM 题；它不是随机造数，也不是声称拥有真实农场观测。
- 情景参数、经济指数和系统动力学系数是显式假设；正式论文应补充本地作物、害虫监测、土壤检测、投入成本和有机溢价数据进行校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2025/E/q03/solution.py`

## 输出
- `mcm/question_results/2025/E/q03/result.json`
- `mcm/question_reports/2025/E/q03/report.md`
- `mcm/question_artifacts/2025/E/q03`
