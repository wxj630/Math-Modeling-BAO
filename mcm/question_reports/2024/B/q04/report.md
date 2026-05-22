# 2024-B q04：加勒比海迁移、多潜水器协调与希腊政府备忘录

## 题目原问
Extrapolate - How might your model be expanded to account for other tourist destinations such as the Caribbean Sea? How will your model change to account for multiple submersibles moving in the same general vicinity? Prepare a two-page memo addressed to the Greek government to help win approval.

## 适合模型
对加勒比海增大洋流和地形不确定性倍数；多潜水器用唯一声学编码、Voronoi 后验分区和资源冲突约束；输出给 Greek government 的审批备忘录。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted`。
- 行数/记录数：{'official_parameters': 15}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 搜索部署与发现概率
- 模型：Bayesian-style survival update with deterministic swept-area coverage over the official location-model uncertainty ellipse。
- 发现概率公式：`P_found(t)=1-exp(-sum_over_intervals(incremental_effective_swept_area/current_uncertainty_area))`。
- 12 小时发现概率：0.7489。
- 24 小时发现概率：0.7812。

#### 初始部署点

| point | east_km | north_km | purpose |
|---|---|---|---|
| P0 predicted center | 2.509 | 1.567 | deploy USBL and first drop beacon |
| P1 down-current ellipse focus | 4.113 | 2.57 | start creeping-line sonar along drift axis |
| P2 up-current ellipse focus | 1.422 | 0.888 | backtrack possible powerless descent path |
| P3 cross-current high-uncertainty edge | 3.238 | 0.399 | cover terrain and density-current ambiguity |
| P4 opposite cross-current edge | 1.779 | 2.736 | complete LBL bracket and close acoustic geometry |

#### 搜索模式

- 0-2 h: interrogate acoustic pingers from the host ship and deploy two LBL beacons around P0/P1
- 2-8 h: run creeping-line side-scan sonar along the drift-axis ellipse from P1 to P2
- 8-16 h: use ROV to inspect acoustic/sonar contacts and seafloor terrain traps
- 16-24 h: add AUV expanding-square search around remaining posterior mass if no confirmed contact

### 迁移到加勒比海与多潜水器
- 加勒比海洋流不确定性倍数：1.35。
- 地形调整：replace Ionian seafloor-wreck bathymetry with reef wall, trench, and strong surface-current layers。
- 通信调整：predefine tourist-route LBL boxes because warm shallow shelves may create more multipath and recreational vessel noise。
- 多潜水器协调规则：assign each submersible a unique acoustic code, maintain non-overlapping safety corridors, and partition the search posterior into Voronoi sectors around last confirmed fixes。
- 模型变化：state vector becomes one ellipse per submersible plus a collision/communication interference constraint matrix。

### 给 Greek government 的审批备忘录
Memo to the Greek government: MCMS approval should require an auditable lost-submersible plan with periodic acoustic telemetry, a host-ship localization kit, preplanned deployment points, a probability-updated search log, and a rescue-vessel mobilization trigger when the 12-hour posterior still leaves substantial uncertainty.

## 模型限制
- 这是可复现的官方题面参数搜索救援实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中的任务约束和显式确定性预案参数。
- 洋流、装备覆盖率和准备时间是可替换的场景参数，不是事故观测数据；正式论文应接入作业海区实时流场、测深、声学设备规格和演练记录校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2024/B/q04/solution.py`

## 输出
- `mcm/question_results/2024/B/q04/result.json`
- `mcm/question_reports/2024/B/q04/report.md`
- `mcm/question_artifacts/2024/B/q04`
