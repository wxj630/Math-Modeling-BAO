# 2016-D q02：历史事件到今日传播的结构验证

## 题目原问
Validate your model's reliability by using data from the past and the prediction capability of your model to predict the information communication situation for today and compare that with today's reality.

## 适合模型
对官方题面点名的 Taylor Swift 传闻、今日重要人物遇刺、Lincoln 遇刺做确定性扩散曲线比较；验证模型是否重现从电报/报纸/火车时代到智能手机时代的 24 小时 awareness 数量级跃迁。对应模型：指数扩散、历史结构验证、情景对比。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted/2016`。
- 行数/记录数：{'official_problem_parameters': 5, 'official_periods': 5}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 历史与今日扩散对比
- Taylor Swift 传闻如果发生在 1860/1870s 代理时代，24h awareness：0.300528。
- Lincoln assassination 历史代理 24h awareness：0.321169。
- 今日重要人物遇刺 24h awareness：0.8844。

| scenario | era | hours | awareness_share | information_value | source_credibility |
|---|---|---|---|---|---|
| taylor_swift_engagement_rumor_if_1860 | 1870s_telegraph_train_newspaper | 1 | 0.032325 | 0.34 | 0.42 |
| taylor_swift_engagement_rumor_if_1860 | 1870s_telegraph_train_newspaper | 3 | 0.087722 | 0.34 | 0.42 |
| taylor_swift_engagement_rumor_if_1860 | 1870s_telegraph_train_newspaper | 6 | 0.151954 | 0.34 | 0.42 |
| taylor_swift_engagement_rumor_if_1860 | 1870s_telegraph_train_newspaper | 12 | 0.233426 | 0.34 | 0.42 |
| taylor_swift_engagement_rumor_if_1860 | 1870s_telegraph_train_newspaper | 24 | 0.300528 | 0.34 | 0.42 |
| taylor_swift_engagement_rumor_if_1860 | 1870s_telegraph_train_newspaper | 48 | 0.325363 | 0.34 | 0.42 |
| taylor_swift_engagement_rumor_if_1860 | 1870s_telegraph_train_newspaper | 72 | 0.327415 | 0.34 | 0.42 |
| taylor_swift_engagement_rumor_if_1860 | 1870s_telegraph_train_newspaper | 168 | 0.3276 | 0.34 | 0.42 |
| lincoln_assassination_historical_proxy | 1870s_telegraph_train_newspaper | 1 | 0.049491 | 1.0 | 0.92 |
| lincoln_assassination_historical_proxy | 1870s_telegraph_train_newspaper | 3 | 0.127172 | 1.0 | 0.92 |
| lincoln_assassination_historical_proxy | 1870s_telegraph_train_newspaper | 6 | 0.204977 | 1.0 | 0.92 |
| lincoln_assassination_historical_proxy | 1870s_telegraph_train_newspaper | 12 | 0.281701 | 1.0 | 0.92 |

### 模型可靠性验证
- 历史代理：Compare a high-value assassination event under the newspaper/telegraph/train era to a high-value event under the smartphone era.
- 今日/历史 24h 比值：2.75369。
- 说明：The validation is structural rather than archival: it checks that the model reproduces the expected order-of-magnitude shift from delayed broadcast to near-immediate connected reach.

## 模型限制
- 这是可复现的官方题面参数信息网络实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中五个历史时期、2050 预测要求和信息价值/偏见/来源/拓扑强度等任务约束。
- media access、transmission speed、network connectivity、gatekeeping filter、channel capacity 和观点影响权重是显式归一化假设，不是新闻传播观测数据；正式论文应补充报纸发行、广播/电视普及、互联网使用、智能手机渗透和平台转发级联数据校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2016/D/q02/solution.py`

## 输出
- `mcm/question_results/2016/D/q02/result.json`
- `mcm/question_reports/2016/D/q02/report.md`
- `mcm/question_artifacts/2016/D/q02`
