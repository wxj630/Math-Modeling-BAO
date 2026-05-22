# 2015 ICM-D Is it sustainable? 官方 PDF + World Bank 实验报告

## 数据来源
- COMAP 官方 PDF：`docs/mcm-2015-2025/official_assets_extracted/2015/Is it sustainable.pdf`。
- World Bank 缓存数据：`docs/mcm-2015-2025/official_assets_extracted/2015/Problem Data- Is it sustainable/world_bank_nepal_indicators.csv`。
- 选定 LDC 示例：Nepal。题面要求从 48 个 LDC 中选择一个国家；本实验选择 Nepal，并只把缓存 World Bank API 指标作为观测值。
- 没有观测到的指标不补造；项目影响系数在 `assumption_audit` 中标为规划假设。

## Q1 国家可持续性模型
- 基线年份：2024。
- 基线得分：0.771044，状态：sustainable。
- 指标维度：清洁水、卫生设施、能源、收入/生计、贫困、森林环境、人口压力。

## Q2 20 年可持续发展计划
- 规划期：20 年。
- 项目数：5。
- 效率最高项目：clean_water_and_sanitation，单位预算增益：0.00977。

## Q3 计划影响评估
- 20 年后得分：0.877497。
- 得分增益：0.106453。
- 20 年后状态：sustainable。

## Q4 模型优缺点
- 优点：指标透明、数据可追溯、项目效率可排序，适合 ICM 对不同干预做初筛。
- 局限：World Bank 年度指标粒度较粗，项目效应不是因果估计；正式论文应补充本地项目成本、气候灾害、治理稳定性和微观贫困数据。

## 输出文件
- `result.json`：docs/mcm-2015-2025/real_solutions/2015/ICM-D/result.json
- `world_bank_indicator_panel.csv`：docs/mcm-2015-2025/real_solutions/2015/ICM-D/artifacts/world_bank_indicator_panel.csv
- `sustainability_index_components.csv`：docs/mcm-2015-2025/real_solutions/2015/ICM-D/artifacts/sustainability_index_components.csv
- `development_plan.csv`：docs/mcm-2015-2025/real_solutions/2015/ICM-D/artifacts/development_plan.csv
- `policy_efficiency.csv`：docs/mcm-2015-2025/real_solutions/2015/ICM-D/artifacts/policy_efficiency.csv
- `sustainability_projection.png`：docs/mcm-2015-2025/real_solutions/2015/ICM-D/artifacts/sustainability_projection.png
