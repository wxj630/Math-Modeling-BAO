# 2023-C-Boats q02：区域对挂牌价的实际与统计影响

## 题目原问
Use your model to explain the effect, if any, of region on listing prices. Discuss whether regional effects are consistent across all sailboat variants and address practical and statistical significance.

## 适合模型
以 Europe 为基准，对 log(price) 做 OLS 区域效应模型，控制长度、船龄、船型和船型-区域交互，报告百分比效应、p 值和船型一致性。

## 数据与真实性
- 数据类型：official_comap_xlsx。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted/2023/Problem Data- Understanding Used Sailboat Prices`。
- 行数/记录数：{'monohull': 2346, 'catamaran': 1145}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 区域效应
- 模型：OLS on log price with controls for length, age, hull type, region, and hull-by-region interactions; Europe is the baseline region。
- 基准区域：Europe。

| region | hull_type | price_effect_pct | p_value | statistically_significant_5pct |
|---|---|---|---|---|
| Caribbean | monohull | -9.449 | 8e-05 | True |
| Caribbean | catamaran | -8.998 | 0.881549 | False |
| USA | monohull | 33.518 | 0.0 | True |
| USA | catamaran | 13.141 | 1e-05 | True |

#### 船型间一致性

| region | catamaran_minus_monohull_log_effect | interaction_p_value | consistent_at_5pct |
|---|---|---|---|
| Caribbean | 0.004968 | 0.881549 | True |
| USA | -0.165597 | 1e-05 | False |

## 模型限制
- 这是可复现的官方帆船 Excel 基线实验，适合做论文骨架、结果表和图；随机森林和 OLS 区域效应都不应被解释为严格因果。
- COMAP 官方数据不含香港记录；香港部分使用带 URL 的补充挂牌样本做情景比较，正式论文应继续扩充香港本地成交/挂牌样本并记录抓取日期。

## 运行方式
`.venv/bin/python mcm/question_solutions/2023/C-Boats/q02/solution.py`

## 输出
- `mcm/question_results/2023/C-Boats/q02/result.json`
- `mcm/question_reports/2023/C-Boats/q02/report.md`
- `mcm/question_artifacts/2023/C-Boats/q02`
