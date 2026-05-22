# 2017 MCM-B Merge After Toll 题面参数实验报告

## 数据来源
- 官方 PDF：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2017/Merge After Toll.pdf`。
- 官方题面参数：每方向 L 条行驶车道、B 个 barrier tollbooth，且 B > L；题面示例为 L=3、B=8。
- 本题没有独立 CSV/XLSX 附件；几何长度、容量、成本和安全权重均为显式可替换规划假设。

## Q1 形状、尺寸与并道模式
- 推荐设计：staged_zipper_merge。
- 收费亭出口车道：8；汇入行驶车道：3。
- 推荐并道长度：420.0 m；冲突指数：0.857143。

## Q2 轻/重交通性能
- 轻交通吞吐量：2400.0 veh/h。
- 重交通吞吐量：4620.0 veh/h。

## Q3 自动驾驶车辆比例敏感性
- 扫描情景数：6。

## Q4 收费亭类型比例敏感性
- 扫描情景数：4。

## New Jersey Turnpike Authority 信函
To the New Jersey Turnpike Authority:

The official 2017 MCM-B statement asks for a toll-plaza fan-in design where B tollbooths merge to L highway lanes, with the example B=8 and L=3. Our recommendation is a staged zipper merge with 420.0 meters of controlled merge distance. The design uses lane assignment and a staged zipper merge to reduce side conflicts before vehicles enter the three-lane roadway. Under light demand the modeled throughput is 2400.0 vehicles per hour; under heavy demand it reaches 4620.0 vehicles per hour before booth service and merge capacity become binding. As electronic toll collection and cooperative autonomous vehicles increase, keep the same lane-count geometry but shorten the effective merge zone only after field verification of headway compliance. This is an auditable planning model, not a replacement for site survey, crash records, or a civil-engineering design review.

## 输出文件
- `result.json`：/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/real_solutions/2017/MCM-B/result.json
- `merge_geometry.csv`：/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/real_solutions/2017/MCM-B/artifacts/merge_geometry.csv
- `traffic_performance.csv`：/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/real_solutions/2017/MCM-B/artifacts/traffic_performance.csv
- `autonomous_vehicle_sensitivity.csv`：/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/real_solutions/2017/MCM-B/artifacts/autonomous_vehicle_sensitivity.csv
- `tollbooth_mix_sensitivity.csv`：/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/real_solutions/2017/MCM-B/artifacts/tollbooth_mix_sensitivity.csv
- `merge_design_frontier.png`：/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/real_solutions/2017/MCM-B/artifacts/merge_design_frontier.png
