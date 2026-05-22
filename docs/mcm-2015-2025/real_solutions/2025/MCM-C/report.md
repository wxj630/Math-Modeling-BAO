# 2025 MCM-C Models for Olympic Medal Tables 真实数据解法

## 数据来源
- 使用 COMAP 官方 `2025_Problem_C_Data.zip` 解压出的 5 个 CSV。
- 未使用随机生成的 `x1/x2/x3` 数据。

## 每问建模与求解
- 奖牌榜预测：以 1988-2020 为训练集，2024 为留出检验；特征包括上一届奖牌、近三届滚动均值、东道主标记、运动员规模、参赛项目、奥运项目数量。
- 2028 洛杉矶预测：用 2024 各国状态外推，设置美国为东道主，用随机森林树分布给出 80% 预测区间。
- 首枚奖牌国家：把 2024 有参赛记录但历史总奖牌为 0 的 NOC 纳入候选，用树预测分布估计 `P(total>=0.5)` 后求和。
- 项目重要性：按 2008-2024 运动员奖牌记录，统计各 NOC 的优势运动奖牌行占比。
- “伟大教练”效应候选：在 NOC-运动-年份层面寻找相对近三届均值的突增，作为后续人工核验教练迁移的证据候选。

## 运行方式
- `/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/real_solutions/2025/MCM-C/solution.py`

## 关键结果
- 2024 留出集 Gold MAE：0.782524，Total MAE：1.709571
- 预计 2028 首次获得奖牌的 NOC 数量期望：11.366667

### 2028 总奖牌预测 Top 10

| NOC | 2024 total | 2028 pred total | 80% interval |
|---|---:|---:|---|
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

| NOC | 2024 total | 2028 pred total | change |
|---|---:|---:|---:|
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

## 输出文件
- `result.json`：完整结构化结果。
- `artifacts/prediction_2028.csv`：所有 NOC 的 2028 预测表。
- `artifacts/sport_importance.json`：各国优势运动。
- `artifacts/prediction_2028_top_total.png`：Top 总奖牌预测图。
