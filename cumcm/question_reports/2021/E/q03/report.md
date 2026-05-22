# 2021-E 问题 3 建模求解实验报告

## 题目原文与任务拆解

- 题目：2021年 CUMCM E题：中药材的鉴别
- 问题：问题 3
- 原问：根据附件 3 中某一种药材的近红外和中红外数据，试鉴别该种药材 的产地，并将下表中所给出编号的药材产地的鉴别结果填入表中。 No 4 15 22 30 34 45 74 114 170 209 OP

### 本问需要完成什么
- 任务 1：根据附件 3 中某一种药材的近红外和中红外数据，试鉴别该种药材 的产地，并将下表中所给出编号的药材产地的鉴别结果填入表中

## 适配模型

- 主模型：红外光谱预处理、特征降维与药材鉴别（CH9：机器学习与统计模型）
- 教程参考：../My-Agent/intro-mathmodel/docs/CH9/第九章-机器学习与统计模型.md

### 候选模型与适配理由
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

- 代码文件：cumcm/question_solutions/2021/E/q03/solution.py
- 单问运行：`.venv/bin/python cumcm/question_solutions/2021/E/q03/solution.py`
- 批量运行：`.venv/bin/python cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：读取附件3近红外和中红外两张表，按No对齐样本和OP标签。
- 步骤 2：分别预处理两类光谱后进行特征拼接，训练融合产地分类器。
- 步骤 3：输出题面10个编号的OP预测以及融合模型验证指标。

## 实验结果与解释

### 产物文件
- cumcm/question_artifacts/2021/E/q03/fusion_origin_predictions_attachment3.csv
- cumcm/question_artifacts/2021/E/q03/fusion_validation_metrics.csv
- cumcm/question_artifacts/2021/E/q03/experiment_table.csv

### 数据来源
- 类型：attachment
- 附件：../../Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/E/附件3.xlsx
- 读取规模：510 行 x 9448 列
- 说明：本题专用算法读取中药材近/中红外光谱附件，按题问分别完成无监督类别分群、OP产地分类、近/中红外融合分类以及Class+OP联合填表预测。

### result.json 核心结果

```json
{
  "method": "herbal_near_mid_ir_fusion_origin_classifier",
  "sample_count": 255,
  "near_wavelength_count": 5996,
  "mid_wavelength_count": 3448,
  "labeled_sample_count": 245,
  "target_count": 10,
  "origin_class_count": 17,
  "validation_accuracy": 0.951613,
  "validation_balanced_accuracy": 0.955882,
  "target_predictions": [
    {
      "No": 4,
      "predicted_OP": "17",
      "confidence": 0.696667
    },
    {
      "No": 15,
      "predicted_OP": "11",
      "confidence": 0.853333
    },
    {
      "No": 22,
      "predicted_OP": "1",
      "confidence": 0.73
    },
    {
      "No": 30,
      "predicted_OP": "2",
      "confidence": 0.9
    },
    {
      "No": 34,
      "predicted_OP": "16",
      "confidence": 0.926667
    },
    {
      "No": 45,
      "predicted_OP": "3",
      "confidence": 0.616667
    },
    {
      "No": 74,
      "predicted_OP": "4",
      "confidence": 0.956667
    },
    {
      "No": 114,
      "predicted_OP": "10",
      "confidence": 0.923333
    },
    {
      "No": 170,
      "predicted_OP": "9",
      "confidence": 0.89
    },
    {
      "No": 209,
      "predicted_OP": "14",
      "confidence": 0.83
    }
  ],
  "report": [
    "附件3的近红外和中红外按No一一对齐，分别预处理后拼接成融合特征。",
    "融合模型利用两种光谱的互补信息识别17个产地类别，并预测题面10个空缺OP。",
    "输出 `fusion_origin_predictions_attachment3.csv` 可直接填入问题3表格。"
  ]
}
```

### 结果解释
- 本问用 `herbal_near_mid_ir_fusion_origin_classifier` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 专用实验报告

- 附件3的近红外和中红外按No一一对齐，分别预处理后拼接成融合特征。
- 融合模型利用两种光谱的互补信息识别17个产地类别，并预测题面10个空缺OP。
- 输出 `fusion_origin_predictions_attachment3.csv` 可直接填入问题3表格。

## 实验报告

本问的核心是：根据附件 3 中某一种药材的近红外和中红外数据，试鉴别该种药材 的产地，并将下表中所给出编号的药材产地的鉴别结果填入表中。 No 4 15 22 30 34 45 74 114 170 209 OP

建模时先将题目要求拆成 1 个任务，再选择 `红外光谱预处理、特征降维与药材鉴别`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
