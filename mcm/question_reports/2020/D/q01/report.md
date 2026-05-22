# 2020-D q01：传球网络、二元三元结构与多尺度指标

## 题目原问
Create a network for the ball passing between players, where each player is a node and each pass constitutes a link between players. Use your passing network to identify network patterns, such as dyadic and triadic configurations and team formations. Also consider other structural indicators and network properties across the games.

## 适合模型
读取 COMAP 官方 matches.csv、passingevents.csv、fullevents.csv；以 Huskies 球员为节点、有向传球为加权边，计算二元边、三角 motif、互惠率、PageRank、介数中心性、密度、加权聚类和位置份额。对应模型：图论网络中心性、复杂网络、多尺度团队结构分析。

## 数据与真实性
- 数据类型：official_comap_csv。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2020/Problem Data- Teaming Strategies/2020_Problem_D_DATA`。
- 行数/记录数：{'matches.csv': 38, 'passingevents.csv': 23429, 'fullevents.csv': 59271}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### Teaming Strategies 传球网络
- Huskies 球员节点数：30。
- Huskies 官方传球数：10435。
- 有向边数：656。
- 赛季网络密度：0.754023；互惠率：0.893293；加权聚类：0.049912。

#### Top pass pairs

| origin | destination | origin_position | destination_position | pass_count |
|---|---|---|---|---|
| Huskies_M1 | Huskies_F2 | M | F | 182 |
| Huskies_M3 | Huskies_M1 | M | M | 168 |
| Huskies_M1 | Huskies_M3 | M | M | 143 |
| Huskies_D3 | Huskies_G1 | D | G | 120 |
| Huskies_F2 | Huskies_M1 | F | M | 117 |
| Huskies_D1 | Huskies_G1 | D | G | 107 |
| Huskies_D1 | Huskies_D3 | D | D | 105 |
| Huskies_D3 | Huskies_D1 | D | D | 98 |
| Huskies_D5 | Huskies_F2 | D | F | 97 |
| Huskies_D1 | Huskies_M1 | D | M | 92 |

#### Top central players

| player | position | weighted_out_degree | weighted_in_degree | pagerank | teamwork_centrality |
|---|---|---|---|---|---|
| Huskies_M1 | M | 1255 | 1017 | 0.089594 | 0.088349 |
| Huskies_F2 | F | 859 | 927 | 0.081094 | 0.068323 |
| Huskies_M3 | M | 887 | 717 | 0.062069 | 0.061749 |
| Huskies_D1 | D | 851 | 678 | 0.055192 | 0.058507 |
| Huskies_D3 | D | 727 | 582 | 0.049954 | 0.051578 |
| Huskies_D5 | D | 625 | 581 | 0.052494 | 0.047269 |
| Huskies_D4 | D | 569 | 615 | 0.054918 | 0.046626 |
| Huskies_M6 | M | 508 | 537 | 0.05317 | 0.044515 |
| Huskies_M4 | M | 497 | 521 | 0.050837 | 0.043406 |
| Huskies_D2 | D | 580 | 467 | 0.03979 | 0.040836 |

### 结构、阵型与多尺度模式

#### 按结果分组的结构指标

| Outcome | matches | avg_passes | avg_density | avg_reciprocity | avg_triads | avg_forward_share | avg_midfield_share | avg_attacking_third | avg_goal_diff |
|---|---|---|---|---|---|---|---|---|---|
| loss | 15.0 | 279.2 | 0.5769 | 0.7126 | 154.2667 | 0.147 | 0.3859 | 0.3068 | -2.3333 |
| tie | 10.0 | 232.1 | 0.519 | 0.6778 | 123.8 | 0.1392 | 0.3793 | 0.2945 | 0.0 |
| win | 13.0 | 302.0 | 0.5758 | 0.7525 | 146.7692 | 0.1927 | 0.3517 | 0.2895 | 1.6154 |

#### 多尺度解释

- micro: repeated dyadic pass pairs and top-pair concentration
- meso: triadic configurations, weighted clustering, and position-share formations
- macro: season-level directed passing network density and reciprocity
- temporal: match-by-match features ordered across all 38 official matches
- 时间尺度说明：MatchPeriod contains 1H/2H values; this workflow aggregates full-match features and keeps half-level fields available for minute-level extensions.

## 模型限制
- 这是可复现的官方 Teaming Strategies CSV 附件实验；只使用 matches.csv、passingevents.csv、fullevents.csv 和 README.txt，不使用随机造数。
- 球队成功模型使用前 30 场训练、后 8 场留出，只说明官方赛季样本内的协作指标可解释性；正式论文应补充更多赛季、对手强度、球员伤停和战术视频标注。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2020/D/q01/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2020/D/q01/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2020/D/q01/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2020/D/q01`
