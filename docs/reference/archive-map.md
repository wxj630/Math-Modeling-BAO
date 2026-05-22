# 归档路径说明

本页说明教程中频繁出现的路径。路径本身保留在仓库根目录，教程页负责解释它们的用法。

## MCM/ICM

| 路径 | 用途 |
|---|---|
| `mcm/problem_index.csv` | 题目总索引。 |
| `mcm/question_solution_index.csv` | 逐问 advanced 解法索引。 |
| `mcm/generic_baselines/generic_baseline_index.csv` | 逐问 baseline 解法索引。 |
| `mcm/question_solutions/<year>/<code>/qXX/solution.py` | 单问 advanced 代码。 |
| `mcm/question_results/<year>/<code>/qXX/result.json` | 单问 advanced 结果。 |
| `mcm/question_reports/<year>/<code>/qXX/report.md` | 单问 advanced 报告。 |
| `mcm/question_artifacts/<year>/<code>/qXX/` | 单问 advanced 表格、图片或辅助产物。 |
| `docs/mcm-2015-2025/official_assets_extracted/` | COMAP 官方附件解压材料，本地保留，默认不进入 Git。 |

## CUMCM

| 路径 | 用途 |
|---|---|
| `cumcm/problem_index.csv` | 题目总索引。 |
| `cumcm/question_solution_index.csv` | 逐问 advanced 解法索引。 |
| `cumcm/generic_baselines/generic_baseline_index.csv` | 逐问 baseline 解法索引。 |
| `cumcm/attachment_manifest.csv` | CUMCM 官方附件清单。 |
| `cumcm/question_solutions/<year>/<code>/qXX/solution.py` | 单问 advanced 代码。 |
| `cumcm/question_results/<year>/<code>/qXX/result.json` | 单问 advanced 结果。 |
| `cumcm/question_reports/<year>/<code>/qXX/report.md` | 单问 advanced 报告。 |
| `cumcm/question_artifacts/<year>/<code>/qXX/` | 单问 advanced 表格、图片、Excel 或辅助产物。 |

## 三层解法命名

| 名称 | 当前状态 |
|---|---|
| Baseline solution | 已归档在 `generic_baselines/`。 |
| Advanced solution | 已归档在 `question_solutions/`、`question_reports/` 等逐问目录。 |
| Outstanding solution | 教程已预留标准与位置，后续可按题新增。 |
