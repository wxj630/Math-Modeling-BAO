# 2022-A 问题3 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2022年 CUMCM A题：波浪能最大输出功率设计
- 问题：问题3
- 原问：如图2 所示，中轴底座固定于隔层的中心位置，中轴架通过转轴铰接于中轴底座 中心，中轴绕转轴转动，PTO 系统连接振子和转轴架，并处于中轴与转轴所在的平面。除了直 线阻尼器，在转轴上还安装了旋转阻尼器和扭转弹簧，直线阻尼器和旋转阻尼器共同做功输出 能量。在波浪的作用下，浮子进行摇荡运动，并通过转轴及扭转弹簧和旋转阻尼器带动中轴转 动。振子随中轴转动，同时沿中轴进行滑动。扭转弹簧的扭矩与浮子和振子的相对角位移成正 比，比例系数为扭转弹簧的刚度。旋转阻尼器的扭矩与浮子和振子的相对角速度成正比，比例 系数为旋转阻尼器的旋转阻尼系数。考虑浮子只做垂荡和纵摇运动（参见附件2），建立浮子 与振子的运动模型。初始时刻浮子和振子平衡于静水中，利用附件3 和附件4 提供的参数值（波 浪频率取1.7152 s−1），假定直线阻尼器和旋转阻尼器的阻尼系数均为常量，分别为10000 N·s/m 和1000 N·m·s，计算浮子与振子在波浪激励力和波浪激励力矩 𝑓cos 𝜔𝑡，𝐿cos 𝜔𝑡（𝑓 为波浪激 励力振幅，𝐿 为波浪激励力矩振幅，𝜔 为波浪频率）作用下前40 个波浪周期内时间间隔为0.2 s 的垂荡位移与速度和纵摇角位移与角速度。将结果存放在result3.xlsx 中。在论文中给出10 s、 20 s、40 s、60 s、100 s 时，浮子与振子的垂荡位移与速度和纵摇角位移与角速度。

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

- 通用代码：cumcm/generic_baselines/solutions/2022/A/q03/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2022/A/q03/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2022/A/q03/result.json
- 实验报告：cumcm/generic_baselines/reports/2022/A/q03/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2022/A/q03/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：../../Documents/Playground/cumcm_unzipped/2022_5eWlbmTt28f88a0815a79d555da8b7072f971633/A题/result1-1.xlsx
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "least_squares_geometry_fit",
  "center": [
    1.037866,
    0.19605
  ],
  "radius": 6.251114674557069,
  "mean_squared_error": 0.002027266921149464,
  "success": true
}
```
