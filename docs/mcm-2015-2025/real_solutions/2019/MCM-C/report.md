# 2019 MCM-C The Opioid Crisis：官方 NFLIS/ACS 数据实验报告

## 数据真实性

- 官方题面：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2019/The Opioid Crisis.pdf`。
- 官方附件目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2019/Problem Data- The Opioid Crisis/2018_MCMProblemC_DATA`。
- 行数：`{'MCM_NFLIS_Data.xlsx': 24062, 'ACS county-year rows': 3245}`。
- ACS 年份：`[2010, 2011, 2012, 2013, 2014, 2015, 2016]`。
- NFLIS 文件实际州别：`['KY', 'OH', 'PA', 'VA', 'WV']`。
- 本解法只读取 COMAP 官方 Excel/CSV，不生成随机 `x1/x2/x3` 数据。

## Part 1：传播与起始位置

- 模型：县-年 NFLIS 面板、heroin/analgesic 分解、每县 OLS 趋势和 2020 外推。
- 县-年记录数：3480。
- 高风险阈值：100 reports；观察阈值：25 reports。

## Part 2：ACS 社会特征关联

- 模型：将 2010-2016 NFLIS 县-年 opioid rate 与 ACS DP02 社会特征按 FIPS/year 合并，计算描述性相关。
- 合并县-年记录数：3051。
- 重要限制：Associations are descriptive and cannot prove causality; the ACS attachment is DP02 social characteristics, not a complete economic panel.

## Part 3：反制策略情景

- 策略：Prioritize counties forecast above 100 reports for integrated lab feedback, treatment access, and supply interruption; monitor 25-99 report counties as watch areas.
- 参数边界：The combined strategy reaches a material reduction only if high-risk counties achieve about 30%+ reduction and watch counties about 10%+ reduction in forecast reports.

## DEA/NFLIS memo

To the Chief Administrator, DEA/NFLIS Database: this model uses only the provided NFLIS and ACS attachments. The most operational result is a county-year early warning panel: counties crossing 100 projected opioid/heroin reports by 2020 should receive rapid lab-feedback review, treatment capacity checks, and coordinated supply-disruption attention, while counties in the 25-99 range should be monitored before they become high-burden areas. The ACS correlations are useful triage signals but should be treated as descriptive, not causal, because the attachment is a social-characteristics panel and not a full economic or prescribing database.
