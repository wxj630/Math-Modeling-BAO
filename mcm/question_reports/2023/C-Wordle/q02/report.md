# 2023-C-Wordle q02：EERIE 在 2023-03-01 的得分分布预测

## 题目原问
For a given future solution word on a future date, develop a model that allows you to predict the associated percentages of (1, 2, 3, 4, 5, 6, X). Give a specific example for EERIE on March 1, 2023 and discuss uncertainty.

## 适合模型
用官方历史分布训练多输出随机森林回归，预测 1/2/3/4/5/6/X 七个百分比桶，非负裁剪并归一化到 100%，用树分布和留出误差给出不确定性。

## 数据与真实性
- 数据类型：official_comap_xlsx。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2023/Problem Data- Predicting Wordle Results`。
- 行数/记录数：{'records': 359}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

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

## 模型限制
- 这是可复现的官方 Wordle 附件数据基线实验，适合做论文骨架、结果表和图，不应把词属性相关性解释为严格因果。
- 官方数据来自 Twitter 报告样本，不等同于全体玩家；预测 2023-03-01 属于外推，正式论文应补充新日期真实结果或滚动更新检验。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2023/C-Wordle/q02/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2023/C-Wordle/q02/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2023/C-Wordle/q02/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2023/C-Wordle/q02`
