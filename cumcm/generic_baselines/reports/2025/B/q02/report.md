# 2025-B 问题2 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2025年 CUMCM B题：碳化硅外延层厚度的确定
- 问题：问题2
- 原问：请根据问题1 的数学模型，设计确定外延层厚度的算法。对附件1 和附件2 提 供的碳化硅晶圆片的光谱实测数据，给出计算结果，并分析结果的可靠性。

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

- 通用代码：cumcm/generic_baselines/solutions/2025/B/q02/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2025/B/q02/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2025/B/q02/result.json
- 实验报告：cumcm/generic_baselines/reports/2025/B/q02/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2025/B/q02/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/B题/附件/附件1.xlsx
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "quadratic_least_squares",
  "coefficients": [
    2.077919,
    0.01761,
    7.8e-05
  ],
  "r2": 0.6581379761412045,
  "mean_abs_error": 2.255123483439905
}
```
