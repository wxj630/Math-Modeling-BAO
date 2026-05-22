# 2020-C q01：三类 Amazon 评论数据的核心评分与评论指标

## 题目原问
Analyze the three product data sets to identify meaningful quantitative and qualitative patterns, relationships, measures, and parameters within and between star ratings, reviews, and helpfulness ratings.

## 适合模型
直接从官方 ZIP 读取 hair_dryer.tsv、microwave.tsv、pacifier.tsv，按产品计算 review_count、mean_star、low-rating share、helpfulness、review length 和 verified share。

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
`.venv/bin/python mcm/question_solutions/2020/C/q01/solution.py`

## 输出
- `mcm/question_results/2020/C/q01/result.json`
- `mcm/question_reports/2020/C/q01/report.md`
- `mcm/question_artifacts/2020/C/q01`
