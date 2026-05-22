# 2023-E q03：三种光污染干预策略

## 题目原问
Describe three possible intervention strategies to address light pollution. Discuss specific actions to implement each strategy and the potential impacts of these actions on the effects of light pollution in general.

## 适合模型
比较 shielded warm-spectrum fixtures、adaptive dimming and curfew controls、zoning ordinance and sign-lighting limits，并保留 habitat buffer dark corridor 作为保护地增强策略。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025`。
- 行数/记录数：{}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

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

## 模型限制
- 这是可复现的官方题面参数光污染风险实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中 light trespass、over-illumination、light clutter、protected/rural/suburban/urban 四类地点、三类干预和 flyer 等题面约束。
- 地点画像、权重、干预降幅、成本和可行性是显式确定性情景参数，不是实地照度、卫星夜光或事故/生态监测数据；正式论文应补充 VIIRS 夜光、地面照度、交通事故、犯罪、睡眠健康和物种迁徙数据校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2023/E/q03/solution.py`

## 输出
- `mcm/question_results/2023/E/q03/result.json`
- `mcm/question_reports/2023/E/q03/report.md`
- `mcm/question_artifacts/2023/E/q03`
