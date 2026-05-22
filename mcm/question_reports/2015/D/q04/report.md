# 2015-D q04：20 页报告、模型优缺点与 ICM 投资建议

## 题目原问
Write a 20-page report that explains your model, sustainability measure, sustainable development plan, and the effect of your plan based on the model and country's environment. Detail the strengths and weaknesses of the model.

## 适合模型
把官方题面、World Bank 数据、指数定义、20 年计划、项目效率排序和模型限制整理为 ICM 可读报告，强调项目效果不是因果估计。对应模型：实验报告、政策备忘录、模型限制说明。

## 数据与真实性
- 数据类型：official_pdf_and_world_bank_csv。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted/2015/Problem Data- Is it sustainable`。
- 行数/记录数：{'world_bank_nepal_indicators.csv': 462}。
- 本脚本只使用 COMAP 官方 PDF、题面推荐的 World Bank 官方公共数据和显式规划假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 国家可持续性评价模型
- 定义：Weighted country sustainability score over needs and limits: water, sanitation, energy, livelihoods, poverty, environment, and population pressure.
- 基线年份：2024。
- 基线得分：0.771044。
- 基线状态：sustainable。
- 阈值规则：score >= 0.70 sustainable; 0.50-0.70 transitional; <0.50 unsustainable

| component | indicator_id | latest_year | latest_value | weight | score | weighted_score | trend_per_year_raw |
|---|---|---|---|---|---|---|---|
| water_access | SH.H2O.BASW.ZS | 2024 | 93.640125 | 0.17 | 0.936401 | 0.159188 | 0.548603 |
| sanitation_access | SH.STA.BASS.ZS | 2024 | 86.025981 | 0.15 | 0.86026 | 0.129039 | 3.283491 |
| energy_access | EG.ELC.ACCS.ZS | 2023 | 94.0 | 0.15 | 0.94 | 0.141 | 1.011111 |
| livelihood | NY.GDP.PCAP.KD | 2024 | 1179.812728 | 0.16 | 0.393271 | 0.062923 | 33.807677 |
| poverty_reduction | SI.POV.DDAY | 2022 | 2.4 | 0.17 | 0.976 | 0.16592 | -2.121053 |
| environment_health | AG.LND.FRST.ZS | 2023 | 41.590722 | 0.12 | 0.415907 | 0.049909 | 0.0 |
| population_pressure | SP.POP.TOTL | 2024 | 29651054.0 | 0.08 | 0.788315 | 0.063065 | 203047.222222 |

### 20 年可持续发展计划
- 选定国家：Nepal。
- 规划期：20 年。
- 策略：Prioritize infrastructure that jointly improves basic needs and ecological limits, then rank programs by score gain per billion USD.

| program | annual_cost_billion_usd | twenty_year_cost_billion_usd | estimated_score_gain | score_gain_per_billion_usd |
|---|---|---|---|---|
| clean_water_and_sanitation | 0.18 | 3.6 | 0.035173 | 0.00977 |
| distributed_clean_energy | 0.14 | 2.8 | 0.0242 | 0.008643 |
| forest_and_disaster_risk_management | 0.1 | 2.0 | 0.0146 | 0.0073 |
| education_and_livelihoods | 0.2 | 4.0 | 0.02488 | 0.00622 |
| climate_resilient_agriculture | 0.16 | 3.2 | 0.01848 | 0.005775 |

### 计划影响评估
- 20 年后得分：0.877497。
- 得分增益：0.106453。
- 20 年后状态：sustainable。
- 说明：Projection applies transparent program-effect assumptions to cached World Bank baseline indicators; it is a planning experiment, not a causal forecast.

| component | score_after_20_years | weighted_score_after |
|---|---|---|
| water_access | 1.0 | 0.17 |
| sanitation_access | 1.0 | 0.15 |
| energy_access | 1.0 | 0.15 |
| livelihood | 0.653271 | 0.104523 |
| poverty_reduction | 1.0 | 0.17 |
| environment_health | 0.555907 | 0.066709 |
| population_pressure | 0.828315 | 0.066265 |

### 最高性价比政策
- 排序方法：estimated 20-year sustainability score gain per billion USD
- 最高性价比项目：clean_water_and_sanitation。
- 单位预算得分增益：0.00977。

## 模型限制
- 这是可复现的官方 PDF + World Bank Data 实验；COMAP 没有提供独立 CSV/XLSX 附件，但题面明确列出 World Bank Data 作为可能资源，因此本工作流缓存 Nepal 官方 World Bank API 指标。
- 项目成本和干预效果是显式规划假设，不是历史因果估计；正式论文应补充本地项目成本、气候灾害、治理稳定性、区域贫困和更多国家对比数据校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2015/D/q04/solution.py`

## 输出
- `mcm/question_results/2015/D/q04/result.json`
- `mcm/question_reports/2015/D/q04/report.md`
- `mcm/question_artifacts/2015/D/q04`
