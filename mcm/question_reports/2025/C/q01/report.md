# 2025-C q01：奖牌数模型、精度与不确定性

## 题目原问
Develop a model for medal counts for each country, for Gold and total medals at a minimum. Include uncertainty/precision estimates and model performance measures.

## 适合模型
特征工程 + 随机森林回归 + 2024 留出检验 + 树分布 80% 预测区间。

## 数据与真实性
- 数据类型：official_comap_csv。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted/2025/2025_Problem_C_Data.zip/2025_Problem_C_Data`。
- 行数/记录数：{'summerOly_medal_counts.csv': 1435, 'summerOly_athletes.csv': 252565, 'summerOly_hosts.csv': 35, 'summerOly_programs.csv': 74, 'data_dictionary.csv': 50}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告
- 训练集：1988-2020 年夏奥国家奖牌与参赛特征。
- 留出检验：2024 年巴黎奥运会。
- 输出目标：Gold 与 Total 两个回归目标。
- Gold MAE/RMSE：0.782524 / 1.760735。
- Total MAE/RMSE：1.709571 / 4.031028。

### 特征变量

- `prev_gold`
- `prev_total`
- `rolling_gold_3`
- `rolling_total_3`
- `is_host`
- `athlete_count`
- `entered_sports`
- `entered_events`
- `event_count`
- `sport_count`

## 模型限制
- 这是可复现的官方数据基线实验，适合做论文骨架和结果表，不应把随机森林相关性解释为严格因果。
- 对异常国家/代表队名称、教练履历、项目规则变化等，需要在竞赛论文中追加人工核验和敏感性分析。

## 运行方式
`.venv/bin/python mcm/question_solutions/2025/C/q01/solution.py`

## 输出
- `mcm/question_results/2025/C/q01/result.json`
- `mcm/question_reports/2025/C/q01/report.md`
- `mcm/question_artifacts/2025/C/q01`
