# 2023-C-Boats q04：帆船数据的其他推论

## 题目原问
Identify and discuss any other interesting and informative inferences or conclusions drawn from the data.

## 适合模型
统计单体船/双体船中位价、双体船溢价、价格与长度/船龄相关性、区域-船型中位价和高价品牌。

## 数据与真实性
- 数据类型：official_comap_xlsx。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2023/Problem Data- Understanding Used Sailboat Prices`。
- 行数/记录数：{'monohull': 2346, 'catamaran': 1145}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 帆船数据其他推论
- 双体船中位价：431654.0 USD。
- 单体船中位价：193182.5 USD。
- 双体船中位溢价：123.444%。
- 价格与长度相关系数：0.369121。
- 价格与船龄相关系数：-0.473493。

#### 区域-船型摘要

| hull_type | region | count | median_price | median_length |
|---|---|---|---|---|
| catamaran | Caribbean | 302 | 380000.0 | 44.6 |
| catamaran | Europe | 735 | 449087.0 | 43.6 |
| catamaran | USA | 108 | 449000.0 | 43.0 |
| monohull | Caribbean | 178 | 176131.0 | 45.0 |
| monohull | Europe | 1783 | 193137.0 | 45.0 |
| monohull | USA | 385 | 210000.0 | 43.0 |

#### 高中位价品牌

| hull_type | make | count | median_price |
|---|---|---|---|
| catamaran | Bali | 54 | 455973.0 |
| catamaran | Lagoon | 682 | 445456.5 |
| monohull | X-Yachts | 42 | 403894.0 |
| catamaran | Fountaine Pajot | 160 | 398964.5 |
| catamaran | Nautitech | 80 | 381105.0 |
| catamaran | Leopard | 89 | 350000.0 |
| monohull | Grand Soleil | 65 | 259945.0 |
| monohull | Dehler | 28 | 205284.0 |
| monohull | Hanse | 179 | 204500.0 |
| monohull | Catalina | 37 | 204069.0 |

## 模型限制
- 这是可复现的官方帆船 Excel 基线实验，适合做论文骨架、结果表和图；随机森林和 OLS 区域效应都不应被解释为严格因果。
- COMAP 官方数据不含香港记录；香港部分使用带 URL 的补充挂牌样本做情景比较，正式论文应继续扩充香港本地成交/挂牌样本并记录抓取日期。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2023/C-Boats/q04/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2023/C-Boats/q04/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2023/C-Boats/q04/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2023/C-Boats/q04`
