# Advanced Solution

Advanced solution 是题意专门化后的可复现解法。它会把官方附件、题面参数、业务约束、输出模板和论文报告结构接起来，目标是形成可以继续写成竞赛论文的工作底稿。

## 升级原则

从 baseline 升级到 advanced 时，优先做四件事：

| 升级点 | Baseline 常见状态 | Advanced 应达到的状态 |
|---|---|---|
| 数据 | 使用题面索引、少量参数或通用实验表。 | 读取官方 CSV、XLSX、PDF 抽取参数或题面明确数值。 |
| 约束 | 只保留模型族里的抽象约束。 | 把小问中的产量、容量、概率、时间、路径、模板格式写进模型。 |
| 输出 | 只证明代码能跑。 | 输出论文可用的表、图、JSON、Excel 或备忘录文本。 |
| 报告 | 解释通用模型。 | 解释题目原问、数据来源、假设、公式、结果、限制和运行命令。 |

## MCM 的 advanced

MCM/ICM 的进阶解法位于：

```text
mcm/question_solutions/
mcm/question_results/
mcm/question_reports/
mcm/question_artifacts/
```

这些解法从 `docs/mcm-2015-2025/official_assets_extracted/` 或题面参数出发，按小问生成独立产物。索引文件是：

```text
mcm/question_solution_index.csv
mcm/question_solution_index.json
```

学习时建议先挑有官方附件的题，例如 2024-C 网球、2025-C 奥运、2025-D 路网，再读只依赖题面参数的综合评价、系统动力学或政策备忘录类题。

## CUMCM 的 advanced

CUMCM 的进阶解法位于：

```text
cumcm/question_solutions/
cumcm/question_results/
cumcm/question_reports/
cumcm/question_artifacts/
```

其中 2024-A、2024-B、2024-C、2024-D、2024-E 等题已经做过明显的题意专门化。索引文件是：

```text
cumcm/question_solution_index.csv
cumcm/question_solution_index.json
```

CUMCM 的进阶解法尤其适合学习“附件解析 + 输出模板 + 约束建模”的完整链条，例如农作物种植策略会读取附件 Excel，并导出 `result1_1.xlsx`、`result1_2.xlsx` 等提交文件。

## 和 baseline 对照阅读

每个 advanced solution 都可以按同一个问题问自己：

- 它比 baseline 多读了哪些真实数据？
- 它把题目里的哪些中文约束写成了变量、边界、概率或目标函数？
- 它输出的表格和图是否能直接放进论文？
- 它有没有说明模型限制，避免把启发式结果写成严格最优？

如果这四个问题能答清楚，advanced solution 就已经具备论文骨架。
