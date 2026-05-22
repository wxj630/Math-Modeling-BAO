# 2017-A q01：Kariba 三方案成本收益简评

## 题目原问
ZRA management requires a brief assessment of repairing, rebuilding, or replacing Kariba Dam with sufficient detail to outline potential costs and benefits.

## 适合模型
只使用官方题面给出的三个选项，构造 normalized cost、implementation years、construction disruption、safety improvement 和 water management flexibility 的可替换评分表。对应模型：多指标综合评价、成本收益分析、决策矩阵。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted/2017`。
- 行数/记录数：{'official_problem_parameters': 5}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### Kariba 三方案简短评估
- 管理建议：Option 1 is a near-term risk bridge, but Option 3 is the strategic option if ZRA can manage multi-site construction and ecological constraints.

| option | description | normalized_cost | implementation_years | construction_disruption | safety_improvement | water_management_flexibility | benefit_score | benefit_cost_ratio |
|---|---|---|---|---|---|---|---|---|
| Option 1 | Repairing the existing Kariba Dam | 42.0 | 4 | 0.28 | 0.48 | 0.34 | 0.279 | 0.664286 |
| Option 2 | Rebuilding the existing Kariba Dam | 96.0 | 8 | 0.66 | 0.82 | 0.58 | 0.44 | 0.458333 |
| Option 3 | Removing Kariba Dam and replacing it with 10 to 20 smaller dams | 118.0 | 11 | 0.78 | 0.88 | 0.91 | 0.5585 | 0.473305 |

### ZRA 管理层简报
Brief assessment for ZRA management:

ZRA asked for a two-page comparison of repairing Kariba, rebuilding Kariba, and replacing Kariba with 10-20 smaller dams. Repair is the lowest-cost bridge, rebuild is the single-dam safety reset, and Option 3 provides the highest flexibility. In this transparent scoring model, Option 3 has the highest benefit score, while the detailed Option 3 design recommends 15 smaller dams with water management index 103.110093. Because the official statement does not provide engineering cost or hydrology tables, all costs and capacities are normalized planning assumptions.

## 模型限制
- 这是可复现的官方题面参数 Zambezi River 水库群规划实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中三种选项、10-20 座小坝、同等或更高水量管理能力、正常/极端流量和暴露限制等要求。
- 成本、坝址坐标、容量、流量指数和暴露天数是显式工程规划假设，不是实测水文或施工数据；正式论文应补充 Zambezi 历史径流、Kariba 库容曲线、生态影响、地形地质、移民和工程造价数据校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2017/A/q01/solution.py`

## 输出
- `mcm/question_results/2017/A/q01/result.json`
- `mcm/question_reports/2017/A/q01/report.md`
- `mcm/question_artifacts/2017/A/q01`
