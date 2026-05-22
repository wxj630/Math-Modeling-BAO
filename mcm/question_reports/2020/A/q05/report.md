# 2020-A q05：Hook Line and Sinker 杂志文章

## 题目原问
Write an article for Hook Line and Sinker explaining the results for a nontechnical audience.

## 适合模型
把北迁情景、可达性时间、运营策略和领海风险整理成非技术杂志文章。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets`。
- 行数/记录数：{'official_parameters': 4}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

## 模型限制
- 这是可复现的官方题面参数 Moving North 鱼群迁移实验；本地官方 PDF 文字层不完整，题面要求由 COMAP 2020 problems 官方页面核对，归档仍指向本地官方 PDF 资产。
- COMAP 没有提供海温、鱼群调查或船队成本附件，因此 thermal shift、fleet range、territorial threshold 和策略得分均为显式确定性情景输入；正式论文应补充 ICES/NOAA/UK fisheries 海温和渔业观测校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2020/A/q05/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2020/A/q05/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2020/A/q05/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2020/A/q05`
