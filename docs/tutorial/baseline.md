# Baseline Solution

Baseline solution 是一道赛题的最低可运行起点。它不负责“拿奖”，而是快速回答：这道题大概属于哪类模型，变量和输出长什么样，哪些小问共享同一套主模型。

## 在赛题中的作用

一个好的 baseline 不应该只服务某个孤立小问。它应该帮助你看见整题骨架：

- 第 1 问通常给出主模型、数据入口或评价指标。
- 后续小问会把主模型推进到预测、优化、情景、敏感性或报告表达。
- Baseline 负责给每个小问留下可运行对照组，便于看出 advanced 到底升级了什么。

## 合格 baseline 的标准

- 能独立运行 `solution.py`。
- 能输出 `result.json`、`report.md` 和至少一份表格或实验产物。
- 明确说明模型选择、变量含义、约束来源和数据来源。
- 能指出它在整题链条中的位置：主模型、扩展、验证、情景还是报告。
- 不把通用模型包装成最终竞赛级结论。

## MCM/ICM 的 baseline

MCM/ICM 的通用基线位于：

```text
mcm/generic_baselines/
```

常见方法族包括 `linear_weighted_score_baseline`、`report_outline_baseline`、`network_path_baseline`、`resource_allocation_baseline`、`first_order_dynamic_baseline`、`linear_trend_forecast_baseline` 等。

在赛题页中，baseline 会作为每个小问的第一份材料出现，例如：

```text
mcm/generic_baselines/reports/2015/C/q01/report.md
mcm/generic_baselines/reports/2015/C/q02/report.md
```

这两个小问不能割裂读：`q01` 建立组织网络，`q02` 才能在这个网络上讨论流失动态。

## CUMCM 的 baseline

CUMCM 的通用基线位于：

```text
cumcm/generic_baselines/
```

常见方法族包括 `linear_programming`、`quadratic_least_squares`、`least_squares_geometry_fit`、`linear_trend_forecast`、`first_order_dynamic_simulation`、`dijkstra_shortest_path`、`std_weight_topsis` 等。

CUMCM 题更常见“附件解析 + 约束建模 + 提交模板”的链条。baseline 先保留经典模型入口，advanced 再把地块、季次、作物、价格、销量、模板格式等具体约束接进去。

## 阅读 baseline 的方法

1. 先进入某道赛题页，看这问在整题链条中的位置。
2. 读 baseline `report.md`，只看模型族、变量、目标和限制。
3. 再读 advanced `report.md`，标出新增的数据、约束和输出。
4. 最后回到整题层面判断：这个升级是否让后续小问更容易成立。
