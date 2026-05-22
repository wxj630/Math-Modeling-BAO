# 2022 MCM-B Water and Hydroelectric Power Sharing

## 数据真实性
- 官方来源：`docs/mcm-2015-2025/official_assets/2022/Water and Hydroelectric Power Sharing`。
- 本题无 COMAP 数值附件；脚本只使用官方题面约束和透明确定性水库/需求场景，不使用随机占位数据。

## 水库串联系统
- 总可持续年释放量：6.428 MAF。
- 重算频率：rerun every 3 months, and immediately after a material height, inflow, or demand update。

## 分配标准
- Do not use historical agreements or political power as allocation inputs.
- Reserve minimum Mexico and Gulf ecological flows before state-sector allocation.
- Meet residential minimum service first, then divide remaining shortages by transparent sector and equity weights.
- Coordinate Lake Powell and Lake Mead as a series system.

## 短缺策略
- Keep residential allocations above the minimum-service threshold whenever possible.
- Do not cut Mexico minimum flow before agricultural and industrial reductions.
- Use hydropower deficits to trigger renewable substitution and demand response rather than extra reservoir drawdown.
- If minimum service cannot be met, rerun monthly and publish state-sector deficit tables.

## 墨西哥与加利福尼亚湾
- Mexico minimum flow：0.9 MAF。
- Gulf ecological flow：0.22 MAF。

## Drought and Thirst 文章摘录
Drought and Thirst article: The proposed plan coordinates Glen Canyon and Hoover operations as one series system. It translates stated reservoir heights into planning storage, reserves minimum Mexico and Gulf flows, and then allocates the remaining water by sector priorities rather than historical power. Residential needs receive the strongest protection, while agriculture and industry share shortage reductions through published weights. Hydropower shortfalls trigger renewable substitution and conservation before deeper drawdown. The plan should be rerun quarterly so infrastructure managers see when demand growth, renewable deployment, or conservation changes the shortage frontier.

## 输出产物
- `reservoir_allocation_plan.csv`：Powell/Mead 高度、库容、释放和水电。
- `state_sector_allocations.csv`：五州三部门需水、分配和缺口。
- `shortage_response_scenarios.csv`：供给下降情景下的短缺响应。
- `demand_change_scenarios.csv`：需求增长/收缩、可再生能源和节水情景。
- `reservoir_allocation_frontier.png`：释放量与短缺边界图。
