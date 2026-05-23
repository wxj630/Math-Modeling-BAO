# 2020-B 问题 1 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2020年 CUMCM B题：穿越沙漠
- 问题：问题 1
- 原问：假设只有一名玩家，在整个游戏时段内每天天气状况事先全部已知，试给出一般情况下玩家的最优策略。求解附件中的“第一关”和“第二关”，并将相应结果分别填入Result.xlsx。

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

- 通用代码：cumcm/generic_baselines/solutions/2020/B/q09/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2020/B/q09/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2020/B/q09/result.json
- 实验报告：cumcm/generic_baselines/reports/2020/B/q09/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2020/B/q09/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：../../Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/B/Result.xlsx
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "linear_trend_forecast",
  "intercept": -2.035984848484844,
  "slope": 0.9575534759358286,
  "r2": 0.9846845049200885,
  "next_12_forecast": [
    44.884135,
    45.841689,
    46.799242,
    47.756796,
    48.714349,
    49.671903,
    50.629456,
    51.58701,
    52.544563,
    53.502117,
    54.45967,
    55.417224
  ]
}
```
