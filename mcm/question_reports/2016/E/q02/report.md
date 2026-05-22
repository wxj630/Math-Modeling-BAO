# 2016-E q02：选择超载地区并解释缺水驱动因素

## 题目原问
Using the UN water scarcity map pick one country or region where water is heavily or moderately overloaded. Explain why and how water is scarce in that region, addressing physical and/or economic scarcity.

## 适合模型
选择 Jordan 作为 heavily overloaded 地区；用 World Bank 总取水占内部资源比例、农业/生活/工业取水份额、饮水和卫生覆盖解释物理稀缺与经济稀缺。对应模型：指标诊断、社会-环境驱动分析。

## 数据与真实性
- 数据类型：official_pdf_and_world_bank_csv。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2016/Problem Data- Are we heading towards a thirsty planet`。
- 行数/记录数：{'world_bank_jordan_water_indicators.csv': 528}。
- 本脚本只使用 COMAP 官方 PDF、题面推荐的 World Bank 官方公共数据和显式规划假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 清洁水供给能力与缺水诊断
- 定义：A region is critical when withdrawals exceed internal renewable resources after adjusting for service gaps and economic capacity.
- 选定地区：Jordan。
- 基线年份：2024。
- freshwater withdrawals/internal resources：139.277%。
- stress index：1.392771。
- scarcity score/status：1.333454 / critical。

| component | value | interpretation |
|---|---|---|
| physical_stress | 1.392771 | withdrawals/internal renewable resources |
| sanitation_quality_gap | 0.035852 | economic scarcity proxy through sanitation service gap |
| basic_water_access_gap | 0.007139 | clean water access gap |
| economic_capacity_offset | 0.334736 | GDP/capita ability to fund infrastructure |

## 模型限制
- 这是可复现的官方 PDF + World Bank Data 水资源实验；COMAP 没有提供独立 CSV/XLSX 附件，但题面要求使用水资源数据源分析缺水，本工作流缓存 Jordan World Bank 官方指标。
- 干预效果、成本和年度降压百分点是显式规划假设，不是历史因果估计；正式论文应补充流域水文、月度供水、地下水、漏损、价格和项目成本数据校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2016/E/q02/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2016/E/q02/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2016/E/q02/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2016/E/q02`
