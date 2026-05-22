# 2022-E q07：应用于多种森林

## 题目原问
Apply your models to various forests.

## 适合模型
将同一碳账户和社会决策模型应用于温带混交林、松木生产林、老龄针叶林和干旱内陆松林。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets`。
- 行数/记录数：{'official_parameters': 8}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

## 模型限制
- 这是可复现的官方题面参数森林固碳实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中 100 年评估、林产品生命周期、多价值决策和延长 10 年采伐间隔等题面约束。
- 森林样例、产品半衰期、决策权重和管理计划参数是显式确定性情景输入，不是地块清查数据；正式论文应补充当地森林库存、土壤碳、产品流向、扰动风险和社区调查校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2022/E/q07/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2022/E/q07/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2022/E/q07/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2022/E/q07`
