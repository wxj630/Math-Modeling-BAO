# 2023-B 问题3 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2023年 CUMCM B题：多波束测线问题
- 问题：问题3
- 原问：考虑一个南北长2 海里、东西宽4 海里的矩形海域内，海域中心点处的海水深度 为110 m，西深东浅，坡度为 1.5∘，多波束换能器的开角为 120∘。请设计一组测量长度最短、 可完全覆盖整个待测海域的测线，且相邻条带之间的重叠率满足 10%~20% 的要求。

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

- 通用代码：cumcm/generic_baselines/solutions/2023/B/q03/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2023/B/q03/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2023/B/q03/result.json
- 实验报告：cumcm/generic_baselines/reports/2023/B/q03/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2023/B/q03/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：../../Documents/Playground/cumcm_unzipped/2023_Y20WPner9fa62862794e6dc82731a5561ce1132f/B题/result1.xlsx
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "linear_programming",
  "success": true,
  "objective_max": 29.814529194667156,
  "decision": [
    0.0,
    0.652559,
    0.133506,
    0.0,
    2.355178,
    0.0
  ],
  "resource_slack": [
    0.0,
    0.0,
    0.0
  ]
}
```
