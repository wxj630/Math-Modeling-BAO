# 2021-A q01：多真菌地表凋落物分解模型

## 题目原问
Build a mathematical model that describes the breakdown of ground litter and woody fibers through fungal activity in the presence of multiple species of fungi.

## 适合模型
将题面指定的 growth rate 与 moisture tolerance 两个 trait 转成分解率、竞争权重和环境适配项，模拟固定 patch 的凋落物质量损失。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets`。
- 行数/记录数：{'official_parameters': 4}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

## 模型限制
- 这是可复现的官方题面参数真菌分解实验；COMAP 没有提供数值附件，因此只使用 PDF 中 growth rate、moisture tolerance、五类环境、环境波动和教材文章等题面约束。
- 真菌 trait、环境湿度和竞争参数是显式确定性情景输入，不是原始实验数据；正式论文应补充 PNAS 原文 isolate measurements、温湿度记录和凋落物质量损失校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2021/A/q01/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2021/A/q01/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2021/A/q01/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2021/A/q01`
