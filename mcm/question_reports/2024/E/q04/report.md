# 2024-E q04：极端天气上升地区的承保模型与两大洲演示

## 题目原问
Develop a model for insurance companies to determine if they should underwrite policies in an area that has a rising number of extreme weather events. Demonstrate your model using two areas on different continents that experience extreme weather events.

## 适合模型
对 North America 飓风洪水走廊和 Asia 气旋洪水走廊做确定性情景演示，明确这些是演示参数而非真实保险组合观测。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted`。
- 行数/记录数：{'official_parameters': 6}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 财产保险承保模型
- 模型：deterministic climate-stress underwriting score balancing net catastrophe loss ratio, affordability, mitigation, and insurer capital buffer。
- 承保分数解释：higher is more sustainable to underwrite。
- approve 阈值：0.62；decline 阈值：0.4。
- 网格行数：180；approve/conditional/decline：37/84/59。

#### 最稳健承保情景

| hazard_frequency_index | severity_index | property_vulnerability | mitigation_effect | underwriting_viability_score | decision |
|---|---|---|---|---|---|
| 0.85 | 0.85 | 0.45 | 0.3 | 0.8113 | approve standard or lightly conditioned underwriting |
| 0.85 | 1.0 | 0.45 | 0.3 | 0.7832 | approve standard or lightly conditioned underwriting |
| 1.0 | 0.85 | 0.45 | 0.3 | 0.7832 | approve standard or lightly conditioned underwriting |
| 0.85 | 0.85 | 0.6 | 0.3 | 0.7582 | approve standard or lightly conditioned underwriting |
| 1.15 | 0.85 | 0.45 | 0.3 | 0.7551 | approve standard or lightly conditioned underwriting |
| 1.0 | 1.0 | 0.45 | 0.3 | 0.7501 | approve standard or lightly conditioned underwriting |

#### 最高风险情景

| hazard_frequency_index | severity_index | property_vulnerability | mitigation_effect | underwriting_viability_score | decision |
|---|---|---|---|---|---|
| 1.45 | 1.4 | 0.75 | 0.0 | -0.2005 | decline new underwriting until community-level risk reduction or public-private backstop exists |
| 1.3 | 1.4 | 0.75 | 0.0 | -0.0902 | decline new underwriting until community-level risk reduction or public-private backstop exists |
| 1.45 | 1.2 | 0.75 | 0.0 | -0.0482 | decline new underwriting until community-level risk reduction or public-private backstop exists |
| 1.45 | 1.4 | 0.75 | 0.15 | 0.0119 | decline new underwriting until community-level risk reduction or public-private backstop exists |
| 1.45 | 1.4 | 0.6 | 0.0 | 0.0127 | decline new underwriting until community-level risk reduction or public-private backstop exists |
| 1.15 | 1.4 | 0.75 | 0.0 | 0.0201 | decline new underwriting until community-level risk reduction or public-private backstop exists |

### 两大洲地区演示
- 说明：Two deterministic region scenarios on different continents, used to demonstrate the official PDF model rather than claim observed portfolio data.。

| region | continent | dominant_hazards | net_loss_ratio | underwriting_viability_score | decision |
|---|---|---|---|---|---|
| Florida Gulf Coast hurricane-flood corridor | North America | hurricane wind, storm surge, coastal flood | 0.4936 | 0.4641 | conditional underwriting with mitigation, deductible, and reinsurance trigger |
| Bangladesh delta cyclone-flood corridor | Asia | cyclone wind, river flood, storm surge | 0.5706 | 0.1173 | decline new underwriting until community-level risk reduction or public-private backstop exists |

## 模型限制
- 这是可复现的官方题面参数保险与保护决策实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中 $1T、1000 起事件、115%、30-60%、57% 等宏观参数。
- 两个地区、建址和地标保护行是显式确定性演示情景，不是保险公司真实承保组合；正式论文应补充当地灾害频率、赔付率、建筑清单、工程造价和社区调查数据校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2024/E/q04/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2024/E/q04/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2024/E/q04/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2024/E/q04`
