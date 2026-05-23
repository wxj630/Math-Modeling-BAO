# 2010-B 问题 1 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2010年 CUMCM B题：2010年上海世博会影响力的定量评估
- 问题：问题 1
- 原问：2010年上海世博会是首次在中国举办的世界博览会。从1851年伦敦的“万国工业博览会”开始，世博会正日益成为各国人民交流历史文化、展示科技成果、体现合作精神、展望未来发展等的重要舞台。请你们选择感兴趣的某个侧面，建立数学模型，利用互联网数据，定量评估2010年上海世博会的影响力

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

- 通用代码：cumcm/generic_baselines/solutions/2010/B/q01/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2010/B/q01/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2010/B/q01/result.json
- 实验报告：cumcm/generic_baselines/reports/2010/B/q01/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2010/B/q01/experiment_table.csv

## 数据来源

- 类型：problem_statement
- 路径：cumcm/problems/2010/B.md
- 说明：未找到可直接读取的数值附件，本问改用题目原文中的参数/表格数字生成实验结果。

## 核心结果

```json
{
  "method": "linear_trend_forecast",
  "intercept": 1865.6607142857147,
  "slope": -190.64404761904768,
  "r2": 0.1899603616350951,
  "next_12_forecast": [
    -7475.897619,
    -7666.541667,
    -7857.185714,
    -8047.829762,
    -8238.47381,
    -8429.117857,
    -8619.761905,
    -8810.405952,
    -9001.05,
    -9191.694048,
    -9382.338095,
    -9572.982143
  ]
}
```
