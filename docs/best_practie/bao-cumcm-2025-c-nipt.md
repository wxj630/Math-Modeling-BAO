# CUMCM 2025-C NIPT 时点与异常判定：Baseline → Advanced → Outstanding 进阶

这道题的主入口是 **数据建模/医学统计决策**。从教程角度看，baseline 解决“能跑通”，advanced 解决“更贴题”，Outstanding 解决“证据链完整、结果可检验、表达能让评委快速相信”。

## 材料入口

| 层级 | PDF | 代码 | 结果 |
|---|---|---|---|
| Baseline | `Math-Modeling-BAO-Reports/cumcm/2025-C/baseline/main.pdf` | `Math-Modeling-BAO/cumcm/generic_baselines/solutions/2025/C` | `Math-Modeling-BAO/cumcm/generic_baselines/results/2025/C` |
| Advanced | `Math-Modeling-BAO-Reports/cumcm/2025-C/advanced/main.pdf` | `Math-Modeling-BAO/cumcm/question_solutions/2025/C` | `Math-Modeling-BAO/cumcm/question_results/2025/C` |
| Outstanding | `Math-Modeling-BAO-Reports/outstanding/cumcm/2025-C/C023/pdf/C023.pdf` | `Math-Modeling-BAO/cumcm/outstanding_solutions/2025/C/C023/solution.py` | `Math-Modeling-BAO/cumcm/outstanding_solutions/2025/C/C023/result.json` |

OCR 文本：`Math-Modeling-BAO-Reports/outstanding/cumcm/2025-C/C023/ocr/C023.md`。

## 数据来源

本题复现使用的数据/参数入口如下：

- `type: official_cumcm_xlsx`
- `file: cumcm/source_materials/extracted/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/C题/附件.xlsx`
- `male_rows: 1082`
- `female_rows: 605`

## Baseline：先把题跑通

Baseline 的价值是建立最小可运行闭环：逐问拆解、选择通用模型、生成 `result.json` 和图表。它通常能回答题目，但假设比较粗，指标之间的连接也不够强。

对这题来说，baseline 更像“第一版计算草稿”：可以帮助确认输入、输出和基本量纲，但还不足以支撑 O 奖级别的论证。

## Advanced：把题目机制接进模型

Advanced 的进步是：孕周/BMI 特征、回归显著性、分组时点和异常分类。

这一层通常已经能进入课程讲解，因为它开始把题目约束、官方数据、逐问任务和可复现代码接起来。相比 baseline，它更像一篇可提交论文的骨架。

## Outstanding：把模型链做完整

选用的 O 奖论文是 `C023`，标题为 `基于混合效应模型的NIPT时点优化与胎儿异常判定`。

它的核心升级是：混合效应模型、BMI 时点优化、女胎异常随机森林和风险解释形成完整医学统计链。

当前复现的关键对齐指标如下：

| 指标 | 复现值 | 论文目标 | 误差/说明 |
|---|---:|---:|---|
| `experiment_result.male_pseudo_r2` | 0.90064 | 见 O 论文表格/OCR | 旧脚本未声明 target_comparison；此处列 result.json 核心输出 |
| `experiment_result.earliest_recommended_week` | 12.0 | 见 O 论文表格/OCR | 旧脚本未声明 target_comparison；此处列 result.json 核心输出 |
| `experiment_result.latest_recommended_week` | 20.0 | 见 O 论文表格/OCR | 旧脚本未声明 target_comparison；此处列 result.json 核心输出 |
| `experiment_result.female_loo_accuracy` | 0.8659 | 见 O 论文表格/OCR | 旧脚本未声明 target_comparison；此处列 result.json 核心输出 |
| `experiment_result.top_female_feature` | X染色体浓度 | 见 O 论文表格/OCR | 旧脚本未声明 target_comparison；此处列 result.json 核心输出 |

## 谁做得最好

| 层级 | 能力 | 主要短板 |
|---|---|---|
| Baseline | 能快速产出逐问结果和基本图表 | 假设、指标和验证还比较模板化 |
| Advanced | 题目机制更清楚，代码和结果更可复现 | 论文级证据链、灵敏度/稳定性和表达还可以加强 |
| Outstanding | 模型、数据、结果、检验和结论形成闭环 | 复现时要区分官方数据、外部数据和论文校准参数 |

结论：这题最好的是 Outstanding，因为它不只是“算法更复杂”，而是把模型选择、约束、结果校验和可解释结论连起来。数据题要接到检测时点决策，并保留显著性、误差和风险阈值。

## 可复现运行

单篇运行：

```bash
/opt/homebrew/bin/python3 Math-Modeling-BAO/cumcm/outstanding_solutions/2025/C/C023/solution.py
```

统一 runner 运行：

```bash
/opt/homebrew/bin/python3 Math-Modeling-BAO/tools/run_outstanding_reproductions.py cumcm-2025-C-C023
```
