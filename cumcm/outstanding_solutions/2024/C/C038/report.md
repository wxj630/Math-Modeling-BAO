# C038 O奖论文复现：基于差分遗传算法的农作物种植策略优化

## 复现定位
本脚本复现 C038 的可验证主线：官方附件驱动的种植面积优化、超产处置、不确定性情景、CVaR 风险和相关性鲁棒比较。

## 问题
2024 CUMCM-C 要求为 2024-2030 年农作物种植制定最优方案，并逐步加入销售、产量、成本、价格不确定性和作物/经济因素相关性。

## 建模
- 从附件 1/2 读取地块、作物、2023 种植和统计数据。
- 用亩利润、适宜地块、季节和轮作约束构造候选表。
- q1 比较滞销浪费与半价销售两种超产情形。
- q2/q3 用情景扰动评估均值、10% 分位和 CVaR，并加入 Spearman 相关性比较。

## 实验结果与分析
- 候选种植组合：1230 行。
- q1 滞销利润：-5389476.0 元；半价销售利润：75678478.0 元，提升 8.1067954e+18%。
- 相关性情景下 CVaR 最优计划：waste，CVaR10=118550698.19 元。

## 代码与产物
- 代码：`cumcm/outstanding_solutions/2024/C/C038/solution.py`
- 结果：`cumcm/outstanding_solutions/2024/C/C038/result.json`
- 图表：`cumcm/outstanding_solutions/2024/C/C038/artifacts/profit_risk_comparison.png`、`cumcm/outstanding_solutions/2024/C/C038/artifacts/correlation_heatmap.png`
- 表格：`cumcm/outstanding_solutions/2024/C/C038/artifacts/result1_1_reproduction.xlsx`、`cumcm/outstanding_solutions/2024/C/C038/artifacts/result1_2_reproduction.xlsx`、`cumcm/outstanding_solutions/2024/C/C038/artifacts/result2_reproduction.xlsx`

## 相对 advanced 的优势
从逐问线性规划结果升级为 O 奖论文式全局农业计划：同一候选表贯穿 q1/q2/q3，显式比较超产处置、不确定性下行风险和相关性扰动。
