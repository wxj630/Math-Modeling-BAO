# 2018-F q10：Gain from privacy and loss from keeping data private

## 题目原问
Assess the potential gain from keeping data private and what is lost by doing so.

## 适合模型
Balance risk, public-good value, and commercial value in the pricing system.

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets`。
- 行数/记录数：{'official_parameters': 3}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

## 模型限制
- 这是可复现的官方数据基线实验，适合做论文骨架和结果表，不应把随机森林相关性解释为严格因果。
- 对异常国家/代表队名称、教练履历、项目规则变化等，需要在竞赛论文中追加人工核验和敏感性分析。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2018/F/q10/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2018/F/q10/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2018/F/q10/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2018/F/q10`
