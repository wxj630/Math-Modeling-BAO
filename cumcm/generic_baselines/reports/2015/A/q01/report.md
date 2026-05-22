# 2015-A 问题 1 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2015年 CUMCM A题：太阳影子定位
- 问题：问题 1
- 原问：建立影子长度变化的数学模型，分析影子长度关于各个参数的变化规律，并应用你们建立的模型画出2015年10月22日北京时间9:00-15:00之间天安门广场（北纬39度54分26秒,东经116度23分29秒）3米高的直杆的太阳影子长度的变化曲线。

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

- 通用代码：cumcm/generic_baselines/solutions/2015/A/q01/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2015/A/q01/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2015/A/q01/result.json
- 实验报告：cumcm/generic_baselines/reports/2015/A/q01/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2015/A/q01/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：../../Documents/Playground/cumcm_unzipped/2015_m00L7uGp5743fadb9289f545d4ed5a1b300622fa/A/附件1-3.xls
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "quadratic_least_squares",
  "coefficients": [
    -10.885971,
    19.911743,
    -0.009879
  ],
  "r2": 0.36815587942517003,
  "mean_abs_error": 0.876433095807558
}
```
