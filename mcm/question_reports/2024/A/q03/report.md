# 2024-A q03：性别比变化对生态系统稳定性的影响

## 题目原问
What is the impact on the stability of the ecosystem given the changes in the sex ratios of lampreys?

## 适合模型
在资源水平和七鳃鳗控制压力上做确定性网格，比较自适应性别比与固定 1:1 性别比的稳定性指标。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted`。
- 行数/记录数：{'official_parameters': 4}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 更大生态系统影响
- 模型：lamprey-host-parasite-food-web difference equations with resource-dependent sex ratio and lamprey reduction pressure。

#### 情景比较

| scenario | mean_resource_index | mean_male_ratio | mean_lamprey | mean_host_fish | ecosystem_stability_score |
|---|---|---|---|---|---|
| fixed_equal_ratio | 0.5 | 0.5 | 1.3586 | 0.05 | 0.258 |
| high_food_adaptive | 0.9 | 0.582 | 1.4 | 0.05 | 0.2552 |
| lamprey_reduced_control | 0.5 | 0.67 | 1.1157 | 0.05 | 0.274 |
| low_food_adaptive | 0.12 | 0.7536 | 1.0066 | 0.05 | 0.2783 |
| medium_food_adaptive | 0.5 | 0.67 | 1.3729 | 0.05 | 0.2568 |

#### 七鳃鳗减少影响
- 解释：reducing lampreys relieves host fish but also reduces lamprey food-web value and parasite habitat。
- 七鳃鳗均值：1.1157；宿主鱼均值：0.05。

### 生态系统稳定性
- 自适应 vs 固定性别比稳定性差值：-0.0012。

#### 稳定性最高网格

| resource_index | lamprey_reduction_pressure | mean_male_ratio | mean_lamprey | mean_host_fish | ecosystem_stability_score |
|---|---|---|---|---|---|
| 0.0 | 0.5 | 0.7732 | 0.4698 | 0.4767 | 0.4829 |
| 0.0 | 0.4 | 0.7732 | 0.555 | 0.3596 | 0.4342 |
| 0.1 | 0.5 | 0.758 | 0.5747 | 0.3329 | 0.4222 |
| 0.0 | 0.3 | 0.7732 | 0.6403 | 0.2499 | 0.3842 |
| 0.1 | 0.4 | 0.758 | 0.6563 | 0.23 | 0.3753 |
| 0.2 | 0.5 | 0.736 | 0.7106 | 0.169 | 0.349 |
| 0.0 | 0.2 | 0.7732 | 0.7256 | 0.1554 | 0.3429 |
| 0.1 | 0.3 | 0.758 | 0.738 | 0.1426 | 0.3379 |

## 模型限制
- 这是可复现的官方题面参数系统动力学实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中 78%/56% 两个性别比例端点。
- 差分方程系数是显式建模假设，用于解释机制和生成论文图表；正式论文应补充本地七鳃鳗、宿主鱼和食物资源监测数据校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2024/A/q03/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2024/A/q03/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2024/A/q03/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2024/A/q03`
