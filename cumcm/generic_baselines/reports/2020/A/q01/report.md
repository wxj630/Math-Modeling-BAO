# 2020-A 问题1 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2020年 CUMCM A题：炉温曲线
- 问题：问题1
- 原问：请对焊接区域的温度变化规律建立数学模型。假设传送带过炉速度为78 cm/min，各温区温度的设定值分别为173ºC（小温区1~5）、198ºC（小温区6）、230ºC（小温区7）和257ºC（小温区8~9），请给出焊接区域中心的温度变化情况，列出小温区3、6、7中点及小温区8结束处焊接区域中心的温度，画出相应的炉温曲线，并将每隔0.5 s焊接区域中心的温度存放在提供的result.csv中。

## 通用模型选择

- 模型：微分方程与动态仿真（CH2：微分方程与动力系统）
- 教程参考：../My-Agent/intro-mathmodel/docs/CH2/第2章-微分方程与动力系统.md
- 通用方法：`first_order_dynamic_simulation`

## 变量、约束与公式

### 变量定义
- y(t): 系统状态
- k: 调节/衰减系数
- y_env: 环境或稳态值
- t: 时间

### 约束条件
- k > 0
- 初值 y(0)=y0
- 状态向稳态单调或振荡趋近

### 模型公式 / 目标函数
- `dy/dt = -k*(y-y_env)`
- `y(0)=y0`

## 运行与产物

- 通用代码：cumcm/generic_baselines/solutions/2020/A/q01/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2020/A/q01/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2020/A/q01/result.json
- 实验报告：cumcm/generic_baselines/reports/2020/A/q01/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2020/A/q01/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：../../Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/A/result.csv
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "first_order_dynamic_simulation",
  "y0": 76.15400935255848,
  "steady_state": 16.636885170979795,
  "k": 0.06972510164231059,
  "final_value": 16.864722129751623
}
```
