# 2025-D q05：项目扰动和实施代价

## 题目原问
Explain the ways the project disrupts other transportation needs and people's lives.

## 适合模型
用项目建议中的 construction/capital/curb trade-off 字段，列出施工、绕行、停车装卸和人行道施工扰动。

## 数据与真实性
- 数据类型：official_comap_csv。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2025/2025_Problem_D_Data.zip/2025_Problem_D_Data`。
- 行数/记录数：{'edges_drive.csv': 91227, 'nodes_drive.csv': 37163, 'Bus_Stops.csv': 2654, 'Bus_Routes.csv': 66, 'MDOT_SHA_Annual_Average_Daily_Traffic_Baltimore.csv': 2398, 'DataDictionary.csv': 111}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

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
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2025/D/q05/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2025/D/q05/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2025/D/q05/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2025/D/q05`
