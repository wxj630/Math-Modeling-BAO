# 2016-C q02：1 亿美元年度预算的优先资助组合

## 题目原问
Identify the schools, the investment amount per school, and the duration the money should be provided to maximize the likelihood of a strong positive effect on student performance.

## 适合模型
按 rank_score 排序，在 annual budget 100,000,000 USD 和 5 年持续资助下贪心选择学校；每校年度 grant 在 2M-10M 之间，随官方 UGDS 规模调整。对应模型：预算约束组合选择、背包思想、投资组合排序。

## 数据与真实性
- 数据类型：official_comap_xlsx_zip。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted/2016/Problem Data- The Goodgrant Challenge`。
- 行数/记录数：{'scorecard': 7804, 'candidate_uids': 2977, 'dictionary': 1953}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### Goodgrant ROI 模型
- 定义：Charitable ROI = weighted student-success potential, demonstrated need, and scalable leverage per grant dollar. It is appropriate for philanthropy because it values Pell-serving institutions, completion/retention/repayment/earnings outcomes, and students reached rather than private profit.
- 过滤规则：Official candidate UID list joined to Scorecard, current operating schools, predominant degree 3 or 4, UGDS > 500.
- 过滤后候选行：1454；已评分行：1454。
- 权重：{'student_success_index': 0.45, 'grant_need_index': 0.35, 'leverage_index': 0.2, 'portfolio_rank_blend': '70% ROI score + 30% ROI units per million'}

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

## 模型限制
- 这是可复现的官方 Goodgrant Scorecard/IPEDS 附件实验；只使用 `ProblemCDATA.zip` 解压出的三份 Excel 和 IPEDS 变量 PDF，不使用随机造数。
- ROI 是慈善投资组合评分，不是严格因果效应；正式论文应补充学校项目执行计划、边际资金吸收能力、地区公平约束、重复资助排除和后续年度 Scorecard 更新。

## 运行方式
`.venv/bin/python mcm/question_solutions/2016/C/q02/solution.py`

## 输出
- `mcm/question_results/2016/C/q02/result.json`
- `mcm/question_reports/2016/C/q02/report.md`
- `mcm/question_artifacts/2016/C/q02`
