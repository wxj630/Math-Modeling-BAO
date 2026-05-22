# 2024-B q02：主船与救援船搜索装备准备

## 题目原问
Prepare - What, if any, additional search equipment would you recommend the company carry on the host ship to deploy if necessary? You may consider different types of equipment but must also consider costs associated with availability, maintenance, readiness, and usage of this equipment. What additional equipment might a rescue vessel need to bring in to assist if necessary?

## 适合模型
多指标装备评价：覆盖面积、探测质量、准备时间、使用成本和维护负担加权，区分主船常备设备与救援船重型设备。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted`。
- 行数/记录数：{'official_parameters': 15}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 搜索装备准备
- 模型：multi-criteria equipment scoring over coverage, detection quality, readiness, usage cost, and maintenance burden。
- 总建议：The host ship should carry acoustic localization, drop beacons, a side-scan option, and an inspection ROV; heavier lift and intervention assets can be pre-contracted for rescue-vessel arrival.

#### 主船常备装备

| asset | readiness_hours | usage_cost_index | coverage_km2_per_hour | quality | search_value_score |
|---|---|---|---|---|---|
| shipboard USBL acoustic locator | 0.25 | 2.0 | 7.5 | 0.72 | 0.5135 |
| AUV with multibeam sonar | 5.0 | 5.0 | 10.5 | 0.75 | 0.455 |
| drop transponder/LBL beacons | 0.8 | 2.8 | 4.2 | 0.8 | 0.4048 |
| side-scan sonar towfish | 1.2 | 3.3 | 5.8 | 0.68 | 0.3897 |

#### 救援船增援装备

| asset | reason |
|---|---|
| work-class ROV with lift/umbilical tools | needed for confirmed deep contact, intervention, and connection to lifting or life-support systems |
| dynamic-positioning rescue vessel | keeps the rescue platform over the contact while operating tethered tools |
| medical decompression and survivor reception team | turns a location success into safe recovery and post-rescue care |

## 模型限制
- 这是可复现的官方题面参数搜索救援实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中的任务约束和显式确定性预案参数。
- 洋流、装备覆盖率和准备时间是可替换的场景参数，不是事故观测数据；正式论文应接入作业海区实时流场、测深、声学设备规格和演练记录校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2024/B/q02/solution.py`

## 输出
- `mcm/question_results/2024/B/q02/result.json`
- `mcm/question_reports/2024/B/q02/report.md`
- `mcm/question_artifacts/2024/B/q02`
