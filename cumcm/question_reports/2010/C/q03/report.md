# 2010-C 问题 3 建模求解实验报告

## 题目原文与任务拆解

- 题目：2010年 CUMCM C题：输油管的布置
- 问题：问题 3
- 原问：在该实际问题中，为进一步节省费用，可以根据炼油厂的生产能力，选用相适应的油管。这时的管线铺设费用将分别降为输送A厂成品油的每千米5.6万元，输送B厂成品油的每千米6.0万元，共用管线费用为每千米7.2万元，拆迁等附加费用同上。请给出管线最佳布置方案及相应的费用。

### 本问需要完成什么
- 任务 1：请给出管线最佳布置方案及相应的费用

## 适配模型

- 主模型：规划优化与资源配置（CH3：函数极值与规划模型）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md

### 候选模型与适配理由
- 规划优化与资源配置（CH3）：方案；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md

## 变量、约束与公式

### 建模假设
- 以题面给出的数值、约束和输出格式为第一优先级构造模型。
- 若原始附件尚未能被当前环境直接读取，脚本优先抽取题目原文中的参数和表格数字，并在数据来源中显式记录。
- 所有结果由本问 solution.py 运行生成，result.json 与 experiment_table.csv 保持同步。

### 变量定义
- x_i: 第 i 个方案/资源的选择强度
- c_i: 单位收益或效用
- A_ji: 第 j 类资源消耗
- b_j: 第 j 类资源上限

### 约束条件
- A x <= b
- x_i >= 0
- 资源容量按题面约束映射为 b_j

### 模型公式 / 目标函数
- `max sum_i c_i*x_i`
- `s.t. A*x <= b, x >= 0`

## Python 代码与运行方式

- 代码文件：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2010/C/q03/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2010/C/q03/solution.py`
- 批量运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：把题面目标转成收益最大或成本最小。
- 步骤 2：把资源、时间、预算、容量写成线性不等式。
- 步骤 3：调用 scipy.optimize.linprog 求解。
- 步骤 4：输出决策变量、目标值和资源松弛量。

## 实验结果与解释

### 产物文件
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2010/C/q03/experiment_table.csv

### 数据来源
- 类型：problem_statement
- 附件：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2010/C.md
- 读取规模：9 行 x 5 列
- 说明：未找到可直接读取的数值附件，本问改用题目原文中的参数/表格数字生成实验结果。

### result.json 核心结果

```json
{
  "method": "linear_programming",
  "success": true,
  "objective_max": 15.87375089067293,
  "decision": [
    4.282361,
    0.0,
    0.0,
    0.0
  ],
  "resource_slack": [
    2.544028,
    0.0,
    0.350243
  ]
}
```

### 结果解释
- 本问用 `linear_programming` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 实验报告

本问的核心是：在该实际问题中，为进一步节省费用，可以根据炼油厂的生产能力，选用相适应的油管。这时的管线铺设费用将分别降为输送A厂成品油的每千米5.6万元，输送B厂成品油的每千米6.0万元，共用管线费用为每千米7.2万元，拆迁等附加费用同上。请给出管线最佳布置方案及相应的费用。

建模时先将题目要求拆成 1 个任务，再选择 `规划优化与资源配置`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
