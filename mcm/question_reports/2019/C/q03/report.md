# 2019-C q03：反制策略情景、参数边界与 DEA/NFLIS 备忘录

## 题目原问
Using a combination of Part 1 and Part 2 results, identify a possible strategy for countering the opioid crisis. Use your models to test effectiveness and identify parameter bounds. Include a memo to the Chief Administrator, DEA/NFLIS Database.

## 适合模型
基于 2020 预测设置 high/watch 县阈值，测试 lab feedback、treatment/prescriber outreach、combined supply/treatment 三类情景的报告减少幅度，并输出 DEA/NFLIS memo。对应模型：情景仿真、阈值政策、敏感性边界。

## 数据与真实性
- 数据类型：official_comap_xlsx_csv。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted/2019/Problem Data- The Opioid Crisis/2018_MCMProblemC_DATA`。
- 行数/记录数：{'MCM_NFLIS_Data.xlsx': 24062, 'ACS county-year rows': 3245}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

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

### 反制策略情景
- 策略：Prioritize counties forecast above 100 reports for integrated lab feedback, treatment access, and supply interruption; monitor 25-99 report counties as watch areas.
- 参数边界：The combined strategy reaches a material reduction only if high-risk counties achieve about 30%+ reduction and watch counties about 10%+ reduction in forecast reports.

#### Strategy scenarios

| scenario | affected_high_counties | affected_watch_counties | projected_2020_reports | reduction_vs_baseline_reports | reduction_vs_baseline_pct |
|---|---|---|---|---|---|
| baseline_no_new_intervention | 141 | 128 | 112463.35 | 0.0 | 0.0 |
| early_warning_lab_feedback | 141 | 128 | 101750.01 | 10713.34 | 9.526 |
| targeted_treatment_and_prescriber_outreach | 141 | 128 | 88949.07 | 23514.28 | 20.908 |
| combined_supply_and_treatment_strategy | 141 | 128 | 78235.73 | 34227.62 | 30.434 |

### DEA/NFLIS memo
To the Chief Administrator, DEA/NFLIS Database: this model uses only the provided NFLIS and ACS attachments. The most operational result is a county-year early warning panel: counties crossing 100 projected opioid/heroin reports by 2020 should receive rapid lab-feedback review, treatment capacity checks, and coordinated supply-disruption attention, while counties in the 25-99 range should be monitored before they become high-burden areas. The ACS correlations are useful triage signals but should be treated as descriptive, not causal, because the attachment is a social-characteristics panel and not a full economic or prescribing database.

## 模型限制
- 这是可复现的官方 The Opioid Crisis Excel/ACS CSV 附件实验；只使用 MCM_NFLIS_Data.xlsx 与 2010-2016 ACS DP02 官方附件，不使用随机造数。
- 官方 NFLIS workbook 实际包含 KY/OH/PA/VA/WV 五州记录，本脚本不补造题面文字中提到但文件缺失的 Tennessee；ACS 相关性是描述性，不等同于成瘾或流行传播的因果解释。

## 运行方式
`.venv/bin/python mcm/question_solutions/2019/C/q03/solution.py`

## 输出
- `mcm/question_results/2019/C/q03/result.json`
- `mcm/question_reports/2019/C/q03/report.md`
- `mcm/question_artifacts/2019/C/q03`
