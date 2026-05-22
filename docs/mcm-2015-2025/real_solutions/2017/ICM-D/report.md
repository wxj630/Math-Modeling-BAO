# 2017 ICM-D Airport Security Checkpoint：官方 TSA workbook 实验报告

## 数据来源
- 官方题面：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2017/Optimizing Passenger Throughput at an Airport Security Checkpoint.pdf`。
- 官方 workbook：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2017/Problem Data- Airport Security Checkpoint/2017_ICM_Problem_D_Data.xlsx`。
- Sheet1 行数：58。
- PreCheck 到达样本：58；Regular 到达样本：47。
- 本实验不使用随机生成的 x1/x2/x3；文化和流程改变是显式确定性敏感性情景。

## 基线排队结果
- PreCheck lanes：1；regular lanes：3。
- combined mean wait：998.732971 s。
- combined p90 wait：2521.0776 s。

## 瓶颈
- Highest p90 process time: property divest/reclaim (114.4 s).
- Largest queue p90 wait: precheck lane.

## 流程修改实验
| modification | mean wait | p90 wait | p90 change | rationale |
|---|---:|---:|---:|---|
| hybrid: 2 PreCheck lanes plus divestment support | 460.08599 | 889.81664 | -1631.26096 | Combines lane balance with process support; included as a transparent upper-bound operational scenario. |
| rebalance lanes to 2 PreCheck / 2 regular | 612.918324 | 1179.9978 | -1341.0798 | Problem statement says 45% are PreCheck but often only one PreCheck lane for every three regular lanes. |
| parallel divestment support and bin preparation | 777.44832 | 2009.34959 | -511.72801 | Reduce Zone B/C property preparation variance without lowering security standards. |

## 文化/旅客风格敏感性
| style | mean wait | p90 wait | description |
|---|---:|---:|---|
| personal-space cautious | 1224.9903 | 3041.7233 | More spacing and slower divestment/reclaim behavior. |
| collective-efficiency | 859.504857 | 2199.2409 | Passengers coordinate bins and move when prompted. |
| individual-fast but variable | 955.20771 | 2421.6731 | Faster median but less orderly behavior; modeled here without random variance. |

## 给安检管理者的建议
To TSA security managers: the official checkpoint workbook points to Zone B/C preparation and scanner/x-ray headways as the most visible sources of high-tail service time. Keep the security standard fixed, but reduce variance by staffing divestment support, improving bin flow, and dynamically balancing PreCheck versus regular lanes when observed demand differs from the legacy one-to-three lane ratio. Cultural or traveler-style differences should be handled with clearer signs, parallel preparation space, and queue marshals rather than by lowering screening intensity.
