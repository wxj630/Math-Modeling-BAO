# 2020-B q02：无添加材料的最佳水沙比例

## 题目原问
Using your model, determine an optimal sand-to-water mixture proportion for the castle foundation, assuming you use no other additives or materials.

## 适合模型
扫描 6%-22% water fraction，把 capillary cohesion、drainage 和 slump risk 映射到 lifetime multiplier，选择同一推荐形状下寿命最长的比例。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets`。
- 行数/记录数：{'official_parameters': 5}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

## 模型限制
- 这是可复现的官方题面参数沙堡基础形状实验；COMAP 没有提供波浪水槽、粒径或潮位附件，因此只使用 PDF 中同海滩、同沙量、同水沙比例、降雨和杂志文章等题面约束。
- 形状、比例、降雨和策略参数是显式确定性物理情景输入，不是实测冲刷数据；正式论文应补充沙粒级配、含水率、压实度、潮汐、波速和降雨入渗校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2020/B/q02/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2020/B/q02/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2020/B/q02/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2020/B/q02`
