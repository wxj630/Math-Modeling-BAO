# 2011-C 问题一 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2011年 CUMCM C题：企业退休职工养老金制度的改革
- 问题：问题一
- 原问：对未来中国经济发展和工资增长的形势做出你认为是简化、合理的假设，并参考附件1，预测从2011年至2035年的山东省职工的年平均工资。

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

- 通用代码：cumcm/generic_baselines/solutions/2011/C/q01/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2011/C/q01/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2011/C/q01/result.json
- 实验报告：cumcm/generic_baselines/reports/2011/C/q01/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2011/C/q01/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：../../Documents/Playground/cumcm_unzipped/2011_LOsf8a1w1cfbe73ef037f2f60e5c144c0f96a94f/C/cumcm2011C附件1_山东省职工平均工资.xls
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "linear_trend_forecast",
  "intercept": 2196.5578739495795,
  "slope": -17.577973949579828,
  "r2": 0.147315120451862,
  "next_12_forecast": [
    1335.23715,
    1317.659176,
    1300.081203,
    1282.503229,
    1264.925255,
    1247.347281,
    1229.769307,
    1212.191333,
    1194.613359,
    1177.035385,
    1159.457411,
    1141.879437
  ]
}
```
