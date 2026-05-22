# 2016-B q04：商业建议与两页执行摘要

## 题目原问
Determine whether an economically attractive opportunity exists. If viable, compare options and recommend how debris should be removed; otherwise provide innovative alternatives for avoiding collisions. Include a two-page executive summary for non-technical decision makers and media analysts.

## 适合模型
把最佳独立/组合候选、what-if 结果和 staged business model 写成给政策制定者与媒体分析师的非技术执行摘要。对应模型：执行摘要、政策建议、模型限制说明。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2016/Space Junk.pdf`。
- 行数/记录数：{'official_problem_parameters': 5}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### What-if 情景
- 方法：deterministic what-if stress tests over debris load and service-market revenue

| scenario | debris_multiplier | revenue_multiplier | best_option | best_npv_musd | best_risk_adjusted_score | commercially_attractive |
|---|---|---|---|---|---|---|
| baseline | 1.0 | 1.0 | laser_tracking_subscription | 277.344 | 0.541494 | True |
| tracked_debris_doubles | 2.0 | 1.15 | laser_tracking_subscription | 349.813 | 0.633163 | True |
| insurance_market_weak | 1.0 | 0.72 | laser_tracking_subscription | 142.069 | 0.370379 | True |
| regulators_support_lasers | 1.1 | 1.05 | laser_tracking_subscription | 301.501 | 0.572051 | True |
| launch_cost_drop_active_removal | 1.35 | 1.0 | laser_tracking_subscription | 277.344 | 0.541494 | True |

### 商业机会判断
- 推荐动作：laser_tracking_subscription。
- 最佳候选：high_energy_lasers+laser_tracking_subscription。
- 解释：A full debris-removal business is capital intensive; the most attractive private opportunity is a staged service model that sells collision avoidance and selectively adds laser deflection/removal when contracts support it.

### Executive summary
Executive summary for policy makers and media analysts:

The official problem states that more than 500,000 pieces of debris are tracked and that the 2009 Kosmos-2251 / Iridium-33 collision made the risk visible. A private company should not begin with an expensive sweeper-satellite-only business. In this screening model, the best near-term commercial option is high_energy_lasers+laser_tracking_subscription, with NPV 398.981 million USD and risk-adjusted score 0.644386. The recommended strategy is staged: sell tracking/avoidance subscriptions first, then add laser deflection for high-value debris when regulation and customer contracts are in place. If revenue weakens, collision-avoidance services remain the least risky fallback; if tracked debris grows faster, hybrid laser-plus-avoidance becomes more attractive.

## 模型限制
- 这是可复现的官方题面参数商业筛选实验；COMAP 没有提供轨道碎片 CSV/XLSX 附件，因此只使用 PDF 中 500,000+ tracked debris、2009 collision 和候选移除方法等约束。
- 成本、收入、技术风险、监管风险、移除能力和协同效应是显式商业情景假设，不是实测轨道/合同数据；正式论文应补充公开 TLE/Space-Track、任务成本、保险费率和监管许可数据校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2016/B/q04/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2016/B/q04/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2016/B/q04/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2016/B/q04`
