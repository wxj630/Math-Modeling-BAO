# 2023-C-Wordle q05：给纽约时报 Puzzle Editor 的摘要信

## 题目原问
Summarize your results in a one- to two-page letter to the Puzzle Editor of the New York Times.

## 适合模型
把报告人数预测、EERIE 分布、难度分类和数据集洞察压缩成编辑可读的决策信。

## 数据与真实性
- 数据类型：official_comap_xlsx。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted/2023/Problem Data- Predicting Wordle Results`。
- 行数/记录数：{'records': 359}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### Wordle 报告人数与困难模式模型
- 模型：log-linear RidgeCV for report counts; RidgeCV for hard-mode rate。
- 预测日期：2023-03-01，预测词：EERIE。
- 报告人数预测：23612。
- 80% 预测区间：[20365, 30713]。
- 报告人数留出 MAE/RMSE：2025.209 / 3677.285。
- 困难模式比例预测：0.137511；困难模式留出 MAE：0.036428。

#### 困难模式词属性影响

| feature | coefficient |
|---|---|
| days_since_start | 0.020859 |
| word_entropy | -0.000888 |
| unique_letters | -0.000797 |
| max_letter_count | -0.000773 |
| vowel_count | 0.000395 |
| rare_letter_count | -0.000391 |
| letter_frequency_score | -0.000355 |
| repeated_vowel_count | 0.000261 |

### EERIE 分布预测
- 模型：RandomForestRegressor on official percentage buckets, clipped and normalized to 100%。
- 预测对象：EERIE @ 2023-03-01。
- 留出平均桶 MAE：3.711 个百分点。

| bucket | predicted_percent | interval80 | holdout_mae |
|---|---|---|---|
| 1 try | 0.245 | [0.0, 0.59] | 0.578 |
| 2 tries | 7.01 | [2.614, 12.716] | 2.617 |
| 3 tries | 22.062 | [15.059, 28.971] | 6.811 |
| 4 tries | 30.668 | [24.759, 37.614] | 4.12 |
| 5 tries | 22.491 | [18.154, 27.633] | 4.758 |
| 6 tries | 11.839 | [7.173, 17.043] | 4.958 |
| 7 or more tries (X) | 5.685 | [0.997, 14.713] | 2.131 |

### Wordle 难度分类
- 模型：difficulty tertiles by expected attempts plus RandomForestClassifier from date and word attributes。
- easy/medium 阈值：4.033403；medium/hard 阈值：4.352357。
- 留出准确率：0.422222。
- EERIE 期望尝试次数：4.26407，难度类别：medium。

#### 重要特征

| feature | importance |
|---|---|
| letter_frequency_score | 0.187621 |
| days_since_start | 0.132151 |
| days_since_start_sq | 0.131605 |
| contest_number | 0.130505 |
| rare_letter_count | 0.092853 |
| weekday | 0.06415 |
| repeated_letters | 0.062474 |
| word_entropy | 0.054908 |
| max_letter_count | 0.053501 |
| unique_letters | 0.034078 |

#### 最难样本

| date | word | expected_attempts | difficulty_class |
|---|---|---|---|
| 2022-09-16 | PARER | 5.99 | hard |
| 2022-10-23 | MUMMY | 5.475248 | hard |
| 2022-08-02 | COYLY | 5.40404 | hard |
| 2022-04-19 | FOYER | 5.30303 | hard |
| 2022-12-26 | JUDGE | 5.232323 | hard |
| 2022-06-29 | GAWKY | 5.131313 | hard |
| 2022-02-19 | SWILL | 5.08 | hard |
| 2022-07-06 | FLUFF | 4.98 | hard |

### Wordle 数据集额外特征
- 前 30 天平均报告人数：243624.47。
- 后 30 天平均报告人数：22138.43。
- 报告人数变化率：-90.91%。
- 重复字母词数量：101；非重复字母词数量：258。
- 重复字母词平均期望尝试次数：4.435085；非重复字母词：4.098676。
- 困难模式平均占比：0.077634。

#### 星期摘要

| weekday | mean_reported_results | mean_expected_attempts |
|---|---|---|
| Mon | 90320.06 | 4.200015 |
| Tue | 92754.1 | 4.230888 |
| Wed | 93844.39 | 4.210129 |
| Thu | 91749.33 | 4.187878 |
| Fri | 91341.69 | 4.154165 |
| Sat | 88160.06 | 4.162801 |
| Sun | 88308.31 | 4.208731 |

### 给 Puzzle Editor 的摘要信
Dear Puzzle Editor,

Using the official 2022 Wordle result file, we modeled participation, score distribution, and word difficulty from observed Twitter-reported outcomes rather than from generated placeholder data. Report counts decline strongly over the year, so the March 1, 2023 forecast is driven mainly by time trend with word attributes as secondary corrections. For EERIE on 2023-03-01, the model predicts about 23612 reports with an 80% interval of [20365, 30713]. The most likely score bucket is 4 tries at 30.668%. Its expected-attempt difficulty is 4.26407, classified as medium. Repeated letters and lower unique-letter counts are associated with higher expected attempts, which is consistent with EERIE's repeated vowel structure.

The data also show a participation drop from the first 30 days to the last 30 days of -90.91%, and a stable concentration of outcomes around the middle attempt buckets. We recommend using the model as an operational forecasting baseline and re-estimating it monthly as new official Wordle outcomes become available.

Sincerely,
MCM modeling team

## 模型限制
- 这是可复现的官方 Wordle 附件数据基线实验，适合做论文骨架、结果表和图，不应把词属性相关性解释为严格因果。
- 官方数据来自 Twitter 报告样本，不等同于全体玩家；预测 2023-03-01 属于外推，正式论文应补充新日期真实结果或滚动更新检验。

## 运行方式
`.venv/bin/python mcm/question_solutions/2023/C-Wordle/q05/solution.py`

## 输出
- `mcm/question_results/2023/C-Wordle/q05/result.json`
- `mcm/question_reports/2023/C-Wordle/q05/report.md`
- `mcm/question_artifacts/2023/C-Wordle/q05`
