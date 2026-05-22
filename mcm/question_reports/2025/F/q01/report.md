# 2025-F q01：全球网络犯罪分布与报告偏差

## 题目原问
How is cybercrime distributed across the globe? Which countries are disproportionately high targets of cybercrimes, where are cybercrimes successful, where are cybercrimes thwarted, where are cybercrimes reported, where are cybercrimes prosecuted? Do you notice any patterns?

## 适合模型
官方 PDF 题面 + 题面引用 VCDB/VERIS 公开事件样本：按受害国统计事件、披露事件和有公开引用的报告事件，并明确起诉/挫败字段在 VCDB 中不可完整观测。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted`。
- 行数/记录数：{'official_parameters': 3}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 网络犯罪分布
- 模型：descriptive country distribution from a deterministic VCDB validated-incident sample。
- VCDB 样本记录：237。
- 国家数：13。
- 起诉字段说明：VCDB records do not consistently encode prosecution outcomes; prosecution is treated as a policy-capacity proxy rather than as a direct incident outcome.。

#### Top 目标国家

| iso3 | country | vcdb_incident_count | share_of_sample | confirmed_disclosure_count | dominant_action_type |
|---|---|---|---|---|---|
| USA | United States | 191 | 0.80591 | 132 | hacking |
| CAN | Canada | 16 | 0.06751 | 12 | hacking |
| GBR | United Kingdom | 13 | 0.05485 | 9 | error |
| AUS | Australia | 4 | 0.01688 | 4 | error |
| IND | India | 3 | 0.01266 | 2 | hacking |
| ESP | Spain | 2 | 0.00844 | 1 | error |
| ZAF | South Africa | 2 | 0.00844 | 2 | physical |
| RUS | Russian Federation | 1 | 0.00422 | 0 | hacking |
| IRL | Ireland | 1 | 0.00422 | 0 | physical |
| SGP | Singapore | 1 | 0.00422 | 0 | hacking |

#### 主要模式

- high counts concentrate in English-language and high-reporting economies, especially the United States, so exposure and reporting bias must be separated from true victimization risk
- data-disclosure records form a more conservative success proxy than raw incident counts
- countries with mature reporting regimes can look worse in incident data because more events become visible

### 数据质量限制
- 样本记录数：237。
- 建议验证：replace the sample with the full VCDB export plus ITU GCI country tables and national CERT/prosecution statistics when preparing a competition paper。
- VCDB is incident-report based and not a complete census of global cybercrime
- English-language and public-reporting bias heavily affects country counts
- successful, thwarted, reported, and prosecuted outcomes are not uniformly encoded in one global dataset
- policy feature scores are a transparent rubric over published policy capabilities, not causal estimates
- World Bank demographic indicators describe national context but can confound exposure, capability, and reporting visibility

## 模型限制
- 这是可复现的官方题面 + 题面引用公开源实验；COMAP 没有提供数值附件，因此本脚本缓存 VCDB/World Bank 数据并保留来源 URL。
- VCDB 是公开报告事件样本，不是全球网络犯罪全集；政策特征矩阵是透明 rubric，不应解释为严格因果估计。

## 运行方式
`.venv/bin/python mcm/question_solutions/2025/F/q01/solution.py`

## 输出
- `mcm/question_results/2025/F/q01/result.json`
- `mcm/question_reports/2025/F/q01/report.md`
- `mcm/question_artifacts/2025/F/q01`
