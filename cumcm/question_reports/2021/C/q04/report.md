# 2021-C 问题 4 建模求解实验报告

## 题目原文与任务拆解

- 题目：2021年 CUMCM C题：生产企业原材料的订购与运输
- 问题：问题 4
- 原问：该企业通过技术改造已具备了提高产能的潜力。 根据现有原材料的供应商和转运 商的实际情况，确定该企业每周的产能可以提高多少，并给出未来 24 周的订购和转运 方案。 注：请将问题 2、问题 3 和问题 4 订购方案的数值结果填入附件 A，转运方案的数 值结果填入附件 B，并作为支撑材料（勿改变文件名）随论文一起提交。 附件 1 的数据说明

### 本问需要完成什么
- 任务 1：根据现有原材料的供应商和转运 商的实际情况，确定该企业每周的产能可以提高多少，并给出未来 24 周的订购和转运 方案

## 适配模型

- 主模型：订购-转运联合规划优化（CH3：函数极值与规划模型）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md

### 候选模型与适配理由
- 规划优化与资源配置（CH3）：方案、订购；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md
- 时间序列预测（CH8）：未来；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH8/第8章-时间序列.md
- 图论网络与路径调度（CH4）：转运；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH4/第4章-复杂网络与图论模型.md

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
- `max sum_i received_{i,t}/coef_i`
- `subject to y_{i,t} <= cap_i, sum_i z_{i,k,t} <= 6000`
- `capacity_increase = mean_t(I_t) - 28200`

## Python 代码与运行方式

- 代码文件：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2021/C/q04/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2021/C/q04/solution.py`
- 批量运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：使用全部402家供应商的稳健供给能力作为可调用供给池。
- 步骤 2：按单位原料产出、重要性和低损耗排序，在8家转运商总容量内尽量提高折算产能。
- 步骤 3：计算未来24周可实现产能、相对2.82万立方米/周的提升量。
- 步骤 4：输出提高产能情形下的订购和转运方案。

## 实验结果与解释

### 产物文件
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2021/C/q04/q4_capacity_max_supplier_scores.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2021/C/q04/q4_capacity_max_weekly_summary.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2021/C/q04/q4_capacity_max_order_plan.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2021/C/q04/q4_capacity_max_transport_plan.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2021/C/q04/q4_capacity_max_附件A_订购方案填报.xlsx
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2021/C/q04/q4_capacity_max_附件B_转运方案填报.xlsx
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2021/C/q04/experiment_table.csv

### 数据来源
- 类型：attachment
- 附件：/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/C/附件1 近5年402家供应商的相关数据.xlsx; /Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/C/附件2 近5年8家转运商的相关数据.xlsx; /Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/C/附件A 订购方案数据结果.xlsx; /Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/C/附件B 转运方案数据结果.xlsx
- 读取规模：410 行 x 240 列
- 说明：本题专用算法读取附件1的402家供应商240周订货/供货量、附件2的8家转运商240周损耗率，并按附件A/B模板生成24周订购与转运方案。

### result.json 核心结果

```json
{
  "method": "maximum_capacity_with_supplier_and_transporter_limits",
  "all_supplier_count": 402,
  "summary": {
    "supplier_count": 285,
    "total_expected_supply_m3": 485358.730008,
    "A_share": 0.32075,
    "B_share": 0.324972,
    "C_share": 0.354277,
    "mean_weekly_product_capacity_m3": 30706.865975,
    "min_demand_satisfaction_ratio": 1.08777,
    "mean_loss_rate_pct": 0.044486,
    "total_cost_proxy": 611463.206424
  },
  "mean_weekly_capacity_increase_m3": 2506.865975,
  "capacity_increase_ratio": 0.088896,
  "weekly_summary_sample": [
    {
      "week": 1,
      "supplier_count_used": 285,
      "order_volume_m3": 23233.720564,
      "expected_supply_m3": 20223.280417,
      "expected_received_m3": 20223.044749,
      "product_equivalent_m3": 30719.200748,
      "demand_satisfaction_ratio": 1.089333,
      "weighted_loss_rate_pct": 0.001165,
      "cost_proxy": 25477.633601,
      "A_supply_m3": 6486.624978,
      "B_supply_m3": 6572.002728,
      "C_supply_m3": 7164.652711
    },
    {
      "week": 2,
      "supplier_count_used": 285,
      "order_volume_m3": 23233.720564,
      "expected_supply_m3": 20223.280417,
      "expected_received_m3": 20223.280417,
      "product_equivalent_m3": 30719.528064,
      "demand_satisfaction_ratio": 1.089345,
      "weighted_loss_rate_pct": 0.0,
      "cost_proxy": 25477.633601,
      "A_supply_m3": 6486.624978,
      "B_supply_m3": 6572.002728,
      "C_supply_m3": 7164.652711
    },
    {
      "week": 3,
      "supplier_count_used": 285,
      "order_volume_m3": 23233.720564,
      "expected_supply_m3": 20223.280417,
      "expected_received_m3": 20222.271048,
      "product_equivalent_m3": 30718.126162,
      "demand_satisfaction_ratio": 1.089295,
      "weighted_loss_rate_pct": 0.004991,
      "cost_proxy": 25477.633601,
      "A_supply_m3": 6486.624978,
      "B_supply_m3": 6572.002728,
      "C_supply_m3": 7164.652711
    },
    {
      "week": 4,
      "supplier_count_used": 285,
      "order_volume_m3": 23233.720564,
      "expected_supply_m3": 20223.280417,
      "expected_received_m3": 20223.280417,
      "product_equivalent_m3": 30719.528064,
      "demand_satisfaction_ratio": 1.089345,
      "weighted_loss_rate_pct": 0.0,
      "cost_proxy": 25477.633601,
      "A_supply_m3": 6486.624978,
      "B_supply_m3": 6572.002728,
      "C_supply_m3": 7164.652711
    },
    {
      "week": 5,
      "supplier_count_used": 285,
      "order_volume_m3": 23233.720564,
      "expected_supply_m3": 20223.280417,
      "expected_received_m3": 20192.901878,
      "product_equivalent_m3": 30677.162553,
      "demand_satisfaction_ratio": 1.087843,
      "weighted_loss_rate_pct": 0.150216,
      "cost_proxy": 25477.633601,
      "A_supply_m3": 6486.624978,
      "B_supply_m3": 6572.002728,
      "C_supply_m3": 7164.652711
    },
    {
      "week": 6,
      "supplier_count_used": 285,
      "order_volume_m3": 23233.720564,
      "expected_supply_m3": 20223.280417,
      "expected_received_m3": 20207.512912,
      "product_equivalent_m3": 30697.628752,
      "demand_satisfaction_ratio": 1.088568,
      "weighted_loss_rate_pct": 0.077967,
      "cost_proxy": 25477.633601,
      "A_supply_m3": 6486.624978,
      "B_supply_m3": 6572.002728,
      "C_supply_m3": 7164.652711
    }
  ],
  "report": [
    "问题4把产能作为目标函数，不再只满足2.82万m³/周，而是在供应商稳健供给上限和8家转运商容量内最大化产成品等价原料。",
    "模型测得24周平均可支撑产能为 30706.87 m³/周，较现有2.82万m³/周提高 2506.87 m³/周。",
    "对应提升比例为 8.8896%，平均运输损耗率为 0.0445%。",
    "本问同样输出附件A/B填报版和长表CSV，便于把产能提升方案直接放入论文支撑材料。"
  ]
}
```

### 结果解释
- 本问用 `maximum_capacity_with_supplier_and_transporter_limits` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 专用实验报告

- 问题4把产能作为目标函数，不再只满足2.82万m³/周，而是在供应商稳健供给上限和8家转运商容量内最大化产成品等价原料。
- 模型测得24周平均可支撑产能为 30706.87 m³/周，较现有2.82万m³/周提高 2506.87 m³/周。
- 对应提升比例为 8.8896%，平均运输损耗率为 0.0445%。
- 本问同样输出附件A/B填报版和长表CSV，便于把产能提升方案直接放入论文支撑材料。

## 实验报告

本问的核心是：该企业通过技术改造已具备了提高产能的潜力。 根据现有原材料的供应商和转运 商的实际情况，确定该企业每周的产能可以提高多少，并给出未来 24 周的订购和转运 方案。 注：请将问题 2、问题 3 和问题 4 订购方案的数值结果填入附件 A，转运方案的数 值结果填入附件 B，并作为支撑材料（勿改变文件名）随论文一起提交。 附件 1 的数据说明

建模时先将题目要求拆成 1 个任务，再选择 `订购-转运联合规划优化`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
