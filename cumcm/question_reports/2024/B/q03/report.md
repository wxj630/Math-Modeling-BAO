# 2024-B 问题 3 建模求解实验报告

## 题目原文与任务拆解

- 题目：2024年 CUMCM B题：生产过程中的决策
- 问题：问题 3
- 原问：对 𝑚 道工序、𝑛 个零配件，已知零配件、半成品和成品的次品率，重复问题 2， 给出生产过程的决策方案。图 1 给出了 2 道工序、8 个零配件的情况，具体数值由表 2 给 出。

### 本问需要完成什么
- 任务 1：对 𝑚 道工序、𝑛 个零配件，已知零配件、半成品和成品的次品率，重复问题 2， 给出生产过程的决策方案
- 任务 2：图 1 给出了 2 道工序、8 个零配件的情况，具体数值由表 2 给 出

## 适配模型

- 主模型：规划优化与资源配置（CH3：函数极值与规划模型）
- 教程参考：../My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md

### 候选模型与适配理由
- 规划优化与资源配置（CH3）：决策、方案；参考 ../My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md
- 概率统计与抽样检验（CH9）：次品；参考 ../My-Agent/intro-mathmodel/docs/CH9/第九章-机器学习与统计模型.md

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

- 代码文件：cumcm/question_solutions/2024/B/q03/solution.py
- 单问运行：`.venv/bin/python cumcm/question_solutions/2024/B/q03/solution.py`
- 批量运行：`.venv/bin/python cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：按题面表 1 或表 2 录入次品率、购买单价、检测成本、装配成本、售价、调换损失和拆解费用。
- 步骤 2：枚举零配件检测、成品/半成品检测和拆解决策组合。
- 步骤 3：对每个组合计算成品合格率、调换风险、回收净值和单件期望利润。
- 步骤 4：按期望利润排序，输出每个情形的最优决策和完整候选表。

## 实验结果与解释

### 产物文件
- cumcm/question_artifacts/2024/B/q03/experiment_table.csv

### 数据来源
- 类型：problem_statement
- 附件：cumcm/problems/2024/B.md
- 读取规模：49 行 x 13 列
- 说明：未找到可直接读取的数值附件，本问改用题目原文中的参数/表格数字生成实验结果。

### result.json 核心结果

```json
{
  "method": "multi_stage_assembly_policy_enumeration",
  "policy_count": 65536,
  "best_policy": {
    "part_inspection_bits": "00000000",
    "semi_inspection_bits": "000",
    "final_inspection": false,
    "semi_disassembly_bits": "000",
    "final_disassembly": true,
    "final_good_probability": 0.28243,
    "defective_to_market_probability": 0.71757,
    "expected_profit": 84.195055,
    "expected_direct_cost": 96.0,
    "expected_replacement_loss": 28.702819,
    "expected_salvage_net": 8.897874,
    "rank": 1
  },
  "top_5_policies": [
    {
      "part_inspection_bits": "00000000",
      "semi_inspection_bits": "000",
      "final_inspection": false,
      "semi_disassembly_bits": "000",
      "final_disassembly": true,
      "final_good_probability": 0.28243,
      "defective_to_market_probability": 0.71757,
      "expected_profit": 84.195055,
      "expected_direct_cost": 96.0,
      "expected_replacement_loss": 28.702819,
      "expected_salvage_net": 8.897874,
      "rank": 1
    },
    {
      "part_inspection_bits": "00000000",
      "semi_inspection_bits": "000",
      "final_inspection": false,
      "semi_disassembly_bits": "100",
      "final_disassembly": true,
      "final_good_probability": 0.28243,
      "defective_to_market_probability": 0.71757,
      "expected_profit": 84.195055,
      "expected_direct_cost": 96.0,
      "expected_replacement_loss": 28.702819,
      "expected_salvage_net": 8.897874,
      "rank": 2
    },
    {
      "part_inspection_bits": "00000000",
      "semi_inspection_bits": "000",
      "final_inspection": false,
      "semi_disassembly_bits": "010",
      "final_disassembly": true,
      "final_good_probability": 0.28243,
      "defective_to_market_probability": 0.71757,
      "expected_profit": 84.195055,
      "expected_direct_cost": 96.0,
      "expected_replacement_loss": 28.702819,
      "expected_salvage_net": 8.897874,
      "rank": 3
    },
    {
      "part_inspection_bits": "00000000",
      "semi_inspection_bits": "000",
      "final_inspection": false,
      "semi_disassembly_bits": "110",
      "final_disassembly": true,
      "final_good_probability": 0.28243,
      "defective_to_market_probability": 0.71757,
      "expected_profit": 84.195055,
      "expected_direct_cost": 96.0,
      "expected_replacement_loss": 28.702819,
      "expected_salvage_net": 8.897874,
      "rank": 4
    },
    {
      "part_inspection_bits": "00000000",
      "semi_inspection_bits": "000",
      "final_inspection": false,
      "semi_disassembly_bits": "001",
      "final_disassembly": true,
      "final_good_probability": 0.28243,
      "defective_to_market_probability": 0.71757,
      "expected_profit": 84.195055,
      "expected_direct_cost": 96.0,
      "expected_replacement_loss": 28.702819,
      "expected_salvage_net": 8.897874,
      "rank": 5
    }
  ],
  "defect_rate_inflation": 0.0,
  "note": "8 个零配件、3 个半成品和 1 个成品的检测/拆解决策用 16 位策略枚举，按期望利润选择最优方案。"
}
```

### 结果解释
- 本问用 `multi_stage_assembly_policy_enumeration` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 实验报告

本问的核心是：对 𝑚 道工序、𝑛 个零配件，已知零配件、半成品和成品的次品率，重复问题 2， 给出生产过程的决策方案。图 1 给出了 2 道工序、8 个零配件的情况，具体数值由表 2 给 出。

建模时先将题目要求拆成 2 个任务，再选择 `规划优化与资源配置`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
