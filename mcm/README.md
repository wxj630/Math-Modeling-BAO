# MCM/ICM Tutorial Archive

本目录保存 MCM/ICM 教程使用的赛题索引、逐问 advanced 解法、通用 baseline 归档、运行结果、实验报告和轻量产物。教程站以“赛题”为入口，逐问内容只作为同一道题内部的递进链条。

## 当前覆盖

- 赛题：66 道。
- 逐问 advanced 实验：371 个。
- 通用 baseline 归档：371 个。
- 覆盖年份与题号：
  - 2015：A, B, C, D
  - 2016-2022：A, B, C, D, E, F
  - 2023：A, B, C, D, E, F, Y, Z
  - 2024-2025：A, B, C, D, E, F

## 本次补齐说明

- `2015-A` 和 `2015-B` 原先缺失，是因为本地早期归档只收到了 ICM 的 C/D PDF；COMAP 2015 官方页面中 MCM A/B 是网页正文题面，不是独立 PDF。现在已将 A/B 题面整理进索引，并补了逐问代码、结果、报告和 baseline。
- 早期抓取中出现过非标准别名，例如 `2019-P06`、`2022-P01`、`2023-C-Wordle`、`2023-C-Boats`、`2023-F-GreenGDP`。教程索引现在统一到官方/教学用 canonical id：`2019-F`、`2022-D`、`2023-C`、`2023-Y`、`2023-F`，原物理代码路径仍保留以复用已有实验结果。
- `2023-Y` 与 `2023-Z` 是用于保留同年额外归档题面的教学编号，避免和官方 A-F 主线冲突。

## 目录

| 路径 | 说明 |
|---|---|
| `problem_index.csv/json` | 赛题级索引，教程页的主入口数据源。 |
| `question_solution_index.csv/json` | 逐问 advanced 解法索引。 |
| `question_solutions/` | 每一问一个可运行 `solution.py`。 |
| `question_results/` | advanced 运行得到的 `result.json`。 |
| `question_reports/` | advanced 逐问实验报告。 |
| `question_artifacts/` | 实验表、图和辅助 JSON 等轻量产物。 |
| `generic_baselines/` | 每一问的通用 baseline 代码、结果、报告和实验表。 |
| `data_manifest.csv/json` | 官方题面与数据资产清单。 |
| `scripts/` | 索引构建、归档和验证脚本。 |

大体积官方原始材料与解压附件不进 Git；线上教程只保存阅读和复现所需的轻量内容。

## 常用命令

运行或重建 advanced 逐问索引：

```bash
.venv/bin/python mcm/scripts/run_question_all.py
.venv/bin/python mcm/scripts/verify_real_data_integration.py
```

重建通用 baseline：

```bash
.venv/bin/python mcm/scripts/archive_generic_baselines.py --all
.venv/bin/python mcm/scripts/verify_generic_baselines.py
```

重建教程赛题页：

```bash
.venv/bin/python tools/build_problem_pages.py
```

覆盖审计：

```bash
.venv/bin/python tools/audit_problem_coverage.py
```
