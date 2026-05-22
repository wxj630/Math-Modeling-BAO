# 2025-C q03：尚未获奖国家的首枚奖牌概率

## 题目原问
Include countries that have yet to earn medals and project how many will earn their first medal in the next Olympics, with odds/confidence.

## 适合模型
将有参赛记录但历史总奖牌为 0 的国家纳入候选，用随机森林树预测分布估计 P(total >= 0.5)，再求期望数量。

## 数据与真实性
- 数据类型：official_comap_csv。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted/2025/2025_Problem_C_Data.zip/2025_Problem_C_Data`。
- 行数/记录数：{'summerOly_medal_counts.csv': 1435, 'summerOly_athletes.csv': 252565, 'summerOly_hosts.csv': 35, 'summerOly_programs.csv': 74, 'data_dictionary.csv': 50}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告
- 首枚奖牌国家数量期望：11.366667。
- 解释：该值是所有未曾获奖但有参赛记录国家的 `P(total>=0.5)` 概率和，不是简单四舍五入的确定数量。

## 模型限制
- 这是可复现的官方数据基线实验，适合做论文骨架和结果表，不应把随机森林相关性解释为严格因果。
- 对异常国家/代表队名称、教练履历、项目规则变化等，需要在竞赛论文中追加人工核验和敏感性分析。

## 运行方式
`.venv/bin/python mcm/question_solutions/2025/C/q03/solution.py`

## 输出
- `mcm/question_results/2025/C/q03/result.json`
- `mcm/question_reports/2025/C/q03/report.md`
- `mcm/question_artifacts/2025/C/q03`
