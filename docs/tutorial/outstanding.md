# Outstanding Solution

Outstanding solution 是按“整道赛题”打磨出来的论文级版本。它不是把每个小问单独加长，而是选择一篇官方获奖论文，复现其中可验证的模型链、代码、实验结果和论文级分析。

## 已落地样例

当前已经为 2025 年可验证题建立了“一题一篇”的第一批 outstanding 复现。MCM/ICM 与 CUMCM 的每道题都选一篇和当前 baseline/advanced 最接近的官方获奖论文；其中 MCM 2025-C 是完整运动员级复现，其余题先使用当前已验证的 advanced/real solution 作为计算核，对齐获奖论文模型链。

| 赛题 | 论文编号 | 论文题名 | 复现状态 |
|---|---|---|---|
| MCM/ICM 2025-A | `2501909` | `Stair Wear: Traces of History` | WVM/WDM paper-guided reproduction |
| MCM/ICM 2025-B | `2504448` | `Sustainable Tourism Management in Juneau` | multi-objective tourism paper-guided reproduction |
| MCM/ICM 2025-C | `2505964` | `2028 Olympic Medal Predictions Based on Random Forest Model` | athlete-level RF + Monte Carlo reproduction |
| MCM/ICM 2025-D | `2507692` | `Optimizing Baltimore Multi-Layer Traffic Network Model Based on Graph Theory & Clustering Algorithm` | multilayer traffic network paper-guided reproduction |
| MCM/ICM 2025-E | `2508861` | `Symphony of Eco-Agriculture` | ecosystem dynamics paper-guided reproduction |
| MCM/ICM 2025-F | `2517199` | `Data-Driven Policy Effectiveness Evaluation` | cyber policy data-panel paper-guided reproduction |
| CUMCM 2025-A | `A196` | `多情形下无人机烟幕遮蔽策略的建模与优化研究` | smoke-screen kinematics paper-guided reproduction |
| CUMCM 2025-B | `B157` | `碳化硅外延层厚度的双光束和多光束干涉法测量研究` | interference thickness paper-guided reproduction |
| CUMCM 2025-C | `C023` | `基于混合效应模型的NIPT时点优化与胎儿异常判定` | NIPT mixed-effects paper-guided reproduction |
| CUMCM 2025-D | `D037` | `矿井突水水流漫延模型与逃生方案问题` | mine water-spread graph paper-guided reproduction |
| CUMCM 2025-E | `E030` | `基于姿态识别的AI辅助智能体测研究` | pose recognition paper-guided reproduction |

2025-C 复现了论文的核心思路：先在运动员/团队参赛条目上构造历史能力特征，再按运动训练随机森林分类器，最后通过 Monte Carlo 把单项概率分配成国家奖牌榜；同时补充 USA Swimming、CHN Table Tennis 的项目数量弹性和 Great Coach 候选分析。

所有 2025 年可验证题的论文选择记录在 [Outstanding 覆盖清单](/reference/outstanding-coverage-audit)。尚未复现的题目只进入清单，不会在赛题页里显示成已完成版本。

MCM/ICM 运行命令：

```bash
python mcm/outstanding_solutions/2025/A/2501909/solution.py
python mcm/outstanding_solutions/2025/B/2504448/solution.py
python mcm/outstanding_solutions/2025/C/2505964/solution.py
python mcm/outstanding_solutions/2025/D/2507692/solution.py
python mcm/outstanding_solutions/2025/E/2508861/solution.py
python mcm/outstanding_solutions/2025/F/2517199/solution.py
```

CUMCM 运行命令：

```bash
python cumcm/outstanding_solutions/2025/A/A196/solution.py
python cumcm/outstanding_solutions/2025/B/B157/solution.py
python cumcm/outstanding_solutions/2025/C/C023/solution.py
python cumcm/outstanding_solutions/2025/D/D037/solution.py
python cumcm/outstanding_solutions/2025/E/E030/solution.py
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

同一道题可以有多篇获奖论文复现，先用 `outstanding_solution_index.csv` 决定教程页展示哪一篇作为当前主样例。

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

## 教程中的预留位

没有复现的赛题页仍会保留 outstanding 位置。补写某道题时，优先选择 A/B/C 这类可验证题型：微分方程、运筹优化、数据建模、仿真或可计算决策问题。社会科学论述型题目可以等可验证样例足够多之后再处理。
