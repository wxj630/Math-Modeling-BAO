# 2021-C q04：新报告到来后的模型更新机制

## 题目原问
Address how you could update your model given additional new reports over time, and how often the updates should occur.

## 适合模型
把新增标签追加到官方 workbook 派生表，按周或新增高风险聚类触发重训；冻结训练截止日期并重新计算留出 AUC、AP、recall 与优先级稳定性。

## 数据与真实性
- 数据类型：official_comap_xlsx。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted/2021/Problem Data- Confirming the Buzz about Hornets/2021_MCM_Problem_C_Data`。
- 行数/记录数：{'2021MCMProblemC_DataSet.xlsx': 4440, '2021MCM_ProblemC_ Images_by_GlobalID.xlsx': 3305}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### Hornets 误判分类模型
- 模型：deterministic split + TF-IDF report text + image metadata + date/coordinate features + distance to training positive sightings + class-weighted logistic regression。
- 标注样本：2083；Positive ID：14；Negative ID：2069。
- 训练行数：1388；留出行数：695；留出阳性数：5。
- ROC-AUC：0.895362；Average Precision：0.802732。
- Positive precision/recall/F1 @0.5：0.4 / 0.8 / 0.533333。
- 重要警告：Only 14 official positive IDs are available, so interval uncertainty is large even when the holdout ranking is strong.

### 新报告到来后的更新机制
- 推荐频率：weekly。
- 触发条件：Retrain when new lab labels arrive or when five or more unresolved reports accumulate within 30 km of a known positive cluster.
- Append new official reports and image metadata to the two workbook-derived tables.
- Freeze previously used training labels for reproducibility, then add new Positive ID and Negative ID records.
- Recompute distance-to-positive and text/image features using only labels available at the update date.
- Run the deterministic holdout split and compare ROC-AUC, average precision, recall, and top-priority stability.
- Publish the updated priority list with model version, training cutoff date, and uncertainty warning.

## 模型限制
- 这是可复现的官方 Hornets Excel 附件实验；只使用 sightings workbook、image mapping workbook 和官方 PDF，不下载题面外部大图包，也不使用随机造数。
- Positive ID 只有 14 条，因此分类留出指标不应被解释成根除证明；正式论文应补充主动诱捕、搜巢、季节性监测和实验室复核记录。

## 运行方式
`.venv/bin/python mcm/question_solutions/2021/C/q04/solution.py`

## 输出
- `mcm/question_results/2021/C/q04/result.json`
- `mcm/question_reports/2021/C/q04/report.md`
- `mcm/question_artifacts/2021/C/q04`
