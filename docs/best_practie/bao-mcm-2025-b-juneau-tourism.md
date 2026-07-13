# MCM 2025-B Juneau 可持续旅游：Baseline → Advanced → Outstanding 进阶

这道题的主入口是 **运筹优化/可持续旅游**。从教程角度看，baseline 解决“能跑通”，advanced 解决“更贴题”，Outstanding 解决“证据链完整、结果可检验、表达能让评委快速相信”。

## 材料入口

| 层级 | PDF | 代码 | 结果 |
|---|---|---|---|
| Baseline | `Math-Modeling-BAO-Reports/mcm/2025-B/baseline/main.pdf` | `Math-Modeling-BAO/mcm/generic_baselines/solutions/2025/B` | `Math-Modeling-BAO/mcm/generic_baselines/results/2025/B` |
| Advanced | `Math-Modeling-BAO-Reports/mcm/2025-B/advanced/main.pdf` | `Math-Modeling-BAO/docs/mcm-2015-2025/real_solutions/2025/MCM-B/solution.py` | `Math-Modeling-BAO/docs/mcm-2015-2025/real_solutions/2025/MCM-B/result.json` |
| Outstanding | `Math-Modeling-BAO-Reports/outstanding/mcm/2025-B/2504448/pdf/2504448.pdf` | `Math-Modeling-BAO/mcm/outstanding_solutions/2025/B/2504448/solution.py` | `Math-Modeling-BAO/mcm/outstanding_solutions/2025/B/2504448/result.json` |

OCR 文本：`Math-Modeling-BAO-Reports/outstanding/mcm/2025-B/2504448/ocr/2504448.md`。

## 数据来源

本题复现使用的数据/参数入口如下：

- `type: official_statement_parameters`
- `source_pdf: docs/mcm-2015-2025/official_assets_extracted/2025/2025_MCM_Problem_B.pdf`

## Baseline：先把题跑通

Baseline 的价值是建立最小可运行闭环：逐问拆解、选择通用模型、生成 `result.json` 和图表。它通常能回答题目，但假设比较粗，指标之间的连接也不够强。

对这题来说，baseline 更像“第一版计算草稿”：可以帮助确认输入、输出和基本量纲，但还不足以支撑 O 奖级别的论证。

## Advanced：把题目机制接进模型

Advanced 的进步是：游客流量、环境承载、居民满意度和政策情景优化。

这一层通常已经能进入课程讲解，因为它开始把题目约束、官方数据、逐问任务和可复现代码接起来。相比 baseline，它更像一篇可提交论文的骨架。

## Outstanding：把模型链做完整

选用的 O 奖论文是 `2504448`，标题为 `Sustainable Tourism Management in Juneau`。

它的核心升级是：动态政策网格把税费、客流、环境压力和居民收益连成可调政策前沿。

当前复现的关键对齐指标如下：

| 指标 | 复现值 | 论文目标 | 误差/说明 |
|---|---:|---:|---|
| `experiment_result.terminal_year` | 2028 | 见 O 论文表格/OCR | 旧脚本未声明 target_comparison；此处列 result.json 核心输出 |
| `experiment_result.optimal_daily_cap` | 11000 | 见 O 论文表格/OCR | 旧脚本未声明 target_comparison；此处列 result.json 核心输出 |
| `experiment_result.optimal_visitor_fee_usd` | 55.0 | 见 O 论文表格/OCR | 旧脚本未声明 target_comparison；此处列 result.json 核心输出 |
| `experiment_result.optimal_conservation_share` | 0.35 | 见 O 论文表格/OCR | 旧脚本未声明 target_comparison；此处列 result.json 核心输出 |
| `experiment_result.annual_visitors` | 1491526 | 见 O 论文表格/OCR | 旧脚本未声明 target_comparison；此处列 result.json 核心输出 |
| `experiment_result.total_revenue_usd` | 431610327.83 | 见 O 论文表格/OCR | 旧脚本未声明 target_comparison；此处列 result.json 核心输出 |

## 谁做得最好

| 层级 | 能力 | 主要短板 |
|---|---|---|
| Baseline | 能快速产出逐问结果和基本图表 | 假设、指标和验证还比较模板化 |
| Advanced | 题目机制更清楚，代码和结果更可复现 | 论文级证据链、灵敏度/稳定性和表达还可以加强 |
| Outstanding | 模型、数据、结果、检验和结论形成闭环 | 复现时要区分官方数据、外部数据和论文校准参数 |

结论：这题最好的是 Outstanding，因为它不只是“算法更复杂”，而是把模型选择、约束、结果校验和可解释结论连起来。优化题如果涉及政策，结果要能给出多目标取舍，而不是一个孤立最优数。

## 可复现运行

单篇运行：

```bash
/opt/homebrew/bin/python3 Math-Modeling-BAO/mcm/outstanding_solutions/2025/B/2504448/solution.py
```

统一 runner 运行：

```bash
/opt/homebrew/bin/python3 Math-Modeling-BAO/tools/run_outstanding_reproductions.py mcm-2025-B-2504448
```
