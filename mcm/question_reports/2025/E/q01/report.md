# 2025-E q01：自然过程与森林转农田框架

## 题目原问
Natural Processes.

## 适合模型
官方 PDF 题面参数 + 确定性月度系统动力学：把森林转农田后的作物、野生植物、害虫、授粉者、蝙蝠、鸟类、土壤和天敌作为状态变量。

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

### 季节性系统动力学
- 模拟长度：120 个月。
- 时间步长：1 month。
- 季节函数：`0.5 + 0.5*sin(2*pi*month/12)`。
- 收获月份 mod 12：[8, 9]。

### 自然过程与当前生态系统
- 模型：monthly deterministic food-web difference equations with crop seasonality, chemical pressure, soil recovery, and consumer feedbacks。
- 解释：a newly converted field can maintain crop output under chemical control, but low wild-plant habitat keeps biodiversity and biological pest control weak。

#### 新清理农田基线

| scenario | producer_stability | consumer_stability | biodiversity_index | pest_pressure | crop_yield_index | ecosystem_stability_score |
|---|---|---|---|---|---|---|
| baseline_chemical | 0.02 | 0.02 | 0.02 | 0.02 | 2.0 | 0.029 |

## 模型限制
- 这是可复现的官方题面参数生态系统实验，适合处理没有独立 CSV/XLSX 附件的 ICM 题；它不是随机造数，也不是声称拥有真实农场观测。
- 情景参数、经济指数和系统动力学系数是显式假设；正式论文应补充本地作物、害虫监测、土壤检测、投入成本和有机溢价数据进行校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2025/E/q01/solution.py`

## 输出
- `mcm/question_results/2025/E/q01/result.json`
- `mcm/question_reports/2025/E/q01/report.md`
- `mcm/question_artifacts/2025/E/q01`
