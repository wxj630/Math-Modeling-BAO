# CUMCM 2020-B 穿越沙漠：Baseline → Advanced → Outstanding 进阶

这道题的本质不是最短路，而是带天气、资源、资金、补给和行动选择的动态决策问题。好的解法必须让路线、资源消耗和风险同时可复查。

## 材料入口

| 层级 | PDF | 代码 | 结果 |
|---|---|---|---|
| Baseline | `Math-Modeling-World-Reports/cumcm/2020-B/baseline/main.pdf` | `Math-Modeling-World-Reports/cumcm/2020-B/baseline/sections/A_code.tex`；`Math-Modeling-World/cumcm/generic_baselines/solutions/2020/B/q01/solution.py` | `Math-Modeling-World/cumcm/generic_baselines/results/2020/B/q01/result.json` |
| Advanced | `Math-Modeling-World-Reports/cumcm/2020-B/advanced/main.pdf` | `Math-Modeling-World-Reports/cumcm/2020-B/advanced/sections/A_code.tex`；`Math-Modeling-World/cumcm/question_solutions/2020/B/q01/solution.py` | `Math-Modeling-World/cumcm/question_results/2020/B/q01/result.json` |
| Outstanding | `Math-Modeling-World-Reports/outstanding/cumcm/2020-B/B108/pdf/B108.pdf` | `Math-Modeling-World/cumcm/outstanding_solutions/2020/B/B108/solution.py` | `Math-Modeling-World/cumcm/outstanding_solutions/2020/B/B108/result.json` |

## Baseline：从时间序列/资源配置开始

Baseline 对不同小问分别匹配时间序列预测和规划优化模型。

当前模型选择：

```text
q01 = time_series
q02 = optimization
q03 = time_series
q04 = time_series
```

这一层最大问题是：它还没有抓住“每天选择行动”的核心结构。沙漠穿越不是预测天气就结束，也不是单纯最短路，而是每天资源和资金状态的递推。

## Advanced：按天展开的动态规划

Advanced 将问题转成动态规划。状态记录日期、位置和是否允许挖矿，转移枚举停留、移动、挖矿等行动，并按天气扣减水和食物。

当前结果：

| 指标 | Advanced |
|---|---:|
| 解决关卡 | 第一关 |
| 到达终点 | true |
| 完成日 | 16 |
| 最终资金 | 9700 |
| 初始水箱数 | 232 |
| 初始食物箱数 | 214 |
| 初始载重 | 1124 kg |
| 挖矿天数 | 3 |
| 挖矿收入 | 3000 |

Advanced 的优点是有完整 `desert_strategy.csv`，每天区域、行动、天气、剩余资金、水、食物都能复查。它的不足也很明确：地图邻接是近似重建，因此结果和 O 奖论文路线不完全一致。

## Outstanding：路线表 + 1024 天气情景 + 随机模拟 + 博弈

Outstanding 对齐 B108 论文，把路线策略、天气枚举、随机模拟和博弈策略放在一起。

关键结果：

| 指标 | Outstanding 复现 | 论文目标 | 误差 |
|---|---:|---:|---:|
| 第一关得分 | 10470 | 10470 | 0 |
| 第一关完成天数 | 24 | 24 | 0 |
| 第二关得分 | 12730 | 12730 | 0 |
| 第二关完成天数 | 30 | 30 | 0 |
| 第三关期望得分 | 9350 | 9350 | 0 |
| 第四关失败概率 | 0.024 | < 0.025 | 满足 |
| 第四关期望收益 | 10272.4 | 10500 | 约 2.17% |

第五关博弈：

```text
equilibrium_strategy = S6
cost_without_communication = 795
cost_with_communication = 520
```

## 谁模拟/优化得最好

| 层级 | 模拟/优化能力 | 结论 |
|---|---|---|
| Baseline | 初步识别资源/时间结构 | 没抓住日级 DP 核心 |
| Advanced | 每日策略可复查，DP 结构清楚 | 地图近似导致结果不够贴论文 |
| Outstanding | 分数、情景枚举、失败概率和博弈均接近论文 | 最适合学习获奖论文的完整决策链 |

结论：Advanced 最适合学习 DP 状态和转移怎么写；Outstanding 最适合学习如何把 DP 扩展成情景分析、风险模拟和博弈策略，从而满足评奖中的“结果经得起检验”。
