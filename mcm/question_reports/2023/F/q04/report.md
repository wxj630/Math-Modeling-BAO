# 2023-F q04：写给 IOC 的一页政策备忘录

## 题目原问
Write a one-page memorandum to the IOC describing your strategy and policy recommendations.

## 适合模型
把指标框架、策略评分、推荐路线、永久举办地/四季分拆的备选价值和下一步治理动作压缩成 IOC 可读备忘录。对应模型：非技术政策报告、执行摘要。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted/2023`。
- 行数/记录数：{}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

## 模型限制
- 这是可复现的官方数据基线实验，适合做论文骨架和结果表，不应把随机森林相关性解释为严格因果。
- 对异常国家/代表队名称、教练履历、项目规则变化等，需要在竞赛论文中追加人工核验和敏感性分析。

## 运行方式
`.venv/bin/python mcm/question_solutions/2023/F/q04/solution.py`

## 输出
- `mcm/question_results/2023/F/q04/result.json`
- `mcm/question_reports/2023/F/q04/report.md`
- `mcm/question_artifacts/2023/F/q04`
