# 2023 MCM-C/Problem Y 二手帆船价格真实数据实验报告

## 数据来源
- 官方附件：`docs/mcm-2015-2025/official_assets_extracted/2023/Problem Data- Understanding Used Sailboat Prices/2023_MCM_Problem_Y_Data.xlsx`。
- 清洗后记录数：3491，单体船 2346，双体船 1145。
- 香港市场补充样本只用于 Q3 情景比较；训练和主模型必须读取 COMAP 官方 Excel。

## Q1 挂牌价解释模型
- 模型：RandomForestRegressor on official COMAP rows with length, age, hull type, make, variant, region, country/state, and variant sample size。
- 留出集：699 行；MAE/RMSE：42771.77 / 71407.35 USD。
- MAPE/Median APE：0.161752 / 0.106591。

## Q2 区域效应
- 区域模型：OLS on log price with controls for length, age, hull type, region, and hull-by-region interactions; Europe is the baseline region。

| region | hull_type | price_effect_pct | p_value | significant |
|---|---|---:|---:|---|
| Caribbean | monohull | -9.449 | 8e-05 | True |
| Caribbean | catamaran | -8.998 | 0.881549 | False |
| USA | monohull | 33.518 | 0.0 | True |
| USA | catamaran | 13.141 | 1e-05 | True |

## Q3 香港市场情景
The COMAP workbook has no Hong Kong rows; the Hong Kong effect is therefore a transparent supplemental-market scenario, not an official-COMAP estimate.

| hull_type | sample_count | median_hk_effect_pct | median_listing_price_usd |
|---|---:|---:|---:|
| catamaran | 4 | 61.486 | 939005.5 |
| monohull | 3 | -2.396 | 230000.0 |

## Q4 其他结论
- 双体船中位价：431654.0 USD；单体船中位价：193182.5 USD。
- 双体船中位溢价：123.444%。
- 价格与长度相关系数：0.369121；价格与船龄相关系数：-0.473493。

## Q5 给香港经纪人的摘要报告
For the Hong Kong broker, the COMAP workbook supports a reliable baseline for Europe, USA, and Caribbean listings, with a holdout MAPE of 0.161752 on official rows. Catamarans have a median price of $431,654, compared with $193,182 for monohulls, a median premium of 123.444%. Region matters after controlling for length, age, and hull type, but the effect is not identical for monohulls and catamarans. The official workbook contains no Hong Kong listings, so the Hong Kong analysis uses a separately documented current-listing scenario: catamaran: median HK effect 61.486% from 4 listings; monohull: median HK effect -2.396% from 3 listings. Treat these Hong Kong effects as broker calibration signals, not as COMAP official data. For pricing practice, quote an interval around the model price, then adjust for local inventory scarcity, survey condition, and equipment quality.

## 输出文件
- `result.json`：docs/mcm-2015-2025/real_solutions/2023/MCM-C-Boats/result.json
- `clean_boat_data.csv`：docs/mcm-2015-2025/real_solutions/2023/MCM-C-Boats/artifacts/clean_boat_data.csv
- `variant_precision.csv`：docs/mcm-2015-2025/real_solutions/2023/MCM-C-Boats/artifacts/variant_precision.csv
- `region_effects.csv`：docs/mcm-2015-2025/real_solutions/2023/MCM-C-Boats/artifacts/region_effects.csv
- `hong_kong_comparables.csv`：docs/mcm-2015-2025/real_solutions/2023/MCM-C-Boats/artifacts/hong_kong_comparables.csv
- `price_by_region_hull.png`：docs/mcm-2015-2025/real_solutions/2023/MCM-C-Boats/artifacts/price_by_region_hull.png
