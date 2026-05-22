# 2019-D 问题 3 建模求解实验报告

## 题目原文与任务拆解

- 题目：2019年 CUMCM D题：空气质量数据的校准
- 问题：问题 3
- 原问：利用国控点数据，建立数学模型对自建点数据进行校准。

### 本问需要完成什么
- 任务 1：利用国控点数据，建立数学模型对自建点数据进行校准

## 适配模型

- 主模型：空气质量自建点数据校准模型（CH9：机器学习与统计模型）
- 教程参考：../My-Agent/intro-mathmodel/docs/CH9/第九章-机器学习与统计模型.md

### 候选模型与适配理由
- 数据拟合与回归分析（CH6）：数据、校准；参考 ../My-Agent/intro-mathmodel/docs/CH6/第六章-数据处理与拟合模型.md

## 变量、约束与公式

### 建模假设
- 附件1国控点小时数据作为校准真值，附件2自建点分钟级数据按小时聚合后与国控点对齐。
- 同一小时内自建点多次观测取均值，气象变量也取小时均值。
- 差异定义为 self_built - national，用于探索零点漂移、量程漂移、交叉干扰和天气影响。
- 校准模型只使用自建点污染物、气象变量和时间特征预测国控点污染物，不把目标时刻国控点值泄漏为特征。
- 通用基线保留在 `cumcm/generic_baselines`，当前结果是从粗二次拟合推进到附件驱动空气质量校准的专用版本。

### 变量定义
- x_t: 自建点六污染物、气象和时间特征
- y_t: 国控点六污染物浓度
- e_t=x_pollutant-y_t: 自建点偏差
- f_j(x_t): 第j种污染物的校准函数

### 约束条件
- 时间对齐后仅保留国控点和自建点同时存在的小时。
- 校准预测值截断为非负浓度。
- 训练/测试按时间顺序切分，避免未来数据参与过去校准。

### 模型公式 / 目标函数
- `bias_j = mean(self_j - national_j)。`
- `corr_j = corr(self_j, national_j)。`
- `factor_importance = RandomForestRegressor(residual_j | pollutants, weather, time).feature_importances_。`
- `calibrated_y = RandomForestRegressor(national pollutants | self pollutants, weather, time)。`
- `improvement = (MAE_before - MAE_after) / MAE_before。`

## Python 代码与运行方式

- 代码文件：cumcm/question_solutions/2019/D/q03/solution.py
- 单问运行：`.venv/bin/python cumcm/question_solutions/2019/D/q03/solution.py`
- 批量运行：`.venv/bin/python cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：读取GBK编码CSV，解析时间并将附件2自建点分钟数据按小时聚合。
- 步骤 2：将附件1国控点数据与自建点小时均值按时间内连接。
- 步骤 3：第1问输出污染物均值、偏差、相关系数、MAE和RMSE。
- 步骤 4：第2问对每种污染物残差训练因素分析模型，输出特征重要性和天气相关性。
- 步骤 5：第3问按时间切分训练/测试，训练多输出校准模型并比较校准前后误差。

## 实验结果与解释

### 产物文件
- cumcm/question_artifacts/2019/D/q03/hourly_aligned_air_quality.csv
- cumcm/question_artifacts/2019/D/q03/pollutant_eda_summary.csv
- cumcm/question_artifacts/2019/D/q03/calibration_model_metrics.csv
- cumcm/question_artifacts/2019/D/q03/calibrated_hourly_predictions.csv
- cumcm/question_artifacts/2019/D/q03/experiment_table.csv

### 数据来源
- 类型：attachment
- 附件：../../Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/D-2019中文/附件1.csv; ../../Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/D-2019中文/附件2.csv; ../../Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/D-2019中文/附件3.docx
- 读取规模：238917 行 x 19 列
- 说明：本题专用算法读取国控点小时数据和自建点分钟级污染物/气象数据，完成小时对齐、差异因素分析和多污染物校准。

### result.json 核心结果

```json
{
  "method": "air_quality_multitarget_calibration",
  "matched_hour_count": 4137,
  "train_sample_count": 3309,
  "test_sample_count": 828,
  "mean_mae_before_calibration": 14.905786,
  "mean_mae_after_calibration": 12.157978,
  "mean_improvement_percent": 15.143425,
  "best_improved_pollutant": "NO2",
  "report": [
    "校准模型以自建点污染物、气象变量和时间特征预测国控点六污染物。",
    "按时间顺序前80%训练、后20%测试，避免随机切分导致未来信息泄漏。",
    "输出校准前后MAE/RMSE/R2和测试期逐小时校准结果，用于检验模型有效性。"
  ]
}
```

### 结果解释
- 本问用 `air_quality_multitarget_calibration` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 专用实验报告

- 校准模型以自建点污染物、气象变量和时间特征预测国控点六污染物。
- 按时间顺序前80%训练、后20%测试，避免随机切分导致未来信息泄漏。
- 输出校准前后MAE/RMSE/R2和测试期逐小时校准结果，用于检验模型有效性。

## 实验报告

本问的核心是：利用国控点数据，建立数学模型对自建点数据进行校准。

建模时先将题目要求拆成 1 个任务，再选择 `空气质量自建点数据校准模型`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
