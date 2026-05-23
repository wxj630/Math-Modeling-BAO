# 2025-D 问题2 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2025年 CUMCM D题：矿井突水水流漫延模型与逃生方案
- 问题：问题2
- 原问：当矿井发生突水后，安全生产部门即刻监控到突水情况，并应尽快为每个工人 的制订出有效逃生方案。请根据问题1 中所建水流漫延模型，协助安全生产部门为各矿工设 计最佳逃生路径。 假设工人在无突水水流巷道时，前进速度为4 m/s；巷道内水面高度小于等于0.3 m 时， 工人逆水行进速度为1 m/s，顺水行进速度为2 m/s；当巷道内水面高度为超过0.3 m 时，不 建议涉水通行。 假设在突水1 分钟时发布逃生通知，请对附件1 和附件2 给出的两个矿井巷道网络，分 别给出各矿工的最佳逃生路径，其中附件1 中的出入口位置分别为 (3252.16,3326.63,10.00)， (3173.10,2819.97,10.00)，矿工的位置分别为 (5808.18,5367.75,10.00)，(5194.00,4785.31, 10.00)，(6190.81,3434.29,10.00)；附件2中的出入口位置分别为 (6336.99,6073.22,36.15)， (6416.05,6579.88,8.69)，矿工的位置分别为 (4395.15,4614.53,6.59)，(3398.34,5965.56, 1.31)，(3879.44,4125.47,6.22)。将结果分别保存到文件result2-1.xlsx 和result2-2.xlsx 中（模 板文件在附件3 中）。

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

- 通用代码：cumcm/generic_baselines/solutions/2025/D/q02/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2025/D/q02/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2025/D/q02/result.json
- 实验报告：cumcm/generic_baselines/reports/2025/D/q02/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2025/D/q02/experiment_table.csv

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
