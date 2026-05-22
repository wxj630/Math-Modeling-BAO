# 2025-A q04：磨损与历史信息一致性

## 题目原问
Is the wear consistent with the information available?

## 适合模型
把日均使用人数、候选年龄区间、中心通行槽、补丁边界和相邻踏步突变放入一致性检查表，识别需要降权的维修踏步。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted`。
- 行数/记录数：{'official_parameters': 3}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 磨损反演结果
#### 使用频率
- 模型：inverse Archard-style wear balance: passages = observed_depth / material_wear_rate。
- 中心磨损中位数：4.3 mm。
- 累计通行量：9555556。
- 日均使用人数：72.67。

#### 方向偏好
- 模型：front/back edge rounding asymmetry plus along-tread slope sign。
- 前/后缘圆角比：1.497。
- 偏好方向：up。

#### 同时使用
- 模型：cross-sectional wear-band shape: center-dominant versus side-band wear。
- 侧带/中心磨损比：0.526。
- 模式：mixed。

### 一致性检查
- 总体判断：mostly consistent, with one likely repaired tread that should be excluded or down-weighted in final age inference。
- 建议：run the inverse model twice: once with all treads and once excluding high patch-boundary treads; compare the age/traffic interval overlap。

| check | value |
|---|---|
| central_channel_expected_for_long_term_public_stairs | True |
| candidate_age_within_historical_range | True |
| estimated_daily_users_within_prior_range | False |
| repair_discontinuities_present | True |

## 模型限制
- 这是可复现的官方题面参数和测量工作流实验，适合处理没有独立 CSV/XLSX 附件的 MCM 题；它不是随机造数，也不是虚构真实观测。
- `worked_example_assumptions` 只是展示考古队填完非破坏测量表后如何反演；正式论文应把现场测量值替换进模板，并对材料磨损系数做来源校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2025/A/q04/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2025/A/q04/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2025/A/q04/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2025/A/q04`
