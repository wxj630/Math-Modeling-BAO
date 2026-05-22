# 2020-B 问题 2 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2020年 CUMCM B题：穿越沙漠
- 问题：问题 2
- 原问：假设所有玩家仅知道当天的天气状况，从第天起，每名玩家在当天行动结束后均知道其余玩家当天的行动方案和剩余的资源数量，随后确定各自第二天的行动方案。试给出一般情况下玩家应采取的策略，并对附件中的“第六关”进行具体讨论。 注1：附件所给地图中，有公共边界的两个区域称为相邻，仅有公共顶点而没有公共边界的两个区域不视作相邻。 注2：Result.xlsx中剩余资金数（剩余水量、剩余食物量）指当日所需资源全部消耗完毕后的资金数（水量、食物量）。若当日还有购买行为，则指完成购买后的资金数（水量、食物量）。

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

- 通用代码：cumcm/generic_baselines/solutions/2020/B/q13/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2020/B/q13/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2020/B/q13/result.json
- 实验报告：cumcm/generic_baselines/reports/2020/B/q13/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2020/B/q13/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：../../Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/B/Result.xlsx
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "linear_programming",
  "success": true,
  "objective_max": 34.24700461469823,
  "decision": [
    0.0,
    0.0,
    0.0,
    4.407576
  ],
  "resource_slack": [
    8.530946,
    0.0,
    0.511818
  ]
}
```
