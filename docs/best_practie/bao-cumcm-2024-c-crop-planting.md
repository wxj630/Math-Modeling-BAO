# CUMCM 2024-C 农作物种植策略：Baseline → Advanced → Outstanding 进阶

这道题的主入口是 **运筹优化/农业种植规划**。从教程角度看，baseline 解决“能跑通”，advanced 解决“更贴题”，Outstanding 解决“证据链完整、结果可检验、表达能让评委快速相信”。

## 材料入口

| 层级 | PDF | 代码 | 结果 |
|---|---|---|---|
| Baseline | `Math-Modeling-World-Reports/cumcm/2024-C/baseline/main.pdf` | `Math-Modeling-World/cumcm/generic_baselines/solutions/2024/C` | `Math-Modeling-World/cumcm/generic_baselines/results/2024/C` |
| Advanced | `Math-Modeling-World-Reports/cumcm/2024-C/advanced/main.pdf` | `Math-Modeling-World/cumcm/question_solutions/2024/C` | `Math-Modeling-World/cumcm/question_results/2024/C` |
| Outstanding | `Math-Modeling-World-Reports/outstanding/cumcm/2024-C/C038/pdf/C038.pdf` | `Math-Modeling-World/cumcm/outstanding_solutions/2024/C/C038/solution.py` | `Math-Modeling-World/cumcm/outstanding_solutions/2024/C/C038/result.json` |

OCR 文本：`Math-Modeling-World-Reports/outstanding/cumcm/2024-C/C038/ocr/C038.md`。

## 数据来源

本题复现使用的数据/参数入口如下：

- `result.json 未声明额外数据源；请查看脚本内 DATA_FILE/PAPER_SOURCE 常量。`

## Baseline：先把题跑通

Baseline 的价值是建立最小可运行闭环：逐问拆解、选择通用模型、生成 `result.json` 和图表。它通常能回答题目，但假设比较粗，指标之间的连接也不够强。

对这题来说，baseline 更像“第一版计算草稿”：可以帮助确认输入、输出和基本量纲，但还不足以支撑 O 奖级别的论证。

## Advanced：把题目机制接进模型

Advanced 的进步是：土地约束、作物收益、轮作约束和多期规划。

这一层通常已经能进入课程讲解，因为它开始把题目约束、官方数据、逐问任务和可复现代码接起来。相比 baseline，它更像一篇可提交论文的骨架。

## Outstanding：把模型链做完整

选用的 O 奖论文是 `C038`，标题为 `基于差分遗传算法的农作物种植策略优化`。

它的核心升级是：用差分遗传算法搜索多地块多作物方案，并保留收益、约束和鲁棒情景比较。

当前复现的关键对齐指标如下：

| 指标 | 复现值 | 论文目标 | 误差/说明 |
|---|---:|---:|---|
| `experiment_result.data_source.type` | official_cumcm_xlsx | 见 O 论文表格/OCR | 旧脚本未声明 target_comparison；此处列 result.json 核心输出 |
| `experiment_result.data_source.land_path` | cumcm/source_materials/extracted/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed... | 见 O 论文表格/OCR | 旧脚本未声明 target_comparison；此处列 result.json 核心输出 |
| `experiment_result.data_source.stat_path` | cumcm/source_materials/extracted/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed... | 见 O 论文表格/OCR | 旧脚本未声明 target_comparison；此处列 result.json 核心输出 |
| `experiment_result.data_source.plots` | 54 | 见 O 论文表格/OCR | 旧脚本未声明 target_comparison；此处列 result.json 核心输出 |
| `experiment_result.data_source.crops` | 42 | 见 O 论文表格/OCR | 旧脚本未声明 target_comparison；此处列 result.json 核心输出 |
| `experiment_result.data_source.candidate_rows` | 1230 | 见 O 论文表格/OCR | 旧脚本未声明 target_comparison；此处列 result.json 核心输出 |

## 谁做得最好

| 层级 | 能力 | 主要短板 |
|---|---|---|
| Baseline | 能快速产出逐问结果和基本图表 | 假设、指标和验证还比较模板化 |
| Advanced | 题目机制更清楚，代码和结果更可复现 | 论文级证据链、灵敏度/稳定性和表达还可以加强 |
| Outstanding | 模型、数据、结果、检验和结论形成闭环 | 复现时要区分官方数据、外部数据和论文校准参数 |

结论：这题最好的是 Outstanding，因为它不只是“算法更复杂”，而是把模型选择、约束、结果校验和可解释结论连起来。农业优化题前面要做收益/产量估计，后面要做多期约束和情景鲁棒性。

## 可复现运行

单篇运行：

```bash
/opt/homebrew/bin/python3 Math-Modeling-World/cumcm/outstanding_solutions/2024/C/C038/solution.py
```

统一 runner 运行：

```bash
/opt/homebrew/bin/python3 Math-Modeling-World/tools/run_outstanding_reproductions.py cumcm-2024-C-C038
```
