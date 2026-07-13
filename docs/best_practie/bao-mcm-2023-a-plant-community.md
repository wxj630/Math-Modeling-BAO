# MCM 2023-A 干旱植物群落：Baseline → Advanced → Outstanding 进阶

这道题的主入口是 **动态系统/生态微分方程**。从教程角度看，baseline 解决“能跑通”，advanced 解决“更贴题”，Outstanding 解决“证据链完整、结果可检验、表达能让评委快速相信”。

## 材料入口

| 层级 | PDF | 代码 | 结果 |
|---|---|---|---|
| Baseline | `Math-Modeling-BAO-Reports/mcm/2023-A/baseline/main.pdf` | `Math-Modeling-BAO/mcm/generic_baselines/solutions/2023/A` | `Math-Modeling-BAO/mcm/generic_baselines/results/2023/A` |
| Advanced | `Math-Modeling-BAO-Reports/mcm/2023-A/advanced/main.pdf` | `Math-Modeling-BAO/docs/mcm-2015-2025/real_solutions/2023/MCM-A/solution.py` | `Math-Modeling-BAO/docs/mcm-2015-2025/real_solutions/2023/MCM-A/result.json` |
| Outstanding | `Math-Modeling-BAO-Reports/outstanding/mcm/2023-A/2309229/pdf/2309229.pdf` | `Math-Modeling-BAO/mcm/outstanding_solutions/2023/A/2309229/solution.py` | `Math-Modeling-BAO/mcm/outstanding_solutions/2023/A/2309229/result.json` |

OCR 文本：`Math-Modeling-BAO-Reports/outstanding/mcm/2023-A/2309229/ocr/2309229.md`。

## 数据来源

本题复现使用的数据/参数入口如下：

- `paper-reported GIID targets`
- `paper-reported sensitivity and habitat-capacity settings`


## Baseline：先把题跑通

Baseline 的价值是建立最小可运行闭环：逐问拆解、选择通用模型、生成 `result.json` 和图表。它通常能回答题目，但假设比较粗，指标之间的连接也不够强。

对这题来说，baseline 更像“第一版计算草稿”：可以帮助确认输入、输出和基本量纲，但还不足以支撑 O 奖级别的论证。

## Advanced：把题目机制接进模型

Advanced 的进步是：多物种差分方程、干旱压力、互补促进项和敏感性分析。

这一层通常已经能进入课程讲解，因为它开始把题目约束、官方数据、逐问任务和可复现代码接起来。相比 baseline，它更像一篇可提交论文的骨架。

## Outstanding：把模型链做完整

选用的 O 奖论文是 `2309229`，标题为 `The Warriors against Drought: Plant Communities`。

它的核心升级是：GIID 风格群落动力学，把 Lotka-Volterra、土壤水分、物种多样性、干旱情景和 beta 灵敏度连成一条证据链。

当前复现的关键对齐指标如下：

| 指标 | 复现值 | 论文目标 | 误差/说明 |
|---|---:|---:|---|
| `optimal_species_count` | 2.0 | 2.0 | abs 0.0, rel 0.0% |
| `five_species_pielou_evenness` | 0.8826 | 0.87 | abs 0.0126, rel 1.4483% |
| `beta_decline_pct` | 32.0 | 32.0 | abs 0.0, rel 0.0% |
| `cov_decrease_1_to_5` | 0.1211 | positive |  |

## 谁做得最好

| 层级 | 能力 | 主要短板 |
|---|---|---|
| Baseline | 能快速产出逐问结果和基本图表 | 假设、指标和验证还比较模板化 |
| Advanced | 题目机制更清楚，代码和结果更可复现 | 论文级证据链、灵敏度/稳定性和表达还可以加强 |
| Outstanding | 模型、数据、结果、检验和结论形成闭环 | 复现时要区分官方数据、外部数据和论文校准参数 |

结论：这题最好的是 Outstanding，因为它不只是“算法更复杂”，而是把模型选择、约束、结果校验和可解释结论连起来。动态题不是只写方程，后面一定要接稳定性、灵敏度和管理解释。

## 可复现运行

单篇运行：

```bash
/opt/homebrew/bin/python3 Math-Modeling-BAO/mcm/outstanding_solutions/2023/A/2309229/solution.py
```

统一 runner 运行：

```bash
/opt/homebrew/bin/python3 Math-Modeling-BAO/tools/run_outstanding_reproductions.py mcm-2023-A-2309229
```
