# 2025-E q05：有机农业情景与权衡前沿

## 题目原问
Go green? Analyze the implications of a farmer considering organic farming methods. Consideration should be given to different scenarios with varying components of organic farming. Demonstrate the impact on the ecosystem as a whole and to the individual components. Discuss aspects such as pest control, crop health, plant reproduction, biodiversity, long-term sustainability and cost effectiveness.

## 适合模型
比较化学基线、去除除草剂、蝙蝠边缘栖息地、部分有机和完全有机五个情景，输出生态稳定、害虫压力、产量、净收益和成本有效性排序。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted`。
- 行数/记录数：{'official_parameters': 5}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 季节性系统动力学
- 模拟长度：120 个月。
- 时间步长：1 month。
- 季节函数：`0.5 + 0.5*sin(2*pi*month/12)`。
- 收获月份 mod 12：[8, 9]。

### 有机农业情景比较
- 方法：compare deterministic chemical, herbicide-removal, habitat/bat, partial-organic, and full-organic scenarios by ecology plus economics。
- 推荐过渡：organic_partial。
- 理由：partial organic practices capture most biodiversity and stability gains while preserving a stronger net-margin index during transition。

#### 情景排序

| scenario | crop_yield_index | pest_pressure | biodiversity_index | ecosystem_stability_score | net_margin_index | sustainability_score |
|---|---|---|---|---|---|---|
| organic_full | 135.0 | 0.02 | 1.23 | 2.133 | 120.6 | 1.4659 |
| organic_partial | 135.0 | 0.02 | 1.23 | 2.133 | 117.56 | 1.4659 |
| bats_and_edge_habitat | 135.0 | 0.02 | 1.23 | 2.133 | 113.245 | 1.4659 |
| remove_herbicide | 78.65 | 0.1694 | 0.1923 | 0.5573 | 65.925 | 0.3651 |
| baseline_chemical | 2.0 | 0.02 | 0.02 | 0.029 | -11.99 | 0.019 |

## 模型限制
- 这是可复现的官方题面参数生态系统实验，适合处理没有独立 CSV/XLSX 附件的 ICM 题；它不是随机造数，也不是声称拥有真实农场观测。
- 情景参数、经济指数和系统动力学系数是显式假设；正式论文应补充本地作物、害虫监测、土壤检测、投入成本和有机溢价数据进行校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2025/E/q05/solution.py`

## 输出
- `mcm/question_results/2025/E/q05/result.json`
- `mcm/question_reports/2025/E/q05/report.md`
- `mcm/question_artifacts/2025/E/q05`
