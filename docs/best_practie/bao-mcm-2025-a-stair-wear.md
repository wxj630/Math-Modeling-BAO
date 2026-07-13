# MCM 2025-A 楼梯磨损历史反演：Baseline → Advanced → Outstanding 进阶

这道题的主入口是 **物理反演/动态磨损**。从教程角度看，baseline 解决“能跑通”，advanced 解决“更贴题”，Outstanding 解决“证据链完整、结果可检验、表达能让评委快速相信”。

## 材料入口

| 层级 | PDF | 代码 | 结果 |
|---|---|---|---|
| Baseline | `Math-Modeling-BAO-Reports/mcm/2025-A/baseline/main.pdf` | `Math-Modeling-BAO/mcm/generic_baselines/solutions/2025/A` | `Math-Modeling-BAO/mcm/generic_baselines/results/2025/A` |
| Advanced | `Math-Modeling-BAO-Reports/mcm/2025-A/advanced/main.pdf` | `Math-Modeling-BAO/docs/mcm-2015-2025/real_solutions/2025/MCM-A/solution.py` | `Math-Modeling-BAO/docs/mcm-2015-2025/real_solutions/2025/MCM-A/result.json` |
| Outstanding | `Math-Modeling-BAO-Reports/outstanding/mcm/2025-A/2501909/pdf/2501909.pdf` | `Math-Modeling-BAO/mcm/outstanding_solutions/2025/A/2501909/solution.py` | `Math-Modeling-BAO/mcm/outstanding_solutions/2025/A/2501909/result.json` |

OCR 文本：`Math-Modeling-BAO-Reports/outstanding/mcm/2025-A/2501909/ocr/2501909.md`。

## 数据来源

本题复现使用的数据/参数入口如下：

- `type: official_statement_plus_explicit_worked_measurement_sheet`
- `source_pdf: docs/mcm-2015-2025/official_assets_extracted/2025/2025_MCM_Problem_A.pdf`
- `note: MCM 2025-A has no numeric attachment; the worked sheet is transparent demonstration data generated in this script.`

## Baseline：先把题跑通

Baseline 的价值是建立最小可运行闭环：逐问拆解、选择通用模型、生成 `result.json` 和图表。它通常能回答题目，但假设比较粗，指标之间的连接也不够强。

对这题来说，baseline 更像“第一版计算草稿”：可以帮助确认输入、输出和基本量纲，但还不足以支撑 O 奖级别的论证。

## Advanced：把题目机制接进模型

Advanced 的进步是：磨损几何、交通强度、年龄反演和不确定性网格。

这一层通常已经能进入课程讲解，因为它开始把题目约束、官方数据、逐问任务和可复现代码接起来。相比 baseline，它更像一篇可提交论文的骨架。

## Outstanding：把模型链做完整

选用的 O 奖论文是 `2501909`，标题为 `Stair Wear: Traces of History`。

它的核心升级是：WVM/WDM 把非破坏测量、磨损体积、横向分布、方向识别和修复检测连成工作流。

当前复现的关键对齐指标如下：

| 指标 | 复现值 | 论文目标 | 误差/说明 |
|---|---:|---:|---|
| `experiment_result.median_center_wear_depth_mm` | 4.35 | 见 O 论文表格/OCR | 旧脚本未声明 target_comparison；此处列 result.json 核心输出 |
| `experiment_result.estimated_passages_per_tread` | 9666667 | 见 O 论文表格/OCR | 旧脚本未声明 target_comparison；此处列 result.json 核心输出 |
| `experiment_result.estimated_daily_users` | 73.52 | 见 O 论文表格/OCR | 旧脚本未声明 target_comparison；此处列 result.json 核心输出 |
| `experiment_result.favored_direction` | up | 见 O 论文表格/OCR | 旧脚本未声明 target_comparison；此处列 result.json 核心输出 |
| `experiment_result.simultaneous_pattern` | mixed | 见 O 论文表格/OCR | 旧脚本未声明 target_comparison；此处列 result.json 核心输出 |
| `experiment_result.lateral_centroid` | -0.0261 | 见 O 论文表格/OCR | 旧脚本未声明 target_comparison；此处列 result.json 核心输出 |

## 谁做得最好

| 层级 | 能力 | 主要短板 |
|---|---|---|
| Baseline | 能快速产出逐问结果和基本图表 | 假设、指标和验证还比较模板化 |
| Advanced | 题目机制更清楚，代码和结果更可复现 | 论文级证据链、灵敏度/稳定性和表达还可以加强 |
| Outstanding | 模型、数据、结果、检验和结论形成闭环 | 复现时要区分官方数据、外部数据和论文校准参数 |

结论：这题最好的是 Outstanding，因为它不只是“算法更复杂”，而是把模型选择、约束、结果校验和可解释结论连起来。物理题要说明测什么、怎么反推、哪些参数不确定。

## 可复现运行

单篇运行：

```bash
/opt/homebrew/bin/python3 Math-Modeling-BAO/mcm/outstanding_solutions/2025/A/2501909/solution.py
```

统一 runner 运行：

```bash
/opt/homebrew/bin/python3 Math-Modeling-BAO/tools/run_outstanding_reproductions.py mcm-2025-A-2501909
```
