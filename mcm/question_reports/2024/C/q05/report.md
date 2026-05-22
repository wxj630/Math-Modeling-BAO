# 2024-C q05：给教练的备忘录与训练建议

## 题目原问
Prepare a memo summarizing findings and advice to coaches about the role of momentum and how to prepare players for flow-changing events.

## 适合模型
把势头定义、随机性证据、换向预警指标和比赛泛化结果转化为教练可执行的临场监控建议。

## 数据与真实性
- 数据类型：official_comap_csv。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted/2024/Problem Data- Momentum in Tennis`。
- 行数/记录数：{'2024_Wimbledon_featured_matches.csv': 7284, '2024_data_dictionary.csv': 46}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### Huskies coach memo
{'message': 'Treat momentum as a measurable serve-adjusted flow signal. It is useful for alerts and preparation, but it should be paired with tactical video review rather than treated as a standalone cause.', 'recommended_live_indicators': ['abs_momentum', 'momentum_delta', 'break_point_pressure', 'unforced_errors', 'winner_rate']}

### 势头流结果
- 比赛：2023-wimbledon-1701，Carlos Alcaraz vs Novak Djokovic。
- 逐分数：334。
- `momentum_p1` 范围：-0.345501 到 0.397021。
- 强势头换向次数：16。

#### 最大势头点

| point_index | set_no | game_no | better_player | momentum_p1 |
|---|---|---|---|---|
| 207 | 3 | 7 | Carlos Alcaraz | 0.397021 |
| 209 | 3 | 7 | Carlos Alcaraz | 0.366411 |
| 217 | 4 | 2 | Carlos Alcaraz | 0.349715 |
| 275 | 5 | 1 | Novak Djokovic | -0.345501 |
| 26 | 1 | 4 | Novak Djokovic | -0.345028 |
| 144 | 3 | 1 | Carlos Alcaraz | 0.339578 |
| 147 | 3 | 1 | Carlos Alcaraz | 0.336908 |
| 271 | 4 | 9 | Novak Djokovic | -0.335485 |

### 势头换向预测
- 预测目标：future momentum sign change with |momentum| >= 0.08 in the next 8 points。
- 训练行数：6950，留出行数：334。
- 留出 ROC-AUC：0.652191。
- 留出 Brier：0.230125。

#### 关键特征

| feature | coefficient |
|---|---|
| abs_momentum | -0.606494 |
| momentum_p1 | -0.101008 |
| p2_unf_err | -0.053191 |
| serve_no | 0.052086 |
| server_is_p1 | 0.050661 |
| speed_mph | 0.042079 |
| rally_count | 0.032498 |
| momentum_delta | 0.031298 |
| p2_break_pt | 0.02746 |
| distance_diff | 0.020708 |

#### 决赛最高换向预警点

| point_index | set_no | game_no | probability | momentum_p1 |
|---|---|---|---|---|
| 74 | 2 | 4 | 0.720524 | -0.021249 |
| 165 | 3 | 4 | 0.704953 | -0.03638 |
| 290 | 5 | 2 | 0.704461 | -0.003825 |
| 93 | 2 | 7 | 0.700914 | -0.009678 |
| 310 | 5 | 6 | 0.697397 | -0.001492 |
| 136 | 2 | 13 | 0.695693 | -0.008776 |
| 243 | 4 | 4 | 0.69418 | 0.003416 |
| 37 | 1 | 6 | 0.689699 | -0.005173 |

### 泛化测试
- 评估比赛数：31。
- 最后 30 分势头预测点数优势方准确率：0.806452。
- 决赛留出结果：{'predicted_winner_from_last30_momentum': 1, 'actual_point_winner': 1, 'correct': 1, 'last30_momentum_p1': 0.0264}。
- 局限：This evaluates point-share winner, not official match winner by sets; it is a robustness check for flow signal transfer across matches.

### 教练备忘录
- 核心建议：Treat momentum as a measurable serve-adjusted flow signal. It is useful for alerts and preparation, but it should be paired with tactical video review rather than treated as a standalone cause.
- 临场监控指标：
- `abs_momentum`
- `momentum_delta`
- `break_point_pressure`
- `unforced_errors`
- `winner_rate`

## 模型限制
- 这是可复现的官方数据基线实验，适合做论文骨架和结果表，不应把随机森林相关性解释为严格因果。
- 对异常国家/代表队名称、教练履历、项目规则变化等，需要在竞赛论文中追加人工核验和敏感性分析。

## 运行方式
`.venv/bin/python mcm/question_solutions/2024/C/q05/solution.py`

## 输出
- `mcm/question_results/2024/C/q05/result.json`
- `mcm/question_reports/2024/C/q05/report.md`
- `mcm/question_artifacts/2024/C/q05`
