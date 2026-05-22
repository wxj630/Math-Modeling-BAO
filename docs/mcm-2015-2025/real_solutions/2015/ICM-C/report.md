# 2015 ICM-C Managing Human Capital in Organizations 题面参数实验报告

## 数据来源
- 官方 PDF：`docs/mcm-2015-2025/official_assets_extracted/2015/Managing Human Capital in Organizations.pdf`。
- 本题没有独立 CSV/XLSX 附件；模型只使用题面给出的组织规模、岗位层级、招聘时间、招聘成本、工资、培训成本、85% 填补率和 18% 流失率。
- 其余系数均列入 `assumption_audit`，作为可替换的确定性情景假设，不当作观测数据。

## Q1 人力资本网络模型
- 组织单元：46 个 7 人部门 + 12 个 4 人办公室 = 370 个岗位。
- 当前填补岗位：314.5；空缺：55.5。
- 高知识风险层级：Junior managers / administrators, Senior managers / executives, Experienced supervisors (branch)。

## Q2 流失动态与生产率影响
- 动态过程：离职影响扩散、中层职业阻塞、知识/协调生产率损失。
- 最高生产率损失层级：junior_manager_administrator。

## Q3 两年招聘与培训预算
- 两年总预算：100.643 sigma。
- 招聘成本：57.189 sigma；培训成本：43.454 sigma。

## Q4 25%/35% 流失率情景
- 25% 年流失能否维持 80% 填补率：True。
- 35% 年流失能否维持 80% 填补率：False。
- 间接影响：筛选质量下降、培训负荷上升、中层协调断裂。

## Q5 中层 30% 流失冲击
- 冲击损失：{'junior_manager_administrator': 5.1, 'experienced_supervisor_branch': 6.38}。
- 仅内部晋升后的中层填补率：0.7603。
- 解释：Internal promotion cushions the management gap, but it transfers vacancies to supervisors and experienced staff, so HR health still deteriorates without external recruiting.

## Q6 团队科学与多层网络
- 建议把信息流、信任、影响力、友谊和培训依赖作为多层网络，使用 multiplex centrality 识别关键员工。

## Q7 执行摘要
To the ICM HR Manager:

The official statement describes 370 positions, 314.5 currently filled positions, and an annual attrition rate of 18%. I modeled ICM as a multilayer human-capital network linking hierarchy, work units, attrition influence, and training/recruiting capacity. The most fragile layers are junior managers and supervisors: they are central enough to transmit knowledge and dissatisfaction, but the statement says middle turnover is unusually high.

For the next two years, the aggregate recruiting-plus-training budget is 100.643 sigma units. Under the explicit throughput assumptions, ICM can sustain 80% fill at 25% annual turnover: True; at 35%: False. The 35% case overloads HR and creates indirect costs through weak screening, manager vacancies, and lost informal knowledge.

If 30% of junior managers and experienced supervisors leave, internal promotions recover part of the gap (0.7603 middle-layer fill), but they drain experienced supervisors and staff. Recommendation: stabilize middle managers first, reserve recruiting capacity for critical roles, and build a multiplex employee network so HR can monitor influence, trust, information flow, and training dependencies before departures cascade.

## 输出文件
- `result.json`：docs/mcm-2015-2025/real_solutions/2015/ICM-C/result.json
- `workforce_level_table.csv`：docs/mcm-2015-2025/real_solutions/2015/ICM-C/artifacts/workforce_level_table.csv
- `two_year_budget.csv`：docs/mcm-2015-2025/real_solutions/2015/ICM-C/artifacts/two_year_budget.csv
- `turnover_scenarios.csv`：docs/mcm-2015-2025/real_solutions/2015/ICM-C/artifacts/turnover_scenarios.csv
- `promotion_shock_projection.csv`：docs/mcm-2015-2025/real_solutions/2015/ICM-C/artifacts/promotion_shock_projection.csv
- `human_capital_health.png`：docs/mcm-2015-2025/real_solutions/2015/ICM-C/artifacts/human_capital_health.png
