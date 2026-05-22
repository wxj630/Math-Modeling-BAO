# 2019-B q05：医疗包载荷、路线与日程

## 题目原问
Provide payload packing configurations, delivery routes and schedule to meet the emergency medical package requirements.

## 适合模型
为每个医院需求行选择最近 staging base 和合适 drone type，计算 round-trip km、sortie minutes 和 morning/midday/afternoon schedule block。对应模型：车辆路径近似、日程调度。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025/official_assets`。
- 行数/记录数：{'official_parameters': 5}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

## 模型限制
- 这是可复现的官方数据基线实验，适合做论文骨架和结果表，不应把随机森林相关性解释为严格因果。
- 对异常国家/代表队名称、教练履历、项目规则变化等，需要在竞赛论文中追加人工核验和敏感性分析。

## 运行方式
`.venv/bin/python mcm/question_solutions/2019/B/q05/solution.py`

## 输出
- `mcm/question_results/2019/B/q05/result.json`
- `mcm/question_reports/2019/B/q05/report.md`
- `mcm/question_artifacts/2019/B/q05`
