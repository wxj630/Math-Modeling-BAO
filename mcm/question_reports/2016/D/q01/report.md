# 2016-D q01：信息流与新闻筛选模型

## 题目原问
Develop one or more model(s) that allow(s) you to explore the flow of information and filter or find what qualifies as news.

## 适合模型
只使用官方题面给出的五个传播时期，构造 media access、transmission speed、network connectivity、gatekeeping filter 和 channel capacity 的显式时代参数；用加权 news score 判断 presidential assassination、war news、celebrity rumor、local storm、viral video 是否达到新闻阈值。对应模型：信息扩散、新闻价值评分、多指标综合评价、阈值分类。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted/2016`。
- 行数/记录数：{'official_problem_parameters': 5, 'official_periods': 5}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 官方五时期传播网络参数
- 这些参数是对题面五个时代的显式、可替换归一化假设，不是观测数据。

| era | representative_year | media_access | transmission_speed | network_connectivity | gatekeeping_filter | channel_capacity | diffusion_rate_per_hour | reachable_population_share |
|---|---|---|---|---|---|---|---|---|
| 1870s_telegraph_train_newspaper | 1875 | 0.18 | 0.1 | 0.08 | 0.78 | 1.0 | 0.124 | 0.3276 |
| 1920s_radio | 1925 | 0.36 | 0.28 | 0.2 | 0.7 | 3.8 | 0.2364 | 0.4632 |
| 1970s_television | 1975 | 0.72 | 0.58 | 0.42 | 0.58 | 15.0 | 0.4276 | 0.7304 |
| 1990s_early_internet | 1995 | 0.46 | 0.74 | 0.64 | 0.42 | 85.0 | 0.5708 | 0.6132 |
| 2010s_smartphone | 2015 | 0.82 | 0.92 | 0.88 | 0.22 | 520.0 | 0.7324 | 0.8844 |

### 信息流与新闻筛选
- 阈值：0.58。
- 定义：weighted information value and social transmissibility filter

| item | information_value | source_credibility | affected_population | novelty | shareability | news_score | qualifies_as_news |
|---|---|---|---|---|---|---|---|
| presidential_assassination | 1.0 | 0.96 | 0.92 | 0.84 | 0.75 | 0.9286 | True |
| major_war_breaking_news | 0.94 | 0.9 | 0.88 | 0.8 | 0.7 | 0.876 | True |
| local_storm_damage | 0.54 | 0.72 | 0.24 | 0.5 | 0.46 | 0.5156 | False |
| celebrity_engagement_rumor | 0.32 | 0.42 | 0.3 | 0.68 | 0.88 | 0.4468 | False |
| viral_cat_video | 0.14 | 0.26 | 0.18 | 0.72 | 0.94 | 0.3372 | False |

## 模型限制
- 这是可复现的官方题面参数信息网络实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中五个历史时期、2050 预测要求和信息价值/偏见/来源/拓扑强度等任务约束。
- media access、transmission speed、network connectivity、gatekeeping filter、channel capacity 和观点影响权重是显式归一化假设，不是新闻传播观测数据；正式论文应补充报纸发行、广播/电视普及、互联网使用、智能手机渗透和平台转发级联数据校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2016/D/q01/solution.py`

## 输出
- `mcm/question_results/2016/D/q01/result.json`
- `mcm/question_reports/2016/D/q01/report.md`
- `mcm/question_artifacts/2016/D/q01`
