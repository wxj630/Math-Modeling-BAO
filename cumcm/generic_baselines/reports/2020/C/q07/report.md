# 2020-C 问题 4 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2020年 CUMCM C题：中小微企业的信贷决策
- 问题：问题 4
- 原问：作废发票：在为交易活动开具发票后，因故取消了该项交易，使发票作废。

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

- 通用代码：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2020/C/q07/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2020/C/q07/solution.py`
- 结果 JSON：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/results/2020/C/q07/result.json
- 实验报告：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/reports/2020/C/q07/report.md
- 实验产物：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/artifacts/2020/C/q07/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/C/附件1：123家有信贷记录企业的相关数据.xlsx
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "quadratic_least_squares",
  "coefficients": [
    2.421039,
    81512.384259,
    -1.209879
  ],
  "r2": 0.22716636061610596,
  "mean_abs_error": 4229597.817632965
}
```
