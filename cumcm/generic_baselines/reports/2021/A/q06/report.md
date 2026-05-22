# 2021-A 问题 3 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2021年 CUMCM A题：FAST”主动反射面的形状调节
- 问题：问题 3
- 原问：每一块反射面板均为基准球面的一部分。 反射面板上开有许多直径小于5 毫米的小圆孔， 用于透漏雨水。 由于小孔的直径小于所观察的天体电磁波的波长， 不影响对天体电磁波的反射， 所以可以认为面板是无孔的。

## 通用模型选择

- 模型：几何解析与运动学参数方程（CH1：解析方法与几何模型）
- 教程参考：../My-Agent/intro-mathmodel/docs/CH1/第1章-解析方法与几何模型.md
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

- 通用代码：cumcm/generic_baselines/solutions/2021/A/q06/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2021/A/q06/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2021/A/q06/result.json
- 实验报告：cumcm/generic_baselines/reports/2021/A/q06/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2021/A/q06/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：../../Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/A/附件1.csv
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "least_squares_geometry_fit",
  "center": [
    0.002375,
    0.000614
  ],
  "radius": 1.3300604842358803,
  "mean_squared_error": 0.23061498649728718,
  "success": true
}
```
