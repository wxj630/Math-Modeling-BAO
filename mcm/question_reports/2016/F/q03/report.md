# 2016-F q03：动态容量、资源前置与资源优先级

## 题目原问
What resources can be prepositioned and how should they be allocated in light of these dynamics? What resources need priority and how do you incorporate resource availability and flow in your model?

## 适合模型
把 shelter、healthcare、water、food 作为每千名难民的资源包，比较需求、政府可用量和 NGO 加成后的缺口，按 weighted unmet need 识别优先资源和前置行动。对应模型：系统动力学、资源配置、库存-流量模型、优先级排序。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2016`。
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

### 政府与 NGO 策略对比
- 政府单独未满足需求：101.68。
- 加入 NGO 后未满足需求：0.0。
- 策略变化：With NGOs, the model shifts from border-only processing to distributed mobile support: health, water, food, and shelter can move toward bottlenecks before destinations reach maximum capacity.

## 模型限制
- 这是可复现的官方题面参数难民政策实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中 715,000+ 申请、Hungary 1,450/100k、32% 批准率、六条路线、最热门/最危险路线、NGO、外生事件和 10 倍扩展等约束。
- 路线安全、可达性、临时容量、日处理能力、资源包和 NGO 增益是显式规划假设，不是边境观测数据；正式论文应补充 UNHCR/IOM/FRONTEX 路线流量、死亡风险、接收容量、庇护审批、公共卫生和本地融合数据校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2016/F/q03/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2016/F/q03/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2016/F/q03/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2016/F/q03`
