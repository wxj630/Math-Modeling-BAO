# 2024-A 问题 1 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2024年 CUMCM A题：板凳龙”  闹元宵
- 问题：问题 1
- 原问：舞龙队沿螺距为 55 cm 的等距螺线顺时针盘入，各把手中心均位于螺线上。龙 头前把手的行进速度始终保持 1 m/s。初始时，龙头位于螺线第 16 圈 A 点处（见图 4）。请 给出从初始时刻到 300 s 为止，每秒整个舞龙队的位置和速度（指龙头、龙身和龙尾各前把 手及龙尾后把手中心的位置和速度，下同），将结果保存到文件 result1.xlsx 中（模板文件见 附件，其中“龙尾 （后）”表示龙尾后把手， 其余的均是前把手，结果保留 6 位小数， 下同）。 同时在论文中给出 0 s、60 s、120 s、180 s、240 s、300 s 时，龙头前把手、龙头后面第 1、 51、101、151、201 节龙身前把手和龙尾后把手的位置和速度（格式见表 1 和表 2）。 27.5 cm 第 2 个孔，孔径 5.5 cm 27.5 cm 第 1 个孔，孔径 5.5 cm 30 cm 27.5 cm 27.5 cm 30 cm 220 cm 第 2 个孔， 孔径 5.5 cm 第 1 个孔， 孔径 5.5 cm 27.5 cm 27.5 cm 前一节龙身后部 后一节龙身前部 前把手 341 cm 2

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

- 通用代码：cumcm/generic_baselines/solutions/2024/A/q01/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2024/A/q01/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2024/A/q01/result.json
- 实验报告：cumcm/generic_baselines/reports/2024/A/q01/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2024/A/q01/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：../../Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/A题/附件/result1.xlsx
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "least_squares_geometry_fit",
  "center": [
    1.653695,
    1.640855
  ],
  "radius": 7.2800100360582105,
  "mean_squared_error": 0.004081474244681732,
  "success": true
}
```
