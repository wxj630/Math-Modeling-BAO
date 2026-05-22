# 2016 MCM-A A Hot Bath 题面参数实验报告

## 数据来源
- 官方 PDF：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2016/A Hot Bath.pdf`。
- 本题没有独立 CSV/XLSX 附件；模型只使用题面的物理约束：单水龙头、简单浴缸、无循环加热、热水恒定细流、满水后溢流排出。
- 浴缸尺寸、热损失、人体体积/温度、泡泡浴隔热系数都是显式可替换假设。

## Q1 温度空间-时间模型与最优策略
- 推荐流量：1.75 L/min。
- 推荐动作：active_stirring。
- 40 分钟溢流水量：70.0 L。
- 平均温度误差：2.5759 C；平均空间温差：7.6766 C。

## Q2 形状、人体和动作敏感性
- 长浅浴缸表面积更大，散热和空间不均匀更明显。
- 人体增加排水体积并与水换热，较冷或较大体型需要更多热水或动作混合。
- 主动搅动降低空间温差，但现实中舒适性和安全性限制其强度。

## Q3 泡泡浴影响
- 解释：Bubble bath suppresses surface heat loss but can also suppress natural surface mixing; this experiment isolates the insulating effect and keeps motion fixed.

## Q4 给浴缸用户的一页说明
For a simple bathtub, the practical strategy is a small continuous trickle of hot water plus gentle motion. In the baseline scenario the model selects about 1.75 L/min with active_stirring, wasting about 70.0 L over a 40 minute bath. Hot water enters near the faucet, cooler water leaves near the overflow, and heat is constantly lost to air, tub walls, and the bather, so perfectly uniform temperature is physically difficult. Gentle stirring matters because it reduces hot and cold spots without requiring a much larger overflow. Bubble bath helps by insulating the surface, but it should not replace mixing.

## 输出文件
- `result.json`：/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/real_solutions/2016/MCM-A/result.json
- `temperature_strategy_grid.csv`：/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/real_solutions/2016/MCM-A/artifacts/temperature_strategy_grid.csv
- `tub_shape_sensitivity.csv`：/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/real_solutions/2016/MCM-A/artifacts/tub_shape_sensitivity.csv
- `bubble_bath_sensitivity.csv`：/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/real_solutions/2016/MCM-A/artifacts/bubble_bath_sensitivity.csv
- `temperature_profiles.png`：/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/real_solutions/2016/MCM-A/artifacts/temperature_profiles.png
