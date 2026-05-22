# 2022-A q03：天气条件对赛果的敏感性

## 题目原问
Determine the potential impact of weather conditions, including wind directions and wind strengths, to determine how sensitive your results are for small differences in the weather and environment.

## 适合模型
在同一逐段功率计划下枚举顺风、静风和逆风，把风速按赛段暴露系数折算到空气阻力项，输出完赛时间变化。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets`。
- 行数/记录数：{'official_parameters': 5}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

## 模型限制
- 这是可复现的官方题面参数骑行功率实验；COMAP 没有提供功率计、GPS 或天气附件，因此只使用 PDF 中两类骑手、不同性别、东京/弗兰德斯/自定义路线、天气敏感性、功率偏差和六人团队计时赛等题面约束。
- 骑手 profile、赛道分段、CdA、滚阻和风暴露系数是显式确定性场景输入，不是实测遥测；正式论文应补充真实路线 GPX、功率历史、气象预报和车手疲劳校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2022/A/q03/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2022/A/q03/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2022/A/q03/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2022/A/q03`
