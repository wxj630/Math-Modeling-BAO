# 2025-D 问题1 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2025年 CUMCM D题：矿井突水水流漫延模型与逃生方案
- 问题：问题1
- 原问：若巷道的某一点发生突水，试分析水流过程，建立突水水流在巷道的流动漫延 模型。 对附件1 和附件2 给出的两个矿井巷道网络，分别给出网络中各巷道水流的变化情况， 其中附件1 中的突水点位置为A1 (5349.03,4931.90,10.00)，附件2 中的突水点位置为A2 (4143.12,4376.28,6.33)。将结果分别保存到文件result1-1.xlsx 和result1-2.xlsx 中（模板文 件在附件3 中，所有结果均保留2 位小数，下同），其中端点水流到达时刻是指突水水流首 次流经该点的时刻，巷道充满水时刻是指巷道中水流的水平面达到巷道最高点的时刻。

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

- 通用代码：cumcm/generic_baselines/solutions/2025/D/q01/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2025/D/q01/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2025/D/q01/result.json
- 实验报告：cumcm/generic_baselines/reports/2025/D/q01/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2025/D/q01/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/D题/附件/附件1.xlsx
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "dijkstra_shortest_path",
  "node_count": 3,
  "source": 0,
  "distances": [
    0.0,
    0.000607,
    1.000911
  ],
  "predecessors": [
    -9999,
    0,
    1
  ]
}
```
