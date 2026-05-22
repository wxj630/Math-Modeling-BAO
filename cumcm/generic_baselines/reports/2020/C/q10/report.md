# 2020-C 问题 7 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2020年 CUMCM C题：中小微企业的信贷决策
- 问题：问题 7
- 原问：客户流失率：因为贷款利率等因素银行失去潜在客户的比率。

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

- 通用代码：cumcm/generic_baselines/solutions/2020/C/q10/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2020/C/q10/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2020/C/q10/result.json
- 实验报告：cumcm/generic_baselines/reports/2020/C/q10/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2020/C/q10/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：../../Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/C/附件1：123家有信贷记录企业的相关数据.xlsx
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "logistic_regression_plus_kmeans",
  "training_accuracy": 0.9333333333333333,
  "cluster_counts": [
    116,
    124
  ]
}
```
