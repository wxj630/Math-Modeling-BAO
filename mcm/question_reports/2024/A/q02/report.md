# 2024-A q02：七鳃鳗种群的优点和缺点

## 题目原问
What are the advantages and disadvantages to the population of lampreys?

## 适合模型
比较低食物高雄性比例与高食物低雄性比例情景，量化配对成功、七鳃鳗丰度、宿主损害和种群持续性权衡。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted`。
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

## 模型限制
- 这是可复现的官方题面参数系统动力学实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中 78%/56% 两个性别比例端点。
- 差分方程系数是显式建模假设，用于解释机制和生成论文图表；正式论文应补充本地七鳃鳗、宿主鱼和食物资源监测数据校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2024/A/q02/solution.py`

## 输出
- `mcm/question_results/2024/A/q02/result.json`
- `mcm/question_reports/2024/A/q02/report.md`
- `mcm/question_artifacts/2024/A/q02`
