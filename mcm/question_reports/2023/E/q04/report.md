# 2023-E q04：两类地点的最有效干预选择

## 题目原问
Choose two of your locations and use your metric to determine which of your intervention strategies is most effective for each of them. Discuss how the chosen intervention strategy impacts the risk level for the location.

## 适合模型
对 protected_land 和 urban 两类地点枚举干预策略，在风险降低、安全惩罚和可行性约束下选择 post-intervention risk 最低方案。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025`。
- 行数/记录数：{}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 四类地点风险评估
- 解释：The same lighting intensity can be high-risk in protected land because biodiversity sensitivity is high, while urban risk is driven by intensity, clutter, glare, and population exposure.。

| location_type | example_location | light_pollution_risk_score | risk_level | sky_glow_component | ecological_component | human_health_component |
|---|---|---|---|---|---|---|
| protected_land | dark-sky sensitive protected habitat | 7.13 | low | 0.0362 | 0.1412 | 0.0451 |
| rural | low-density agricultural village | 13.67 | low | 0.1021 | 0.2039 | 0.1057 |
| suburban | residential-commercial edge community | 37.12 | moderate | 0.4006 | 0.3325 | 0.3656 |
| urban | dense mixed-use city district | 63.34 | high | 0.783 | 0.3805 | 0.6854 |

### 干预策略评分

| strategy | sky_glow_reduction | trespass_reduction | clutter_reduction | safety_penalty | cost_index | strategy_value_score |
|---|---|---|---|---|---|---|
| zoning ordinance and sign-lighting limits | 0.27 | 0.22 | 0.42 | 0.04 | 0.24 | 0.2898 |
| adaptive dimming and curfew controls | 0.38 | 0.26 | 0.24 | 0.07 | 0.36 | 0.2865 |
| shielded warm-spectrum fixtures | 0.3 | 0.34 | 0.18 | 0.02 | 0.46 | 0.2758 |
| habitat buffer dark corridor | 0.24 | 0.4 | 0.18 | 0.09 | 0.52 | 0.2345 |

#### 一般影响

- Shielding and warm spectrum reduce sky glow and ecological disruption without a major safety penalty.
- Adaptive dimming gives the strongest nighttime intensity reduction but must protect pedestrian and traffic safety.
- Zoning and sign limits reduce clutter and over-illumination at low public cost but require enforcement capacity.

### 两类地点最优干预选择
- 选择规则：choose the strategy with the lowest post-intervention risk while including safety penalty and feasibility。

| location_type | strategy | risk_before | risk_after | risk_reduction_points | specific_actions |
|---|---|---|---|---|---|
| protected_land | adaptive dimming and curfew controls | 7.13 | 4.93 | 2.2 | dim after peak activity, use motion sensors, turn off decorative lighting overnight |
| urban | adaptive dimming and curfew controls | 63.34 | 43.79 | 19.55 | dim after peak activity, use motion sensors, turn off decorative lighting overnight |

## 模型限制
- 这是可复现的官方题面参数光污染风险实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中 light trespass、over-illumination、light clutter、protected/rural/suburban/urban 四类地点、三类干预和 flyer 等题面约束。
- 地点画像、权重、干预降幅、成本和可行性是显式确定性情景参数，不是实地照度、卫星夜光或事故/生态监测数据；正式论文应补充 VIIRS 夜光、地面照度、交通事故、犯罪、睡眠健康和物种迁徙数据校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2023/E/q04/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2023/E/q04/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2023/E/q04/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2023/E/q04`
