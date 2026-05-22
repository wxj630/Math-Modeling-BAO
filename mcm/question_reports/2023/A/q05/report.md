# 2023-A q05：污染和栖息地减少对结论的影响

## 题目原问
How do other factors such as pollution and habitat reduction impact your conclusions?

## 适合模型
把污染负荷作为生长惩罚、栖息地质量作为承载量约束，比较 baseline、high pollution、habitat reduction、combined stress 和 restoration buffer。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025`。
- 行数/记录数：{'official_parameters': 6}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

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

## 模型限制
- 这是可复现的官方题面参数植物群落动态实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中单物种风险、四个及以上物种受益、不规则干旱、污染和栖息地减少等题面约束。
- 物种性状、干旱时间表、污染负荷和栖息地质量是显式确定性情景参数，不是野外观测；正式论文应补充样方长期监测、降水、土壤、污染和群落功能性状数据校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2023/A/q05/solution.py`

## 输出
- `mcm/question_results/2023/A/q05/result.json`
- `mcm/question_reports/2023/A/q05/report.md`
- `mcm/question_artifacts/2023/A/q05`
