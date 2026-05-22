# 2024-D q02：维持最优水位的控制算法

## 题目原问
Establish algorithms to maintain optimal water levels in the five lakes from inflow and outflow data.

## 适合模型
对 Soo Locks/St. Mary's 与 Moses-Saunders/St. Lawrence 两个可控出流采用目标偏差比例控制，并按历史月度 10%-90% 流量裁剪。

## 数据与真实性
- 数据类型：official_comap_xlsx。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2024/Data- Great Lakes Water Problem/2024_Problem_D_Great_Lakes.xlsx`。
- 行数/记录数：{'records': 2548, 'level_records': 1380, 'flow_records': 1168}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 五大湖网络模型
- 湖泊节点：Lake Superior -> Lake Michigan and Lake Huron -> Lake St. Clair -> Lake Erie -> Lake Ontario
- 连接河流：St. Mary's River -> St. Clair River -> Detroit River -> Niagara River -> Ottawa River -> St. Lawrence River

#### 控制坝

| lake | controlled_outflow | control |
|---|---|---|
| Lake Superior | St. Mary's River | Soo Locks / Compensating Works |
| Lake Ontario | St. Lawrence River | Moses-Saunders Dam |

### 控制算法
- 规则：monthly median flow plus 900 cms per meter above target, clipped to historical 10th-90th percentile by month

| lake | control_flow | mean_abs_level_deviation_m | mean_abs_recommended_change_cms | max_recommended_change_cms |
|---|---|---|---|---|
| Lake Ontario | St. Lawrence River | 0.152681 | 136.499176 | 702.0 |
| Lake Superior | St. Mary's River | 0.186775 | 159.972069 | 449.218411 |

## 模型限制
- 这是可复现的官方数据基线实验，适合做论文骨架和结果表，不应把随机森林相关性解释为严格因果。
- 对异常国家/代表队名称、教练履历、项目规则变化等，需要在竞赛论文中追加人工核验和敏感性分析。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2024/D/q02/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2024/D/q02/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2024/D/q02/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2024/D/q02`
