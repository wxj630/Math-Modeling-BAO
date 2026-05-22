# 2024-F q07：对非法野生动物贸易的可测量影响

## 题目原问
In other words, what will the measurable impact on illegal wildlife trade be?

## 适合模型
以 no-project 5 年路径为反事实基线，计算第 5 年贸易额差值和 cumulative reduction percent。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted`。
- 行数/记录数：{'official_parameters': 5}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 五年影响预测
- 方法：compound no-project growth path compared with deterministic yearly intervention reductions under implementation maturity。
- 第 5 年无项目贸易额：31.4737 billion USD。
- 第 5 年项目贸易额：20.8262 billion USD。
- 第 5 年累计降低：33.83%。

| year | baseline_illegal_trade_value_billion_usd | projected_illegal_trade_value_billion_usd | cumulative_trade_reduction_pct |
|---|---|---|---|
| 1 | 27.4275 | 26.6609 | 2.795 |
| 2 | 28.3875 | 26.1991 | 7.709 |
| 3 | 29.381 | 25.0463 | 14.754 |
| 4 | 30.4094 | 23.2169 | 23.652 |
| 5 | 31.4737 | 20.8262 | 33.83 |

## 模型限制
- 这是可复现的官方题面参数非法野生动物贸易项目设计实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中 26.5B USD/year、第四大非法贸易和 5 年项目要求。
- 客户评分、干预减幅、预算和达标概率是显式确定性项目情景，不是执法数据库观测；正式论文应补充 seizure records、CITES/UNODC 路线资料、平台下架数据和地方伙伴调研校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2024/F/q07/solution.py`

## 输出
- `mcm/question_results/2024/F/q07/result.json`
- `mcm/question_reports/2024/F/q07/report.md`
- `mcm/question_artifacts/2024/F/q07`
