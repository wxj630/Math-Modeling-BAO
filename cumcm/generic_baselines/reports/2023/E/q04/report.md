# 2023-E 问题4 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2023年 CUMCM E题：黄河水沙监测数据分析
- 问题：问题4
- 原问：根据该水文站的水沙通量和河底高程的变化情况，分析每年6-7 月小浪底水库进 行“调水调沙”的实际效果。如果不进行“调水调沙”，10 年以后该水文站的河底高程会如何？ 附件1 2016-2021 年黄河水沙监测数据 附件2 黄河断面的测量数据 附件3 黄河部分监测点的监测数据 附录 说明 (1) “水位”和“河底高程”均以“1985 国家高程基准”（海拔72.26 米）为基准面。 (2) 附件中的“起点距离”以河岸边某定点作为起点。

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

- 通用代码：cumcm/generic_baselines/solutions/2023/E/q04/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2023/E/q04/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2023/E/q04/result.json
- 实验报告：cumcm/generic_baselines/reports/2023/E/q04/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2023/E/q04/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：../../Documents/Playground/cumcm_unzipped/2023_Y20WPner9fa62862794e6dc82731a5561ce1132f/E题/附件1.xlsx
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "quadratic_least_squares",
  "coefficients": [
    27.871143,
    0.656365,
    -0.000332
  ],
  "r2": 0.0957036981299928,
  "mean_abs_error": 7.3866470404988895
}
```
