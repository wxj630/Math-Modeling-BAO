# 2021-E 问题 4 建模求解实验报告

## 题目原文与任务拆解

- 题目：2021年 CUMCM E题：中药材的鉴别
- 问题：问题 4
- 原问：附件 4 给出了几种药材的近红外光谱数据，试鉴别药材的类别与产 地，并将下表中所给出编号的药材类别与产地的鉴别结果填入表各中。 No 94 109 140 278 308 330 347 Class OP

### 本问需要完成什么
- 任务 1：附件 4 给出了几种药材的近红外光谱数据，试鉴别药材的类别与产 地，并将下表中所给出编号的药材类别与产地的鉴别结果填入表各中

## 适配模型

- 主模型：红外光谱预处理、特征降维与药材鉴别（CH9：机器学习与统计模型）
- 教程参考：../My-Agent/intro-mathmodel/docs/CH9/第九章-机器学习与统计模型.md

### 候选模型与适配理由
- 图像文本与信号特征（CH10）：光谱；参考 ../My-Agent/intro-mathmodel/docs/CH10/第10章-图像、文本与信号数据.md
- 机器学习与统计识别（CH9）：鉴别；参考 ../My-Agent/intro-mathmodel/docs/CH9/第九章-机器学习与统计模型.md
- 数据拟合与回归分析（CH6）：数据；参考 ../My-Agent/intro-mathmodel/docs/CH6/第六章-数据处理与拟合模型.md

## 变量、约束与公式

### 建模假设
- 附件中的每一行表示一个药材样本，No为样本编号，Class为药材类别，OP为产地，后续列为各波数下的吸光度。
- 吸光度可能为负值，保留原始校正值；缺失光谱点用同一波数列均值填补。
- 分类前对每条光谱做Savitzky-Golay一阶导数和平行标准正态变换，以削弱基线漂移和总体强度差异。
- 题目表格中留空的编号只参与预测，不用于模型训练；验证精度来自有标签样本的分层留出集。
- 通用基线集中保留在 `cumcm/generic_baselines`，当前结果是从通用聚类/拟合推进到附件光谱鉴别的专用版本。

### 变量定义
- X_i(lambda): 第i个样本在波数lambda处的吸光度
- z_i: 经导数、SNV和降维后的光谱特征向量
- c_i: 药材类别Class
- o_i: 药材产地OP
- p(y|z_i): 分类器给出的类别或产地概率

### 约束条件
- 训练集只使用Class/OP非空的样本。
- 预测目标编号必须与题目表格给定No一致。
- 第3问近红外和中红外按同一No对齐后进行特征融合。
- 输出表保留样本编号、预测类别/产地和最大投票概率，便于直接填表。

### 模型公式 / 目标函数
- `SNV(x_i)=(x_i-mean(x_i))/std(x_i)`
- `d_i(lambda)=SavitzkyGolayDerivative(x_i(lambda))`
- `Q1: choose k maximizing silhouette(KMeans(PCA(SNV(X)), k)), k in [2,8]`
- `Q2/Q3/Q4: y_hat=ExtraTreesClassifier(SNV(derivative(X)))`
- `validation_accuracy = mean(y_hat_j == y_j) on stratified holdout`

## Python 代码与运行方式

- 代码文件：cumcm/question_solutions/2021/E/q04/solution.py
- 单问运行：`.venv/bin/python cumcm/question_solutions/2021/E/q04/solution.py`
- 批量运行：`.venv/bin/python cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：读取附件4近红外光谱，分别构建Class和OP两个监督学习任务。
- 步骤 2：用Class非空样本训练类别分类器，用OP非空样本训练产地分类器。
- 步骤 3：对题面7个编号同时输出Class和OP预测，并给出两个分类器的验证精度。

## 实验结果与解释

### 产物文件
- cumcm/question_artifacts/2021/E/q04/class_origin_predictions_attachment4.csv
- cumcm/question_artifacts/2021/E/q04/class_origin_validation_metrics.csv
- cumcm/question_artifacts/2021/E/q04/experiment_table.csv

### 数据来源
- 类型：attachment
- 附件：../../Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/E/附件4.xlsx
- 读取规模：399 行 x 5999 列
- 说明：本题专用算法读取中药材近/中红外光谱附件，按题问分别完成无监督类别分群、OP产地分类、近/中红外融合分类以及Class+OP联合填表预测。

### result.json 核心结果

```json
{
  "method": "herbal_near_ir_class_origin_classifier",
  "sample_count": 399,
  "wavelength_count": 5996,
  "target_count": 7,
  "class_labeled_count": 256,
  "origin_labeled_count": 349,
  "class_count": 3,
  "origin_class_count": 16,
  "class_validation_accuracy": 1.0,
  "origin_validation_accuracy": 0.931818,
  "target_predictions": [
    {
      "No": 94,
      "predicted_Class": "A",
      "class_confidence": 1.0,
      "predicted_OP": "5",
      "op_confidence": 0.606667
    },
    {
      "No": 109,
      "predicted_Class": "A",
      "class_confidence": 1.0,
      "predicted_OP": "3",
      "op_confidence": 0.683333
    },
    {
      "No": 140,
      "predicted_Class": "A",
      "class_confidence": 1.0,
      "predicted_OP": "1",
      "op_confidence": 0.696667
    },
    {
      "No": 278,
      "predicted_Class": "C",
      "class_confidence": 1.0,
      "predicted_OP": "1",
      "op_confidence": 0.73
    },
    {
      "No": 308,
      "predicted_Class": "C",
      "class_confidence": 0.993333,
      "predicted_OP": "3",
      "op_confidence": 0.973333
    },
    {
      "No": 330,
      "predicted_Class": "C",
      "class_confidence": 1.0,
      "predicted_OP": "4",
      "op_confidence": 0.893333
    },
    {
      "No": 347,
      "predicted_Class": "B",
      "class_confidence": 1.0,
      "predicted_OP": "11",
      "op_confidence": 0.836667
    }
  ],
  "report": [
    "附件4同时存在Class缺失和OP缺失，因此分别训练药材类别分类器和产地分类器。",
    "题面指定7个编号的Class与OP均为空，最终表同时给出类别、产地和模型投票置信度。",
    "输出 `class_origin_predictions_attachment4.csv` 可直接填入问题4表格。"
  ]
}
```

### 结果解释
- 本问用 `herbal_near_ir_class_origin_classifier` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 专用实验报告

- 附件4同时存在Class缺失和OP缺失，因此分别训练药材类别分类器和产地分类器。
- 题面指定7个编号的Class与OP均为空，最终表同时给出类别、产地和模型投票置信度。
- 输出 `class_origin_predictions_attachment4.csv` 可直接填入问题4表格。

## 实验报告

本问的核心是：附件 4 给出了几种药材的近红外光谱数据，试鉴别药材的类别与产 地，并将下表中所给出编号的药材类别与产地的鉴别结果填入表各中。 No 94 109 140 278 308 330 347 Class OP

建模时先将题目要求拆成 1 个任务，再选择 `红外光谱预处理、特征降维与药材鉴别`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
