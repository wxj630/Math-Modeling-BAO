# 2024-A 问题 4 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2024年 CUMCM A题：板凳龙”  闹元宵
- 问题：问题 4
- 原问：盘入螺线的螺距为 1.7 m，盘出螺线与盘入螺线关于螺线中心呈中心对称，舞 龙队在问题 3 设定的调头空间内完成调头，调头路径是由两段圆弧相切连接而成的 S 形曲 线，前一段圆弧的半径是后一段的 2 倍， 它与盘入、盘出螺线均相切。能否调整圆弧， 仍保 持各部分相切，使得调头曲线变短？ 龙头前把手的行进速度始终保持 1 m/s。以调头开始时间为零时刻， 给出从−100 s 开始 到100 s 为止， 每秒舞龙队的位置和速度， 将结果存放到文件result4.xlsx 中 （模板文件见附 件） 。 同时在论文中给出−100 s、−50 s、0 s、50 s、100 s 时，龙头前把手、 龙头后面第1、 51、101、151、201 节龙身前把手和龙尾后把手的位置和速度。

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

- 通用代码：cumcm/generic_baselines/solutions/2024/A/q04/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2024/A/q04/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2024/A/q04/result.json
- 实验报告：cumcm/generic_baselines/reports/2024/A/q04/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2024/A/q04/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：../../Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/A题/附件/result1.xlsx
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "least_squares_geometry_fit",
  "center": [
    0.805375,
    1.409971
  ],
  "radius": 5.506288052958869,
  "mean_squared_error": 0.0033546582306843453,
  "success": true
}
```
