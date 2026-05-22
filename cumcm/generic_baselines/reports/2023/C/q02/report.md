# 2023-C 问题2 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2023年 CUMCM C题：蔬菜类商品的自动定价与补货决策
- 问题：问题2
- 原问：考虑商超以品类为单位做补货计划，请分析各蔬菜品类的销售总量与成本加成 定价的关系，并给出各蔬菜品类未来一周(2023 年7 月1-7 日)的日补货总量和定价策略， 使得商超收益最大。

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

- 通用代码：cumcm/generic_baselines/solutions/2023/C/q02/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2023/C/q02/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2023/C/q02/result.json
- 实验报告：cumcm/generic_baselines/reports/2023/C/q02/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2023/C/q02/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：../../Documents/Playground/cumcm_unzipped/2023_Y20WPner9fa62862794e6dc82731a5561ce1132f/C题/附件1.xlsx
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "linear_programming",
  "success": true,
  "objective_max": 5.7763291263739855,
  "decision": [
    1.474718,
    0.0,
    0.0,
    0.801792
  ],
  "resource_slack": [
    3.255199,
    0.0,
    0.0
  ]
}
```
