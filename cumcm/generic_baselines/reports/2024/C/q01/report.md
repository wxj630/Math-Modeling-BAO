# 2024-C 问题 1 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2024年 CUMCM C题：农作物的种植策略
- 问题：问题 1
- 原问：假定各种农作物未来的预期销售量、种植成本、亩产量和销售价格相对于 2023 年保持 稳定，每季种植的农作物在当季销售。如果某种作物每季的总产量超过相应的预期销售量，超过部 分不能正常销售。请针对以下两种情况，分别给出该乡村 2024~2030 年农作物的最优种植方案，将 结果分别填入 result1_1.xlsx 和 result1_2.xlsx 中（模板文件见附件 3）。 (1) 超过部分滞销，造成浪费； (2) 超过部分按 2023 年销售价格的 50%降价出售。

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

- 通用代码：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2024/C/q01/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2024/C/q01/solution.py`
- 结果 JSON：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/results/2024/C/q01/result.json
- 实验报告：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/reports/2024/C/q01/report.md
- 实验产物：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/artifacts/2024/C/q01/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/C题/附件1.xlsx
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "linear_programming",
  "success": true,
  "objective_max": 23.963979880339547,
  "decision": [
    0.0,
    0.0,
    0.0,
    1.569817
  ],
  "resource_slack": [
    44.996458,
    0.0,
    1.037074
  ]
}
```
