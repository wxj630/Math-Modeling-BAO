# 2025-D 问题4 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2025年 CUMCM D题：矿井突水水流漫延模型与逃生方案
- 问题：问题4
- 原问：当矿井出现第二个突水点后，安全生产部门即刻监控到突水情况，并尽快调整 逃生方案。请协助安全生产部门调整最佳逃生路径。 在前面问题的基础上，假设在第二突水点突水1 分钟后，安全生产部门发布调整后的逃 生方案。对附件1 和附件2 给出的两个矿井巷道网络，分别给出各矿工调整后的最佳逃生路 径。请将结果分别保存到文件result4-1.xlsx 和result4-2.xlsx 中（模板文件在附件3 中）。 附件说明 附件1.xlsx、附件2.xlsx 两个矿井的巷道网络数据，均包含“端点”和“巷道”两个 工作表。“端点”工作表记录了巷道中各端点的三维坐标 (X, Y, Z)（其中 XY 为水平面，Z 为 高程）；“巷道”工作表记录了各巷道的两个端点编号。 附件3 计算结果模板文件夹，其中 result𝑖-𝑗.xlsx 问题 𝑖 中矿井 𝑗 的结果文件模板

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

- 通用代码：cumcm/generic_baselines/solutions/2025/D/q04/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2025/D/q04/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2025/D/q04/result.json
- 实验报告：cumcm/generic_baselines/reports/2025/D/q04/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2025/D/q04/experiment_table.csv

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
