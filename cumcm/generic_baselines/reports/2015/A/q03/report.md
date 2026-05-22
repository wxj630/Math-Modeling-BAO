# 2015-A 问题 3 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2015年 CUMCM A题：太阳影子定位
- 问题：问题 3
- 原问：根据某固定直杆在水平地面上的太阳影子顶点坐标数据，建立数学模型确定直杆所处的地点和日期。将你们的模型分别应用于附件2和附件3的影子顶点坐标数据，给出若干个可能的地点与日期。

## 通用模型选择

- 模型：时间序列预测（CH8：时间序列）
- 教程参考：../My-Agent/intro-mathmodel/docs/CH8/第8章-时间序列.md
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

- 通用代码：cumcm/generic_baselines/solutions/2015/A/q03/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2015/A/q03/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2015/A/q03/result.json
- 实验报告：cumcm/generic_baselines/reports/2015/A/q03/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2015/A/q03/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：../../Documents/Playground/cumcm_unzipped/2015_m00L7uGp5743fadb9289f545d4ed5a1b300622fa/A/附件1-3.xls
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "linear_trend_forecast",
  "intercept": 126.52003038194451,
  "slope": -2.9064917200854716,
  "r2": 0.04618828282258336,
  "next_12_forecast": [
    -15.898064,
    -18.804556,
    -21.711047,
    -24.617539,
    -27.524031,
    -30.430523,
    -33.337014,
    -36.243506,
    -39.149998,
    -42.056489,
    -44.962981,
    -47.869473
  ]
}
```
