# 2020-B q04：延长沙堡寿命的其他策略

## 题目原问
What other strategies, if any, might you use to make your sandcastle last longer?

## 适合模型
只列不引入未授权支撑材料的策略：波向布置、牺牲裙边、薄层压实、排水沟和轻微提高位置，并给出寿命倍率。

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
`.venv/bin/python mcm/question_solutions/2020/B/q04/solution.py`

## 输出
- `mcm/question_results/2020/B/q04/result.json`
- `mcm/question_reports/2020/B/q04/report.md`
- `mcm/question_artifacts/2020/B/q04`
