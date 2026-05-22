# Baseline Solution

Baseline solution 是每一问的第一版可运行模型。它的目标不是拿奖，而是把题目从自然语言推进到一套可执行的变量、约束、目标函数、结果文件和报告结构。

## 为什么需要 baseline

数学建模最容易卡在“还没想清楚，所以还不能写代码”。Baseline 反过来做：先用透明、朴素、可审计的模型把问题跑通，再把不足暴露出来。

一个合格 baseline 应该做到：

- 能独立运行 `solution.py`。
- 能输出 `result.json` 和至少一份表格或报告。
- 明确说明模型选择、变量含义、约束来源和数据来源。
- 不把通用模型包装成最终竞赛级结论。
- 为 advanced solution 留出清晰的升级方向。

## MCM 的 baseline

MCM/ICM 的通用基线位于：

```text
mcm/generic_baselines/
```

当前方法族包括 `linear_weighted_score_baseline`、`report_outline_baseline`、`network_path_baseline`、`resource_allocation_baseline`、`first_order_dynamic_baseline`、`linear_trend_forecast_baseline` 等。它们会根据小问文本、方法关键词、数据来源和产物就绪度，生成最低可运行脚手架。

典型文件：

```text
mcm/generic_baselines/solutions/2024/C/q01/solution.py
mcm/generic_baselines/results/2024/C/q01/result.json
mcm/generic_baselines/reports/2024/C/q01/report.md
mcm/generic_baselines/artifacts/2024/C/q01/experiment_table.csv
```

## CUMCM 的 baseline

CUMCM 的通用基线位于：

```text
cumcm/generic_baselines/
```

当前方法族包括 `linear_programming`、`quadratic_least_squares`、`least_squares_geometry_fit`、`linear_trend_forecast`、`first_order_dynamic_simulation`、`dijkstra_shortest_path`、`std_weight_topsis` 等。它更像传统数模课堂里的“经典模型入口”：规划、最小二乘、路径、评价、预测、抽样。

典型文件：

```text
cumcm/generic_baselines/solutions/2024/C/q01/solution.py
cumcm/generic_baselines/results/2024/C/q01/result.json
cumcm/generic_baselines/reports/2024/C/q01/report.md
cumcm/generic_baselines/artifacts/2024/C/q01/experiment_table.csv
```

## 阅读 baseline 的方法

1. 先读 `report.md`，只看模型选择、变量、约束、公式和限制。
2. 再读 `result.json`，确认结果字段是否能支撑论文表格。
3. 打开 `solution.py`，看数据读取和模型求解是否仍是通用模板。
4. 对照 advanced solution，标出三类差距：数据差距、约束差距、论文表达差距。

Baseline 的价值在于给 advanced 解法提供对照组。保留它，后续复盘时才能看见模型是怎样一步步变强的。
