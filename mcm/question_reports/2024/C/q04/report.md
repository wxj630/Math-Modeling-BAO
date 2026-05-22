# 2024-C q04：跨比赛泛化测试与局限

## 题目原问
Test the model on one or more other matches, discuss prediction quality, missing factors, and generalizability to other matches or sports.

## 适合模型
用全体 31 场比赛最后 30 分平均势头预测点数优势方，并把温网决赛作为留出比赛检查。

## 数据与真实性
- 数据类型：official_comap_csv。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2024/Problem Data- Momentum in Tennis`。
- 行数/记录数：{'2024_Wimbledon_featured_matches.csv': 7284, '2024_data_dictionary.csv': 46}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 泛化测试
- 评估比赛数：31。
- 最后 30 分势头预测点数优势方准确率：0.806452。
- 决赛留出结果：{'predicted_winner_from_last30_momentum': 1, 'actual_point_winner': 1, 'correct': 1, 'last30_momentum_p1': 0.0264}。
- 局限：This evaluates point-share winner, not official match winner by sets; it is a robustness check for flow signal transfer across matches.

## 模型限制
- 这是可复现的官方数据基线实验，适合做论文骨架和结果表，不应把随机森林相关性解释为严格因果。
- 对异常国家/代表队名称、教练履历、项目规则变化等，需要在竞赛论文中追加人工核验和敏感性分析。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2024/C/q04/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2024/C/q04/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2024/C/q04/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2024/C/q04`
