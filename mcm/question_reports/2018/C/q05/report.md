# 2018-C q05：四州能源 compact 目标与行动

## 题目原问
Develop a plan for an interstate compact among the four states that moves the region toward cleaner renewable energy. Identify target values and practical actions.

## 适合模型
以 2009 最佳州 benchmark 和 2025/2050 基线中位水平设置 compact target，计算各州 gap，并提出可交易清洁能源信用、跨州输电储能、需求侧效率三类行动。对应模型：目标规划、差距分析、多主体政策组合。

## 数据与真实性
- 数据类型：official_comap_xlsx。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted/2018/Problem Data- Energy Production`。
- 行数/记录数：{'seseds': 105744, 'msncodes': 605}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 2009 最佳能源画像
- 最佳州：CA（California）。
- renewable consumption share：0.089027。
- non-hydro renewable share：0.055027。
- clean profile score：0.875。

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

### Interstate Compact 目标
- 目标规则：Set compact targets at least as high as the 2009 best state and above the projected median baseline.

| state | year | baseline_renewable_share | compact_target_share | required_gap |
|---|---|---|---|---|
| AZ | 2025 | 0.025953 | 0.089027 | 0.063074 |
| CA | 2025 | 0.082612 | 0.089027 | 0.006415 |
| NM | 2025 | 0.067057 | 0.089027 | 0.02197 |
| TX | 2025 | 0.029067 | 0.089027 | 0.05996 |
| AZ | 2050 | 0.0 | 0.137493 | 0.137493 |
| CA | 2050 | 0.070503 | 0.137493 | 0.06699 |
| NM | 2050 | 0.110853 | 0.137493 | 0.02664 |
| TX | 2050 | 0.044482 | 0.137493 | 0.093011 |

### Compact 行动建议
- 行动：Create a four-state renewable portfolio standard with tradable clean-energy credits.
- 模型依据：Raises renewable_consumption_share toward the compact target while allowing state-specific resource mixes.
- 行动：Build transmission and storage projects that connect Texas wind, California solar, and Arizona/New Mexico solar resources.
- 模型依据：Addresses geography differences visible in the official state profiles and reduces curtailment risk.
- 行动：Pair demand efficiency with electrification so total energy per capita falls while renewable electricity grows.
- 模型依据：Targets energy_consumption_per_capita_mmbtu as well as renewable share.

## 模型限制
- 这是可复现的官方 Energy Production SEDS workbook 实验；只使用 `2018_MCM_Problem_C_Data.xlsx` 的 `seseds` 与 `msncodes` 工作表，不使用随机造数或外部能源观测。
- 2025/2050 结果是题目要求的 no-policy baseline 线性外推，不是未来真实观测；compact target 和政策行动是基于官方历史数据的规划建议，正式论文应补充最新 EIA/州能源政策数据做情景校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2018/C/q05/solution.py`

## 输出
- `mcm/question_results/2018/C/q05/result.json`
- `mcm/question_reports/2018/C/q05/report.md`
- `mcm/question_artifacts/2018/C/q05`
