# 2018-D 问题 1 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2018年 CUMCM D题：汽车总装线的配置
- 问题：问题 1
- 原问：每天白班和晚班都是按照先A1后A2的品牌顺序，装配当天两种品牌各一半数量的汽车。如9月17日需装配的A1和A2的汽车分别为364和96辆，则该日每班首先装配182辆A1汽车，随后装配48辆A2汽车。

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

- 通用代码：cumcm/generic_baselines/solutions/2018/D/q03/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2018/D/q03/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2018/D/q03/result.json
- 实验报告：cumcm/generic_baselines/reports/2018/D/q03/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2018/D/q03/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：../../Documents/Playground/cumcm_unzipped/2018_lcGi8NeCd14458641de55ec1d705ea01714ff2dd/2018-D-Chinese/CUMCM-2018-Problem-D-Chinese-Appendix.xlsx
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "linear_trend_forecast",
  "intercept": 3659.1878787878795,
  "slope": -16.369506844506855,
  "r2": 0.0024771096055143937,
  "next_12_forecast": [
    2857.082043,
    2840.712537,
    2824.34303,
    2807.973523,
    2791.604016,
    2775.234509,
    2758.865002,
    2742.495495,
    2726.125989,
    2709.756482,
    2693.386975,
    2677.017468
  ]
}
```
