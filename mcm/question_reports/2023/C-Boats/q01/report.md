# 2023-C-Boats q01：二手帆船挂牌价解释模型与估计精度

## 题目原问
Develop a mathematical model that explains the listing price of each sailboat in the provided spreadsheet. Include useful predictors, identify data sources, and discuss precision for each sailboat variant's price.

## 适合模型
读取官方单体船/双体船 Excel，清洗长度、船龄、品牌、型号、区域和价格，用随机森林预测 log(price)，并在留出集按型号统计误差精度。

## 数据与真实性
- 数据类型：official_comap_xlsx。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted/2023/Problem Data- Understanding Used Sailboat Prices`。
- 行数/记录数：{'monohull': 2346, 'catamaran': 1145}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 特征变量

- `length_ft`
- `age_years`
- `variant_observation_count`
- `hull_type`
- `make`
- `variant`
- `geographic_region`
- `country_region_state`

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

## 模型限制
- 这是可复现的官方帆船 Excel 基线实验，适合做论文骨架、结果表和图；随机森林和 OLS 区域效应都不应被解释为严格因果。
- COMAP 官方数据不含香港记录；香港部分使用带 URL 的补充挂牌样本做情景比较，正式论文应继续扩充香港本地成交/挂牌样本并记录抓取日期。

## 运行方式
`.venv/bin/python mcm/question_solutions/2023/C-Boats/q01/solution.py`

## 输出
- `mcm/question_results/2023/C-Boats/q01/result.json`
- `mcm/question_reports/2023/C-Boats/q01/report.md`
- `mcm/question_artifacts/2023/C-Boats/q01`
