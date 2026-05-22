# 2020-C q04：低星级是否激发更多评论

## 题目原问
Do specific star ratings incite more reviews, for example after seeing a series of low star ratings?

## 适合模型
按时间排序计算 previous-20-review mean rating，比较低评分环境和高评分环境之后的评论数量与评论长度。

## 数据与真实性
- 数据类型：official_comap_tsv_zip。
- 官方数据目录：`docs/mcm-2015-2025/official_assets`。
- 行数/记录数：{'hair_dryer.tsv': 11470, 'microwave.tsv': 1615, 'pacifier.tsv': 18939}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

## 模型限制
- 这是可复现的官方 A Wealth of Data Amazon TSV 附件实验；只使用 `Problem Data- A Wealth of Data` 官方 ZIP 内 hair_dryer.tsv、microwave.tsv 和 pacifier.tsv。
- 描述词 lift 是透明关键词规则，不是深度语义模型；结果描述历史竞品评论，不是 Sunshine Company 新品的因果销售预测。

## 运行方式
`.venv/bin/python mcm/question_solutions/2020/C/q04/solution.py`

## 输出
- `mcm/question_results/2020/C/q04/result.json`
- `mcm/question_reports/2020/C/q04/report.md`
- `mcm/question_artifacts/2020/C/q04`
