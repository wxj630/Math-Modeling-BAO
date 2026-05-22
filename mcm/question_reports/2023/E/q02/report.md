# 2023-E q02：四类地点风险评估和解释

## 题目原问
Apply your metric and interpret its results on the following four diverse types of locations: a protected land location, a rural community, a suburban community, and an urban community.

## 适合模型
对 protected_land、rural、suburban、urban 四类题面地点分别设置可替换确定性场景参数，计算风险分、风险等级和主要成分解释。

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

### 四类地点风险评估
- 解释：The same lighting intensity can be high-risk in protected land because biodiversity sensitivity is high, while urban risk is driven by intensity, clutter, glare, and population exposure.。

| location_type | example_location | light_pollution_risk_score | risk_level | sky_glow_component | ecological_component | human_health_component |
|---|---|---|---|---|---|---|
| protected_land | dark-sky sensitive protected habitat | 7.13 | low | 0.0362 | 0.1412 | 0.0451 |
| rural | low-density agricultural village | 13.67 | low | 0.1021 | 0.2039 | 0.1057 |
| suburban | residential-commercial edge community | 37.12 | moderate | 0.4006 | 0.3325 | 0.3656 |
| urban | dense mixed-use city district | 63.34 | high | 0.783 | 0.3805 | 0.6854 |

## 模型限制
- 这是可复现的官方题面参数光污染风险实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中 light trespass、over-illumination、light clutter、protected/rural/suburban/urban 四类地点、三类干预和 flyer 等题面约束。
- 地点画像、权重、干预降幅、成本和可行性是显式确定性情景参数，不是实地照度、卫星夜光或事故/生态监测数据；正式论文应补充 VIIRS 夜光、地面照度、交通事故、犯罪、睡眠健康和物种迁徙数据校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2023/E/q02/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2023/E/q02/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2023/E/q02/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2023/E/q02`
