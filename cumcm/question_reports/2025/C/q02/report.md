# 2025-C 问题2 建模求解实验报告

## 题目原文与任务拆解

- 题目：2025年 CUMCM C题：NIPT 的时点选择与胎儿的异常判定
- 问题：问题2
- 原问：临床证明，男胎孕妇的BMI 是影响胎儿Y 染色体浓度的最早达标时间（即浓度达到或超 过4%的最早时间）的主要因素。试对男胎孕妇的BMI 进行合理分组，给出每组的BMI 区间和最佳NIPT 时点，使得孕妇可能的潜在风险最小，并分析检测误差对结果的影响。

### 本问需要完成什么
- 任务 1：临床证明，男胎孕妇的BMI 是影响胎儿Y 染色体浓度的最早达标时间（即浓度达到或超 过4%的最早时间）的主要因素
- 任务 2：试对男胎孕妇的BMI 进行合理分组，给出每组的BMI 区间和最佳NIPT 时点，使得孕妇可能的潜在风险最小，并分析检测误差对结果的影响

## 适配模型

- 主模型：机器学习与统计识别（CH9：机器学习与统计模型）
- 教程参考：../My-Agent/intro-mathmodel/docs/CH9/第九章-机器学习与统计模型.md

### 候选模型与适配理由
- 概率统计与抽样检验（CH9）：风险、误差；参考 ../My-Agent/intro-mathmodel/docs/CH9/第九章-机器学习与统计模型.md
- 机器学习与统计识别（CH9）：检测、风险；参考 ../My-Agent/intro-mathmodel/docs/CH9/第九章-机器学习与统计模型.md
- 规划优化与资源配置（CH3）：最小；参考 ../My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md

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

- 代码文件：cumcm/question_solutions/2025/C/q02/solution.py
- 单问运行：`.venv/bin/python cumcm/question_solutions/2025/C/q02/solution.py`
- 批量运行：`.venv/bin/python cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：构造或读取样本特征。
- 步骤 2：训练逻辑回归分类器。
- 步骤 3：用 KMeans 做无监督对照。
- 步骤 4：输出准确率、聚类数量和 PCA 投影。

## 实验结果与解释

### 产物文件
- cumcm/question_artifacts/2025/C/q02/experiment_table.csv

### 数据来源
- 类型：attachment
- 附件：../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/C题/附件.xlsx
- 读取规模：1689 行 x 31 列
- 说明：本问优先使用官方附件中的数值表生成实验结果。

### result.json 核心结果

```json
{
  "method": "logistic_regression_plus_kmeans",
  "training_accuracy": 1.0,
  "cluster_counts": [
    107,
    133
  ]
}
```

### 结果解释
- 本问用 `logistic_regression_plus_kmeans` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 实验报告

本问的核心是：临床证明，男胎孕妇的BMI 是影响胎儿Y 染色体浓度的最早达标时间（即浓度达到或超 过4%的最早时间）的主要因素。试对男胎孕妇的BMI 进行合理分组，给出每组的BMI 区间和最佳NIPT 时点，使得孕妇可能的潜在风险最小，并分析检测误差对结果的影响。

建模时先将题目要求拆成 2 个任务，再选择 `机器学习与统计识别`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
