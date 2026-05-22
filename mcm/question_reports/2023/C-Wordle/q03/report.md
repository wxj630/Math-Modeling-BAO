# 2023-C-Wordle q03：答案词难度分类与 EERIE 难度

## 题目原问
Develop and summarize a model to classify solution words by difficulty. Identify attributes associated with each classification. Using your model, how difficult is EERIE? Discuss accuracy.

## 适合模型
用 1-6/X 百分比分布计算期望尝试次数，并按训练集三分位划分 easy/medium/hard；再用随机森林分类器从日期和词属性预测难度类别。

## 数据与真实性
- 数据类型：official_comap_xlsx。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2023/Problem Data- Predicting Wordle Results`。
- 行数/记录数：{'records': 359}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

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

## 模型限制
- 这是可复现的官方 Wordle 附件数据基线实验，适合做论文骨架、结果表和图，不应把词属性相关性解释为严格因果。
- 官方数据来自 Twitter 报告样本，不等同于全体玩家；预测 2023-03-01 属于外推，正式论文应补充新日期真实结果或滚动更新检验。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2023/C-Wordle/q03/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2023/C-Wordle/q03/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2023/C-Wordle/q03/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2023/C-Wordle/q03`
