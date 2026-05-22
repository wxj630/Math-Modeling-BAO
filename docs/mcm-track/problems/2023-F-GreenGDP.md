# 2023-F-GreenGDP ICM-F: Green GDP

> 这是一个赛题整体入口。先看整题主线，再进入 5 个小问的 baseline、advanced 和 outstanding 预留位。

## 整题主线

本题共 5 个小问。阅读时不要把小问拆成孤岛：`选择可审计的 Green GDP 计算方法` 通常给出主模型或数据入口，后续小问逐步加入动态、情景、评价、决策或论文表达要求，最后由 `给巴西领导人的一页非技术报告` 收束成整题结论。

## 赛题材料

| 项目 | 内容 |
|---|---|
| 赛题 | `2023-F-GreenGDP` |
| 小问数 | 5 |
| 推荐模型族 | linear_trend_forecast_baseline；linear_weighted_score_baseline；report_outline_baseline |
| 数据来源 | official_pdf_and_world_bank_api |

## 小问递进链

### q01 选择可审计的 Green GDP 计算方法

**递进作用：** 建立整题主模型或数据入口，后续小问通常都继承这里的变量、指标或数据清洗结果。

**题意摘要：** There are many proposed ways to calculate GGDP that have already been developed. Select one that your team believes could have a measurable impact on climate mitigation if it replaced GDP as the primary measure of econo…

- Baseline：linear_weighted_score_baseline；[report.md](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/reports/2023/F-GreenGDP/q01/report.md)；[solution.py](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/solutions/2023/F-GreenGDP/q01/solution.py)
- Advanced：official_pdf_and_world_bank_api；[report.md](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_reports/2023/F-GreenGDP/q01/report.md)；[solution.py](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_solutions/2023/F-GreenGDP/q01/solution.py)；[result.json](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_results/2023/F-GreenGDP/q01/result.json)
- 实验产物：[artifact](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_artifacts/2023/F-GreenGDP/q01/ggdp_formula_components.csv)
- Outstanding：预留，用来补强鲁棒性、误差分析、论文图表和整题叙事。

### q02 GGDP 替代 GDP 的全球气候影响模型

**递进作用：** 在前问基础上加入新的约束、数据或评价口径，推进整题模型链。

**题意摘要：** Make a simple model that is easily defendable to estimate the expected global impact on climate mitigation if your selected GGDP is adopted as the primary measure of the economic health of a nation.

- Baseline：linear_weighted_score_baseline；[report.md](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/reports/2023/F-GreenGDP/q02/report.md)；[solution.py](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/solutions/2023/F-GreenGDP/q02/solution.py)
- Advanced：official_pdf_and_world_bank_api；[report.md](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_reports/2023/F-GreenGDP/q02/report.md)；[solution.py](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_solutions/2023/F-GreenGDP/q02/solution.py)；[result.json](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_results/2023/F-GreenGDP/q02/result.json)
- 实验产物：[artifact](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_artifacts/2023/F-GreenGDP/q02/world_bank_green_gdp_panel.csv)
- Outstanding：预留，用来补强鲁棒性、误差分析、论文图表和整题叙事。

### q03 全球尺度替换 GDP 的收益与阻力权衡

**递进作用：** 把前面模型转成成本、收益或资源配置结果，连接业务决策。

**题意摘要：** Determine if your model indicates that the switch is worthwhile at a global scale, comparing both the potential upside of climate mitigation impact and the potential downside of the effort required to replace the status…

- Baseline：linear_weighted_score_baseline；[report.md](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/reports/2023/F-GreenGDP/q03/report.md)；[solution.py](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/solutions/2023/F-GreenGDP/q03/solution.py)
- Advanced：official_pdf_and_world_bank_api；[report.md](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_reports/2023/F-GreenGDP/q03/report.md)；[solution.py](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_solutions/2023/F-GreenGDP/q03/solution.py)；[result.json](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_results/2023/F-GreenGDP/q03/result.json)
- 实验产物：[artifact](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_artifacts/2023/F-GreenGDP/q03/global_impact_scenarios.csv)
- Outstanding：预留，用来补强鲁棒性、误差分析、论文图表和整题叙事。

### q04 巴西国家案例：自然资源、森林和未来世代

**递进作用：** 把静态模型推进到时间演化或预测，形成递进分析。

**题意摘要：** Select a country and provide a more in-depth analysis of how this shift might impact them, explicitly tied to the changes between how GDP and GGDP are calculated.

- Baseline：linear_trend_forecast_baseline；[report.md](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/reports/2023/F-GreenGDP/q04/report.md)；[solution.py](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/solutions/2023/F-GreenGDP/q04/solution.py)
- Advanced：official_pdf_and_world_bank_api；[report.md](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_reports/2023/F-GreenGDP/q04/report.md)；[solution.py](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_solutions/2023/F-GreenGDP/q04/solution.py)；[result.json](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_results/2023/F-GreenGDP/q04/result.json)
- 实验产物：[artifact](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_artifacts/2023/F-GreenGDP/q04/brazil_country_analysis.csv)
- Outstanding：预留，用来补强鲁棒性、误差分析、论文图表和整题叙事。

### q05 给巴西领导人的一页非技术报告

**递进作用：** 把前面模型、实验和限制收束成论文或备忘录，是整题表达质量的出口。

**题意摘要：** Based on your country-specific analysis, write a one-page non-technical report to the leaders of that country on whether to support a switch to GGDP or to reject a switch and maintain GDP.

- Baseline：report_outline_baseline；[report.md](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/reports/2023/F-GreenGDP/q05/report.md)；[solution.py](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/solutions/2023/F-GreenGDP/q05/solution.py)
- Advanced：official_pdf_and_world_bank_api；[report.md](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_reports/2023/F-GreenGDP/q05/report.md)；[solution.py](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_solutions/2023/F-GreenGDP/q05/solution.py)；[result.json](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_results/2023/F-GreenGDP/q05/result.json)
- 实验产物：[artifact](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_artifacts/2023/F-GreenGDP/q05/green_gdp_policy_frontier.png)
- Outstanding：预留，用来补强鲁棒性、误差分析、论文图表和整题叙事。

## 复现提示

本页不复制代码和实验结果；代码、结果和报告仍保存在仓库原目录。需要运行时，回到 [运行与复现](/reference/reproduce) 查看命令。

