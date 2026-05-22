# 2021-B 问题 3 建模求解实验报告

## 题目原文与任务拆解

- 题目：2021年 CUMCM B题：乙醇偶合制备 C4 烯烃
- 问题：问题 3
- 原问：如何选择催化剂组合与温度，使得在相同实验条件下 C4 烯烃收率尽可能 高。若使温度低于 350 度，又如何选择催化剂组合与温度，使得 C4 烯烃收率尽可 能高。

### 本问需要完成什么
- 任务 1：如何选择催化剂组合与温度，使得在相同实验条件下 C4 烯烃收率尽可能 高
- 任务 2：若使温度低于 350 度，又如何选择催化剂组合与温度，使得 C4 烯烃收率尽可 能高

## 适配模型

- 主模型：乙醇偶合C4烯烃响应面拟合与实验设计（CH6：数据处理与拟合模型）
- 教程参考：../My-Agent/intro-mathmodel/docs/CH6/第六章-数据处理与拟合模型.md

### 候选模型与适配理由
- 微分方程与动态仿真（CH2）：温度；参考 ../My-Agent/intro-mathmodel/docs/CH2/第2章-微分方程与动力系统.md
- 启发式搜索与群体智能（CH5）：组合；参考 ../My-Agent/intro-mathmodel/docs/CH5/第五章-进化计算与群体智能.md

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

- 代码文件：cumcm/question_solutions/2021/B/q03/solution.py
- 单问运行：`.venv/bin/python cumcm/question_solutions/2021/B/q03/solution.py`
- 批量运行：`.venv/bin/python cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：计算附件1每条实验的C4烯烃收率。
- 步骤 2：对每种催化剂组合建立温度-收率二次响应曲线，并在250-400摄氏度网格上预测。
- 步骤 3：分别搜索全温区最大收率和低于350摄氏度的最大收率方案。
- 步骤 4：输出响应面网格和优化结果表。

## 实验结果与解释

### 产物文件
- cumcm/question_artifacts/2021/B/q03/response_surface_grid.csv
- cumcm/question_artifacts/2021/B/q03/yield_optimization.csv

### 数据来源
- 类型：attachment
- 附件：../../Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/B/附件1.xlsx; ../../Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/B/附件2.xlsx
- 读取规模：121 行 x 18 列
- 说明：本题专用算法读取附件1性能数据表和附件2稳定性测试，解析催化剂组合特征，计算C4烯烃收率并做响应面优化与新增实验设计。

### result.json 核心结果

```json
{
  "method": "ethanol_coupling_c4_yield_optimization",
  "performance_sample_count": 114,
  "catalyst_count": 21,
  "best_overall": {
    "catalyst_id": "A2",
    "temperature_c": 400.0,
    "c4_yield_percent": 56.583721,
    "catalyst_combination": "200mg 2wt%Co/SiO2- 200mg HAP-乙醇浓度1.68ml/min"
  },
  "best_below_350": {
    "catalyst_id": "A2",
    "temperature_c": 349.0,
    "c4_yield_percent": 26.459214,
    "catalyst_combination": "200mg 2wt%Co/SiO2- 200mg HAP-乙醇浓度1.68ml/min"
  },
  "report": [
    "本问按题面定义计算C4烯烃收率，并对每个催化剂组合拟合温度-收率二次响应曲线。",
    "在250-400摄氏度网格上搜索最大预测收率，同时单独给出低于350摄氏度约束下的最优方案。",
    "响应面网格和优化结果分别写入 `response_surface_grid.csv` 与 `yield_optimization.csv`。"
  ]
}
```

### 结果解释
- 本问用 `ethanol_coupling_c4_yield_optimization` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 专用实验报告

- 本问按题面定义计算C4烯烃收率，并对每个催化剂组合拟合温度-收率二次响应曲线。
- 在250-400摄氏度网格上搜索最大预测收率，同时单独给出低于350摄氏度约束下的最优方案。
- 响应面网格和优化结果分别写入 `response_surface_grid.csv` 与 `yield_optimization.csv`。

## 实验报告

本问的核心是：如何选择催化剂组合与温度，使得在相同实验条件下 C4 烯烃收率尽可能 高。若使温度低于 350 度，又如何选择催化剂组合与温度，使得 C4 烯烃收率尽可 能高。

建模时先将题目要求拆成 2 个任务，再选择 `乙醇偶合C4烯烃响应面拟合与实验设计`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
