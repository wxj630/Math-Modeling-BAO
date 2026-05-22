# 2021-F q02：多国应用与待改进国家选择

## 题目原问
Apply your model to several countries, and then select a nation whose system of higher education has room for improvement based on your analysis.

## 适合模型
把同一健康度模型应用到 Germany、United States、Japan、Australia 和 Brazil，按 current score、room for improvement 和 weakest dimension 选择转型对象。

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
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2021/F/q02/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2021/F/q02/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2021/F/q02/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2021/F/q02`
