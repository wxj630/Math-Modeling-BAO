# MCM 2015-A Ebola：Baseline → Advanced → Outstanding 进阶

这道题的主线是传染病动力学，但获奖论文不会停在 SEIR 曲线，而是把疫情传播、药物产能、医疗中心选址和药品分配连成一条干预链。

## 材料入口

| 层级 | PDF | 代码 | 结果 |
|---|---|---|---|
| Baseline | `Math-Modeling-BAO-Reports/mcm/2015-A/baseline/main.pdf` | `Math-Modeling-BAO-Reports/mcm/2015-A/baseline/sections/A_code.tex`；`Math-Modeling-BAO/mcm/generic_baselines/solutions/2015/A/q01/solution.py` | `Math-Modeling-BAO/mcm/generic_baselines/results/2015/A/q01/result.json` |
| Advanced | `Math-Modeling-BAO-Reports/mcm/2015-A/advanced/main.pdf` | `Math-Modeling-BAO-Reports/mcm/2015-A/advanced/sections/A_code.tex`；`Math-Modeling-BAO/mcm/question_solutions/2015/A/q01/solution.py` | `Math-Modeling-BAO/mcm/question_results/2015/A/q01/result.json` |
| Outstanding | `Math-Modeling-BAO-Reports/outstanding/mcm/2015-A/35532/pdf/35532.pdf` | `Math-Modeling-BAO/mcm/outstanding_solutions/2015/A/35532/solution.py` | `Math-Modeling-BAO/mcm/outstanding_solutions/2015/A/35532/result.json` |

## Baseline：先把动态过程跑起来

Baseline 选择的是一阶动态仿真基线。它的价值是快速说明：Ebola 不是静态评分题，而是随时间演化的状态变量问题。

当前结果：

```text
method = first_order_dynamic_baseline
baseline_score = 0.498857
artifact = mcm/question_artifacts/2015/A/q01/experiment_table.csv
```

这一层能让论文有一个最低起点：变量随时间变化，参数影响未来曲线。但是它的假设很粗，既没有真实疫情初值，也没有药物、隔离、医疗中心这些题目核心机制。

## Advanced：从通用动态模型走向题目专用模型

Advanced 保留动态建模框架，并开始把题目拆成传播、药物和公告信三个任务。当前代码仍偏 scaffold，主要作用是把问题结构和输出材料整理清楚。

进步点：

- 从“只做曲线”变成“传播 + 生产 + 配送 + 建议信”的完整任务框架。
- 把后续 outstanding 要用的干预变量提前暴露出来。
- 让摘要和结构开始服务整题，而不是只解释一个 ODE。

不足：

- 还没有把论文中的 Table 7 初值、隔离状态、药物产量阈值接进方程。
- 对医疗中心选址和药品分配还没有形成可检验结果。

## Outstanding：SEIQR + 药物产能 + 医疗中心覆盖

Outstanding 复现的是 35532 论文链条。它把人群状态扩展为 SEIQR，并加入药物产量对传播/恢复的影响，再用集合覆盖选择医疗中心。

关键结果：

| 指标 | Outstanding 复现 | 论文目标 | 误差 |
|---|---:|---:|---:|
| 最小日药品产量阈值 `Gm` | 4000 | 4000 | 0 |
| 医疗中心数量 | 7 | 7 | 0 |

药品分配结果：

| 国家 | `Gm=4000` 下药品分配 |
|---|---:|
| Guinea | 1084.89 |
| Liberia | 1575.19 |
| Sierra Leone | 1339.92 |

选出的医疗中心：

```text
Freetown, Makeni, Bo, Pujehun, Kenema, Kabala, Koidu
```

## 谁模拟/优化得最好

| 层级 | 模拟/优化能力 | 评奖视角 |
|---|---|---|
| Baseline | 能做最粗动态仿真 | 假设太粗，只能算入门 |
| Advanced | 整题结构更完整 | 还缺真实参数和可检验结论 |
| Outstanding | 同时复现传播、药物阈值、中心覆盖和分配 | 最符合“假设用于后续模型、结果经得起检验”的要求 |

结论：这题最值得学习的是 outstanding 的混合结构。微分方程负责模拟疫情，优化和覆盖模型负责回答“怎么干预”。只会 `solve_ivp` 不够，必须把干预策略接到模型结果上。
