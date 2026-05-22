# 2016-C q03：ROI 权重稳健性与未来更新

## 题目原问
Validate the model and discuss how the Goodgrant Foundation should assess 2016 donations and future philanthropic educational investments.

## 适合模型
比较 base、need_priority、outcome_priority、scale_priority 四组权重场景，统计 Top20 overlap 和首选学校变化，说明 ROI 不是因果估计而是年度可更新的慈善投资指标。对应模型：敏感性分析、稳健性检验、模型更新机制。

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

### ROI 权重稳健性

| scenario | success_w | need_w | leverage_w | top20_overlap_with_base | top_school |
|---|---|---|---|---|---|
| base | 0.45 | 0.35 | 0.2 | 18 | University of California-Irvine |
| need_priority | 0.3 | 0.5 | 0.2 | 13 | California State University-Los Angeles |
| outcome_priority | 0.6 | 0.25 | 0.15 | 11 | University of California-San Diego |
| scale_priority | 0.35 | 0.25 | 0.4 | 17 | University of California-Irvine |

## 模型限制
- 这是可复现的官方 Goodgrant Scorecard/IPEDS 附件实验；只使用 `ProblemCDATA.zip` 解压出的三份 Excel 和 IPEDS 变量 PDF，不使用随机造数。
- ROI 是慈善投资组合评分，不是严格因果效应；正式论文应补充学校项目执行计划、边际资金吸收能力、地区公平约束、重复资助排除和后续年度 Scorecard 更新。

## 运行方式
`.venv/bin/python mcm/question_solutions/2016/C/q03/solution.py`

## 输出
- `mcm/question_results/2016/C/q03/result.json`
- `mcm/question_reports/2016/C/q03/report.md`
- `mcm/question_artifacts/2016/C/q03`
