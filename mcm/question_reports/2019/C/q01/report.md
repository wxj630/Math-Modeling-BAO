# 2019-C q01：NFLIS 县域传播、起始位置与 2020 风险预测

## 题目原问
Using the NFLIS data provided, build a mathematical model to describe the spread and characteristics of the reported synthetic opioid and heroin incidents in and between the five states and their counties over time. Identify possible locations where specific opioid use might have started, and forecast future threshold concerns.

## 适合模型
读取官方 MCM_NFLIS_Data.xlsx，按 FIPS/year/state/county 汇总 heroin 与 synthetic_or_other_analgesic 报告，构建县-年面板；用最早阳性县和 2010-2017 每县 OLS 趋势识别起点和 2020 高风险阈值。对应模型：时空面板、趋势回归、阈值预警。

## 数据与真实性
- 数据类型：official_comap_xlsx_csv。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted/2019/Problem Data- The Opioid Crisis/2018_MCMProblemC_DATA`。
- 行数/记录数：{'MCM_NFLIS_Data.xlsx': 24062, 'ACS county-year rows': 3245}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### Opioid Crisis 传播模型
- 县-年面板行数：3480。
- 县数量：461。
- 物质类别：['heroin', 'synthetic_or_other_analgesic']。

#### 各州可能起始县

| state | earliest_year | county | fips | opioid_reports | rate_per_1000_drug_reports |
|---|---|---|---|---|---|
| KY | 2010 | JEFFERSON | 21111 | 1293 | 238.297088 |
| KY | 2010 | FAYETTE | 21067 | 547 | 278.08846 |
| OH | 2010 | HAMILTON | 39061 | 3628 | 263.280116 |
| OH | 2010 | MONTGOMERY | 39113 | 1685 | 216.081046 |
| PA | 2010 | PHILADELPHIA | 42101 | 6259 | 186.763346 |
| PA | 2010 | ALLEGHENY | 42003 | 3415 | 401.764706 |
| VA | 2010 | RICHMOND | 51760 | 599 | 207.697642 |
| VA | 2010 | FAIRFAX | 51059 | 383 | 114.773749 |
| WV | 2010 | KANAWHA | 54039 | 340 | 236.111111 |
| WV | 2010 | MERCER | 54055 | 326 | 555.366269 |

### 2020 风险预测与阈值
- 方法：Per-county ordinary least squares trend on official 2010-2017 NFLIS opioid reports.
- high threshold：100 reports。
- watch threshold：25 reports。
- 县级趋势中位 MAE：14.3036。

#### 2020 forecast top counties

| state | county | FIPS_Combined | observed_2017_reports | forecast_2020_reports | forecast_threshold |
|---|---|---|---|---|---|
| OH | HAMILTON | 39061 | 9995.0 | 11277.99 | high |
| OH | CUYAHOGA | 39035 | 7381.0 | 9042.05 | high |
| PA | PHILADELPHIA | 42101 | 9156.0 | 8544.23 | high |
| PA | ALLEGHENY | 42003 | 4653.0 | 5830.85 | high |
| OH | FRANKLIN | 39049 | 3016.0 | 4292.05 | high |
| OH | MONTGOMERY | 39113 | 3560.0 | 4278.2 | high |
| OH | LAKE | 39085 | 2127.0 | 2922.56 | high |
| PA | DELAWARE | 42045 | 1667.0 | 2119.83 | high |
| KY | JEFFERSON | 21111 | 2124.0 | 2044.29 | high |
| OH | BUTLER | 39017 | 1275.0 | 1616.11 | high |

### 扩散与空间聚类
- 题面新蜂后范围：None km。
- Positive ID 数：None。
- 首个阳性日期：None；最后阳性日期：None。
- 首个阳性到最远阳性距离：None km。
- 精度说明：None

## 模型限制
- 这是可复现的官方 The Opioid Crisis Excel/ACS CSV 附件实验；只使用 MCM_NFLIS_Data.xlsx 与 2010-2016 ACS DP02 官方附件，不使用随机造数。
- 官方 NFLIS workbook 实际包含 KY/OH/PA/VA/WV 五州记录，本脚本不补造题面文字中提到但文件缺失的 Tennessee；ACS 相关性是描述性，不等同于成瘾或流行传播的因果解释。

## 运行方式
`.venv/bin/python mcm/question_solutions/2019/C/q01/solution.py`

## 输出
- `mcm/question_results/2019/C/q01/result.json`
- `mcm/question_reports/2019/C/q01/report.md`
- `mcm/question_artifacts/2019/C/q01`
