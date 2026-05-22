# 2020-D q04：从足球团队推广到一般跨学科团队

## 题目原问
As our societies increasingly solve problems involving teams, can you generalize your findings to say something about how to design and monitor successful teams in other settings?

## 适合模型
把球员映射为专家，把传球映射为任务交接，提炼互惠信息流、冗余三元组、互动类型多样性和持续监控机制，说明如何迁移到科研、工程、医疗或应急团队。对应模型：复杂网络类比、组织协作指标迁移。

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

### 一般跨学科团队推广
The soccer result generalizes to interdisciplinary teams by replacing players with specialists and passes with task handoffs. Successful interdisciplinary teams should have reciprocal information flow, redundant triads that prevent single-point failure, enough diversity of interaction types to adapt under pressure, and a monitoring routine that compares current teamwork indicators with past successful patterns.

## 模型限制
- 这是可复现的官方 Teaming Strategies CSV 附件实验；只使用 matches.csv、passingevents.csv、fullevents.csv 和 README.txt，不使用随机造数。
- 球队成功模型使用前 30 场训练、后 8 场留出，只说明官方赛季样本内的协作指标可解释性；正式论文应补充更多赛季、对手强度、球员伤停和战术视频标注。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2020/D/q04/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2020/D/q04/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2020/D/q04/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2020/D/q04`
