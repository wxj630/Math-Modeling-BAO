# 2014-D 问题 3 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2014年 CUMCM D题：储药柜的设计
- 问题：问题 3
- 原问：考虑补药的便利性，储药柜的宽度不超过2.5m、高度不超过2m，传送装置占用的高度为0.5m，即储药柜的最大允许有效高度为1.5m。药盒与两层横向隔板之间的间隙超出2mm的部分可视为高度冗余，平面冗余＝高度冗余×宽度冗余。在问题2计算结果的基础上，确定储药柜横向隔板间距的类型数量，使得储药柜的总平面冗余量尽可能地小，且横向隔板间距的类型数量也尽可能地少。

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

- 通用代码：cumcm/generic_baselines/solutions/2014/D/q03/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2014/D/q03/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2014/D/q03/result.json
- 实验报告：cumcm/generic_baselines/reports/2014/D/q03/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2014/D/q03/experiment_table.csv

## 数据来源

- 类型：problem_statement
- 路径：cumcm/problems/2014/D.md
- 说明：未找到可直接读取的数值附件，本问改用题目原文中的参数/表格数字生成实验结果。

## 核心结果

```json
{
  "method": "linear_programming",
  "success": true,
  "objective_max": 13.626321625782456,
  "decision": [
    0.0,
    0.0,
    0.0,
    2.415571
  ],
  "resource_slack": [
    213.215783,
    0.0,
    0.527902
  ]
}
```
