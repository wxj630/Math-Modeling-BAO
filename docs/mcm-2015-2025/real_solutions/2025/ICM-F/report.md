# 2025 ICM-F Cyber Strong?

## 数据真实性
- 官方来源：`docs/mcm-2015-2025/official_assets_extracted/2025/2025_ICM_Problem_F.pdf`。
- 本题无 COMAP 数值附件；代码使用题面引用的 VCDB、World Bank 指标和 ITU GCI 框架做可审计公开源工作流。
- 所有网络数据都会缓存到 artifacts/cache；政策特征矩阵是透明 rubric，不是随机造数。

## Q1 网络犯罪分布
- VCDB 样本记录数：237。
- 国家数：13。
- 主要模式：
- high counts concentrate in English-language and high-reporting economies, especially the United States, so exposure and reporting bias must be separated from true victimization risk
- data-disclosure records form a more conservative success proxy than raw incident counts
- countries with mature reporting regimes can look worse in incident data because more events become visible

## Q2 政策有效性模式
- 理论：strong national cybersecurity policy combines enforceable law, national strategy, mandatory reporting, incident-response institutions, capacity building, and international cooperation; no single pillar is enough。
- mandatory reporting and incident-response institutions increase visible reports, so raw count reduction is not the right effectiveness metric
- international cooperation matters because the official problem emphasizes cross-border jurisdiction and prosecution barriers
- capacity building is a mitigation lever for countries with fast digitization but lower reporting maturity

## Q3 人口统计与混杂因素
- 面板国家数：12。
- 警告：internet access and GDP proxy both exposure and reporting capacity; they can inflate observed cybercrime counts even when policy is effective。

## 给 ITU 峰会领导人的备忘录
Memo for leaders attending the ITU Cybersecurity Summit

Objective: identify policy patterns that help countries reduce cybercrime harm without inventing a new cybersecurity index. Our analysis uses the official ICM-F problem statement, a VCDB incident sample, World Bank national context indicators, and the ITU GCI concept of legal, technical, organizational, capacity-building, and cooperation pillars.

Theory: cyber-strong countries combine enforceable cyber law, mandatory reporting, a national strategy, operational incident response, workforce capacity, and cross-border cooperation. The data warning is important: countries with stronger reporting systems may show more recorded incidents, not necessarily more insecurity.

Findings: visible cybercrime concentrates in high-connectivity, high-reporting economies; disclosure counts are a better harm proxy than raw event counts; and demographics such as internet access and GDP can confound policy evaluation. Leaders should judge policy by reduced harm, faster detection, higher reporting completeness, prosecution capacity, and international cooperation, not by raw incident counts alone.

## 局限与可靠性
- VCDB is incident-report based and not a complete census of global cybercrime
- English-language and public-reporting bias heavily affects country counts
- successful, thwarted, reported, and prosecuted outcomes are not uniformly encoded in one global dataset
- policy feature scores are a transparent rubric over published policy capabilities, not causal estimates
- World Bank demographic indicators describe national context but can confound exposure, capability, and reporting visibility

## 输出产物
- `vcdb_country_distribution.csv`
- `policy_feature_matrix.csv`
- `cyber_country_panel.csv`
- `demographic_correlations.csv`
- `cyber_policy_map.png`
