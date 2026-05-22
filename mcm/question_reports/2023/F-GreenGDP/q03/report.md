# 2023-F-GreenGDP q03：全球尺度替换 GDP 的收益与阻力权衡

## 题目原问
Determine if your model indicates that the switch is worthwhile at a global scale, comparing both the potential upside of climate mitigation impact and the potential downside of the effort required to replace the status quo.

## 适合模型
对 cautious pilot、phased G20/resource exporters、full primary metric switch 三种情景比较 climate/resource benefit index、transition effort index 和 net benefit score。对应模型：成本收益、多情景评价。

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
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2023/F-GreenGDP/q03/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2023/F-GreenGDP/q03/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2023/F-GreenGDP/q03/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2023/F-GreenGDP/q03`
