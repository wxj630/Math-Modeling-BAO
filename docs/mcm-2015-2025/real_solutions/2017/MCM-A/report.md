# 2017 MCM-A Managing The Zambezi River 题面参数实验报告

## 数据来源
- 官方 PDF：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2017/Managing The Zambezi River.pdf`。
- 官方题面参数：三种方案；Option 3 必须移除 Kariba 并用 10-20 座较小水坝替代；新系统需具有与 Kariba 相同或更高的总体水量管理能力。
- 本题没有独立 CSV/XLSX 附件；成本、坝址坐标、容量和流量指数都是显式可替换规划假设。

## Requirement 1 三方案简短评估
Brief assessment for ZRA management:

ZRA asked for a two-page comparison of repairing Kariba, rebuilding Kariba, and replacing Kariba with 10-20 smaller dams. Repair is the lowest-cost bridge, rebuild is the single-dam safety reset, and Option 3 provides the highest flexibility. In this transparent scoring model, Option 3 has the highest benefit score, while the detailed Option 3 design recommends 15 smaller dams with water management index 103.110093. Because the official statement does not provide engineering cost or hydrology tables, all costs and capacities are normalized planning assumptions.

## Requirement 2 Option 3 详细设计
- 推荐小坝数量：15。
- 水量管理指数：103.110093，Kariba reference：100.0。
- 安全-成本平衡：40.740093。

## 调度策略
- 原则：Operate the dam chain as staggered buffers rather than independent reservoirs.。

## 极端流量与暴露限制
- 极端情景数：4。
- 暴露限制河段数：5。

## 输出文件
- `result.json`：/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/real_solutions/2017/MCM-A/result.json
- `option_assessment.csv`：/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/real_solutions/2017/MCM-A/artifacts/option_assessment.csv
- `dam_placement_plan.csv`：/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/real_solutions/2017/MCM-A/artifacts/dam_placement_plan.csv
- `flow_modulation_policy.csv`：/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/real_solutions/2017/MCM-A/artifacts/flow_modulation_policy.csv
- `extreme_flow_guidance.csv`：/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/real_solutions/2017/MCM-A/artifacts/extreme_flow_guidance.csv
- `exposure_restrictions.csv`：/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/real_solutions/2017/MCM-A/artifacts/exposure_restrictions.csv
- `dam_system_frontier.png`：/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/real_solutions/2017/MCM-A/artifacts/dam_system_frontier.png
