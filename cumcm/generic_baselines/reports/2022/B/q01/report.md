# 2022-B 问题 1 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2022年 CUMCM B题：无人机遂行编队飞行中的纯方位无源定位
- 问题：问题 1
- 原问：编队由 10 架无人机组成，形成圆形编队，其中 9 架无人机（编号 FY01~FY09）均 匀分布在某一圆周上，另 1 架无人机（编号 FY00）位于圆心（见图 2）。无人机基于自身感知 的高度信息，均保持在同一个高度上飞行。

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

- 通用代码：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2022/B/q01/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2022/B/q01/solution.py`
- 结果 JSON：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/results/2022/B/q01/result.json
- 实验报告：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/reports/2022/B/q01/report.md
- 实验产物：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/artifacts/2022/B/q01/experiment_table.csv

## 数据来源

- 类型：problem_statement
- 路径：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2022/B.md
- 说明：未找到可直接读取的数值附件，本问改用题目原文中的参数/表格数字生成实验结果。

## 核心结果

```json
{
  "method": "least_squares_geometry_fit",
  "center": [
    2.534512,
    0.363111
  ],
  "radius": 2.924535340909232,
  "mean_squared_error": 0.0027512456522224894,
  "success": true
}
```
