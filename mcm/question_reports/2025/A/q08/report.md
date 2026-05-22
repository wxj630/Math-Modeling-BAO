# 2025-A q08：典型日人数与短时峰值

## 题目原问
What information can be determined with respect to the numbers of people using the stairs in a typical day and were there large numbers of people using the stairs over a short time or a small number of people over a longer time?

## 适合模型
综合日均使用人数、同时使用指数和年龄可靠性区间，把典型日拆成短时峰值使用和长时低强度通行两部分。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted`。
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

### 年龄与可靠性
- 模型：deterministic uncertainty grid over material wear coefficient and plausible daily traffic。
- 年龄估计：340.3 年。
- 合理区间：[283.6, 397.0] 年。
- 可靠性：medium: age is identifiable only jointly with material wear rate and daily traffic prior。
- 合理网格数：2 / 30。

### 典型日使用模式
- 日均使用人数：72.67。
- 峰值时段占比：0.376。
- 峰值时段人数：27.3。
- 低强度时段每小时人数：4.5。
- 判断：mixed ceremonial peaks plus regular low-intensity circulation。

## 模型限制
- 这是可复现的官方题面参数和测量工作流实验，适合处理没有独立 CSV/XLSX 附件的 MCM 题；它不是随机造数，也不是虚构真实观测。
- `worked_example_assumptions` 只是展示考古队填完非破坏测量表后如何反演；正式论文应把现场测量值替换进模板，并对材料磨损系数做来源校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2025/A/q08/solution.py`

## 输出
- `mcm/question_results/2025/A/q08/result.json`
- `mcm/question_reports/2025/A/q08/report.md`
- `mcm/question_artifacts/2025/A/q08`
