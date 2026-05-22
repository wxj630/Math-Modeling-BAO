# 2017-D q01：安检流程排队模型与瓶颈识别

## 题目原问
Develop one or more model(s) that allow(s) you to explore the flow of passengers through a security check point and identify bottlenecks. Clearly identify where problem areas exist in the current process.

## 适合模型
读取官方 2017_ICM_Problem_D_Data.xlsx 的 TSA Pre-Check/Regular 到达时间、ID 检查、毫米波、X-ray 和取物样本，构造确定性 G/G/c 排队模型；基线采用题面 one PreCheck lane for every three regular lanes。对应模型：排队论、离散事件仿真、瓶颈分析。

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

## 模型限制
- 这是可复现的官方 Airport Security Checkpoint workbook 实验；只使用 `2017_ICM_Problem_D_Data.xlsx` 的 Sheet1 到达和过程样本，不使用随机造数。
- 排队仿真是按官方样本确定性回放；PreCheck 加速、取物时间归一化、文化/旅客风格乘数和流程修改均为显式假设，正式论文应补充小时级真实排队、成本、安检失败率和多机场数据校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2017/D/q01/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2017/D/q01/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2017/D/q01/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2017/D/q01`
