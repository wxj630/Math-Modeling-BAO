# 2017 MCM-C Cooperate and Navigate：官方交通 workbook 实验报告

## 数据来源
- 官方题面：`docs/mcm-2015-2025/official_assets_extracted/2017/Cooperate and Navigate.pdf`。
- 官方 workbook：`docs/mcm-2015-2025/official_assets_extracted/2017/Problem Data- Cooperate and Navigate/2017_MCM_Problem_C_Data.xlsx`。
- `parsed mile posts` 行数：224。
- `definitions` 行数：8。
- 本实验不使用随机生成的 x1/x2/x3 数据；10%、50%、90% 是题目要求讨论的自动驾驶渗透率情景。

## 路网画像
| route | miles | weighted ADT | max ADT | baseline congested segments |
|---|---:|---:|---:|---:|
| I-5 | 117.4 | 150329.727 | 242000 | 41 |
| I-90 | 23.42 | 101108.027 | 162000 | 2 |
| I-405 | 30.32 | 144818.602 | 195000 | 30 |
| SR-520 | 12.83 | 75384.256 | 109000 | 1 |

## 自动驾驶渗透率情景
| AV share | capacity multiplier | congested share | peak vehicle-hours | saved vs baseline | median speed |
|---:|---:|---:|---:|---:|---:|
| 0.0 | 1.0 | 0.330357 | 19781.936124 | 0.0 | 55.335212 |
| 0.1 | 1.0345 | 0.276786 | 19418.392267 | 363.543857 | 55.886466 |
| 0.5 | 1.3625 | 0.066964 | 17747.961637 | 2033.974487 | 58.56735 |
| 0.9 | 1.9945 | 0.0 | 17097.567118 | 2684.369005 | 59.682065 |

## 临界点与专用车道
- 临界点定义：first AV share where total peak vehicle-hours are at least 10% below the all-human baseline。
- 临界 AV share：0.49。
- 专用车道规则：Do not reserve scarce two-lane facilities. Pilot one AV-only lane only on >=3 lane-per-direction segments when AV demand is at least 50% and modeled vehicle-hours beat mixed traffic.
- 候选路段数：0。

## 给州长的建议摘要
To the Governor: the official 2017 MCM-C traffic workbook shows that the I-5/I-90/I-405/SR-520 corridor has many segments near or above a volume-capacity ratio of one under a simple peak-hour model. At 10% automated vehicles, the benefit is modest and should be handled in mixed traffic. Around the modeled tipping point, cooperative vehicles begin reducing total peak vehicle-hours materially. Dedicated AV lanes should therefore be piloted only on high-volume corridors with at least three lanes per direction and at least 50% AV demand; otherwise, taking a lane away from human drivers can make congestion worse.

## 产物
- `clean_traffic_segments.csv`
- `adoption_scenario_summary.csv`
- `adoption_segment_profiles.csv`
- `dedicated_lane_candidates.csv`
- `route_congestion_profiles.png`
