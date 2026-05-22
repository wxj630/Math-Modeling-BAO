# 2023-F-GreenGDP q04：巴西国家案例：自然资源、森林和未来世代

## 题目原问
Select a country and provide a more in-depth analysis of how this shift might impact them, explicitly tied to the changes between how GDP and GGDP are calculated.

## 适合模型
选择 Brazil，使用 World Bank 观察到的 natural resource rents、forest area、CO2 damage 和 GGDP gap，解释资源租金再投资、森林资本和碳损害可见性。对应模型：国家案例、多指标解释。

## 数据与真实性
- 数据类型：official_pdf_and_world_bank_api。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted/2023`。
- 行数/记录数：{}。
- 本脚本只使用 COMAP 官方 PDF、World Bank WDI 官方 API/缓存和显式政策响应假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

## 模型限制
- 这是可复现的官方数据基线实验，适合做论文骨架和结果表，不应把随机森林相关性解释为严格因果。
- 对异常国家/代表队名称、教练履历、项目规则变化等，需要在竞赛论文中追加人工核验和敏感性分析。

## 运行方式
`.venv/bin/python mcm/question_solutions/2023/F-GreenGDP/q04/solution.py`

## 输出
- `mcm/question_results/2023/F-GreenGDP/q04/result.json`
- `mcm/question_reports/2023/F-GreenGDP/q04/report.md`
- `mcm/question_artifacts/2023/F-GreenGDP/q04`
