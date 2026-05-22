# 2024-B 问题 4 建模求解实验报告

## 题目原文与任务拆解

- 题目：2024年 CUMCM B题：生产过程中的决策
- 问题：问题 4
- 原问：假设问题 2 和问题 3 中零配件、 半成品和成品的次品率均是通过抽样检测方法 （例如，你在问题 1 中使用的方法）得到的，请重新完成问题 2 和问题 3。 附录 说明 (1) 半成品、成品的次品率是将正品零配件（或者半成品）装配后的产品次品率； (2) 不合格成品中的调换损失是指除调换次品之外的损失 （如： 物流成本、企业信誉等） 。 (3) 购买单价、 检测成本、 装配成本、 市场售价、 调换损失和拆解费用的单位均为元/件。

### 本问需要完成什么
- 任务 1：假设问题 2 和问题 3 中零配件、 半成品和成品的次品率均是通过抽样检测方法 （例如，你在问题 1 中使用的方法）得到的，请重新完成问题 2 和问题 3。 附录 说明
- 任务 2：(1) 半成品、成品的次品率是将正品零配件（或者半成品）装配后的产品次品率
- 任务 3：(2) 不合格成品中的调换损失是指除调换次品之外的损失 （如： 物流成本、企业信誉等）
- 任务 4：(3) 购买单价、 检测成本、 装配成本、 市场售价、 调换损失和拆解费用的单位均为元/件

## 适配模型

- 主模型：规划优化与资源配置（CH3：函数极值与规划模型）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md

### 候选模型与适配理由
- 概率统计与抽样检验（CH9）：抽样、次品；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH9/第九章-机器学习与统计模型.md
- 规划优化与资源配置（CH3）：成本；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md
- 机器学习与统计识别（CH9）：检测；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH9/第九章-机器学习与统计模型.md

## 变量、约束与公式

### 建模假设
- 以题面给出的数值、约束和输出格式为第一优先级构造模型。
- 若原始附件尚未能被当前环境直接读取，脚本优先抽取题目原文中的参数和表格数字，并在数据来源中显式记录。
- 所有结果由本问 solution.py 运行生成，result.json 与 experiment_table.csv 保持同步。

### 变量定义
- d_i: 第 i 个零配件是否检测
- d_s: 半成品是否检测
- d_f: 成品是否检测
- r_s,r_f: 半成品/成品不合格后是否拆解
- q: 进入市场产品为合格品的概率
- E[profit]: 单件期望利润

### 约束条件
- 被检测出的不合格零配件、半成品或成品不得直接进入下一环节。
- 未检测成品进入市场后，按不合格概率产生调换损失。
- 拆解只在检测发现或市场退回的不合格品上发生，并计入拆解费用与回收价值。
- 所有检测/拆解决策均为 0-1 变量，通过枚举求全局最优。

### 模型公式 / 目标函数
- `max E[profit(policy)]`
- `q = product(component_good_probability)*(1-p_assembly)`
- `E[profit] = E[sales] - E[purchase+test+assembly+replacement] + E[salvage-disassembly]`

## Python 代码与运行方式

- 代码文件：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2024/B/q04/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2024/B/q04/solution.py`
- 批量运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：按题面表 1 或表 2 录入次品率、购买单价、检测成本、装配成本、售价、调换损失和拆解费用。
- 步骤 2：枚举零配件检测、成品/半成品检测和拆解决策组合。
- 步骤 3：对每个组合计算成品合格率、调换风险、回收净值和单件期望利润。
- 步骤 4：按期望利润排序，输出每个情形的最优决策和完整候选表。

## 实验结果与解释

### 产物文件
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2024/B/q04/experiment_table.csv

### 数据来源
- 类型：problem_statement
- 附件：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2024/B.md
- 读取规模：49 行 x 13 列
- 说明：未找到可直接读取的数值附件，本问改用题目原文中的参数/表格数字生成实验结果。

### result.json 核心结果

```json
{
  "method": "sampling_uncertainty_robust_policy_recalculation",
  "inflation_rule": "p_robust = p_hat + 1.645*sqrt(p_hat*(1-p_hat)/128)",
  "table1_best_policies": [
    {
      "inspect_part1": false,
      "inspect_part2": false,
      "inspect_product": false,
      "disassemble_defective_product": true,
      "market_good_probability": 0.628058,
      "defective_to_market_probability": 0.371942,
      "expected_profit": 28.463528,
      "expected_revenue": 56.0,
      "expected_direct_cost": 28.0,
      "expected_replacement_loss": 2.231649,
      "expected_salvage_net": 2.695177,
      "case": 1,
      "rank": 1
    },
    {
      "inspect_part1": false,
      "inspect_part2": false,
      "inspect_product": false,
      "disassemble_defective_product": true,
      "market_good_probability": 0.408255,
      "defective_to_market_probability": 0.591745,
      "expected_profit": 27.768225,
      "expected_revenue": 56.0,
      "expected_direct_cost": 28.0,
      "expected_replacement_loss": 3.55047,
      "expected_salvage_net": 3.318694,
      "case": 2,
      "rank": 1
    },
    {
      "inspect_part1": false,
      "inspect_part2": false,
      "inspect_product": false,
      "disassemble_defective_product": true,
      "market_good_probability": 0.628058,
      "defective_to_market_probability": 0.371942,
      "expected_profit": 19.536931,
      "expected_revenue": 56.0,
      "expected_direct_cost": 28.0,
      "expected_replacement_loss": 11.158246,
      "expected_salvage_net": 2.695177,
      "case": 3,
      "rank": 1
    },
    {
      "inspect_part1": true,
      "inspect_part2": false,
      "inspect_product": false,
      "disassemble_defective_product": true,
      "market_good_probability": 0.550327,
      "defective_to_market_probability": 0.449673,
      "expected_profit": 14.59356,
      "expected_revenue": 56.0,
      "expected_direct_cost": 30.739994,
      "expected_replacement_loss": 13.490182,
      "expected_salvage_net": 2.823735,
      "case": 4,
      "rank": 1
    },
    {
      "inspect_part1": false,
      "inspect_part2": false,
      "inspect_product": false,
      "disassemble_defective_product": true,
      "market_good_probability": 0.544056,
      "defective_to_market_probability": 0.455944,
      "expected_profit": 26.133423,
      "expected_revenue": 56.0,
      "expected_direct_cost": 28.0,
      "expected_replacement_loss": 4.559436,
      "expected_salvage_net": 2.692859,
      "case": 5,
      "rank": 1
    },
    {
      "inspect_part1": false,
      "inspect_part2": false,
      "inspect_product": false,
      "disassemble_defective_product": false,
      "market_good_probability": 0.774407,
      "defective_to_market_probability": 0.225593,
      "expected_profit": 25.744073,
      "expected_revenue": 56.0,
      "expected_direct_cost": 28.0,
      "expected_replacement_loss": 2.255927,
      "expected_salvage_net": 0.0,
      "case": 6,
      "rank": 1
    }
  ],
  "table2_best_policy": {
    "part_inspection_bits": "00000000",
    "semi_inspection_bits": "000",
    "final_inspection": false,
    "semi_disassembly_bits": "000",
    "final_disassembly": true,
    "final_good_probability": 0.155597,
    "defective_to_market_probability": 0.844403,
    "expected_profit": 80.694468,
    "expected_direct_cost": 96.0,
    "expected_replacement_loss": 33.776133,
    "expected_salvage_net": 10.470601,
    "rank": 1
  },
  "table1_average_best_profit": 23.706623,
  "table2_best_profit": 80.694468,
  "note": "用问题1的抽样不确定性思想把次品率上调到保守估计，再分别重算问题2和问题3的最优策略。"
}
```

### 结果解释
- 本问用 `sampling_uncertainty_robust_policy_recalculation` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 实验报告

本问的核心是：假设问题 2 和问题 3 中零配件、 半成品和成品的次品率均是通过抽样检测方法 （例如，你在问题 1 中使用的方法）得到的，请重新完成问题 2 和问题 3。 附录 说明 (1) 半成品、成品的次品率是将正品零配件（或者半成品）装配后的产品次品率； (2) 不合格成品中的调换损失是指除调换次品之外的损失 （如： 物流成本、企业信誉等） 。 (3) 购买单价、…

建模时先将题目要求拆成 4 个任务，再选择 `规划优化与资源配置`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
