# 2018-C q02：1960-2009 能源结构演化

## 题目原问
Use the historical data to explain how the four states' energy profiles evolved over time and how their clean renewable energy use changed.

## 适合模型
按州和年份构造 1960-2009 renewable consumption share 历史序列，并对 1990-2009 做每州 OLS 斜率估计，判断 improving/declining 趋势。对应模型：时间序列趋势回归、状态比较、能源转型路径分析。

## 数据与真实性
- 数据类型：official_comap_xlsx。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted/2018/Problem Data- Energy Production`。
- 行数/记录数：{'seseds': 105744, 'msncodes': 605}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 四州能源画像
- 画像年份：2009。
- 评价准则：45% renewable consumption share, 25% non-hydro renewable share, 20% renewable per capita, minus 10% total energy intensity rank.

#### 2009 state profiles

| state | state_name | renewable_consumption_share | renewable_production_share | nonhydro_renewable_share | energy_consumption_per_capita_mmbtu | clean_profile_score |
|---|---|---|---|---|---|---|
| CA | California | 0.089027 | 0.243757 | 0.055027 | 217.024469 | 0.875 |
| NM | New Mexico | 0.05318 | 0.014006 | 0.049233 | 333.826284 | 0.4875 |
| AZ | Arizona | 0.071163 | 0.155118 | 0.028029 | 220.763519 | 0.45 |
| TX | Texas | 0.031568 | 0.025489 | 0.030679 | 456.080488 | 0.1875 |

### 历史演化模型
- 方法：OLS slope on 1990-2009 official renewable consumption share by state.

| state | renewable_share_1960 | renewable_share_2009 | change_1960_2009 | recent_slope_per_year | interpretation |
|---|---|---|---|---|---|
| AZ | 0.127792 | 0.071163 | -0.056629 | -0.002184 | declining |
| CA | 0.07827 | 0.089027 | 0.010757 | -0.000484 | declining |
| NM | 0.022409 | 0.05318 | 0.030771 | 0.001752 | improving |
| TX | 0.011316 | 0.031568 | 0.020252 | 0.000617 | improving |

## 模型限制
- 这是可复现的官方 Energy Production SEDS workbook 实验；只使用 `2018_MCM_Problem_C_Data.xlsx` 的 `seseds` 与 `msncodes` 工作表，不使用随机造数或外部能源观测。
- 2025/2050 结果是题目要求的 no-policy baseline 线性外推，不是未来真实观测；compact target 和政策行动是基于官方历史数据的规划建议，正式论文应补充最新 EIA/州能源政策数据做情景校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2018/C/q02/solution.py`

## 输出
- `mcm/question_results/2018/C/q02/result.json`
- `mcm/question_reports/2018/C/q02/report.md`
- `mcm/question_artifacts/2018/C/q02`
