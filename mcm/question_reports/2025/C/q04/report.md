# 2025-C q04：项目数量、运动类型与国家优势运动

## 题目原问
Consider the number and types of events. Explore relationships between events and medal counts, important sports for countries, and host-selected events.

## 适合模型
把每届项目数、运动数量、运动员参赛规模、参赛项目数作为预测特征，并用 2008-2024 奖牌运动员记录统计各国优势运动占比。

## 数据与真实性
- 数据类型：official_comap_csv。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted/2025/2025_Problem_C_Data.zip/2025_Problem_C_Data`。
- 行数/记录数：{'summerOly_medal_counts.csv': 1435, 'summerOly_athletes.csv': 252565, 'summerOly_hosts.csv': 35, 'summerOly_programs.csv': 74, 'data_dictionary.csv': 50}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

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

### 国家优势运动

| NOC | top_sports |
|---|---|
| United States | Swimming(0.235584); Athletics(0.161744); Basketball(0.084388) |
| Australia | Swimming(0.371859); Hockey(0.085427); Rowing(0.080402) |
| Great Britain | Rowing(0.195349); Athletics(0.128682); Cycling(0.089922) |
| France | Handball(0.189983); Basketball(0.103627); Judo(0.098446) |
| Netherlands | Hockey(0.325967); Rowing(0.209945); Athletics(0.085635) |
| Brazil | Football(0.383838); Volleyball(0.286195); Judo(0.084175) |
| China | Swimming(0.120567); Diving(0.104965); Table Tennis(0.078014) |
| Germany | Hockey(0.157303); Football(0.132959); Rowing(0.104869) |
| Canada | Football(0.192691); Rowing(0.189369); Swimming(0.139535) |
| Spain | Handball(0.183486); Basketball(0.146789); Football(0.134557) |
| Japan | Judo(0.170732); Baseball/Softball(0.095122); Swimming(0.095122) |
| Italy | Fencing(0.198225); Water Polo(0.115385); Volleyball(0.109467) |

## 模型限制
- 这是可复现的官方数据基线实验，适合做论文骨架和结果表，不应把随机森林相关性解释为严格因果。
- 对异常国家/代表队名称、教练履历、项目规则变化等，需要在竞赛论文中追加人工核验和敏感性分析。

## 运行方式
`.venv/bin/python mcm/question_solutions/2025/C/q04/solution.py`

## 输出
- `mcm/question_results/2025/C/q04/result.json`
- `mcm/question_reports/2025/C/q04/report.md`
- `mcm/question_artifacts/2025/C/q04`
