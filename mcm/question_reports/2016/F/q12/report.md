# 2016-F q12：新增长期健康安全参数与时间阈值

## 题目原问
Do new parameters need to be added? How does this increase the time required to resolve refugee placement, and what new issues might arise such as disease control, childbirth, and education?

## 适合模型
加入 disease surveillance、birth/maternal care、school-age education、employment/housing absorption、social cohesion 等长期参数，并设置 180 天阈值触发长期政策。对应模型：长期安置系统动力学、公共卫生模型、教育和社会融合约束。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2016`。
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

### 10 倍规模扩展
- scale factor：10。
- scaled refugees：7150000。
- 不扩容处理天数：352.22。
- 长期参数触发阈值：180 天。

#### 新增参数
- disease surveillance and vaccination coverage
- birth and maternal care rate
- school-age child education capacity
- long-term employment and housing absorption
- local social cohesion and misinformation risk

#### 不可扩展特征
- manual case processing
- single-route bottleneck relief
- short-term shelter-only planning
- government-only resource deployment

#### 改变或失效的参数
- temporary camp capacity becomes less useful than long-term housing absorption
- route popularity becomes less important than international burden sharing
- daily transport becomes coupled to disease control and education continuity

## 模型限制
- 这是可复现的官方题面参数难民政策实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中 715,000+ 申请、Hungary 1,450/100k、32% 批准率、六条路线、最热门/最危险路线、NGO、外生事件和 10 倍扩展等约束。
- 路线安全、可达性、临时容量、日处理能力、资源包和 NGO 增益是显式规划假设，不是边境观测数据；正式论文应补充 UNHCR/IOM/FRONTEX 路线流量、死亡风险、接收容量、庇护审批、公共卫生和本地融合数据校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2016/F/q12/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2016/F/q12/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2016/F/q12/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2016/F/q12`
