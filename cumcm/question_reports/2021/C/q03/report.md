# 2021-C 问题 3 建模求解实验报告

## 题目原文与任务拆解

- 题目：2021年 CUMCM C题：生产企业原材料的订购与运输
- 问题：问题 3
- 原问：该企业为了压缩生产成本，现计划尽量多地采购 A 类和尽量少地采购 C 类原材 料，以减少转运及仓储的成本，同时希望转运商的转运损耗率尽量少。请制定新的订购 方案及转运方案，并分析方案的实施效果。

### 本问需要完成什么
- 任务 1：请制定新的订购 方案及转运方案，并分析方案的实施效果

## 适配模型

- 主模型：订购-转运联合规划优化（CH3：函数极值与规划模型）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md

### 候选模型与适配理由
- 规划优化与资源配置（CH3）：成本、方案、采购、订购；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md
- 图论网络与路径调度（CH4）：转运；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH4/第4章-复杂网络与图论模型.md
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
- `min weighted_cost = purchase_cost + transport_loss + 0.08*C_volume - 0.04*A_volume`
- `priority(A) < priority(B) < priority(C), 在满足需求前提下尽量多采购A类、少采购C类。`
- `transport assignment remains min loss subject to 6000 m^3/week carrier capacity.`

## Python 代码与运行方式

- 代码文件：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2021/C/q03/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2021/C/q03/solution.py`
- 批量运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：沿用问题2的最少供应商集合和稳健供给上限。
- 步骤 2：将材料优先级改为A类优先、C类惩罚，重新生成24周订购计划。
- 步骤 3：用同一转运商容量约束进行最小损耗分配。
- 步骤 4：与问题2方案比较A/C采购占比、损耗率、成本代理值和需求满足率。

## 实验结果与解释

### 产物文件
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2021/C/q03/q3_prefer_a_supplier_scores.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2021/C/q03/q3_prefer_a_weekly_summary.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2021/C/q03/q3_prefer_a_order_plan.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2021/C/q03/q3_prefer_a_transport_plan.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2021/C/q03/q3_prefer_a_附件A_订购方案填报.xlsx
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2021/C/q03/q3_prefer_a_附件B_转运方案填报.xlsx
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2021/C/q03/experiment_table.csv

### 数据来源
- 类型：attachment
- 附件：/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/C/附件1 近5年402家供应商的相关数据.xlsx; /Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/C/附件2 近5年8家转运商的相关数据.xlsx; /Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/C/附件A 订购方案数据结果.xlsx; /Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/C/附件B 转运方案数据结果.xlsx
- 读取规模：410 行 x 240 列
- 说明：本题专用算法读取附件1的402家供应商240周订货/供货量、附件2的8家转运商240周损耗率，并按附件A/B模板生成24周订购与转运方案。

### result.json 核心结果

```json
{
  "method": "a_preferred_low_c_transport_plan",
  "minimum_supplier_count": 46,
  "summary": {
    "supplier_count": 46,
    "total_expected_supply_m3": 445348.283878,
    "A_share": 0.324131,
    "B_share": 0.337998,
    "C_share": 0.337871,
    "mean_weekly_product_capacity_m3": 28228.188778,
    "min_demand_satisfaction_ratio": 1.000997,
    "mean_loss_rate_pct": 0.026417,
    "total_cost_proxy": 549178.692506
  },
  "baseline_q2_summary": {
    "supplier_count": 46,
    "total_expected_supply_m3": 446415.337932,
    "A_share": 0.323356,
    "B_share": 0.311145,
    "C_share": 0.365499,
    "mean_weekly_product_capacity_m3": 28228.199932,
    "min_demand_satisfaction_ratio": 1.001,
    "mean_loss_rate_pct": 0.026944,
    "total_cost_proxy": 549345.497886
  },
  "A_share_change_vs_q2": 0.000775,
  "C_share_change_vs_q2": -0.027628,
  "weekly_summary_sample": [
    {
      "week": 1,
      "supplier_count_used": 46,
      "order_volume_m3": 20799.600541,
      "expected_supply_m3": 18551.258819,
      "expected_received_m3": 18551.200385,
      "product_equivalent_m3": 28228.199991,
      "demand_satisfaction_ratio": 1.001,
      "weighted_loss_rate_pct": 0.000315,
      "cost_proxy": 22877.119153,
      "A_supply_m3": 6014.631679,
      "B_supply_m3": 6271.949999,
      "C_supply_m3": 6264.677141
    },
    {
      "week": 2,
      "supplier_count_used": 45,
      "order_volume_m3": 20799.522528,
      "expected_supply_m3": 18551.200392,
      "expected_received_m3": 18551.200392,
      "product_equivalent_m3": 28228.2,
      "demand_satisfaction_ratio": 1.001,
      "weighted_loss_rate_pct": 0.0,
      "cost_proxy": 22877.04114,
      "A_supply_m3": 6014.631679,
      "B_supply_m3": 6271.949999,
      "C_supply_m3": 6264.618714
    },
    {
      "week": 3,
      "supplier_count_used": 46,
      "order_volume_m3": 20799.85666,
      "expected_supply_m3": 18551.450637,
      "expected_received_m3": 18551.200278,
      "product_equivalent_m3": 28228.199842,
      "demand_satisfaction_ratio": 1.001,
      "weighted_loss_rate_pct": 0.00135,
      "cost_proxy": 22877.375272,
      "A_supply_m3": 6014.631679,
      "B_supply_m3": 6271.949999,
      "C_supply_m3": 6264.868959
    },
    {
      "week": 4,
      "supplier_count_used": 45,
      "order_volume_m3": 20799.522528,
      "expected_supply_m3": 18551.200392,
      "expected_received_m3": 18551.200392,
      "product_equivalent_m3": 28228.2,
      "demand_satisfaction_ratio": 1.001,
      "weighted_loss_rate_pct": 0.0,
      "cost_proxy": 22877.04114,
      "A_supply_m3": 6014.631679,
      "B_supply_m3": 6271.949999,
      "C_supply_m3": 6264.618714
    },
    {
      "week": 5,
      "supplier_count_used": 46,
      "order_volume_m3": 20814.857326,
      "expected_supply_m3": 18564.687491,
      "expected_received_m3": 18551.175184,
      "product_equivalent_m3": 28228.11813,
      "demand_satisfaction_ratio": 1.000997,
      "weighted_loss_rate_pct": 0.072785,
      "cost_proxy": 22892.375938,
      "A_supply_m3": 6014.631679,
      "B_supply_m3": 6271.949999,
      "C_supply_m3": 6278.105813
    },
    {
      "week": 6,
      "supplier_count_used": 46,
      "order_volume_m3": 20804.742055,
      "expected_supply_m3": 18555.109505,
      "expected_received_m3": 18551.172668,
      "product_equivalent_m3": 28228.161495,
      "demand_satisfaction_ratio": 1.000999,
      "weighted_loss_rate_pct": 0.021217,
      "cost_proxy": 22882.260667,
      "A_supply_m3": 6014.631679,
      "B_supply_m3": 6271.949999,
      "C_supply_m3": 6268.527827
    }
  ],
  "report": [
    "问题3在问题2可行供应商集合上改变目标权重：A类优先、C类惩罚，并继续使用最低损耗转运分配。",
    "A类供货占比由问题2的 0.3234 调整为 0.3241，C类占比由 0.3655 调整为 0.3379。",
    "24周最小需求满足率为 1.0010，平均运输损耗率为 0.0264%。",
    "该方案牺牲一部分单纯采购成本排序，换取A类材料占比提升和C类材料占比下降，适合写作中的多目标权衡分析。"
  ]
}
```

### 结果解释
- 本问用 `a_preferred_low_c_transport_plan` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 专用实验报告

- 问题3在问题2可行供应商集合上改变目标权重：A类优先、C类惩罚，并继续使用最低损耗转运分配。
- A类供货占比由问题2的 0.3234 调整为 0.3241，C类占比由 0.3655 调整为 0.3379。
- 24周最小需求满足率为 1.0010，平均运输损耗率为 0.0264%。
- 该方案牺牲一部分单纯采购成本排序，换取A类材料占比提升和C类材料占比下降，适合写作中的多目标权衡分析。

## 实验报告

本问的核心是：该企业为了压缩生产成本，现计划尽量多地采购 A 类和尽量少地采购 C 类原材 料，以减少转运及仓储的成本，同时希望转运商的转运损耗率尽量少。请制定新的订购 方案及转运方案，并分析方案的实施效果。

建模时先将题目要求拆成 1 个任务，再选择 `订购-转运联合规划优化`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
