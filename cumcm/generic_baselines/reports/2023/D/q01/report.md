# 2023-D 问题 1 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2023年 CUMCM D题：圈养湖羊的空间利用率
- 问题：问题 1
- 原问：不考虑不确定因素和种羊的淘汰更新，假定自然交配期 20 天，母羊都能受孕，孕 期 149 天，每胎产羔 2 只，哺乳期 40 天，羔羊育肥期 210 天，母羊空怀休整期 20 天。该湖羊 养殖场现有 112 个标准羊栏，在实现连续生产的条件下，试确定养殖场种公羊与基础母羊的合 理数量， 并估算年化出栏羊只数量的范围。 若该养殖场希望每年出栏不少于 1500 只羊，试估算 现有标准羊栏数量的缺口。

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

- 通用代码：cumcm/generic_baselines/solutions/2023/D/q01/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2023/D/q01/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2023/D/q01/result.json
- 实验报告：cumcm/generic_baselines/reports/2023/D/q01/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2023/D/q01/experiment_table.csv

## 数据来源

- 类型：problem_statement
- 路径：cumcm/problems/2023/D.md
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
