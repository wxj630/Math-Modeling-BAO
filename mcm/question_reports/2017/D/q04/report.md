# 2017-D q04：安全经理政策建议、验证和未来工作

## 题目原问
Propose policy and procedural recommendations for security managers based on your model. Validate the model, assess strengths and weaknesses, and propose ideas for improvement.

## 适合模型
将瓶颈、流程修改和文化敏感性结果整理为 TSA security managers memo，并明确官方样本规模、无随机造数、缺少小时级真实速度/成本数据等验证限制。对应模型：政策决策报告、模型验证、局限性分析。

## 数据与真实性
- 数据类型：official_comap_xlsx。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2017/Problem Data- Airport Security Checkpoint`。
- 行数/记录数：{'Sheet1': 58}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

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

### 文化/旅客风格敏感性
- 方法：Deterministic one-at-a-time multipliers on official process samples; traveler styles are sensitivity scenarios, not observed cultures in the workbook.

| traveler_style | property_multiplier | id_multiplier | combined_mean_wait_s | combined_p90_wait_s | description |
|---|---|---|---|---|---|
| personal-space cautious | 1.25 | 1.05 | 1224.9903 | 3041.7233 | More spacing and slower divestment/reclaim behavior. |
| collective-efficiency | 0.85 | 0.95 | 859.504857 | 2199.2409 | Passengers coordinate bins and move when prompted. |
| individual-fast but variable | 0.95 | 1.0 | 955.20771 | 2421.6731 | Faster median but less orderly behavior; modeled here without random variance. |

### TSA security manager memo
To TSA security managers: the official checkpoint workbook points to Zone B/C preparation and scanner/x-ray headways as the most visible sources of high-tail service time. Keep the security standard fixed, but reduce variance by staffing divestment support, improving bin flow, and dynamically balancing PreCheck versus regular lanes when observed demand differs from the legacy one-to-three lane ratio. Cultural or traveler-style differences should be handled with clearer signs, parallel preparation space, and queue marshals rather than by lowering screening intensity.

## 模型限制
- 这是可复现的官方 Airport Security Checkpoint workbook 实验；只使用 `2017_ICM_Problem_D_Data.xlsx` 的 Sheet1 到达和过程样本，不使用随机造数。
- 排队仿真是按官方样本确定性回放；PreCheck 加速、取物时间归一化、文化/旅客风格乘数和流程修改均为显式假设，正式论文应补充小时级真实排队、成本、安检失败率和多机场数据校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2017/D/q04/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2017/D/q04/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2017/D/q04/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2017/D/q04`
