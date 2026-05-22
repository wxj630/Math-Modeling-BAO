# 2018-B 问题 3 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2018年 CUMCM B题：赛题
- 问题：问题 3
- 原问：CNC在加工过程中可能发生故障（据统计：故障的发生概率约为1%）的情况，每次故障排除（人工处理，未完成的物料报废）时间介于10~20分钟之间，故障排除后即刻加入作业序列。要求分别考虑一道工序和两道工序的物料加工作业情况。 请你们团队完成下列两项任务： 任务1：对一般问题进行研究，给出RGV动态调度模型和相应的求解算法； 任务2：利用表1中系统作业参数的3组数据分别检验模型的实用性和算法的有效性，给出RGV的调度策略和系统的作业效率，并将具体的结果分别填入附件2的EXCEL表中。

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

- 通用代码：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2018/B/q03/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2018/B/q03/solution.py`
- 结果 JSON：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/results/2018/B/q03/result.json
- 实验报告：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/reports/2018/B/q03/report.md
- 实验产物：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/artifacts/2018/B/q03/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2018_lcGi8NeCd14458641de55ec1d705ea01714ff2dd/2018-B-Chinese/CUMCM-2018-Problem-B-Chinese-Appendix-2/Case_1_result.xls
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "linear_programming",
  "success": true,
  "objective_max": 37.12931146946421,
  "decision": [
    0.0,
    2.388079,
    0.0,
    0.0,
    0.0,
    0.938812
  ],
  "resource_slack": [
    0.0,
    0.0,
    0.774047
  ]
}
```
