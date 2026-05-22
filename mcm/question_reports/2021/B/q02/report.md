# 2021-B q02：未来十年极端火灾概率变化与设备成本

## 题目原问
Illustrate how the model adapts to changing likelihood of extreme fire events over the next decade and project equipment cost increases if drone cost stays constant.

## 适合模型
逐年提高 extreme fire likelihood multiplier，在能力安全分低于阈值时增加 SSA/repeater 无人机，输出十年设备成本投影。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets`。
- 行数/记录数：{'official_parameters': 8}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

## 模型限制
- 这是可复现的官方题面参数野火无人机采购实验；COMAP 没有提供 GIS/事件附件，因此只使用 PDF 中 AUD 10000、30km、20m/s、2.5h、1.75h、5W、10W、20km 等题面参数。
- 火场等级、地形复杂度和年度频率是显式确定性规划情景，不是 CFA 事件库；正式论文应补充火点 GIS、地形遮挡、风烟、飞行管制和人员部署数据校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2021/B/q02/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2021/B/q02/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2021/B/q02/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2021/B/q02`
