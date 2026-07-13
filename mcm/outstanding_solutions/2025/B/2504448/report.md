# 2025 MCM-B Outstanding 复现：2504448

## 复现对象
- 获奖论文：`2504448`，Sustainable Tourism Management in Juneau
- 复现定位：按论文的旅游需求、经济收益、环境影响、居民满意度和动态规划主链重新求解。

## 关键结果
- 终端年份：2028。
- 推荐日游客上限：11000。
- 推荐游客费：55.0 USD。
- 保护支出比例：0.35。
- 年游客量：1491526；总收入：431610327.83 USD。
- 可持续性得分：1.007；居民接受度：1.0。

## 相对 Advanced 的优势
不再复制 policy grid 结果；本脚本直接构建 2024-2028 动态规划状态转移，显式耦合游客需求、税费、保护支出、冰川压力和居民接受度。

## 输出产物
- `dynamic_policy_grid`：`mcm/outstanding_solutions/2025/B/2504448/artifacts/dynamic_policy_grid.csv`
- `yearly_policy`：`mcm/outstanding_solutions/2025/B/2504448/artifacts/yearly_policy.csv`
- `sensitivity`：`mcm/outstanding_solutions/2025/B/2504448/artifacts/sensitivity.csv`
- `tourism_policy_frontier`：`mcm/outstanding_solutions/2025/B/2504448/artifacts/tourism_policy_frontier.png`
- `sensitivity_tornado`：`mcm/outstanding_solutions/2025/B/2504448/artifacts/sensitivity_tornado.png`
