# 2023-C-Wordle q01：报告人数变化、3 月 1 日预测区间与困难模式比例

## 题目原问
The number of reported results vary daily. Develop a model to explain this variation and use your model to create a prediction interval for the number of reported results on March 1, 2023. Do any attributes of the word affect the percentage of scores reported that were played in Hard Mode?

## 适合模型
官方 Wordle Excel 清洗 + 对数报告人数 RidgeCV 时间趋势回归 + 词属性标准化回归解释困难模式比例 + 留出集误差评估。

## 数据与真实性
- 数据类型：official_comap_xlsx。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2023/Problem Data- Predicting Wordle Results`。
- 行数/记录数：{'records': 359}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 特征变量

- `days_since_start`
- `days_since_start_sq`
- `contest_number`
- `weekday`
- `is_weekend`
- `unique_letters`
- `repeated_letters`
- `max_letter_count`
- `vowel_count`
- `repeated_vowel_count`
- `rare_letter_count`
- `word_entropy`
- `letter_frequency_score`

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

## 模型限制
- 这是可复现的官方 Wordle 附件数据基线实验，适合做论文骨架、结果表和图，不应把词属性相关性解释为严格因果。
- 官方数据来自 Twitter 报告样本，不等同于全体玩家；预测 2023-03-01 属于外推，正式论文应补充新日期真实结果或滚动更新检验。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2023/C-Wordle/q01/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2023/C-Wordle/q01/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2023/C-Wordle/q01/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2023/C-Wordle/q01`
