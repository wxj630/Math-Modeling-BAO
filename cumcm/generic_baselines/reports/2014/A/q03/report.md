# 2014-A 问题 3 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2014年 CUMCM A题：嫦娥三号软着陆轨道设计与控制策略
- 问题：问题 3
- 原问：对于你们设计的着陆轨道和控制策略做相应的误差分析和敏感性分析。 附件1： 问题的背景与参考资料； 附件2： 嫦娥三号着陆过程的六个阶段及其状态要求； 附件3：距月面2400m处的数字高程图； 附件4：距月面100m处的数字高程图。

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

- 通用代码：cumcm/generic_baselines/solutions/2014/A/q03/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2014/A/q03/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2014/A/q03/result.json
- 实验报告：cumcm/generic_baselines/reports/2014/A/q03/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2014/A/q03/experiment_table.csv

## 数据来源

- 类型：problem_statement
- 路径：cumcm/problems/2014/A.md
- 说明：未找到可直接读取的数值附件，本问改用题目原文中的参数/表格数字生成实验结果。

## 核心结果

```json
{
  "method": "least_squares_geometry_fit",
  "center": [
    1.596702,
    1.583168
  ],
  "radius": 2.6559562943654074,
  "mean_squared_error": 0.001737823550789533,
  "success": true
}
```
