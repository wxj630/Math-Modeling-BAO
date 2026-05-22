# 2020-A q03：小型渔业公司的运营适应策略

## 题目原问
Recommend operational changes that small fishing companies can make as fish move north.

## 适合模型
比较 gear modernization、cooperative vessel sharing、cold-chain landing partnership、alternative species portfolio 和 joint access agreement 的 range gain、成本和配额韧性。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025/official_assets`。
- 行数/记录数：{'official_parameters': 4}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

## 模型限制
- 这是可复现的官方题面参数 Moving North 鱼群迁移实验；本地官方 PDF 文字层不完整，题面要求由 COMAP 2020 problems 官方页面核对，归档仍指向本地官方 PDF 资产。
- COMAP 没有提供海温、鱼群调查或船队成本附件，因此 thermal shift、fleet range、territorial threshold 和策略得分均为显式确定性情景输入；正式论文应补充 ICES/NOAA/UK fisheries 海温和渔业观测校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2020/A/q03/solution.py`

## 输出
- `mcm/question_results/2020/A/q03/result.json`
- `mcm/question_reports/2020/A/q03/report.md`
- `mcm/question_artifacts/2020/A/q03`
