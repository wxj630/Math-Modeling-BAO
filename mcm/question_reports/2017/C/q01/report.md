# 2017-C q01：官方路网画像与交通流模型

## 题目原问
Build a model of traffic-flow effects using the number of lanes, peak and/or average traffic volume, and the percentage of self-driving cooperating vehicles on I-5, I-90, I-405, and SR-520.

## 适合模型
读取官方 2017_MCM_Problem_C_Data.xlsx 的 parsed mile posts 和 definitions 工作表，按 route/milepost/ADT/lanes 构造路段容量、峰小时流量、V/C ratio 和 BPR 速度函数。对应模型：交通流基本图、容量约束、BPR 延误函数、路网分段画像。

## 数据与真实性
- 数据类型：official_comap_xlsx。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2017/Problem Data- Cooperate and Navigate`。
- 行数/记录数：{'parsed mile posts': 224, 'definitions': 8}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 官方路网画像
- 路段数：224。
- 方向性总里程：183.97 miles。

#### Route summary

| route_id | route_label | segments | miles | weighted_adt_2015 | max_adt_2015 | median_lanes_per_direction | baseline_congested_segments |
|---|---|---|---|---|---|---|---|
| 5 | I-5 | 135 | 117.4 | 150329.727 | 242000 | 3.0 | 41 |
| 90 | I-90 | 27 | 23.42 | 101108.027 | 162000 | 3.0 | 2 |
| 405 | I-405 | 47 | 30.32 | 144818.602 | 195000 | 3.0 | 30 |
| 520 | SR-520 | 15 | 12.83 | 75384.256 | 109000 | 2.0 | 1 |

#### Most congested official segments

| route_id | start_milepost | end_milepost | adt_2015 | avg_lanes_per_direction | baseline_vc_ratio |
|---|---|---|---|---|---|
| 5 | 163.48 | 164.22 | 242000 | 2.5 | 1.936 |
| 5 | 163.36 | 163.48 | 238000 | 2.5 | 1.904 |
| 405 | 10.56 | 10.93 | 177000 | 2.0 | 1.77 |
| 405 | 3.3 | 3.69 | 172000 | 2.0 | 1.72 |
| 405 | 9.59 | 9.96 | 161000 | 2.0 | 1.61 |
| 405 | 6.72 | 7.2 | 154000 | 2.0 | 1.54 |
| 405 | 4.79 | 5.19 | 153000 | 2.0 | 1.53 |
| 405 | 7.69 | 8.98 | 152000 | 2.0 | 1.52 |
| 405 | 8.98 | 9.59 | 151000 | 2.0 | 1.51 |
| 405 | 5.89 | 6.34 | 148000 | 2.0 | 1.48 |

### 交通流参数与假设
- peak hour daily share：0.08。
- speed limit：60 mph。
- 人类驾驶容量假设：2000 veh/h/lane。
- AV 专用车道容量假设：3600 veh/h/lane。
- 说明：Capacity and peak-hour conversion are explicit traffic-flow assumptions applied to the official COMAP segment workbook, not observed fields in the workbook.

## 模型限制
- 这是可复现的官方 Cooperate and Navigate 交通 workbook 实验；只使用 `2017_MCM_Problem_C_Data.xlsx` 的 `parsed mile posts` 与 `definitions` 工作表，不使用随机造数。
- 峰小时占比、每车道容量、AV 容量倍率和 BPR 速度函数是显式交通流假设，用于把官方 ADT/车道数转换成可比较性能指标；正式论文应补充小时级探测器速度、OD 需求和实际 AV 行为数据校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2017/C/q01/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2017/C/q01/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2017/C/q01/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2017/C/q01`
