# 2024-D 问题 3 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2024年 CUMCM D题：反潜航空深弹命中概率
- 问题：问题 3
- 原问：由于单枚深弹命中率较低，为了增强杀伤效果，通常需要投掷多枚深弹。若一 架反潜飞机可携带 9 枚航空深弹， 所有深弹的定深引信引爆深度均相同， 投弹落点在平面上 呈阵列形状（见图 2） 。在问题2 的参数下，请设计投弹方案（包括定深引信引爆深度，以 及投弹落点之间的平面间隔） ，使得投弹命中（指至少一枚深弹命中潜艇）的概率最大。

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

- 通用代码：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2024/D/q03/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2024/D/q03/solution.py`
- 结果 JSON：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/results/2024/D/q03/result.json
- 实验报告：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/reports/2024/D/q03/report.md
- 实验产物：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/artifacts/2024/D/q03/experiment_table.csv

## 数据来源

- 类型：problem_statement
- 路径：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2024/D.md
- 说明：未找到可直接读取的数值附件，本问改用题目原文中的参数/表格数字生成实验结果。

## 核心结果

```json
{
  "method": "binomial_sampling_design",
  "p0": 0.09,
  "p1": 0.165,
  "alpha": 0.05,
  "beta": 0.1,
  "sample_size": 699,
  "acceptance_number": 62,
  "reject_good_probability": null,
  "accept_bad_probability": null
}
```
