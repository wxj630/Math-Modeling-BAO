# 2016-E q05：有干预水资源预测与关键问题判断

## 题目原问
Use the intervention from Task 4 and your model to project water availability into the future. Can the region become less susceptible to water scarcity? Will water become a critical issue, and when?

## 适合模型
对比无干预和有干预 15 年 stress index，判断是否降低易受缺水影响以及是否仍为 critical。对应模型：反事实预测、情景对比、政策效果评估。

## 数据与真实性
- 数据类型：official_pdf_and_world_bank_csv。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2016/Problem Data- Are we heading towards a thirsty planet`。
- 行数/记录数：{'world_bank_jordan_water_indicators.csv': 528}。
- 本脚本只使用 COMAP 官方 PDF、题面推荐的 World Bank 官方公共数据和显式规划假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 15 年无干预预测
- 最近人口增长率：0.021443。
- 用水增长率假设：0.042886。
- 15 年后 stress index：2.614749。
- 居民影响：Without intervention, higher stress implies more intermittent supply, higher water prices, more agricultural constraints, and greater health risk during drought periods.

| year_after_start | freshwater_withdrawal_pct_internal_resources | stress_index | status |
|---|---|---|---|
| 0 | 139.277 | 1.392771 | critical |
| 1 | 145.25 | 1.452501 | critical |
| 2 | 151.479 | 1.514792 | critical |
| 3 | 157.976 | 1.579755 | critical |
| 4 | 164.75 | 1.647504 | critical |
| 5 | 171.816 | 1.718158 | critical |
| 6 | 179.184 | 1.791842 | critical |
| 7 | 186.869 | 1.868687 | critical |

### 干预计划
- 策略：combine demand reduction, reuse, leakage control, new non-conventional supply, and watershed recharge; avoid relying on one megaproject

| program | annual_cost_musd | annual_withdrawal_reduction_pct_points | annual_quality_gain_pct_points | efficiency_score_per_billion_usd |
|---|---|---|---|---|
| agricultural_efficiency | 120 | 2.4 | 0.2 | 1.388889 |
| leakage_reduction_and_metering | 85 | 1.5 | 0.3 | 1.294118 |
| wastewater_reuse_and_sanitation | 95 | 1.1 | 0.9 | 1.087719 |
| rainwater_harvesting_and_aquifer_recharge | 70 | 0.8 | 0.2 | 0.857143 |
| desalination_and_renewable_energy | 220 | 1.7 | 0.4 | 0.575758 |

### 有干预预测
- 15 年后 stress index：1.489763。
- 相对无干预降低：1.124986。
- 是否降低易受缺水影响：True。
- 无干预是否 critical：True。

## 模型限制
- 这是可复现的官方 PDF + World Bank Data 水资源实验；COMAP 没有提供独立 CSV/XLSX 附件，但题面要求使用水资源数据源分析缺水，本工作流缓存 Jordan World Bank 官方指标。
- 干预效果、成本和年度降压百分点是显式规划假设，不是历史因果估计；正式论文应补充流域水文、月度供水、地下水、漏损、价格和项目成本数据校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2016/E/q05/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2016/E/q05/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2016/E/q05/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2016/E/q05`
