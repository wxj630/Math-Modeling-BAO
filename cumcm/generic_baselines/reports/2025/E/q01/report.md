# 2025-E 问题1 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2025年 CUMCM E题：AI 辅助智能体测
- 问题：问题1
- 原问：附件1 是两位立定跳远运动者的跳远视频、位置信息和跳远成绩。其中，位置 信息包含运动者在整个跳远过程中的33 个关键节点（见附件2）在视频不同帧的位置坐标。 请确定运动者在跳远过程中的起跳和落地时刻，并描述滞空阶段（从起跳到落地）的运动 过程。

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

- 通用代码：cumcm/generic_baselines/solutions/2025/E/q01/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2025/E/q01/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2025/E/q01/result.json
- 实验报告：cumcm/generic_baselines/reports/2025/E/q01/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2025/E/q01/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件1/运动者1的跳远位置信息.xlsx
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "least_squares_geometry_fit",
  "center": [
    0.191661,
    -0.160736
  ],
  "radius": 1.3877604185373116,
  "mean_squared_error": 0.13671668593294262,
  "success": true
}
```
