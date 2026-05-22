# 2022-A 问题1 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2022年 CUMCM A题：波浪能最大输出功率设计
- 问题：问题1
- 原问：如图1 所示，中轴底座固定于隔层的中心位置，弹簧和直线阻尼器一端固定在振 子上，一端固定在中轴底座上，振子沿中轴做往复运动。直线阻尼器的阻尼力与浮子和振子的 相对速度成正比，比例系数为直线阻尼器的阻尼系数。考虑浮子在波浪中只做垂荡运动（参见 附件1），建立浮子与振子的运动模型。初始时刻浮子和振子平衡于静水中，利用附件3 和附 件4 提供的参数值（其中波浪频率取1.4005 s−1，这里及以下出现的频率均指圆频率，角度均 采用弧度制），分别对以下两种情况计算浮子和振子在波浪激励力 𝑓cos 𝜔𝑡（𝑓 为波浪激励力 振幅，𝜔 为波浪频率）作用下前40 个波浪周期内时间间隔为0.2 s 的垂荡位移和速度：(1) 直 线阻尼器的阻尼系数为10000 N·s/m；(2) 直线阻尼器的阻尼系数与浮子和振子的相对速度的绝 对值的幂成正比，其中比例系数取10000，幂指数取0.5。将结果存放在result1-1.xlsx 和 result1-2.xlsx 中。在论文中给出10 s、20 s、40 s、60 s、100 s 时，浮子与振子的垂荡位移和速 度。

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

- 通用代码：cumcm/generic_baselines/solutions/2022/A/q01/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2022/A/q01/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2022/A/q01/result.json
- 实验报告：cumcm/generic_baselines/reports/2022/A/q01/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2022/A/q01/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：../../Documents/Playground/cumcm_unzipped/2022_5eWlbmTt28f88a0815a79d555da8b7072f971633/A题/result1-1.xlsx
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "least_squares_geometry_fit",
  "center": [
    1.735459,
    0.886226
  ],
  "radius": 3.8800270179967047,
  "mean_squared_error": 0.0037373896210244656,
  "success": true
}
```
