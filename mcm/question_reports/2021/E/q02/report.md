# 2021-E q02：公平与可持续优先系统的变化和实施时间

## 题目原问
What happens if a food system is optimized for equity and sustainability? How would that system differ from the current one? How long would such a system take to implement?

## 适合模型
比较 current_efficiency_profit 与 equity_sustainability_balanced 权重下的国家得分、环境压力和食品不安全差距，并用 15 年阶段计划表示实施节奏。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025/official_assets`。
- 行数/记录数：{'official_parameters': 7}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### UN 优先级与 10 年计划
- 方法：weighted food-system health score over efficiency, profitability, sustainability, equity, and nutrition resilience。
- 10 年 first-wave priorities：None。
- 预期网络进展增益：None。
- 评价指标：None。

#### 优先级排序

无可展示记录。

## 模型限制
- 这是可复现的官方题面参数食物系统再优化实验；COMAP 没有提供国家食物系统 CSV/XLSX 附件，因此只使用 PDF 中 hunger、环境足迹、效率、利润、可持续、公平、发达/发展中国家和可扩展性等题面约束。
- 国家分数、政策收益、成本和 15 年路线图是显式确定性规划输入，不是 FAO/World Bank/国家营养监测实测数据；正式论文应补充粮食安全、营养、生产者收入、排放、水足迹和治理能力数据校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2021/E/q02/solution.py`

## 输出
- `mcm/question_results/2021/E/q02/result.json`
- `mcm/question_reports/2021/E/q02/report.md`
- `mcm/question_artifacts/2021/E/q02`
