# 2016-E q04：覆盖所有缺水驱动因素的干预计划

## 题目原问
For your chosen region, design an intervention plan taking all the drivers of water scarcity into account. Discuss surrounding-area and ecosystem impacts, strengths and weaknesses.

## 适合模型
设计农业节水、污水回用和卫生、漏损控制、海水淡化+可再生能源、雨水收集和地下水回补五类组合计划，并记录周边生态影响。对应模型：干预组合设计、成本效益分析、生态外部性评估。

## 数据与真实性
- 数据类型：official_pdf_and_world_bank_csv。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2016/Problem Data- Are we heading towards a thirsty planet`。
- 行数/记录数：{'world_bank_jordan_water_indicators.csv': 528}。
- 本脚本只使用 COMAP 官方 PDF、题面推荐的 World Bank 官方公共数据和显式规划假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 清洁水供给能力与缺水诊断
- 定义：A region is critical when withdrawals exceed internal renewable resources after adjusting for service gaps and economic capacity.
- 选定地区：Jordan。
- 基线年份：2024。
- freshwater withdrawals/internal resources：139.277%。
- stress index：1.392771。
- scarcity score/status：1.333454 / critical。

| component | value | interpretation |
|---|---|---|
| physical_stress | 1.392771 | withdrawals/internal renewable resources |
| sanitation_quality_gap | 0.035852 | economic scarcity proxy through sanitation service gap |
| basic_water_access_gap | 0.007139 | clean water access gap |
| economic_capacity_offset | 0.334736 | GDP/capita ability to fund infrastructure |

### 干预计划
- 策略：combine demand reduction, reuse, leakage control, new non-conventional supply, and watershed recharge; avoid relying on one megaproject

| program | annual_cost_musd | annual_withdrawal_reduction_pct_points | annual_quality_gain_pct_points | efficiency_score_per_billion_usd |
|---|---|---|---|---|
| agricultural_efficiency | 120 | 2.4 | 0.2 | 1.388889 |
| leakage_reduction_and_metering | 85 | 1.5 | 0.3 | 1.294118 |
| wastewater_reuse_and_sanitation | 95 | 1.1 | 0.9 | 1.087719 |
| rainwater_harvesting_and_aquifer_recharge | 70 | 0.8 | 0.2 | 0.857143 |
| desalination_and_renewable_energy | 220 | 1.7 | 0.4 | 0.575758 |

## 模型限制
- 这是可复现的官方 PDF + World Bank Data 水资源实验；COMAP 没有提供独立 CSV/XLSX 附件，但题面要求使用水资源数据源分析缺水，本工作流缓存 Jordan World Bank 官方指标。
- 干预效果、成本和年度降压百分点是显式规划假设，不是历史因果估计；正式论文应补充流域水文、月度供水、地下水、漏损、价格和项目成本数据校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2016/E/q04/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2016/E/q04/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2016/E/q04/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2016/E/q04`
