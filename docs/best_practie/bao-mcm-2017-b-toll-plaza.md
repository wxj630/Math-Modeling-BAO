# MCM 2017-B Toll Plaza：Baseline → Advanced → Outstanding 进阶

这道题是典型运筹优化混合题：排队论解决收费服务能力，合流设计解决安全和流量，敏感性分析解决不同交通组成和自动驾驶比例的变化。

## 材料入口

| 层级 | PDF | 代码 | 结果 |
|---|---|---|---|
| Baseline | `Math-Modeling-BAO-Reports/mcm/2017-B/baseline/main.pdf` | `Math-Modeling-BAO-Reports/mcm/2017-B/baseline/sections/A_code.tex`；`Math-Modeling-BAO/mcm/generic_baselines/solutions/2017/B/q01/solution.py` | `Math-Modeling-BAO/mcm/generic_baselines/results/2017/B/q01/result.json` |
| Advanced | `Math-Modeling-BAO-Reports/mcm/2017-B/advanced/main.pdf` | `Math-Modeling-BAO-Reports/mcm/2017-B/advanced/sections/A_code.tex`；`Math-Modeling-BAO/mcm/question_solutions/2017/B/q01/solution.py` | `Math-Modeling-BAO/mcm/question_results/2017/B/q01/result.json` |
| Outstanding | `Math-Modeling-BAO-Reports/outstanding/mcm/2017-B/69427/pdf/69427.pdf` | `Math-Modeling-BAO/mcm/outstanding_solutions/2017/B/69427/solution.py` | `Math-Modeling-BAO/mcm/outstanding_solutions/2017/B/69427/result.json` |

## Baseline：把问题看成资源配置和证据表

Baseline 把收费亭和车道看成资源配置问题，并用证据表承接轻交通、重交通、自动驾驶比例和收费方式比例。

当前模型选择：

```text
q01 = resource_allocation_baseline
q02 = evidence_table_baseline
q03 = first_order_dynamic_baseline
q04 = first_order_dynamic_baseline
```

这一层能让问题“有表可算”，但还没有真正把 8 到 3 车道合流的几何冲突、容量瓶颈和事故风险连起来。

## Advanced：合流方案的多指标比较

Advanced 构造了多个合流设计候选，并计算冲突指数、成本指数、安全分和容量。推荐方案是 staged zipper merge。

候选方案中的关键结果：

| 方案 | 合流长度 | 安全分 | 通行能力 | 目标分 |
|---|---:|---:|---:|---:|
| short direct taper | 260 m | 53.615385 | 4620 veh/h | 47.877502 |
| staged zipper merge | 420 m | 84.571429 | 4620 veh/h | 57.93568 |

轻重交通模拟：

| 交通情景 | 需求 | 吞吐 | 平均延误 |
|---|---:|---:|---:|
| light traffic | 2400 veh/h | 2400 veh/h | 0 min |
| heavy traffic | 6200 veh/h | 4620 veh/h | 6.155844 min |

Advanced 的优点是评委能看见“为什么选 staged zipper merge”：安全分更高，同时吞吐不变。

## Outstanding：M/G/k 收费亭数量 + 最大流 + 事故率敏感性

Outstanding 对齐 69427 论文，复现了收费亭数量、最大流、事故率和 NJ 迁移应用。

关键结果：

| 指标 | Outstanding 复现 | 论文目标 | 误差 |
|---|---:|---:|---:|
| 单向收费车道数 | 7 | 7 | 0 |
| 最大流量 | 1375 veh/h | 1375 veh/h | 0 |
| 事故率 | 0.009 | 0.009 | 0 |
| 面积 | 4650.1875 m2 | 4650.1875 m2 | 0 |
| NJ 面积 | 9614.56 m2 | 9614.56 m2 | 0 |

NJ 应用：

```text
toll_lanes = 10
booth_proportion = 5:3:2
area = 9614.56 m2
```

## 谁模拟/优化得最好

| 层级 | 模拟/优化能力 | 结论 |
|---|---|---|
| Baseline | 资源配置框架初步成立 | 太抽象 |
| Advanced | 多方案设计、容量和安全指标最清楚 | 工程解释性强 |
| Outstanding | 与 O 奖论文关键数值完全对齐 | 最适合学习获奖论文的结果链 |

结论：Advanced 的设计比较最适合看“怎么建模”，Outstanding 最适合看“怎么把模型结果打磨成获奖论文”。如果要在论文里说谁优化得最好，staged zipper merge 是 advanced 中的最好方案；如果按 O 奖复现标准，69427 outstanding 最强。
