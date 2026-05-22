# 2023-C-Boats q03：香港市场可比挂牌样本与区域效应情景

## 题目原问
Discuss how the regional modeling can be useful in the Hong Kong (SAR) market. Choose an informative subset split between monohulls and catamarans, find comparable Hong Kong listing prices, and model the Hong Kong regional effect.

## 适合模型
明确官方 Excel 没有香港行；用带来源 URL 的香港当前挂牌补充样本做情景校准，并与官方区域模型对同船型/长度/船龄的预测中位价比较。

## 数据与真实性
- 数据类型：official_comap_xlsx。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2023/Problem Data- Understanding Used Sailboat Prices`。
- 行数/记录数：{'monohull': 2346, 'catamaran': 1145}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 香港市场情景
- 官方 Excel 中香港行数：0。
- 解释：The COMAP workbook has no Hong Kong rows; the Hong Kong effect is therefore a transparent supplemental-market scenario, not an official-COMAP estimate.
- 补充来源数：2。

#### 香港可比挂牌样本

| make | variant | hull_type | length_ft | year | listing_price_usd | known_region_model_price_median_usd | hk_effect_pct_vs_known_region_model | source |
|---|---|---|---|---|---|---|---|---|
| Beneteau | Sense 43 | monohull | 43.0 | 2013 | 230000.0 | 221860.82 | 3.669 | boats.com |
| Beneteau | Sense 51 | monohull | 51.0 | 2017 | 445000.0 | 596342.91 | -25.379 | boats.com |
| Jeanneau | Sun Odyssey 389 | monohull | 38.9 | 2019 | 190000.0 | 194663.86 | -2.396 | boats.com |
| Lagoon | 46 | catamaran | 46.0 | 2020 | 973092.0 | 760920.12 | 27.884 | boats.com |
| Lagoon | 42 | catamaran | 42.0 | 2022 | 904919.0 | 485906.43 | 86.233 | boats.com |
| Lagoon | 450 | catamaran | 45.0 | 2014 | 745426.0 | 475635.15 | 56.722 | boats.com |
| Fountaine Pajot | Saba 50 | catamaran | 50.0 | 2016 | 1242844.0 | 747573.55 | 66.25 | boats.com |

#### 按船型汇总

| hull_type | sample_count | median_hk_effect_pct | mean_hk_effect_pct | median_listing_price_usd |
|---|---|---|---|---|
| catamaran | 4 | 61.486 | 59.272 | 939005.5 |
| monohull | 3 | -2.396 | -8.035 | 230000.0 |

## 模型限制
- 这是可复现的官方帆船 Excel 基线实验，适合做论文骨架、结果表和图；随机森林和 OLS 区域效应都不应被解释为严格因果。
- COMAP 官方数据不含香港记录；香港部分使用带 URL 的补充挂牌样本做情景比较，正式论文应继续扩充香港本地成交/挂牌样本并记录抓取日期。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2023/C-Boats/q03/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2023/C-Boats/q03/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2023/C-Boats/q03/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2023/C-Boats/q03`
