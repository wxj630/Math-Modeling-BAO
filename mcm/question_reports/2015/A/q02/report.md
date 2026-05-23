# 2015-A q02：世界医学协会非技术公告信

## 题目原问
Prepare a 1-2 page non-technical letter for the world medical association to use in their announcement.

## 适合模型


## 数据与真实性
- 数据类型：official_html_statement。
- 官方来源：https://www.contest.comap.com/undergraduate/contests/mcm/contests/2015/problems/。
- 本脚本只使用 COMAP 官方网页题面和显式建模假设，不使用随机占位观测。

## 建模与求解报告
- 模型族：报告提纲基线（CH0）。
- baseline score：0.486143。
- 命中关键词：letter, 备忘录。
- 这个 advanced 占位层把 2015 官方 HTML 题面接入教程链路；后续可替换为更细的 SEIR/贝叶斯搜索专用实验。

## 运行方式
`.venv/bin/python mcm/question_solutions/2015/A/q02/solution.py`

## 输出
- `mcm/question_results/2015/A/q02/result.json`
- `mcm/question_reports/2015/A/q02/report.md`
- `mcm/question_artifacts/2015/A/q02`
