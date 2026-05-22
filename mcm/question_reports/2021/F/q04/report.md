# 2021-F q04：当前状态与拟议健康状态测量

## 题目原问
Use your model to measure the health of both the current system and proposed, healthy, sustainable system for your selected nation.

## 适合模型
在 0-10 年轨迹上计算选定国家当前健康分、最终健康分以及 access、affordability、funding、innovation 等维度变化。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets`。
- 行数/记录数：{'official_parameters': 3}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

## 模型限制
- 这是可复现的官方题面参数高等教育系统健康度实验；COMAP 没有提供国家高教 workbook，因此只使用 PDF 中 system health、sustainable system、多国比较、政策时间线和现实影响等题面约束。
- 国家健康维度分、政策增益和利益相关者影响是显式确定性规划输入，不是 UNESCO/OECD/国家教育财政或就业记录；正式论文应补充学费、债务、完成率、就业、科研、国际学生和财政稳定性数据校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2021/F/q04/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2021/F/q04/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2021/F/q04/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2021/F/q04`
