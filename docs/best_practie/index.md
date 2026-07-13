# Best Practice 索引

Best Practice 是这个教程的“读法说明书”。它不只是列算法，而是回答：一篇数模论文怎样从 baseline 变成 advanced，再继续走到可以对照 O 奖论文的 outstanding。

当前按 6 个模块阅读，序号就是推荐顺序。

## 00 阅读总图

| 问题 | 去哪里看 |
|---|---|
| 评委到底看什么 | [01 评奖标准](./award-evaluation-rules.md) |
| B/A/O 三层差别是什么 | [02 B/A/O 递进方法](./solution-levels-and-judging-rubric.md) |
| 一道题到底属于哪类模型 | [03 混合题型](./mixed-problem-patterns.md) 和 [04 求解器选择](./solver-selection-guide.md) |
| 数据、外部资料、文献怎么写 | [05 数据来源](./data-source-practice.md)、[06 文献综述](./literature-review-practice.md)、[07 数模论文 vs 科研论文](./modeling-paper-vs-research-paper.md) |
| 想直接看完整案例 | 先读 Batch 1 的 6 篇，再读 Batch 2 的 9 篇 |

PDF 不再作为独立学习路线。每道赛题的 Baseline / Advanced / Outstanding PDF 已经放进 MCM/CUMCM 赛题索引的 `BAO PDF` 列；完整 PDF 清单只作为下载 manifest 保留在 [PDF 下载清单](/reference/report-pdf-library)。

## 01 评奖标准与论文观

| 序号 | 文档 | 核心作用 |
|---:|---|---|
| 01 | [评奖标准](./award-evaluation-rules.md) | 把“假设合理、模型创新、结果正确、表达清楚”落成可检查项 |
| 02 | [B/A/O 递进方法](./solution-levels-and-judging-rubric.md) | 解释 baseline、advanced、outstanding 分别应该强在哪里 |
| 03 | [数模论文 vs 科研论文](./modeling-paper-vs-research-paper.md) | 避免把数模论文写成追求前沿复杂度的科研论文 |

## 02 题型识别与求解器

| 序号 | 文档 | 核心作用 |
|---:|---|---|
| 04 | [混合题型](./mixed-problem-patterns.md) | 说明“微分方程题”常接优化，“优化题”常接数据估计，“数据题”常接决策 |
| 05 | [求解器选择](./solver-selection-guide.md) | 对齐 ODE、优化、统计学习、图模型分别主要用什么库和求解器 |

三类题型可以这样记：

| 类别 | 典型起点 | 获奖论文通常继续接什么 |
|---|---|---|
| 微分方程/动态系统 | 状态随时间演化，使用 ODE、差分方程、动力系统仿真 | 优化、控制、资源分配、稳定性分析 |
| 运筹优化 | 路径、调度、选址、分配、排队、搜索 | 数据估计、情景模拟、风险评价、鲁棒性 |
| 数据建模 | 回归、分类、聚类、预测、统计检验 | 决策、排序、资源配置、政策建议 |

## 03 数据与文献

| 序号 | 文档 | 核心作用 |
|---:|---|---|
| 06 | [数据来源](./data-source-practice.md) | 区分官方数据、外部公开数据、O 奖论文参数和我们自己的假设 |
| 07 | [文献综述](./literature-review-practice.md) | 用 related work 引出“为什么本文采用适配题目的模型链” |
| 08 | [LLM 时代 O 奖观察](./llm-era-outstanding-patterns.md) | 比较 2023-2025 之后 O 奖论文的共性、变化和风险 |

## 04 Batch 1：三大题型 × MCM/CUMCM

这 6 篇是当前最适合入门的完整 B/A/O 案例：同一类数学基础分别看美赛和国赛各一题。

| 序号 | 类型 | 竞赛 | 案例 |
|---:|---|---|---|
| 01 | 微分方程/动态系统 | MCM | [2015-A Ebola](./bao-mcm-2015-a-ebola.md) |
| 02 | 微分方程/动态系统 | CUMCM | [2018-A 高温作业服装](./bao-cumcm-2018-a-heat-clothing.md) |
| 03 | 运筹优化 | MCM | [2017-B Merge After Toll](./bao-mcm-2017-b-toll-plaza.md) |
| 04 | 运筹优化 | CUMCM | [2020-B 穿越沙漠](./bao-cumcm-2020-b-desert-crossing.md) |
| 05 | 数据建模 | MCM | [2019-C Opioids](./bao-mcm-2019-c-opioid.md) |
| 06 | 数据建模 | CUMCM | [2020-C 中小微企业信贷](./bao-cumcm-2020-c-credit.md) |

## 05 Batch 2：2023-2025 MCM ABC

这 9 篇是现代样板，覆盖 LLM 爆发后的 2023、2024、2025 三年 MCM A/B/C。它们仍按三类题型理解：A 偏动态/物理机制，B 偏优化/决策，C 偏数据建模。

| 序号 | 年份 | 题号 | 类型 | 案例 | O 论文 |
|---:|---|---|---|---|---|
| 07 | 2023 | A | 动态系统/生态模型 | [Plant Community](./bao-mcm-2023-a-plant-community.md) | 2309229 |
| 08 | 2023 | B | 运筹优化/空间分区 | [Maasai Mara](./bao-mcm-2023-b-maasai-mara.md) | 2315379 |
| 09 | 2023 | C | 数据建模/预测分类 | [Wordle](./bao-mcm-2023-c-wordle.md) | 2307946 |
| 10 | 2024 | A | 动态系统/生态模型 | [Lamprey](./bao-mcm-2024-a-lamprey.md) | 2407093 |
| 11 | 2024 | B | 运筹优化/搜索救援 | [Submersible Search](./bao-mcm-2024-b-submersible-search.md) | 2419984 |
| 12 | 2024 | C | 数据建模/统计推断 | [Tennis Momentum](./bao-mcm-2024-c-tennis-momentum.md) | 2401298 |
| 13 | 2025 | A | 物理反演/动态磨损 | [Stair Wear](./bao-mcm-2025-a-stair-wear.md) | 2501909 |
| 14 | 2025 | B | 运筹优化/可持续旅游 | [Juneau Tourism](./bao-mcm-2025-b-juneau-tourism.md) | 2504448 |
| 15 | 2025 | C | 数据建模/预测排序 | [Olympic Medals](./bao-mcm-2025-c-olympic-medals.md) | 2505964 |

## 06 扩展材料与候选案例

下面这些文档有参考价值，但不计入当前“正式 15 篇 O 奖复现”口径；它们更适合作为后续转正、补齐 CUMCM 现代样板时的候选材料。

| 类别 | 文档 |
|---|---|
| CUMCM 2023 ABC 候选 | [2023-A 定日镜场](./bao-cumcm-2023-a-heliostat-field.md)、[2023-B 多波束测线](./bao-cumcm-2023-b-multibeam-lines.md)、[2023-C 蔬菜定价](./bao-cumcm-2023-c-vegetable-pricing.md) |
| CUMCM 2024 ABC 候选 | [2024-A 板凳龙](./bao-cumcm-2024-a-dragon-dance.md)、[2024-B 生产决策](./bao-cumcm-2024-b-production-decision.md)、[2024-C 农作物规划](./bao-cumcm-2024-c-crop-planting.md) |
| CUMCM 2025 ABC 候选 | [2025-A 烟幕遮蔽](./bao-cumcm-2025-a-smoke-screen.md)、[2025-B 碳化硅测厚](./bao-cumcm-2025-b-sic-thickness.md)、[2025-C NIPT](./bao-cumcm-2025-c-nipt.md) |
| 审计记录 | [2023-2025 MCM ABC 复现审计](./outstanding-reproduction-audit-2023-2025-abc.md)、[2024 MCM ABC 复现核对](./outstanding-reproduction-audit-2024-abc.md) |

## 后续扩展规则

以后补新案例时，每道题都沿用同一结构：

1. 材料入口：赛题页、Baseline PDF、Advanced PDF、O 奖 PDF/OCR、代码、结果。
2. 题型定位：它属于动态、优化、数据建模，还是混合题。
3. Baseline：能跑通什么，哪里太粗。
4. Advanced：接入了哪些真实数据和题面约束。
5. Outstanding：论文级模型链、验证、灵敏度分析和表达到底强在哪里。
6. 数据和文献：哪些来自官方，哪些来自外部，哪些来自 O 奖论文。
7. 复现状态：当前代码能不能重跑，结果和论文对齐到什么程度。
