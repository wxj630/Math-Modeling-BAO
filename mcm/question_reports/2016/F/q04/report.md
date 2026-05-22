# 2016-F q04：政府与 NGO 协同策略

## 题目原问
How does the inclusion of NGO's change your model and strategy?

## 适合模型
比较 government-only 和 with-NGO 两种资源策略的 unmet need；NGO 不改变法律准入，但增加移动医疗、水、食物和临时 shelter 能力，使模型从边境处理转为分布式救援。对应模型：情景对比、资源协同、公共-非政府协作模型。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2016`。
- 行数/记录数：{'official_problem_parameters': 7}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

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

### 支持最优迁移模式的政策包
- 目标：minimize unsafe movement and unmet basic needs while respecting legal and cultural constraints of affected countries
- 操作指标：weekly safe placements plus weighted unmet resource reduction

- Open multiple entry points on high-volume routes to prevent single-border bottlenecks.
- Shift refugees away from the Central Mediterranean when safer capacity exists.
- Preposition shelter and healthcare before destinations hit maximum capacity.
- Use a quota plus capacity trigger so France and Germany do not carry all resettlement burden.
- Give NGOs formal logistics lanes for mobile clinics, water, food, and temporary shelter.
- Protect local population health with registration, vaccination, sanitation, and transparent risk communication.

## 模型限制
- 这是可复现的官方题面参数难民政策实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中 715,000+ 申请、Hungary 1,450/100k、32% 批准率、六条路线、最热门/最危险路线、NGO、外生事件和 10 倍扩展等约束。
- 路线安全、可达性、临时容量、日处理能力、资源包和 NGO 增益是显式规划假设，不是边境观测数据；正式论文应补充 UNHCR/IOM/FRONTEX 路线流量、死亡风险、接收容量、庇护审批、公共卫生和本地融合数据校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2016/F/q04/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2016/F/q04/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2016/F/q04/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2016/F/q04`
