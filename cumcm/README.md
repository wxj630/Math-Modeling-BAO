# CUMCM Tutorial Archive

本目录保存 CUMCM 教程使用的赛题索引、逐问 advanced 解法、通用 baseline 归档、运行结果、实验报告和轻量产物。教程站以“赛题”为入口，同一道题的各小问按递进关系组织。

## 当前覆盖

- 赛题：63 道。
- 逐问 advanced 实验：243 个。
- 通用 baseline 归档：243 个。
- 覆盖年份与题号：
  - 2010-2011：A, B, C, D
  - 2014-2018：A, B, C, D
  - 2019-2025：A, B, C, D, E

## 本次补齐说明

- CUMCM 2025 官方页面提供的是一个包含 A-E 题面和附件的压缩包。之前只看到少量文件，是因为压缩包里的中文文件名需要按 GBK 还原，普通解压路径把题面目录识别坏了。
- 现在 `2025-A` 到 `2025-E` 已全部进入 `problem_index.csv/json`、`question_solution_index.csv/json` 和教程页，并生成了逐问 advanced 代码、结果、报告、轻量产物与 generic baseline。
- 2022 不再只显示 B/D；当前索引包含 `2022-A` 到 `2022-E`。历史上只展示 B/D，是因为最早只有这两题做了较深的题意专门化，不代表官方题面缺失。

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
| `attachment_manifest.csv/json` | 官方附件扫描清单。 |
| `scripts/` | 附件扫描、索引构建、归档和验证脚本。 |

大体积官方原始材料、下载压缩包和解压附件不进 Git；线上教程只保存阅读和复现所需的轻量内容。

## 常用命令

运行或重建 advanced 逐问索引：

```bash
.venv/bin/python cumcm/scripts/run_question_all.py
.venv/bin/python cumcm/scripts/verify_question_outputs.py
```

扫描附件并重建通用 baseline：

```bash
.venv/bin/python cumcm/scripts/build_attachment_manifest.py
.venv/bin/python cumcm/scripts/archive_generic_baselines.py --all
.venv/bin/python cumcm/scripts/verify_generic_baselines.py
```

重建教程赛题页：

```bash
.venv/bin/python tools/build_problem_pages.py
```

覆盖审计：

```bash
.venv/bin/python tools/audit_problem_coverage.py
```
