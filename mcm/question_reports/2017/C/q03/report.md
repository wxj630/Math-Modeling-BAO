# 2017-C q03：均衡与性能突变临界点

## 题目原问
Determine whether equilibria exist and whether there is a tipping point where performance changes markedly.

## 适合模型
把总峰小时 vehicle-hours 作为系统性能指标，在 0%-100% AV share 网格上寻找首次比全人类驾驶基线降低 10% 的临界点，并解释该点附近的容量反馈。对应模型：离散均衡扫描、阈值分析、系统性能曲线。

## 数据与真实性
- 数据类型：official_comap_xlsx。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted/2017/Problem Data- Cooperate and Navigate`。
- 行数/记录数：{'parsed mile posts': 224, 'definitions': 8}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 10%/50%/90% 自动驾驶渗透率情景
- 模型：BPR speed model with deterministic AV capacity multiplier: 1 + 1.20*p^2 + 0.25*p*(1-p).

| av_share | capacity_multiplier | mean_vc_ratio | congested_segment_share_vc_gt_1 | total_peak_vehicle_hours | vehicle_hours_saved_vs_baseline | median_speed_mph |
|---|---|---|---|---|---|---|
| 0.0 | 1.0 | 0.858012 | 0.330357 | 19781.936124 | 0.0 | 55.335212 |
| 0.1 | 1.0345 | 0.829398 | 0.276786 | 19418.392267 | 363.543857 | 55.886466 |
| 0.5 | 1.3625 | 0.629734 | 0.066964 | 17747.961637 | 2033.974487 | 58.56735 |
| 0.9 | 1.9945 | 0.430189 | 0.0 | 17097.567118 | 2684.369005 | 59.682065 |

### 性能临界点
- 判据：first AV share where total peak vehicle-hours are at least 10% below the all-human baseline
- AV share：0.49。
- baseline peak vehicle-hours：19781.936124。
- target peak vehicle-hours：17803.742512。
- achieved peak vehicle-hours：17777.667893。

## 模型限制
- 这是可复现的官方 Cooperate and Navigate 交通 workbook 实验；只使用 `2017_MCM_Problem_C_Data.xlsx` 的 `parsed mile posts` 与 `definitions` 工作表，不使用随机造数。
- 峰小时占比、每车道容量、AV 容量倍率和 BPR 速度函数是显式交通流假设，用于把官方 ADT/车道数转换成可比较性能指标；正式论文应补充小时级探测器速度、OD 需求和实际 AV 行为数据校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2017/C/q03/solution.py`

## 输出
- `mcm/question_results/2017/C/q03/result.json`
- `mcm/question_reports/2017/C/q03/report.md`
- `mcm/question_artifacts/2017/C/q03`
