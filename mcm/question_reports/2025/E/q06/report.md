# 2025-E q06：给探索有机农业农民的一页信

## 题目原问
Include a one-page letter to a farmer who is exploring organic farming practices.

## 适合模型
把食物网模型、有机情景排序、成本/生态权衡和实施监测指标压缩成非技术农民信。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted`。
- 行数/记录数：{'official_parameters': 5}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 有机农业情景比较
- 方法：compare deterministic chemical, herbicide-removal, habitat/bat, partial-organic, and full-organic scenarios by ecology plus economics。
- 推荐过渡：organic_partial。
- 理由：partial organic practices capture most biodiversity and stability gains while preserving a stronger net-margin index during transition。

#### 情景排序

| scenario | crop_yield_index | pest_pressure | biodiversity_index | ecosystem_stability_score | net_margin_index | sustainability_score |
|---|---|---|---|---|---|---|
| organic_full | 135.0 | 0.02 | 1.23 | 2.133 | 120.6 | 1.4659 |
| organic_partial | 135.0 | 0.02 | 1.23 | 2.133 | 117.56 | 1.4659 |
| bats_and_edge_habitat | 135.0 | 0.02 | 1.23 | 2.133 | 113.245 | 1.4659 |
| remove_herbicide | 78.65 | 0.1694 | 0.1923 | 0.5573 | 65.925 | 0.3651 |
| baseline_chemical | 2.0 | 0.02 | 0.02 | 0.029 | -11.99 | 0.019 |

### 给农民的一页信
Dear farmer,

Our model treats your converted forest field as a living food web, not just as a crop-production surface. The main result is that immediately eliminating all chemical tools can raise ecological health, but it also exposes you to a transition period with cost and pest-control risk. The strongest practical first step is the organic partial path: reduce broad-spectrum chemicals, add organic soil inputs, restore field-edge habitat, and support bats and insectivorous birds. This keeps crop health in a workable range while rebuilding natural pest control, pollination, and soil recovery.

A good implementation plan is to monitor crop vigor, pest pressure, beneficial insects, bat activity, bird counts, and soil health monthly. If pest pressure stays controlled and your net margin remains acceptable, expand the organic components. You should also seek conservation incentives for habitat strips, bat boxes, and transition costs, because the ecological benefits extend beyond your farm.

Sincerely,
COMAP ecosystem modeling team

### 策略建议与政策激励

#### 推荐策略

- phase down herbicide and broad-spectrum pesticide over 3-5 growing seasons rather than removing all chemical control at once
- install bat boxes and restore edge habitat/wildflower strips to rebuild biological pest control
- use partial organic input first, track pest pressure and crop-yield index monthly, then expand to full organic if margins remain stable
- advocate cost-share payments or ecosystem-service credits for habitat strips, biological pest control, and transition certification costs

#### 政策激励

- transition grants for first three years of organic inputs
- pollinator and bat-habitat conservation payments
- reduced insurance premiums or low-interest loans for farms with measured biodiversity buffers

## 模型限制
- 这是可复现的官方题面参数生态系统实验，适合处理没有独立 CSV/XLSX 附件的 ICM 题；它不是随机造数，也不是声称拥有真实农场观测。
- 情景参数、经济指数和系统动力学系数是显式假设；正式论文应补充本地作物、害虫监测、土壤检测、投入成本和有机溢价数据进行校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2025/E/q06/solution.py`

## 输出
- `mcm/question_results/2025/E/q06/result.json`
- `mcm/question_reports/2025/E/q06/report.md`
- `mcm/question_artifacts/2025/E/q06`
