# 2017-B q04：收费亭类型比例敏感性与 NJTA 信

## 题目原问
How is your solution affected by the proportions of conventional tollbooths, exact-change tollbooths, and electronic toll collection booths?

## 适合模型
比较 mostly conventional、balanced、electronic priority 和 transponder dominant 四种收费服务率组合，判断瓶颈从收费侧转向并道侧的条件，并生成 New Jersey Turnpike Authority 信函。对应模型：服务率模型、情景扫描、非技术政策报告。

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
`.venv/bin/python mcm/question_solutions/2017/B/q04/solution.py`

## 输出
- `mcm/question_results/2017/B/q04/result.json`
- `mcm/question_reports/2017/B/q04/report.md`
- `mcm/question_artifacts/2017/B/q04`
