# 2016-F q06：支持最优迁移模式的政策包与 UN 信件

## 题目原问
Write a report on your model and propose a set of policies that will support the optimal set of conditions ensuring the optimal migration pattern.

## 适合模型
把安全路线分流、多个入口点、容量触发配额、shelter/healthcare 前置、NGO 物流通道和本地居民健康安全合并为政策包，并写给 UN Secretary General 和 Chief of Migration 的一页政策信。对应模型：政策优化、执行摘要、风险治理、健康安全约束。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted/2016`。
- 行数/记录数：{'official_problem_parameters': 7}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 六条路线容量约束流动模型
- 方法：capacity-constrained deterministic route allocation over the six official travel routes, with explicit emergency overflow when stated crisis scale exceeds temporary route capacity
- 总分配人数：715000。
- 临时容量合计：670000。
- 应急溢出安置人数：45000。

| route | entry_point | allocated_refugees | share_of_total | safety_score | accessibility_score | estimated_processing_days | capacity_binding | emergency_overflow_refugees |
|---|---|---|---|---|---|---|---|---|
| West Mediterranean | Spain | 55000 | 0.07692 | 0.58 | 0.5 | 26.19 | True | 0 |
| Central Mediterranean | Italy | 86000 | 0.12028 | 0.28 | 0.48 | 29.66 | True | 0 |
| Eastern Mediterranean | Greece/Turkey | 329000 | 0.46014 | 0.62 | 0.82 | 40.12 | True | 45000 |
| West Balkans | Hungary/Serbia | 162000 | 0.22657 | 0.5 | 0.68 | 35.22 | True | 0 |
| Eastern Borders | Eastern EU border | 48000 | 0.06713 | 0.54 | 0.36 | 35.56 | True | 0 |
| Albania to Greece | Albania/Greece | 35000 | 0.04895 | 0.6 | 0.42 | 30.43 | True | 0 |

### 动态容量与资源前置
- 方法：priority ranking by weighted unmet resource units after government plus NGO prepositioning
- 最高优先资源：shelter。
- 加入 NGO 后 weighted unmet need：0.0。

| resource | required_units | available_units | unmet_units | priority_weight | weighted_gap | prepositioning_action |
|---|---|---|---|---|---|---|
| shelter | 715.0 | 730.0 | 0.0 | 0.33 | 0.0 | preposition modular shelter near route bottlenecks and high-capacity destinations |
| healthcare | 271.7 | 310.0 | 0.0 | 0.27 | 0.0 | deploy mobile clinics and vaccination/triage teams at entry points |
| water | 1036.75 | 1140.0 | 0.0 | 0.22 | 0.0 | stage purification, trucking, and sanitation units near camps |
| food | 915.2 | 1040.0 | 0.0 | 0.18 | 0.0 | stage dry rations and local procurement contracts |

### 支持最优迁移模式的政策包
- 目标：minimize unsafe movement and unmet basic needs while respecting legal and cultural constraints of affected countries
- 操作指标：weekly safe placements plus weighted unmet resource reduction

- Open multiple entry points on high-volume routes to prevent single-border bottlenecks.
- Shift refugees away from the Central Mediterranean when safer capacity exists.
- Preposition shelter and healthcare before destinations hit maximum capacity.
- Use a quota plus capacity trigger so France and Germany do not carry all resettlement burden.
- Give NGOs formal logistics lanes for mobile clinics, water, food, and temporary shelter.
- Protect local population health with registration, vaccination, sanitation, and transparent risk communication.

### 给 UN 的政策信
To the UN Secretary General and the Chief of Migration:

ICM-RUN recommends a capacity-triggered refugee movement policy for the 715,000 applications reported by the end of October 2015. The model keeps the official six routes visible, shifts volume toward safer capacity such as Eastern Mediterranean, and flags shelter as the current priority resource. The UN should authorize multiple entry points, preposition shelter and healthcare, give NGOs formal logistics roles, and use quota triggers before Germany and France absorb a disproportionate burden. The policy should remain resilient to external security shocks by maintaining contingency entry points, humanitarian screening lanes, and transparent public health communication.

## 模型限制
- 这是可复现的官方题面参数难民政策实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中 715,000+ 申请、Hungary 1,450/100k、32% 批准率、六条路线、最热门/最危险路线、NGO、外生事件和 10 倍扩展等约束。
- 路线安全、可达性、临时容量、日处理能力、资源包和 NGO 增益是显式规划假设，不是边境观测数据；正式论文应补充 UNHCR/IOM/FRONTEX 路线流量、死亡风险、接收容量、庇护审批、公共卫生和本地融合数据校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2016/F/q06/solution.py`

## 输出
- `mcm/question_results/2016/F/q06/result.json`
- `mcm/question_reports/2016/F/q06/report.md`
- `mcm/question_artifacts/2016/F/q06`
