# 2011-B 问题 2 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2011年 CUMCM B题：交巡警服务平台的设置与调度
- 问题：问题 2
- 原问：针对全市（主城六区A，B，C，D，E，F）的具体情况，按照设置交巡警服务平台的原则和任务，分析研究该市现有交巡警服务平台设置方案（参见附件）的合理性。如果有明显不合理，请给出解决方案。 如果该市地点P（第32个节点）处发生了重大刑事案件，在案发3分钟后接到报警，犯罪嫌疑人已驾车逃跑。为了快速搜捕嫌疑犯，请给出调度全市交巡警服务平台警力资源的最佳围堵方案。 附件1：A区和全市六区交通网络与平台设置的示意图。 附件2：全市六区交通网络与平台设置的相关数据表（共5个工作表）。

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

- 通用代码：cumcm/generic_baselines/solutions/2011/B/q02/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2011/B/q02/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2011/B/q02/result.json
- 实验报告：cumcm/generic_baselines/reports/2011/B/q02/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2011/B/q02/experiment_table.csv

## 数据来源

- 类型：problem_statement
- 路径：cumcm/problems/2011/B.md
- 说明：未找到可直接读取的数值附件，本问改用题目原文中的参数/表格数字生成实验结果。

## 核心结果

```json
{
  "method": "dijkstra_shortest_path",
  "node_count": 3,
  "source": 0,
  "distances": [
    0.0,
    0.236842,
    0.236842
  ],
  "predecessors": [
    -9999,
    0,
    0
  ]
}
```
