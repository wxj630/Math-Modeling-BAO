# 2023-E 问题1 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2023年 CUMCM E题：黄河水沙监测数据分析
- 问题：问题1
- 原问：研究该水文站黄河水的含沙量与时间、水位、水流量的关系，并估算近6 年该水 文站的年总水流量和年总排沙量。

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

- 通用代码：cumcm/generic_baselines/solutions/2023/E/q01/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2023/E/q01/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2023/E/q01/result.json
- 实验报告：cumcm/generic_baselines/reports/2023/E/q01/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2023/E/q01/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：../../Documents/Playground/cumcm_unzipped/2023_Y20WPner9fa62862794e6dc82731a5561ce1132f/E题/附件1.xlsx
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "dijkstra_shortest_path",
  "node_count": 3,
  "source": 0,
  "distances": [
    0.0,
    0.133333,
    0.266667
  ],
  "predecessors": [
    -9999,
    0,
    0
  ]
}
```
