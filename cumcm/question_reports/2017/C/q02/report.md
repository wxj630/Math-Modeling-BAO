# 2017-C 问题 2 建模求解实验报告

## 题目原文与任务拆解

- 题目：2017年 CUMCM C题：颜色与物质浓度辨识
- 问题：问题 2
- 原问：对附件Data2.xls中的数据，建立颜色读数和物质浓度的数学模型，并给出模型的误差分析

### 本问需要完成什么
- 任务 1：对附件Data2.xls中的数据，建立颜色读数和物质浓度的数学模型，并给出模型的误差分析

## 适配模型

- 主模型：颜色读数与物质浓度辨识模型（CH6：数据处理与拟合模型）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH6/第六章-数据处理与拟合模型.md

### 候选模型与适配理由
- 数据拟合与回归分析（CH6）：数据、分析；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH6/第六章-数据处理与拟合模型.md
- 概率统计与抽样检验（CH9）：误差；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH9/第九章-机器学习与统计模型.md

## 变量、约束与公式

### 建模假设
- 同一浓度下的多行颜色读数视为重复测量，颜色通道读数先标准化后建模。
- 水样浓度记为0ppm；空白单元格表示同一浓度或同一物质的重复观测。
- Data1用于比较5组数据的可辨识性，评价指标同时考虑组间分离、组内稳定、单调相关和交叉验证误差。
- Data2用于建立二氧化硫浓度预测模型，采用PLS提取颜色潜变量后用二次Ridge回归刻画非线性响应。
- 通用基线继续保留在 `cumcm/generic_baselines`，当前结果是从粗二次拟合推进到附件驱动颜色-浓度辨识的专用版本。

### 变量定义
- x=(R,G,B,H,S): 颜色读数向量
- c: 物质浓度(ppm)
- z=PLS(x): 颜色潜变量
- s_j: 第j组Data1数据质量评分

### 约束条件
- 训练和验证按真实附件样本进行，不合成颜色读数。
- 预测浓度截断到非负区间，避免物理上无意义的负浓度。
- 同一浓度重复观测既用于估计组内方差，也用于误差验证。

### 模型公式 / 目标函数
- `separation = mean(||mu_i-mu_j||) / (mean within scatter + eps)。`
- `quality = 0.35*separation_score + 0.25*monotonicity + 0.25*cv_score + 0.15*r2_score。`
- `z = PLSRegression(StandardScaler(x), c)，c_hat = Ridge(PolynomialFeatures(z, degree=2))。`
- `MAE = mean(|c-c_hat|), RMSE = sqrt(mean((c-c_hat)^2))。`

## Python 代码与运行方式

- 代码文件：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2017/C/q02/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2017/C/q02/solution.py`
- 批量运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：清洗Data1/Data2，前向填充物质名和浓度，水样转为0ppm。
- 步骤 2：对Data1每种物质分别计算颜色组间分离度、主方向单调性、留一浓度验证误差和训练拟合优度。
- 步骤 3：把指标归一化后生成5组数据的可辨识性排序和样本预测表。
- 步骤 4：对Data2训练PLS+二次Ridge模型，输出训练误差、留一误差、逐样本残差和颜色通道影响摘要。

## 实验结果与解释

### 产物文件
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2017/C/q02/data2_prediction_errors.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2017/C/q02/data2_error_summary.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2017/C/q02/data2_feature_coefficients.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2017/C/q02/experiment_table.csv

### 数据来源
- 类型：attachment
- 附件：/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2017_IqAO5Qqi8f23d8738a07a0604b8629ce9bb061ad/CUMCM2017Problems/C/Data1.xls; /Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2017_IqAO5Qqi8f23d8738a07a0604b8629ce9bb061ad/CUMCM2017Problems/C/Data2.xls
- 读取规模：73 行 x 7 列
- 说明：本题专用算法读取Data1的5种物质多浓度颜色读数和Data2二氧化硫重复测量数据，完成可辨识性排序、浓度预测模型和误差分析。

### result.json 核心结果

```json
{
  "method": "color_concentration_pls_ridge_error_analysis",
  "substance": "二氧化硫",
  "sample_count": 25,
  "group_count": 7,
  "pls_components": 3,
  "train_mae_ppm": 5.533963,
  "train_rmse_ppm": 7.613651,
  "train_r2": 0.977727,
  "loo_mae_ppm": 7.458539,
  "loo_rmse_ppm": 10.217607,
  "loo_r2": 0.959886,
  "report": [
    "Data2为二氧化硫颜色读数，水样按0ppm处理，其余空白浓度行按上一浓度重复测量处理。",
    "模型先用PLS提取颜色潜变量，再用二次Ridge回归描述颜色-浓度的非线性关系。",
    "误差分析同时输出训练误差、逐样本留一预测误差和按浓度分组的MAE/RMSE。"
  ]
}
```

### 结果解释
- 本问用 `color_concentration_pls_ridge_error_analysis` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 专用实验报告

- Data2为二氧化硫颜色读数，水样按0ppm处理，其余空白浓度行按上一浓度重复测量处理。
- 模型先用PLS提取颜色潜变量，再用二次Ridge回归描述颜色-浓度的非线性关系。
- 误差分析同时输出训练误差、逐样本留一预测误差和按浓度分组的MAE/RMSE。

## 实验报告

本问的核心是：对附件Data2.xls中的数据，建立颜色读数和物质浓度的数学模型，并给出模型的误差分析

建模时先将题目要求拆成 1 个任务，再选择 `颜色读数与物质浓度辨识模型`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
