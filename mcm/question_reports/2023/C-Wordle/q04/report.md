# 2023-C-Wordle q04：Wordle 数据集的其他有趣特征

## 题目原问
List and describe some other interesting features of this data set.

## 适合模型
统计报告人数年度衰减、困难模式平均占比、重复字母与期望尝试次数差异、星期效应和关键相关系数。

## 数据与真实性
- 数据类型：official_comap_xlsx。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted/2023/Problem Data- Predicting Wordle Results`。
- 行数/记录数：{'records': 359}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

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

## 模型限制
- 这是可复现的官方 Wordle 附件数据基线实验，适合做论文骨架、结果表和图，不应把词属性相关性解释为严格因果。
- 官方数据来自 Twitter 报告样本，不等同于全体玩家；预测 2023-03-01 属于外推，正式论文应补充新日期真实结果或滚动更新检验。

## 运行方式
`.venv/bin/python mcm/question_solutions/2023/C-Wordle/q04/solution.py`

## 输出
- `mcm/question_results/2023/C-Wordle/q04/result.json`
- `mcm/question_reports/2023/C-Wordle/q04/report.md`
- `mcm/question_artifacts/2023/C-Wordle/q04`
