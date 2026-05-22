# 2022-A q01：两类骑手与不同性别的功率 profile

## 题目原问
Define the power profiles of two types of riders. One rider should be a time trial specialist and the other a different type. Consider profiles of riders of different genders.

## 适合模型
用 critical-power + W prime 曲线定义 time trial specialist 与 climber-puncheur，并给出男女 profile、CdA、质量和能量预算。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025/official_assets`。
- 行数/记录数：{'official_parameters': 5}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

## 模型限制
- 这是可复现的官方题面参数骑行功率实验；COMAP 没有提供功率计、GPS 或天气附件，因此只使用 PDF 中两类骑手、不同性别、东京/弗兰德斯/自定义路线、天气敏感性、功率偏差和六人团队计时赛等题面约束。
- 骑手 profile、赛道分段、CdA、滚阻和风暴露系数是显式确定性场景输入，不是实测遥测；正式论文应补充真实路线 GPX、功率历史、气象预报和车手疲劳校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2022/A/q01/solution.py`

## 输出
- `mcm/question_results/2022/A/q01/result.json`
- `mcm/question_reports/2022/A/q01/report.md`
- `mcm/question_artifacts/2022/A/q01`
