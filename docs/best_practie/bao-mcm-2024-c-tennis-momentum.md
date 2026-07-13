# MCM 2024-C 网球势头：Baseline → Advanced → Outstanding 进阶

这道题属于数据建模/统计推断类。它的入口是官方逐分数据，但 O 奖论文不会只训练一个分类器，而是先定义“势头是什么”，再检验它是否只是随机波动，最后才预测和给教练建议。

## 材料入口

| 层级 | PDF | 代码 | 结果 |
|---|---|---|---|
| Baseline | `Math-Modeling-World-Reports/mcm/2024-C/baseline/main.pdf` | `Math-Modeling-World/mcm/generic_baselines/solutions/2024/C/q01/solution.py` 到 `q05/solution.py` | `Math-Modeling-World/mcm/generic_baselines/results/2024/C/q01/result.json` 到 `q05/result.json` |
| Advanced | `Math-Modeling-World-Reports/mcm/2024-C/advanced/main.pdf` | `Math-Modeling-World/docs/mcm-2015-2025/real_solutions/2024/MCM-C/solution.py`；逐问包装器在 `mcm/question_solutions/2024/C/` | `Math-Modeling-World/docs/mcm-2015-2025/real_solutions/2024/MCM-C/result.json`；逐问结果在 `mcm/question_results/2024/C/` |
| Outstanding | `Math-Modeling-World-Reports/outstanding/mcm/2024-C/2401298/pdf/2401298.pdf` | `Math-Modeling-World/mcm/outstanding_solutions/2024/C/2401298/solution.py` | `Math-Modeling-World/mcm/outstanding_solutions/2024/C/2401298/result.json` |

OCR 文本在 `Math-Modeling-World-Reports/outstanding/mcm/2024-C/2401298/ocr/2401298.md`。

## 数据和求解库

这题有官方数据，是三题里数据最干净的一题：

```text
Math-Modeling-World/mcm/source_materials/official_extracted/2024/Problem Data- Momentum in Tennis/2024_Wimbledon_featured_matches.csv
Math-Modeling-World/mcm/source_materials/official_extracted/2024/Problem Data- Momentum in Tennis/2024_data_dictionary.csv
```

Advanced 使用：

```text
numpy, pandas, matplotlib, sklearn
```

Outstanding 复现使用：

```text
numpy, pandas, matplotlib, scipy.stats
```

这里的数据建模不是“有数据就上黑盒模型”。核心是先做发球优势校正，把 point result 变成 residual，再讨论 residual 是否存在时间结构。

## Baseline：先把官方数据和输出物跑起来

Baseline 的逐问结果：

| 小问 | Baseline 方法 | baseline_score |
|---|---|---:|
| q01 | `network_path_baseline` | 0.506514 |
| q02 | `linear_weighted_score_baseline` | 0.602429 |
| q03 | `linear_trend_forecast_baseline` | 0.640857 |
| q04 | `linear_trend_forecast_baseline` | 0.627143 |
| q05 | `report_outline_baseline` | 0.579514 |

baseline 已经能产出一些图表路径，例如 `final_match_momentum_flow.png` 和 `largest_momentum_points.csv`，但模型选择还很粗。

一句大白话：baseline 会“把数据跑出东西”，但还没有认真回答势头是不是独立随机波动，也没有定义可辩护的 momentum。

## Advanced：发球校正残差 + EWMA + 逻辑回归预警

Advanced 的整题实现放在：

```text
Math-Modeling-World/docs/mcm-2015-2025/real_solutions/2024/MCM-C/solution.py
```

它的主线是：

```text
官方逐分 CSV
→ 发球胜率基线
→ point-level residual
→ EWMA momentum_p1
→ 随机波动评估
→ 未来 8 分换向逻辑回归
→ 教练备忘录
```

关键结果：

| 指标 | Advanced 结果 |
|---|---:|
| 官方逐分记录 | 7284 |
| 比赛数 | 31 |
| 发球方总得分率 | 0.673119 |
| 一发发球方得分率 | 0.754134 |
| 二发发球方得分率 | 0.529501 |
| 决赛 `momentum_p1` 最小值 | -0.345501 |
| 决赛 `momentum_p1` 最大值 | 0.397021 |
| 决赛强换向次数 | 16 |
| 逻辑回归 holdout ROC AUC | 0.652191 |
| 逻辑回归 holdout AP | 0.601059 |

advanced 的进步是明显的：它不只预测 winner，而是把“势头”定义成发球期望之外的残差表现，再用这个指标解释比赛流程。

## Outstanding：先证据链，再 Bayesian 网络

O 奖论文 2401298 的标题是 `"Momentum" Exists In Tennis Game As Residual Effect - A Dual-Temporal Bayesian Network Model`。

论文 OCR 显示它的模型链是：

```text
server/returner reweighting
→ sliding window and AUC
→ Ljung-Box Q Test and Runs Test
→ Naive Binomial residual momentum
→ Dual-Temporal Bayesian Network
→ entropy reduction feature importance
→ sensitivity analysis
→ coaching memo
```

当前复现关键结果：

| 指标 | Outstanding 复现 |
|---|---:|
| 官方逐分记录 | 7284 |
| 比赛数 | 31 |
| median Ljung-Box p-value | 0.712832 |
| 5% 水平拒绝 iid 的比赛数 | 0 |
| median Runs Test p-value | 0.290172 |
| Bayesian transition rows | 26 |
| 最强转移概率 | 0.6726 |
| swing warning rate | 0.0032 |
| final match warning rate | 0.006 |

这篇 O 奖论文好在它没有把 momentum 写成玄学。它先承认随机性检验并没有强烈拒绝 iid，再说“即便随机性很强，发球校正后的残差和双时间状态仍能提供微弱但可解释的预警信号”。这个表达非常重要，因为它比“模型证明 momentum 存在”更克制，也更经得起检验。

## 谁建模得最好

| 层级 | 数据建模能力 | 评奖视角 |
|---|---|---|
| Baseline | 能读取官方数据并产出基本表图 | 方法和题意贴合度不够 |
| Advanced | 定义发球残差势头，并用逻辑回归做换向预警 | 可复现、可解释，已经适合课程讲解 |
| Outstanding | 把 residual、随机性检验、Bayesian 网络和策略建议连成证据链 | 三题里当前复现对论文方法和数据对齐最好 |

结论：这题最值得学习的是“数据建模题不是只训练模型”。先定义变量，再做统计检验，再预测，再把结果变成决策建议，这条链条才像论文。
