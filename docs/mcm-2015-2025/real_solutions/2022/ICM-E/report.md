# 2022 ICM-E Forestry for Carbon Sequestration

## 数据真实性
- 官方来源：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets/2022/Forestry for Carbon Sequestration`。
- 本题无 COMAP 数值附件；脚本只使用官方题面要求和显式确定性森林管理情景，不使用随机占位数据。

## 官方题面参数
- 评估年限：100 年。
- 当前采伐间隔：40 年；过渡要求：延长 10 年。

## 模型摘要
- 碳模型：annual deterministic live-tree, soil, product-pool, and substitution-credit carbon accounting。
- 决策权重：{'carbon_storage': 0.38, 'biodiversity': 0.22, 'recreation': 0.14, 'cultural': 0.1, 'forest_products': 0.16}。
- 推荐包含采伐的森林：temperate mixed hardwood community forest，方案：selective_60_year，100 年 CO2e：1066.4192 t/ha。

## 管理计划谱系
Leave the forest uncut when no_harvest has the highest decision score or when biodiversity sensitivity is high and community product need is low.
The 50-year interval is the first extension beyond current 40-year practice that preserves product flow while increasing living and product carbon.

## 社区文章摘录
A local community can protect its forest and still use wood carefully. The model counts carbon in standing trees, soil, and long-lived products, then compares those benefits with habitat, recreation, cultural use, and local product needs. For the managed pine production forest, a longer harvest interval with more wood going into durable products stores substantial carbon over 100 years while keeping jobs and stewardship revenue. The recommendation is not to cut every forest: the old-growth reserve remains best left uncut. The point is to match the plan to the forest, monitor the carbon account, and move gradually so residents, workers, and forest users can see the tradeoffs.

## 输出产物
- `carbon_stock_trajectories.csv`：逐年活树、土壤、产品碳轨迹。
- `management_plan_scores.csv`：各森林与管理计划的碳和社会得分。
- `forest_application_results.csv`：各种森林的推荐计划。
- `transition_schedule.csv`：从 40 年到 50 年采伐间隔的过渡安排。
- `management_tradeoff_frontier.png`：100 年 CO2e 与社会得分权衡图。
