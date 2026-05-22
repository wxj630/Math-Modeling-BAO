# CUMCM 解法教程

CUMCM 赛道保留了经典数模题的题面、附件、逐问实验和通用基线。它特别适合学习中文赛题中常见的“附件数据解析、约束建模、输出 Excel 模板、论文表格生成”。

| 层级 | 路径 | 说明 |
|---|---|---|
| Baseline | `cumcm/generic_baselines/` | 题目专用化之前的第一版通用模型。 |
| Advanced | `cumcm/question_solutions/` | 逐问专用解法，读取附件或题面参数并生成结果。 |
| Attachments | `cumcm/source_materials/` 与 `cumcm/attachment_manifest.csv` | 官方附件、重抽取材料和附件清单。 |

## 当前覆盖

`cumcm/README.md` 记录了逐问层、通用基线和附件接入状态。当前逐问层已覆盖 196 个问题，每一问都有独立 Python 入口、`result.json`、`report.md` 和 `experiment_table.csv`。

教程站中的 [CUMCM 全量解法索引](./solution-index.md) 已把每个小问的 baseline report、advanced report 和 outstanding 预留位串在一起。

## 学习路径

1. 从 `cumcm/problem_index.csv` 或 `cumcm/question_solution_index.csv` 选择一道题。
2. 先看 `cumcm/generic_baselines/reports/.../report.md`，理解第一版模型为什么只能算 baseline。
3. 再看 `cumcm/question_reports/.../report.md`，关注它如何接入附件、输出模板和题目约束。
4. 运行对应 `solution.py`，检查是否生成题目要求的 `result*.xlsx`、图表或实验表。
5. 用 outstanding 标准补敏感性、误差分析、论文叙事和可视化。

## 推荐案例

| 题目 | Baseline 入口 | Advanced 入口 | 学习重点 |
|---|---|---|---|
| 2024-C 农作物种植策略 | `cumcm/generic_baselines/reports/2024/C/q01/report.md` | `cumcm/question_reports/2024/C/q01/report.md` | Excel 附件解析、轮作约束、滞销/折价收益和提交模板。 |
| 2024-A 板凳龙 | `cumcm/generic_baselines/reports/2024/A/q01/report.md` | `cumcm/question_reports/2024/A/q01/report.md` | 螺线运动学、碰撞扫描和速度约束。 |
| 2024-B 生产检测 | `cumcm/generic_baselines/reports/2024/B/q01/report.md` | `cumcm/question_reports/2024/B/q01/report.md` | 抽样检测、装配决策、拆解和鲁棒重算。 |

详细拆解见 [CUMCM 2024-C 农作物规划案例](/case-studies/cumcm-2024-c)。
