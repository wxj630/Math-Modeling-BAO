# 2019-B 问题 2 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2019年 CUMCM B题：同心协力”策略研究
- 问题：问题 2
- 原问：在现实情形中，队员发力时机和力度不可能做到精确控制，存在一定误 差， 于是鼓面可能出现倾斜。 试建立模型描述队员的发力时机和力度与某一特定 时刻的鼓面倾斜角度的关系。 设队员人数为8， 绳长为1.7m， 鼓面初始时刻是水 平静止的，初始位置较绳子水平时下降 11 cm，表 1 中给出了队员们的不同发力 时机和力度，求 0.1 s 时鼓面的倾斜角度。

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

- 通用代码：cumcm/generic_baselines/solutions/2019/B/q02/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2019/B/q02/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2019/B/q02/result.json
- 实验报告：cumcm/generic_baselines/reports/2019/B/q02/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2019/B/q02/experiment_table.csv

## 数据来源

- 类型：problem_statement
- 路径：cumcm/problems/2019/B.md
- 说明：未找到可直接读取的数值附件，本问改用题目原文中的参数/表格数字生成实验结果。

## 核心结果

```json
{
  "method": "least_squares_geometry_fit",
  "center": [
    2.512678,
    1.359846
  ],
  "radius": 3.185144341383319,
  "mean_squared_error": 0.01756089026811107,
  "success": true
}
```
