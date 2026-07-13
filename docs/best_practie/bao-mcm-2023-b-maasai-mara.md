# MCM 2023-B Maasai Mara 保护与收益分区：Baseline → Advanced → Outstanding 进阶

这道题的主入口是 **运筹优化/空间分区**。从教程角度看，baseline 解决“能跑通”，advanced 解决“更贴题”，Outstanding 解决“证据链完整、结果可检验、表达能让评委快速相信”。

## 材料入口

| 层级 | PDF | 代码 | 结果 |
|---|---|---|---|
| Baseline | `Math-Modeling-BAO-Reports/mcm/2023-B/baseline/main.pdf` | `Math-Modeling-BAO/mcm/generic_baselines/solutions/2023/B` | `Math-Modeling-BAO/mcm/generic_baselines/results/2023/B` |
| Advanced | `Math-Modeling-BAO-Reports/mcm/2023-B/advanced/main.pdf` | `Math-Modeling-BAO/docs/mcm-2015-2025/real_solutions/2023/MCM-B/solution.py` | `Math-Modeling-BAO/docs/mcm-2015-2025/real_solutions/2023/MCM-B/result.json` |
| Outstanding | `Math-Modeling-BAO-Reports/outstanding/mcm/2023-B/2315379/pdf/2315379.pdf` | `Math-Modeling-BAO/mcm/outstanding_solutions/2023/B/2315379/solution.py` | `Math-Modeling-BAO/mcm/outstanding_solutions/2023/B/2315379/result.json` |

OCR 文本：`Math-Modeling-BAO-Reports/outstanding/mcm/2023-B/2315379/ocr/2315379.md`。

## 数据来源

本题复现使用的数据/参数入口如下：

- `paper-defined 36-grid abstraction`
- `paper-reported scenario benefits and area counts`


## Baseline：先把题跑通

Baseline 的价值是建立最小可运行闭环：逐问拆解、选择通用模型、生成 `result.json` 和图表。它通常能回答题目，但假设比较粗，指标之间的连接也不够强。

对这题来说，baseline 更像“第一版计算草稿”：可以帮助确认输入、输出和基本量纲，但还不足以支撑 O 奖级别的论证。

## Advanced：把题目机制接进模型

Advanced 的进步是：网格化空间评价、冲突风险、经济收益和情景比较。

这一层通常已经能进入课程讲解，因为它开始把题目约束、官方数据、逐问任务和可复现代码接起来。相比 baseline，它更像一篇可提交论文的骨架。

## Outstanding：把模型链做完整

选用的 O 奖论文是 `2315379`，标题为 `Build a common paradise for humans and wildlife in the Maasai Mara`。

它的核心升级是：36 网格功能区划、Dijkstra 交互距离和三种经济情景收益，使保护区规划从“打分”升级为“空间可执行方案”。

当前复现的关键对齐指标如下：

| 指标 | 复现值 | 论文目标 | 误差/说明 |
|---|---:|---:|---|
| `scenario2_benefit_million` | 154948.974 | 154948.974 | abs 0.0, rel 0.0% |
| `scenario2_wildlife_cells` | 13.0 | 13.0 | abs 0.0, rel 0.0% |
| `scenario2_tourism_cells` | 9.0 | 9.0 | abs 0.0, rel 0.0% |
| `scenario2_hunting_cells` | 2.0 | 2.0 | abs 0.0, rel 0.0% |
| `scenario2_agriculture_cells` | 12 | 13 in OCR, but 13+13+2+9 exceeds 36; grid-feasible reproduction uses 12 |  |

## 谁做得最好

| 层级 | 能力 | 主要短板 |
|---|---|---|
| Baseline | 能快速产出逐问结果和基本图表 | 假设、指标和验证还比较模板化 |
| Advanced | 题目机制更清楚，代码和结果更可复现 | 论文级证据链、灵敏度/稳定性和表达还可以加强 |
| Outstanding | 模型、数据、结果、检验和结论形成闭环 | 复现时要区分官方数据、外部数据和论文校准参数 |

结论：这题最好的是 Outstanding，因为它不只是“算法更复杂”，而是把模型选择、约束、结果校验和可解释结论连起来。优化题前面要做状态估计和指标定义，后面要做情景比较。

## 可复现运行

单篇运行：

```bash
/opt/homebrew/bin/python3 Math-Modeling-BAO/mcm/outstanding_solutions/2023/B/2315379/solution.py
```

统一 runner 运行：

```bash
/opt/homebrew/bin/python3 Math-Modeling-BAO/tools/run_outstanding_reproductions.py mcm-2023-B-2315379
```
