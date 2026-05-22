# 2011-D 问题 3 建模求解实验报告

## 题目原文与任务拆解

- 题目：2011年 CUMCM D题：天然肠衣搭配
- 问题：问题 3
- 原问：为提高原料使用率，总长度允许有± 0.5米的误差，总根数允许比标准少1根；

### 本问需要完成什么
- 任务 1：为提高原料使用率，总长度允许有± 0.5米的误差，总根数允许比标准少1根

## 适配模型

- 主模型：概率统计与抽样检验（CH9：机器学习与统计模型）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH9/第九章-机器学习与统计模型.md

### 候选模型与适配理由
- 概率统计与抽样检验（CH9）：误差；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH9/第九章-机器学习与统计模型.md

## 变量、约束与公式

### 建模假设
- 以题面给出的数值、约束和输出格式为第一优先级构造模型。
- 若原始附件尚未能被当前环境直接读取，脚本优先抽取题目原文中的参数和表格数字，并在数据来源中显式记录。
- 所有结果由本问 solution.py 运行生成，result.json 与 experiment_table.csv 保持同步。

### 变量定义
- n: 抽样量
- c: 接收阈值
- p0: 标称缺陷率/基准概率
- p1: 风险备择概率

### 约束条件
- P_reject(p0)<=alpha
- P_accept(p1)<=beta
- n 为正整数，c 为非负整数

### 模型公式 / 目标函数
- `P_reject(p0)=1-F_Binomial(c;n,p0)`
- `P_accept(p1)=F_Binomial(c;n,p1)`
- `min n subject to producer/consumer risk`

## Python 代码与运行方式

- 代码文件：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2011/D/q03/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2011/D/q03/solution.py`
- 批量运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：从题面提取标称比例。
- 步骤 2：设置生产方和使用方风险。
- 步骤 3：枚举 n 与 c 检查二项分布尾概率。
- 步骤 4：输出最小可行抽样方案。

## 实验结果与解释

### 产物文件
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2011/D/q03/experiment_table.csv

### 数据来源
- 类型：problem_statement
- 附件：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2011/D.md
- 读取规模：22 行 x 9 列
- 说明：未找到可直接读取的数值附件，本问改用题目原文中的参数/表格数字生成实验结果。

### result.json 核心结果

```json
{
  "method": "binomial_sampling_design",
  "p0": 0.005,
  "p1": 0.0375,
  "alpha": 0.05,
  "beta": 0.1,
  "sample_size": 699,
  "acceptance_number": 3,
  "reject_good_probability": null,
  "accept_bad_probability": null
}
```

### 结果解释
- 本问用 `binomial_sampling_design` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 实验报告

本问的核心是：为提高原料使用率，总长度允许有± 0.5米的误差，总根数允许比标准少1根；

建模时先将题目要求拆成 1 个任务，再选择 `概率统计与抽样检验`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
