# 2023-E q05：宣传最有效干预策略的一页 flyer

## 题目原问
Finally, for one of your identified locations and its most-effective intervention strategy, produce a 1-page flyer to promote the strategy for that location.

## 适合模型
把保护夜空、暖色全截光、夜间调光、标识限光、生态迁徙和睡眠/安全收益压缩成一页公众宣传 flyer。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025`。
- 行数/记录数：{}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 光污染风险指标
- 量表：0-100。
- 公式：`100*(0.24*sky_glow + 0.25*ecological + 0.20*human_health + 0.16*safety_glare + 0.15*night_sky_loss)`。
- 人类与非人类平衡：Ecological sensitivity and human exposure receive comparable total weight, matching the prompt's human and non-human concerns.。

#### 指标组件

- sky_glow
- ecological_exposure
- human_health
- safety_glare
- night_sky_loss

### 两类地点最优干预选择
- 选择规则：choose the strategy with the lowest post-intervention risk while including safety penalty and feasibility。

| location_type | strategy | risk_before | risk_after | risk_reduction_points | specific_actions |
|---|---|---|---|---|---|
| protected_land | adaptive dimming and curfew controls | 7.13 | 4.93 | 2.2 | dim after peak activity, use motion sensors, turn off decorative lighting overnight |
| urban | adaptive dimming and curfew controls | 63.34 | 43.79 | 19.55 | dim after peak activity, use motion sensors, turn off decorative lighting overnight |

### 一页宣传 Flyer
Flyer: Protect the Night, Keep the Light. Use shielded warm lights, dim lights after peak hours, and cap sign lighting. This lowers sky glow, protects wildlife migration and plant cycles, improves sleep, and keeps necessary safety lighting where people need it.

## 模型限制
- 这是可复现的官方题面参数光污染风险实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中 light trespass、over-illumination、light clutter、protected/rural/suburban/urban 四类地点、三类干预和 flyer 等题面约束。
- 地点画像、权重、干预降幅、成本和可行性是显式确定性情景参数，不是实地照度、卫星夜光或事故/生态监测数据；正式论文应补充 VIIRS 夜光、地面照度、交通事故、犯罪、睡眠健康和物种迁徙数据校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2023/E/q05/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2023/E/q05/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2023/E/q05/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2023/E/q05`
