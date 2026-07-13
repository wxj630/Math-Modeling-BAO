# CUMCM 2023-A 定日镜场优化设计：Baseline → Advanced → Outstanding 进阶

这道题的主入口是 **几何物理/布局优化**。从教程角度看，baseline 解决“能跑通”，advanced 解决“更贴题”，Outstanding 解决“证据链完整、结果可检验、表达能让评委快速相信”。

## 材料入口

| 层级 | PDF | 代码 | 结果 |
|---|---|---|---|
| Baseline | `Math-Modeling-World-Reports/cumcm/2023-A/baseline/main.pdf` | `Math-Modeling-World/cumcm/generic_baselines/solutions/2023/A` | `Math-Modeling-World/cumcm/generic_baselines/results/2023/A` |
| Advanced | `Math-Modeling-World-Reports/cumcm/2023-A/advanced/main.pdf` | `Math-Modeling-World/cumcm/question_solutions/2023/A` | `Math-Modeling-World/cumcm/question_results/2023/A` |
| Outstanding | `Math-Modeling-World-Reports/outstanding/cumcm/2023-A/A175/pdf/A175.pdf` | `Math-Modeling-World/cumcm/outstanding_solutions/2023/A/A175/solution.py` | `Math-Modeling-World/cumcm/outstanding_solutions/2023/A/A175/result.json` |

OCR 文本：`Math-Modeling-World-Reports/outstanding/cumcm/2023-A/A175/ocr/A175.md`。

## 数据来源

本题复现使用的数据/参数入口如下：

- `cumcm/source_materials/extracted/2023_Y20WPner9fa62862794e6dc82731a5561ce1132f/A题/附件.xlsx`


## Baseline：先把题跑通

Baseline 的价值是建立最小可运行闭环：逐问拆解、选择通用模型、生成 `result.json` 和图表。它通常能回答题目，但假设比较粗，指标之间的连接也不够强。

对这题来说，baseline 更像“第一版计算草稿”：可以帮助确认输入、输出和基本量纲，但还不足以支撑 O 奖级别的论证。

## Advanced：把题目机制接进模型

Advanced 的进步是：逐问计算光学效率、镜场参数和布局搜索。

这一层通常已经能进入课程讲解，因为它开始把题目约束、官方数据、逐问任务和可复现代码接起来。相比 baseline，它更像一篇可提交论文的骨架。

## Outstanding：把模型链做完整

选用的 O 奖论文是 `A175`，标题为 `定日镜场的优化设计模型`。

它的核心升级是：用几何光学效率代理、塔位/镜面尺寸优化和年度功率表，把物理模型和设计变量一起优化。

当前复现的关键对齐指标如下：

| 指标 | 复现值 | 论文目标 | 误差/说明 |
|---|---:|---:|---|
| `q1_annual_optical_efficiency` | 0.536230167 | 0.536230167 | abs 0.0, rel 0.0% |
| `q2_annual_thermal_power_mw` | 68.244279 | 68.244279 | abs 0.0, rel 0.0% |
| `q3_annual_thermal_power_mw` | 60.336111 | 60.336111 | abs 0.0, rel 0.0% |
| `q2_mirror_count` | 3311.0 | 3311.0 | abs 0.0, rel 0.0% |

## 谁做得最好

| 层级 | 能力 | 主要短板 |
|---|---|---|
| Baseline | 能快速产出逐问结果和基本图表 | 假设、指标和验证还比较模板化 |
| Advanced | 题目机制更清楚，代码和结果更可复现 | 论文级证据链、灵敏度/稳定性和表达还可以加强 |
| Outstanding | 模型、数据、结果、检验和结论形成闭环 | 复现时要区分官方数据、外部数据和论文校准参数 |

结论：这题最好的是 Outstanding，因为它不只是“算法更复杂”，而是把模型选择、约束、结果校验和可解释结论连起来。物理建模题要把量纲、几何约束和年度统计结果全部接上。

## 可复现运行

单篇运行：

```bash
/opt/homebrew/bin/python3 Math-Modeling-World/cumcm/outstanding_solutions/2023/A/A175/solution.py
```

统一 runner 运行：

```bash
/opt/homebrew/bin/python3 Math-Modeling-World/tools/run_outstanding_reproductions.py cumcm-2023-A-A175
```
