# 2019-B q06：道路网络视频侦察飞行计划

## 题目原问
Provide a flight plan for onboard video cameras to assess major highways and roads.

## 适合模型
把 PR-3、PR-52、PR-22 和 San Juan metro hospital ring 作为视频侦察走廊，安排 video-capable drones 在医疗波次之间巡检。对应模型：覆盖路径规划、侦察调度。

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
`.venv/bin/python mcm/question_solutions/2019/B/q06/solution.py`

## 输出
- `mcm/question_results/2019/B/q06/result.json`
- `mcm/question_reports/2019/B/q06/report.md`
- `mcm/question_artifacts/2019/B/q06`
