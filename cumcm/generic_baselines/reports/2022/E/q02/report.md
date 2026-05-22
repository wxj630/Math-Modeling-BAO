# 2022-E 问题2 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2022年 CUMCM E题：小批量物料的生产安排
- 问题：问题2
- 原问：如果按照物料需求量的预测值来安排生产，可能会产生较大的库存，或者出现较 多的缺货，给企业带来经济和信誉方面的损失。企业希望从需求量的预测值、需求特征、库存 量和缺货量等方面综合考虑，以便更合理地安排生产。 请提供一种制定生产计划的方法，从第101 周（见附录(1)）开始，在每周初，制定本周的 物料生产计划（见附录(2)），安排生产，直至第177 周为止，使得平均服务水平不低于85%（见 附录(3)）。这里假设：本周计划生产的物料，只能在下周及以后使用。为便于统一计算结果， 进一步假设第100 周末的库存量和缺货量均为零，第100 周的生产计划数恰好等于第101 周的 实际需求数。 请在问题1 选定的6 种物料中选择一种物料，将其第 101 ∼110 周的生产计划数、实际 需求量、库存量、缺货量（见附录(4)）和服务水平按表1 的形式填写，放在正文中。

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

- 通用代码：cumcm/generic_baselines/solutions/2022/E/q02/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2022/E/q02/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2022/E/q02/result.json
- 实验报告：cumcm/generic_baselines/reports/2022/E/q02/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2022/E/q02/experiment_table.csv

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
