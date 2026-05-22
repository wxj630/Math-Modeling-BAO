# 2021-C 问题 1 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2021年 CUMCM C题：生产企业原材料的订购与运输
- 问题：问题 1
- 原问：企业的订货量：第一列为供应商的名称； 第二列为供应商供应原材料的类别； 第三列及以后共240 列为企业向各供应商每周的订货量 （单位： 立方米） ； 数值 “0”表 示相应的周（所在列）没有向供应商（所在行）订货。

## 通用模型选择

- 模型：数据拟合与回归分析（CH6：数据处理与拟合模型）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH6/第六章-数据处理与拟合模型.md
- 通用方法：`quadratic_least_squares`

## 变量、约束与公式

### 变量定义
- x: 题面影响因素或测量自变量
- y: 待解释/待标定指标
- beta: 回归参数
- epsilon: 随机误差

### 约束条件
- 样本点按题面数值范围或标准化区间构造
- 最小二乘残差平方和最小

### 模型公式 / 目标函数
- `min_beta sum_i (y_i - beta0 - beta1*x_i - beta2*x_i^2)^2`
- `R^2 = 1 - SSE/SST`

## 运行与产物

- 通用代码：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2021/C/q05/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2021/C/q05/solution.py`
- 结果 JSON：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/results/2021/C/q05/result.json
- 实验报告：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/reports/2021/C/q05/report.md
- 实验产物：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/artifacts/2021/C/q05/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/C/附件1 近5年402家供应商的相关数据.xlsx
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "quadratic_least_squares",
  "coefficients": [
    431.06556,
    -1.043377,
    0.001378
  ],
  "r2": 0.21977393216454688,
  "mean_abs_error": 9.080568558147373
}
```
