# 2023-D 问题 2 建模求解实验报告

## 题目原文与任务拆解

- 题目：2023年 CUMCM D题：圈养湖羊的空间利用率
- 问题：问题 2
- 原问：在问题 1 的基础上，对 112 个标准羊栏给出具体的生产计划（包括种公羊与基础 母羊的配种时机和数量、羊栏的使用方案、年化出栏羊只数量等），使得年化出栏羊只数量最 大。

### 本问需要完成什么
- 任务 1：在问题 1 的基础上，对 112 个标准羊栏给出具体的生产计划（包括种公羊与基础 母羊的配种时机和数量、羊栏的使用方案、年化出栏羊只数量等），使得年化出栏羊只数量最 大

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
- b: 每批开始配种的基础母羊数量
- tau: 相邻批次开始配种的间隔天数
- M: 基础母羊存栏数，约为 b*C/tau
- R: 种公羊数量，满足不低于 1:50 且覆盖同时配种羊栏
- P_t: 第 t 天总羊栏需求
- Y: 年化出栏羔羊数量

### 约束条件
- 自然交配期每栏 1 只种公羊且不超过 14 只基础母羊。
- 怀孕期每栏不超过 8 只待产母羊。
- 哺乳期每栏不超过 6 只母羊及其羔羊。
- 育肥期每栏不超过 14 只羔羊，空怀休整期每栏不超过 14 只母羊。
- 确定性问题要求 max_t P_t <= 112；缺口估算用 max_t P_t - 112。

### 模型公式 / 目标函数
- `P_t = mating_t + pregnant_t + lactating_t + fattening_t + resting_t + ram_t`
- `Y = lamb_outputs_in_window / window_days * 365`
- `max Y subject to max_t P_t <= 112`

## Python 代码与运行方式

- 代码文件：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2023/D/q02/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2023/D/q02/solution.py`
- 批量运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：把每批配种转化为交配、怀孕、哺乳、育肥、休整五类日历区间。
- 步骤 2：逐日统计各阶段羊只数量并按容量上取整为羊栏数。
- 步骤 3：枚举批次规模和配种间隔，筛选 112 个标准羊栏内可行方案。
- 步骤 4：输出基础母羊、种公羊、最大羊栏需求、空间利用率和年化出栏量。

## 实验结果与解释

### 产物文件
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2023/D/q02/experiment_table.csv

### 数据来源
- 类型：problem_statement
- 附件：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2023/D.md
- 读取规模：36 行 x 17 列
- 说明：未找到可直接读取的数值附件，本问改用题目原文中的参数/表格数字生成实验结果。

### result.json 核心结果

```json
{
  "method": "deterministic_hu_sheep_production_plan",
  "production_plan": {
    "batch_ewes": 28,
    "interval_days": 15,
    "base_ewes": 428,
    "rams": 9,
    "annual_output": 1344.0,
    "max_pens": 111.0,
    "mean_pens": 110.8,
    "utilization": 0.989286,
    "feasible_112_pens": true
  },
  "daily_pen_table_days": "steady-year days 730-849",
  "annual_output": 1344.0,
  "max_pens": 111.0,
  "mean_pens": 110.8,
  "utilization": 0.989286,
  "note": "生产计划为每 interval_days 天启动一批 batch_ewes 只基础母羊配种，并按阶段容量安排羊栏。"
}
```

### 结果解释
- 本问用 `deterministic_hu_sheep_production_plan` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 实验报告

本问的核心是：在问题 1 的基础上，对 112 个标准羊栏给出具体的生产计划（包括种公羊与基础 母羊的配种时机和数量、羊栏的使用方案、年化出栏羊只数量等），使得年化出栏羊只数量最 大。

建模时先将题目要求拆成 1 个任务，再选择 `规划优化与资源配置`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
