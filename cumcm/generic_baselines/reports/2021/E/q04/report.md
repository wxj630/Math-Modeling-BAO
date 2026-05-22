# 2021-E 问题 4 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2021年 CUMCM E题：中药材的鉴别
- 问题：问题 4
- 原问：附件 4 给出了几种药材的近红外光谱数据，试鉴别药材的类别与产 地，并将下表中所给出编号的药材类别与产地的鉴别结果填入表各中。 No 94 109 140 278 308 330 347 Class OP

## 通用模型选择

- 模型：机器学习与统计识别（CH9：机器学习与统计模型）
- 教程参考：../My-Agent/intro-mathmodel/docs/CH9/第九章-机器学习与统计模型.md
- 通用方法：`logistic_regression_plus_kmeans`

## 变量、约束与公式

### 变量定义
- X: 样本特征矩阵
- y: 类别/状态标签
- theta: 逻辑回归参数
- z_i: 聚类标签

### 约束条件
- 特征标准化或同量纲
- 类别概率位于 [0,1]

### 模型公式 / 目标函数
- `P(y=1|x)=sigmoid(theta^T*x)`
- `min cross_entropy(y, sigmoid(X*theta))`
- `min within_cluster_sum_of_squares`

## 运行与产物

- 通用代码：cumcm/generic_baselines/solutions/2021/E/q04/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2021/E/q04/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2021/E/q04/result.json
- 实验报告：cumcm/generic_baselines/reports/2021/E/q04/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2021/E/q04/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：../../Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/E/附件1.xlsx
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "logistic_regression_plus_kmeans",
  "training_accuracy": 0.5416666666666666,
  "cluster_counts": [
    239,
    1
  ]
}
```
