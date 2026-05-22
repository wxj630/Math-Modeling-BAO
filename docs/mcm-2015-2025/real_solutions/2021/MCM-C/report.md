# 2021 MCM-C Confirming the Buzz about Hornets

## 数据与真实性
- 官方题面：`docs/mcm-2015-2025/official_assets_extracted/2021/Confirming the Buzz about Hornets.pdf`。
- 官方附件：`docs/mcm-2015-2025/official_assets_extracted/2021/Problem Data- Confirming the Buzz about Hornets/2021_MCM_Problem_C_Data/2021MCMProblemC_DataSet.xlsx` 与 `docs/mcm-2015-2025/official_assets_extracted/2021/Problem Data- Confirming the Buzz about Hornets/2021_MCM_Problem_C_Data/2021MCM_ProblemC_ Images_by_GlobalID.xlsx`。
- 背景资料：`docs/mcm-2015-2025/official_assets_extracted/2021/Problem Data- Confirming the Buzz about Hornets/2021_MCM_Problem_C_Data/2021MCM_ProblemC_Vespamandarina.pdf`。
- 只使用题面提供的两个 Excel 和 PDF；不使用随机造数、不使用外部图片下载、不使用额外生态数据。
- 行数：`{'2021MCMProblemC_DataSet.xlsx': 4440, '2021MCM_ProblemC_ Images_by_GlobalID.xlsx': 3305}`。

## 建模与求解
- 数据解释：清洗检测日期、提交日期、经纬度、报告文本、实验室状态和图片/视频映射。
- 误判分类：用 Positive ID / Negative ID 训练确定性留出分类器，特征包括坐标、月份、提交延迟、图片/视频、文本 TF-IDF、是否提到标本/蜂群损失，以及距训练阳性点的距离。
- 资源优先级：对 Unprocessed / Unverified 报告按分类概率、30km 新蜂后范围、图片/标本证据和响应时效排序。
- 更新机制：每周或新标签累计后重训，并保留训练截止日期和留出评估。
- 根除证据：把无阳性持续时间、30km 范围内高优先级报告处理、主动监测阴性和公众报告量作为联合标准。

## 关键结果
- Positive ID：14；Negative ID：2069。
- 留出 ROC-AUC：0.895362；Average Precision：0.802732。
- 待排序 unresolved 报告：2357。
- 首个阳性到最远阳性距离：118.726431 km。

### Top priority reports
| GlobalID | Lab Status | positive_probability | distance_km | priority_score | image_count | has_specimen |
|---|---|---:|---:|---:|---:|---:|
| {BD39DA58-3EAF-4B94-8E8B-0FC2FC7F4919} | Unverified | 0.967214 | 2.24119 | 0.899672 | 0.0 | 1 |
| {D4F58ECB-63F3-4D4B-968D-34B635F47A29} | Unverified | 0.965523 | 12.657099 | 0.871958 | 0.0 | 1 |
| {0CAC26D0-208E-4CAF-8894-00687E0B7124} | Unverified | 0.968491 | 9.722486 | 0.860677 | 0.0 | 1 |
| {D6EC52B4-3638-4B8E-854B-9A707E9E1755} | Unverified | 0.881427 | 29.992852 | 0.846485 | 0.0 | 1 |
| {BE7A4DBE-2249-4C25-AC31-6194ADB0637E} | Unverified | 0.994529 | 10.38441 | 0.836608 | 0.0 | 0 |
| {C50A62CD-47D4-417B-9E52-9818C1CFECAD} | Unverified | 0.981134 | 0.193825 | 0.828303 | 0.0 | 0 |
| {69559F23-FD0B-403C-9439-69575177396A} | Unverified | 0.970532 | 3.865544 | 0.82173 | 0.0 | 0 |
| {AAA0468B-170C-4FD2-A07E-E25BB936066B} | Unverified | 0.969568 | 12.986628 | 0.821132 | 0.0 | 0 |
| {653837DF-1C5B-43DE-8326-F85F5AFF142E} | Unverified | 0.961239 | 5.689481 | 0.815968 | 0.0 | 0 |
| {8D023A92-A0ED-4CD9-90DA-F65586B38092} | Unverified | 0.828571 | 12.668765 | 0.813714 | 1.0 | 0 |

## WSDA two-page memorandum
To the Washington State Department of Agriculture: using only the official contest workbook and image-mapping workbook, we recommend a weekly triage cycle. Reports should be prioritized when the classifier assigns high Positive ID probability, the location lies within the 30 km queen-establishment range of prior positives, and the report includes a specimen, photo, or video. The current deterministic holdout ROC-AUC is 0.895362, but only 14 positives are available, so decisions should remain conservative. The data do not yet constitute eradication evidence; eradication would require multiple active seasons without positives, completed follow-up of high-priority unresolved reports, and negative targeted surveillance around prior clusters.

## 输出文件
- `artifacts/clean_sightings.csv`
- `artifacts/classification_holdout_predictions.csv`
- `artifacts/priority_reports.csv`
- `artifacts/positive_sightings.csv`
- `artifacts/spread_timeline.csv`
- `artifacts/hornet_spread_map.png`
- `artifacts/priority_reports.png`
