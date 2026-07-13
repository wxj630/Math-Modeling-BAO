# MCM 2024-A 七鳃鳗：Baseline → Advanced → Outstanding 进阶

这道题属于动态系统/生态模型类。它的入口是“性别比随资源变化”，但 O 奖解法不会停在一条响应曲线，而是把生命周期、宿主、寄生者、捕食者、生态多样性和稳定性评价连成模型链。

## 材料入口

| 层级 | PDF | 代码 | 结果 |
|---|---|---|---|
| Baseline | `Math-Modeling-BAO-Reports/mcm/2024-A/baseline/main.pdf` | `Math-Modeling-BAO/mcm/generic_baselines/solutions/2024/A/q01/solution.py` 到 `q04/solution.py` | `Math-Modeling-BAO/mcm/generic_baselines/results/2024/A/q01/result.json` 到 `q04/result.json` |
| Advanced | `Math-Modeling-BAO-Reports/mcm/2024-A/advanced/main.pdf` | `Math-Modeling-BAO/docs/mcm-2015-2025/real_solutions/2024/MCM-A/solution.py`；逐问包装器在 `mcm/question_solutions/2024/A/` | `Math-Modeling-BAO/docs/mcm-2015-2025/real_solutions/2024/MCM-A/result.json`；逐问结果在 `mcm/question_results/2024/A/` |
| Outstanding | `Math-Modeling-BAO-Reports/outstanding/mcm/2024-A/2407093/pdf/2407093.pdf` | `Math-Modeling-BAO/mcm/outstanding_solutions/2024/A/2407093/solution.py` | `Math-Modeling-BAO/mcm/outstanding_solutions/2024/A/2407093/result.json` |

OCR 文本在 `Math-Modeling-BAO-Reports/outstanding/mcm/2024-A/2407093/ocr/2407093.md`。

## 数据和求解库

这题没有官方 CSV/XLSX 附件，主要依赖题面 PDF 给出的性别比端点：资源少时雄性比例约 `0.78`，资源多时雄性比例约 `0.56`。

当前 advanced 和 outstanding 复现主要用：

```text
numpy, pandas, matplotlib
```

这里不是典型 `solve_ivp` ODE 题，而是离散月份差分仿真。核心是把生物机制写成状态更新方程，再用网格情景和稳定性指标比较结果。

## Baseline：先判断这是动态生态题

Baseline 的逐问模型仍然是通用基线：

| 小问 | Baseline 方法 | baseline_score |
|---|---|---:|
| q01 | `evidence_table_baseline` | 0.491457 |
| q02 | `evidence_table_baseline` | 0.436457 |
| q03 | `linear_weighted_score_baseline` | 0.488886 |
| q04 | `threshold_classification_baseline` | 0.410543 |

它的价值是快速识别关键词：资源、性别比、生态系统、稳定性。问题是它没有真正模拟七鳃鳗，也没有把宿主、寄生者、捕食者接进去。

一句大白话：baseline 知道这是生态动态题，但还只是“题目理解 + 通用评分”，不是一个可解释的生态模型。

## Advanced：把题面参数接进差分仿真

Advanced 的整题实现放在：

```text
Math-Modeling-BAO/docs/mcm-2015-2025/real_solutions/2024/MCM-A/solution.py
```

它做了三件关键事：

1. 用题面端点建立资源到雄性比例的线性响应：

```text
male_ratio(resource) = 0.78 - (0.78 - 0.56) * resource_index
```

2. 用月度差分方程模拟 lamprey、host fish、parasites、predators food web。
3. 输出响应曲线、情景比较、稳定性表和图。

关键结果：

| 指标 | Advanced 结果 |
|---|---|
| 资源指数 0 时雄性比例 | 0.78 |
| 资源指数 1 时雄性比例 | 0.56 |
| 中等资源自适应雄性比例 | 约 0.67 |
| 输出图表 | `sex_ratio_response.csv`、`ecosystem_trajectories.csv`、`stability_surface.csv`、`lamprey_tradeoff_frontier.png` |

advanced 的进步是：它终于让“资源影响性别比，性别比影响生态状态”成为可运行模型。缺点也清楚：生命周期结构还比较粗，稳定性指标也偏工程化。

## Outstanding：把生态链条做完整

O 奖论文 2407093 的标题是 `Coexist or Extinct? Relationship between Lampreys and Environment`。

论文 OCR 显示它的模型链是：

```text
BFM Model
→ Logistic population growth
→ juvenile/female/male lifecycle
→ Lotka-Volterra predator-prey
→ Nicholson-Bailey host-parasite
→ Simpson/Shannon diversity
→ resistance/resilience/comprehensive stability
→ sensitivity analysis
```

复现代码中的方法说明是：

```text
资源驱动性别比 + 分阶段种群动力学 + Lotka-Volterra/Nicholson-Bailey + 3R 稳定性指标 + 敏感性网格
```

这比 advanced 强在两点：

- 模型结构从“总量种群”升级为“幼体、雌体、雄体”的生命周期模型。
- 评价从“看曲线”升级为“多样性 + resistance + resilience + sustainability”的稳定性证据链。

校准后的复现结果已经把方向拉回到论文结论：四个资源情景下，adaptive 相对 fixed 的综合稳定性提升分别为 `3.26%`、`1.04%`、`0.31%`、`3.08%`。中等资源情景下，adaptive 的寄生者指数为 `8.562`、宿主鱼指数为 `1080.356`，不再出现早期复现里的寄生者灭绝问题。

## 谁模拟得最好

| 层级 | 模拟能力 | 评奖视角 |
|---|---|---|
| Baseline | 只能识别题型和给粗评分 | 不足以支撑论文结论 |
| Advanced | 能用题面端点跑出资源性别比和生态情景 | 适合做课程里的“可运行专用模型” |
| Outstanding | 生命周期、物种交互、多样性和稳定性都进入同一链条 | 结构和关键结论方向已经对齐 O 奖论文 |

结论：这题最值得学习的是“微分方程/动态系统题不是只有方程”。方程后面必须接评价指标、稳定性检验和管理建议，否则论文只是在画曲线。
