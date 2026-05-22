# 2025 ICM-D A Roadmap to a Better City 真实数据解法

## 数据来源
- 使用 COMAP 官方 `2025_Problem_D_Data.zip` 解压出的路网、公交站、公交线路和 AADT 交通量 CSV。
- 没有使用随机生成交通流或虚构站点。

## 网络模型
- 驾车路网节点：37162，边：89958。
- 公交站：2654，公交线路：66。
- AADT 交通量记录：2398。

## Q1 桥梁坍塌/重建影响
- 识别 I-695/Baltimore Beltway 港口桥梁走廊边数：12。
- 样本 OD 平均额外距离：0.0 km，最大额外比例：0.0%，断连 OD 数：1。

| OD | status | baseline km | collapse km | extra km | extra % |
|---|---|---:|---:|---:|---:|
| Key Bridge west-east approaches | disconnected | 13.083 | None | None | None |
| Port to Dundalk | connected | 59.505 | 59.505 | 0.0 | 0.0 |
| Southwest Gateway to Dundalk | connected | 57.19 | 57.19 | 0.0 | 0.0 |
| Downtown to Port | connected | 9.3 | 9.3 | 0.0 | 0.0 |
| Mondawmin to Port jobs | connected | 13.748 | 13.748 | 0.0 | 0.0 |
| Rogers Ave to Inner Harbor | connected | 10.565 | 10.565 | 0.0 | 0.0 |

## Q2 公交/步行项目
- 推荐项目：Install shelters, lighting, ADA boarding pads, and bus-priority curb management at the highest-ridership unsheltered stops.
- 无候车亭站点：2295 / 2654。
- 前 10 个高客流无候车亭站点覆盖客流：16266。

| stop | riders | routes | nearest node |
|---|---:|---:|---:|
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

## Q3-Q5 推荐项目、收益、利益相关者与扰动
### Rebuild and harden the Francis Scott Key / I-695 harbor crossing corridor.
- 主要收益：Restores direct connectivity for Key Bridge west-east approaches under the removal scenario.
- 居民收益：Improves access between port-adjacent jobs, east/south neighborhoods, and regional highways.
- 其他利益相关者：Port freight, commuters, emergency services, and pass-through traffic gain reliability; construction staging creates short-run delays.
- 扰动：Major capital cost, detours, construction noise, and possible induced traffic unless paired with transit and safety improvements.
### Install shelters, lighting, ADA boarding pads, and bus-priority curb management at the highest-ridership unsheltered stops.
- 主要收益：Targets 16266 boardings/alightings at the top 10 unsheltered high-ridership stops.
- 居民收益：Benefits bus-dependent residents directly through weather protection, safer waiting areas, and more reliable boarding.
- 其他利益相关者：Transit agency operations improve, nearby businesses may gain foot traffic, drivers may face curb-management changes.
- 扰动：Temporary sidewalk work, curb reallocation, and potential parking/loading conflicts near priority stops.

## Q6 安全策略
- Prioritize pedestrian refuge, protected crossings, lighting, speed management, and bus-stop hardening where high-ridership stops overlap high traffic exposure.

| road | AADT | lanes | AADT/lane | class |
|---|---:|---:|---:|---|
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

## Q7 给市长的一页备忘录摘要
Mayor, the model recommends a paired program: rebuild and harden the I-695 harbor crossing to restore regional freight/emergency redundancy, while immediately funding bus-stop safety upgrades at the highest-ridership unsheltered stops. The bridge project protects port access and regional reliability but causes construction disruption; the transit project directly helps daily residents at modest scale, with curb and sidewalk tradeoffs. Safety benefits are strongest if both projects include lighting, refuge crossings, speed management, and bus-priority curb design.

## 输出文件
- `result.json`：结构化结果。
- `artifacts/bridge_od_impacts.csv/png`：桥梁走廊移除 OD 影响。
- `artifacts/priority_bus_stops.csv/png`：公交站项目优先级。
- `artifacts/high_exposure_roads.csv`：高安全暴露道路。
