# 2022-B q06：解决水资源与水电竞争利益的标准

## 题目原问
Recommend the best means to resolve competing interests of water availability and electricity production. Explicitly state the criteria.

## 适合模型
列出不使用历史协议/政治权力、居民最低服务、Mexico/Gulf 保护、部门公平权重和水电替代触发的数学标准。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025/official_assets`。
- 行数/记录数：{'official_parameters': 6}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

## 模型限制
- 这是可复现的官方题面参数水库-水电分配实验；COMAP 没有提供水库运行、州需求或机组曲线附件，因此只使用 PDF 中 Powell/Mead 串联、五州、Mexico/Gulf flow、供需变化和不得依赖历史协议等题面约束。
- 水位、库容曲线、部门需水和水电系数是显式确定性场景输入，不是 BOR/电网实测数据；正式论文应补充官方水文、用水、电力、生态和跨境流量数据校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2022/B/q06/solution.py`

## 输出
- `mcm/question_results/2022/B/q06/result.json`
- `mcm/question_reports/2022/B/q06/report.md`
- `mcm/question_artifacts/2022/B/q06`
