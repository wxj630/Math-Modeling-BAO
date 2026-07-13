# MCM 2024-B 失联潜水器：Baseline → Advanced → Outstanding 进阶

这道题属于运筹优化/搜索救援类。它看起来是“怎么搜最快”，但真正难点在前面：失联目标在哪里、位置不确定性多大、装备如何选择、搜索结果如何反过来更新下一步路径。

## 材料入口

| 层级 | PDF | 代码 | 结果 |
|---|---|---|---|
| Baseline | `Math-Modeling-BAO-Reports/mcm/2024-B/baseline/main.pdf` | `Math-Modeling-BAO/mcm/generic_baselines/solutions/2024/B/q01/solution.py` 到 `q04/solution.py` | `Math-Modeling-BAO/mcm/generic_baselines/results/2024/B/q01/result.json` 到 `q04/result.json` |
| Advanced | `Math-Modeling-BAO-Reports/mcm/2024-B/advanced/main.pdf` | `Math-Modeling-BAO/docs/mcm-2015-2025/real_solutions/2024/MCM-B/solution.py`；逐问包装器在 `mcm/question_solutions/2024/B/` | `Math-Modeling-BAO/docs/mcm-2015-2025/real_solutions/2024/MCM-B/result.json`；逐问结果在 `mcm/question_results/2024/B/` |
| Outstanding | `Math-Modeling-BAO-Reports/outstanding/mcm/2024-B/2419984/pdf/2419984.pdf` | `Math-Modeling-BAO/mcm/outstanding_solutions/2024/B/2419984/solution.py` | `Math-Modeling-BAO/mcm/outstanding_solutions/2024/B/2419984/result.json` |

OCR 文本在 `Math-Modeling-BAO-Reports/outstanding/mcm/2024-B/2419984/ocr/2419984.md`。

## 数据和求解库

这题没有官方事故 CSV。官方 PDF 给任务约束，真实建模需要外部或场景数据，例如海区水深、洋流、装备覆盖率、声学定位能力和救援船准备时间。

当前 advanced 代码主要用：

```text
math, numpy, pandas, matplotlib
```

当前 outstanding 复现主要用：

```text
numpy, pandas, matplotlib
```

这里的“优化”没有直接调用 `scipy.optimize` 或 MILP 求解器，而是用确定性规则、概率更新、网格排序和 ACO 风格路径代价来构造可复现搜索方案。

## Baseline：先把“搜索优化题”识别出来

Baseline 的逐问结果：

| 小问 | Baseline 方法 | baseline_score |
|---|---|---:|
| q01 | `linear_trend_forecast_baseline` | 0.592314 |
| q02 | `linear_weighted_score_baseline` | 0.611171 |
| q03 | `network_path_baseline` | 0.585743 |
| q04 | `report_outline_baseline` | 0.525257 |

baseline 能抓住关键词：位置预测、装备评分、搜索路径、政府备忘录。它的不足是显然的：还没有真正把“位置不确定性”传到“搜索路径”里。

一句大白话：baseline 知道这题要找路、配装备、写备忘录，但还没有形成“搜哪里取决于概率后验”的闭环。

## Advanced：位置椭圆 + 装备评分 + 发现概率曲线

Advanced 的整题实现放在：

```text
Math-Modeling-BAO/docs/mcm-2015-2025/real_solutions/2024/MCM-B/solution.py
```

它做了四件事：

1. 用洋流漂移和垂直状态不确定性，生成位置椭圆。
2. 按覆盖面积、探测质量、准备时间、成本、维护负担给装备打分。
3. 将搜索面积转成发现概率：

```text
P_found(t) = 1 - exp(-sum(effective_swept_area / uncertainty_area))
```

4. 输出部署点和搜索模式。

关键结果：

| 指标 | Advanced 结果 |
|---|---|
| 12 小时位置不确定面积 | 16.9261 km2 |
| 24 小时位置不确定面积 | 62.5273 km2 |
| 12 小时发现概率 | 0.7489 |
| 24 小时发现概率 | 0.7812 |
| 初始部署点 | P0 predicted center, P1/P2 drift-axis focus, P3/P4 cross-current edge |

advanced 已经是完整的救援预案。它比 baseline 强在“前一问结果服务后一问”：位置模型给搜索模型提供不确定区域，装备评分决定扫测速度和质量，发现概率随时间更新。

## Outstanding：后验位置驱动搜索路径

O 奖论文 2419984 的标题是 `Time is Life: Precise Localization and Faster Search`。

论文 OCR 显示它的模型链是：

```text
Ionian Sea depth/current data
→ RK4 drift dynamics
→ Monte Carlo uncertainty
→ entropy-weight equipment scoring
→ Bayesian grid posterior
→ ant colony search path
→ sensitivity analysis on drag coefficients
```

复现代码中的方法说明是：

```text
RK4 动力漂移 + Monte Carlo 粒子 + 熵权装备评分 + Bayesian 搜索更新 + ACO 风格路径排序
```

当前复现关键结果：

| 指标 | Outstanding 复现 |
|---|---:|
| Monte Carlo 粒子数 | 100000 |
| 10 小时均值位置 x | 7698.65 m |
| 10 小时均值位置 y | -2324.78 m |
| 10 小时 95% 位置面积 | 0.9722 km2 |
| 最高装备 | surface_drift_buoys |
| 装备最高分 | 0.8357 |
| 6 小时发现概率 | 0.4068 |
| 1 小时启动、10 小时发现概率 | 0.43 |
| 3 小时启动、10 小时发现概率 | 0.2338 |
| 5 小时启动、10 小时发现概率 | 0.1158 |
| 18 小时扩展搜索发现概率 | 0.4377 |
| 搜索网格数 | 18 |

论文 OCR 中提到“1 小时启动搜索时，10 小时内发现概率约 43%；5 小时启动时约 10%”。校准后的复现用 100000 个 Monte Carlo 粒子、400m 网格和 ACO 风格路径排序，对齐了 `0.43` 这个关键目标；5 小时延迟启动得到 `0.1158`，也贴近论文“约 10%”的量级。

## 谁优化得最好

| 层级 | 优化能力 | 评奖视角 |
|---|---|---|
| Baseline | 能把题归到路径/评分/报告框架 | 没有后验概率闭环 |
| Advanced | 位置椭圆、装备、部署点、发现概率已经连起来 | 可作为完整可运行方案 |
| Outstanding | 用 Monte Carlo 后验和 Bayesian 更新驱动 ACO 风格搜索 | 关键概率已经校准到论文 OCR 报告量级 |

结论：这题最值得学习的是“运筹优化题通常不是只有优化”。优化之前必须先估计状态和风险；优化之后还要根据搜索结果更新下一步决策。
