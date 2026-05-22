# 2024-D 问题 1 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2024年 CUMCM D题：反潜航空深弹命中概率
- 问题：问题 1
- 原问：投射一枚深弹，潜艇中心位置的深度定位没有误差， 两个水平坐标定位均服从 正态分布。分析投弹最大命中概率与投弹落点平面坐标及定深引信引爆深度之间的关系， 并 给出使得投弹命中概率最大的投弹方案，及相应的最大命中概率表达式。 针对以下参数值给出最大命中概率：潜艇长 100 m，宽 20 m，高 25 m，潜艇航向方位 角为 90∘，深弹杀伤半径为 20 m，潜艇中心位置的水平定位标准差 𝜎 = 120 m，潜艇中心 位置的深度定位值为 150 m.

## 通用模型选择

- 模型：概率统计与抽样检验（CH9：机器学习与统计模型）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH9/第九章-机器学习与统计模型.md
- 通用方法：`binomial_sampling_design`

## 变量、约束与公式

### 变量定义
- n: 抽样量
- c: 接收阈值
- p0: 标称缺陷率/基准概率
- p1: 风险备择概率

### 约束条件
- P_reject(p0)<=alpha
- P_accept(p1)<=beta
- n 为正整数，c 为非负整数

### 模型公式 / 目标函数
- `P_reject(p0)=1-F_Binomial(c;n,p0)`
- `P_accept(p1)=F_Binomial(c;n,p1)`
- `min n subject to producer/consumer risk`

## 运行与产物

- 通用代码：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2024/D/q01/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2024/D/q01/solution.py`
- 结果 JSON：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/results/2024/D/q01/result.json
- 实验报告：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/reports/2024/D/q01/report.md
- 实验产物：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/artifacts/2024/D/q01/experiment_table.csv

## 数据来源

- 类型：problem_statement
- 路径：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2024/D.md
- 说明：未找到可直接读取的数值附件，本问改用题目原文中的参数/表格数字生成实验结果。

## 核心结果

```json
{
  "method": "binomial_sampling_design",
  "p0": 0.2,
  "p1": 0.33000000000000007,
  "alpha": 0.05,
  "beta": 0.1,
  "sample_size": 699,
  "acceptance_number": 139,
  "reject_good_probability": null,
  "accept_bad_probability": null
}
```
