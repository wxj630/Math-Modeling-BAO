# 2016-E q03：15 年无干预水资源预测与居民影响

## 题目原问
In your chosen region, use your model to show what the water situation will be in 15 years. How does this situation impact the lives of citizens? Incorporate environmental drivers' effects.

## 适合模型
用最近人口增长率乘以题面用水增长为人口增长两倍的约束，外推无干预 stress index，并给出居民生活影响。对应模型：趋势外推、需求增长模型、风险阈值分析。

## 数据与真实性
- 数据类型：official_pdf_and_world_bank_csv。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted/2016/Problem Data- Are we heading towards a thirsty planet`。
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

## 模型限制
- 这是可复现的官方 PDF + World Bank Data 水资源实验；COMAP 没有提供独立 CSV/XLSX 附件，但题面要求使用水资源数据源分析缺水，本工作流缓存 Jordan World Bank 官方指标。
- 干预效果、成本和年度降压百分点是显式规划假设，不是历史因果估计；正式论文应补充流域水文、月度供水、地下水、漏损、价格和项目成本数据校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2016/E/q03/solution.py`

## 输出
- `mcm/question_results/2016/E/q03/result.json`
- `mcm/question_reports/2016/E/q03/report.md`
- `mcm/question_artifacts/2016/E/q03`
