# 2025-D q01：Key Bridge 坍塌/重建的路网影响

## 题目原问
What does the network model show is the impact of the Francis Scott Key Bridge collapse and/or reconstruction on Baltimore transportation stakeholders?

## 适合模型
基于官方驾车路网构建加权有向图，移除 I-695/Baltimore Beltway 港口桥梁走廊边，比较关键 OD 最短路和断连状态。

## 数据与真实性
- 数据类型：official_comap_csv。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2025/2025_Problem_D_Data.zip/2025_Problem_D_Data`。
- 行数/记录数：{'edges_drive.csv': 91227, 'nodes_drive.csv': 37163, 'Bus_Stops.csv': 2654, 'Bus_Routes.csv': 66, 'MDOT_SHA_Annual_Average_Daily_Traffic_Baltimore.csv': 2398, 'DataDictionary.csv': 111}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 路网规模
- 驾车节点：37162。
- 驾车边：89958。
- 最大弱连通分量节点：37162。
- 公交线路：66，公交站：2654。

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

## 模型限制
- 这是可复现的官方数据基线实验，适合做论文骨架和结果表，不应把随机森林相关性解释为严格因果。
- 对异常国家/代表队名称、教练履历、项目规则变化等，需要在竞赛论文中追加人工核验和敏感性分析。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2025/D/q01/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2025/D/q01/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2025/D/q01/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2025/D/q01`
