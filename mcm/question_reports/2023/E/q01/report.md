# 2023-E q01：通用光污染风险指标

## 题目原问
Develop a broadly applicable metric to identify the light pollution risk level of a location.

## 适合模型
官方 PDF 题面现象 + 0-100 综合评价指标：sky glow、生态暴露、人类健康、安全眩光和夜空损失；对应教程模型：综合评价与权重决策。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025`。
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

## 模型限制
- 这是可复现的官方题面参数光污染风险实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中 light trespass、over-illumination、light clutter、protected/rural/suburban/urban 四类地点、三类干预和 flyer 等题面约束。
- 地点画像、权重、干预降幅、成本和可行性是显式确定性情景参数，不是实地照度、卫星夜光或事故/生态监测数据；正式论文应补充 VIIRS 夜光、地面照度、交通事故、犯罪、睡眠健康和物种迁徙数据校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2023/E/q01/solution.py`

## 输出
- `mcm/question_results/2023/E/q01/result.json`
- `mcm/question_reports/2023/E/q01/report.md`
- `mcm/question_artifacts/2023/E/q01`
