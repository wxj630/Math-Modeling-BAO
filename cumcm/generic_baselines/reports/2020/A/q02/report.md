# 2020-A 问题2 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2020年 CUMCM A题：炉温曲线
- 问题：问题2
- 原问：假设各温区温度的设定值分别为182ºC（小温区1~5）、203ºC（小温区6）、237ºC（小温区7）、254ºC（小温区8~9），请确定允许的最大传送带过炉速度。

## 通用模型选择

- 模型：微分方程与动态仿真（CH2：微分方程与动力系统）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH2/第2章-微分方程与动力系统.md
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

- 通用代码：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2020/A/q02/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2020/A/q02/solution.py`
- 结果 JSON：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/results/2020/A/q02/result.json
- 实验报告：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/reports/2020/A/q02/report.md
- 实验产物：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/artifacts/2020/A/q02/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/A/result.csv
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "first_order_dynamic_simulation",
  "y0": 122.70093821737366,
  "steady_state": 15.691281394379653,
  "k": 0.04264074931879825,
  "final_value": 19.228649482628832
}
```
