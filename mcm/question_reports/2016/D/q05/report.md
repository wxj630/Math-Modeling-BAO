# 2016-D q05：信息价值、偏见、来源和拓扑强度敏感性

## 题目原问
Determine how information value, people's initial opinion and bias, form of the message or its source, and the topology or strength of the information network in a region, country, or worldwide could be used to spread information and influence public opinion.

## 适合模型
在同一观点影响公式上做 one-at-a-time 敏感性分析，识别 information value、source credibility、initial bias、message form、network strength 中最能改变传播和观点结果的因素。对应模型：敏感性分析、影响因子排序、舆论传播策略设计。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted/2016`。
- 行数/记录数：{'official_problem_parameters': 5, 'official_periods': 5}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 2050 通信网络容量预测
- 预测年份：2050。
- 2050 容量指数：2483.157。
- 相对 2010s multiplier：4.775。

### 公众兴趣和观点影响
- 方法：one-step influence score inspired by DeGroot opinion updating and threshold persuasion

| scenario | information_value | source_credibility | initial_bias | message_form_strength | network_strength | persuasion_index | final_support_share | opinion_shift_from_neutral |
|---|---|---|---|---|---|---|---|---|
| trusted_public_health_warning | 0.9 | 0.92 | 0.2 | 0.7 | 0.86 | 0.7352 | 0.83084 | 0.33084 |
| local_emergency_from_official_source | 0.84 | 0.88 | 0.18 | 0.66 | 0.62 | 0.6576 | 0.79592 | 0.29592 |
| scientific_correction_after_false_post | 0.62 | 0.82 | 0.7 | 0.48 | 0.58 | 0.4284 | 0.69278 | 0.19278 |
| celebrity_rumor_visual_shortform | 0.3 | 0.46 | 0.55 | 0.9 | 0.88 | 0.3906 | 0.67577 | 0.17577 |
| partisan_low_credibility_claim | 0.55 | 0.28 | 0.82 | 0.62 | 0.74 | 0.2922 | 0.63149 | 0.13149 |

### 影响因素敏感性
- 最敏感因素：information_value。

| factor | direction | low_score | baseline_score | high_score | absolute_swing |
|---|---|---|---|---|---|
| information_value | positive | 0.399 | 0.459 | 0.519 | 0.12 |
| source_credibility | positive | 0.407 | 0.459 | 0.511 | 0.104 |
| initial_bias | negative | 0.503 | 0.459 | 0.415 | 0.088 |
| network_strength | positive | 0.419 | 0.459 | 0.499 | 0.08 |
| message_form_strength | positive | 0.431 | 0.459 | 0.487 | 0.056 |

## 模型限制
- 这是可复现的官方题面参数信息网络实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中五个历史时期、2050 预测要求和信息价值/偏见/来源/拓扑强度等任务约束。
- media access、transmission speed、network connectivity、gatekeeping filter、channel capacity 和观点影响权重是显式归一化假设，不是新闻传播观测数据；正式论文应补充报纸发行、广播/电视普及、互联网使用、智能手机渗透和平台转发级联数据校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2016/D/q05/solution.py`

## 输出
- `mcm/question_results/2016/D/q05/result.json`
- `mcm/question_reports/2016/D/q05/report.md`
- `mcm/question_artifacts/2016/D/q05`
