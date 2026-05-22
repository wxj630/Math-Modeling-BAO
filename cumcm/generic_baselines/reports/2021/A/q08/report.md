# 2021-A 问题 5 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2021年 CUMCM A题：FAST”主动反射面的形状调节
- 问题：问题 5
- 原问：主索节点调节后，相邻节点之间的距离可能会发生微小变化，变化幅度不超过 0.07%。

## 通用模型选择

- 模型：图论网络与路径调度（CH4：复杂网络与图论模型）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH4/第4章-复杂网络与图论模型.md
- 通用方法：`dijkstra_shortest_path`

## 变量、约束与公式

### 变量定义
- G=(V,E): 交通/转运/关系网络
- w_ij: 边成本、距离或时间
- d_i: 从源点到节点 i 的最短距离
- pre_i: 最短路前驱节点

### 约束条件
- 边权非负
- 路径必须由网络中已有边组成

### 模型公式 / 目标函数
- `d_j = min_i(d_i + w_ij)`
- `min path_cost(source, target)`

## 运行与产物

- 通用代码：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2021/A/q08/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2021/A/q08/solution.py`
- 结果 JSON：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/results/2021/A/q08/result.json
- 实验报告：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/reports/2021/A/q08/report.md
- 实验产物：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/artifacts/2021/A/q08/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/A/附件1.csv
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "dijkstra_shortest_path",
  "node_count": 3,
  "source": 0,
  "distances": [
    0.0,
    6.0,
    7.80431
  ],
  "predecessors": [
    -9999,
    0,
    1
  ]
}
```
