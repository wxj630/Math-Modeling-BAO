# 2024-E 问题 4 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2024年 CUMCM E题：交通流量管控
- 问题：问题 4
- 原问：五一黄金周期间，该小镇对景区周边道路实行了临时性交通管理措施，具体 管控措施见附件 3。请结合数据评价临时管控措施在两条主路上的效果。 附件 1 路段行驶方向编号及交叉口之间的距离 附件 2 纬中路各交叉口车辆信息 附件 3 五一黄金周期间交通管控措施

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

- 通用代码：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2024/E/q04/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2024/E/q04/solution.py`
- 结果 JSON：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/results/2024/E/q04/result.json
- 实验报告：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/reports/2024/E/q04/report.md
- 实验产物：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/artifacts/2024/E/q04/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/E题/附件1.xlsx
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "dijkstra_shortest_path",
  "node_count": 3,
  "source": 0,
  "distances": [
    0.0,
    1.111111,
    1.333333
  ],
  "predecessors": [
    -9999,
    0,
    0
  ]
}
```
