# 2021-B 问题 1 建模求解实验报告

## 题目原文与任务拆解

- 题目：2021年 CUMCM B题：乙醇偶合制备 C4 烯烃
- 问题：问题 1
- 原问：对附件 1 中每种催化剂组合，分别研究乙醇转化率、C4 烯烃的选择性与温 度的关系， 并对附件 2 中 350 度时给定的催化剂组合在一次实验不同时间的测试结 果进行分析。

### 本问需要完成什么
- 任务 1：对附件 1 中每种催化剂组合，分别研究乙醇转化率、C4 烯烃的选择性与温 度的关系， 并对附件 2 中 350 度时给定的催化剂组合在一次实验不同时间的测试结 果进行分析

## 适配模型

- 主模型：乙醇偶合C4烯烃响应面拟合与实验设计（CH6：数据处理与拟合模型）
- 教程参考：../My-Agent/intro-mathmodel/docs/CH6/第六章-数据处理与拟合模型.md

### 候选模型与适配理由
- 启发式搜索与群体智能（CH5）：组合；参考 ../My-Agent/intro-mathmodel/docs/CH5/第五章-进化计算与群体智能.md
- 数据拟合与回归分析（CH6）：分析；参考 ../My-Agent/intro-mathmodel/docs/CH6/第六章-数据处理与拟合模型.md

## 变量、约束与公式

### 建模假设
- 附件1中同一催化剂组合跨温度的空白编号沿用上一行催化剂编号和组合说明。
- C4烯烃收率按题面定义取乙醇转化率与C4烯烃选择性的乘积再除以100。
- 温度-性能关系在实验温区内用二次响应面近似；离散催化剂组合用解析出的Co负载量、装料比、乙醇浓度和装料方式表征。
- 附件2稳定性测试在350摄氏度下分析时间趋势，不直接外推到其他温度。
- 新增5次实验优先选择预测收率高、温度低于或接近优选区、且与既有实验点有一定差异的候选点。

### 变量定义
- x_1: 温度T
- x_2: Co负载量wt%
- x_3: Co/SiO2装料质量
- x_4: HAP装料质量
- x_5: 乙醇进料浓度
- m: 装料方式A/B
- Y_conv: 乙醇转化率
- S_c4: C4烯烃选择性
- R_c4: C4烯烃收率

### 约束条件
- R_c4 = Y_conv * S_c4 / 100。
- 预测温度限制在附件1覆盖温区的邻近范围，默认250-400摄氏度。
- 低温优化情景要求T < 350摄氏度。
- 新增实验不得重复已有催化剂-温度组合。

### 模型公式 / 目标函数
- `per_catalyst: Y=a+bT+cT^2`
- `global_response: R_c4 = beta0 + beta1*T + beta2*T^2 + beta3*Co + beta4*ratio + beta5*flow + beta6*mode_B + epsilon`
- `influence_j = standardized linear coefficient or correlation score`
- `best_overall = argmax_{catalyst,T} predicted R_c4`
- `best_below_350 = argmax_{catalyst,T<350} predicted R_c4`
- `new_experiment_score = predicted_yield + 0.15*uncertainty_proxy + diversity_bonus`

## Python 代码与运行方式

- 代码文件：cumcm/question_solutions/2021/B/q01/solution.py
- 单问运行：`.venv/bin/python cumcm/question_solutions/2021/B/q01/solution.py`
- 批量运行：`.venv/bin/python cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：读取附件1性能数据并补全催化剂编号，按催化剂分别拟合转化率、选择性与温度的二次关系。
- 步骤 2：读取附件2稳定性测试，计算350摄氏度下转化率、C4选择性和收率随时间的线性趋势。
- 步骤 3：输出每个催化剂的温度响应摘要和稳定性趋势表。

## 实验结果与解释

### 产物文件
- cumcm/question_artifacts/2021/B/q01/temperature_response_by_catalyst.csv
- cumcm/question_artifacts/2021/B/q01/stability_trends.csv
- cumcm/question_artifacts/2021/B/q01/experiment_table.csv

### 数据来源
- 类型：attachment
- 附件：../../Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/B/附件1.xlsx; ../../Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/B/附件2.xlsx
- 读取规模：121 行 x 18 列
- 说明：本题专用算法读取附件1性能数据表和附件2稳定性测试，解析催化剂组合特征，计算C4烯烃收率并做响应面优化与新增实验设计。

### result.json 核心结果

```json
{
  "method": "ethanol_catalyst_temperature_response",
  "performance_sample_count": 114,
  "catalyst_count": 21,
  "stability_sample_count": 7,
  "best_observed": {
    "catalyst_id": "A3",
    "temperature_c": 400.0,
    "c4_yield_percent": 44.72806,
    "ethanol_conversion_percent": 83.713382,
    "c4_selectivity_percent": 53.43,
    "catalyst_combination": "200mg 1wt%Co/SiO2- 200mg HAP-乙醇浓度0.9ml/min"
  },
  "stability_trends": [
    {
      "target": "conversion",
      "start_value": 43.547389,
      "end_value": 29.906009,
      "slope_per_min": -0.05276089,
      "r2": 0.932923
    },
    {
      "target": "c4_selectivity",
      "start_value": 39.9,
      "end_value": 39.04,
      "slope_per_min": 0.00275353,
      "r2": 0.046419
    },
    {
      "target": "c4_yield",
      "start_value": 17.375408,
      "end_value": 11.675306,
      "slope_per_min": -0.01988796,
      "r2": 0.85748
    }
  ],
  "report": [
    "本问对附件1逐催化剂拟合温度-转化率、温度-C4选择性和温度-C4收率关系。",
    "附件2按时间做线性趋势分析，观察350摄氏度下催化剂活性衰减和选择性变化。",
    "输出 `temperature_response_by_catalyst.csv` 与 `stability_trends.csv` 作为论文分析表。"
  ]
}
```

### 结果解释
- 本问用 `ethanol_catalyst_temperature_response` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 专用实验报告

- 本问对附件1逐催化剂拟合温度-转化率、温度-C4选择性和温度-C4收率关系。
- 附件2按时间做线性趋势分析，观察350摄氏度下催化剂活性衰减和选择性变化。
- 输出 `temperature_response_by_catalyst.csv` 与 `stability_trends.csv` 作为论文分析表。

## 实验报告

本问的核心是：对附件 1 中每种催化剂组合，分别研究乙醇转化率、C4 烯烃的选择性与温 度的关系， 并对附件 2 中 350 度时给定的催化剂组合在一次实验不同时间的测试结 果进行分析。

建模时先将题目要求拆成 1 个任务，再选择 `乙醇偶合C4烯烃响应面拟合与实验设计`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
