# 2021-E 问题 2 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2021年 CUMCM E题：中药材的鉴别
- 问题：问题 2
- 原问：根据附件 2 中某一种药材的中红外光谱数据，分析不同产地药材的 特征和差异性，试鉴别药材的产地，并将下表中所给出编号的药材产地的鉴别结 果填入表格中。 No 3 14 38 48 58 71 79 86 89 110 134 152 227 331 618 OP

## 通用模型选择

- 模型：数据拟合与回归分析（CH6：数据处理与拟合模型）
- 教程参考：../My-Agent/intro-mathmodel/docs/CH6/第六章-数据处理与拟合模型.md
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

- 通用代码：cumcm/generic_baselines/solutions/2021/E/q02/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2021/E/q02/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2021/E/q02/result.json
- 实验报告：cumcm/generic_baselines/reports/2021/E/q02/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2021/E/q02/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：../../Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/E/附件1.xlsx
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "quadratic_least_squares",
  "coefficients": [
    19.480896,
    -0.257897,
    0.000718
  ],
  "r2": 0.026401753736170708,
  "mean_abs_error": 6.733169150098216
}
```
