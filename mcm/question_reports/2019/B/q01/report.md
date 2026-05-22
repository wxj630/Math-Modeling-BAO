# 2019-B q01：DroneGo 波多黎各灾害响应系统

## 题目原问
Develop a DroneGo disaster response system to support the Puerto Rico hurricane disaster scenario.

## 适合模型
读取官方 PDF 附件表中的 drone 尺寸、载荷、速度、飞行时间、货舱、MED 包尺寸和需求地点，构造三集装箱 DroneGo 响应系统。对应模型：设施选址、配送调度、装箱规划。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets`。
- 行数/记录数：{'official_parameters': 5}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 潜水器位置预测模型
- 模型：None。
- 12 小时不确定区域：None km^2。
- 24 小时不确定区域：None km^2。
- 12 小时预测中心：None km。

#### 主要不确定性

#### 降低不确定性的遥测

无可展示记录。

## 模型限制
- 这是可复现的官方数据基线实验，适合做论文骨架和结果表，不应把随机森林相关性解释为严格因果。
- 对异常国家/代表队名称、教练履历、项目规则变化等，需要在竞赛论文中追加人工核验和敏感性分析。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2019/B/q01/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2019/B/q01/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2019/B/q01/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2019/B/q01`
