# 2023-C-Wordle MCM-C: Predicting Wordle Results

> 这是一个赛题整体入口。先看整题主线，再进入 5 个小问的 baseline、advanced 和 outstanding 预留位。

## 整题主线

本题共 5 个小问。阅读时不要把小问拆成孤岛：`报告人数变化、3 月 1 日预测区间与困难模式比例` 通常给出主模型或数据入口，后续小问逐步加入动态、情景、评价、决策或论文表达要求，最后由 `给纽约时报 Puzzle Editor 的摘要信` 收束成整题结论。

## 赛题材料

| 项目 | 内容 |
|---|---|
| 赛题 | `2023-C-Wordle` |
| 小问数 | 5 |
| 推荐模型族 | linear_trend_forecast_baseline；report_outline_baseline；threshold_classification_baseline |
| 数据来源 | official_comap_xlsx |

## 小问递进链

### q01 报告人数变化、3 月 1 日预测区间与困难模式比例

**递进作用：** 建立整题主模型或数据入口，后续小问通常都继承这里的变量、指标或数据清洗结果。

**题意摘要：** The number of reported results vary daily. Develop a model to explain this variation and use your model to create a prediction interval for the number of reported results on March 1, 2023. Do any attributes of the word…

- Baseline：linear_trend_forecast_baseline；[report.md](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/reports/2023/C-Wordle/q01/report.md)；[solution.py](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/solutions/2023/C-Wordle/q01/solution.py)
- Advanced：official_comap_xlsx；[report.md](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_reports/2023/C-Wordle/q01/report.md)；[solution.py](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_solutions/2023/C-Wordle/q01/solution.py)；[result.json](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_results/2023/C-Wordle/q01/result.json)
- 实验产物：[artifact](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_artifacts/2023/C-Wordle/q01/reported_results_forecast.png)
- Outstanding：预留，用来补强鲁棒性、误差分析、论文图表和整题叙事。

### q02 EERIE 在 2023-03-01 的得分分布预测

**递进作用：** 把静态模型推进到时间演化或预测，形成递进分析。

**题意摘要：** For a given future solution word on a future date, develop a model that allows you to predict the associated percentages of (1, 2, 3, 4, 5, 6, X). Give a specific example for EERIE on March 1, 2023 and discuss uncertain…

- Baseline：linear_trend_forecast_baseline；[report.md](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/reports/2023/C-Wordle/q02/report.md)；[solution.py](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/solutions/2023/C-Wordle/q02/solution.py)
- Advanced：official_comap_xlsx；[report.md](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_reports/2023/C-Wordle/q02/report.md)；[solution.py](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_solutions/2023/C-Wordle/q02/solution.py)；[result.json](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_results/2023/C-Wordle/q02/result.json)
- 实验产物：[artifact](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_artifacts/2023/C-Wordle/q02/eerie_prediction.csv)
- Outstanding：预留，用来补强鲁棒性、误差分析、论文图表和整题叙事。

### q03 答案词难度分类与 EERIE 难度

**递进作用：** 在前问基础上加入新的约束、数据或评价口径，推进整题模型链。

**题意摘要：** Develop and summarize a model to classify solution words by difficulty. Identify attributes associated with each classification. Using your model, how difficult is EERIE? Discuss accuracy.

- Baseline：threshold_classification_baseline；[report.md](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/reports/2023/C-Wordle/q03/report.md)；[solution.py](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/solutions/2023/C-Wordle/q03/solution.py)
- Advanced：official_comap_xlsx；[report.md](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_reports/2023/C-Wordle/q03/report.md)；[solution.py](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_solutions/2023/C-Wordle/q03/solution.py)；[result.json](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_results/2023/C-Wordle/q03/result.json)
- 实验产物：[artifact](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_artifacts/2023/C-Wordle/q03/difficulty_by_word.csv)
- Outstanding：预留，用来补强鲁棒性、误差分析、论文图表和整题叙事。

### q04 Wordle 数据集的其他有趣特征

**递进作用：** 在前问基础上加入新的约束、数据或评价口径，推进整题模型链。

**题意摘要：** List and describe some other interesting features of this data set.

- Baseline：report_outline_baseline；[report.md](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/reports/2023/C-Wordle/q04/report.md)；[solution.py](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/solutions/2023/C-Wordle/q04/solution.py)
- Advanced：official_comap_xlsx；[report.md](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_reports/2023/C-Wordle/q04/report.md)；[solution.py](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_solutions/2023/C-Wordle/q04/solution.py)；[result.json](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_results/2023/C-Wordle/q04/result.json)
- 实验产物：[artifact](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_artifacts/2023/C-Wordle/q04/wordle_clean_data.csv)
- Outstanding：预留，用来补强鲁棒性、误差分析、论文图表和整题叙事。

### q05 给纽约时报 Puzzle Editor 的摘要信

**递进作用：** 把前面模型、实验和限制收束成论文或备忘录，是整题表达质量的出口。

**题意摘要：** Summarize your results in a one- to two-page letter to the Puzzle Editor of the New York Times.

- Baseline：report_outline_baseline；[report.md](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/reports/2023/C-Wordle/q05/report.md)；[solution.py](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/solutions/2023/C-Wordle/q05/solution.py)
- Advanced：official_comap_xlsx；[report.md](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_reports/2023/C-Wordle/q05/report.md)；[solution.py](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_solutions/2023/C-Wordle/q05/solution.py)；[result.json](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_results/2023/C-Wordle/q05/result.json)
- 实验产物：[artifact](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_artifacts/2023/C-Wordle/q05/eerie_distribution.png)
- Outstanding：预留，用来补强鲁棒性、误差分析、论文图表和整题叙事。

## 复现提示

本页不复制代码和实验结果；代码、结果和报告仍保存在仓库原目录。需要运行时，回到 [运行与复现](/reference/reproduce) 查看命令。

