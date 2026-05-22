# 2018-C q04：无政策变化下 2025/2050 基线预测

## 题目原问
Predict the energy profiles of the four states in 2025 and 2050 if no policy changes are made.

## 适合模型
使用官方 1990-2009 SEDS renewable share 与 per-capita energy 线性趋势外推 2025、2050，明确这是 no-policy baseline 而不是未来观测数据。对应模型：线性趋势预测、基线情景、外推不确定性说明。

## 数据与真实性
- 数据类型：official_comap_xlsx。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted/2018/Problem Data- Energy Production`。
- 行数/记录数：{'seseds': 105744, 'msncodes': 605}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 历史演化模型
- 方法：OLS slope on 1990-2009 official renewable consumption share by state.

| state | renewable_share_1960 | renewable_share_2009 | change_1960_2009 | recent_slope_per_year | interpretation |
|---|---|---|---|---|---|
| AZ | 0.127792 | 0.071163 | -0.056629 | -0.002184 | declining |
| CA | 0.07827 | 0.089027 | 0.010757 | -0.000484 | declining |
| NM | 0.022409 | 0.05318 | 0.030771 | 0.001752 | improving |
| TX | 0.011316 | 0.031568 | 0.020252 | 0.000617 | improving |

### 2025/2050 无政策基线预测
- 方法：No-policy baseline linear trend using official 1990-2009 state SEDS shares.

| state | year | baseline_renewable_consumption_share | baseline_energy_consumption_per_capita_mmbtu | model |
|---|---|---|---|---|
| AZ | 2025 | 0.025953 | 227.914234 | linear trend fit on 1990-2009 official SEDS variables |
| AZ | 2050 | 0.0 | 207.945397 | linear trend fit on 1990-2009 official SEDS variables |
| CA | 2025 | 0.082612 | 215.105021 | linear trend fit on 1990-2009 official SEDS variables |
| CA | 2050 | 0.070503 | 196.736156 | linear trend fit on 1990-2009 official SEDS variables |
| NM | 2025 | 0.067057 | 324.979615 | linear trend fit on 1990-2009 official SEDS variables |
| NM | 2050 | 0.110853 | 290.162626 | linear trend fit on 1990-2009 official SEDS variables |
| TX | 2025 | 0.029067 | 418.008429 | linear trend fit on 1990-2009 official SEDS variables |
| TX | 2050 | 0.044482 | 288.613201 | linear trend fit on 1990-2009 official SEDS variables |

## 模型限制
- 这是可复现的官方 Energy Production SEDS workbook 实验；只使用 `2018_MCM_Problem_C_Data.xlsx` 的 `seseds` 与 `msncodes` 工作表，不使用随机造数或外部能源观测。
- 2025/2050 结果是题目要求的 no-policy baseline 线性外推，不是未来真实观测；compact target 和政策行动是基于官方历史数据的规划建议，正式论文应补充最新 EIA/州能源政策数据做情景校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2018/C/q04/solution.py`

## 输出
- `mcm/question_results/2018/C/q04/result.json`
- `mcm/question_reports/2018/C/q04/report.md`
- `mcm/question_artifacts/2018/C/q04`
