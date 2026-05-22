# 2025-C q05：伟大教练效应候选与投资建议

## 题目原问
Examine evidence of changes that might be due to a great coach effect; estimate contribution and choose three countries/sports for investing in a great coach.

## 适合模型
在国家-运动-年份层面计算奖牌运动员行数相对近三届均值的突增，作为需要人工核验教练迁移资料的候选证据。

## 数据与真实性
- 数据类型：official_comap_csv。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2025/2025_Problem_C_Data.zip/2025_Problem_C_Data`。
- 行数/记录数：{'summerOly_medal_counts.csv': 1435, 'summerOly_athletes.csv': 252565, 'summerOly_hosts.csv': 35, 'summerOly_programs.csv': 74, 'data_dictionary.csv': 50}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 伟大教练效应候选

| NOC | Sport | Year | medal_rows | jump_vs_recent_mean |
|---|---|---|---|---|
| United States | Baseball/Softball | 2020 | 39 | 39.0 |
| Japan | Baseball/Softball | 2020 | 39 | 39.0 |
| Australia | Swimming | 2000 | 46 | 33.666667 |
| Great Britain | Athletics | 2024 | 40 | 28.333333 |
| Russia | Water Polo | 2000 | 25 | 25.0 |
| China | Swimming | 2024 | 36 | 24.333333 |
| South Korea | Baseball | 2000 | 24 | 24.0 |
| Dominican Republic | Baseball/Softball | 2020 | 24 | 24.0 |
| Serbia | Basketball | 2016 | 24 | 24.0 |
| Russia | Volleyball | 2000 | 24 | 24.0 |
| Australia | Baseball | 2004 | 24 | 24.0 |
| Poland | Athletics | 2020 | 23 | 20.666667 |

### 投资建议
- United States：优先核验并投资 `Baseball/Softball` 高水平教练团队；以异常跃升量 `39.0` 作为上限型增益参考。
- Japan：优先核验并投资 `Baseball/Softball` 高水平教练团队；以异常跃升量 `39.0` 作为上限型增益参考。
- Australia：优先核验并投资 `Swimming` 高水平教练团队；以异常跃升量 `33.666667` 作为上限型增益参考。
- 将候选表中 `jump_vs_recent_mean` 高、且国家已有基础参赛规模的运动作为优先人工核验对象。
- 该数据只能识别异常跃升，不能单独证明教练因果效应；正式论文应补充教练履历时间线作为外部解释。

## 模型限制
- 这是可复现的官方数据基线实验，适合做论文骨架和结果表，不应把随机森林相关性解释为严格因果。
- 对异常国家/代表队名称、教练履历、项目规则变化等，需要在竞赛论文中追加人工核验和敏感性分析。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2025/C/q05/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2025/C/q05/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2025/C/q05/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2025/C/q05`
