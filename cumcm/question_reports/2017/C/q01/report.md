# 2017-C 问题 1 建模求解实验报告

## 题目原文与任务拆解

- 题目：2017年 CUMCM C题：颜色与物质浓度辨识
- 问题：问题 1
- 原问：附件Data1.xls中分别给出了5种物质在不同浓度下的颜色读数，讨论从这5组数据中能否确定颜色读数和物质浓度之间的关系，并给出一些准则来评价这5组数据的优劣

### 本问需要完成什么
- 任务 1：附件Data1.xls中分别给出了5种物质在不同浓度下的颜色读数，讨论从这5组数据中能否确定颜色读数和物质浓度之间的关系，并给出一些准则来评价这5组数据的优劣

## 适配模型

- 主模型：颜色读数与物质浓度辨识模型（CH7：权重生成与评价模型）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH7/第7章-权重生成与评价模型.md

### 候选模型与适配理由
- 数据拟合与回归分析（CH6）：数据；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH6/第六章-数据处理与拟合模型.md
- 综合评价与权重决策（CH7）：评价；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH7/第7章-权重生成与评价模型.md

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

- 代码文件：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2017/C/q01/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2017/C/q01/solution.py`
- 批量运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：清洗Data1/Data2，前向填充物质名和浓度，水样转为0ppm。
- 步骤 2：对Data1每种物质分别计算颜色组间分离度、主方向单调性、留一浓度验证误差和训练拟合优度。
- 步骤 3：把指标归一化后生成5组数据的可辨识性排序和样本预测表。
- 步骤 4：对Data2训练PLS+二次Ridge模型，输出训练误差、留一误差、逐样本残差和颜色通道影响摘要。

## 实验结果与解释

### 产物文件
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2017/C/q01/data1_group_quality.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2017/C/q01/data1_sample_predictions.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2017/C/q01/experiment_table.csv

### 数据来源
- 类型：attachment
- 附件：/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2017_IqAO5Qqi8f23d8738a07a0604b8629ce9bb061ad/CUMCM2017Problems/C/Data1.xls; /Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2017_IqAO5Qqi8f23d8738a07a0604b8629ce9bb061ad/CUMCM2017Problems/C/Data2.xls
- 读取规模：73 行 x 7 列
- 说明：本题专用算法读取Data1的5种物质多浓度颜色读数和Data2二氧化硫重复测量数据，完成可辨识性排序、浓度预测模型和误差分析。

### result.json 核心结果

```json
{
  "method": "color_concentration_identifiability_ranking",
  "substance_count": 5,
  "sample_count": 48,
  "best_substance": "工业碱",
  "best_quality_score": 0.899436,
  "mean_group_cv_mae_ppm": 132.049014,
  "ranking": [
    {
      "rank": 1,
      "substance": "工业碱",
      "sample_count": 7,
      "concentration_count": 7,
      "min_concentration_ppm": 0.0,
      "max_concentration_ppm": 11.8,
      "separation_ratio": 129290666971.88832,
      "spearman_abs_pc1_concentration": 0.892857,
      "train_mae_ppm": 1.570626,
      "loo_mae_ppm": 3.909871,
      "leave_one_concentration_mae_ppm": 3.909871,
      "train_r2": 0.518703,
      "quality_score": 0.899436
    },
    {
      "rank": 2,
      "substance": "硫酸铝钾",
      "sample_count": 6,
      "concentration_count": 6,
      "min_concentration_ppm": 0.0,
      "max_concentration_ppm": 5.0,
      "separation_ratio": 66459777059.944115,
      "spearman_abs_pc1_concentration": 0.885714,
      "train_mae_ppm": 0.681665,
      "loo_mae_ppm": 1.209778,
      "leave_one_concentration_mae_ppm": 1.209778,
      "train_r2": 0.61303,
      "quality_score": 0.742805
    },
    {
      "rank": 3,
      "substance": "组胺",
      "sample_count": 10,
      "concentration_count": 5,
      "min_concentration_ppm": 0.0,
      "max_concentration_ppm": 100.0,
      "separation_ratio": 21.175728,
      "spearman_abs_pc1_concentration": 0.984732,
      "train_mae_ppm": 2.429538,
      "loo_mae_ppm": 4.183573,
      "leave_one_concentration_mae_ppm": 15.080403,
      "train_r2": 0.993728,
      "quality_score": 0.639135
    },
    {
      "rank": 4,
      "substance": "溴酸钾",
      "sample_count": 10,
      "concentration_count": 5,
      "min_concentration_ppm": 0.0,
      "max_concentration_ppm": 100.0,
      "separation_ratio": 66.505876,
      "spearman_abs_pc1_concentration": 0.984732,
      "train_mae_ppm": 1.561983,
      "loo_mae_ppm": 3.054742,
      "leave_one_concentration_mae_ppm": 22.688144,
      "train_r2": 0.997509,
      "quality_score": 0.636622
    },
    {
      "rank": 5,
      "substance": "奶中尿素",
      "sample_count": 15,
      "concentration_count": 6,
      "min_concentration_ppm": 0.0,
      "max_concentration_ppm": 2000.0,
      "separation_ratio": 3.448139,
      "spearman_abs_pc1_concentration": 0.897659,
      "train_mae_ppm": 226.706865,
      "loo_mae_ppm": 500.335856,
      "leave_one_concentration_mae_ppm": 617.356872,
      "train_r2": 0.852067,
      "quality_score": 0.352225
    }
  ],
  "report": [
    "Data1按5种物质分别建模，质量评价综合颜色组间分离度、主成分单调性、交叉验证误差和训练拟合优度。",
    "当前评分最高的是工业碱，说明其颜色读数随浓度变化最稳定、最容易辨识。",
    "输出 `data1_group_quality.csv` 作为五组数据优劣准则，`data1_sample_predictions.csv` 保留逐样本预测与误差。"
  ]
}
```

### 结果解释
- 本问用 `color_concentration_identifiability_ranking` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 专用实验报告

- Data1按5种物质分别建模，质量评价综合颜色组间分离度、主成分单调性、交叉验证误差和训练拟合优度。
- 当前评分最高的是工业碱，说明其颜色读数随浓度变化最稳定、最容易辨识。
- 输出 `data1_group_quality.csv` 作为五组数据优劣准则，`data1_sample_predictions.csv` 保留逐样本预测与误差。

## 实验报告

本问的核心是：附件Data1.xls中分别给出了5种物质在不同浓度下的颜色读数，讨论从这5组数据中能否确定颜色读数和物质浓度之间的关系，并给出一些准则来评价这5组数据的优劣

建模时先将题目要求拆成 1 个任务，再选择 `颜色读数与物质浓度辨识模型`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
