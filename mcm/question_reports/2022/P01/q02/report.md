# 2022-P01 q02：优化 D&A 能力的系统变更建议

## 题目原问
After ICM Corporation uses your model to determine its current D&A maturity level, demonstrate how it could recommend changes to maximize data asset potential.

## 适合模型
按最大加权缺口生成 0-24 个月路线图，包括数据 owner、catalog/lineage、质量流程、客户仪表盘和模型监控。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025/official_assets`。
- 行数/记录数：{'official_parameters': 4}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

## 模型限制
- 这是可复现的官方题面参数 D&A 成熟度实验；题面明确 ICM Corporation 不能分享内部人员、技术、流程或数据细节，因此只使用 people/technology/process、海港、卡车公司迁移和客户信等题面约束。
- KPI 当前分、目标分和路线图收益是显式 rubric 输入，不是 ICM 内部审计记录；正式咨询应补充访谈、系统日志、数据目录覆盖率、质量事件和客户满意度调查校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2022/P01/q02/solution.py`

## 输出
- `mcm/question_results/2022/P01/q02/result.json`
- `mcm/question_reports/2022/P01/q02/report.md`
- `mcm/question_artifacts/2022/P01/q02`
