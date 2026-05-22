# 2023-B 问题1 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2023年 CUMCM B题：多波束测线问题
- 问题：问题1
- 原问：与测线方向垂直的平面和海底坡面的交线构成一条与水平面夹角为 𝛼 的斜线（图 7），称 𝛼 为坡度。请建立多波束测深的覆盖宽度及相邻条带之间重叠率的数学模型。

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

- 通用代码：cumcm/generic_baselines/solutions/2023/B/q01/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2023/B/q01/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2023/B/q01/result.json
- 实验报告：cumcm/generic_baselines/reports/2023/B/q01/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2023/B/q01/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：../../Documents/Playground/cumcm_unzipped/2023_Y20WPner9fa62862794e6dc82731a5561ce1132f/B题/result1.xlsx
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "quadratic_least_squares",
  "coefficients": [
    -726.372727,
    761.75303,
    -161.719697
  ],
  "r2": 0.8586478618662563,
  "mean_abs_error": 110.440909090909
}
```
