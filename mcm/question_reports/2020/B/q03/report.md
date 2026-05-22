# 2020-B q03：降雨下的形状稳健性

## 题目原问
Adjust your model as needed to determine how the best 3-dimensional sandcastle foundation is affected by rain, and whether it remains best when it is raining.

## 适合模型
把 light shower、steady rain、heavy burst 作为额外径流负荷施加到 erosion index，比较推荐形状与备选低矮形状在雨中的寿命。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025/official_assets`。
- 行数/记录数：{'official_parameters': 5}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

## 模型限制
- 这是可复现的官方题面参数沙堡基础形状实验；COMAP 没有提供波浪水槽、粒径或潮位附件，因此只使用 PDF 中同海滩、同沙量、同水沙比例、降雨和杂志文章等题面约束。
- 形状、比例、降雨和策略参数是显式确定性物理情景输入，不是实测冲刷数据；正式论文应补充沙粒级配、含水率、压实度、潮汐、波速和降雨入渗校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2020/B/q03/solution.py`

## 输出
- `mcm/question_results/2020/B/q03/result.json`
- `mcm/question_reports/2020/B/q03/report.md`
- `mcm/question_artifacts/2020/B/q03`
