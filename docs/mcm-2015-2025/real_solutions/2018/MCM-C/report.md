# 2018 MCM-C Energy Production：官方 SEDS Workbook 实验报告

## 数据真实性

- 官方题面：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2018/Energy Production.pdf`。
- 官方 workbook：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2018/Problem Data- Energy Production/2018_MCM_Problem_C_Data.xlsx`。
- 行数：`{'seseds': 105744, 'msncodes': 605}`。
- 本解法只读取 COMAP 官方 workbook，不生成随机 `x1/x2/x3` 数据。

## Part I：四州能源画像和演化

- 画像年份：2009。
- 最佳 2009 profile：CA，criteria=45% renewable consumption share, 25% non-hydro renewable share, 20% renewable per capita, minus 10% total energy intensity rank.

## Part I-D：2025/2050 无政策预测

- 方法：No-policy baseline linear trend using official 1990-2009 state SEDS shares.

## Part II：Compact targets 与行动

- 目标规则：Set compact targets at least as high as the 2009 best state and above the projected median baseline.

## Governors memo

To the Governors of Arizona, California, New Mexico, and Texas: the official SEDS workbook shows that the four states start from different energy profiles, so the compact should set a shared renewable-share target while allowing different resource mixes. Use the 2009 best-profile benchmark as the minimum political target, then require each state to close its projected 2025 and 2050 gaps with renewable portfolio standards, transmission/storage cooperation, and demand efficiency.
