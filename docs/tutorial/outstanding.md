# Outstanding Solution

Outstanding solution 是预留给后续继续打磨的位置。它不是简单把 advanced solution 写得更长，而是把“能跑、能解释”的解法升级成“更可信、更漂亮、更像高质量竞赛论文”的完整作品。

## 建议目录

后续可以在仓库中新增：

```text
mcm/outstanding_solutions/
cumcm/outstanding_solutions/
```

每个 outstanding 解法建议保留和现有归档一致的结构：

```text
outstanding_solutions/<year>/<code>/qXX/
  solution.py
  result.json
  report.md
  paper_outline.md
  artifacts/
```

这样它可以继续和 baseline、advanced 一一对照。

## 进入 outstanding 前的检查

一个 advanced solution 值得升级时，通常已经满足：

- 数据源清楚：官方附件、题面参数、外部公开数据的边界写清楚。
- 模型链完整：变量、约束、目标、求解方法和解释能闭环。
- 结果稳定：至少有基本敏感性分析或参数扰动。
- 产物可用：图、表、JSON、Excel 或备忘录能支撑论文正文。

## Outstanding 要补什么

| 方向 | 要做的增强 |
|---|---|
| 算法 | 从启发式、贪心、固定权重升级到更可解释的优化、统计验证、仿真或组合模型。 |
| 鲁棒性 | 加入参数敏感性、交叉验证、留出评估、置信区间、极端情景或误差传播。 |
| 论文表达 | 形成摘要、模型假设、符号表、模型建立、求解过程、结果分析、优缺点和改进方向。 |
| 可视化 | 用一到三张关键图讲清主结果，不堆图，不让表格淹没结论。 |
| 审计 | 明确哪些结论来自官方数据，哪些来自假设，哪些只是情景分析。 |

## 教程中的预留位

当前教程先把 outstanding 的标准和目录留出来。后续补写某道题时，可以在对应案例页追加“Outstanding 解法”小节，并把链接接到新的 `outstanding_solutions/` 目录。
