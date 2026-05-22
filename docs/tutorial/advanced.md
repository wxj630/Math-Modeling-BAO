# Advanced Solution

Advanced solution 是把赛题主线真正接起来的可复现解法。它不只是“某一问写得更复杂”，而是让每个小问继承前面的变量、数据、假设和结论，形成可以继续写成论文的整题底稿。

## 升级原则

| 升级点 | Baseline 常见状态 | Advanced 应达到的状态 |
|---|---|---|
| 数据 | 使用题面索引、少量参数或通用实验表。 | 读取官方 CSV、XLSX、PDF 抽取参数或题面明确数值。 |
| 约束 | 只保留模型族里的抽象约束。 | 把赛题中的产量、容量、概率、时间、路径、模板格式写进模型。 |
| 递进 | 每问可以独立跑，但联系弱。 | 后一问能解释它继承或改变了前一问的哪些假设。 |
| 输出 | 只证明代码能跑。 | 输出论文可用的表、图、JSON、Excel 或备忘录文本。 |
| 报告 | 解释通用模型。 | 解释整题语境、小问作用、数据来源、公式、结果、限制和运行命令。 |

## MCM/ICM 的 advanced

MCM/ICM 的进阶解法位于：

```text
mcm/question_solutions/
mcm/question_results/
mcm/question_reports/
mcm/question_artifacts/
```

这些材料现在通过赛题页组织。比如 [2015-C](/mcm-track/problems/2015-C) 会先展示人力资本网络、流失动态、预算、压力情景、多层网络和最终报告之间的关系，再给出每一问的 advanced report、solution、result 和 artifact。

## CUMCM 的 advanced

CUMCM 的进阶解法位于：

```text
cumcm/question_solutions/
cumcm/question_results/
cumcm/question_reports/
cumcm/question_artifacts/
```

以 [2024-C 农作物种植策略](/cumcm-track/problems/2024-C) 为例，第 1 问建立稳定参数下的 2024-2030 种植方案，第 2 问加入销量、亩产、成本、价格的不确定性，第 3 问再考虑作物替代、互补和相关性。advanced 的价值在于把这条递进链保留下来。

## 和 baseline 对照阅读

每个 advanced solution 都可以按同一个问题问自己：

- 它比 baseline 多读了哪些真实数据？
- 它继承了前一问的哪些变量、假设或中间结果？
- 它把题目里的哪些约束写成了模型？
- 它输出的表格和图是否能直接放进论文？
- 它有没有说明模型限制，避免把启发式结果写成严格最优？

如果这五个问题能答清楚，advanced solution 就已经具备整题论文骨架。
