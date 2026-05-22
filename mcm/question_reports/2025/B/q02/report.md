# 2025-B q02：模型迁移到其他过度旅游目的地

## 题目原问
Demonstrate how the model could be adapted to another tourist destination impacted by overtourism, and how to promote less crowded attractions or locations.

## 适合模型
把朱诺模型的容量、收费、居民接受度和资源健康指标迁移到 Barcelona overtourism district，用文化景点拥挤替代冰川退缩约束。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2025`。
- 行数/记录数：{'official_parameters': 8}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 朱诺可持续旅游模型
- 目标：maximize weighted sustainability score subject to minimum revenue, resident acceptance, attraction health, and feasible visitor volume。

#### 基线

| annual_visitors | visitors_per_resident | total_revenue_usd | hidden_cost_usd | sustainability_score |
|---|---|---|---|---|
| 1600000 | 53.333 | 375000000.0 | 154163000.0 | 0.6738 |

#### 推荐政策

| daily_cap | visitor_fee_usd | conservation_share | annual_visitors | total_revenue_usd | resident_acceptance_index | environment_index | sustainability_score |
|---|---|---|---|---|---|---|---|
| 10000 | 50.0 | 0.35 | 1408000 | 400400000.0 | 0.78 | 0.80235 | 0.908447 |

#### 收入支出反馈

- conservation：fund glacier trail protection, visitor dispersal to whale watching/rain forest sites, and ecological monitoring
- infrastructure：water, waste, dock scheduling, shuttle electrification, and queue management
- community：resident dividend/community grants, seasonal worker housing mitigation, and visitor behavior enforcement

### 迁移到其他过度旅游目的地
- 目的地：Barcelona overtourism district。
- 选择理由：It has concentrated visitor pressure, resident crowding complaints, and a need to redirect tourists to less saturated attractions; the same model structure applies with different constraints.

#### 迁移后的约束

| constraint | value |
|---|---|
| resident_population_reference | 1620000 |
| district_level_planning_population | 180000 |
| recommended_annual_visitor_target_for_district | 8448000 |
| key_changed_weight | resident acceptance receives higher weight than glacier/attraction health; cultural-site crowding replaces glacier recession. |

#### 政策迁移

- replace cruise daily cap with timed-entry caps at saturated districts
- replace glacier conservation fund with cultural-site maintenance and transit dispersal fund
- use fees to promote under-visited neighborhoods through transit passes and bundled tickets

## 模型限制
- 这是可复现的官方题面参数实验，适合处理没有独立 CSV/XLSX 附件的 MCM 题；它不是随机造数，也不是外部数据回归。
- 价格弹性、隐性成本和支出反馈是显式建模假设，正式论文应通过城市公开预算、港口客流和居民调查进一步校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2025/B/q02/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2025/B/q02/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2025/B/q02/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2025/B/q02`
