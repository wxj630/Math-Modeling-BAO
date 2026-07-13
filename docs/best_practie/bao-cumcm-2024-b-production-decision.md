# CUMCM 2024-B 生产过程决策优化：Baseline → Advanced → Outstanding 进阶

这道题的主入口是 **运筹优化/抽检决策**。从教程角度看，baseline 解决“能跑通”，advanced 解决“更贴题”，Outstanding 解决“证据链完整、结果可检验、表达能让评委快速相信”。

## 材料入口

| 层级 | PDF | 代码 | 结果 |
|---|---|---|---|
| Baseline | `Math-Modeling-BAO-Reports/cumcm/2024-B/baseline/main.pdf` | `Math-Modeling-BAO/cumcm/generic_baselines/solutions/2024/B` | `Math-Modeling-BAO/cumcm/generic_baselines/results/2024/B` |
| Advanced | `Math-Modeling-BAO-Reports/cumcm/2024-B/advanced/main.pdf` | `Math-Modeling-BAO/cumcm/question_solutions/2024/B` | `Math-Modeling-BAO/cumcm/question_results/2024/B` |
| Outstanding | `Math-Modeling-BAO-Reports/outstanding/cumcm/2024-B/B159/pdf/B159.pdf` | `Math-Modeling-BAO/cumcm/outstanding_solutions/2024/B/B159/solution.py` | `Math-Modeling-BAO/cumcm/outstanding_solutions/2024/B/B159/result.json` |

OCR 文本：`Math-Modeling-BAO-Reports/outstanding/cumcm/2024-B/B159/ocr/B159.md`。

## 数据来源

本题复现使用的数据/参数入口如下：

- `result.json 未声明额外数据源；请查看脚本内 DATA_FILE/PAPER_SOURCE 常量。`

## Baseline：先把题跑通

Baseline 的价值是建立最小可运行闭环：逐问拆解、选择通用模型、生成 `result.json` 和图表。它通常能回答题目，但假设比较粗，指标之间的连接也不够强。

对这题来说，baseline 更像“第一版计算草稿”：可以帮助确认输入、输出和基本量纲，但还不足以支撑 O 奖级别的论证。

## Advanced：把题目机制接进模型

Advanced 的进步是：抽样检验、次品率估计、返工/拆解决策和期望成本比较。

这一层通常已经能进入课程讲解，因为它开始把题目约束、官方数据、逐问任务和可复现代码接起来。相比 baseline，它更像一篇可提交论文的骨架。

## Outstanding：把模型链做完整

选用的 O 奖论文是 `B159`，标题为 `生产过程中的决策优化设计`。

它的核心升级是：把检测误差、生产阶段、拆解返工和利润风险放在统一决策树/优化框架下。

当前复现的关键对齐指标如下：

| 指标 | 复现值 | 论文目标 | 误差/说明 |
|---|---:|---:|---|
| `experiment_result.q1_sampling[0].mode` | reject_high | 见 O 论文表格/OCR | 旧脚本未声明 target_comparison；此处列 result.json 核心输出 |
| `experiment_result.q1_sampling[0].n` | 270 | 见 O 论文表格/OCR | 旧脚本未声明 target_comparison；此处列 result.json 核心输出 |
| `experiment_result.q1_sampling[0].c` | 36 | 见 O 论文表格/OCR | 旧脚本未声明 target_comparison；此处列 result.json 核心输出 |
| `experiment_result.q1_sampling[0].false_alarm` | 0.046596 | 见 O 论文表格/OCR | 旧脚本未声明 target_comparison；此处列 result.json 核心输出 |
| `experiment_result.q1_sampling[0].power` | 0.801472 | 见 O 论文表格/OCR | 旧脚本未声明 target_comparison；此处列 result.json 核心输出 |
| `experiment_result.q2.enumerated_decisions` | 96 | 见 O 论文表格/OCR | 旧脚本未声明 target_comparison；此处列 result.json 核心输出 |

## 谁做得最好

| 层级 | 能力 | 主要短板 |
|---|---|---|
| Baseline | 能快速产出逐问结果和基本图表 | 假设、指标和验证还比较模板化 |
| Advanced | 题目机制更清楚，代码和结果更可复现 | 论文级证据链、灵敏度/稳定性和表达还可以加强 |
| Outstanding | 模型、数据、结果、检验和结论形成闭环 | 复现时要区分官方数据、外部数据和论文校准参数 |

结论：这题最好的是 Outstanding，因为它不只是“算法更复杂”，而是把模型选择、约束、结果校验和可解释结论连起来。优化题的关键是把不确定性估计接到决策成本，而不是只解一个静态最优。

## 可复现运行

单篇运行：

```bash
/opt/homebrew/bin/python3 Math-Modeling-BAO/cumcm/outstanding_solutions/2024/B/B159/solution.py
```

统一 runner 运行：

```bash
/opt/homebrew/bin/python3 Math-Modeling-BAO/tools/run_outstanding_reproductions.py cumcm-2024-B-B159
```
