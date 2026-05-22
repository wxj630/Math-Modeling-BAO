# 2016 ICM-E Are we heading towards a thirsty planet? 官方 PDF + World Bank 实验报告

## 数据来源
- 官方 PDF：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2016/Are we heading towards a thirsty planet.pdf`。
- World Bank 缓存数据：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2016/Problem Data- Are we heading towards a thirsty planet/world_bank_jordan_water_indicators.csv`。
- 选定地区：Jordan，用 World Bank 观测到的 freshwater withdrawals/internal resources 指标体现水资源严重超载。

## Q1 清洁水供给能力模型
- 基线年份：2024。
- 基线 stress index：1.392771。
- 稀缺状态：critical。

## Q2 缺水原因
- 物理稀缺：总取水量超过内部可再生淡水资源。
- 经济稀缺：基础服务覆盖率高但管理、漏损、成本和水质风险仍会限制可靠供水。

## Q3 15 年无干预预测
- 15 年后 stress index：2.614749。
- 居民影响：Without intervention, higher stress implies more intermittent supply, higher water prices, more agricultural constraints, and greater health risk during drought periods.

## Q4 干预计划
- 项目数：5。
- 策略：combine demand reduction, reuse, leakage control, new non-conventional supply, and watershed recharge; avoid relying on one megaproject

## Q5 有干预预测
- 15 年后 stress index：1.489763。
- 相对无干预降低：1.124986。
- 是否降低易受缺水影响：True。

## Q6 模型优缺点
- 优点：观测指标可追溯，区分物理稀缺和经济稀缺，能比较干预路径。
- 局限：World Bank 年度国家级指标不能替代流域/月度水文数据；干预效果是规划假设，不是因果估计。

## 输出文件
- `result.json`：/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/real_solutions/2016/ICM-E/result.json
- `world_bank_water_panel.csv`：/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/real_solutions/2016/ICM-E/artifacts/world_bank_water_panel.csv
- `water_scarcity_components.csv`：/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/real_solutions/2016/ICM-E/artifacts/water_scarcity_components.csv
- `intervention_plan.csv`：/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/real_solutions/2016/ICM-E/artifacts/intervention_plan.csv
- `water_forecast.csv`：/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/real_solutions/2016/ICM-E/artifacts/water_forecast.csv
- `water_stress_projection.png`：/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/real_solutions/2016/ICM-E/artifacts/water_stress_projection.png
