# 2022-D 问题 1 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2022年 CUMCM D题：气象报文信息卫星通信传输
- 问题：问题 1
- 原问：(1) 要求在 𝐾 分钟内完成 𝑁 (≥ 5) 支分队主站间气象报文的信息共享，请研究 𝐾 的最小值与 𝑁 的关系，并建立 𝐾 分钟内实现 𝑁 个主站间气象报文信息共享的一般传输 模型。 (2) 在上述模型中， 取 𝑁 = 9， 给出 𝐾 的相应最小值， 并根据一般传输模型给出此时主站 间气象报文的信息共享方案，将结果按表 1 的格式填报。填报结果时，注意消息的完整性，例 如：在“发送信息所属站点序号”一栏中填写“5”，表示本轮所发送消息来自于第 5 号主站，

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

- 通用代码：cumcm/generic_baselines/solutions/2022/D/q01/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2022/D/q01/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2022/D/q01/result.json
- 实验报告：cumcm/generic_baselines/reports/2022/D/q01/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2022/D/q01/experiment_table.csv

## 数据来源

- 类型：problem_statement
- 路径：cumcm/problems/2022/D.md
- 说明：未找到可直接读取的数值附件，本问改用题目原文中的参数/表格数字生成实验结果。

## 核心结果

```json
{
  "method": "linear_programming",
  "success": true,
  "objective_max": 7.248143164883373,
  "decision": [
    0.0,
    0.0,
    2.429282,
    0.0
  ],
  "resource_slack": [
    221.842125,
    0.0,
    0.564207
  ]
}
```
