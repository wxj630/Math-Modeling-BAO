# 2011-B 问题 1 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2011年 CUMCM B题：交巡警服务平台的设置与调度
- 问题：问题 1
- 原问：附件1中的附图1给出了该市中心城区A的交通网络和现有的20个交巡警服务平台的设置情况示意图，相关的数据信息见附件2。请为各交巡警服务平台分配管辖范围，使其在所管辖的范围内出现突发事件时，尽量能在3分钟内有交巡警（警车的时速为60km/h）到达事发地。 对于重大突发事件，需要调度全区20个交巡警服务平台的警力资源，对进出该区的13条交通要道实现快速全封锁。实际中一个平台的警力最多封锁一个路口，请给出该区交巡警服务平台警力合理的调度方案。 根据现有交巡警服务平台的工作量不均衡和有些地方出警时间过长的实际情况，拟在该区内再增加2至5个平台，请确定需要增加平台的具体个数和位置。

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

- 通用代码：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2011/B/q01/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2011/B/q01/solution.py`
- 结果 JSON：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/results/2011/B/q01/result.json
- 实验报告：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/reports/2011/B/q01/report.md
- 实验产物：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/artifacts/2011/B/q01/experiment_table.csv

## 数据来源

- 类型：problem_statement
- 路径：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2011/B.md
- 说明：未找到可直接读取的数值附件，本问改用题目原文中的参数/表格数字生成实验结果。

## 核心结果

```json
{
  "method": "dijkstra_shortest_path",
  "node_count": 3,
  "source": 0,
  "distances": [
    0.0,
    0.2,
    0.2
  ],
  "predecessors": [
    -9999,
    0,
    0
  ]
}
```
