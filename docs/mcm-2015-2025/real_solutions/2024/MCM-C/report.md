# 2024 MCM-C Momentum in Tennis 真实数据解法

## 数据来源
- 使用 COMAP 官方 `2024_Wimbledon_featured_matches.csv` 和 `2024_data_dictionary.csv`。
- 每一行是温网 2023 男单第三轮以后比赛的一分；本解法不生成随机比赛数据。

## 建模核心
- 先估计发球方在一发/二发情境下的平均得分率，得到每分中 player1 的发球校正期望胜率。
- 用 `actual_p1_win - expected_p1_win` 得到去除发球优势后的残差。
- 对残差做指数加权平均，定义 `momentum_p1`；正值表示 player1 超出发球期望，负值表示 player2 占优。
- 以未来 8 分内是否发生强势头换向作为波动预测标签，训练逻辑回归模型解释关键因素。

## 官方数据规模
- 逐分记录：7284 行。
- 数据字典：46 行。
- 比赛数：31 场。

## Q1 比赛流程和可视化
- 决赛 `2023-wimbledon-1701`：Carlos Alcaraz vs Novak Djokovic，共 334 分。
- `momentum_p1` 范围：[-0.345501, 0.397021]。
- 强势头换向次数：16。
- 可视化：`artifacts/final_match_momentum_flow.png`。

## Q2 随机波动假设评估
- 全部比赛发球校正残差 lag-1 平均相关：0.022716。
- 跨比赛 z 值：1.973167。
- 决赛最长连续得分串：7 分。
- 解释：该证据能反驳“完全没有时间结构”的强表述，但不能单独证明心理动量因果。

## Q3 波动预测模型
- 训练行数：6950，留出比赛：2023-wimbledon-1701。
- 训练 ROC-AUC：0.661331，留出 ROC-AUC：0.652191。
- 留出 Brier：0.230125。

### 关键特征系数
| feature | coefficient |
|---|---:|
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

## Q4 泛化测试
- 使用最后 30 分平均势头预测点数优势方，跨 31 场准确率：0.806452。
- 决赛留出检查：{'predicted_winner_from_last30_momentum': 1, 'actual_point_winner': 1, 'correct': 1, 'last30_momentum_p1': 0.0264}。
- 局限：该检验针对逐分优势信号，不等同于正式盘分制胜负预测。

## Q5 给教练的建议摘要
- 动量不是神秘变量，可以被定义为发球校正后的连续超预期表现。
- 比赛中应重点监控 `abs_momentum`、`momentum_delta`、破发点压力、非受迫失误和制胜分。
- 当未来 8 分换向概率升高时，建议通过发球落点、接发保守度、拍间恢复和局间战术沟通降低连续丢分风险。

## 输出文件
- `result.json`：结构化结果。
- `artifacts/final_match_momentum_flow.csv`：决赛逐分势头表。
- `artifacts/final_match_momentum_flow.png`：决赛势头曲线。
- `artifacts/swing_model_coefficients.csv`：波动预测模型系数。
