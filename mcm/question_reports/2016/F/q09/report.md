# 2016-F q09：面向外生事件的韧性移民政策

## 题目原问
How will the immigration policies that you recommend be designed to be resilient to these types of events?

## 适合模型
用 contingency entry points、人道筛查和长期 asylum adjudication 分离、NGO 物流通道、透明公共卫生沟通来保持政策韧性。对应模型：鲁棒政策设计、应急预案、韧性网络。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted/2016`。
- 行数/记录数：{'official_problem_parameters': 7}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 支持最优迁移模式的政策包
- 目标：minimize unsafe movement and unmet basic needs while respecting legal and cultural constraints of affected countries
- 操作指标：weekly safe placements plus weighted unmet resource reduction

- Open multiple entry points on high-volume routes to prevent single-border bottlenecks.
- Shift refugees away from the Central Mediterranean when safer capacity exists.
- Preposition shelter and healthcare before destinations hit maximum capacity.
- Use a quota plus capacity trigger so France and Germany do not carry all resettlement burden.
- Give NGOs formal logistics lanes for mobile clinics, water, food, and temporary shelter.
- Protect local population health with registration, vaccination, sanitation, and transparent risk communication.

### 外生事件压力测试
- 事件：major terrorist attack linked in public debate to the refugee crisis

#### 参数变化
- approval rate decreases
- border processing capacity decreases
- route safety decreases near closed borders
- local acceptance and housing readiness decrease
- security screening time increases

#### 路线压力

| route | baseline_safety | post_event_safety | baseline_daily_capacity | post_event_daily_capacity | cascading_effect |
|---|---|---|---|---|---|
| West Mediterranean | 0.58 | 0.4988 | 2100 | 1638 | queue spillover to neighboring routes and higher shelter/healthcare pressure |
| Central Mediterranean | 0.28 | 0.252 | 2900 | 2378 | queue spillover to neighboring routes and higher shelter/healthcare pressure |
| Eastern Mediterranean | 0.62 | 0.4712 | 8200 | 5576 | queue spillover to neighboring routes and higher shelter/healthcare pressure |
| West Balkans | 0.5 | 0.38 | 4600 | 3128 | queue spillover to neighboring routes and higher shelter/healthcare pressure |
| Eastern Borders | 0.54 | 0.4644 | 1350 | 1053 | queue spillover to neighboring routes and higher shelter/healthcare pressure |
| Albania to Greece | 0.6 | 0.516 | 1150 | 897 | queue spillover to neighboring routes and higher shelter/healthcare pressure |

#### 韧性设计
- pre-authorize contingency entry points
- separate humanitarian screening from long-run asylum adjudication
- keep NGO logistics corridors open during lockdowns
- maintain transparent communication with local populations

### 给 UN 的政策信
To the UN Secretary General and the Chief of Migration:

ICM-RUN recommends a capacity-triggered refugee movement policy for the 715,000 applications reported by the end of October 2015. The model keeps the official six routes visible, shifts volume toward safer capacity such as Eastern Mediterranean, and flags shelter as the current priority resource. The UN should authorize multiple entry points, preposition shelter and healthcare, give NGOs formal logistics roles, and use quota triggers before Germany and France absorb a disproportionate burden. The policy should remain resilient to external security shocks by maintaining contingency entry points, humanitarian screening lanes, and transparent public health communication.

## 模型限制
- 这是可复现的官方题面参数难民政策实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中 715,000+ 申请、Hungary 1,450/100k、32% 批准率、六条路线、最热门/最危险路线、NGO、外生事件和 10 倍扩展等约束。
- 路线安全、可达性、临时容量、日处理能力、资源包和 NGO 增益是显式规划假设，不是边境观测数据；正式论文应补充 UNHCR/IOM/FRONTEX 路线流量、死亡风险、接收容量、庇护审批、公共卫生和本地融合数据校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2016/F/q09/solution.py`

## 输出
- `mcm/question_results/2016/F/q09/result.json`
- `mcm/question_reports/2016/F/q09/report.md`
- `mcm/question_artifacts/2016/F/q09`
