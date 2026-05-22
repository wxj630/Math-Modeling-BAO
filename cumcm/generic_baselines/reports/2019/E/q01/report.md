# 2019-E 问题 1 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2019年 CUMCM E题：薄利多销”分析
- 问题：问题 1
- 原问：计算该商场从2016年11月30日到2019年1月2日每天的营业额和利润率（注意：由于未知原因，数据中非打折商品的成本价缺失。一般情况下，零售商的利润率在20%-40%之间)

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

- 通用代码：cumcm/generic_baselines/solutions/2019/E/q01/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2019/E/q01/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2019/E/q01/result.json
- 实验报告：cumcm/generic_baselines/reports/2019/E/q01/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2019/E/q01/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：../../Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/E-2019中文/data/附件1.csv
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "linear_programming",
  "success": true,
  "objective_max": 30363.855305676116,
  "decision": [
    6.924218,
    0.0,
    0.0,
    0.0
  ],
  "resource_slack": [
    19891176592946.6,
    0.056619,
    0.0
  ]
}
```
