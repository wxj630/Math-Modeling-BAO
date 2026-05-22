# 2016-C q04：给 CFO Alpha Chiang 的两页以内信

## 题目原问
Include a letter to the Chief Financial Officer of the Goodgrant Foundation, Mr. Alpha Chiang, describing the optimal investment strategy, modeling approach, major results, and ROI concept.

## 适合模型
把官方数据来源、ROI 定义、推荐学校组合、年度预算和稳健性检查压缩成 CFO 可读的非技术信。对应模型：非技术政策报告、投资组合说明、ROI 解释。

## 数据与真实性
- 数据类型：official_comap_xlsx_zip。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted/2016/Problem Data- The Goodgrant Challenge`。
- 行数/记录数：{'scorecard': 7804, 'candidate_uids': 2977, 'dictionary': 1953}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 推荐资助组合
- 年预算：100000000 USD。
- 持续年数：5。
- 五年总预算：500000000 USD。
- 推荐学校数：10。

| UNITID | INSTNM | STABBR | annual_grant_usd | five_year_grant_usd | roi_score | expected_students_reached | rank_score |
|---|---|---|---|---|---|---|---|
| 110653 | University of California-Irvine | CA | 10000000.0 | 50000000.0 | 82.057599 | 10159.0 | 87.440319 |
| 110680 | University of California-San Diego | CA | 10000000.0 | 50000000.0 | 82.032235 | 10169.0 | 87.422564 |
| 110644 | University of California-Davis | CA | 10000000.0 | 50000000.0 | 79.77542 | 11380.0 | 85.842794 |
| 110662 | University of California-Los Angeles | CA | 10000000.0 | 50000000.0 | 79.370855 | 10389.0 | 85.559598 |
| 110635 | University of California-Berkeley | CA | 10000000.0 | 50000000.0 | 77.579122 | 8400.0 | 84.305385 |
| 110671 | University of California-Riverside | CA | 8900000.0 | 44500000.0 | 77.54864 | 10497.0 | 84.284048 |
| 134130 | University of Florida | FL | 10000000.0 | 50000000.0 | 75.065743 | 10373.0 | 82.54602 |
| 230038 | Brigham Young University-Provo | UT | 10000000.0 | 50000000.0 | 74.869283 | 9934.0 | 82.408498 |
| 110583 | California State University-Long Beach | CA | 10000000.0 | 50000000.0 | 74.281675 | 14407.0 | 81.997173 |
| 110705 | University of California-Santa Barbara | CA | 9200000.0 | 46000000.0 | 74.215957 | 7354.0 | 81.95117 |

### ROI 权重稳健性

| scenario | success_w | need_w | leverage_w | top20_overlap_with_base | top_school |
|---|---|---|---|---|---|
| base | 0.45 | 0.35 | 0.2 | 18 | University of California-Irvine |
| need_priority | 0.3 | 0.5 | 0.2 | 13 | California State University-Los Angeles |
| outcome_priority | 0.6 | 0.25 | 0.15 | 11 | University of California-San Diego |
| scale_priority | 0.35 | 0.25 | 0.4 | 17 | University of California-Irvine |

### CFO letter
Dear Mr. Alpha Chiang: We recommend that the Goodgrant Foundation invest the annual $100 million in a ranked portfolio of candidate institutions selected from the official IPEDS UID list and College Scorecard outcomes. Our ROI is not financial profit; it is a charitable return index combining student success, service to high-need students, and scale per grant dollar. The attached plan funds multiple institutions for five years, avoids duplicating purely prestige-driven giving, and should be re-estimated annually as new Scorecard and IPEDS data arrive.

## 模型限制
- 这是可复现的官方 Goodgrant Scorecard/IPEDS 附件实验；只使用 `ProblemCDATA.zip` 解压出的三份 Excel 和 IPEDS 变量 PDF，不使用随机造数。
- ROI 是慈善投资组合评分，不是严格因果效应；正式论文应补充学校项目执行计划、边际资金吸收能力、地区公平约束、重复资助排除和后续年度 Scorecard 更新。

## 运行方式
`.venv/bin/python mcm/question_solutions/2016/C/q04/solution.py`

## 输出
- `mcm/question_results/2016/C/q04/result.json`
- `mcm/question_reports/2016/C/q04/report.md`
- `mcm/question_artifacts/2016/C/q04`
