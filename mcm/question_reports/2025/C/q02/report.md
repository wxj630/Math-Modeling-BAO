# 2025-C q02：2028 洛杉矶奖牌榜预测、进步与退步国家

## 题目原问
Project the 2028 Los Angeles medal table, include prediction intervals, and identify countries likely to improve or do worse than 2024.

## 适合模型
用 2024 国家状态外推到 2028，设置美国东道主变量，比较预测总奖牌与 2024 实际总奖牌。

## 数据与真实性
- 数据类型：official_comap_csv。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2025/2025_Problem_C_Data.zip/2025_Problem_C_Data`。
- 行数/记录数：{'summerOly_medal_counts.csv': 1435, 'summerOly_athletes.csv': 252565, 'summerOly_hosts.csv': 35, 'summerOly_programs.csv': 74, 'data_dictionary.csv': 50}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

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

### 2028 金牌预测 Top 10

| NOC | 2024_gold | pred_2028_gold | interval80 |
|---|---|---|---|
| United States | 40 | 41.089526 | [36.333333, 46.860317] |
| China | 40 | 32.589243 | [23.0, 41.1] |
| France | 16 | 24.923106 | [14.0, 36.516667] |
| Australia | 18 | 23.25275 | [7.191667, 41.0] |
| Germany | 12 | 21.23934 | [8.655556, 37.0] |
| Great Britain | 14 | 14.826892 | [4.0, 24.0] |
| Italy | 12 | 13.932317 | [7.49, 23.7] |
| Japan | 20 | 13.697753 | [4.0, 25.871429] |
| Netherlands | 15 | 10.024259 | [7.2, 13.0] |
| Canada | 9 | 9.922688 | [5.666667, 15.5] |

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

### 最可能退步

| NOC | actual_2024_total | pred_2028_total | change |
|---|---|---|---|
| Great Britain | 65 | 45.577937 | -19.422063 |
| United States | 126 | 107.51955 | -18.48045 |
| Japan | 45 | 33.888143 | -11.111857 |
| South Korea | 32 | 22.864341 | -9.135659 |
| Australia | 53 | 45.329872 | -7.670128 |
| China | 91 | 84.470517 | -6.529483 |
| France | 64 | 58.873614 | -5.126386 |
| Kyrgyzstan | 6 | 2.536803 | -3.463197 |
| Uzbekistan | 13 | 9.610442 | -3.389558 |
| Netherlands | 34 | 31.375702 | -2.624298 |

## 模型限制
- 这是可复现的官方数据基线实验，适合做论文骨架和结果表，不应把随机森林相关性解释为严格因果。
- 对异常国家/代表队名称、教练履历、项目规则变化等，需要在竞赛论文中追加人工核验和敏感性分析。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2025/C/q02/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2025/C/q02/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2025/C/q02/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2025/C/q02`
