# 数学建模 Best Practice 索引

这个目录用于沉淀教程材料：不是单纯列算法，而是解释一篇数模论文怎样从 baseline 变成 advanced，再接近 outstanding。

当前先把材料分成三层：通用评奖标准、数据与文献、具体赛题案例。后续扩展 2023/2024/2025 的 MCM/CUMCM ABC 题时，也按这个结构补。

## 先读这几篇

| 主题 | 文档 | 适合解决的问题 |
|---|---|---|
| 评奖标准 | [award-evaluation-rules.md](./award-evaluation-rules.md) | 先知道评委看什么 |
| B/A/O 递进 | [solution-levels-and-judging-rubric.md](./solution-levels-and-judging-rubric.md) | 理解 baseline、advanced、outstanding 的差别 |
| 求解器选择 | [solver-selection-guide.md](./solver-selection-guide.md) | 判断 ODE、优化、数据建模分别用什么库和求解器 |
| 混合题型 | [mixed-problem-patterns.md](./mixed-problem-patterns.md) | 防止把题目误看成单一算法题 |
| 数据来源 | [data-source-practice.md](./data-source-practice.md) | 说明官方数据、外部数据、O 奖论文参数怎么区分 |
| 文献综述 | [literature-review-practice.md](./literature-review-practice.md) | 写 related work，并引出自己的方法创新 |
| 数模论文 vs 科研论文 | [modeling-paper-vs-research-paper.md](./modeling-paper-vs-research-paper.md) | 区分追求前沿和追求适配，避免 lit review 写偏 |

## 三类题型的核心理解

我们现在强调的 ABC 三类题型可以这样记：

| 类别 | 典型起点 | 真正获奖时通常还会接什么 |
|---|---|---|
| 微分方程/动态系统 | 状态随时间演化，使用 ODE、差分方程、动力系统仿真 | 优化、控制、资源分配、稳定性分析 |
| 运筹优化 | 路径、调度、选址、分配、排队、搜索 | 数据估计、情景模拟、风险评价、鲁棒性 |
| 数据建模 | 回归、分类、聚类、预测、统计检验 | 决策、排序、资源配置、政策建议 |

重要的是：题型只是入口，不是终点。优秀论文往往是混合链条。

## 已有 6 篇经典 B/A/O 案例

| 类型 | 竞赛 | 案例 |
|---|---|---|
| 微分方程/动态系统 | MCM | [bao-mcm-2015-a-ebola.md](./bao-mcm-2015-a-ebola.md) |
| 微分方程/动态系统 | CUMCM | [bao-cumcm-2018-a-heat-clothing.md](./bao-cumcm-2018-a-heat-clothing.md) |
| 运筹优化 | MCM | [bao-mcm-2017-b-toll-plaza.md](./bao-mcm-2017-b-toll-plaza.md) |
| 运筹优化 | CUMCM | [bao-cumcm-2020-b-desert-crossing.md](./bao-cumcm-2020-b-desert-crossing.md) |
| 数据建模 | MCM | [bao-mcm-2019-c-opioid.md](./bao-mcm-2019-c-opioid.md) |
| 数据建模 | CUMCM | [bao-cumcm-2020-c-credit.md](./bao-cumcm-2020-c-credit.md) |

## 2023-2025 ABC B/A/O 案例

这 18 篇是当前教程的现代样板：2023、2024、2025 三年，MCM/CUMCM 两个竞赛，每年 A/B/C 三题。每篇文档都按 baseline、advanced、outstanding 三层解释，并给出 PDF、代码、结果和 O 奖复现入口。

| 年份 | 竞赛 | 题号 | 类型 | 文档 | O 论文 |
|---|---|---|---|---|---|
| 2023 | MCM | A | 动态系统/生态微分方程 | [bao-mcm-2023-a-plant-community.md](./bao-mcm-2023-a-plant-community.md) | 2309229 |
| 2023 | MCM | B | 运筹优化/空间分区 | [bao-mcm-2023-b-maasai-mara.md](./bao-mcm-2023-b-maasai-mara.md) | 2315379 |
| 2023 | MCM | C | 数据建模/预测与分类 | [bao-mcm-2023-c-wordle.md](./bao-mcm-2023-c-wordle.md) | 2307946 |
| 2023 | CUMCM | A | 几何物理/布局优化 | [bao-cumcm-2023-a-heliostat-field.md](./bao-cumcm-2023-a-heliostat-field.md) | A175 |
| 2023 | CUMCM | B | 运筹优化/测线布设 | [bao-cumcm-2023-b-multibeam-lines.md](./bao-cumcm-2023-b-multibeam-lines.md) | B226 |
| 2023 | CUMCM | C | 数据建模/定价补货决策 | [bao-cumcm-2023-c-vegetable-pricing.md](./bao-cumcm-2023-c-vegetable-pricing.md) | C050 |
| 2024 | MCM | A | 动态系统/生态模型 | [bao-mcm-2024-a-lamprey.md](./bao-mcm-2024-a-lamprey.md) | 2407093 |
| 2024 | MCM | B | 运筹优化/搜索救援 | [bao-mcm-2024-b-submersible-search.md](./bao-mcm-2024-b-submersible-search.md) | 2419984 |
| 2024 | MCM | C | 数据建模/统计推断 | [bao-mcm-2024-c-tennis-momentum.md](./bao-mcm-2024-c-tennis-momentum.md) | 2401298 |
| 2024 | CUMCM | A | 动态系统/几何运动学 | [bao-cumcm-2024-a-dragon-dance.md](./bao-cumcm-2024-a-dragon-dance.md) | A016 |
| 2024 | CUMCM | B | 运筹优化/抽检决策 | [bao-cumcm-2024-b-production-decision.md](./bao-cumcm-2024-b-production-decision.md) | B159 |
| 2024 | CUMCM | C | 运筹优化/农业种植规划 | [bao-cumcm-2024-c-crop-planting.md](./bao-cumcm-2024-c-crop-planting.md) | C038 |
| 2025 | MCM | A | 物理反演/动态磨损 | [bao-mcm-2025-a-stair-wear.md](./bao-mcm-2025-a-stair-wear.md) | 2501909 |
| 2025 | MCM | B | 运筹优化/可持续旅游 | [bao-mcm-2025-b-juneau-tourism.md](./bao-mcm-2025-b-juneau-tourism.md) | 2504448 |
| 2025 | MCM | C | 数据建模/预测排序 | [bao-mcm-2025-c-olympic-medals.md](./bao-mcm-2025-c-olympic-medals.md) | 2505964 |
| 2025 | CUMCM | A | 动态系统/轨迹优化 | [bao-cumcm-2025-a-smoke-screen.md](./bao-cumcm-2025-a-smoke-screen.md) | A196 |
| 2025 | CUMCM | B | 数据拟合/物理参数反演 | [bao-cumcm-2025-b-sic-thickness.md](./bao-cumcm-2025-b-sic-thickness.md) | B157 |
| 2025 | CUMCM | C | 数据建模/医学统计决策 | [bao-cumcm-2025-c-nipt.md](./bao-cumcm-2025-c-nipt.md) | C023 |

## 复现审计与 LLM 时代观察

| 文档 | 用途 |
|---|---|
| [outstanding-reproduction-audit-2023-2025-abc.md](./outstanding-reproduction-audit-2023-2025-abc.md) | 核对 2023-2025 MCM/CUMCM ABC 共 18 篇 O 奖复现是否能统一 runner 跑通 |
| [outstanding-reproduction-audit-2024-abc.md](./outstanding-reproduction-audit-2024-abc.md) | 核对 2024 ABC 的 O 论文 OCR、PDF、复现代码和结果是否对得上 |
| [llm-era-outstanding-patterns.md](./llm-era-outstanding-patterns.md) | 分析 2023-2025 之后 O 奖论文和早期 O 奖论文的相同点、变化点和风险点 |

## 后续扩展规则

以后补 2023、2024、2025 的 MCM/CUMCM ABC 题时，每道题都建议沿用同一个结构：

1. 材料入口：baseline PDF、advanced PDF、O 奖 PDF/OCR、代码、结果。
2. 题型定位：它属于动态、优化、数据建模，还是混合题。
3. Baseline：能跑通什么，哪里太粗。
4. Advanced：接入了哪些真实数据和题面约束。
5. Outstanding：论文级模型链、验证、灵敏度分析和表达到底强在哪里。
6. 数据和文献：哪些来自官方，哪些来自外部，哪些来自 O 奖论文。
7. 复现状态：当前代码能不能重跑，结果和论文对齐到什么程度。
