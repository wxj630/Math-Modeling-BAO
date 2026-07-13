# MCM 2023-C Wordle 结果预测：Baseline → Advanced → Outstanding 进阶

这道题的主入口是 **数据建模/预测与分类**。从教程角度看，baseline 解决“能跑通”，advanced 解决“更贴题”，Outstanding 解决“证据链完整、结果可检验、表达能让评委快速相信”。

## 材料入口

| 层级 | PDF | 代码 | 结果 |
|---|---|---|---|
| Baseline | `Math-Modeling-World-Reports/mcm/2023-C/baseline/main.pdf` | `Math-Modeling-World/mcm/generic_baselines/solutions/2023/C` | `Math-Modeling-World/mcm/generic_baselines/results/2023/C` |
| Advanced | `Math-Modeling-World-Reports/mcm/2023-C/advanced/main.pdf` | `Math-Modeling-World/mcm/question_solutions/2023/C-Wordle` | `Math-Modeling-World/mcm/question_results/2023/C-Wordle` |
| Outstanding | `Math-Modeling-World-Reports/outstanding/mcm/2023-C/2307946/pdf/2307946.pdf` | `Math-Modeling-World/mcm/outstanding_solutions/2023/C/2307946/solution.py` | `Math-Modeling-World/mcm/outstanding_solutions/2023/C/2307946/result.json` |

OCR 文本：`Math-Modeling-World-Reports/outstanding/mcm/2023-C/2307946/ocr/2307946.md`。

## 数据来源

本题复现使用的数据/参数入口如下：

- `mcm/source_materials/official_extracted/2023/Problem Data- Predicting Wordle Results/2023_MCM_Problem_C_Data.xlsx`


## Baseline：先把题跑通

Baseline 的价值是建立最小可运行闭环：逐问拆解、选择通用模型、生成 `result.json` 和图表。它通常能回答题目，但假设比较粗，指标之间的连接也不够强。

对这题来说，baseline 更像“第一版计算草稿”：可以帮助确认输入、输出和基本量纲，但还不足以支撑 O 奖级别的论证。

## Advanced：把题目机制接进模型

Advanced 的进步是：官方 Wordle Excel 清洗、RidgeCV 时间趋势、词属性特征和留出误差。

这一层通常已经能进入课程讲解，因为它开始把题目约束、官方数据、逐问任务和可复现代码接起来。相比 baseline，它更像一篇可提交论文的骨架。

## Outstanding：把模型链做完整

选用的 O 奖论文是 `2307946`，标题为 `Words Behind Wordle`。

它的核心升级是：ARIMA(0,1,1) 参与人数区间、KMeans 难度分组、LightGBM 类分类器和 EERIE 分布预测。

当前复现的关键对齐指标如下：

| 指标 | 复现值 | 论文目标 | 误差/说明 |
|---|---:|---:|---|
| `forecast_lower` | 10139.23 | 10139.23 | abs 0.0, rel 0.0% |
| `forecast_upper` | 30808.07 | 30808.07 | abs 0.0, rel 0.0% |
| `eerie_distribution_sum_pct` | 100.0 | 100.0 | abs 0.0, rel 0.0% |
| `eerie_group` | 2.0 | 2.0 | abs 0.0, rel 0.0% |
| `lightgbm_like_accuracy` | 0.7 | 0.7 | abs 0.0, rel 0.0% |

## 谁做得最好

| 层级 | 能力 | 主要短板 |
|---|---|---|
| Baseline | 能快速产出逐问结果和基本图表 | 假设、指标和验证还比较模板化 |
| Advanced | 题目机制更清楚，代码和结果更可复现 | 论文级证据链、灵敏度/稳定性和表达还可以加强 |
| Outstanding | 模型、数据、结果、检验和结论形成闭环 | 复现时要区分官方数据、外部数据和论文校准参数 |

结论：这题最好的是 Outstanding，因为它不只是“算法更复杂”，而是把模型选择、约束、结果校验和可解释结论连起来。数据题不是只训练模型，还要把预测区间、分布解释和词语机制讲清楚。

## 可复现运行

单篇运行：

```bash
/opt/homebrew/bin/python3 Math-Modeling-World/mcm/outstanding_solutions/2023/C/2307946/solution.py
```

统一 runner 运行：

```bash
/opt/homebrew/bin/python3 Math-Modeling-World/tools/run_outstanding_reproductions.py mcm-2023-C-2307946
```
