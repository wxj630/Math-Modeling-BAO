# 2010-C 问题 3 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2010年 CUMCM C题：输油管的布置
- 问题：问题 3
- 原问：在该实际问题中，为进一步节省费用，可以根据炼油厂的生产能力，选用相适应的油管。这时的管线铺设费用将分别降为输送A厂成品油的每千米5.6万元，输送B厂成品油的每千米6.0万元，共用管线费用为每千米7.2万元，拆迁等附加费用同上。请给出管线最佳布置方案及相应的费用。

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

- 通用代码：cumcm/generic_baselines/solutions/2010/C/q03/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2010/C/q03/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2010/C/q03/result.json
- 实验报告：cumcm/generic_baselines/reports/2010/C/q03/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2010/C/q03/experiment_table.csv

## 数据来源

- 类型：problem_statement
- 路径：cumcm/problems/2010/C.md
- 说明：未找到可直接读取的数值附件，本问改用题目原文中的参数/表格数字生成实验结果。

## 核心结果

```json
{
  "method": "linear_programming",
  "success": true,
  "objective_max": 15.87375089067293,
  "decision": [
    4.282361,
    0.0,
    0.0,
    0.0
  ],
  "resource_slack": [
    2.544028,
    0.0,
    0.350243
  ]
}
```
