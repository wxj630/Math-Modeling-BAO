# 2021-C 问题 1 建模求解实验报告

## 题目原文与任务拆解

- 题目：2021年 CUMCM C题：生产企业原材料的订购与运输
- 问题：问题 1
- 原问：根据附件1，对402 家供应商的供货特征进行量化分析，建立反映保障企业生产 重要性的数学模型，在此基础上确定50 家最重要的供应商， 并在论文中列表给出结果。

### 本问需要完成什么
- 任务 1：根据附件1，对402 家供应商的供货特征进行量化分析，建立反映保障企业生产 重要性的数学模型，在此基础上确定50 家最重要的供应商， 并在论文中列表给出结果

## 适配模型

- 主模型：供应商评价与订购转运规划（CH7：权重生成与评价模型）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH7/第7章-权重生成与评价模型.md

### 候选模型与适配理由
- 数据拟合与回归分析（CH6）：分析；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH6/第六章-数据处理与拟合模型.md

## 变量、约束与公式

### 建模假设
- 附件1的近240周订货量、供货量可代表供应商未来短期供给能力和履约稳定性。
- A、B、C类原材料单位产品消耗量分别为0.60、0.66、0.72立方米，采购单价相对C类分别为1.20、1.10、1.00。
- 每家转运商每周运输能力为6000立方米，供应商每周供货尽量由一家转运商承运；超出容量时才拆分。
- 未来24周计划使用历史近48周和近24周供给统计形成稳健供给上限，方案结果是可复现实验基线而非官方唯一最优解。

### 变量定义
- s_i: 第 i 家供应商的重要性综合得分
- x_{i,t}: 第 t 周向供应商 i 的订货量
- y_{i,t}: 第 t 周供应商 i 的预期供货量
- z_{i,k,t}: 第 t 周由转运商 k 承运供应商 i 的供货量
- I_t: 第 t 周折算为产成品体积的可用接收原料能力

### 约束条件
- 0 <= y_{i,t} <= cap_i，其中 cap_i 由供应商近48周稳健供给能力估计。
- sum_i received_{i,t}/coef_i >= 28200，保证每周2.82万立方米产能需求。
- sum_i z_{i,k,t} <= 6000，任一转运商每周承运量不超过6000立方米。
- sum_k z_{i,k,t} = y_{i,t}，所有预期供货量均安排转运。
- 问题3增加A类优先、C类惩罚；问题4放松产能目标并最大化可实现周产能。

### 模型公式 / 目标函数
- `s_i = 0.35*capacity_i + 0.25*reliability_i + 0.15*stability_i + 0.15*activity_i + 0.10*efficiency_i`
- `capacity_i = normalize(sum_t supply_{i,t}/coef_i)`
- `reliability_i = clip(1 - mean_t |supply_{i,t}-order_{i,t}|/(order_{i,t}+1), 0, 1)`
- `取 s_i 最高的50家作为最重要供应商。`

## Python 代码与运行方式

- 代码文件：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2021/C/q01/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2021/C/q01/solution.py`
- 批量运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：读取附件1的订货量和供货量两个工作表。
- 步骤 2：按供应总量、履约可靠性、供给稳定性、活跃周比例和材料效率构造指标。
- 步骤 3：对指标做0-1标准化并加权得到重要性得分。
- 步骤 4：输出402家供应商评分表和前50家供应商清单。

## 实验结果与解释

### 产物文件
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2021/C/q01/supplier_importance_scores.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2021/C/q01/top50_suppliers.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2021/C/q01/experiment_table.csv

### 数据来源
- 类型：attachment
- 附件：/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/C/附件1 近5年402家供应商的相关数据.xlsx; /Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/C/附件2 近5年8家转运商的相关数据.xlsx; /Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/C/附件A 订购方案数据结果.xlsx; /Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/C/附件B 转运方案数据结果.xlsx
- 读取规模：410 行 x 240 列
- 说明：本题专用算法读取附件1的402家供应商240周订货/供货量、附件2的8家转运商240周损耗率，并按附件A/B模板生成24周订购与转运方案。

### result.json 核心结果

```json
{
  "method": "supplier_importance_entropy_weighted_score",
  "supplier_count": 402,
  "top50_supplier_ids": [
    "S229",
    "S361",
    "S275",
    "S329",
    "S282",
    "S268",
    "S306",
    "S194",
    "S151",
    "S356",
    "S352",
    "S108",
    "S340",
    "S247",
    "S143",
    "S131",
    "S365",
    "S140",
    "S294",
    "S284",
    "S308",
    "S330",
    "S218",
    "S266",
    "S244",
    "S080",
    "S123",
    "S031",
    "S348",
    "S346",
    "S189",
    "S067",
    "S314",
    "S307",
    "S040",
    "S003",
    "S213",
    "S076",
    "S395",
    "S005",
    "S374",
    "S139",
    "S367",
    "S007",
    "S364",
    "S037",
    "S114",
    "S046",
    "S269",
    "S211"
  ],
  "top10_suppliers": [
    {
      "supplier_id": "S229",
      "material": "A",
      "importance_score": 0.96091,
      "rank": 1,
      "total_supplied_m3": 354887.0,
      "total_product_equivalent_m3": 591478.333333,
      "robust_weekly_supply_m3": 1574.55,
      "robust_weekly_product_m3": 2624.25,
      "fulfillment_ratio": 0.986112,
      "reliability_score": 0.987771,
      "stability_score": 0.759783,
      "active_week_ratio": 1.0,
      "unit_raw_cost_index": 1.2,
      "raw_per_product_m3": 0.6
    },
    {
      "supplier_id": "S361",
      "material": "C",
      "importance_score": 0.881942,
      "rank": 2,
      "total_supplied_m3": 328080.0,
      "total_product_equivalent_m3": 455666.666667,
      "robust_weekly_supply_m3": 1488.2,
      "robust_weekly_product_m3": 2066.944444,
      "fulfillment_ratio": 0.98389,
      "reliability_score": 0.985577,
      "stability_score": 0.772785,
      "active_week_ratio": 1.0,
      "unit_raw_cost_index": 1.0,
      "raw_per_product_m3": 0.72
    },
    {
      "supplier_id": "S275",
      "material": "A",
      "importance_score": 0.78167,
      "rank": 3,
      "total_supplied_m3": 158553.0,
      "total_product_equivalent_m3": 264255.0,
      "robust_weekly_supply_m3": 708.75,
      "robust_weekly_product_m3": 1181.25,
      "fulfillment_ratio": 1.002548,
      "reliability_score": 0.990384,
      "stability_score": 0.851445,
      "active_week_ratio": 1.0,
      "unit_raw_cost_index": 1.2,
      "raw_per_product_m3": 0.6
    },
    {
      "supplier_id": "S329",
      "material": "A",
      "importance_score": 0.778287,
      "rank": 4,
      "total_supplied_m3": 156518.0,
      "total_product_equivalent_m3": 260863.333333,
      "robust_weekly_supply_m3": 676.0,
      "robust_weekly_product_m3": 1126.666667,
      "fulfillment_ratio": 1.001075,
      "reliability_score": 0.988349,
      "stability_score": 0.845668,
      "active_week_ratio": 1.0,
      "unit_raw_cost_index": 1.2,
      "raw_per_product_m3": 0.6
    },
    {
      "supplier_id": "S282",
      "material": "A",
      "importance_score": 0.760721,
      "rank": 5,
      "total_supplied_m3": 169340.0,
      "total_product_equivalent_m3": 282233.333333,
      "robust_weekly_supply_m3": 994.55,
      "robust_weekly_product_m3": 1657.583333,
      "fulfillment_ratio": 1.0048,
      "reliability_score": 0.98706,
      "stability_score": 0.646402,
      "active_week_ratio": 1.0,
      "unit_raw_cost_index": 1.2,
      "raw_per_product_m3": 0.6
    },
    {
      "supplier_id": "S268",
      "material": "C",
      "importance_score": 0.736047,
      "rank": 6,
      "total_supplied_m3": 129786.0,
      "total_product_equivalent_m3": 180258.333333,
      "robust_weekly_supply_m3": 540.775,
      "robust_weekly_product_m3": 751.076389,
      "fulfillment_ratio": 1.003216,
      "reliability_score": 0.986994,
      "stability_score": 0.884324,
      "active_week_ratio": 1.0,
      "unit_raw_cost_index": 1.0,
      "raw_per_product_m3": 0.72
    },
    {
      "supplier_id": "S306",
      "material": "C",
      "importance_score": 0.723157,
      "rank": 7,
      "total_supplied_m3": 126096.0,
      "total_product_equivalent_m3": 175133.333333,
      "robust_weekly_supply_m3": 547.1,
      "robust_weekly_product_m3": 759.861111,
      "fulfillment_ratio": 1.00331,
      "reliability_score": 0.986533,
      "stability_score": 0.819379,
      "active_week_ratio": 1.0,
      "unit_raw_cost_index": 1.0,
      "raw_per_product_m3": 0.72
    },
    {
      "supplier_id": "S194",
      "material": "C",
      "importance_score": 0.710634,
      "rank": 8,
      "total_supplied_m3": 101365.0,
      "total_product_equivalent_m3": 140784.722222,
      "robust_weekly_supply_m3": 425.1,
      "robust_weekly_product_m3": 590.416667,
      "fulfillment_ratio": 0.999852,
      "reliability_score": 0.982048,
      "stability_score": 0.878882,
      "active_week_ratio": 1.0,
      "unit_raw_cost_index": 1.0,
      "raw_per_product_m3": 0.72
    },
    {
      "supplier_id": "S151",
      "material": "C",
      "importance_score": 0.698317,
      "rank": 9,
      "total_supplied_m3": 194498.0,
      "total_product_equivalent_m3": 270136.111111,
      "robust_weekly_supply_m3": 810.408333,
      "robust_weekly_product_m3": 1125.56713,
      "fulfillment_ratio": 0.729796,
      "reliability_score": 0.969135,
      "stability_score": 0.307971,
      "active_week_ratio": 1.0,
      "unit_raw_cost_index": 1.0,
      "raw_per_product_m3": 0.72
    },
    {
      "supplier_id": "S356",
      "material": "C",
      "importance_score": 0.691707,
      "rank": 10,
      "total_supplied_m3": 130307.0,
      "total_product_equivalent_m3": 180981.944444,
      "robust_weekly_supply_m3": 773.25,
      "robust_weekly_product_m3": 1073.958333,
      "fulfillment_ratio": 0.982618,
      "reliability_score": 0.975105,
      "stability_score": 0.605686,
      "active_week_ratio": 1.0,
      "unit_raw_cost_index": 1.0,
      "raw_per_product_m3": 0.72
    }
  ],
  "score_formula": "0.35 capacity + 0.25 reliability + 0.15 stability + 0.15 activity + 0.10 material efficiency",
  "report": [
    "问题1把“保障企业生产重要性”拆成供给规模、履约可靠性、供给稳定性、活跃程度和材料效率五类指标。",
    "供给规模使用240周累计供货折算为产成品体积，避免只看原料立方米导致A/B/C材料不可比。",
    "可靠性使用有订货周的相对偏差，稳定性使用正供货周均值/(均值+标准差)，活跃程度使用非零供货周比例。",
    "实验得到前50家供应商，前10家为：S229, S361, S275, S329, S282, S268, S306, S194, S151, S356。"
  ]
}
```

### 结果解释
- 本问用 `supplier_importance_entropy_weighted_score` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 专用实验报告

- 问题1把“保障企业生产重要性”拆成供给规模、履约可靠性、供给稳定性、活跃程度和材料效率五类指标。
- 供给规模使用240周累计供货折算为产成品体积，避免只看原料立方米导致A/B/C材料不可比。
- 可靠性使用有订货周的相对偏差，稳定性使用正供货周均值/(均值+标准差)，活跃程度使用非零供货周比例。
- 实验得到前50家供应商，前10家为：S229, S361, S275, S329, S282, S268, S306, S194, S151, S356。

## 实验报告

本问的核心是：根据附件1，对402 家供应商的供货特征进行量化分析，建立反映保障企业生产 重要性的数学模型，在此基础上确定50 家最重要的供应商， 并在论文中列表给出结果。

建模时先将题目要求拆成 1 个任务，再选择 `供应商评价与订购转运规划`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
