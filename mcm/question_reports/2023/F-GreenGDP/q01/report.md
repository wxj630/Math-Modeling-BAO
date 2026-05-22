# 2023-F-GreenGDP q01：选择可审计的 Green GDP 计算方法

## 题目原问
There are many proposed ways to calculate GGDP that have already been developed. Select one that your team believes could have a measurable impact on climate mitigation if it replaced GDP as the primary measure of economic health.

## 适合模型
选用 World Bank adjusted-savings 风格的 GGDP：GDP 扣除 CO2 damage、natural resource depletion 和 net forest depletion，并将公式组件写入可审计表。对应模型：环境会计、指标体系。

## 数据与真实性
- 数据类型：official_pdf_and_world_bank_api。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2023`。
- 行数/记录数：{}。
- 本脚本只使用 COMAP 官方 PDF、World Bank WDI 官方 API/缓存和显式政策响应假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

## 模型限制
- 这是可复现的官方数据基线实验，适合做论文骨架和结果表，不应把随机森林相关性解释为严格因果。
- 对异常国家/代表队名称、教练履历、项目规则变化等，需要在竞赛论文中追加人工核验和敏感性分析。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2023/F-GreenGDP/q01/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2023/F-GreenGDP/q01/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2023/F-GreenGDP/q01/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2023/F-GreenGDP/q01`
