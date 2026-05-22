# 2019-A q04：不同援助水平下的人类社区规模

## 题目原问
How large a community is necessary to support a dragon for varying levels of assistance that can be provided to the dragons?

## 适合模型
扫描 0%、25%、50%、75% 人类供食份额，把猎物 kg/day 转换为牧养家庭和专业 handler 需求。对应模型：资源供给规划、社区承载能力。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025/official_assets`。
- 行数/记录数：{'official_parameters': 4}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

## 模型限制
- 这是可复现的官方数据基线实验，适合做论文骨架和结果表，不应把随机森林相关性解释为严格因果。
- 对异常国家/代表队名称、教练履历、项目规则变化等，需要在竞赛论文中追加人工核验和敏感性分析。

## 运行方式
`.venv/bin/python mcm/question_solutions/2019/A/q04/solution.py`

## 输出
- `mcm/question_results/2019/A/q04/result.json`
- `mcm/question_reports/2019/A/q04/report.md`
- `mcm/question_artifacts/2019/A/q04`
