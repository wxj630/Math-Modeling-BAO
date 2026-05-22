# 2016-C q01：Goodgrant 慈善 ROI 定义与候选学校评分

## 题目原问
Develop a model to determine an optimal investment strategy based on each candidate school's demonstrated potential for effective use of private funding and an estimated philanthropic ROI.

## 适合模型
读取官方 ProblemCDATA.zip 中 Scorecard 主表、候选 IPEDS UID 表和数据字典，筛选 current operating、predominant degree 3/4、UGDS>500 的候选学校；构造 student_success、grant_need、leverage 三类指数和 charitable ROI。对应模型：多指标综合评价、标准化加权评分、教育投资 ROI。

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

## 模型限制
- 这是可复现的官方 Goodgrant Scorecard/IPEDS 附件实验；只使用 `ProblemCDATA.zip` 解压出的三份 Excel 和 IPEDS 变量 PDF，不使用随机造数。
- ROI 是慈善投资组合评分，不是严格因果效应；正式论文应补充学校项目执行计划、边际资金吸收能力、地区公平约束、重复资助排除和后续年度 Scorecard 更新。

## 运行方式
`.venv/bin/python mcm/question_solutions/2016/C/q01/solution.py`

## 输出
- `mcm/question_results/2016/C/q01/result.json`
- `mcm/question_reports/2016/C/q01/report.md`
- `mcm/question_artifacts/2016/C/q01`
