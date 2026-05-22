# 2019-P06 q01：全球去中心化数字金融可行性模型

## 题目原问
Construct a model that represents a global decentralized digital financial system and identifies key factors that limit or facilitate growth, access, security, and stability.

## 适合模型
把题面 growth、access、security、stability 拆成国家原型的 unbanked share、digital access、regulatory trust、currency instability 和 illicit flow risk，计算 adoption viability。对应模型：多指标综合评价、政策可行性评分。

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
`.venv/bin/python mcm/question_solutions/2019/P06/q01/solution.py`

## 输出
- `mcm/question_results/2019/P06/q01/result.json`
- `mcm/question_reports/2019/P06/q01/report.md`
- `mcm/question_artifacts/2019/P06/q01`
