# MCM 2019-C Opioid Crisis：Baseline → Advanced → Outstanding 进阶

这道题的主线是数据建模，但优秀解法不能只做趋势预测。它需要把官方 NFLIS 数据、社会经济因素、空间传播思想和干预策略组织成完整证据链。

## 材料入口

| 层级 | PDF | 代码 | 结果 |
|---|---|---|---|
| Baseline | `Math-Modeling-World-Reports/mcm/2019-C/baseline/main.pdf` | `Math-Modeling-World-Reports/mcm/2019-C/baseline/sections/A_code.tex`；`Math-Modeling-World/mcm/generic_baselines/solutions/2019/C/q01/solution.py` | `Math-Modeling-World/mcm/generic_baselines/results/2019/C/q01/result.json` |
| Advanced | `Math-Modeling-World-Reports/mcm/2019-C/advanced/main.pdf` | `Math-Modeling-World-Reports/mcm/2019-C/advanced/sections/A_code.tex`；`Math-Modeling-World/mcm/question_solutions/2019/C/q01/solution.py` | `Math-Modeling-World/mcm/question_results/2019/C/q01/result.json` |
| Outstanding | `Math-Modeling-World-Reports/outstanding/mcm/2019-C/1901213/pdf/1901213.pdf` | `Math-Modeling-World/mcm/outstanding_solutions/2019/C/1901213/solution.py` | `Math-Modeling-World/mcm/outstanding_solutions/2019/C/1901213/result.json` |

## Baseline：县级线性趋势预测

Baseline 将题目识别为线性趋势预测和报告备忘录问题。

当前模型选择：

```text
q01 = linear_trend_forecast_baseline
q02 = linear_trend_forecast_baseline
q03 = report_outline_baseline
```

这一层能得到一个“哪些县未来更严重”的初步表，但它没有解释扩散机制，也没有把社会经济变量用于模型修正。

## Advanced：官方 NFLIS/ACS 数据驱动

Advanced 使用官方 NFLIS 数据构造县年面板，并合并 ACS 社会经济指标。它已经从“趋势线”升级为真实数据管线。

关键结果：

| 指标 | Advanced |
|---|---:|
| county-year rows | 3480 |
| county count | 461 |
| substance classes | heroin, synthetic_or_other_analgesic |

2020 高风险预测示例：

| 县 | 州 | 2017 观测报告 | 2020 预测报告 | 模型内 R2 |
|---|---|---:|---:|---:|
| Hamilton | OH | 9995 | 11277.99 | 0.8258 |
| Cuyahoga | OH | 7381 | 9042.05 | 0.9302 |
| Philadelphia | PA | 9156 | 8544.23 | 0.3714 |

Advanced 的优点是数据扎实、结果可复现；不足是空间传播结构还不够像 O 奖论文中的“成瘾传播/Markov 扩散”。

## Outstanding：空间 Markov 传播边 + 源头识别

Outstanding 复现 1901213 的核心思想：把 opioid 滥用看成可传播过程，用县级数据构造传播边、估计源头，并继续保留趋势预测。

关键结果：

| 指标 | Outstanding |
|---|---:|
| county-year rows | 3480 |
| transition edges | 1745 |

估计源头前五：

| 源头县 | attributed growth reports |
|---|---:|
| Hamilton, OH | 4578.026 |
| Philadelphia, PA | 3991.222 |
| Allegheny, PA | 3033.816 |
| Montgomery, OH | 3032.171 |
| Cuyahoga, OH | 2843.451 |

2020 预测前列：

| 县 | 州 | 2020 预测报告 |
|---|---|---:|
| Hamilton | OH | 11277.99 |
| Cuyahoga | OH | 9042.05 |
| Philadelphia | PA | 8544.23 |

## 谁模拟/优化得最好

| 层级 | 模拟/预测能力 | 结论 |
|---|---|---|
| Baseline | 可以做线性趋势 | 缺传播解释 |
| Advanced | 官方数据和预测最扎实 | 仍偏统计描述 |
| Outstanding | 加入传播边和源头识别 | 最符合 O 奖论文的机制建模 |

结论：这题不是看“哪个机器学习模型最复杂”，而是看能否把数据预测升级为传播机制。Outstanding 的优势是让评委看到 opioid crisis 如何从县域之间扩散，而不仅是某条趋势线变高。
