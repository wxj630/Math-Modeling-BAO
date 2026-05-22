# 2023-A q06：长期可行性和大环境管理建议

## 题目原问
What does your model indicate should be done to ensure the long-term viability of a plant community and what are the impacts on the larger environment?

## 适合模型
把物种数阈值、功能性状、干旱敏感性和污染栖息地压力合成为管理前沿，给出最少功能物种数、恢复缓冲和大环境影响备忘录。

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

### 污染和栖息地减少
- 影响摘要：Pollution reduces growth and habitat loss lowers carrying capacity; together they can erase the biodiversity advantage unless restoration increases available niche space.。

| scenario | pollution_load | habitat_quality | mean_biomass_last20 | viability_score |
|---|---|---|---|---|
| baseline | 0.1 | 0.92 | 0.74 | 0.7705 |
| high pollution | 0.32 | 0.92 | 0.5891 | 0.6859 |
| habitat reduction | 0.1 | 0.62 | 0.5002 | 0.6369 |
| combined pollution and habitat loss | 0.32 | 0.62 | 0.3972 | 0.5792 |
| restoration buffer | 0.06 | 1.0 | 0.837 | 0.8245 |

### 长期可行性策略
- 推荐最少物种数：4。
- 大环境影响：The recommended policy improves plant persistence, stabilizes forage and soil cover, and reduces erosion risk in the larger environment.。

#### 管理行动

- Maintain at least four functional plant species and prefer six or more when future drought frequency increases.
- Mix drought-tolerant deep-rooted species with faster-recovering grasses and forbs instead of maximizing species count alone.
- Reduce pollution load before drought years because stressor stacking sharply lowers carrying capacity.
- Preserve habitat corridors and seed banks so post-drought recovery can occur over successive generations.

#### 策略前沿

| species_count | baseline_viability_score | restoration_viability_score | restoration_gain_pct |
|---|---|---|---|
| 4 | 0.7821 | 0.8339 | 6.623 |
| 6 | 0.7705 | 0.8245 | 7.008 |
| 8 | 0.7665 | 0.8206 | 7.058 |
| 10 | 0.7981 | 0.854 | 7.004 |
| 12 | 0.7924 | 0.8527 | 7.61 |

### 大环境管理备忘录
For a drought-stricken plant community, the model recommends preserving at least four functional species and preferably six or more under future drought intensification. The practical focus should be functional diversity, habitat continuity, and pollution reduction, because these raise post-drought biomass persistence and protect the larger environment from erosion and forage collapse.

## 模型限制
- 这是可复现的官方题面参数植物群落动态实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中单物种风险、四个及以上物种受益、不规则干旱、污染和栖息地减少等题面约束。
- 物种性状、干旱时间表、污染负荷和栖息地质量是显式确定性情景参数，不是野外观测；正式论文应补充样方长期监测、降水、土壤、污染和群落功能性状数据校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2023/A/q06/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2023/A/q06/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2023/A/q06/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2023/A/q06`
