# 2024-C q03：比赛流程换向预测与关键因素

## 题目原问
Develop a model to predict when flow is about to shift from one player to the other and identify relevant factors.

## 适合模型
以未来 8 分内强势头换向为标签，使用逻辑回归解释 `abs_momentum`、破发点、发球、速度、回合数和非受迫失误等因素。

## 数据与真实性
- 数据类型：official_comap_csv。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2024/Problem Data- Momentum in Tennis`。
- 行数/记录数：{'2024_Wimbledon_featured_matches.csv': 7284, '2024_data_dictionary.csv': 46}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 特征变量

- `momentum_p1`
- `abs_momentum`
- `momentum_delta`
- `server_is_p1`
- `serve_no`
- `p1_break_pt`
- `p2_break_pt`
- `rally_count`
- `speed_mph`
- `distance_diff`
- `p1_unf_err`
- `p2_unf_err`
- `p1_winner`
- `p2_winner`
- `score_pressure`

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

## 模型限制
- 这是可复现的官方数据基线实验，适合做论文骨架和结果表，不应把随机森林相关性解释为严格因果。
- 对异常国家/代表队名称、教练履历、项目规则变化等，需要在竞赛论文中追加人工核验和敏感性分析。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2024/C/q03/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2024/C/q03/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2024/C/q03/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2024/C/q03`
