# 2020-C q02：产品声誉随时间增加或下降的模式

## 题目原问
Identify and discuss time-based measures and patterns within each data set that might suggest a product's reputation is increasing or decreasing.

## 适合模型
按 review_date 聚合月度 mean_star、review_count 和 low_rating_share，计算月度评分斜率和低分斜率判断声誉方向。

## 数据与真实性
- 数据类型：official_comap_tsv_zip。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets`。
- 行数/记录数：{'hair_dryer.tsv': 11470, 'microwave.tsv': 1615, 'pacifier.tsv': 18939}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

## 模型限制
- 这是可复现的官方 A Wealth of Data Amazon TSV 附件实验；只使用 `Problem Data- A Wealth of Data` 官方 ZIP 内 hair_dryer.tsv、microwave.tsv 和 pacifier.tsv。
- 描述词 lift 是透明关键词规则，不是深度语义模型；结果描述历史竞品评论，不是 Sunshine Company 新品的因果销售预测。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2020/C/q02/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2020/C/q02/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2020/C/q02/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2020/C/q02`
