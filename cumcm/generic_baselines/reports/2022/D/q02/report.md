# 2022-D 问题 2 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2022年 CUMCM D题：气象报文信息卫星通信传输
- 问题：问题 2
- 原问：为了提高气象信息的地理密度，除了实现主站间气象报文的信息共享外，还需要 使用副站气象信息加以补充。 (1) 若要求在 𝐾 分钟内完成 𝑁 个主站间气象报文的信息共享，且每个主站满足条件：对 每支分队， 成功接收该分队至少一个副站的气象报文的概率不低于0.9。 请就 𝐾 (≥ 5) 的情形， 研究 𝑁 的最大值与 𝐾 的关系，并建立 𝐾 分钟内满足以上条件的信息传输的一般模型。若主 站间气象报文信息共享的传输方案与问题 1 相同，则只需给出副站气象报文的传输方案。 (2) 对于 𝐾 = 7， 给出 𝑁 的最大值， 并根据一般传输模型给出此时副站气象报文的传输方 案，将结果按表 2 的格式填报。求出在你们的传输方案下平均有多少个主站能成功接收每支分 队至少一个副站的气象报文，以及任一主站平均能成功接收多少个副站的气象报文。

## 通用模型选择

- 模型：规划优化与资源配置（CH3：函数极值与规划模型）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md
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

- 通用代码：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2022/D/q02/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2022/D/q02/solution.py`
- 结果 JSON：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/results/2022/D/q02/result.json
- 实验报告：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/reports/2022/D/q02/report.md
- 实验产物：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/artifacts/2022/D/q02/experiment_table.csv

## 数据来源

- 类型：problem_statement
- 路径：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2022/D.md
- 说明：未找到可直接读取的数值附件，本问改用题目原文中的参数/表格数字生成实验结果。

## 核心结果

```json
{
  "method": "linear_programming",
  "success": true,
  "objective_max": 7.530347652922812,
  "decision": [
    0.0,
    0.0,
    2.425123,
    0.0
  ],
  "resource_slack": [
    221.697031,
    0.0,
    0.56464
  ]
}
```
