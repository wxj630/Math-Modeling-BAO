# 2020-F q01：环境迁移人口规模和文化风险

## 题目原问
Analyze the scope of the EDP issue in terms of population at risk and risk of loss of culture.

## 适合模型
对 Maldives、Tuvalu、Kiribati 和 Marshall Islands 在 managed/middle/high sea-level scenarios 下投影 80 年 population at risk，并计算 culture loss risk。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets`。
- 行数/记录数：{'official_parameters': 4}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

## 模型限制
- 这是可复现的官方题面参数气候迁移与文化保护实验；COMAP 没有提供岛屿高程、人口或迁移附件，因此只使用 PDF 中 Maldives、Tuvalu、Kiribati、Marshall Islands、EDP、人权、文化保护和 UN 响应等题面约束。
- 海平面、人口、文化风险和政策得分是显式确定性情景输入，不是 IPCC/UNHCR/国家人口普查或社区文化档案；正式论文应补充地理、人口、法律、主权和社区主导文化数据校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2020/F/q01/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2020/F/q01/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2020/F/q01/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2020/F/q01`
