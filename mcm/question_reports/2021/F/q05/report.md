# 2021-F q05：政策组合和实施时间线

## 题目原问
Propose targeted policies and an implementation timeline that will support the migration from the current state to your proposed state.

## 适合模型
按年排布 need-based affordability compact、completion advising、funding floor、teaching quality feedback、research exchange recovery 和 renewal councils。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025/official_assets`。
- 行数/记录数：{'official_parameters': 3}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

## 模型限制
- 这是可复现的官方题面参数高等教育系统健康度实验；COMAP 没有提供国家高教 workbook，因此只使用 PDF 中 system health、sustainable system、多国比较、政策时间线和现实影响等题面约束。
- 国家健康维度分、政策增益和利益相关者影响是显式确定性规划输入，不是 UNESCO/OECD/国家教育财政或就业记录；正式论文应补充学费、债务、完成率、就业、科研、国际学生和财政稳定性数据校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2021/F/q05/solution.py`

## 输出
- `mcm/question_results/2021/F/q05/result.json`
- `mcm/question_reports/2021/F/q05/report.md`
- `mcm/question_artifacts/2021/F/q05`
