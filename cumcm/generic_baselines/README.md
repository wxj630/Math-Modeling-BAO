# CUMCM 通用基线归档

本目录保存题目专用化之前的第一版通用模型结果，避免在后续深化算法时把早期思路直接覆盖掉。

## 目录

- `solutions/`：每问一个可重新运行的通用基线 `solution.py`。
- `results/`：通用基线 `result.json`。
- `reports/`：通用基线 Markdown 报告。
- `artifacts/`：通用基线实验表和其它产物。
- `generic_baseline_index.csv/json`：通用基线索引。

## 重新生成

```bash
.venv/bin/python cumcm/scripts/archive_generic_baselines.py --all
```

## 方法分布

- `quadratic_least_squares`：67 问
- `linear_programming`：63 问
- `least_squares_geometry_fit`：33 问
- `linear_trend_forecast`：14 问
- `first_order_dynamic_simulation`：11 问
- `dijkstra_shortest_path`：10 问
- `logistic_regression_plus_kmeans`：9 问
- `std_weight_topsis`：8 问
- `binomial_sampling_design`：6 问
- `fft_feature_extraction`：2 问
