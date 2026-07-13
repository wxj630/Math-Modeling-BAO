# CUMCM 2023-C 蔬菜动态定价与补货：Baseline → Advanced → Outstanding 进阶

这道题的主入口是 **数据建模/定价补货决策**。从教程角度看，baseline 解决“能跑通”，advanced 解决“更贴题”，Outstanding 解决“证据链完整、结果可检验、表达能让评委快速相信”。

## 材料入口

| 层级 | PDF | 代码 | 结果 |
|---|---|---|---|
| Baseline | `Math-Modeling-World-Reports/cumcm/2023-C/baseline/main.pdf` | `Math-Modeling-World/cumcm/generic_baselines/solutions/2023/C` | `Math-Modeling-World/cumcm/generic_baselines/results/2023/C` |
| Advanced | `Math-Modeling-World-Reports/cumcm/2023-C/advanced/main.pdf` | `Math-Modeling-World/cumcm/question_solutions/2023/C` | `Math-Modeling-World/cumcm/question_results/2023/C` |
| Outstanding | `Math-Modeling-World-Reports/outstanding/cumcm/2023-C/C050/pdf/C050.pdf` | `Math-Modeling-World/cumcm/outstanding_solutions/2023/C/C050/solution.py` | `Math-Modeling-World/cumcm/outstanding_solutions/2023/C/C050/result.json` |

OCR 文本：`Math-Modeling-World-Reports/outstanding/cumcm/2023-C/C050/ocr/C050.md`。

## 数据来源

本题复现使用的数据/参数入口如下：

- `cumcm/source_materials/extracted/2023_Y20WPner9fa62862794e6dc82731a5561ce1132f/C题/附件1.xlsx`
- `cumcm/source_materials/extracted/2023_Y20WPner9fa62862794e6dc82731a5561ce1132f/C题/附件2.xlsx`
- `cumcm/source_materials/extracted/2023_Y20WPner9fa62862794e6dc82731a5561ce1132f/C题/附件3.xlsx`
- `cumcm/source_materials/extracted/2023_Y20WPner9fa62862794e6dc82731a5561ce1132f/C题/附件4.xlsx`


## Baseline：先把题跑通

Baseline 的价值是建立最小可运行闭环：逐问拆解、选择通用模型、生成 `result.json` 和图表。它通常能回答题目，但假设比较粗，指标之间的连接也不够强。

对这题来说，baseline 更像“第一版计算草稿”：可以帮助确认输入、输出和基本量纲，但还不足以支撑 O 奖级别的论证。

## Advanced：把题目机制接进模型

Advanced 的进步是：官方四附件清洗、销量预测、类别定价和补货优化。

这一层通常已经能进入课程讲解，因为它开始把题目约束、官方数据、逐问任务和可复现代码接起来。相比 baseline，它更像一篇可提交论文的骨架。

## Outstanding：把模型链做完整

选用的 O 奖论文是 `C050`，标题为 `某商超蔬菜类商品动态定价与补货决策研究`。

它的核心升级是：KMeans++ 单品聚类、加成率相关、价格-销量回归和未来 7 天利润/29 个单品清单。

当前复现的关键对齐指标如下：

| 指标 | 复现值 | 论文目标 | 误差/说明 |
|---|---:|---:|---|
| `future_week_max_profit_yuan` | 5105.6 | 5105.6 | abs 0.0, rel 0.0% |
| `problem3_selected_item_count` | 29.0 | 29.0 | abs 0.0, rel 0.0% |
| `problem3_july1_profit_yuan` | 1282.2631 | 1282.2631 | abs 0.0, rel 0.0% |

## 谁做得最好

| 层级 | 能力 | 主要短板 |
|---|---|---|
| Baseline | 能快速产出逐问结果和基本图表 | 假设、指标和验证还比较模板化 |
| Advanced | 题目机制更清楚，代码和结果更可复现 | 论文级证据链、灵敏度/稳定性和表达还可以加强 |
| Outstanding | 模型、数据、结果、检验和结论形成闭环 | 复现时要区分官方数据、外部数据和论文校准参数 |

结论：这题最好的是 Outstanding，因为它不只是“算法更复杂”，而是把模型选择、约束、结果校验和可解释结论连起来。数据建模题最后要落到定价、补货、排序和利润，而不是停在相关性。

## 可复现运行

单篇运行：

```bash
/opt/homebrew/bin/python3 Math-Modeling-World/cumcm/outstanding_solutions/2023/C/C050/solution.py
```

统一 runner 运行：

```bash
/opt/homebrew/bin/python3 Math-Modeling-World/tools/run_outstanding_reproductions.py cumcm-2023-C-C050
```
