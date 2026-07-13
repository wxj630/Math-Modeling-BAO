# Outstanding Solution

Outstanding solution 是按“整道赛题”打磨出来的论文级版本。它不是把每个小问单独加长，而是选择一篇官方获奖论文，复现其中可验证的模型链、代码、实验结果和论文级分析。

当前正式口径是 **15 篇 O 奖复现**：Batch 1 的 6 篇用于理解三大题型在 MCM/CUMCM 中的基本形态，Batch 2 的 9 篇用于观察 2023-2025 MCM ABC 题在 LLM 时代之后的论文风格。

## Batch 1：三大题型 × MCM/CUMCM

| 题型 | 赛题 | 论文编号 | 文档 |
|---|---|---|---|
| 微分方程/动态系统 | MCM 2015-A Ebola | `35532` | [B/A/O 案例](/best_practie/bao-mcm-2015-a-ebola) |
| 微分方程/动态系统 | CUMCM 2018-A 高温作业服装 | `A466` | [B/A/O 案例](/best_practie/bao-cumcm-2018-a-heat-clothing) |
| 运筹优化 | MCM 2017-B Merge After Toll | `69427` | [B/A/O 案例](/best_practie/bao-mcm-2017-b-toll-plaza) |
| 运筹优化 | CUMCM 2020-B 穿越沙漠 | `B108` | [B/A/O 案例](/best_practie/bao-cumcm-2020-b-desert-crossing) |
| 数据建模 | MCM 2019-C Opioids | `1901213` | [B/A/O 案例](/best_practie/bao-mcm-2019-c-opioid) |
| 数据建模 | CUMCM 2020-C 中小微企业信贷 | `C227` | [B/A/O 案例](/best_practie/bao-cumcm-2020-c-credit) |

## Batch 2：2023-2025 MCM ABC

| 年份 | A：动态/机制 | B：优化/决策 | C：数据建模 |
|---|---|---|---|
| 2023 | `2309229` [Plant Community](/best_practie/bao-mcm-2023-a-plant-community) | `2315379` [Maasai Mara](/best_practie/bao-mcm-2023-b-maasai-mara) | `2307946` [Wordle](/best_practie/bao-mcm-2023-c-wordle) |
| 2024 | `2407093` [Lamprey](/best_practie/bao-mcm-2024-a-lamprey) | `2419984` [Submersible Search](/best_practie/bao-mcm-2024-b-submersible-search) | `2401298` [Tennis Momentum](/best_practie/bao-mcm-2024-c-tennis-momentum) |
| 2025 | `2501909` [Stair Wear](/best_practie/bao-mcm-2025-a-stair-wear) | `2504448` [Juneau Tourism](/best_practie/bao-mcm-2025-b-juneau-tourism) | `2505964` [Olympic Medals](/best_practie/bao-mcm-2025-c-olympic-medals) |

## 运行正式复现

运行正式 15 篇：

```bash
python tools/run_outstanding_reproductions.py --formal --keep-going
```

只运行 Batch 1：

```bash
python tools/run_outstanding_reproductions.py --batch 1 --keep-going
```

只运行 Batch 2：

```bash
python tools/run_outstanding_reproductions.py --batch 2 --keep-going
```

## 目录约定

仓库按赛题组织 outstanding，而不是按小问散放：

```text
mcm/outstanding_solutions/
cumcm/outstanding_solutions/
```

```text
outstanding_solutions/<year>/<code>/
  <paper_id>/
    solution.py
    result.json
    report.md
    artifacts/
```

同一道题可以有多篇获奖论文 PDF，但当前正式复现只认一篇主样例。其它 PDF 作为阅读和后续复现候选，放在赛题索引的 `BAO PDF` 列和 [PDF 下载清单](/reference/report-pdf-library) 中。

## 进入 outstanding 前的检查

一个赛题值得升级时，通常已经满足：

- 主线清楚：每一问知道自己继承和推进了什么。
- 数据源清楚：官方附件、题面参数、外部公开数据的边界写清楚。
- 模型链完整：变量、约束、目标、求解方法和解释能闭环。
- 结果稳定：至少有基本敏感性分析或参数扰动。
- 产物可用：图、表、JSON、Excel 或备忘录能支撑论文正文。

## Outstanding 要补什么

| 方向 | 要做的增强 |
|---|---|
| 整题叙事 | 把小问串成“问题背景 -> 主模型 -> 扩展 -> 验证 -> 决策建议”的论文结构。 |
| 算法 | 从启发式、贪心、固定权重升级到更可解释的优化、统计验证、仿真或组合模型。 |
| 鲁棒性 | 加入参数敏感性、交叉验证、留出评估、置信区间、极端情景或误差传播。 |
| 可视化 | 用一到三张关键图讲清主结果，不堆图，不让表格淹没结论。 |
| 审计 | 明确哪些结论来自官方数据，哪些来自假设，哪些只是情景分析。 |
