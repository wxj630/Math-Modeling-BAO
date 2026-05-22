# 2023-A q04：未来干旱频率和变异范围变化的影响

## 题目原问
What are the impact of a greater frequency and wider variation of the occurrence of droughts in future weather cycles? If droughts are less frequent, does the number of species have the same impact on the overall population?

## 适合模型
固定 6 物种群落，改变干旱间隔与严重度倍数，输出 more frequent / less frequent / wider variation 情景下的可持续得分和生物多样性边际价值。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025`。
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

### 干旱频率和严重度敏感性
- 低频干旱解释：When droughts are less frequent, biodiversity still improves stability, but the margin over low-richness communities narrows because recovery years dominate.。
- 未来天气解释：More frequent or more severe drought cycles shift the model toward needing functional complementarity and at least four species to avoid persistent biomass loss.。

| scenario | interval_years | severity_multiplier | mean_biomass_last20 | viability_score |
|---|---|---|---|---|
| less frequent | 11 | 1.0 | 0.7413 | 0.7677 |
| baseline irregular | 7 | 1.0 | 0.74 | 0.7705 |
| more frequent | 4 | 1.0 | 0.7158 | 0.7565 |
| very frequent | 3 | 1.0 | 0.7107 | 0.7544 |
| milder variation | 7 | 0.75 | 0.7456 | 0.7757 |
| wider severity variation | 7 | 1.25 | 0.7351 | 0.767 |

## 模型限制
- 这是可复现的官方题面参数植物群落动态实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中单物种风险、四个及以上物种受益、不规则干旱、污染和栖息地减少等题面约束。
- 物种性状、干旱时间表、污染负荷和栖息地质量是显式确定性情景参数，不是野外观测；正式论文应补充样方长期监测、降水、土壤、污染和群落功能性状数据校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2023/A/q04/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2023/A/q04/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2023/A/q04/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2023/A/q04`
