# MCM 2025-C 奥运奖牌预测：Baseline → Advanced → Outstanding 进阶

这道题的主入口是 **数据建模/预测排序**。从教程角度看，baseline 解决“能跑通”，advanced 解决“更贴题”，Outstanding 解决“证据链完整、结果可检验、表达能让评委快速相信”。

## 材料入口

| 层级 | PDF | 代码 | 结果 |
|---|---|---|---|
| Baseline | `Math-Modeling-BAO-Reports/mcm/2025-C/baseline/main.pdf` | `Math-Modeling-BAO/mcm/generic_baselines/solutions/2025/C` | `Math-Modeling-BAO/mcm/generic_baselines/results/2025/C` |
| Advanced | `Math-Modeling-BAO-Reports/mcm/2025-C/advanced/main.pdf` | `Math-Modeling-BAO/docs/mcm-2015-2025/real_solutions/2025/MCM-C/solution.py` | `Math-Modeling-BAO/docs/mcm-2015-2025/real_solutions/2025/MCM-C/result.json` |
| Outstanding | `Math-Modeling-BAO-Reports/outstanding/mcm/2025-C/2505964/pdf/2505964.pdf` | `Math-Modeling-BAO/mcm/outstanding_solutions/2025/C/2505964/solution.py` | `Math-Modeling-BAO/mcm/outstanding_solutions/2025/C/2505964/result.json` |

OCR 文本：`Math-Modeling-BAO-Reports/outstanding/mcm/2025-C/2505964/ocr/2505964.md`。

## 数据来源

本题复现使用的数据/参数入口如下：

- `type: official_comap_csv`
- `root: docs/mcm-2015-2025/official_assets_extracted/2025/2025_Problem_C_Data.zip/2025_Problem_C_Data`
- `rows: summerOly_medal_counts.csv: 1435`
- `rows: summerOly_athletes.csv: 252565`
- `rows: summerOly_hosts.csv: 35`
- `rows: summerOly_programs.csv: 74`
- `rows: data_dictionary.csv: 50`

## Baseline：先把题跑通

Baseline 的价值是建立最小可运行闭环：逐问拆解、选择通用模型、生成 `result.json` 和图表。它通常能回答题目，但假设比较粗，指标之间的连接也不够强。

对这题来说，baseline 更像“第一版计算草稿”：可以帮助确认输入、输出和基本量纲，但还不足以支撑 O 奖级别的论证。

## Advanced：把题目机制接进模型

Advanced 的进步是：历史奖牌、项目、主场效应和机器学习预测。

这一层通常已经能进入课程讲解，因为它开始把题目约束、官方数据、逐问任务和可复现代码接起来。相比 baseline，它更像一篇可提交论文的骨架。

## Outstanding：把模型链做完整

选用的 O 奖论文是 `2505964`，标题为 `2028 Olympic Medal Predictions Based on Random Forest Model`。

它的核心升级是：随机森林预测国家奖牌，并输出运动员/国家概率表和不确定性检查。

当前复现的关键对齐指标如下：

| 指标 | 复现值 | 论文目标 | 误差/说明 |
|---|---:|---:|---|
| `model_evaluation.holdout_year` | 2024 | 见 O 论文表格/OCR | 旧脚本未声明 target_comparison；此处列 result.json 核心输出 |
| `model_evaluation.sport_models` | 50 | 见 O 论文表格/OCR | 旧脚本未声明 target_comparison；此处列 result.json 核心输出 |
| `model_evaluation.status_counts.GoldBinary:fallback_mean` | 7 | 见 O 论文表格/OCR | 旧脚本未声明 target_comparison；此处列 result.json 核心输出 |
| `model_evaluation.status_counts.GoldBinary:random_forest` | 43 | 见 O 论文表格/OCR | 旧脚本未声明 target_comparison；此处列 result.json 核心输出 |
| `model_evaluation.status_counts.MedalBinary:fallback_mean` | 7 | 见 O 论文表格/OCR | 旧脚本未声明 target_comparison；此处列 result.json 核心输出 |
| `model_evaluation.status_counts.MedalBinary:random_forest` | 43 | 见 O 论文表格/OCR | 旧脚本未声明 target_comparison；此处列 result.json 核心输出 |

## 谁做得最好

| 层级 | 能力 | 主要短板 |
|---|---|---|
| Baseline | 能快速产出逐问结果和基本图表 | 假设、指标和验证还比较模板化 |
| Advanced | 题目机制更清楚，代码和结果更可复现 | 论文级证据链、灵敏度/稳定性和表达还可以加强 |
| Outstanding | 模型、数据、结果、检验和结论形成闭环 | 复现时要区分官方数据、外部数据和论文校准参数 |

结论：这题最好的是 Outstanding，因为它不只是“算法更复杂”，而是把模型选择、约束、结果校验和可解释结论连起来。预测题最后要给排序、区间、异常国家解释和可复查数据表。

## 可复现运行

单篇运行：

```bash
/opt/homebrew/bin/python3 Math-Modeling-BAO/mcm/outstanding_solutions/2025/C/2505964/solution.py
```

统一 runner 运行：

```bash
/opt/homebrew/bin/python3 Math-Modeling-BAO/tools/run_outstanding_reproductions.py mcm-2025-C-2505964
```
