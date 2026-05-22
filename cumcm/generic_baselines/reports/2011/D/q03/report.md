# 2011-D 问题 3 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2011年 CUMCM D题：天然肠衣搭配
- 问题：问题 3
- 原问：为提高原料使用率，总长度允许有± 0.5米的误差，总根数允许比标准少1根；

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

- 通用代码：cumcm/generic_baselines/solutions/2011/D/q03/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2011/D/q03/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2011/D/q03/result.json
- 实验报告：cumcm/generic_baselines/reports/2011/D/q03/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2011/D/q03/experiment_table.csv

## 数据来源

- 类型：problem_statement
- 路径：cumcm/problems/2011/D.md
- 说明：未找到可直接读取的数值附件，本问改用题目原文中的参数/表格数字生成实验结果。

## 核心结果

```json
{
  "method": "binomial_sampling_design",
  "p0": 0.005,
  "p1": 0.0375,
  "alpha": 0.05,
  "beta": 0.1,
  "sample_size": 699,
  "acceptance_number": 3,
  "reject_good_probability": null,
  "accept_bad_probability": null
}
```
