# 2017-D q02：两类以上流程修改实验

## 题目原问
Develop two or more potential modifications to the current process to improve passenger throughput and reduce variance in wait time. Model these changes to demonstrate how your modifications impact the process.

## 适合模型
比较 2 PreCheck/2 regular 动态车道重平衡、并行取筐/物品准备支持、混合方案三类确定性场景，以 combined mean wait、p90 wait 和 checkpoint clear time 评价。对应模型：方案仿真、多指标比较、服务系统优化。

## 数据与真实性
- 数据类型：official_comap_xlsx。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2017/Problem Data- Airport Security Checkpoint`。
- 行数/记录数：{'Sheet1': 58}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 安检基线排队模型
- PreCheck lanes：1；regular lanes：3。
- combined mean wait：998.732971 s。
- combined p90 wait：2521.0776 s。
- checkpoint clear time：3908.2765 s。

#### Queue metrics

| queue | servers | passenger_count | mean_wait_s | p90_wait_s | max_wait_s | mean_service_s | last_finish_s |
|---|---|---|---|---|---|---|---|
| precheck | 1 | 58 | 1577.992103 | 2945.2368 | 3169.007 | 67.384078 | 3908.2765 |
| regular | 3 | 47 | 283.902553 | 596.03 | 696.51 | 89.751915 | 3659.41 |

### 瓶颈分析
- Highest p90 process time: property divest/reclaim (114.4 s).
- Largest queue p90 wait: precheck lane.

#### Stage service summary

| stage | median_s | p90_s |
|---|---|---|
| property divest/reclaim | 28.0 | 114.4 |
| x-ray belt headway | 2.35 | 15.548 |
| millimeter wave scanner headway | 11.0 | 15.532 |
| ID check | 10.995 | 15.11 |

### 流程修改实验

| modification | precheck_lanes | regular_lanes | combined_mean_wait_s | combined_p90_wait_s | mean_wait_change_vs_baseline_s | p90_wait_change_vs_baseline_s | checkpoint_clear_time_s |
|---|---|---|---|---|---|---|---|
| hybrid: 2 PreCheck lanes plus divestment support | 2 | 2 | 460.08599 | 889.81664 | -538.646981 | -1631.26096 | 3650.319 |
| rebalance lanes to 2 PreCheck / 2 regular | 2 | 2 | 612.918324 | 1179.9978 | -385.814647 | -1341.0798 | 3659.41 |
| parallel divestment support and bin preparation | 1 | 3 | 777.44832 | 2009.34959 | -221.284651 | -511.72801 | 3650.319 |

## 模型限制
- 这是可复现的官方 Airport Security Checkpoint workbook 实验；只使用 `2017_ICM_Problem_D_Data.xlsx` 的 Sheet1 到达和过程样本，不使用随机造数。
- 排队仿真是按官方样本确定性回放；PreCheck 加速、取物时间归一化、文化/旅客风格乘数和流程修改均为显式假设，正式论文应补充小时级真实排队、成本、安检失败率和多机场数据校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2017/D/q02/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2017/D/q02/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2017/D/q02/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2017/D/q02`
