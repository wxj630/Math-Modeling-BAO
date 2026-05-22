# 2024-B 问题 4 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2024年 CUMCM B题：生产过程中的决策
- 问题：问题 4
- 原问：假设问题 2 和问题 3 中零配件、 半成品和成品的次品率均是通过抽样检测方法 （例如，你在问题 1 中使用的方法）得到的，请重新完成问题 2 和问题 3。 附录 说明 (1) 半成品、成品的次品率是将正品零配件（或者半成品）装配后的产品次品率； (2) 不合格成品中的调换损失是指除调换次品之外的损失 （如： 物流成本、企业信誉等） 。 (3) 购买单价、 检测成本、 装配成本、 市场售价、 调换损失和拆解费用的单位均为元/件。

## 通用模型选择

- 模型：规划优化与资源配置（CH3：函数极值与规划模型）
- 教程参考：../My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md
- 通用方法：`linear_programming`

## 变量、约束与公式

### 变量定义
- x_i: 第 i 个方案/资源的选择强度
- c_i: 单位收益或效用
- A_ji: 第 j 类资源消耗
- b_j: 第 j 类资源上限

### 约束条件
- A x <= b
- x_i >= 0
- 资源容量按题面约束映射为 b_j

### 模型公式 / 目标函数
- `max sum_i c_i*x_i`
- `s.t. A*x <= b, x >= 0`

## 运行与产物

- 通用代码：cumcm/generic_baselines/solutions/2024/B/q04/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2024/B/q04/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2024/B/q04/result.json
- 实验报告：cumcm/generic_baselines/reports/2024/B/q04/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2024/B/q04/experiment_table.csv

## 数据来源

- 类型：problem_statement
- 路径：cumcm/problems/2024/B.md
- 说明：未找到可直接读取的数值附件，本问改用题目原文中的参数/表格数字生成实验结果。

## 核心结果

```json
{
  "method": "linear_programming",
  "success": true,
  "objective_max": 6.160197122253828,
  "decision": [
    0.0,
    0.0,
    2.315599,
    0.0
  ],
  "resource_slack": [
    163.453561,
    0.0,
    0.556562
  ]
}
```
