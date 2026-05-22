# 2025 MCM-B Sustainable Tourism 题面参数实验报告

## 数据来源
- 官方 PDF：`docs/mcm-2015-2025/official_assets_extracted/2025/2025_MCM_Problem_B.pdf`。
- 本题没有独立 CSV/XLSX 附件；模型只使用题面给出的朱诺人口、游客量、峰值游客、收入和冰川退缩参数，并把其他参数作为显式假设。

## Q1 朱诺可持续旅游模型
- 基线游客/居民比：53.33。
- 推荐日上限：10000，游客费：50.0 USD，保护支出比例：0.35。
- 推荐方案年度游客：1408000；总收入：400400000.0 USD；可持续得分：0.908447。

## 敏感性分析
| factor | correlation_with_score | score_change_p10_p90 | interpretation |
|---|---:|---:|---|
| fee_revenue_usd | 0.919311 | 0.112079 | funds available for mitigation raises the score in this grid. |
| visitor_fee_usd | 0.909965 | 0.142135 | added revenue and price response raises the score in this grid. |
| annual_visitors | -0.868509 | -0.112079 | volume after cap and fee response reduces the score in this grid. |
| hidden_cost_usd | -0.743621 | -0.20902 | infrastructure, crowding, and carbon burden reduces the score in this grid. |
| conservation_share | 0.227667 | 0.0 | fee allocation toward attraction health raises the score in this grid. |
| daily_cap | -0.117707 | -0.0235 | daily crowding pressure and maximum seasonal volume reduces the score in this grid. |

## Q2 迁移到其他过度旅游目的地
- 目的地：Barcelona overtourism district。
- 迁移原因：It has concentrated visitor pressure, resident crowding complaints, and a need to redirect tourists to less saturated attractions; the same model structure applies with different constraints.。
- 政策迁移：replace cruise daily cap with timed-entry caps at saturated districts; replace glacier conservation fund with cultural-site maintenance and transit dispersal fund; use fees to promote under-visited neighborhoods through transit passes and bundled tickets

## Q3 给朱诺旅游委员会备忘录
To the Juneau Tourism Board:

Using the official problem-statement values for Juneau, the baseline is 1.6 million annual cruise passengers, about 53 visitors per resident, and busiest days near 20,000 visitors. The model recommends keeping tourism economically viable while lowering peak pressure: daily cap 10000, visitor fee $50.0, and conservation share 0.35. This policy produces about 1,408,000 annual visitors, total revenue $400,400,000, and a sustainability score of 0.908447, compared with the baseline score 0.6738. The most influential factor in the grid is fee_revenue_usd, so enforcement of caps and fee-funded mitigation should receive the most attention.

Spend new fee revenue on glacier and trail conservation, water/waste/dock infrastructure, electric shuttles, and community programs. The same framework can be transferred to other overtourism locations such as Barcelona by replacing glacier health with cultural-site crowding and using timed-entry plus visitor dispersal.

Recommendation: adopt a moderate cap-fee package, publish transparent annual indicators, and reserve enough fee revenue for visible resident benefits.

## 输出文件
- `result.json`：docs/mcm-2015-2025/real_solutions/2025/MCM-B/result.json
- `policy_grid.csv`：docs/mcm-2015-2025/real_solutions/2025/MCM-B/artifacts/policy_grid.csv
- `frontier_policies.csv`：docs/mcm-2015-2025/real_solutions/2025/MCM-B/artifacts/frontier_policies.csv
- `sensitivity.csv`：docs/mcm-2015-2025/real_solutions/2025/MCM-B/artifacts/sensitivity.csv
- `tourism_policy_frontier.png`：docs/mcm-2015-2025/real_solutions/2025/MCM-B/artifacts/tourism_policy_frontier.png
