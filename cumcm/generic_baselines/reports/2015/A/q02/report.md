# 2015-A 问题 2 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2015年 CUMCM A题：太阳影子定位
- 问题：问题 2
- 原问：根据某固定直杆在水平地面上的太阳影子顶点坐标数据，建立数学模型确定直杆所处的地点。将你们的模型应用于附件1的影子顶点坐标数据，给出若干个可能的地点。

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

- 通用代码：cumcm/generic_baselines/solutions/2015/A/q02/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2015/A/q02/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2015/A/q02/result.json
- 实验报告：cumcm/generic_baselines/reports/2015/A/q02/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2015/A/q02/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：../../Documents/Playground/cumcm_unzipped/2015_m00L7uGp5743fadb9289f545d4ed5a1b300622fa/A/附件1-3.xls
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "least_squares_geometry_fit",
  "center": [
    3.85948,
    -0.275895
  ],
  "radius": 4.1191377206736846,
  "mean_squared_error": 0.004260155881486349,
  "success": true
}
```
