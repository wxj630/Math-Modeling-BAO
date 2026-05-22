# 2024-D q01：五大湖分月最优水位目标

## 题目原问
Determine optimal water levels of the five Great Lakes at any time of year, considering stakeholder desires.

## 适合模型
用官方月度水位历史中位数定义分月目标水位，用 25%-75% 分位数形成兼顾洪涝、航运和生态的运行带。

## 数据与真实性
- 数据类型：official_comap_xlsx。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted/2024/Data- Great Lakes Water Problem/2024_Problem_D_Great_Lakes.xlsx`。
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

### 分月最优水位目标
- 方法：monthly historical median with interquartile operating band

| lake | annual_target_mean_m | mean_operating_band_width_m | seasonal_target_min_m | seasonal_target_max_m |
|---|---|---|---|---|
| Lake Erie | 174.203333 | 0.424583 | 174.02 | 174.36 |
| Lake Michigan and Lake Huron | 176.1375 | 0.669167 | 175.96 | 176.33 |
| Lake Ontario | 74.818333 | 0.2325 | 74.51 | 75.13 |
| Lake St. Clair | 174.986667 | 0.494167 | 174.85 | 175.15 |
| Lake Superior | 183.293333 | 0.381667 | 183.11 | 183.44 |

## 模型限制
- 这是可复现的官方数据基线实验，适合做论文骨架和结果表，不应把随机森林相关性解释为严格因果。
- 对异常国家/代表队名称、教练履历、项目规则变化等，需要在竞赛论文中追加人工核验和敏感性分析。

## 运行方式
`.venv/bin/python mcm/question_solutions/2024/D/q01/solution.py`

## 输出
- `mcm/question_results/2024/D/q01/result.json`
- `mcm/question_reports/2024/D/q01/report.md`
- `mcm/question_artifacts/2024/D/q01`
