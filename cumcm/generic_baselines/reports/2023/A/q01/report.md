# 2023-A 问题1 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2023年 CUMCM A题：定日镜场的优化设计
- 问题：问题1
- 原问：若将吸收塔建于该圆形定日镜场中心，定日镜尺寸均为 6 m×6 m，安装高度均为 4 m，且给定所有定日镜中心的位置（以下简称为定日镜位置，相关数据见附件），请计算该定 日镜场的年平均光学效率、年平均输出热功率，以及单位镜面面积年平均输出热功率（光学效 率及输出热功率的定义见附录）。请将结果分别按表1 和表2 的格式填入表格。

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

- 通用代码：cumcm/generic_baselines/solutions/2023/A/q01/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2023/A/q01/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2023/A/q01/result.json
- 实验报告：cumcm/generic_baselines/reports/2023/A/q01/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2023/A/q01/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：../../Documents/Playground/cumcm_unzipped/2023_Y20WPner9fa62862794e6dc82731a5561ce1132f/A题/result2.xlsx
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "least_squares_geometry_fit",
  "center": [
    -1.313316,
    -1.988447
  ],
  "radius": 4.462514933178243,
  "mean_squared_error": 0.0037851606077457093,
  "success": true
}
```
