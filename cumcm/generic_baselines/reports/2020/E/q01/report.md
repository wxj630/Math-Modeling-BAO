# 2020-E 问题 1 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2020年 CUMCM E题：校园供水系统智能管理
- 问题：问题 1
- 原问：输水管网的漏损是一个严重问题。资料显示，在维护良好的公共供水网络中，平均失水在5%左右；而在比较老旧的管网中，失水则会更多。请利用附件提供的数据，建立数学模型，分析该校园供水管网的漏损情况

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

- 通用代码：cumcm/generic_baselines/solutions/2020/E/q01/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2020/E/q01/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2020/E/q01/result.json
- 实验报告：cumcm/generic_baselines/reports/2020/E/q01/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2020/E/q01/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：../../Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/E/附件_一季度.xlsx
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "quadratic_least_squares",
  "coefficients": [
    1.0,
    -0.166781,
    1.9e-05
  ],
  "r2": 1.0,
  "mean_abs_error": 3.047242828439304e-12
}
```
