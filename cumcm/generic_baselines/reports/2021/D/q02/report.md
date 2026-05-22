# 2021-D 问题 2 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2021年 CUMCM D题：连铸切割的
- 问题：问题 2
- 原问：在结晶器出现异常时，给出实时的最优切割方案：(1)在钢坯第 1 次出现报废段时，给出此段钢坯的切割方案；(2)在出现新的报废段后 （如图2）， 给出新一段钢坯的切割方案和当前段钢坯切割的调整方案，或声明不作调整。 假设结晶器出现异常的时刻在 0.0、45.6、98.6、131.5、190.8、233.3、 266.0、270.7 和327.9（单位：分钟） ， 用户目标值是9.5 米， 目标范围是9.0~10.0 米。在满足基本要求和正常要求的条件下， 按 “初始切割方案、 调整后的切割方 案、切割损失”等内容列表给出这些时刻具体的最优切割方案。

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

- 通用代码：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2021/D/q02/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2021/D/q02/solution.py`
- 结果 JSON：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/results/2021/D/q02/result.json
- 实验报告：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/reports/2021/D/q02/report.md
- 实验产物：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/artifacts/2021/D/q02/experiment_table.csv

## 数据来源

- 类型：problem_statement
- 路径：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2021/D.md
- 说明：未找到可直接读取的数值附件，本问改用题目原文中的参数/表格数字生成实验结果。

## 核心结果

```json
{
  "method": "linear_programming",
  "success": true,
  "objective_max": 4.653651627935094,
  "decision": [
    0.0,
    0.0,
    0.0,
    2.327846
  ],
  "resource_slack": [
    213.044773,
    0.0,
    0.583951
  ]
}
```
