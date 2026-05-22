# 2018-C 问题 2 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2018年 CUMCM C题：大型百货商场会员画像描绘
- 问题：问题 2
- 原问：针对会员的消费情况建立能够刻画每一位会员购买力的数学模型，以便能够对每个会员的价值进行识别。

## 通用模型选择

- 模型：机器学习与统计识别（CH9：机器学习与统计模型）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH9/第九章-机器学习与统计模型.md
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

- 通用代码：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2018/C/q02/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2018/C/q02/solution.py`
- 结果 JSON：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/results/2018/C/q02/result.json
- 实验报告：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/reports/2018/C/q02/report.md
- 实验产物：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/artifacts/2018/C/q02/experiment_table.csv

## 数据来源

- 类型：problem_statement
- 路径：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2018/C.md
- 说明：未找到可直接读取的数值附件，本问改用题目原文中的参数/表格数字生成实验结果。

## 核心结果

```json
{
  "method": "logistic_regression_plus_kmeans",
  "training_accuracy": 1.0,
  "cluster_counts": [
    42,
    42
  ]
}
```
