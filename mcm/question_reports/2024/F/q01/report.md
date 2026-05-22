# 2024-F q01：客户是谁

## 题目原问
Who is your client?

## 适合模型
用 mandate、跨境权力、数据访问、执行能力、使命匹配和政治可行性构造客户多指标评分，选择 WCO coordinated customs task force。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted`。
- 行数/记录数：{'official_parameters': 5}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 客户选择
- 选择客户：World Customs Organization coordinated customs task force。
- 选择理由：highest fit because customs coordination has authority over border chokepoints and access to shipment-risk metadata。
- 模型：multi-criteria client fit score over mandate, cross-border power, data access, implementation capacity, mission alignment, and political feasibility。

#### 候选客户评分

| client | mandate_fit | cross_border_power | data_access | implementation_capacity | client_fit_score |
|---|---|---|---|---|---|
| World Customs Organization coordinated customs task force | 0.94 | 0.92 | 0.86 | 0.82 | 0.8768 |
| Global e-commerce marketplace trust-and-safety coalition | 0.76 | 0.54 | 0.92 | 0.8 | 0.7458 |
| Regional wildlife conservation NGO consortium | 0.82 | 0.45 | 0.61 | 0.64 | 0.7 |
| National park agency in a source country | 0.88 | 0.36 | 0.52 | 0.58 | 0.6488 |

## 模型限制
- 这是可复现的官方题面参数非法野生动物贸易项目设计实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中 26.5B USD/year、第四大非法贸易和 5 年项目要求。
- 客户评分、干预减幅、预算和达标概率是显式确定性项目情景，不是执法数据库观测；正式论文应补充 seizure records、CITES/UNODC 路线资料、平台下架数据和地方伙伴调研校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2024/F/q01/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2024/F/q01/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2024/F/q01/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2024/F/q01`
