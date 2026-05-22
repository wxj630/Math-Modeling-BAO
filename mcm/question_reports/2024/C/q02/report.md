# 2024-C q02：教练随机波动假设检验

## 题目原问
A coach is skeptical that momentum plays a role and assumes swings are random. Use the model or metrics to evaluate this claim.

## 适合模型
对发球校正残差做跨比赛 lag-1 相关、最长连续得分串和决赛势头范围分析，评估是否存在时间结构。

## 数据与真实性
- 数据类型：official_comap_csv。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted/2024/Problem Data- Momentum in Tennis`。
- 行数/记录数：{'2024_Wimbledon_featured_matches.csv': 7284, '2024_data_dictionary.csv': 46}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 随机波动假设评估
- 比赛数：31。
- 发球校正残差 lag-1 平均相关：0.022716。
- 跨比赛 z 值：1.973167。
- 决赛最长连续得分串：7。
- 解释：Serve-adjusted residual correlation and long runs quantify whether point flow departs from independent point-by-point variation; values are evidence of temporal structure, not proof of psychological causality.

## 模型限制
- 这是可复现的官方数据基线实验，适合做论文骨架和结果表，不应把随机森林相关性解释为严格因果。
- 对异常国家/代表队名称、教练履历、项目规则变化等，需要在竞赛论文中追加人工核验和敏感性分析。

## 运行方式
`.venv/bin/python mcm/question_solutions/2024/C/q02/solution.py`

## 输出
- `mcm/question_results/2024/C/q02/result.json`
- `mcm/question_reports/2024/C/q02/report.md`
- `mcm/question_artifacts/2024/C/q02`
