# 2025-C 问题1 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2025年 CUMCM C题：NIPT 的时点选择与胎儿的异常判定
- 问题：问题1
- 原问：试分析胎儿Y 染色体浓度与孕妇的孕周数和BMI 等指标的相关特性，给出相应的关系模 型，并检验其显著性。

## 通用模型选择

- 模型：综合评价与权重决策（CH7：权重生成与评价模型）
- 教程参考：../My-Agent/intro-mathmodel/docs/CH7/第7章-权重生成与评价模型.md
- 通用方法：`std_weight_topsis`

## 变量、约束与公式

### 变量定义
- a_ij: 方案 i 在指标 j 上的标准化表现
- w_j: 指标权重
- D_i^+: 到理想解距离
- C_i: TOPSIS 贴近度

### 约束条件
- 各指标同向化后归一化
- sum_j w_j = 1, w_j >= 0

### 模型公式 / 目标函数
- `w_j = std(a_.j)/sum_j std(a_.j)`
- `C_i = D_i^-/(D_i^+ + D_i^-)`
- `rank = argsort(-C_i)`

## 运行与产物

- 通用代码：cumcm/generic_baselines/solutions/2025/C/q01/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2025/C/q01/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2025/C/q01/result.json
- 实验报告：cumcm/generic_baselines/reports/2025/C/q01/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2025/C/q01/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/C题/附件.xlsx
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "std_weight_topsis",
  "weights": [
    0.888593,
    0.111407
  ],
  "scores": [
    0.998597,
    0.000156,
    0.001649,
    0.003288,
    0.004929,
    0.006576,
    0.008216,
    0.009857,
    0.011498,
    0.01314,
    0.014786,
    0.016427,
    0.018068,
    0.01971,
    0.021351,
    0.022993,
    0.024638,
    0.02628,
    0.027921,
    0.029563,
    0.031208,
    0.03285,
    0.034491,
    0.036133,
    0.037778,
    0.03942,
    0.041061,
    0.042703,
    0.044348,
    0.045989,
    0.047631,
    0.049273,
    0.050914,
    0.052559,
    0.054201,
    0.055842,
    0.057484,
    0.059129,
    0.060771,
    0.062412
  ],
  "best_option": 1
}
```
