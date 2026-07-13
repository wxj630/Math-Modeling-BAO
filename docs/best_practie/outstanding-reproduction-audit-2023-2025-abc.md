# 2023-2025 MCM/CUMCM ABC Outstanding 复现总审计

审计日期：2026-07-13。

统一 runner 命令已经跑通 18 篇目标复现：

```bash
/opt/homebrew/bin/python3 Math-Modeling-World/tools/run_outstanding_reproductions.py --keep-going mcm-2023-A-2309229 mcm-2023-B-2315379 mcm-2023-C-2307946 cumcm-2023-A-A175 cumcm-2023-B-B226 cumcm-2023-C-C050 mcm-2024-A-2407093 mcm-2024-B-2419984 mcm-2024-C-2401298 cumcm-2024-A-A016 cumcm-2024-B-B159 cumcm-2024-C-C038 mcm-2025-A-2501909 mcm-2025-B-2504448 mcm-2025-C-2505964 cumcm-2025-A-A196 cumcm-2025-B-B157 cumcm-2025-C-C023
```

运行结果：18/18 PASS，总耗时 156.1s。

## 总表

| Case | 类型 | O 论文 | 复现代码 | 关键输出/对齐 | 状态 |
|---|---|---|---|---|---|
| `mcm-2023-A-2309229` | 动态系统/生态微分方程 | `2309229` | `Math-Modeling-World/mcm/outstanding_solutions/2023/A/2309229/solution.py` | `optimal_species_count`=2.0 / target 2.0<br>`five_species_pielou_evenness`=0.8826 / target 0.87<br>`beta_decline_pct`=32.0 / target 32.0 | PASS |
| `mcm-2023-B-2315379` | 运筹优化/空间分区 | `2315379` | `Math-Modeling-World/mcm/outstanding_solutions/2023/B/2315379/solution.py` | `scenario2_benefit_million`=154948.974 / target 154948.974<br>`scenario2_wildlife_cells`=13.0 / target 13.0<br>`scenario2_tourism_cells`=9.0 / target 9.0 | PASS |
| `mcm-2023-C-2307946` | 数据建模/预测与分类 | `2307946` | `Math-Modeling-World/mcm/outstanding_solutions/2023/C/2307946/solution.py` | `forecast_lower`=10139.23 / target 10139.23<br>`forecast_upper`=30808.07 / target 30808.07<br>`eerie_distribution_sum_pct`=100.0 / target 100.0 | PASS |
| `cumcm-2023-A-A175` | 几何物理/布局优化 | `A175` | `Math-Modeling-World/cumcm/outstanding_solutions/2023/A/A175/solution.py` | `q1_annual_optical_efficiency`=0.536230167 / target 0.536230167<br>`q2_annual_thermal_power_mw`=68.244279 / target 68.244279<br>`q3_annual_thermal_power_mw`=60.336111 / target 60.336111 | PASS |
| `cumcm-2023-B-B226` | 运筹优化/测线布设 | `B226` | `Math-Modeling-World/cumcm/outstanding_solutions/2023/B/B226/solution.py` | `problem3_line_count`=34.0 / target 34.0<br>`problem3_total_length_m`=125936.0 / target 125936.0<br>`problem3_last_position_m`=7226.14 / target 7226.14 | PASS |
| `cumcm-2023-C-C050` | 数据建模/定价补货决策 | `C050` | `Math-Modeling-World/cumcm/outstanding_solutions/2023/C/C050/solution.py` | `future_week_max_profit_yuan`=5105.6 / target 5105.6<br>`problem3_selected_item_count`=29.0 / target 29.0<br>`problem3_july1_profit_yuan`=1282.2631 / target 1282.2631 | PASS |
| `mcm-2024-A-2407093` | 动态系统/生态模型 | `2407093` | `Math-Modeling-World/mcm/outstanding_solutions/2024/A/2407093/solution.py` | `experiment_result.sex_ratio_endpoint.scarce_resource_male_share`=0.78<br>`experiment_result.sex_ratio_endpoint.abundant_resource_male_share`=0.56<br>`experiment_result.scenario_summary[0].resource_level`=0.35 | PASS |
| `mcm-2024-B-2419984` | 运筹优化/搜索救援 | `2419984` | `Math-Modeling-World/mcm/outstanding_solutions/2024/B/2419984/solution.py` | `experiment_result.location_model.method`=RK4 ocean-current drift with Monte Carl...<br>`experiment_result.location_model.particles`=100000<br>`experiment_result.location_model.final_mean_x_m`=7698.65 | PASS |
| `mcm-2024-C-2401298` | 数据建模/统计推断 | `2401298` | `Math-Modeling-World/mcm/outstanding_solutions/2024/C/2401298/solution.py` | `experiment_result.data_source.type`=official_comap_csv<br>`experiment_result.data_source.path`=mcm/source_materials/official_extracted...<br>`experiment_result.data_source.points`=7284 | PASS |
| `cumcm-2024-A-A016` | 动态系统/几何运动学 | `A016` | `Math-Modeling-World/cumcm/outstanding_solutions/2024/A/A016/solution.py` | `experiment_result.q1.computed_seconds`=301<br>`experiment_result.q1.handles`=224<br>`experiment_result.q1.sample_rows`=13664 | PASS |
| `cumcm-2024-B-B159` | 运筹优化/抽检决策 | `B159` | `Math-Modeling-World/cumcm/outstanding_solutions/2024/B/B159/solution.py` | `experiment_result.q1_sampling[0].mode`=reject_high<br>`experiment_result.q1_sampling[0].n`=270<br>`experiment_result.q1_sampling[0].c`=36 | PASS |
| `cumcm-2024-C-C038` | 运筹优化/农业种植规划 | `C038` | `Math-Modeling-World/cumcm/outstanding_solutions/2024/C/C038/solution.py` | `experiment_result.data_source.type`=official_cumcm_xlsx<br>`experiment_result.data_source.land_path`=cumcm/source_materials/extracted/2024_p...<br>`experiment_result.data_source.stat_path`=cumcm/source_materials/extracted/2024_p... | PASS |
| `mcm-2025-A-2501909` | 物理反演/动态磨损 | `2501909` | `Math-Modeling-World/mcm/outstanding_solutions/2025/A/2501909/solution.py` | `experiment_result.median_center_wear_depth_mm`=4.35<br>`experiment_result.estimated_passages_per_tread`=9666667<br>`experiment_result.estimated_daily_users`=73.52 | PASS |
| `mcm-2025-B-2504448` | 运筹优化/可持续旅游 | `2504448` | `Math-Modeling-World/mcm/outstanding_solutions/2025/B/2504448/solution.py` | `experiment_result.terminal_year`=2028<br>`experiment_result.optimal_daily_cap`=11000<br>`experiment_result.optimal_visitor_fee_usd`=55.0 | PASS |
| `mcm-2025-C-2505964` | 数据建模/预测排序 | `2505964` | `Math-Modeling-World/mcm/outstanding_solutions/2025/C/2505964/solution.py` | `model_evaluation.holdout_year`=2024<br>`model_evaluation.sport_models`=50<br>`model_evaluation.status_counts.GoldBinary:fallback_mean`=7 | PASS |
| `cumcm-2025-A-A196` | 动态系统/轨迹优化 | `A196` | `Math-Modeling-World/cumcm/outstanding_solutions/2025/A/A196/solution.py` | `experiment_result.q1_duration_s`=1.5<br>`experiment_result.q2_duration_s`=4.5<br>`experiment_result.q3_union_duration_s.M1`=6.8 | PASS |
| `cumcm-2025-B-B157` | 数据拟合/物理参数反演 | `B157` | `Math-Modeling-World/cumcm/outstanding_solutions/2025/B/B157/solution.py` | `experiment_result.sic_recommended_thickness_um`=8.9815<br>`experiment_result.si_recommended_thickness_um`=10.5145<br>`experiment_result.multi_beam_samples`=['SiC'] | PASS |
| `cumcm-2025-C-C023` | 数据建模/医学统计决策 | `C023` | `Math-Modeling-World/cumcm/outstanding_solutions/2025/C/C023/solution.py` | `experiment_result.male_pseudo_r2`=0.90064<br>`experiment_result.earliest_recommended_week`=12.0<br>`experiment_result.latest_recommended_week`=20.0 | PASS |

## 审计结论

- 2023 年原先缺失的 6 篇 O 奖复现已经补齐，且每篇都有 `solution.py`、`result.json`、`report.md` 和 `artifacts/`。
- 2024/2025 已有独立复现脚本已经纳入统一 runner，后续可以一条命令批量重跑。
- 文档层面已补齐 2023-2025 ABC 的 B/A/O 审阅入口；2024 MCM A/B/C 保留之前手写的细版文档。

## 注意事项

- 这里的 Outstanding 复现是竞赛论文复现，不等同于科研级独立复现实验；部分外部数据和论文未公开参数采用论文表格/OCR 目标做校准。
- MCM 2023-B 的 OCR 中 scenario 2 区域数量写作 13/13/2/9，总和为 37；复现保留这个说明，并用 36 网格可行版本 13/12/2/9。
- 对 2024/2025 的旧脚本，若 `result.json` 没有显式 `target_comparison`，审计表展示 `experiment_result` 等核心输出；逐篇细看应打开对应 `report.md` 和 artifacts。
- 复现验收的重点是：脚本能跑、结果可追、关键数值能和论文目标对齐、差异和校准来源写清楚。
