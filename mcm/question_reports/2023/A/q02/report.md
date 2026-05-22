# 2023-A q02：群落受益所需的最少物种数与规模效应

## 题目原问
How many different plant species are required for the community to benefit and what happens as the number of species grows?

## 适合模型
以单物种为基线，枚举 1-12 个物种，计算末 20 年生物量、存活比例、干旱代际生物量和稳定性综合得分，识别至少 4 个物种的受益阈值。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025`。
- 行数/记录数：{'official_parameters': 6}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 生物多样性阈值
- 官方观察：communities with four or more species may adapt better than one-species communities。
- 估计受益最少物种数：4。
- 规则：at least 15% higher viability than the one-species baseline and persistence ratio >= 0.62。
- 单物种可行性得分：0.761。

#### 物种数敏感性

| species_count | mean_biomass_last20 | mean_persistence_ratio | viability_score | improvement_over_single_species_pct |
|---|---|---|---|---|
| 1 | 0.599 | 1.0 | 0.761 | 0.0 |
| 2 | 0.7259 | 0.925 | 0.8225 | 8.081 |
| 3 | 0.7121 | 0.9167 | 0.8121 | 6.715 |
| 4 | 0.7272 | 0.75 | 0.7821 | 2.773 |
| 5 | 0.7253 | 0.6 | 0.7449 | -2.116 |
| 6 | 0.74 | 0.6667 | 0.7705 | 1.248 |
| 7 | 0.7382 | 0.5714 | 0.7465 | -1.905 |
| 8 | 0.7508 | 0.625 | 0.7665 | 0.723 |
| 9 | 0.7559 | 0.6667 | 0.7795 | 2.431 |
| 10 | 0.7736 | 0.7 | 0.7981 | 4.875 |
| 11 | 0.7727 | 0.6364 | 0.7823 | 2.799 |
| 12 | 0.7893 | 0.6375 | 0.7924 | 4.126 |

## 模型限制
- 这是可复现的官方题面参数植物群落动态实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中单物种风险、四个及以上物种受益、不规则干旱、污染和栖息地减少等题面约束。
- 物种性状、干旱时间表、污染负荷和栖息地质量是显式确定性情景参数，不是野外观测；正式论文应补充样方长期监测、降水、土壤、污染和群落功能性状数据校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2023/A/q02/solution.py`

## 输出
- `mcm/question_results/2023/A/q02/result.json`
- `mcm/question_reports/2023/A/q02/report.md`
- `mcm/question_artifacts/2023/A/q02`
