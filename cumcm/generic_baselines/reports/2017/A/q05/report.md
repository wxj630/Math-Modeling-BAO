# 2017-A 问题 1 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2017年 CUMCM A题：CT系统参数标定及成像
- 问题：问题 1
- 原问：-(4)中的所有数值结果均保留4位小数。同时提供(2)和(3)重建得到的介质吸收率的数据文件（大小为256×256，格式同附件1，文件名分别为problem2.xls和problem3.xls）

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

- 通用代码：cumcm/generic_baselines/solutions/2017/A/q05/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2017/A/q05/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2017/A/q05/result.json
- 实验报告：cumcm/generic_baselines/reports/2017/A/q05/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2017/A/q05/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：../../Documents/Playground/cumcm_unzipped/2017_IqAO5Qqi8f23d8738a07a0604b8629ce9bb061ad/CUMCM2017Problems/A/A题附件.xls
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "quadratic_least_squares",
  "coefficients": [
    0.0,
    0.0,
    0.0
  ],
  "r2": 1.0,
  "mean_abs_error": 0.0
}
```
