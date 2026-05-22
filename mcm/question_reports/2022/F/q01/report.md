# 2022-F q01：外层空间条约承诺与全球公平定义

## 题目原问
What is global equity, and how might we measure it?

## 适合模型
将 Outer Space Treaty 的 benefit of all countries 原则转为 benefit_sharing、participation、technology_transfer、governance_voice、risk burden、peaceful use 六维公平指标。对应模型：多指标评价、政策指标体系。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025/official_assets/2022/All for One and One (Space) for All!`。
- 行数/记录数：{}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

## 模型限制
- 这是可复现的官方数据基线实验，适合做论文骨架和结果表，不应把随机森林相关性解释为严格因果。
- 对异常国家/代表队名称、教练履历、项目规则变化等，需要在竞赛论文中追加人工核验和敏感性分析。

## 运行方式
`.venv/bin/python mcm/question_solutions/2022/F/q01/solution.py`

## 输出
- `mcm/question_results/2022/F/q01/result.json`
- `mcm/question_reports/2022/F/q01/report.md`
- `mcm/question_artifacts/2022/F/q01`
