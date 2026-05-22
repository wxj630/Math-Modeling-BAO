# 2011-A 问题 3 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2011年 CUMCM A题：城市表层土壤重金属污染分析
- 问题：问题 3
- 原问：分析重金属污染物的传播特征，由此建立模型，确定污染源的位置。

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

- 通用代码：cumcm/generic_baselines/solutions/2011/A/q03/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2011/A/q03/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2011/A/q03/result.json
- 实验报告：cumcm/generic_baselines/reports/2011/A/q03/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2011/A/q03/experiment_table.csv

## 数据来源

- 类型：problem_statement
- 路径：cumcm/problems/2011/A.md
- 说明：未找到可直接读取的数值附件，本问改用题目原文中的参数/表格数字生成实验结果。

## 核心结果

```json
{
  "method": "quadratic_least_squares",
  "coefficients": [
    2.921949,
    0.46142,
    -0.000228
  ],
  "r2": 0.2812154226760658,
  "mean_abs_error": 1.6901452032709539
}
```
