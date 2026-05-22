# 2021-C 问题 2 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2021年 CUMCM C题：生产企业原材料的订购与运输
- 问题：问题 2
- 原问：供应商的供货量：第一列为供应商的名称； 第二列为供应商供应原材料的类别； 第三列及以后共240 列为各供应商每周的供货量 （单位： 立方米） ； 数值 “0” 表示相应 的周（所在列）供应商（所在行）没有供货。 附件 2 的数据说明 第一列为转运商的名称； 第二列及以后共240 列为每周各转运商的运输损耗率 （%）， 即 100%−=供货量 接收量损耗率 供货量 ；数值“0”表示没有运送。

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

- 通用代码：cumcm/generic_baselines/solutions/2021/C/q06/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2021/C/q06/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2021/C/q06/result.json
- 实验报告：cumcm/generic_baselines/reports/2021/C/q06/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2021/C/q06/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：../../Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/C/附件1 近5年402家供应商的相关数据.xlsx
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "dijkstra_shortest_path",
  "node_count": 3,
  "source": 0,
  "distances": [
    0.0,
    2.677686,
    7.677686
  ],
  "predecessors": [
    -9999,
    0,
    1
  ]
}
```
