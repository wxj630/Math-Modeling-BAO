# 2020-B 问题 3 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2020年 CUMCM B题：穿越沙漠
- 问题：问题 3
- 原问：现有名玩家，他们有相同的初始资金，且同时从起点出发。若某天其中的任意名玩家均从区域A行走到区域B()，则他们中的任一位消耗的资源数量均为基础消耗量的倍；若某天其中的任意名玩家在同一矿山挖矿，则他们中的任一位消耗的资源数量均为基础消耗量的倍，且每名玩家一天可通过挖矿获得的资金是基础收益的；若某天其中的任意名玩家在同一村庄购买资源，每箱价格均为基准价格的倍。其他情况下消耗资源数量与资源价格与单人游戏相同。

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

- 通用代码：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2020/B/q11/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2020/B/q11/solution.py`
- 结果 JSON：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/results/2020/B/q11/result.json
- 实验报告：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/reports/2020/B/q11/report.md
- 实验产物：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/artifacts/2020/B/q11/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/B/Result.xlsx
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "linear_programming",
  "success": true,
  "objective_max": 34.24700461469823,
  "decision": [
    0.0,
    0.0,
    0.0,
    4.407576
  ],
  "resource_slack": [
    8.530946,
    0.0,
    0.511818
  ]
}
```
