# 2024-E 问题 1 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2024年 CUMCM E题：交通流量管控
- 问题：问题 1
- 原问：对经中路-纬中路交叉口，根据车流量的差异，可将一天分成若干个时段，估 计不同时段各个相位（包括四个方向直行、转弯）车流量。

## 通用模型选择

- 模型：时间序列预测（CH8：时间序列）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH8/第8章-时间序列.md
- 通用方法：`linear_trend_forecast`

## 变量、约束与公式

### 变量定义
- t: 时间索引
- y_t: 历史观测指标
- a,b: 趋势回归参数
- y_{t+h}: 未来预测值

### 约束条件
- 短期趋势用线性项近似
- 预测区间延续历史趋势假设

### 模型公式 / 目标函数
- `y_t = a + b*t + epsilon_t`
- `forecast(t+h)=a+b*(t+h)`

## 运行与产物

- 通用代码：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2024/E/q01/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2024/E/q01/solution.py`
- 结果 JSON：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/results/2024/E/q01/result.json
- 实验报告：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/reports/2024/E/q01/report.md
- 实验产物：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/artifacts/2024/E/q01/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/E题/附件1.xlsx
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "linear_trend_forecast",
  "intercept": -1.2857142857142847,
  "slope": 1.6428571428571426,
  "r2": 0.6547029702970297,
  "next_12_forecast": [
    79.214286,
    80.857143,
    82.5,
    84.142857,
    85.785714,
    87.428571,
    89.071429,
    90.714286,
    92.357143,
    94.0,
    95.642857,
    97.285714
  ]
}
```
