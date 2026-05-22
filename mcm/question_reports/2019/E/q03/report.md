# 2019-E q03：环境恶化如何计入项目成本

## 题目原问
How would environmental degradation be accounted for in these project costs?

## 适合模型
对社区道路、郊区住房、总部搬迁、跨国管线和商业水道扩展逐项计算 traditional NPV 与加入生态服务损失后的 true NPV。对应模型：全成本核算、残余生态负债。

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
`.venv/bin/python mcm/question_solutions/2019/E/q03/solution.py`

## 输出
- `mcm/question_results/2019/E/q03/result.json`
- `mcm/question_reports/2019/E/q03/report.md`
- `mcm/question_artifacts/2019/E/q03`
