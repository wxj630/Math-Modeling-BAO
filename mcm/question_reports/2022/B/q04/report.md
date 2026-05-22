# 2022-B q04：Mexico 权利与加利福尼亚湾入海流量

## 题目原问
Mexico has claims on residual water. Address Mexico's rights and how much water should flow into the Gulf of California after allocations.

## 适合模型
把 Mexico 最小流和 Gulf 生态流写成显式约束，在州部门分配前保护，除非居民最低服务触发紧急重算。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets`。
- 行数/记录数：{'official_parameters': 6}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

## 模型限制
- 这是可复现的官方题面参数水库-水电分配实验；COMAP 没有提供水库运行、州需求或机组曲线附件，因此只使用 PDF 中 Powell/Mead 串联、五州、Mexico/Gulf flow、供需变化和不得依赖历史协议等题面约束。
- 水位、库容曲线、部门需水和水电系数是显式确定性场景输入，不是 BOR/电网实测数据；正式论文应补充官方水文、用水、电力、生态和跨境流量数据校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2022/B/q04/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2022/B/q04/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2022/B/q04/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2022/B/q04`
