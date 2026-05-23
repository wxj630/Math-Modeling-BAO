# 2019-A 问题3 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2019年 CUMCM A题：高压油管的压力控制
- 问题：问题3
- 原问：在问题2的基础上，再增加一个喷油嘴，每个喷嘴喷油规律相同，喷油和供油策略应如何调整？为了更有效地控制高压油管的压力，现计划在D处安装一个单向减压阀（图5）。单向减压阀出口为直径为1.4mm的圆，打开后高压油管内的燃油可以在压力下回流到外部低压油路中，从而使得高压油管内燃油的压力减小。请给出高压油泵和减压阀的控制方案。

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

- 通用代码：cumcm/generic_baselines/solutions/2019/A/q03/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2019/A/q03/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2019/A/q03/result.json
- 实验报告：cumcm/generic_baselines/reports/2019/A/q03/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2019/A/q03/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：../../Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/A-2019中文/附件1-凸轮边缘曲线.xlsx
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "linear_programming",
  "success": true,
  "objective_max": 27.650710618753237,
  "decision": [
    0.198238,
    0.0,
    1.802039,
    0.0,
    1.25728,
    0.0
  ],
  "resource_slack": [
    0.0,
    0.0,
    0.0
  ]
}
```
