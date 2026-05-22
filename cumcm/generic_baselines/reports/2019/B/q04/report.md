# 2019-B 问题 4 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2019年 CUMCM B题：同心协力”策略研究
- 问题：问题 4
- 原问：当鼓面发生倾斜时， 球跳动方向不再竖直， 于是需要队员调整拉绳策略。 假设人数为 10，绳长为 2m，球的反弹高度为 60cm，相对于竖直方向产生 1 度 的倾斜角度，且倾斜方向在水平面的投影指向某两位队员之间， 与这两位队员的 夹角之比为 1:2。为了将球调整为竖直状态弹跳，请给出在可精确控制条件下所 有队员的发力时机及力度，并分析在现实情形中这种调整策略的实施效果。

## 通用模型选择

- 模型：几何解析与运动学参数方程（CH1：解析方法与几何模型）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH1/第1章-解析方法与几何模型.md
- 通用方法：`least_squares_geometry_fit`

## 变量、约束与公式

### 变量定义
- p_i=(x_i,y_i): 几何观测点
- c=(a,b): 中心或定位参数
- r: 半径/尺度参数
- e_i: 几何残差

### 约束条件
- r >= 0
- 观测点满足题面几何关系的近似约束

### 模型公式 / 目标函数
- `min_{a,b,r} mean_i (||p_i-c||_2-r)^2`
- `e_i=||p_i-c||_2-r`

## 运行与产物

- 通用代码：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2019/B/q04/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2019/B/q04/solution.py`
- 结果 JSON：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/results/2019/B/q04/result.json
- 实验报告：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/reports/2019/B/q04/report.md
- 实验产物：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/artifacts/2019/B/q04/experiment_table.csv

## 数据来源

- 类型：problem_statement
- 路径：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2019/B.md
- 说明：未找到可直接读取的数值附件，本问改用题目原文中的参数/表格数字生成实验结果。

## 核心结果

```json
{
  "method": "least_squares_geometry_fit",
  "center": [
    2.512834,
    1.360135
  ],
  "radius": 3.1853958759594,
  "mean_squared_error": 0.017587419851854923,
  "success": true
}
```
