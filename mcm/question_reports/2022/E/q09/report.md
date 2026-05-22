# 2022-E q09：推荐森林管理计划及理由

## 题目原问
What forest management plan should be used for this forest? Why is this the best approach?

## 适合模型
用 100 年 CO2e、林产品需求、生物多样性敏感度和社会得分解释推荐方案。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025/official_assets`。
- 行数/记录数：{'official_parameters': 8}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

## 模型限制
- 这是可复现的官方题面参数森林固碳实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中 100 年评估、林产品生命周期、多价值决策和延长 10 年采伐间隔等题面约束。
- 森林样例、产品半衰期、决策权重和管理计划参数是显式确定性情景输入，不是地块清查数据；正式论文应补充当地森林库存、土壤碳、产品流向、扰动风险和社区调查校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2022/E/q09/solution.py`

## 输出
- `mcm/question_results/2022/E/q09/result.json`
- `mcm/question_reports/2022/E/q09/report.md`
- `mcm/question_artifacts/2022/E/q09`
