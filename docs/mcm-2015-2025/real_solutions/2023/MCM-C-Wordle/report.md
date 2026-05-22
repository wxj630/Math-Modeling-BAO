# 2023 MCM-C Wordle 真实数据实验报告

## 数据来源
- 官方附件：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2023/Problem Data- Predicting Wordle Results/2023_MCM_Problem_C_Data.xlsx`。
- 清洗后记录数：359，日期范围：2022-01-07 到 2022-12-31。
- 读取字段包括日期、比赛编号、答案词、报告人数、困难模式人数和 1/2/3/4/5/6/X 百分比分布。

## Q1 报告人数变化与困难模式比例
- 模型：对报告人数取对数后做 RidgeCV 回归，特征包含时间趋势、星期、比赛编号和答案词字母属性。
- 最近 45 天留出检验 MAE/RMSE：2025.209 / 3677.285。
- 对 2023-03-01 的报告人数预测：23612，80% 区间 [20365, 30713]。
- EERIE 的困难模式比例预测：0.137511；困难模式比例留出 MAE：0.036428。
- 词属性影响用标准化 Ridge 系数排序，绝对值越大代表关联更强。

## Q2 EERIE 分布预测
- 模型：RandomForestRegressor on official percentage buckets, clipped and normalized to 100%。
- 留出集平均桶 MAE：3.711 个百分点。

| bucket | predicted_percent | interval80 | holdout_mae_pp |
|---|---:|---|---:|
| 1 try | 0.245 | [0.0, 0.59] | 0.578 |
| 2 tries | 7.01 | [2.614, 12.716] | 2.617 |
| 3 tries | 22.062 | [15.059, 28.971] | 6.811 |
| 4 tries | 30.668 | [24.759, 37.614] | 4.12 |
| 5 tries | 22.491 | [18.154, 27.633] | 4.758 |
| 6 tries | 11.839 | [7.173, 17.043] | 4.958 |
| 7 or more tries (X) | 5.685 | [0.997, 14.713] | 2.131 |

## Q3 难度分类
- 难度指标：用 1/2/3/4/5/6/X 分布计算期望尝试次数，其中 X 按第 7 档处理。
- easy/medium 阈值：4.033403；medium/hard 阈值：4.352357。
- 最近 45 天分类留出准确率：0.422222。
- EERIE 按预测分布得到期望尝试次数 4.26407，分类为 `medium`。

## Q4 数据集其他特征
- 前 30 天平均报告人数：243624.47；后 30 天平均报告人数：22138.43；变化 -90.91%。
- 重复字母词平均期望尝试次数：4.435085；非重复字母词：4.098676。
- 困难模式平均占比：0.077634。

## 给纽约时报 Puzzle Editor 的摘要信
Dear Puzzle Editor,

Using the official 2022 Wordle result file, we modeled participation, score distribution, and word difficulty from observed Twitter-reported outcomes rather than from generated placeholder data. Report counts decline strongly over the year, so the March 1, 2023 forecast is driven mainly by time trend with word attributes as secondary corrections. For EERIE on 2023-03-01, the model predicts about 23612 reports with an 80% interval of [20365, 30713]. The most likely score bucket is 4 tries at 30.668%. Its expected-attempt difficulty is 4.26407, classified as medium. Repeated letters and lower unique-letter counts are associated with higher expected attempts, which is consistent with EERIE's repeated vowel structure.

The data also show a participation drop from the first 30 days to the last 30 days of -90.91%, and a stable concentration of outcomes around the middle attempt buckets. We recommend using the model as an operational forecasting baseline and re-estimating it monthly as new official Wordle outcomes become available.

Sincerely,
MCM modeling team

## 输出文件
- `result.json`：/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/real_solutions/2023/MCM-C-Wordle/result.json
- `wordle_clean_data.csv`：/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/real_solutions/2023/MCM-C-Wordle/artifacts/wordle_clean_data.csv
- `eerie_prediction.csv`：/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/real_solutions/2023/MCM-C-Wordle/artifacts/eerie_prediction.csv
- `reported_results_forecast.png`：/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/real_solutions/2023/MCM-C-Wordle/artifacts/reported_results_forecast.png
- `eerie_distribution.png`：/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/real_solutions/2023/MCM-C-Wordle/artifacts/eerie_distribution.png
