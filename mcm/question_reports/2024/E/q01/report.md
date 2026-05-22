# 2024-E q01：保险公司应在什么条件下承保

## 题目原问
Under what conditions should insurance companies underwrite policies?

## 适合模型
官方 PDF 宏观参数 + 气候压力承保可持续性分数：综合净巨灾损失率、保障缺口导致的可负担性压力、减灾效果和资本缓冲。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted`。
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

## 模型限制
- 这是可复现的官方题面参数保险与保护决策实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中 $1T、1000 起事件、115%、30-60%、57% 等宏观参数。
- 两个地区、建址和地标保护行是显式确定性演示情景，不是保险公司真实承保组合；正式论文应补充当地灾害频率、赔付率、建筑清单、工程造价和社区调查数据校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2024/E/q01/solution.py`

## 输出
- `mcm/question_results/2024/E/q01/result.json`
- `mcm/question_reports/2024/E/q01/report.md`
- `mcm/question_artifacts/2024/E/q01`
