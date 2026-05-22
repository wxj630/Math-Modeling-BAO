# 2024-A q04：对寄生虫和其他生态系统成员的优势

## 题目原问
Can an ecosystem with variable sex ratios in the lamprey population offer advantages to others in the ecosystem, such as parasites?

## 适合模型
从宿主鱼、七鳃鳗寄生者、捕食者/人类食物资源三类受益方分析可变性别比稳定七鳃鳗丰度后的间接收益与代价。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted`。
- 行数/记录数：{'official_parameters': 4}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 七鳃鳗种群优缺点
- 低食物雄性比例：0.7536。
- 高食物雄性比例：0.582。

#### 优点
- male-biased low-food cohorts preserve mating opportunities when larval resources are poor
- resource-sensitive sex ratios prevent overproduction of females when juvenile survival is low
- adaptive ratios can dampen population overshoot relative to a fixed sex ratio

#### 缺点
- strong male bias lowers female availability and can bottleneck reproduction
- sex-ratio plasticity makes population forecasts more sensitive to resource measurement error
- host-fish damage can remain high if lamprey survival is also resource-supported

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

### 对寄生虫和其他物种的影响
- 权衡：variable sex ratios can indirectly help parasites and lamprey consumers by stabilizing lamprey persistence, but high lamprey density harms host fish。

| species_group | condition |
|---|---|
| host fish | benefits when lamprey reduction pressure lowers parasitic mortality |
| parasites of lampreys | benefit when lamprey abundance remains moderate to high |
| predators / human harvest using lampreys as food | benefit from sustained lamprey biomass |

## 模型限制
- 这是可复现的官方题面参数系统动力学实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中 78%/56% 两个性别比例端点。
- 差分方程系数是显式建模假设，用于解释机制和生成论文图表；正式论文应补充本地七鳃鳗、宿主鱼和食物资源监测数据校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2024/A/q04/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2024/A/q04/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2024/A/q04/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2024/A/q04`
