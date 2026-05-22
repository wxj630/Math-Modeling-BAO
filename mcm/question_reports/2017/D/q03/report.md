# 2017-D q03：文化规范与旅客风格敏感性

## 题目原问
Consider how cultural norms may impact the way in which passengers process through checkpoints as a sensitivity analysis. How can the security system accommodate these differences in a manner that expedites passenger throughput and reduces variance?

## 适合模型
在官方流程样本上施加 personal-space cautious、collective-efficiency、individual-fast but variable 三类确定性乘数，说明这些是旅客风格敏感性而非 workbook 中的文化观测。对应模型：敏感性分析、情景参数、服务时间扰动。

## 数据与真实性
- 数据类型：official_comap_xlsx。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted/2017/Problem Data- Airport Security Checkpoint`。
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

### 文化/旅客风格敏感性
- 方法：Deterministic one-at-a-time multipliers on official process samples; traveler styles are sensitivity scenarios, not observed cultures in the workbook.

| traveler_style | property_multiplier | id_multiplier | combined_mean_wait_s | combined_p90_wait_s | description |
|---|---|---|---|---|---|
| personal-space cautious | 1.25 | 1.05 | 1224.9903 | 3041.7233 | More spacing and slower divestment/reclaim behavior. |
| collective-efficiency | 0.85 | 0.95 | 859.504857 | 2199.2409 | Passengers coordinate bins and move when prompted. |
| individual-fast but variable | 0.95 | 1.0 | 955.20771 | 2421.6731 | Faster median but less orderly behavior; modeled here without random variance. |

## 模型限制
- 这是可复现的官方 Airport Security Checkpoint workbook 实验；只使用 `2017_ICM_Problem_D_Data.xlsx` 的 Sheet1 到达和过程样本，不使用随机造数。
- 排队仿真是按官方样本确定性回放；PreCheck 加速、取物时间归一化、文化/旅客风格乘数和流程修改均为显式假设，正式论文应补充小时级真实排队、成本、安检失败率和多机场数据校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2017/D/q03/solution.py`

## 输出
- `mcm/question_results/2017/D/q03/result.json`
- `mcm/question_reports/2017/D/q03/report.md`
- `mcm/question_artifacts/2017/D/q03`
