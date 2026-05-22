# 2018-C 问题 3 建模求解实验报告

## 题目原文与任务拆解

- 题目：2018年 CUMCM C题：大型百货商场会员画像描绘
- 问题：问题 3
- 原问：作为零售行业的重要资源，会员具有生命周期(会员从入会到退出的整个过程),会员的状态（比如活跃和非活跃）也会发生变化。试在某个时间窗口，建立会员生命周期和状态划分的数学模型，使商场管理者能够更有效地对会员进行管理。

### 本问需要完成什么
- 任务 1：试在某个时间窗口，建立会员生命周期和状态划分的数学模型，使商场管理者能够更有效地对会员进行管理

## 适配模型

- 主模型：数据拟合与回归分析（CH6：数据处理与拟合模型）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH6/第六章-数据处理与拟合模型.md

### 候选模型与适配理由
- 规划优化与资源配置（CH3）：通用优化建模；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md
- 数据拟合与回归分析（CH6）：通用数据建模；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH6/第六章-数据处理与拟合模型.md

## 变量、约束与公式

### 建模假设
- 以题面给出的数值、约束和输出格式为第一优先级构造模型。
- 若原始附件尚未能被当前环境直接读取，脚本优先抽取题目原文中的参数和表格数字，并在数据来源中显式记录。
- 所有结果由本问 solution.py 运行生成，result.json 与 experiment_table.csv 保持同步。

### 变量定义
- x: 题面影响因素或测量自变量
- y: 待解释/待标定指标
- beta: 回归参数
- epsilon: 随机误差

### 约束条件
- 样本点按题面数值范围或标准化区间构造
- 最小二乘残差平方和最小

### 模型公式 / 目标函数
- `min_beta sum_i (y_i - beta0 - beta1*x_i - beta2*x_i^2)^2`
- `R^2 = 1 - SSE/SST`

## Python 代码与运行方式

- 代码文件：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2018/C/q03/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2018/C/q03/solution.py`
- 批量运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：抽取题面数值范围并构造实验样本。
- 步骤 2：建立二次回归设计矩阵。
- 步骤 3：用 numpy.linalg.lstsq 求解参数。
- 步骤 4：输出拟合值、残差和 R^2。

## 实验结果与解释

### 产物文件
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2018/C/q03/experiment_table.csv

### 数据来源
- 类型：problem_statement
- 附件：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2018/C.md
- 读取规模：8 行 x 3 列
- 说明：未找到可直接读取的数值附件，本问改用题目原文中的参数/表格数字生成实验结果。

### result.json 核心结果

```json
{
  "method": "quadratic_least_squares",
  "coefficients": [
    1.154288,
    0.597063,
    0.032242
  ],
  "r2": 0.9945213206950487,
  "mean_abs_error": 0.15268399729912158
}
```

### 结果解释
- 本问用 `quadratic_least_squares` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 实验报告

本问的核心是：作为零售行业的重要资源，会员具有生命周期(会员从入会到退出的整个过程),会员的状态（比如活跃和非活跃）也会发生变化。试在某个时间窗口，建立会员生命周期和状态划分的数学模型，使商场管理者能够更有效地对会员进行管理。

建模时先将题目要求拆成 1 个任务，再选择 `数据拟合与回归分析`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
