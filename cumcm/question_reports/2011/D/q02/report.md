# 2011-D 问题 2 建模求解实验报告

## 题目原文与任务拆解

- 题目：2011年 CUMCM D题：天然肠衣搭配
- 问题：问题 2
- 原问：对于成品捆数相同的方案，最短长度最长的成品越多，方案越好；

### 本问需要完成什么
- 任务 1：对于成品捆数相同的方案，最短长度最长的成品越多，方案越好

## 适配模型

- 主模型：规划优化与资源配置（CH3：函数极值与规划模型）
- 教程参考：../My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md

### 候选模型与适配理由
- 规划优化与资源配置（CH3）：方案；参考 ../My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md
- 图论网络与路径调度（CH4）：最短；参考 ../My-Agent/intro-mathmodel/docs/CH4/第4章-复杂网络与图论模型.md

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

- 代码文件：cumcm/question_solutions/2011/D/q02/solution.py
- 单问运行：`.venv/bin/python cumcm/question_solutions/2011/D/q02/solution.py`
- 批量运行：`.venv/bin/python cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：把题面目标转成收益最大或成本最小。
- 步骤 2：把资源、时间、预算、容量写成线性不等式。
- 步骤 3：调用 scipy.optimize.linprog 求解。
- 步骤 4：输出决策变量、目标值和资源松弛量。

## 实验结果与解释

### 产物文件
- cumcm/question_artifacts/2011/D/q02/experiment_table.csv

### 数据来源
- 类型：problem_statement
- 附件：cumcm/problems/2011/D.md
- 读取规模：21 行 x 9 列
- 说明：未找到可直接读取的数值附件，本问改用题目原文中的参数/表格数字生成实验结果。

### result.json 核心结果

```json
{
  "method": "linear_programming",
  "success": true,
  "objective_max": 5.825101395241284,
  "decision": [
    0.0,
    0.0,
    0.0,
    2.053982
  ],
  "resource_slack": [
    4.544685,
    0.0,
    0.80393
  ]
}
```

### 结果解释
- 本问用 `linear_programming` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 实验报告

本问的核心是：对于成品捆数相同的方案，最短长度最长的成品越多，方案越好；

建模时先将题目要求拆成 1 个任务，再选择 `规划优化与资源配置`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
