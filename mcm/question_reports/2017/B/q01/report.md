# 2017-B q01：收费亭后 8 到 3 车道并道几何

## 题目原问
Determine the shape, size, and merging pattern of the area following the toll barrier in which vehicles fan in from B tollbooth egress lanes down to L lanes of traffic.

## 适合模型
只使用官方题面参数 L、B、B > L 和 3 车道/8 收费亭示例，构造 short taper、staged zipper、collector-distributor 和 metered merge 四类可替换几何方案，按冲突指数、吞吐能力和土地/控制成本评分。对应模型：道路几何规划、多目标评分、成本-安全权衡。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted/2017`。
- 行数/记录数：{'official_problem_parameters': 7}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

## 模型限制
- 这是可复现的官方数据基线实验，适合做论文骨架和结果表，不应把随机森林相关性解释为严格因果。
- 对异常国家/代表队名称、教练履历、项目规则变化等，需要在竞赛论文中追加人工核验和敏感性分析。

## 运行方式
`.venv/bin/python mcm/question_solutions/2017/B/q01/solution.py`

## 输出
- `mcm/question_results/2017/B/q01/result.json`
- `mcm/question_reports/2017/B/q01/report.md`
- `mcm/question_artifacts/2017/B/q01`
