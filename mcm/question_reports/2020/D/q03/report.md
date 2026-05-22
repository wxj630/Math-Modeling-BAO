# 2020-D q03：给 Huskies 教练的结构策略建议

## 题目原问
Use the insights gained from your teamwork model to inform the coach about what kinds of structural strategies have been effective for the Huskies. Advise the coach on what changes the network analysis indicates that they should make next season to improve team success.

## 适合模型
比较胜/负场协作指标差异与决策树特征重要性，形成互惠传球、midfield-forward 三角、传球多样性、赛后监测四类建议，并给出面向教练的非技术备忘录。对应模型：对比分析、特征重要性、策略决策表。

## 数据与真实性
- 数据类型：official_comap_csv。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted/2020/Problem Data- Teaming Strategies/2020_Problem_D_DATA`。
- 行数/记录数：{'matches.csv': 38, 'passingevents.csv': 23429, 'fullevents.csv': 59271}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

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

### 给教练的结构策略建议

- 建议：Keep the passing network reciprocal rather than hub-only.
- 证据：Season reciprocity is 0.893293; wins have reciprocity 0.7525 versus losses 0.7126.
- 模型族：directed graph reciprocity and weighted centrality
- 建议：Use midfield-forward triangles as the default attacking build-up pattern.
- 证据：Wins average 146.77 triadic configurations versus 154.27 in losses.
- 模型族：triadic network motifs and formation shares
- 建议：Protect pass diversity instead of relying on one repeated dyad.
- 证据：The best positive feature gap is pass_advantage = 150.5692.
- 模型族：entropy, concentration, and contribution-distribution indicators
- 建议：Monitor match-by-match teamwork features after tactical changes.
- 证据：The holdout model uses only network/event indicators and predicts non-loss outcomes on the last 8 official matches.
- 模型族：interpretable classification with temporal holdout

### Huskies coach memo
To the Huskies coach: use the season passing network as a tactical dashboard. The official data show that coordination should be managed as a graph, not as isolated player totals: track reciprocal passing links, midfield-forward triads, pass-type diversity, and whether one dyad is carrying too much of the build-up. For next season, rehearse possessions that keep at least three stable passing outlets around the ball, protect the midfield bridge players, and review the teamwork feature table after every match rather than waiting for final league results.

## 模型限制
- 这是可复现的官方 Teaming Strategies CSV 附件实验；只使用 matches.csv、passingevents.csv、fullevents.csv 和 README.txt，不使用随机造数。
- 球队成功模型使用前 30 场训练、后 8 场留出，只说明官方赛季样本内的协作指标可解释性；正式论文应补充更多赛季、对手强度、球员伤停和战术视频标注。

## 运行方式
`.venv/bin/python mcm/question_solutions/2020/D/q03/solution.py`

## 输出
- `mcm/question_results/2020/D/q03/result.json`
- `mcm/question_reports/2020/D/q03/report.md`
- `mcm/question_artifacts/2020/D/q03`
