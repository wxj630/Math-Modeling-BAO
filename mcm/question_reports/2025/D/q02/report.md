# 2025-D q02：公交/步行系统改造项目影响

## 题目原问
Select a project that impacts the bus or pedestrian walkway systems and show its effects on stakeholders.

## 适合模型
用官方公交站客流、候车亭字段和最近驾车节点，筛选高客流无候车亭站点，形成公交站安全与可达性升级项目。

## 数据与真实性
- 数据类型：official_comap_csv。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted/2025/2025_Problem_D_Data.zip/2025_Problem_D_Data`。
- 行数/记录数：{'edges_drive.csv': 91227, 'nodes_drive.csv': 37163, 'Bus_Stops.csv': 2654, 'Bus_Routes.csv': 66, 'MDOT_SHA_Annual_Average_Daily_Traffic_Baltimore.csv': 2398, 'DataDictionary.csv': 111}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 公交/步行项目
- 推荐项目：Install shelters, lighting, ADA boarding pads, and bus-priority curb management at the highest-ridership unsheltered stops.
- 无候车亭站点：2295 / 2654。
- 无候车亭站点客流占比：0.7022。
- 前 10 个高客流无候车亭站点覆盖客流：16266。

| stop_name | riders_total | route_count | nearest_drive_node |
|---|---|---|---|
| MONDAWMIN METRO STATION BAY 1 | 2488 | 1 | 49390032 |
| MONDAWMIN METRO STATION BAY 3 | 2484 | 1 | 49415115 |
| ROGERS AVE METRO STATION BAY 1 | 1859 | 1 | 49494946 |
| SAINT PAUL ST & FAYETTE ST fs sb | 1505 | 12 | 288278866 |
| NORTH AVE & PENNSYLVANIA AVE eb | 1393 | 1 | 49457784 |
| THE ALAMEDA & 32ND ST fs nb | 1374 | 3 | 49396365 |
| MONDAWMIN METRO STATION BAY 6 | 1325 | 1 | 1383183938 |
| SARATOGA ST & EUTAW ST wb | 1288 | 3 | 49555274 |
| FAYETTE ST & SAINT PAUL ST wb | 1287 | 10 | 288278866 |
| WEST BALTIMORE MARC STATION BAY 2 | 1263 | 1 | 49519861 |

## 模型限制
- 这是可复现的官方数据基线实验，适合做论文骨架和结果表，不应把随机森林相关性解释为严格因果。
- 对异常国家/代表队名称、教练履历、项目规则变化等，需要在竞赛论文中追加人工核验和敏感性分析。

## 运行方式
`.venv/bin/python mcm/question_solutions/2025/D/q02/solution.py`

## 输出
- `mcm/question_results/2025/D/q02/result.json`
- `mcm/question_reports/2025/D/q02/report.md`
- `mcm/question_artifacts/2025/D/q02`
