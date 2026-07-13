# 2025 CUMCM-C Outstanding 复现：C023 NIPT 混合效应模型

## 复现定位
- 论文：C023，基于混合效应模型的NIPT时点优化与胎儿异常判定。
- 本脚本直接读取男女胎检测数据，重建 logit(FF) 混合效应近似、BMI 风险分组、检测误差分析和女胎异常判定。

## 男胎模型
- 样本行数：1082，孕妇数：267。
- pseudo R2：0.90064，残差 sigma：0.47707。

## BMI 分组时点
| BMI range | n | week | pass prob | risk |
|---|---:|---:|---:|---:|
| 20.7-30.52 | 67 | 12.0 | 0.7645 | 2.2349 |
| 30.65-32.34 | 67 | 12.0 | 0.7339 | 2.3831 |
| 32.35-34.37 | 66 | 12.0 | 0.7493 | 2.303 |
| 34.43-46.88 | 67 | 20.0 | 0.809 | 3.2937 |

## 女胎异常判定
- 方法：random forest classifier on chromosome Z scores, GC/read-quality features, X concentration, and BMI; fallback to Z-score rule if positives are too sparse
- LOO accuracy：0.8659，F1：0.3721。

## 相比 Advanced 的提升
从逐问统计摘要升级为 O 奖论文式闭环：用官方重复检测数据拟合 logit 胎儿浓度模型，显式估计个体随机效应，按 BMI 最小化达标风险，并用女胎多指标模型输出异常概率。

## 输出产物
- `male_model_coefficients`: `cumcm/outstanding_solutions/2025/C/C023/artifacts/male_model_coefficients.csv`
- `bmi_nipt_timing`: `cumcm/outstanding_solutions/2025/C/C023/artifacts/bmi_nipt_timing.csv`
- `female_abnormal_scores`: `cumcm/outstanding_solutions/2025/C/C023/artifacts/female_abnormal_scores.csv`
- `correlations`: `cumcm/outstanding_solutions/2025/C/C023/artifacts/male_y_correlations.csv`
- `nipt_timing_plot`: `cumcm/outstanding_solutions/2025/C/C023/artifacts/nipt_timing_plot.png`
- `female_feature_importance_plot`: `cumcm/outstanding_solutions/2025/C/C023/artifacts/female_feature_importance.png`
