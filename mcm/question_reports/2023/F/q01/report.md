# 2023-F q01：奥运会举办影响指标框架

## 题目原问
Build metrics for the impacts of hosting the games from economic, land use, human satisfaction, travel, opportunity for future improvements, host city/nation prestige, and other criteria.

## 适合模型
把官方题面列出的经济、土地利用、人类满意度、旅行、未来改进、主办声望和体育团结转成 7 维权重指标，并写入可审计 metric framework。对应模型：多指标评价、权重评分、政策指标体系。

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
`.venv/bin/python mcm/question_solutions/2023/F/q01/solution.py`

## 输出
- `mcm/question_results/2023/F/q01/result.json`
- `mcm/question_reports/2023/F/q01/report.md`
- `mcm/question_artifacts/2023/F/q01`
