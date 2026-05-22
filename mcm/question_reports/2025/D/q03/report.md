# 2025-D q03：推荐项目对居民的收益

## 题目原问
Recommend a project for the transportation network that best improves residents' lives. What are the benefits to residents?

## 适合模型
综合桥梁韧性和高客流公交站升级，量化直接连通性恢复和无候车亭高客流覆盖。

## 数据与真实性
- 数据类型：official_comap_csv。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted/2025/2025_Problem_D_Data.zip/2025_Problem_D_Data`。
- 行数/记录数：{'edges_drive.csv': 91227, 'nodes_drive.csv': 37163, 'Bus_Stops.csv': 2654, 'Bus_Routes.csv': 66, 'MDOT_SHA_Annual_Average_Daily_Traffic_Baltimore.csv': 2398, 'DataDictionary.csv': 111}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 桥梁坍塌/重建影响
- 移除桥梁走廊边数：12。
- 移除桥梁走廊总长度：12.981 km。
- 断连 OD 数：1。
- 最大额外比例：0.0%。

| od_pair | status_after_removal | baseline_km | collapse_km | extra_km | extra_pct |
|---|---|---|---|---|---|
| Key Bridge west-east approaches | disconnected | 13.083 | None | None | None |
| Port to Dundalk | connected | 59.505 | 59.505 | 0.0 | 0.0 |
| Southwest Gateway to Dundalk | connected | 57.19 | 57.19 | 0.0 | 0.0 |
| Downtown to Port | connected | 9.3 | 9.3 | 0.0 | 0.0 |
| Mondawmin to Port jobs | connected | 13.748 | 13.748 | 0.0 | 0.0 |
| Rogers Ave to Inner Harbor | connected | 10.565 | 10.565 | 0.0 | 0.0 |

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

### 项目收益、利益相关者与扰动

#### Rebuild and harden the Francis Scott Key / I-695 harbor crossing corridor.
- 主要收益：Restores direct connectivity for Key Bridge west-east approaches under the removal scenario.
- 居民收益：Improves access between port-adjacent jobs, east/south neighborhoods, and regional highways.
- 其他利益相关者：Port freight, commuters, emergency services, and pass-through traffic gain reliability; construction staging creates short-run delays.
- 扰动：Major capital cost, detours, construction noise, and possible induced traffic unless paired with transit and safety improvements.
#### Install shelters, lighting, ADA boarding pads, and bus-priority curb management at the highest-ridership unsheltered stops.
- 主要收益：Targets 16266 boardings/alightings at the top 10 unsheltered high-ridership stops.
- 居民收益：Benefits bus-dependent residents directly through weather protection, safer waiting areas, and more reliable boarding.
- 其他利益相关者：Transit agency operations improve, nearby businesses may gain foot traffic, drivers may face curb-management changes.
- 扰动：Temporary sidewalk work, curb reallocation, and potential parking/loading conflicts near priority stops.

## 模型限制
- 这是可复现的官方数据基线实验，适合做论文骨架和结果表，不应把随机森林相关性解释为严格因果。
- 对异常国家/代表队名称、教练履历、项目规则变化等，需要在竞赛论文中追加人工核验和敏感性分析。

## 运行方式
`.venv/bin/python mcm/question_solutions/2025/D/q03/solution.py`

## 输出
- `mcm/question_results/2025/D/q03/result.json`
- `mcm/question_reports/2025/D/q03/report.md`
- `mcm/question_artifacts/2025/D/q03`
