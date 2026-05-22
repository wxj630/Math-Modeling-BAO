# 2020 ICM-D Teaming Strategies：官方足球事件数据实验报告

## 数据真实性

- 官方题面：`docs/mcm-2015-2025/official_assets_extracted/2020/Teaming Strategies.pdf`。
- 官方附件目录：`docs/mcm-2015-2025/official_assets_extracted/2020/Problem Data- Teaming Strategies/2020_Problem_D_DATA`。
- 行数：`{'matches.csv': 38, 'passingevents.csv': 23429, 'fullevents.csv': 59271}`。
- 本解法只读取 COMAP 官方 CSV 和 README，不生成随机 `x1/x2/x3` 数据。

## 每问建模与求解

### q01 传球网络、二元/三元结构与多尺度指标

- 模型：有向加权图、PageRank、介数中心性、互惠率、加权聚类和三角形 motif。
- Huskies 球员节点数：30；传球数：10435；有向边：656。
- 赛季网络密度：0.754023；互惠率：0.893293。

### q02 团队表现指标与团队协作模型

- 模型：传球熵、贡献 Gini、前向传球比例、进攻三区比例、shot/duel/foul 事件计数和解释型决策树。
- 目标变量：1 for win or tie, 0 for loss; model inputs exclude goals and final score.
- 时间留出：前 30 场训练，后 8 场检验。
- 留出准确率：0.75；balanced accuracy：0.666667。

### q03 给 Huskies 教练的结构策略建议

- Keep the passing network reciprocal rather than hub-only. 证据：Season reciprocity is 0.893293; wins have reciprocity 0.7525 versus losses 0.7126.
- Use midfield-forward triangles as the default attacking build-up pattern. 证据：Wins average 146.77 triadic configurations versus 154.27 in losses.
- Protect pass diversity instead of relying on one repeated dyad. 证据：The best positive feature gap is pass_advantage = 150.5692.
- Monitor match-by-match teamwork features after tactical changes. 证据：The holdout model uses only network/event indicators and predicts non-loss outcomes on the last 8 official matches.

### q04 对一般团队协作的推广

The soccer result generalizes to interdisciplinary teams by replacing players with specialists and passes with task handoffs. Successful interdisciplinary teams should have reciprocal information flow, redundant triads that prevent single-point failure, enough diversity of interaction types to adapt under pressure, and a monitoring routine that compares current teamwork indicators with past successful patterns.

## 给教练的备忘录

To the Huskies coach: use the season passing network as a tactical dashboard. The official data show that coordination should be managed as a graph, not as isolated player totals: track reciprocal passing links, midfield-forward triads, pass-type diversity, and whether one dyad is carrying too much of the build-up. For next season, rehearse possessions that keep at least three stable passing outlets around the ball, protect the midfield bridge players, and review the teamwork feature table after every match rather than waiting for final league results.

## 产物

- `artifacts/match_teamwork_features.csv`：38 场比赛逐场团队协作指标。
- `artifacts/passing_network_edges.csv`：赛季有向传球边表。
- `artifacts/player_centrality.csv`：球员中心性和位置角色。
- `artifacts/teamwork_feature_importance.csv`：模型特征重要性。
- `artifacts/passing_network_top_edges.png`：Top 传球边图。
