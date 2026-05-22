# Outstanding Solution

Outstanding solution 是按“整道赛题”打磨出来的论文级版本。它不是把每个小问单独加长，而是让整题主线更可信、更漂亮、更像高质量竞赛论文。

## 建议目录

后续可以在仓库中新增：

```text
mcm/outstanding_solutions/
cumcm/outstanding_solutions/
```

建议按赛题组织，而不是只按小问散放：

```text
outstanding_solutions/<year>/<code>/
  paper_outline.md
  assumptions.md
  sensitivity.md
  figures/
  q01/
  q02/
  ...
```

每个 `qXX/` 可以继续保留 `solution.py`、`result.json`、`report.md` 和 artifacts，但赛题级文件要负责统一假设、符号、图表风格和论文叙事。

## 进入 outstanding 前的检查

一个赛题值得升级时，通常已经满足：

- 主线清楚：每一问知道自己继承和推进了什么。
- 数据源清楚：官方附件、题面参数、外部公开数据的边界写清楚。
- 模型链完整：变量、约束、目标、求解方法和解释能闭环。
- 结果稳定：至少有基本敏感性分析或参数扰动。
- 产物可用：图、表、JSON、Excel 或备忘录能支撑论文正文。

## Outstanding 要补什么

| 方向 | 要做的增强 |
|---|---|
| 整题叙事 | 把小问串成“问题背景 -> 主模型 -> 扩展 -> 验证 -> 决策建议”的论文结构。 |
| 算法 | 从启发式、贪心、固定权重升级到更可解释的优化、统计验证、仿真或组合模型。 |
| 鲁棒性 | 加入参数敏感性、交叉验证、留出评估、置信区间、极端情景或误差传播。 |
| 可视化 | 用一到三张关键图讲清主结果，不堆图，不让表格淹没结论。 |
| 审计 | 明确哪些结论来自官方数据，哪些来自假设，哪些只是情景分析。 |

## 教程中的预留位

每个赛题页的小问都会保留 outstanding 位置。后续补写某道题时，优先补赛题级 `paper_outline.md` 和统一假设，再补各小问的算法与图表。
