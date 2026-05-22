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

## Baseline 全局报告

Baseline 层把整题拆成 5 个最低可运行脚手架，覆盖的通用模型族为：linear_trend_forecast_baseline×1；linear_weighted_score_baseline×3；report_outline_baseline×1。它的价值不是给出最终答案，而是快速回答三个问题：题面有哪些可用数字，应该从哪个经典模型族切入，代码、结果和报告是否能跑通。

**q01 选择可审计的 Green GDP 计算方法**

- 问题：There are many proposed ways to calculate GGDP that have already been developed. Select one that your team believes could have a measurable impact on climate mitigation if it repl…
- 建模：从 `linear_weighted_score_baseline` 建立通用变量、约束和可运行脚手架。
- 代码入口：[solution.py](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/solutions/2023/F-GreenGDP/q01/solution.py) / [report.md](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/reports/2023/F-GreenGDP/q01/report.md) / [result.json](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/results/2023/F-GreenGDP/q01/result.json)
- 实验结果：method=linear_weighted_score_baseline；baseline_score=0.580171；numeric_token_count=1；method_confidence=0.6824
- 分析：baseline 适合作为建模起点和覆盖检查；它还没有充分吸收题目专用数据、业务约束和论文表达要求。

**q02 GGDP 替代 GDP 的全球气候影响模型**

- 问题：Make a simple model that is easily defendable to estimate the expected global impact on climate mitigation if your selected GGDP is adopted as the primary measure of the economic…
- 建模：从 `linear_weighted_score_baseline` 建立通用变量、约束和可运行脚手架。
- 代码入口：[solution.py](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/solutions/2023/F-GreenGDP/q02/solution.py) / [report.md](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/reports/2023/F-GreenGDP/q02/report.md) / [result.json](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/results/2023/F-GreenGDP/q02/result.json)
- 实验结果：method=linear_weighted_score_baseline；baseline_score=0.566457；numeric_token_count=1；method_confidence=0.6824
- 分析：baseline 适合作为建模起点和覆盖检查；它还没有充分吸收题目专用数据、业务约束和论文表达要求。

**q03 全球尺度替换 GDP 的收益与阻力权衡**

- 问题：Determine if your model indicates that the switch is worthwhile at a global scale, comparing both the potential upside of climate mitigation impact and the potential downside of t…
- 建模：从 `linear_weighted_score_baseline` 建立通用变量、约束和可运行脚手架。
- 代码入口：[solution.py](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/solutions/2023/F-GreenGDP/q03/solution.py) / [report.md](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/reports/2023/F-GreenGDP/q03/report.md) / [result.json](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/results/2023/F-GreenGDP/q03/result.json)
- 实验结果：method=linear_weighted_score_baseline；baseline_score=0.7096；numeric_token_count=1；method_confidence=1
- 分析：baseline 适合作为建模起点和覆盖检查；它还没有充分吸收题目专用数据、业务约束和论文表达要求。

**q04 巴西国家案例：自然资源、森林和未来世代**

- 问题：Select a country and provide a more in-depth analysis of how this shift might impact them, explicitly tied to the changes between how GDP and GGDP are calculated.
- 建模：从 `linear_trend_forecast_baseline` 建立通用变量、约束和可运行脚手架。
- 代码入口：[solution.py](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/solutions/2023/F-GreenGDP/q04/solution.py) / [report.md](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/reports/2023/F-GreenGDP/q04/report.md) / [result.json](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/results/2023/F-GreenGDP/q04/result.json)
- 实验结果：method=linear_trend_forecast_baseline；baseline_score=0.551029；numeric_token_count=1；method_confidence=0.6824
- 分析：baseline 适合作为建模起点和覆盖检查；它还没有充分吸收题目专用数据、业务约束和论文表达要求。

**q05 给巴西领导人的一页非技术报告**

- 问题：Based on your country-specific analysis, write a one-page non-technical report to the leaders of that country on whether to support a switch to GGDP or to reject a switch and main…
- 建模：从 `report_outline_baseline` 建立通用变量、约束和可运行脚手架。
- 代码入口：[solution.py](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/solutions/2023/F-GreenGDP/q05/solution.py) / [report.md](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/reports/2023/F-GreenGDP/q05/report.md) / [result.json](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/results/2023/F-GreenGDP/q05/result.json)
- 实验结果：method=report_outline_baseline；baseline_score=0.666971；numeric_token_count=0；method_confidence=1
- 分析：baseline 适合作为建模起点和覆盖检查；它还没有充分吸收题目专用数据、业务约束和论文表达要求。

**Baseline 读法。** 先看它选择的模型族和 baseline score/实验表，再回到题面判断它漏掉了哪些真实约束。凡是只停留在通用评分、关键词匹配或线性脚手架的地方，就是 advanced 需要升级的地方。

## Advanced 全局报告

Advanced 层使用当前仓库已有的题目专用代码和实验结果，把小问串成一条整题模型链。数据来源覆盖：official_pdf_and_world_bank_api×5。阅读时重点看每问如何继承前问变量、约束、附件字段或情景设定。

**q01 选择可审计的 Green GDP 计算方法**

- 问题：There are many proposed ways to calculate GGDP that have already been developed. Select one that your team believes could have a measurable impact on climate mitigation if it repl…
- 建模：选用 World Bank adjusted-savings 风格的 GGDP：GDP 扣除 CO2 damage、natural resource depletion 和 net forest depletion，并将公式组件写入可审计表。对应模型：环境会计、指标体系。
- 代码入口：[solution.py](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_solutions/2023/F-GreenGDP/q01/solution.py) / [report.md](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_reports/2023/F-GreenGDP/q01/report.md) / [result.json](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_results/2023/F-GreenGDP/q01/result.json)
- 数据：official_pdf_and_world_bank_api；路径: docs/mcm-2015-2025/official_assets_extracted/2023
- 实验结果：selected_ggdp_method: method_id=adjusted_savings_green_gdp；description=A World-Bank adjusted-savings style GGDP subtracts observed environme…；formula=GGDP = GDP * (1 - observed adjusted-savings environmental penalty per…；assumption_audit: truthfulness_note=This workflow uses the official PDF and World Bank WDI observations w…
- 产物：[artifact](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_artifacts/2023/F-GreenGDP/q01/ggdp_formula_components.csv)
- 分析：advanced 已把当前小问落到可复现实验，读者可以直接沿 result.json、report.md 和 artifact 把结论改写成论文段落。

**q02 GGDP 替代 GDP 的全球气候影响模型**

- 问题：Make a simple model that is easily defendable to estimate the expected global impact on climate mitigation if your selected GGDP is adopted as the primary measure of the economic…
- 建模：调用 World Bank WDI 最新可用 GDP、CO2 damage、资源耗减、森林耗减、森林面积和资源租金指标，构建全球与国家面板并估计 GGDP penalty。对应模型：公开数据面板、确定性情景模型。
- 代码入口：[solution.py](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_solutions/2023/F-GreenGDP/q02/solution.py) / [report.md](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_reports/2023/F-GreenGDP/q02/report.md) / [result.json](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_results/2023/F-GreenGDP/q02/result.json)
- 数据：official_pdf_and_world_bank_api；路径: docs/mcm-2015-2025/official_assets_extracted/2023
- 实验结果：global_impact_model: model_note=The simple model translates the official prompt's GGDP adoption quest…；selected_ggdp_method: method_id=adjusted_savings_green_gdp；description=A World-Bank adjusted-savings style GGDP subtracts observed environme…；formula=GGDP = GDP * (1 - observed adjusted-savings environmental penalty per…
- 产物：[artifact](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_artifacts/2023/F-GreenGDP/q02/world_bank_green_gdp_panel.csv)
- 分析：advanced 已把当前小问落到可复现实验，读者可以直接沿 result.json、report.md 和 artifact 把结论改写成论文段落。

**q03 全球尺度替换 GDP 的收益与阻力权衡**

- 问题：Determine if your model indicates that the switch is worthwhile at a global scale, comparing both the potential upside of climate mitigation impact and the potential downside of t…
- 建模：对 cautious pilot、phased G20/resource exporters、full primary metric switch 三种情景比较 climate/resource benefit index、transition effort index 和 net benefit score。对应模型：成本收益、多情景评价。
- 代码入口：[solution.py](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_solutions/2023/F-GreenGDP/q03/solution.py) / [report.md](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_reports/2023/F-GreenGDP/q03/report.md) / [result.json](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_results/2023/F-GreenGDP/q03/result.json)
- 数据：official_pdf_and_world_bank_api；路径: docs/mcm-2015-2025/official_assets_extracted/2023
- 实验结果：global_worthwhile_assessment: scenario_used=phased_g20_plus_resource_exporters；recommendation=support_switch；reasoning=The phased strategy is the most defensible global option because it t…；global_impact_model: model_note=The simple model translates the official prompt's GGDP adoption quest…
- 产物：[artifact](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_artifacts/2023/F-GreenGDP/q03/global_impact_scenarios.csv)
- 分析：advanced 已把当前小问落到可复现实验，读者可以直接沿 result.json、report.md 和 artifact 把结论改写成论文段落。

**q04 巴西国家案例：自然资源、森林和未来世代**

- 问题：Select a country and provide a more in-depth analysis of how this shift might impact them, explicitly tied to the changes between how GDP and GGDP are calculated.
- 建模：选择 Brazil，使用 World Bank 观察到的 natural resource rents、forest area、CO2 damage 和 GGDP gap，解释资源租金再投资、森林资本和碳损害可见性。对应模型：国家案例、多指标解释。
- 代码入口：[solution.py](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_solutions/2023/F-GreenGDP/q04/solution.py) / [report.md](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_reports/2023/F-GreenGDP/q04/report.md) / [result.json](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_results/2023/F-GreenGDP/q04/result.json)
- 数据：official_pdf_and_world_bank_api；路径: docs/mcm-2015-2025/official_assets_extracted/2023
- 实验结果：country_case_study: country_iso3=BRA；country=Brazil；green_gdp_penalty_pct_gni=5.0118；selected_ggdp_method: method_id=adjusted_savings_green_gdp；description=A World-Bank adjusted-savings style GGDP subtracts observed environme…；formula=GGDP = GDP * (1 - observed adjusted-savings environmental penalty per…
- 产物：[artifact](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_artifacts/2023/F-GreenGDP/q04/brazil_country_analysis.csv)
- 分析：advanced 已把当前小问落到可复现实验，读者可以直接沿 result.json、report.md 和 artifact 把结论改写成论文段落。

**q05 给巴西领导人的一页非技术报告**

- 问题：Based on your country-specific analysis, write a one-page non-technical report to the leaders of that country on whether to support a switch to GGDP or to reject a switch and main…
- 建模：把 adjusted-savings GGDP 公式、Brazil GGDP penalty、森林/资源政策含义、全球 phased switch 建议和实施风险压缩成领导人可读报告。对应模型：政策备忘录、非技术摘要。
- 代码入口：[solution.py](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_solutions/2023/F-GreenGDP/q05/solution.py) / [report.md](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_reports/2023/F-GreenGDP/q05/report.md) / [result.json](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_results/2023/F-GreenGDP/q05/result.json)
- 数据：official_pdf_and_world_bank_api；路径: docs/mcm-2015-2025/official_assets_extracted/2023
- 实验结果：one_page_country_report=One-page report to Brazil's economic and environmental leaders  Recom…；country_case_study: country_iso3=BRA；country=Brazil；green_gdp_penalty_pct_gni=5.0118；global_worthwhile_assessment: scenario_used=phased_g20_plus_resource_exporters；recommendation=support_switch；reasoning=The phased strategy is the most defensible global option because it t…
- 产物：[artifact](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_artifacts/2023/F-GreenGDP/q05/green_gdp_policy_frontier.png)
- 分析：advanced 已把当前小问落到可复现实验，读者可以直接沿 result.json、report.md 和 artifact 把结论改写成论文段落。

**Advanced 读法。** 先读模型升级列，确认它把题面数据、附件字段、情景假设或输出模板写进了变量和约束；再读实验结果列，确认 result.json 与 artifact 中已经留下可复现的表、图或决策结果。

## Advanced 相对 Baseline 的优势

**q01 选择可审计的 Green GDP 计算方法**

- 建模优势：Baseline 从 `linear_weighted_score_baseline` 的通用变量和评分出发；Advanced 升级为 选用 World Bank adjusted-savings 风格的 GGDP：GDP 扣除 CO2 damage、natural resource depletion 和 net forest depletion，并将公式组件写入可审计表。对应模型：环境会计、指标体系。，并把题面/附件里的真实数据、约束和输出格式纳入模型。
- 结果优势：Baseline 主要给出 method=linear_weighted_score_baseline；baseline_score=0.580171；numeric_token_count=1；method_confidence=0.6824；Advanced 进一步给出 selected_ggdp_method: method_id=adjusted_savings_green_gdp；description=A World-Bank adjusted-savings style GGDP subtracts observed environme…；formula=GGDP = GDP * (1 - observed adjusted-savings environmental penalty per…；assumption_audit: truthfulness_note=This workflow uses the official PDF and World Bank WDI observations w…，可直接支撑论文中的表格、图或策略解释。

**q02 GGDP 替代 GDP 的全球气候影响模型**

- 建模优势：Baseline 从 `linear_weighted_score_baseline` 的通用变量和评分出发；Advanced 升级为 调用 World Bank WDI 最新可用 GDP、CO2 damage、资源耗减、森林耗减、森林面积和资源租金指标，构建全球与国家面板并估计 GGDP penalty。对应模型：公开数据面板、确定性情景模型。，并把题面/附件里的真实数据、约束和输出格式纳入模型。
- 结果优势：Baseline 主要给出 method=linear_weighted_score_baseline；baseline_score=0.566457；numeric_token_count=1；method_confidence=0.6824；Advanced 进一步给出 global_impact_model: model_note=The simple model translates the official prompt's GGDP adoption quest…；selected_ggdp_method: method_id=adjusted_savings_green_gdp；description=A World-Bank adjusted-savings style GGDP subtracts observed environme…；formula=GGDP = GDP * (1 - observed adjusted-savings environmental penalty per…，可直接支撑论文中的表格、图或策略解释。

**q03 全球尺度替换 GDP 的收益与阻力权衡**

- 建模优势：Baseline 从 `linear_weighted_score_baseline` 的通用变量和评分出发；Advanced 升级为 对 cautious pilot、phased G20/resource exporters、full primary metric switch 三种情景比较 climate/resource benefit index、transition effort index 和 net benefit score。对应模型：成本收益、多情景评价。，并把题面/附件里的真实数据、约束和输出格式纳入模型。
- 结果优势：Baseline 主要给出 method=linear_weighted_score_baseline；baseline_score=0.7096；numeric_token_count=1；method_confidence=1；Advanced 进一步给出 global_worthwhile_assessment: scenario_used=phased_g20_plus_resource_exporters；recommendation=support_switch；reasoning=The phased strategy is the most defensible global option because it t…；global_impact_model: model_note=The simple model translates the official prompt's GGDP adoption quest…，可直接支撑论文中的表格、图或策略解释。

**q04 巴西国家案例：自然资源、森林和未来世代**

- 建模优势：Baseline 从 `linear_trend_forecast_baseline` 的通用变量和评分出发；Advanced 升级为 选择 Brazil，使用 World Bank 观察到的 natural resource rents、forest area、CO2 damage 和 GGDP gap，解释资源租金再投资、森林资本和碳损害可见性。对应模型：国家案例、多指标解释。，并把题面/附件里的真实数据、约束和输出格式纳入模型。
- 结果优势：Baseline 主要给出 method=linear_trend_forecast_baseline；baseline_score=0.551029；numeric_token_count=1；method_confidence=0.6824；Advanced 进一步给出 country_case_study: country_iso3=BRA；country=Brazil；green_gdp_penalty_pct_gni=5.0118；selected_ggdp_method: method_id=adjusted_savings_green_gdp；description=A World-Bank adjusted-savings style GGDP subtracts observed environme…；formula=GGDP = GDP * (1 - observed adjusted-savings environmental penalty per…，可直接支撑论文中的表格、图或策略解释。

**q05 给巴西领导人的一页非技术报告**

- 建模优势：Baseline 从 `report_outline_baseline` 的通用变量和评分出发；Advanced 升级为 把 adjusted-savings GGDP 公式、Brazil GGDP penalty、森林/资源政策含义、全球 phased switch 建议和实施风险压缩成领导人可读报告。对应模型：政策备忘录、非技术摘要。，并把题面/附件里的真实数据、约束和输出格式纳入模型。
- 结果优势：Baseline 主要给出 method=report_outline_baseline；baseline_score=0.666971；numeric_token_count=0；method_confidence=1；Advanced 进一步给出 one_page_country_report=One-page report to Brazil's economic and environmental leaders  Recom…；country_case_study: country_iso3=BRA；country=Brazil；green_gdp_penalty_pct_gni=5.0118；global_worthwhile_assessment: scenario_used=phased_g20_plus_resource_exporters；recommendation=support_switch；reasoning=The phased strategy is the most defensible global option because it t…，可直接支撑论文中的表格、图或策略解释。



## 小问递进链

### q01 选择可审计的 Green GDP 计算方法

**递进作用：** 建立整题主模型或数据入口，后续小问通常都继承这里的变量、指标或数据清洗结果。

**题意摘要：** There are many proposed ways to calculate GGDP that have already been developed. Select one that your team believes could have a measurable impact on climate mitigation if it replaced GDP as the primary measure of econo…

- Baseline：从 `linear_weighted_score_baseline` 的通用脚手架开始；代码入口：[solution.py](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/solutions/2023/F-GreenGDP/q01/solution.py) / [report.md](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/reports/2023/F-GreenGDP/q01/report.md) / [result.json](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/results/2023/F-GreenGDP/q01/result.json)；实验结果：method=linear_weighted_score_baseline；baseline_score=0.580171；numeric_token_count=1；method_confidence=0.6824
- Advanced：official_pdf_and_world_bank_api；代码入口：[solution.py](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_solutions/2023/F-GreenGDP/q01/solution.py) / [report.md](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_reports/2023/F-GreenGDP/q01/report.md) / [result.json](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_results/2023/F-GreenGDP/q01/result.json)；实验结果：selected_ggdp_method: method_id=adjusted_savings_green_gdp；description=A World-Bank adjusted-savings style GGDP subtracts observed environme…；formula=GGDP = GDP * (1 - observed adjusted-savings environmental penalty per…；assumption_audit: truthfulness_note=This workflow uses the official PDF and World Bank WDI observations w…
- 实验产物：[artifact](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_artifacts/2023/F-GreenGDP/q01/ggdp_formula_components.csv)
- Outstanding：预留，用来补强鲁棒性、误差分析、论文图表和整题叙事。

### q02 GGDP 替代 GDP 的全球气候影响模型

**递进作用：** 在前问基础上加入新的约束、数据或评价口径，推进整题模型链。

**题意摘要：** Make a simple model that is easily defendable to estimate the expected global impact on climate mitigation if your selected GGDP is adopted as the primary measure of the economic health of a nation.

- Baseline：从 `linear_weighted_score_baseline` 的通用脚手架开始；代码入口：[solution.py](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/solutions/2023/F-GreenGDP/q02/solution.py) / [report.md](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/reports/2023/F-GreenGDP/q02/report.md) / [result.json](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/results/2023/F-GreenGDP/q02/result.json)；实验结果：method=linear_weighted_score_baseline；baseline_score=0.566457；numeric_token_count=1；method_confidence=0.6824
- Advanced：official_pdf_and_world_bank_api；代码入口：[solution.py](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_solutions/2023/F-GreenGDP/q02/solution.py) / [report.md](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_reports/2023/F-GreenGDP/q02/report.md) / [result.json](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_results/2023/F-GreenGDP/q02/result.json)；实验结果：global_impact_model: model_note=The simple model translates the official prompt's GGDP adoption quest…；selected_ggdp_method: method_id=adjusted_savings_green_gdp；description=A World-Bank adjusted-savings style GGDP subtracts observed environme…；formula=GGDP = GDP * (1 - observed adjusted-savings environmental penalty per…
- 实验产物：[artifact](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_artifacts/2023/F-GreenGDP/q02/world_bank_green_gdp_panel.csv)
- Outstanding：预留，用来补强鲁棒性、误差分析、论文图表和整题叙事。

### q03 全球尺度替换 GDP 的收益与阻力权衡

**递进作用：** 把前面模型转成成本、收益或资源配置结果，连接业务决策。

**题意摘要：** Determine if your model indicates that the switch is worthwhile at a global scale, comparing both the potential upside of climate mitigation impact and the potential downside of the effort required to replace the status…

- Baseline：从 `linear_weighted_score_baseline` 的通用脚手架开始；代码入口：[solution.py](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/solutions/2023/F-GreenGDP/q03/solution.py) / [report.md](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/reports/2023/F-GreenGDP/q03/report.md) / [result.json](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/results/2023/F-GreenGDP/q03/result.json)；实验结果：method=linear_weighted_score_baseline；baseline_score=0.7096；numeric_token_count=1；method_confidence=1
- Advanced：official_pdf_and_world_bank_api；代码入口：[solution.py](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_solutions/2023/F-GreenGDP/q03/solution.py) / [report.md](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_reports/2023/F-GreenGDP/q03/report.md) / [result.json](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_results/2023/F-GreenGDP/q03/result.json)；实验结果：global_worthwhile_assessment: scenario_used=phased_g20_plus_resource_exporters；recommendation=support_switch；reasoning=The phased strategy is the most defensible global option because it t…；global_impact_model: model_note=The simple model translates the official prompt's GGDP adoption quest…
- 实验产物：[artifact](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_artifacts/2023/F-GreenGDP/q03/global_impact_scenarios.csv)
- Outstanding：预留，用来补强鲁棒性、误差分析、论文图表和整题叙事。

### q04 巴西国家案例：自然资源、森林和未来世代

**递进作用：** 把静态模型推进到时间演化或预测，形成递进分析。

**题意摘要：** Select a country and provide a more in-depth analysis of how this shift might impact them, explicitly tied to the changes between how GDP and GGDP are calculated.

- Baseline：从 `linear_trend_forecast_baseline` 的通用脚手架开始；代码入口：[solution.py](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/solutions/2023/F-GreenGDP/q04/solution.py) / [report.md](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/reports/2023/F-GreenGDP/q04/report.md) / [result.json](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/results/2023/F-GreenGDP/q04/result.json)；实验结果：method=linear_trend_forecast_baseline；baseline_score=0.551029；numeric_token_count=1；method_confidence=0.6824
- Advanced：official_pdf_and_world_bank_api；代码入口：[solution.py](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_solutions/2023/F-GreenGDP/q04/solution.py) / [report.md](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_reports/2023/F-GreenGDP/q04/report.md) / [result.json](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_results/2023/F-GreenGDP/q04/result.json)；实验结果：country_case_study: country_iso3=BRA；country=Brazil；green_gdp_penalty_pct_gni=5.0118；selected_ggdp_method: method_id=adjusted_savings_green_gdp；description=A World-Bank adjusted-savings style GGDP subtracts observed environme…；formula=GGDP = GDP * (1 - observed adjusted-savings environmental penalty per…
- 实验产物：[artifact](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_artifacts/2023/F-GreenGDP/q04/brazil_country_analysis.csv)
- Outstanding：预留，用来补强鲁棒性、误差分析、论文图表和整题叙事。

### q05 给巴西领导人的一页非技术报告

**递进作用：** 把前面模型、实验和限制收束成论文或备忘录，是整题表达质量的出口。

**题意摘要：** Based on your country-specific analysis, write a one-page non-technical report to the leaders of that country on whether to support a switch to GGDP or to reject a switch and maintain GDP.

- Baseline：从 `report_outline_baseline` 的通用脚手架开始；代码入口：[solution.py](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/solutions/2023/F-GreenGDP/q05/solution.py) / [report.md](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/reports/2023/F-GreenGDP/q05/report.md) / [result.json](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/generic_baselines/results/2023/F-GreenGDP/q05/result.json)；实验结果：method=report_outline_baseline；baseline_score=0.666971；numeric_token_count=0；method_confidence=1
- Advanced：official_pdf_and_world_bank_api；代码入口：[solution.py](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_solutions/2023/F-GreenGDP/q05/solution.py) / [report.md](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_reports/2023/F-GreenGDP/q05/report.md) / [result.json](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_results/2023/F-GreenGDP/q05/result.json)；实验结果：one_page_country_report=One-page report to Brazil's economic and environmental leaders  Recom…；country_case_study: country_iso3=BRA；country=Brazil；green_gdp_penalty_pct_gni=5.0118；global_worthwhile_assessment: scenario_used=phased_g20_plus_resource_exporters；recommendation=support_switch；reasoning=The phased strategy is the most defensible global option because it t…
- 实验产物：[artifact](https://github.com/wxj630/Math-Modeling-World/blob/main/mcm/question_artifacts/2023/F-GreenGDP/q05/green_gdp_policy_frontier.png)
- Outstanding：预留，用来补强鲁棒性、误差分析、论文图表和整题叙事。

## 复现提示

本页只抽取代码、结果和报告中的关键摘要；完整代码、result.json、report.md 和 artifact 仍保存在仓库原目录。需要运行时，回到 [运行与复现](/reference/reproduce) 查看命令。
