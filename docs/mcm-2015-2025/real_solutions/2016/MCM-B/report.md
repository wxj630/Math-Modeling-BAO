# 2016 MCM-B Space Junk 题面参数实验报告

## 数据来源
- 官方 PDF：`docs/mcm-2015-2025/official_assets_extracted/2016/Space Junk.pdf`。
- 官方题面参数：tracked debris > 500,000；2009 年 Kosmos-2251 / Iridium-33 collision；候选方案包括 space-based water jets、high energy lasers、sweeper satellites，以及不可行时的 collision avoidance。
- 本题没有独立 CSV/XLSX 附件；商业收入、成本、风险和协同效应均为显式可替换情景假设。

## Q1 时间相关商业机会模型
- 最佳候选：high_energy_lasers+laser_tracking_subscription。
- 10 年 NPV：398.981 million USD。
- 风险调整得分：0.644386。

## Q2 成本、风险、收益比较
- 输出 `alternative_scores.csv` 比较 capex、opex、revenue、10 年移除数量、风险得分和 NPV。

## Q3 组合方案与 what-if 情景
- 输出 `combination_scores.csv` 和 `what_if_scenarios.csv`，比较组合协同与市场变化。

## Q4 商业建议与执行摘要
- 推荐动作：laser_tracking_subscription。
Executive summary for policy makers and media analysts:

The official problem states that more than 500,000 pieces of debris are tracked and that the 2009 Kosmos-2251 / Iridium-33 collision made the risk visible. A private company should not begin with an expensive sweeper-satellite-only business. In this screening model, the best near-term commercial option is high_energy_lasers+laser_tracking_subscription, with NPV 398.981 million USD and risk-adjusted score 0.644386. The recommended strategy is staged: sell tracking/avoidance subscriptions first, then add laser deflection for high-value debris when regulation and customer contracts are in place. If revenue weakens, collision-avoidance services remain the least risky fallback; if tracked debris grows faster, hybrid laser-plus-avoidance becomes more attractive.

## 输出文件
- `result.json`：docs/mcm-2015-2025/real_solutions/2016/MCM-B/result.json
- `alternative_scores.csv`：docs/mcm-2015-2025/real_solutions/2016/MCM-B/artifacts/alternative_scores.csv
- `combination_scores.csv`：docs/mcm-2015-2025/real_solutions/2016/MCM-B/artifacts/combination_scores.csv
- `what_if_scenarios.csv`：docs/mcm-2015-2025/real_solutions/2016/MCM-B/artifacts/what_if_scenarios.csv
- `debris_strategy_frontier.png`：docs/mcm-2015-2025/real_solutions/2016/MCM-B/artifacts/debris_strategy_frontier.png
