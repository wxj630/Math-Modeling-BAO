# 2019-B 问题 3 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2019年 CUMCM B题：同心协力”策略研究
- 问题：问题 3
- 原问：在现实情形中，根据问题 2 的模型，你们在问题 1 中给出的策略是否需 要调整？如果需要，如何调整？

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

- 通用代码：cumcm/generic_baselines/solutions/2019/B/q03/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2019/B/q03/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2019/B/q03/result.json
- 实验报告：cumcm/generic_baselines/reports/2019/B/q03/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2019/B/q03/experiment_table.csv

## 数据来源

- 类型：problem_statement
- 路径：cumcm/problems/2019/B.md
- 说明：未找到可直接读取的数值附件，本问改用题目原文中的参数/表格数字生成实验结果。

## 核心结果

```json
{
  "method": "linear_programming",
  "success": true,
  "objective_max": 3.921667972717475,
  "decision": [
    0.0,
    0.0,
    2.329794,
    0.0
  ],
  "resource_slack": [
    171.444141,
    0.0,
    0.503437
  ]
}
```
