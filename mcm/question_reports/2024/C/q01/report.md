# 2024-C q01：发球校正势头流与比赛流程可视化

## 题目原问
Develop a model that captures the flow of play as points occur, identify which player is performing better at a given time and how much better, and provide a visualization.

## 适合模型
发球胜率基线 + 逐分残差 + 指数加权移动平均势头指数 + 决赛逐分可视化。

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

### 发球基线
- 全部发球方得分率：0.673119。
- 一发发球方得分率：0.754134。
- 二发发球方得分率：0.529501。

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

## 模型限制
- 这是可复现的官方数据基线实验，适合做论文骨架和结果表，不应把随机森林相关性解释为严格因果。
- 对异常国家/代表队名称、教练履历、项目规则变化等，需要在竞赛论文中追加人工核验和敏感性分析。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2024/C/q01/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2024/C/q01/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2024/C/q01/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2024/C/q01`
