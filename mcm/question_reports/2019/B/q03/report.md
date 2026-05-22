# 2019-B q03：一到三个集装箱的最佳布置位置

## 题目原问
Identify best locations on Puerto Rico to position one, two, or three cargo containers for medical delivery and road reconnaissance.

## 适合模型
按需求点距离、道路视频覆盖和港口/机场接入评分 San Juan、Ceiba、Arecibo 三个 staging nodes。对应模型：设施选址、多目标评分。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025/official_assets`。
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
`.venv/bin/python mcm/question_solutions/2019/B/q03/solution.py`

## 输出
- `mcm/question_results/2019/B/q03/result.json`
- `mcm/question_reports/2019/B/q03/report.md`
- `mcm/question_artifacts/2019/B/q03`
