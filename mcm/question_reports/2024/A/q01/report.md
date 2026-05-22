# 2024-A q01：七鳃鳗可变性别比对更大生态系统的影响

## 题目原问
What is the impact on the larger ecological system when the population of lampreys can alter its sex ratio?

## 适合模型
官方 PDF 题面参数 0.78/0.56 雄性比例端点 + 资源驱动性别比响应曲线 + 七鳃鳗-宿主鱼-寄生者-食物网差分方程。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted`。
- 行数/记录数：{'official_parameters': 4}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 七鳃鳗资源-性别比模型
- 模型：linear adaptive response between the two official male-ratio endpoints, embedded in monthly ecosystem dynamics。
- 公式：`male_ratio(resource)=0.78-(0.78-0.56)*resource_index`。

#### 响应曲线样本

| resource_index | male_ratio | female_ratio | mating_success_index |
|---|---|---|---|
| 0.0 | 0.78 | 0.22 | 0.6864 |
| 0.05 | 0.769 | 0.231 | 0.7106 |
| 0.1 | 0.758 | 0.242 | 0.7337 |
| 0.15 | 0.747 | 0.253 | 0.756 |
| 0.2 | 0.736 | 0.264 | 0.7772 |
| 0.25 | 0.725 | 0.275 | 0.7975 |
| 0.3 | 0.714 | 0.286 | 0.8168 |
| 0.35 | 0.703 | 0.297 | 0.8352 |

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

## 模型限制
- 这是可复现的官方题面参数系统动力学实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中 78%/56% 两个性别比例端点。
- 差分方程系数是显式建模假设，用于解释机制和生成论文图表；正式论文应补充本地七鳃鳗、宿主鱼和食物资源监测数据校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2024/A/q01/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2024/A/q01/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2024/A/q01/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2024/A/q01`
