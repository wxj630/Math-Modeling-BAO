# 2020-D q02：团队表现指标与协作成功模型

## 题目原问
Identify performance indicators that reflect successful teamwork such as diversity in the types of plays, coordination among players or distribution of contributions. Use the performance indicators and team level processes that you have identified to create a model that captures structural, configurational, and dynamical aspects of teamwork.

## 适合模型
构建逐场协作特征表：传球总数、相对传球优势、网络密度、互惠率、聚类、传球类型熵、头部传球对占比、贡献 Gini、平均传球距离、前向传球和进攻三区比例、射门/对抗/犯规事件；用前 30 场训练、后 8 场时间留出检验非输球分类模型。对应模型：指标体系、解释型决策树、时间留出验证。

## 数据与真实性
- 数据类型：official_comap_csv。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted/2020/Problem Data- Teaming Strategies/2020_Problem_D_DATA`。
- 行数/记录数：{'matches.csv': 38, 'passingevents.csv': 23429, 'fullevents.csv': 59271}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

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

### 团队协作成功模型
- 目标变量：1 for win or tie, 0 for loss; model inputs exclude goals and final score.
- 模型：deterministic DecisionTreeClassifier(max_depth=2, min_samples_leaf=3)。
- 训练场次：30；留出场次：8。
- 留出 accuracy：0.75；balanced accuracy：0.666667。

#### 特征重要性

| feature | importance |
|---|---|
| network_density | 0.5375315530755949 |
| average_pass_length | 0.46246844692440525 |
| passes | 0.0 |
| pass_advantage | 0.0 |
| players_involved | 0.0 |
| network_reciprocity | 0.0 |
| weighted_clustering | 0.0 |
| pass_type_entropy | 0.0 |

#### 留出预测

| MatchID | Outcome | team_success_non_loss | predicted_success_non_loss |
|---|---|---|---|
| 31 | win | 1 | 0 |
| 32 | loss | 0 | 1 |
| 33 | tie | 1 | 1 |
| 34 | tie | 1 | 1 |
| 35 | win | 1 | 1 |
| 36 | win | 1 | 1 |
| 37 | tie | 1 | 1 |
| 38 | loss | 0 | 0 |

## 模型限制
- 这是可复现的官方 Teaming Strategies CSV 附件实验；只使用 matches.csv、passingevents.csv、fullevents.csv 和 README.txt，不使用随机造数。
- 球队成功模型使用前 30 场训练、后 8 场留出，只说明官方赛季样本内的协作指标可解释性；正式论文应补充更多赛季、对手强度、球员伤停和战术视频标注。

## 运行方式
`.venv/bin/python mcm/question_solutions/2020/D/q02/solution.py`

## 输出
- `mcm/question_results/2020/D/q02/result.json`
- `mcm/question_reports/2020/D/q02/report.md`
- `mcm/question_artifacts/2020/D/q02`
