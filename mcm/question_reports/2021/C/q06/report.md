# 2021-C q06：给 WSDA 的两页备忘录

## 题目原问
Include a two-page memorandum that summarizes your results for the Washington State Department of Agriculture.

## 适合模型
将分类性能、优先级规则、30km 范围限制、每周更新流程和根除证据条件整理成面向 Washington State Department of Agriculture 的非技术 memo。

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

### 有限资源调查优先级
- 待排序 unresolved 报告：2357。
- 评分规则：0.62*classification probability + 0.18*within 30km queen range + image/specimen/date-response bonuses。

#### Top priority reports

| GlobalID | Lab Status | positive_probability | distance_to_training_positive_km | priority_score | image_count | has_specimen |
|---|---|---|---|---|---|---|
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

### 根除证据标准
- 当前数据评估：The 2020 workbook does not prove eradication: the last positive detection is too recent relative to the last submission date, and unresolved/unverified reports remain.
- 最后阳性到最后提交间隔：22 天。
- No Positive ID reports for at least two full active seasons after the last confirmed detection.
- High-priority unresolved reports inside the 30 km queen range are investigated and reclassified negative or unsupported.
- Targeted trap and nest-search records around prior positive clusters remain negative through fall dispersal.
- Public-report volume remains sufficient that absence of positives is informative, not merely a reporting gap.
- Model top-priority scores for new reports remain below a predeclared action threshold for a full season.

### WSDA 两页备忘录
To the Washington State Department of Agriculture: using only the official contest workbook and image-mapping workbook, we recommend a weekly triage cycle. Reports should be prioritized when the classifier assigns high Positive ID probability, the location lies within the 30 km queen-establishment range of prior positives, and the report includes a specimen, photo, or video. The current deterministic holdout ROC-AUC is 0.895362, but only 14 positives are available, so decisions should remain conservative. The data do not yet constitute eradication evidence; eradication would require multiple active seasons without positives, completed follow-up of high-priority unresolved reports, and negative targeted surveillance around prior clusters.

## 模型限制
- 这是可复现的官方 Hornets Excel 附件实验；只使用 sightings workbook、image mapping workbook 和官方 PDF，不下载题面外部大图包，也不使用随机造数。
- Positive ID 只有 14 条，因此分类留出指标不应被解释成根除证明；正式论文应补充主动诱捕、搜巢、季节性监测和实验室复核记录。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2021/C/q06/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2021/C/q06/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2021/C/q06/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2021/C/q06`
