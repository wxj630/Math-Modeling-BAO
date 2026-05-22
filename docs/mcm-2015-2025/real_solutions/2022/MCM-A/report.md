# 2022 MCM-A Power Profile of a Cyclist

## 数据真实性
- 官方来源：`docs/mcm-2015-2025/official_assets/2022/Power Profile of a Cyclist`。
- 本题无 COMAP 数值附件；脚本只使用官方题面要求和透明确定性骑手/赛道参数，不使用随机占位数据。

## 骑手功率模型
- 模型：critical-power curve with finite above-threshold work capacity and aerodynamic rider parameters。
- 覆盖 time trial specialist 与 climber-puncheur 两类骑手，并分别给出男女 profile。

## 赛道策略
- 指导案例：male time trial specialist / 2021 Olympic Time Trial course in Tokyo / 42.14 min。
- 方法：segment-by-segment power targeting with energy budget, grade, turns, aerodynamic drag, and accumulated high-power load。

## 敏感性与团队计时赛扩展
- 天气方法：repeat the same segment power plan under tailwind, calm, and headwind conditions scaled by segment wind exposure。
- 功率偏差方法：deterministic plus/minus target-power perturbation around the guidance plan。
- 团队计时赛：6 名车手，第 4 名过线计时。

## Directeur Sportif 指导
Directeur Sportif race guidance: use the Tokyo plan as a power corridor rather than a rigid second-by-second script. For the male time trial specialist, the target ride is 42.14 minutes over 31.6 km with an energy margin of 3343.62 kJ. Hold steady aero power on flat exposed sectors, allow controlled over-threshold work on climbs and exits from sharp turns, and recover on descents without letting speed collapse. If headwind rises, widen split targets on exposed sectors first; if the rider is more than 4% above target power early, call for immediate recovery because the high-power load grows faster than the time gain.

## 输出产物
- `rider_power_profiles.csv`：两类骑手和性别 profile 的功率曲线。
- `course_strategy_results.csv`：三条路线、四个 profile 的完赛时间与能量预算。
- `course_segment_power_plan.csv`：逐段目标功率、速度、用时和能量。
- `weather_sensitivity.csv`：风速扰动敏感性。
- `target_power_deviation.csv`：目标功率偏差敏感性。
- `power_course_frontier.png`：赛道长度与预测时间权衡图。
