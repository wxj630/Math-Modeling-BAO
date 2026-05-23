# 2017-D 问题2 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2017年 CUMCM D题：巡检线路的排班
- 问题：问题2
- 原问：如果巡检人员每巡检2小时左右需要休息一次，休息时间大约是5到10分钟，在中午12时和下午6时左右需要进餐一次，每次进餐时间为30分钟，仍采用每天三班倒，每班需要多少人，巡检线路如何安排，并给出巡检人员的巡检线路和巡检的时间表。

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

- 通用代码：cumcm/generic_baselines/solutions/2017/D/q02/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2017/D/q02/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2017/D/q02/result.json
- 实验报告：cumcm/generic_baselines/reports/2017/D/q02/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2017/D/q02/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：../../Documents/Playground/cumcm_unzipped/2017_IqAO5Qqi8f23d8738a07a0604b8629ce9bb061ad/CUMCM2017Problems/D/CUMCM-2017-appendix-D.xlsx
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "linear_trend_forecast",
  "intercept": 9.97486849795441,
  "slope": 0.09801285797779083,
  "r2": 0.044177985034651646,
  "next_12_forecast": [
    14.777499,
    14.875511,
    14.973524,
    15.071537,
    15.16955,
    15.267563,
    15.365576,
    15.463589,
    15.561601,
    15.659614,
    15.757627,
    15.85564
  ]
}
```
