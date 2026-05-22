# 2022-A 问题2 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2022年 CUMCM A题：波浪能最大输出功率设计
- 问题：问题2
- 原问：仍考虑浮子在波浪中只做垂荡运动，分别对以下两种情况建立确定直线阻尼器的 最优阻尼系数的数学模型，使得PTO 系统的平均输出功率最大：(1) 阻尼系数为常量，阻尼系 数在区间 [0,100000] 内取值；(2) 阻尼系数与浮子和振子的相对速度的绝对值的幂成正比，比 例系数在区间 [0,100000] 内取值，幂指数在区间 [0,1] 内取值。利用附件3 和附件4 提供的 参数值（波浪频率取2.2143 s−1）分别计算两种情况的最大输出功率及相应的最优阻尼系数。

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

- 通用代码：cumcm/generic_baselines/solutions/2022/A/q02/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2022/A/q02/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2022/A/q02/result.json
- 实验报告：cumcm/generic_baselines/reports/2022/A/q02/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2022/A/q02/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：../../Documents/Playground/cumcm_unzipped/2022_5eWlbmTt28f88a0815a79d555da8b7072f971633/A题/result1-1.xlsx
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "linear_programming",
  "success": true,
  "objective_max": 30.92026290094436,
  "decision": [
    0.0,
    0.0,
    0.434656,
    0.0,
    0.0,
    2.577869
  ],
  "resource_slack": [
    0.0,
    1.062366,
    0.0
  ]
}
```
