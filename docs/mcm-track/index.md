# MCM/ICM 解法教程

MCM/ICM 赛道目前有两套核心归档：

| 层级 | 路径 | 说明 |
|---|---|---|
| Baseline | `mcm/generic_baselines/` | 每问最低可运行脚手架，用于模型选择和覆盖检查。 |
| Advanced | `mcm/question_solutions/` | 逐问真实数据或题面参数解法，配套结果、报告和 artifacts。 |
| Source materials | `mcm/source_materials/` 与 `docs/mcm-2015-2025/official_assets_extracted/` | 官方 PDF、附件、解压数据和清洗材料。 |

## 当前覆盖

`mcm/README.md` 记录了当前真实逐问实验覆盖情况：MCM/ICM 已整理为逐问 `solution.py`、`result.json`、`report.md` 和实验产物，并通过 `mcm/question_solution_index.csv` 建立索引。

教程站中的 [MCM/ICM 全量解法索引](./solution-index.md) 已把每个小问的 baseline report、advanced report 和 outstanding 预留位串在一起。

## 学习路径

1. 从 `mcm/generic_baselines/generic_baseline_index.csv` 选择一道题，读通用基线报告。
2. 到 `mcm/question_solution_index.csv` 找同一小问的 advanced 解法。
3. 对照 `source_type` 字段，确认它使用的是官方附件、官方 PDF 还是题面参数。
4. 运行单问 `solution.py`，检查 `question_results/` 和 `question_artifacts/` 是否更新。
5. 用 [Outstanding Solution](/tutorial/outstanding) 的标准判断还缺哪些论文级增强。

## 推荐案例

| 题目 | Baseline 入口 | Advanced 入口 | 学习重点 |
|---|---|---|---|
| 2024-C Momentum in Tennis | `mcm/generic_baselines/reports/2024/C/q01/report.md` | `mcm/question_reports/2024/C/q01/report.md` | 从关键词脚手架升级到逐分网球数据、势头指数和可视化。 |
| 2025-C Olympics | `mcm/generic_baselines/reports/2025/C/q01/report.md` | `mcm/question_reports/2025/C/q01/report.md` | 官方奥运 CSV、留出评估、预测区间和教练效应。 |
| 2025-D Baltimore Bridge | `mcm/generic_baselines/reports/2025/D/q01/report.md` | `mcm/question_reports/2025/D/q01/report.md` | 路网、公交站、AADT 数据和城市恢复决策。 |

详细拆解见 [MCM 2024-C 网球势头案例](/case-studies/mcm-2024-c)。
