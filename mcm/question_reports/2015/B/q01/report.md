# 2015-B q01：失联飞机开放水域搜索规划模型

## 题目原问
Build a generic mathematical model to assist searchers in planning an open-water search for a lost plane flying from Point A to Point B with no signal from the downed plane.

## 适合模型


## 数据与真实性
- 数据类型：official_html_statement。
- 官方来源：https://www.contest.comap.com/undergraduate/contests/mcm/contests/2015/problems/。
- 本脚本只使用 COMAP 官方网页题面和显式建模假设，不使用随机占位观测。

## 建模与求解报告
- 模型族：网络路径基线（CH4）。
- baseline score：0.432143。
- 命中关键词：路径。
- 这个 advanced 占位层把 2015 官方 HTML 题面接入教程链路；后续可替换为更细的 SEIR/贝叶斯搜索专用实验。

## 运行方式
`.venv/bin/python mcm/question_solutions/2015/B/q01/solution.py`

## 输出
- `mcm/question_results/2015/B/q01/result.json`
- `mcm/question_reports/2015/B/q01/report.md`
- `mcm/question_artifacts/2015/B/q01`
