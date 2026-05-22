# 2021-A 问题 1 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2021年 CUMCM A题：FAST”主动反射面的形状调节
- 问题：问题 1
- 原问：主动反射面共有主索节点2226 个， 节点间连接主索6525 根， 不考虑周边支承结构连接 的部分反射面板， 共有反射面板4300 块。 基准球面的球心在坐标原点， 附件1 给出了所有主索 节点的坐标和编号，附件2 给出了促动器下端点（地锚点）坐标、基准态时上端点（顶端）的 坐标，以及促动器对应的主索节点编号，附件3 给出了4300 块反射面板对应的主索节点编号。

## 通用模型选择

- 模型：图论网络与路径调度（CH4：复杂网络与图论模型）
- 教程参考：../My-Agent/intro-mathmodel/docs/CH4/第4章-复杂网络与图论模型.md
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

- 通用代码：cumcm/generic_baselines/solutions/2021/A/q04/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2021/A/q04/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2021/A/q04/result.json
- 实验报告：cumcm/generic_baselines/reports/2021/A/q04/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2021/A/q04/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：../../Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/A/附件1.csv
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "dijkstra_shortest_path",
  "node_count": 3,
  "source": 0,
  "distances": [
    0.0,
    2.0,
    3.80431
  ],
  "predecessors": [
    -9999,
    0,
    1
  ]
}
```
