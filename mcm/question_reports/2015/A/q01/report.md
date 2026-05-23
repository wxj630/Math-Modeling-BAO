# 2015-A q01：Ebola 传播、药物生产与配送优化模型

## 题目原问
Build a realistic, sensible, and useful model that considers Ebola spread, medicine demand, feasible delivery systems, delivery locations, manufacturing speed, and other critical factors to optimize eradication or containment.

## 适合模型


## 数据与真实性
- 数据类型：official_html_statement。
- 官方来源：https://www.contest.comap.com/undergraduate/contests/mcm/contests/2015/problems/。
- 本脚本只使用 COMAP 官方网页题面和显式建模假设，不使用随机占位观测。

## 建模与求解报告
- 模型族：一阶动态仿真基线（CH2）。
- baseline score：0.498857。
- 命中关键词：spread, 敏感性。
- 这个 advanced 占位层把 2015 官方 HTML 题面接入教程链路；后续可替换为更细的 SEIR/贝叶斯搜索专用实验。

## 运行方式
`.venv/bin/python mcm/question_solutions/2015/A/q01/solution.py`

## 输出
- `mcm/question_results/2015/A/q01/result.json`
- `mcm/question_reports/2015/A/q01/report.md`
- `mcm/question_artifacts/2015/A/q01`
