# 2016-A q02：浴缸形状、体积、人体和动作敏感性

## 题目原问
Use your model to determine the extent to which your strategy depends upon the shape and volume of the tub, the shape/volume/temperature of the person in the bathtub, and the motions made by the person in the bathtub.

## 适合模型
固定推荐流量，比较短深、基准、长浅浴缸，以及静止、轻柔动作、主动搅动的温度误差和空间温差；人体体积/温度作为显式假设。对应模型：参数扫描、几何尺度分析、混合强度模型、敏感性分析。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2016/A Hot Bath.pdf`。
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

### 形状、人体与动作敏感性
- 人体影响说明：A larger or cooler bather increases displacement and heat exchange, so the same trickle requires stronger mixing or slightly higher flow; the scenario uses the visible person assumptions in data_source.

#### Tub shape rows

| shape | surface_area_m2 | water_depth_m | mean_abs_error_c | mean_spatial_range_c | comfort_score |
|---|---|---|---|---|---|
| short_deep_tub | 0.91 | 0.52 | 2.2632 | 7.9658 | 0.093582 |
| baseline_rectangular_tub | 1.12 | 0.42 | 2.5754 | 8.1245 | 0.089888 |
| long_shallow_tub | 1.4 | 0.34 | 3.0526 | 8.3607 | 0.08481 |

#### Motion rows

| motion | mean_abs_error_c | mean_spatial_range_c | comfort_score |
|---|---|---|---|
| still | 2.5753 | 8.4127 | 0.088064 |
| gentle_motion | 2.5754 | 8.1245 | 0.089888 |
| active_stirring | 2.5759 | 7.6766 | 0.092875 |

## 模型限制
- 这是可复现的官方题面参数热传导/混合实验；COMAP 没有提供传感器 CSV/XLSX 附件，因此只使用 PDF 中单水龙头、无循环加热、恒定细流、溢流排水、空间-时间温度和泡泡浴等约束。
- 浴缸尺寸、热损失、人体体积/温度、混合强度和泡泡浴隔热系数是显式物理情景假设，不是实测浴缸数据；正式论文应补充浴缸几何和多点温度传感器数据校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2016/A/q02/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2016/A/q02/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2016/A/q02/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2016/A/q02`
