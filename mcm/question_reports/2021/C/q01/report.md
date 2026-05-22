# 2021-C q01：公众报告数据解释与扩散可预测性

## 题目原问
Address and discuss whether or not the spread of this pest over time can be predicted, and with what level of precision.

## 适合模型
读取官方 4440 条 sightings workbook，按 Positive ID 时间和经纬度构建阳性时间线与空间聚类；用题面 30km 新蜂后范围解释可预测精度边界。对应模型：空间统计、时间序列描述、风险地图。

## 数据与真实性
- 数据类型：official_comap_xlsx。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2021/Problem Data- Confirming the Buzz about Hornets/2021_MCM_Problem_C_Data`。
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

### 扩散与空间聚类
- 题面新蜂后范围：30 km。
- Positive ID 数：14。
- 首个阳性日期：2019-09-19；最后阳性日期：2020-10-01。
- 首个阳性到最远阳性距离：118.726431 km。
- 精度说明：Spread can be described as clustered public-report detections, but cannot be forecast with high spatial precision from 14 positives alone.

## 模型限制
- 这是可复现的官方 Hornets Excel 附件实验；只使用 sightings workbook、image mapping workbook 和官方 PDF，不下载题面外部大图包，也不使用随机造数。
- Positive ID 只有 14 条，因此分类留出指标不应被解释成根除证明；正式论文应补充主动诱捕、搜巢、季节性监测和实验室复核记录。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2021/C/q01/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2021/C/q01/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2021/C/q01/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2021/C/q01`
