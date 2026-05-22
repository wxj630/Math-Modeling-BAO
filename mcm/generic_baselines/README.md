# MCM 通用基线归档

本目录保存 MCM 真实赛题工作流之上的最低可运行通用基线。它用于保留第一版建模脚手架和覆盖检查，不替代 `mcm/question_solutions` 中的真实数据工作流。

## 目录

- `solutions/`：每问一个可重新运行的通用基线 `solution.py`。
- `results/`：通用基线 `result.json`。
- `reports/`：通用基线 Markdown 报告。
- `artifacts/`：通用基线实验表。
- `generic_baseline_index.csv/json`：通用基线索引。

## 重新生成

```bash
/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python mcm/scripts/archive_generic_baselines.py --all
```

## 方法分布

- `linear_weighted_score_baseline`：68 问
- `report_outline_baseline`：58 问
- `network_path_baseline`：53 问
- `evidence_table_baseline`：51 问
- `resource_allocation_baseline`：47 问
- `first_order_dynamic_baseline`：42 问
- `linear_trend_forecast_baseline`：35 问
- `threshold_classification_baseline`：13 问
