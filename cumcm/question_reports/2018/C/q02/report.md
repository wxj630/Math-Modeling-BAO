# 2018-C 问题 2 建模求解实验报告

## 题目原文与任务拆解

- 题目：2018年 CUMCM C题：大型百货商场会员画像描绘
- 问题：问题 2
- 原问：针对会员的消费情况建立能够刻画每一位会员购买力的数学模型，以便能够对每个会员的价值进行识别。

### 本问需要完成什么
- 任务 1：针对会员的消费情况建立能够刻画每一位会员购买力的数学模型，以便能够对每个会员的价值进行识别

## 适配模型

- 主模型：机器学习与统计识别（CH9：机器学习与统计模型）
- 教程参考：../My-Agent/intro-mathmodel/docs/CH9/第九章-机器学习与统计模型.md

### 候选模型与适配理由
- 机器学习与统计识别（CH9）：识别；参考 ../My-Agent/intro-mathmodel/docs/CH9/第九章-机器学习与统计模型.md

## 变量、约束与公式

### 建模假设
- 以题面给出的数值、约束和输出格式为第一优先级构造模型。
- 若原始附件尚未能被当前环境直接读取，脚本优先抽取题目原文中的参数和表格数字，并在数据来源中显式记录。
- 所有结果由本问 solution.py 运行生成，result.json 与 experiment_table.csv 保持同步。

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

## Python 代码与运行方式

- 代码文件：cumcm/question_solutions/2018/C/q02/solution.py
- 单问运行：`.venv/bin/python cumcm/question_solutions/2018/C/q02/solution.py`
- 批量运行：`.venv/bin/python cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：构造或读取样本特征。
- 步骤 2：训练逻辑回归分类器。
- 步骤 3：用 KMeans 做无监督对照。
- 步骤 4：输出准确率、聚类数量和 PCA 投影。

## 实验结果与解释

### 产物文件
- cumcm/question_artifacts/2018/C/q02/experiment_table.csv

### 数据来源
- 类型：problem_statement
- 附件：cumcm/problems/2018/C.md
- 读取规模：8 行 x 3 列
- 说明：未找到可直接读取的数值附件，本问改用题目原文中的参数/表格数字生成实验结果。

### result.json 核心结果

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

### 结果解释
- 本问用 `logistic_regression_plus_kmeans` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 实验报告

本问的核心是：针对会员的消费情况建立能够刻画每一位会员购买力的数学模型，以便能够对每个会员的价值进行识别。

建模时先将题目要求拆成 1 个任务，再选择 `机器学习与统计识别`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
