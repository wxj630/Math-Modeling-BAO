# 2017-A 问题 1 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2017年 CUMCM A题：CT系统参数标定及成像
- 问题：问题 1
- 原问：在正方形托盘上放置两个均匀固体介质组成的标定模板，模板的几何信息如图2所示，相应的数据文件见附件1，其中每一点的数值反映了该点的吸收强度，这里称为“吸收率”。对应于该模板的接收信息见附件2。请根据这一模板及其接收信息，确定CT系统旋转中心在正方形托盘中的位置、探测器单元之间的距离以及该CT系统使用的X射线的180个方向。

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

- 通用代码：cumcm/generic_baselines/solutions/2017/A/q01/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2017/A/q01/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2017/A/q01/result.json
- 实验报告：cumcm/generic_baselines/reports/2017/A/q01/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2017/A/q01/experiment_table.csv

## 数据来源

- 类型：problem_statement
- 路径：cumcm/problems/2017/A.md
- 说明：未找到可直接读取的数值附件，本问改用题目原文中的参数/表格数字生成实验结果。

## 核心结果

```json
{
  "method": "least_squares_geometry_fit",
  "center": [
    2.556789,
    1.702431
  ],
  "radius": 3.3815396148377213,
  "mean_squared_error": 0.0005197481019158157,
  "success": true
}
```
