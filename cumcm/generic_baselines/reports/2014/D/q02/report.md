# 2014-D 问题 2 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2014年 CUMCM D题：储药柜的设计
- 问题：问题 2
- 原问：药盒与两侧竖向隔板之间的间隙超出2mm的部分可视为宽度冗余。增加竖向隔板的间距类型数量可以有效地减少宽度冗余，但会增加储药柜的加工成本，同时降低了储药槽的适应能力。设计时希望总宽度冗余尽可能小，同时也希望间距的类型数量尽可能少。仍利用附件1的数据，给出合理的竖向隔板间距类型的数量以及每种类型对应的药品编号。

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

- 通用代码：cumcm/generic_baselines/solutions/2014/D/q02/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2014/D/q02/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2014/D/q02/result.json
- 实验报告：cumcm/generic_baselines/reports/2014/D/q02/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2014/D/q02/experiment_table.csv

## 数据来源

- 类型：problem_statement
- 路径：cumcm/problems/2014/D.md
- 说明：未找到可直接读取的数值附件，本问改用题目原文中的参数/表格数字生成实验结果。

## 核心结果

```json
{
  "method": "linear_programming",
  "success": true,
  "objective_max": 13.950379852239479,
  "decision": [
    0.0,
    0.0,
    0.0,
    2.41537
  ],
  "resource_slack": [
    213.20992,
    0.0,
    0.527923
  ]
}
```
