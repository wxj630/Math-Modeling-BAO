# CUMCM 2018-A 高温作业服：Baseline → Advanced → Outstanding 进阶

这道题表面是传热微分方程，真正的论文级目标是服装厚度设计。评委关心的不只是温度曲线能不能算出来，还关心参数是否由附件标定、厚度是否满足安全约束、结论是否能复现。

## 材料入口

| 层级 | PDF | 代码 | 结果 |
|---|---|---|---|
| Baseline | `Math-Modeling-World-Reports/cumcm/2018-A/baseline/main.pdf` | `Math-Modeling-World-Reports/cumcm/2018-A/baseline/sections/A_code.tex`；`Math-Modeling-World/cumcm/generic_baselines/solutions/2018/A/q01/solution.py` | `Math-Modeling-World/cumcm/generic_baselines/results/2018/A/q01/result.json` |
| Advanced | `Math-Modeling-World-Reports/cumcm/2018-A/advanced/main.pdf` | `Math-Modeling-World-Reports/cumcm/2018-A/advanced/sections/A_code.tex`；`Math-Modeling-World/cumcm/question_solutions/2018/A/q01/solution.py` | `Math-Modeling-World/cumcm/question_results/2018/A/q01/result.json` |
| Outstanding | `Math-Modeling-World-Reports/outstanding/cumcm/2018-A/A466/pdf/A466.pdf` | `Math-Modeling-World/cumcm/outstanding_solutions/2018/A/A466/solution.py` | `Math-Modeling-World/cumcm/outstanding_solutions/2018/A/A466/result.json` |

## Baseline：用微分方程/动态仿真建立起点

Baseline 将问题归入微分方程与动态仿真。它能说明皮肤温度是时间函数，也能给出一个温度变化的粗略模拟。

当前模型选择：

```text
q01 selected_model = 微分方程与动态仿真
q02 selected_model = 数据拟合与回归分析
```

这一层的问题是：它还没有充分利用附件中的材料参数和实测皮肤温度曲线，因此厚度结论只能算粗估。

## Advanced：附件驱动的传热参数标定和厚度搜索

Advanced 开始真正读取官方附件，使用热阻-热容模型标定参数，并按约束搜索厚度。

问题 2 结果：

| 指标 | Advanced |
|---|---:|
| 环境温度 | 65 C |
| 时间 | 60 min |
| 最优 II 层厚度 | 19.8 mm |
| 固定 IV 层厚度 | 5.5 mm |
| 最高皮肤温度 | 44.049667 C |
| 超过 44 C 时间 | 4.6 min |
| 标定 MAE | 0.08223 C |
| 标定 RMSE | 0.188948 C |

问题 3 结果：

| 指标 | Advanced |
|---|---:|
| 环境温度 | 80 C |
| 时间 | 30 min |
| 最优 II 层厚度 | 26.1 mm |
| 最优 IV 层厚度 | 6.4 mm |
| 可变总厚度 | 32.5 mm |
| 最高皮肤温度 | 44.622524 C |
| 超过 44 C 时间 | 4.9 min |

Advanced 的优点是安全裕量很足，最高温度远低于 47 C；不足是厚度偏保守，和 O 奖论文的薄层设计不够贴近。

## Outstanding：对齐 A466 的 Crank-Nicholson 思路和厚度目标

Outstanding 复现 A466 的论文目标，使用论文拟合的换热系数，并搜索满足最高温度和超过 44 C 时间约束的最小厚度。

关键结果：

| 问题 | 指标 | Outstanding 复现 | 论文目标 | 误差 |
|---|---|---:|---:|---:|
| 问题 2 | II 层厚度 | 17.6 mm | 17.6 mm | 0 |
| 问题 2 | 超过 44 C 时间 | 281 s | 281 s | 0 |
| 问题 3 | II 层厚度 | 19.3 mm | 19.3 mm | 0 |
| 问题 3 | IV 层厚度 | 6.4 mm | 6.4 mm | 0 |
| 问题 3 | 超过 44 C 时间 | 290 s | 290 s | 0 |

论文参数：

```text
h_I = 117.41 W/(m^2*C)
h_IV = 8.36 W/(m^2*C)
```

## 谁模拟/优化得最好

| 层级 | 模拟/优化能力 | 结论 |
|---|---|---|
| Baseline | 能说明温度随时间变化 | 只能作入门对照 |
| Advanced | 标定误差小，安全约束保守满足 | 模拟稳，厚度偏厚 |
| Outstanding | 与 O 奖论文厚度和关键秒数对齐 | 最适合学习获奖论文的“参数标定 + 厚度优化”写法 |

结论：Advanced 更像工程保守设计，Outstanding 更像竞赛论文设计。评奖视角下，Outstanding 的优势是结果更贴近论文目标，且能把厚度优化讲成清楚的约束问题。
