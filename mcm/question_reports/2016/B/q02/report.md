# 2016-B q02：成本、风险、收益与重要因素估计

## 题目原问
Your model should include quantitative and/or qualitative estimates of costs, risks, benefits, as well as other important factors.

## 适合模型
对 water jets、high energy lasers、sweeper satellites、tracking subscription 逐项估计 capex、opex、revenue、10 年移除数量、技术风险、监管风险和 scalability。对应模型：多指标综合评价、成本效益分析、风险矩阵。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted/2016/Space Junk.pdf`。
- 行数/记录数：{'official_problem_parameters': 5}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 独立商业方案评估
- 方法：deterministic private-firm screening over cost, revenue, risk, scalability, and 10-year debris-risk reduction proxy

| option | category | capex_musd | annual_revenue_musd | ten_year_debris_removed | risk_score | npv_musd | risk_adjusted_score | commercially_attractive |
|---|---|---|---|---|---|---|---|---|
| laser_tracking_subscription | collision_avoidance_service | 85.0 | 72.0 | 0 | 0.153 | 277.344 | 0.541494 | True |
| high_energy_lasers | active_removal_or_deflection | 260.0 | 92.0 | 24000 | 0.407 | 102.344 | 0.102994 | True |
| space_based_water_jets | active_removal | 420.0 | 105.0 | 18000 | 0.397 | -84.496 | -0.117226 | False |
| sweeper_satellites | active_removal | 780.0 | 135.0 | 52000 | 0.481 | -511.597 | -0.543127 | False |

### 商业机会判断
- 推荐动作：laser_tracking_subscription。
- 最佳候选：high_energy_lasers+laser_tracking_subscription。
- 解释：A full debris-removal business is capital intensive; the most attractive private opportunity is a staged service model that sells collision avoidance and selectively adds laser deflection/removal when contracts support it.

## 模型限制
- 这是可复现的官方题面参数商业筛选实验；COMAP 没有提供轨道碎片 CSV/XLSX 附件，因此只使用 PDF 中 500,000+ tracked debris、2009 collision 和候选移除方法等约束。
- 成本、收入、技术风险、监管风险、移除能力和协同效应是显式商业情景假设，不是实测轨道/合同数据；正式论文应补充公开 TLE/Space-Track、任务成本、保险费率和监管许可数据校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2016/B/q02/solution.py`

## 输出
- `mcm/question_results/2016/B/q02/result.json`
- `mcm/question_reports/2016/B/q02/report.md`
- `mcm/question_artifacts/2016/B/q02`
