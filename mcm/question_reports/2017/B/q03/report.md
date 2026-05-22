# 2017-B q03：自动驾驶车辆比例敏感性

## 题目原问
How does your solution change as more autonomous (self-driving) vehicles are added to the traffic mix?

## 适合模型
扫描 0%-80% 自动驾驶比例，用车头时距容量倍率和建议并道长度调整估计是否需要保留 staged zipper 或设置协同并道车道。对应模型：混合交通容量、敏感性分析、政策阈值。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2017`。
- 行数/记录数：{'official_problem_parameters': 7}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

## 模型限制
- 这是可复现的官方数据基线实验，适合做论文骨架和结果表，不应把随机森林相关性解释为严格因果。
- 对异常国家/代表队名称、教练履历、项目规则变化等，需要在竞赛论文中追加人工核验和敏感性分析。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2017/B/q03/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2017/B/q03/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2017/B/q03/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2017/B/q03`
