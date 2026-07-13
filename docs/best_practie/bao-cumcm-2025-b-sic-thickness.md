# CUMCM 2025-B 碳化硅外延层厚度测量：Baseline → Advanced → Outstanding 进阶

这道题的主入口是 **数据拟合/物理参数反演**。从教程角度看，baseline 解决“能跑通”，advanced 解决“更贴题”，Outstanding 解决“证据链完整、结果可检验、表达能让评委快速相信”。

## 材料入口

| 层级 | PDF | 代码 | 结果 |
|---|---|---|---|
| Baseline | `Math-Modeling-World-Reports/cumcm/2025-B/baseline/main.pdf` | `Math-Modeling-World/cumcm/generic_baselines/solutions/2025/B` | `Math-Modeling-World/cumcm/generic_baselines/results/2025/B` |
| Advanced | `Math-Modeling-World-Reports/cumcm/2025-B/advanced/main.pdf` | `Math-Modeling-World/cumcm/question_solutions/2025/B` | `Math-Modeling-World/cumcm/question_results/2025/B` |
| Outstanding | `Math-Modeling-World-Reports/outstanding/cumcm/2025-B/B157/pdf/B157.pdf` | `Math-Modeling-World/cumcm/outstanding_solutions/2025/B/B157/solution.py` | `Math-Modeling-World/cumcm/outstanding_solutions/2025/B/B157/result.json` |

OCR 文本：`Math-Modeling-World-Reports/outstanding/cumcm/2025-B/B157/ocr/B157.md`。

## 数据来源

本题复现使用的数据/参数入口如下：

- `type: official_cumcm_xlsx`
- `root: cumcm/source_materials/extracted/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/B题`
- `files: cumcm/source_materials/extracted/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/B题/附件/附件1.xlsx`
- `files: cumcm/source_materials/extracted/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/B题/附件/附件2.xlsx`
- `files: cumcm/source_materials/extracted/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/B题/附件/附件3.xlsx`
- `files: cumcm/source_materials/extracted/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/B题/附件/附件4.xlsx`

## Baseline：先把题跑通

Baseline 的价值是建立最小可运行闭环：逐问拆解、选择通用模型、生成 `result.json` 和图表。它通常能回答题目，但假设比较粗，指标之间的连接也不够强。

对这题来说，baseline 更像“第一版计算草稿”：可以帮助确认输入、输出和基本量纲，但还不足以支撑 O 奖级别的论证。

## Advanced：把题目机制接进模型

Advanced 的进步是：干涉光谱预处理、厚度拟合、残差检查和多束修正。

这一层通常已经能进入课程讲解，因为它开始把题目约束、官方数据、逐问任务和可复现代码接起来。相比 baseline，它更像一篇可提交论文的骨架。

## Outstanding：把模型链做完整

选用的 O 奖论文是 `B157`，标题为 `碳化硅外延层厚度的双光束和多光束干涉法测量研究`。

它的核心升级是：双光束/多光束干涉联合拟合，输出厚度、残差图和联合估计摘要。

当前复现的关键对齐指标如下：

| 指标 | 复现值 | 论文目标 | 误差/说明 |
|---|---:|---:|---|
| `experiment_result.sic_recommended_thickness_um` | 8.9815 | 见 O 论文表格/OCR | 旧脚本未声明 target_comparison；此处列 result.json 核心输出 |
| `experiment_result.si_recommended_thickness_um` | 10.5145 | 见 O 论文表格/OCR | 旧脚本未声明 target_comparison；此处列 result.json 核心输出 |
| `experiment_result.multi_beam_samples` | ['SiC'] | 见 O 论文表格/OCR | 旧脚本未声明 target_comparison；此处列 result.json 核心输出 |
| `joint_thickness_summary[0].sample` | Si | 见 O 论文表格/OCR | 旧脚本未声明 target_comparison；此处列 result.json 核心输出 |
| `joint_thickness_summary[0].joint_two_beam_thickness_um` | 10.5145 | 见 O 论文表格/OCR | 旧脚本未声明 target_comparison；此处列 result.json 核心输出 |
| `joint_thickness_summary[0].joint_airy_corrected_thickness_um` | 10.5144 | 见 O 论文表格/OCR | 旧脚本未声明 target_comparison；此处列 result.json 核心输出 |

## 谁做得最好

| 层级 | 能力 | 主要短板 |
|---|---|---|
| Baseline | 能快速产出逐问结果和基本图表 | 假设、指标和验证还比较模板化 |
| Advanced | 题目机制更清楚，代码和结果更可复现 | 论文级证据链、灵敏度/稳定性和表达还可以加强 |
| Outstanding | 模型、数据、结果、检验和结论形成闭环 | 复现时要区分官方数据、外部数据和论文校准参数 |

结论：这题最好的是 Outstanding，因为它不只是“算法更复杂”，而是把模型选择、约束、结果校验和可解释结论连起来。参数反演题要同时讲物理公式、数据拟合和残差诊断。

## 可复现运行

单篇运行：

```bash
/opt/homebrew/bin/python3 Math-Modeling-World/cumcm/outstanding_solutions/2025/B/B157/solution.py
```

统一 runner 运行：

```bash
/opt/homebrew/bin/python3 Math-Modeling-World/tools/run_outstanding_reproductions.py cumcm-2025-B-B157
```
