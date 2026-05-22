# 2016-F q11：规模急剧增加时改变或失效的参数

## 题目原问
What parameters in your model change or become irrelevant when the scope of the crisis increases dramatically?

## 适合模型
分析临时 camp capacity、route popularity、daily transport 等参数在长期/超大规模危机中如何让位于住房吸收、国际负担分担、疾病控制和教育连续性。对应模型：尺度转移、参数有效性审计、长期系统动力学。

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
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2016/F/q11/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2016/F/q11/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2016/F/q11/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2016/F/q11`
