# 2023-C-Boats q05：给香港帆船经纪人的报告

## 题目原问
Prepare a one- to two-page report for the Hong Kong (SAR) sailboat broker with a few well-chosen graphics.

## 适合模型
把官方价格模型精度、区域效应、香港情景、双体/单体差异和经纪报价建议压缩成可执行摘要。

## 数据与真实性
- 数据类型：official_comap_xlsx。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted/2023/Problem Data- Understanding Used Sailboat Prices`。
- 行数/记录数：{'monohull': 2346, 'catamaran': 1145}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 帆船挂牌价模型
- 模型：RandomForestRegressor on official COMAP rows with length, age, hull type, make, variant, region, country/state, and variant sample size。
- 目标变量：log(Listing Price USD)。
- 训练行数：2792，留出行数：699。
- 留出 MAE/RMSE：42771.77 / 71407.35 USD。
- 留出 MAPE/Median APE：0.161752 / 0.106591。

#### 型号价格精度

| hull_type | make | variant | holdout_count | observed_median_price | predicted_median_price | median_abs_pct_error |
|---|---|---|---|---|---|---|
| catamaran | Lagoon | 450 | 30 | 472657.5 | 457933.4 | 0.076469 |
| catamaran | Lagoon | 42 | 17 | 480291.0 | 518398.16 | 0.068159 |
| catamaran | Lagoon | 440 | 16 | 327712.5 | 340632.05 | 0.067211 |
| catamaran | Lagoon | 400 | 15 | 333781.0 | 329393.69 | 0.032397 |
| monohull | Bavaria | 50 Cruiser | 11 | 133617.0 | 135071.32 | 0.12578 |
| monohull | Beneteau | Oceanis 45 | 11 | 241786.0 | 235775.08 | 0.13826 |
| catamaran | Lagoon | 500 | 10 | 510198.5 | 514944.3 | 0.024505 |
| catamaran | Lagoon | 450F | 10 | 558043.0 | 529563.07 | 0.065192 |
| monohull | Bavaria | Cruiser 46 | 10 | 148803.0 | 147819.21 | 0.107113 |
| monohull | Beneteau | Oceanis 40 | 10 | 130942.0 | 109947.68 | 0.12412 |
| monohull | Bavaria | 40 Cruiser | 9 | 97162.0 | 98908.06 | 0.040773 |
| monohull | Beneteau | Oceanis 50 | 9 | 199900.0 | 204771.44 | 0.083002 |

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

### 帆船数据其他推论
- 双体船中位价：431654.0 USD。
- 单体船中位价：193182.5 USD。
- 双体船中位溢价：123.444%。
- 价格与长度相关系数：0.369121。
- 价格与船龄相关系数：-0.473493。

#### 区域-船型摘要

| hull_type | region | count | median_price | median_length |
|---|---|---|---|---|
| catamaran | Caribbean | 302 | 380000.0 | 44.6 |
| catamaran | Europe | 735 | 449087.0 | 43.6 |
| catamaran | USA | 108 | 449000.0 | 43.0 |
| monohull | Caribbean | 178 | 176131.0 | 45.0 |
| monohull | Europe | 1783 | 193137.0 | 45.0 |
| monohull | USA | 385 | 210000.0 | 43.0 |

#### 高中位价品牌

| hull_type | make | count | median_price |
|---|---|---|---|
| catamaran | Bali | 54 | 455973.0 |
| catamaran | Lagoon | 682 | 445456.5 |
| monohull | X-Yachts | 42 | 403894.0 |
| catamaran | Fountaine Pajot | 160 | 398964.5 |
| catamaran | Nautitech | 80 | 381105.0 |
| catamaran | Leopard | 89 | 350000.0 |
| monohull | Grand Soleil | 65 | 259945.0 |
| monohull | Dehler | 28 | 205284.0 |
| monohull | Hanse | 179 | 204500.0 |
| monohull | Catalina | 37 | 204069.0 |

### 给香港经纪人的摘要报告
For the Hong Kong broker, the COMAP workbook supports a reliable baseline for Europe, USA, and Caribbean listings, with a holdout MAPE of 0.161752 on official rows. Catamarans have a median price of $431,654, compared with $193,182 for monohulls, a median premium of 123.444%. Region matters after controlling for length, age, and hull type, but the effect is not identical for monohulls and catamarans. The official workbook contains no Hong Kong listings, so the Hong Kong analysis uses a separately documented current-listing scenario: catamaran: median HK effect 61.486% from 4 listings; monohull: median HK effect -2.396% from 3 listings. Treat these Hong Kong effects as broker calibration signals, not as COMAP official data. For pricing practice, quote an interval around the model price, then adjust for local inventory scarcity, survey condition, and equipment quality.

## 模型限制
- 这是可复现的官方帆船 Excel 基线实验，适合做论文骨架、结果表和图；随机森林和 OLS 区域效应都不应被解释为严格因果。
- COMAP 官方数据不含香港记录；香港部分使用带 URL 的补充挂牌样本做情景比较，正式论文应继续扩充香港本地成交/挂牌样本并记录抓取日期。

## 运行方式
`.venv/bin/python mcm/question_solutions/2023/C-Boats/q05/solution.py`

## 输出
- `mcm/question_results/2023/C-Boats/q05/result.json`
- `mcm/question_reports/2023/C-Boats/q05/report.md`
- `mcm/question_artifacts/2023/C-Boats/q05`
