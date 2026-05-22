# 2016-F q08：邻国难民流动级联效应

## 题目原问
What would be the cascading effects on the movement of refugees in neighboring countries?

## 适合模型
对 West Balkans、Eastern Mediterranean 等高流量路线施加安全和处理容量下降，输出各路线 post-event safety/capacity 与 queue spillover 解释。对应模型：网络级联、瓶颈传播、压力测试。

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

## 模型限制
- 这是可复现的官方题面参数难民政策实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中 715,000+ 申请、Hungary 1,450/100k、32% 批准率、六条路线、最热门/最危险路线、NGO、外生事件和 10 倍扩展等约束。
- 路线安全、可达性、临时容量、日处理能力、资源包和 NGO 增益是显式规划假设，不是边境观测数据；正式论文应补充 UNHCR/IOM/FRONTEX 路线流量、死亡风险、接收容量、庇护审批、公共卫生和本地融合数据校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2016/F/q08/solution.py`

## 输出
- `mcm/question_results/2016/F/q08/result.json`
- `mcm/question_reports/2016/F/q08/report.md`
- `mcm/question_artifacts/2016/F/q08`
