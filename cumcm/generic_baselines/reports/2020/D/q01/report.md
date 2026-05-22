# 2020-D 问题1 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2020年 CUMCM D题：接触式轮廓仪的自动标注
- 问题：问题1
- 原问：附件1中的表level是工件1在水平状态下的测量数据，其轮廓线如图4所示，请标注出轮廓线的各项参数值：槽口宽度（如等）、圆弧半径（如等）、圆心之间的距离（如等）、圆弧的长度、水平线段的长度（如等）、斜线线段的长度、斜线与水平线之间的夹角（如等）和人字形线的高度（）。

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

- 通用代码：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2020/D/q01/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2020/D/q01/solution.py`
- 结果 JSON：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/results/2020/D/q01/result.json
- 实验报告：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/reports/2020/D/q01/report.md
- 实验产物：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/artifacts/2020/D/q01/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/D/附件1_工件1的测量数据.xlsx
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "least_squares_geometry_fit",
  "center": [
    -10.55792,
    11.727232
  ],
  "radius": 15.842884482190431,
  "mean_squared_error": 0.0005569176943839104,
  "success": true
}
```
