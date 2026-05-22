# 2016-A q03：泡泡浴添加剂对结果的影响

## 题目原问
If the person used a bubble bath additive while initially filling the bathtub to assist in cleansing, how would this affect your model's results?

## 适合模型
把泡泡浴作为表面热阻/隔热因子，比较无泡沫、薄泡沫、中等泡沫和厚泡沫下的温度误差、空间温差和 comfort score。对应模型：边界热阻模型、情景分析、表面散热修正。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted/2016/A Hot Bath.pdf`。
- 行数/记录数：{}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 温度空间-时间模型与推荐策略
- 目标：keep mean bath temperature close to initial target, reduce spatial unevenness, and penalize overflow waste
- 推荐流量：1.75 L/min。
- 推荐动作：active_stirring。
- 平均温度误差：2.5759 C。
- 平均空间温差：7.6766 C。
- 40 分钟溢流水量：70.0 L。

| flow_l_per_min | motion | mean_abs_error_c | mean_spatial_range_c | final_mean_c | wasted_liters | comfort_score |
|---|---|---|---|---|---|---|
| 0.0 | still | 4.3515 | 0.0 | 32.1447 | 0.0 | 0.186864 |
| 0.0 | gentle_motion | 4.3515 | 0.0 | 32.1447 | 0.0 | 0.186864 |
| 0.0 | active_stirring | 4.3515 | 0.0 | 32.1447 | 0.0 | 0.186864 |
| 0.25 | still | 4.0977 | 2.1417 | 32.6637 | 10.0 | 0.143656 |
| 0.25 | gentle_motion | 4.0977 | 1.9651 | 32.6637 | 10.0 | 0.146632 |
| 0.25 | active_stirring | 4.0977 | 1.7408 | 32.6637 | 10.0 | 0.150595 |
| 0.5 | still | 3.8439 | 3.8472 | 33.1827 | 20.0 | 0.121629 |
| 0.5 | gentle_motion | 3.8439 | 3.5713 | 33.1827 | 20.0 | 0.124985 |
| 0.5 | active_stirring | 3.8439 | 3.2078 | 33.1827 | 20.0 | 0.129698 |
| 0.75 | still | 3.5902 | 5.205 | 33.7017 | 30.0 | 0.108646 |
| 0.75 | gentle_motion | 3.5902 | 4.882 | 33.7017 | 30.0 | 0.111784 |
| 0.75 | active_stirring | 3.5902 | 4.4413 | 33.7016 | 30.0 | 0.116371 |

### 泡泡浴影响
- 解释：Bubble bath suppresses surface heat loss but can also suppress natural surface mixing; this experiment isolates the insulating effect and keeps motion fixed.

| bubble_case | surface_heat_loss_reduction_factor | mean_abs_error_c | mean_spatial_range_c | final_mean_c | comfort_score |
|---|---|---|---|---|---|
| no_bubbles | 1.0 | 2.5754 | 8.1245 | 35.7754 | 0.089888 |
| thin_bubble_layer | 1.15 | 2.2747 | 7.9717 | 36.2643 | 0.09344 |
| moderate_bubble_layer | 1.35 | 1.9687 | 7.8132 | 36.7688 | 0.097377 |
| thick_bubble_layer | 1.6 | 1.6861 | 7.6642 | 37.2412 | 0.101343 |

## 模型限制
- 这是可复现的官方题面参数热传导/混合实验；COMAP 没有提供传感器 CSV/XLSX 附件，因此只使用 PDF 中单水龙头、无循环加热、恒定细流、溢流排水、空间-时间温度和泡泡浴等约束。
- 浴缸尺寸、热损失、人体体积/温度、混合强度和泡泡浴隔热系数是显式物理情景假设，不是实测浴缸数据；正式论文应补充浴缸几何和多点温度传感器数据校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2016/A/q03/solution.py`

## 输出
- `mcm/question_results/2016/A/q03/result.json`
- `mcm/question_reports/2016/A/q03/report.md`
- `mcm/question_artifacts/2016/A/q03`
