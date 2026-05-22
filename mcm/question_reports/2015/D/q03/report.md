# 2015-D q03：20 年计划影响评估与最高性价比政策

## 题目原问
Evaluate the effect your 20-year sustainability plan has on your country's sustainability measure. Determine which programs or policies produce the greatest effect on the sustainability measure for your country.

## 适合模型
把项目年度增益作为显式规划假设累积到各组件分数，计算 20 年后总分、状态变化，并用 score gain per billion USD 排序。对应模型：系统动力学、成本效益分析、项目效率排序。

## 数据与真实性
- 数据类型：official_pdf_and_world_bank_csv。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2015/Problem Data- Is it sustainable`。
- 行数/记录数：{'world_bank_nepal_indicators.csv': 462}。
- 本脚本只使用 COMAP 官方 PDF、题面推荐的 World Bank 官方公共数据和显式规划假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

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
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2015/D/q03/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2015/D/q03/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2015/D/q03/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2015/D/q03`
