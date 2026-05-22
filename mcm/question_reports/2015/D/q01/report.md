# 2015-D q01：国家可持续性评价模型

## 题目原问
Develop a model for the sustainability of a country. This model should provide a measure to distinguish more sustainable countries and policies from less sustainable ones, and clearly define when and how a country is sustainable or unsustainable.

## 适合模型
使用 COMAP 官方 PDF 和题面推荐的 World Bank Data，读取 Nepal 的人口、GDP/人、极端贫困、清洁水、用电、森林、卫生设施等缓存指标，构造 0-1 加权可持续性指数。对应模型：多指标综合评价、可持续发展指标、阈值分类。

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

## 模型限制
- 这是可复现的官方 PDF + World Bank Data 实验；COMAP 没有提供独立 CSV/XLSX 附件，但题面明确列出 World Bank Data 作为可能资源，因此本工作流缓存 Nepal 官方 World Bank API 指标。
- 项目成本和干预效果是显式规划假设，不是历史因果估计；正式论文应补充本地项目成本、气候灾害、治理稳定性、区域贫困和更多国家对比数据校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2015/D/q01/solution.py`

## 输出
- `mcm/question_results/2015/D/q01/result.json`
- `mcm/question_reports/2015/D/q01/report.md`
- `mcm/question_artifacts/2015/D/q01`
