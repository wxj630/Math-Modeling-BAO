# 2025-C q06：原创洞察与国家奥委会决策含义

## 题目原问
Identify original insights about Olympic medal counts and explain how they inform national Olympic committees.

## 适合模型
综合模型特征、2028 预测变化、优势运动集中度和候选教练效应，形成面向奥委会的资源配置解释。

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

### 2028 总奖牌预测 Top 10

| NOC | 2024 | pred_2028_total | interval80 |
|---|---|---|---|
| United States | 126 | 107.51955 | [95.971429, 117.075] |
| China | 91 | 84.470517 | [66.14, 100.68] |
| France | 64 | 58.873614 | [45.9, 83.775] |
| Great Britain | 65 | 45.577937 | [17.5, 63.342857] |
| Australia | 53 | 45.329872 | [18.5, 73.05] |
| Germany | 33 | 43.744927 | [22.9, 69.0] |
| Italy | 40 | 42.052496 | [22.0, 58.0] |
| Japan | 45 | 33.888143 | [12.333333, 62.0] |
| Canada | 27 | 31.658298 | [22.0, 43.82] |
| Netherlands | 34 | 31.375702 | [21.9, 44.033333] |

### 最可能进步

| NOC | actual_2024_total | pred_2028_total | change |
|---|---|---|---|
| Refugee Olympic Team | 1 | 23.902372 | 22.902372 |
| Ivory Coast | 1 | 23.531737 | 22.531737 |
| Germany | 33 | 43.744927 | 10.744927 |
| Korea | 0 | 10.298167 | 10.298167 |
| Moldova | 4 | 14.105338 | 10.105338 |
| Czechia | 0 | 7.76505 | 7.76505 |
| Hong Kong | 4 | 10.07823 | 6.07823 |
| Czech Republic | 5 | 10.550329 | 5.550329 |
| Türkiye | 0 | 5.28202 | 5.28202 |
| Spain | 18 | 23.170459 | 5.170459 |

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

### 伟大教练效应候选

| NOC | Sport | Year | medal_rows | jump_vs_recent_mean |
|---|---|---|---|---|
| United States | Baseball/Softball | 2020 | 39 | 39.0 |
| Japan | Baseball/Softball | 2020 | 39 | 39.0 |
| Australia | Swimming | 2000 | 46 | 33.666667 |
| Great Britain | Athletics | 2024 | 40 | 28.333333 |
| Russia | Water Polo | 2000 | 25 | 25.0 |
| China | Swimming | 2024 | 36 | 24.333333 |
| South Korea | Baseball | 2000 | 24 | 24.0 |
| Dominican Republic | Baseball/Softball | 2020 | 24 | 24.0 |
| Serbia | Basketball | 2016 | 24 | 24.0 |
| Russia | Volleyball | 2000 | 24 | 24.0 |
| Australia | Baseball | 2004 | 24 | 24.0 |
| Poland | Athletics | 2020 | 23 | 20.666667 |

### 投资建议
- United States：优先核验并投资 `Baseball/Softball` 高水平教练团队；以异常跃升量 `39.0` 作为上限型增益参考。
- Japan：优先核验并投资 `Baseball/Softball` 高水平教练团队；以异常跃升量 `39.0` 作为上限型增益参考。
- Australia：优先核验并投资 `Swimming` 高水平教练团队；以异常跃升量 `33.666667` 作为上限型增益参考。
- 将候选表中 `jump_vs_recent_mean` 高、且国家已有基础参赛规模的运动作为优先人工核验对象。
- 该数据只能识别异常跃升，不能单独证明教练因果效应；正式论文应补充教练履历时间线作为外部解释。

## 模型限制
- 这是可复现的官方数据基线实验，适合做论文骨架和结果表，不应把随机森林相关性解释为严格因果。
- 对异常国家/代表队名称、教练履历、项目规则变化等，需要在竞赛论文中追加人工核验和敏感性分析。

## 运行方式
`.venv/bin/python mcm/question_solutions/2025/C/q06/solution.py`

## 输出
- `mcm/question_results/2025/C/q06/result.json`
- `mcm/question_reports/2025/C/q06/report.md`
- `mcm/question_artifacts/2025/C/q06`
