# 2022-E 问题1 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2022年 CUMCM E题：小批量物料的生产安排
- 问题：问题1
- 原问：请对附件中的历史数据进行分析，选择6 种应当重点关注的物料（可从物料需求 出现的频数、数量、趋势和销售单价等方面考虑），建立物料需求的周预测模型（即以周为基 本时间单位，预测物料的周需求量，见附录(1)），并利用历史数据对预测模型进行评价。

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

- 通用代码：cumcm/generic_baselines/solutions/2022/E/q01/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2022/E/q01/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2022/E/q01/result.json
- 实验报告：cumcm/generic_baselines/reports/2022/E/q01/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2022/E/q01/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：../../Documents/Playground/cumcm_unzipped/2022_5eWlbmTt28f88a0815a79d555da8b7072f971633/E题/附件.xlsx
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "quadratic_least_squares",
  "coefficients": [
    0.927314,
    276098.705416,
    -3.174141
  ],
  "r2": 0.9999999965953736,
  "mean_abs_error": 9986.500744688507
}
```
