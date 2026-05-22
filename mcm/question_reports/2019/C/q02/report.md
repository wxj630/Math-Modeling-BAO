# 2019-C q02：ACS 社会经济因素关联与模型修正

## 题目原问
Using the U.S. Census socio-economic data provided, determine whether use or trends-in-use are associated with any of the provided Census data, and modify the model from Part 1 to include important factors.

## 适合模型
读取 2010-2016 官方 ACS DP02 CSV，按 FIPS/year 合并 NFLIS opioid_rate_per_1000_drug_reports，计算教育、退伍军人、残障、外来出生、居住稳定性等特征的描述性相关。对应模型：面板合并、相关分析、社会特征解释。

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

### ACS 社会特征关联
- 合并县-年行数：3051。
- 目标：opioid_rate_per_1000_drug_reports。
- 方法：County-year Pearson correlations between official NFLIS opioid rate and official ACS DP02 social characteristics.
- 谨慎解释：Associations are descriptive and cannot prove causality; the ACS attachment is DP02 social characteristics, not a complete economic panel.

#### Top correlations

| feature | correlation_with_opioid_rate_per_1000 | usable_county_year_rows | interpretation |
|---|---|---|---|
| disability_pct | 0.176142 | 1748 | positive association |
| foreign_born_pct | -0.15202 | 1748 | negative association |
| bachelor_or_higher_pct | -0.130754 | 3051 | negative association |
| high_school_or_higher_pct | -0.122604 | 3051 | negative association |
| civilian_veteran_pct | -0.106733 | 1748 | negative association |
| total_households | -0.048063 | 3051 | negative association |
| same_house_one_year_pct | 0.008547 | 1748 | positive association |

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
`.venv/bin/python mcm/question_solutions/2019/C/q02/solution.py`

## 输出
- `mcm/question_results/2019/C/q02/result.json`
- `mcm/question_reports/2019/C/q02/report.md`
- `mcm/question_artifacts/2019/C/q02`
