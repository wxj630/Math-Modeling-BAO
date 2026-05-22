# 2018-C q06：给四州州长的能源政策备忘录

## 题目原问
Write a concise memo to the Governors of Arizona, California, New Mexico, and Texas explaining the model results and recommending compact actions.

## 适合模型
把四州能源画像、2009 最佳 benchmark、2025/2050 gap 和政策行动翻译为州长可读备忘录。对应模型：非技术决策报告、政策建议、模型结果解释。

## 数据与真实性
- 数据类型：official_comap_xlsx。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2018/Problem Data- Energy Production`。
- 行数/记录数：{'seseds': 105744, 'msncodes': 605}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

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

### Governors memo
To the Governors of Arizona, California, New Mexico, and Texas: the official SEDS workbook shows that the four states start from different energy profiles, so the compact should set a shared renewable-share target while allowing different resource mixes. Use the 2009 best-profile benchmark as the minimum political target, then require each state to close its projected 2025 and 2050 gaps with renewable portfolio standards, transmission/storage cooperation, and demand efficiency.

## 模型限制
- 这是可复现的官方 Energy Production SEDS workbook 实验；只使用 `2018_MCM_Problem_C_Data.xlsx` 的 `seseds` 与 `msncodes` 工作表，不使用随机造数或外部能源观测。
- 2025/2050 结果是题目要求的 no-policy baseline 线性外推，不是未来真实观测；compact target 和政策行动是基于官方历史数据的规划建议，正式论文应补充最新 EIA/州能源政策数据做情景校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2018/C/q06/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2018/C/q06/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2018/C/q06/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2018/C/q06`
