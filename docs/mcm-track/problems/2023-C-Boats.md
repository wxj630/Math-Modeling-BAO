# 2023-C-Boats MCM-C: Understanding Used Sailboat Prices

> 这是一个赛题整体入口。先看整题主线，再进入 5 个小问的 baseline、advanced 和 outstanding 预留位。

## 整题主线

本题共 5 个小问。阅读时不要把小问拆成孤岛：`二手帆船挂牌价解释模型与估计精度` 通常给出主模型或数据入口，后续小问逐步加入动态、情景、评价、决策或论文表达要求，最后由 `给香港帆船经纪人的报告` 收束成整题结论。

## 赛题材料

| 项目 | 内容 |
|---|---|
| 赛题 | `2023-C-Boats` |
| 小问数 | 5 |
| 推荐模型族 | evidence_table_baseline；linear_trend_forecast_baseline；report_outline_baseline |
| 数据来源 | official_comap_xlsx |

## 小问递进链

### q01 二手帆船挂牌价解释模型与估计精度

**递进作用：** 建立整题主模型或数据入口，后续小问通常都继承这里的变量、指标或数据清洗结果。

**题意摘要：** Develop a mathematical model that explains the listing price of each sailboat in the provided spreadsheet. Include useful predictors, identify data sources, and discuss precision for each sailboat variant's price.

- Baseline：linear_trend_forecast_baseline；[report.md](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/reports/2023/C-Boats/q01/report.md)；[solution.py](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/solutions/2023/C-Boats/q01/solution.py)
- Advanced：official_comap_xlsx；[report.md](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_reports/2023/C-Boats/q01/report.md)；[solution.py](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_solutions/2023/C-Boats/q01/solution.py)；[result.json](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_results/2023/C-Boats/q01/result.json)
- 实验产物：[artifact](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_artifacts/2023/C-Boats/q01/variant_precision.csv)
- Outstanding：预留，用来补强鲁棒性、误差分析、论文图表和整题叙事。

### q02 区域对挂牌价的实际与统计影响

**递进作用：** 在前问基础上加入新的约束、数据或评价口径，推进整题模型链。

**题意摘要：** Use your model to explain the effect, if any, of region on listing prices. Discuss whether regional effects are consistent across all sailboat variants and address practical and statistical significance.

- Baseline：report_outline_baseline；[report.md](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/reports/2023/C-Boats/q02/report.md)；[solution.py](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/solutions/2023/C-Boats/q02/solution.py)
- Advanced：official_comap_xlsx；[report.md](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_reports/2023/C-Boats/q02/report.md)；[solution.py](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_solutions/2023/C-Boats/q02/solution.py)；[result.json](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_results/2023/C-Boats/q02/result.json)
- 实验产物：[artifact](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_artifacts/2023/C-Boats/q02/region_effects.csv)
- Outstanding：预留，用来补强鲁棒性、误差分析、论文图表和整题叙事。

### q03 香港市场可比挂牌样本与区域效应情景

**递进作用：** 在前面模型基础上做情景、敏感性或可靠性检查。

**题意摘要：** Discuss how the regional modeling can be useful in the Hong Kong (SAR) market. Choose an informative subset split between monohulls and catamarans, find comparable Hong Kong listing prices, and model the Hong Kong regio…

- Baseline：linear_trend_forecast_baseline；[report.md](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/reports/2023/C-Boats/q03/report.md)；[solution.py](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/solutions/2023/C-Boats/q03/solution.py)
- Advanced：official_comap_xlsx；[report.md](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_reports/2023/C-Boats/q03/report.md)；[solution.py](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_solutions/2023/C-Boats/q03/solution.py)；[result.json](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_results/2023/C-Boats/q03/result.json)
- 实验产物：[artifact](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_artifacts/2023/C-Boats/q03/hong_kong_comparables.csv)
- Outstanding：预留，用来补强鲁棒性、误差分析、论文图表和整题叙事。

### q04 帆船数据的其他推论

**递进作用：** 在前问基础上加入新的约束、数据或评价口径，推进整题模型链。

**题意摘要：** Identify and discuss any other interesting and informative inferences or conclusions drawn from the data.

- Baseline：evidence_table_baseline；[report.md](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/reports/2023/C-Boats/q04/report.md)；[solution.py](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/solutions/2023/C-Boats/q04/solution.py)
- Advanced：official_comap_xlsx；[report.md](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_reports/2023/C-Boats/q04/report.md)；[solution.py](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_solutions/2023/C-Boats/q04/solution.py)；[result.json](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_results/2023/C-Boats/q04/result.json)
- 实验产物：[artifact](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_artifacts/2023/C-Boats/q04/price_by_region_hull.png)
- Outstanding：预留，用来补强鲁棒性、误差分析、论文图表和整题叙事。

### q05 给香港帆船经纪人的报告

**递进作用：** 把前面模型、实验和限制收束成论文或备忘录，是整题表达质量的出口。

**题意摘要：** Prepare a one- to two-page report for the Hong Kong (SAR) sailboat broker with a few well-chosen graphics.

- Baseline：report_outline_baseline；[report.md](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/reports/2023/C-Boats/q05/report.md)；[solution.py](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/solutions/2023/C-Boats/q05/solution.py)
- Advanced：official_comap_xlsx；[report.md](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_reports/2023/C-Boats/q05/report.md)；[solution.py](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_solutions/2023/C-Boats/q05/solution.py)；[result.json](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_results/2023/C-Boats/q05/result.json)
- 实验产物：[artifact](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_artifacts/2023/C-Boats/q05/model_fit_actual_vs_predicted.png)
- Outstanding：预留，用来补强鲁棒性、误差分析、论文图表和整题叙事。

## 复现提示

本页不复制代码和实验结果；代码、结果和报告仍保存在仓库原目录。需要运行时，回到 [运行与复现](/reference/reproduce) 查看命令。

