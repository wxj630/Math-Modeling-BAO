# 2025-D q06：交通系统服务城市安全

## 题目原问
Safety is a significant issue facing Baltimore. How can the transportation system be used to best address this issue?

## 适合模型
用 AADT/lane 暴露和高客流公交站，形成行人庇护岛、照明、速度管理、公交站硬化和路口安全优先级。

## 数据与真实性
- 数据类型：official_comap_csv。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2025/2025_Problem_D_Data.zip/2025_Problem_D_Data`。
- 行数/记录数：{'edges_drive.csv': 91227, 'nodes_drive.csv': 37163, 'Bus_Stops.csv': 2654, 'Bus_Routes.csv': 66, 'MDOT_SHA_Annual_Average_Daily_Traffic_Baltimore.csv': 2398, 'DataDictionary.csv': 111}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 安全优先级
- 策略：Prioritize pedestrian refuge, protected crossings, lighting, speed management, and bus-stop hardening where high-ridership stops overlap high traffic exposure.

#### 高暴露道路

| road_name | aadt_current | lanes | aadt_per_lane | functional_class |
|---|---|---|---|---|
| RAMP 6 FR IS 70 EB TO IS 695 SB | 42491 | 1 | 42491.0 | Interstate |
| RAMP 4 FR IS 795 NB TO MD 940 EB | 32420 | 1 | 32420.0 | Interstate |
| RAMP 4 FR IS 795 NB TO MD 940 EB | 32420 | 1 | 32420.0 | Interstate |
| BALTO BELTWAY | 221282 | 8 | 27660.25 | Interstate |
| BALTO BELTWAY | 165202 | 6 | 27533.67 | Interstate |
| BALTO BELTWAY | 188932 | 7 | 26990.29 | Interstate |
| BALTO BELTWAY | 188084 | 7 | 26869.14 | Interstate |
| BALTO BELTWAY | 161050 | 6 | 26841.67 | Interstate |
| BALTO BELTWAY | 183437 | 7 | 26205.29 | Interstate |
| FORT MCHENRY TUNNEL | 182984 | 7 | 26140.57 | Interstate |

#### 高客流公交站

| stop_name | riders_total | shelter | routes |
|---|---|---|---|
| NORTH AVE & PENNSYLVANIA AVE wb | 2527 | Yes | GD,22,85,85 |
| MONDAWMIN METRO STATION BAY 1 | 2488 | No | 22,22 |
| MONDAWMIN METRO STATION BAY 3 | 2484 | No | 29,29 |
| BALTIMORE ST & CHARLES ST eb | 1978 | Yes | RD,56,71,78,105,120,150,160,210,215,310,OR,PR |
| ROGERS AVE METRO STATION BAY 1 | 1859 | No | 80,80 |
| PRATT ST & LIGHT ST eb | 1845 | Yes | YW,54,65,76,94,154,BR,NV |
| PRATT ST & HOWARD ST eb | 1724 | Yes | YW,54,76,94,154,163,BR,NV |
| EUTAW ST & PRESTON ST fs sb | 1702 | Yes | YW,53,53,54,54,73,73,154,154,LM |
| REISTERSTOWN RD & LIBERTY HEIGHTS AVE fs sb | 1599 | Yes | LM,85 |
| SAINT PAUL ST & FAYETTE ST fs sb | 1505 | No | SV,67,76,95,103,120,210,215,310,410,411,GR |

## 模型限制
- 这是可复现的官方数据基线实验，适合做论文骨架和结果表，不应把随机森林相关性解释为严格因果。
- 对异常国家/代表队名称、教练履历、项目规则变化等，需要在竞赛论文中追加人工核验和敏感性分析。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2025/D/q06/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2025/D/q06/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2025/D/q06/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2025/D/q06`
