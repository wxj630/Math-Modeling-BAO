# 2015-C 问题 1 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2015年 CUMCM C题：月上柳梢头
- 问题：问题 1
- 原问：根据所建立的模型，分析2016年北京地区“月上柳梢头，人约黄昏后”发生的日期与时间。根据模型判断2016年在哈尔滨、上海、广州、昆明、成都、乌鲁木齐是否能发生这一情景？如果能，请给出相应的日期与时间；如果不能，请给出原因

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

- 通用代码：cumcm/generic_baselines/solutions/2015/C/q01/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2015/C/q01/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2015/C/q01/result.json
- 实验报告：cumcm/generic_baselines/reports/2015/C/q01/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2015/C/q01/experiment_table.csv

## 数据来源

- 类型：problem_statement
- 路径：cumcm/problems/2015/C.md
- 说明：未找到可直接读取的数值附件，本问改用题目原文中的参数/表格数字生成实验结果。

## 核心结果

```json
{
  "method": "linear_trend_forecast",
  "intercept": 2014.5857142857142,
  "slope": -215.3142857142857,
  "r2": 0.18699322145655617,
  "next_12_forecast": [
    -8535.814286,
    -8751.128571,
    -8966.442857,
    -9181.757143,
    -9397.071429,
    -9612.385714,
    -9827.7,
    -10043.014286,
    -10258.328571,
    -10473.642857,
    -10688.957143,
    -10904.271429
  ]
}
```
