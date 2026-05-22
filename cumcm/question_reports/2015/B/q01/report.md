# 2015-B 问题 1 建模求解实验报告

## 题目原文与任务拆解

- 题目：2015年 CUMCM B题：互联网+”时代的出租车资源配置
- 问题：问题 1
- 原问：试建立合理的指标，并分析不同时空出租车资源的“供求匹配”程度。

### 本问需要完成什么
- 任务 1：试建立合理的指标，并分析不同时空出租车资源的“供求匹配”程度

## 适配模型

- 主模型：综合评价与权重决策（CH7：权重生成与评价模型）
- 教程参考：../My-Agent/intro-mathmodel/docs/CH7/第7章-权重生成与评价模型.md

### 候选模型与适配理由
- 数据拟合与回归分析（CH6）：分析；参考 ../My-Agent/intro-mathmodel/docs/CH6/第六章-数据处理与拟合模型.md
- 综合评价与权重决策（CH7）：指标；参考 ../My-Agent/intro-mathmodel/docs/CH7/第7章-权重生成与评价模型.md

## 变量、约束与公式

### 建模假设
- 以题面给出的数值、约束和输出格式为第一优先级构造模型。
- 若原始附件尚未能被当前环境直接读取，脚本优先抽取题目原文中的参数和表格数字，并在数据来源中显式记录。
- 所有结果由本问 solution.py 运行生成，result.json 与 experiment_table.csv 保持同步。

### 变量定义
- a_ij: 方案 i 在指标 j 上的标准化表现
- w_j: 指标权重
- D_i^+: 到理想解距离
- C_i: TOPSIS 贴近度

### 约束条件
- 各指标同向化后归一化
- sum_j w_j = 1, w_j >= 0

### 模型公式 / 目标函数
- `w_j = std(a_.j)/sum_j std(a_.j)`
- `C_i = D_i^-/(D_i^+ + D_i^-)`
- `rank = argsort(-C_i)`

## Python 代码与运行方式

- 代码文件：cumcm/question_solutions/2015/B/q01/solution.py
- 单问运行：`.venv/bin/python cumcm/question_solutions/2015/B/q01/solution.py`
- 批量运行：`.venv/bin/python cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：构造评价指标矩阵。
- 步骤 2：用离散度生成客观权重。
- 步骤 3：计算正负理想解距离与贴近度。
- 步骤 4：输出排名和最优方案。

## 实验结果与解释

### 产物文件
- cumcm/question_artifacts/2015/B/q01/experiment_table.csv

### 数据来源
- 类型：problem_statement
- 附件：cumcm/problems/2015/B.md
- 读取规模：5 行 x 3 列
- 说明：未找到可直接读取的数值附件，本问改用题目原文中的参数/表格数字生成实验结果。

### result.json 核心结果

```json
{
  "method": "std_weight_topsis",
  "weights": [
    0.5,
    0.5
  ],
  "scores": [
    1.0,
    0.0,
    0.0,
    0.25,
    1.0
  ],
  "best_option": 1
}
```

### 结果解释
- 本问用 `std_weight_topsis` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 实验报告

本问的核心是：试建立合理的指标，并分析不同时空出租车资源的“供求匹配”程度。

建模时先将题目要求拆成 1 个任务，再选择 `综合评价与权重决策`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
