# 2025-A 问题5 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2025年 CUMCM A题：烟幕干扰弹的投放策略
- 问题：问题5
- 原问：利用5 架无人机，每架无人机至多投放3 枚烟幕干扰弹，实施对M1、M2、M3 等3 枚来袭导弹的干扰。请给出烟幕干扰弹的投放策略，并将结果保存到文件result3.xlsx 中 （模板文件见附件）。

## 通用模型选择

- 模型：规划优化与资源配置（CH3：函数极值与规划模型）
- 教程参考：../My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md
- 通用方法：`linear_programming`

## 变量、约束与公式

### 变量定义
- x_i: 第 i 个方案/资源的选择强度
- c_i: 单位收益或效用
- A_ji: 第 j 类资源消耗
- b_j: 第 j 类资源上限

### 约束条件
- A x <= b
- x_i >= 0
- 资源容量按题面约束映射为 b_j

### 模型公式 / 目标函数
- `max sum_i c_i*x_i`
- `s.t. A*x <= b, x >= 0`

## 运行与产物

- 通用代码：cumcm/generic_baselines/solutions/2025/A/q05/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2025/A/q05/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2025/A/q05/result.json
- 实验报告：cumcm/generic_baselines/reports/2025/A/q05/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2025/A/q05/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/A题/附件/result1.xlsx
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "linear_programming",
  "success": true,
  "objective_max": 36.458463773857005,
  "decision": [
    1.102447,
    0.0,
    0.0,
    0.0,
    1.764316,
    0.466523
  ],
  "resource_slack": [
    0.0,
    0.0,
    0.0
  ]
}
```
