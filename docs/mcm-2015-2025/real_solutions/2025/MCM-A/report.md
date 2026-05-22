# 2025 MCM-A Testing Time: The Constant Wear On Stairs

## 数据真实性
- 官方来源：`docs/mcm-2015-2025/official_assets_extracted/2025/2025_MCM_Problem_A.pdf`。
- 本题无官方数值附件；代码只使用官方题面约束、显式测量模板和确定性 worked example 反演，不使用随机占位数据。
- `worked_example_assumptions` 只演示考古队填完测量表后如何反推，不冒充实际楼梯观测。

## 非破坏测量
- 工具：卷尺、直尺/塞尺、卡尺、手机倾角仪、比例照片、便携硬度/密度代理测量、目视补丁评分。
- 输出：`measurement_template.csv`、`wear_profile.csv`、`wear_cross_section.png`。

## 每问建模与结果

### Q1 使用频率
- 模型：inverse Archard-style wear balance: passages = observed_depth / material_wear_rate。
- 结果：估计每级踏步累计通行 9555556 次，日均使用 72.67 人。

### Q2 行进方向
- 模型：front/back edge rounding asymmetry plus along-tread slope sign。
- 结果：front/back 圆角比 1.497，偏好方向 `up`。

### Q3 同时使用
- 模型：cross-sectional wear-band shape: center-dominant versus side-band wear。
- 结果：侧带/中心磨损比 0.526，模式 `mixed`。

### Q4 与历史信息一致性
- 结论：mostly consistent, with one likely repaired tread that should be excluded or down-weighted in final age inference。

### Q5 年龄与可靠性
- 年龄估计：340.3 年。
- 合理区间：[283.6, 397.0] 年。
- 可靠性：medium: age is identifiable only jointly with material wear rate and daily traffic prior。

### Q6 维修或翻新
- 候选数：2。
- 详见 `renovation_candidates.csv`。

### Q7 材料来源
- 指导：compare non-destructive hardness/density proxies and observed wear rate against candidate quarry or timber reference samples。

### Q8 典型日使用模式
- 估计峰值期使用占比：0.376。
- 判断：mixed ceremonial peaks plus regular low-intensity circulation。

## 运行方式
`.venv/bin/python docs/mcm-2015-2025/real_solutions/2025/MCM-A/solution.py`
