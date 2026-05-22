# 2024-B 问题 1 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2024年 CUMCM B题：生产过程中的决策
- 问题：问题 1
- 原问：供应商声称一批零配件（零配件 1 或零配件 2）的次品率不会超过某个标称值。 企业准备采用抽样检测方法决定是否接收从供应商购买的这批零配件， 检测费用由企业自行 承担。请为企业设计检测次数尽可能少的抽样检测方案。 如果标称值为 10%，根据你们的抽样检测方案， 针对以下两种情形， 分别给出具体结果： (1) 在 95%的信度下认定零配件次品率超过标称值，则拒收这批零配件； (2) 在 90%的信度下认定零配件次品率不超过标称值，则接收这批零配件。

## 通用模型选择

- 模型：概率统计与抽样检验（CH9：机器学习与统计模型）
- 教程参考：../My-Agent/intro-mathmodel/docs/CH9/第九章-机器学习与统计模型.md
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

- 通用代码：cumcm/generic_baselines/solutions/2024/B/q01/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2024/B/q01/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2024/B/q01/result.json
- 实验报告：cumcm/generic_baselines/reports/2024/B/q01/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2024/B/q01/experiment_table.csv

## 数据来源

- 类型：problem_statement
- 路径：cumcm/problems/2024/B.md
- 说明：未找到可直接读取的数值附件，本问改用题目原文中的参数/表格数字生成实验结果。

## 核心结果

```json
{
  "method": "binomial_sampling_design",
  "p0": 0.01,
  "p1": 0.045,
  "alpha": 0.05,
  "beta": 0.1,
  "sample_size": 699,
  "acceptance_number": 6,
  "reject_good_probability": null,
  "accept_bad_probability": null
}
```
