# 2016-B q03：独立方案、组合方案与 what-if 情景

## 题目原问
Your model should be able to assess independent alternatives as well as combinations of alternatives and be able to explore a variety of important what-if scenarios.

## 适合模型
枚举两项/三项组合并加入集成成本和协同收益；对 debris 翻倍、市场变弱、监管支持激光、主动移除成本下降做情景压力测试。对应模型：组合优化、情景分析、敏感性分析。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted/2016/Space Junk.pdf`。
- 行数/记录数：{'official_problem_parameters': 5}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 组合方案评估
- 方法：evaluate pair and triple combinations with transparent integration cost and synergy assumptions

| combination | capex_musd | annual_revenue_musd | ten_year_debris_removed | risk_score | npv_musd | risk_adjusted_score | commercially_attractive |
|---|---|---|---|---|---|---|---|
| high_energy_lasers+laser_tracking_subscription | 365.7 | 172.2 | 25920 | 0.2935 | 398.981 | 0.644386 | True |
| space_based_water_jets+high_energy_lasers+laser_tracking_subscription | 856.8 | 295.9 | 48720 | 0.346 | 324.309 | 0.592873 | True |
| space_based_water_jets+laser_tracking_subscription | 535.3 | 185.85 | 19440 | 0.2885 | 202.339 | 0.446826 | True |
| high_energy_lasers+sweeper_satellites+laser_tracking_subscription | 1260.0 | 328.9 | 88160 | 0.374 | -147.334 | 0.13743 | False |
| space_based_water_jets+high_energy_lasers | 720.8 | 206.85 | 45360 | 0.4155 | 18.181 | 0.046398 | False |
| sweeper_satellites+laser_tracking_subscription | 916.9 | 217.35 | 56160 | 0.3305 | -247.033 | 0.004954 | False |
| space_based_water_jets+sweeper_satellites+laser_tracking_subscription | 1439.2 | 343.2 | 81200 | 0.37067 | -353.777 | -0.070969 | False |
| high_energy_lasers+sweeper_satellites | 1102.4 | 238.35 | 82080 | 0.4575 | -431.191 | -0.395474 | False |
| space_based_water_jets+high_energy_lasers+sweeper_satellites | 1635.2 | 365.2 | 109040 | 0.45533 | -547.093 | -0.471425 | False |
| space_based_water_jets+sweeper_satellites | 1272.0 | 252.0 | 75600 | 0.4525 | -627.832 | -0.613033 | False |

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

## 模型限制
- 这是可复现的官方题面参数商业筛选实验；COMAP 没有提供轨道碎片 CSV/XLSX 附件，因此只使用 PDF 中 500,000+ tracked debris、2009 collision 和候选移除方法等约束。
- 成本、收入、技术风险、监管风险、移除能力和协同效应是显式商业情景假设，不是实测轨道/合同数据；正式论文应补充公开 TLE/Space-Track、任务成本、保险费率和监管许可数据校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2016/B/q03/solution.py`

## 输出
- `mcm/question_results/2016/B/q03/result.json`
- `mcm/question_reports/2016/B/q03/report.md`
- `mcm/question_artifacts/2016/B/q03`
