# 2022-C 问题4 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2022年 CUMCM C题：古代玻璃制品的成分分析与鉴别
- 问题：问题4
- 原问：针对不同类别的玻璃文物样品，分析其化学成分之间的关联关系，并比较不同类 别之间的化学成分关联关系的差异性。 附件 表单1 玻璃文物的基本信息 表单2 已分类玻璃文物的化学成分比例，其中 (1) 文物采样点为该编号文物表面某部位的随机采样，其风化属性与附件表单1 中相应文 物一致。 (2) 部位1 和部位2 是文物造型上不同的两个部位，其成分与含量可能存在差异。 (3) 未风化点是风化文物表面未风化区域内的点。 (4) 严重风化点取自风化层。 表单3 未分类玻璃文物的化学成分比例

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

- 通用代码：cumcm/generic_baselines/solutions/2022/C/q04/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2022/C/q04/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2022/C/q04/result.json
- 实验报告：cumcm/generic_baselines/reports/2022/C/q04/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2022/C/q04/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：../../Documents/Playground/cumcm_unzipped/2022_5eWlbmTt28f88a0815a79d555da8b7072f971633/C题/附件.xlsx
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "logistic_regression_plus_kmeans",
  "training_accuracy": 0.717391304347826,
  "cluster_counts": [
    69,
    69
  ]
}
```
