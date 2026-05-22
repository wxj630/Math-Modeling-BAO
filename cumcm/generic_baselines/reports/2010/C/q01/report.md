# 2010-C 问题 1 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2010年 CUMCM C题：输油管的布置
- 问题：问题 1
- 原问：针对两炼油厂到铁路线距离和两炼油厂间距离的各种不同情形，提出你的设计方案。在方案设计时，若有共用管线，应考虑共用管线费用与非共用管线费用相同或不同的情形。

## 通用模型选择

- 模型：规划优化与资源配置（CH3：函数极值与规划模型）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md
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

- 通用代码：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2010/C/q01/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2010/C/q01/solution.py`
- 结果 JSON：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/results/2010/C/q01/result.json
- 实验报告：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/reports/2010/C/q01/report.md
- 实验产物：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/artifacts/2010/C/q01/experiment_table.csv

## 数据来源

- 类型：problem_statement
- 路径：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2010/C.md
- 说明：未找到可直接读取的数值附件，本问改用题目原文中的参数/表格数字生成实验结果。

## 核心结果

```json
{
  "method": "linear_programming",
  "success": true,
  "objective_max": 17.233648186482903,
  "decision": [
    4.530565,
    0.0,
    0.0,
    0.0
  ],
  "resource_slack": [
    3.068588,
    0.0,
    0.288192
  ]
}
```
