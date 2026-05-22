# 2023-D 问题 2 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2023年 CUMCM D题：圈养湖羊的空间利用率
- 问题：问题 2
- 原问：在问题 1 的基础上，对 112 个标准羊栏给出具体的生产计划（包括种公羊与基础 母羊的配种时机和数量、羊栏的使用方案、年化出栏羊只数量等），使得年化出栏羊只数量最 大。

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

- 通用代码：cumcm/generic_baselines/solutions/2023/D/q02/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2023/D/q02/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2023/D/q02/result.json
- 实验报告：cumcm/generic_baselines/reports/2023/D/q02/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2023/D/q02/experiment_table.csv

## 数据来源

- 类型：problem_statement
- 路径：cumcm/problems/2023/D.md
- 说明：未找到可直接读取的数值附件，本问改用题目原文中的参数/表格数字生成实验结果。

## 核心结果

```json
{
  "method": "linear_programming",
  "success": true,
  "objective_max": 4.3424927198318475,
  "decision": [
    0.0,
    0.0,
    2.179714,
    0.0
  ],
  "resource_slack": [
    158.989836,
    0.0,
    0.529588
  ]
}
```
