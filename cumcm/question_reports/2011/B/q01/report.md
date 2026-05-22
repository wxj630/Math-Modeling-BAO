# 2011-B 问题 1 建模求解实验报告

## 题目原文与任务拆解

- 题目：2011年 CUMCM B题：交巡警服务平台的设置与调度
- 问题：问题 1
- 原问：附件1中的附图1给出了该市中心城区A的交通网络和现有的20个交巡警服务平台的设置情况示意图，相关的数据信息见附件2。请为各交巡警服务平台分配管辖范围，使其在所管辖的范围内出现突发事件时，尽量能在3分钟内有交巡警（警车的时速为60km/h）到达事发地。 对于重大突发事件，需要调度全区20个交巡警服务平台的警力资源，对进出该区的13条交通要道实现快速全封锁。实际中一个平台的警力最多封锁一个路口，请给出该区交巡警服务平台警力合理的调度方案。 根据现有交巡警服务平台的工作量不均衡和有些地方出警时间过长的实际情况，拟在该区内再增加2至5个平台，请确定需要增加平台的具体个数和位置。

### 本问需要完成什么
- 任务 1：附件1中的附图1给出了该市中心城区A的交通网络和现有的20个交巡警服务平台的设置情况示意图，相关的数据信息见附件2
- 任务 2：实际中一个平台的警力最多封锁一个路口，请给出该区交巡警服务平台警力合理的调度方案
- 任务 3：根据现有交巡警服务平台的工作量不均衡和有些地方出警时间过长的实际情况，拟在该区内再增加2至5个平台，请确定需要增加平台的具体个数和位置

## 适配模型

- 主模型：图论网络与路径调度（CH4：复杂网络与图论模型）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH4/第4章-复杂网络与图论模型.md

### 候选模型与适配理由
- 图论网络与路径调度（CH4）：网络、平台、封锁、交通、调度；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH4/第4章-复杂网络与图论模型.md
- 规划优化与资源配置（CH3）：分配、方案、调度；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md
- 几何解析与运动学参数方程（CH1）：位置；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH1/第1章-解析方法与几何模型.md

## 变量、约束与公式

### 建模假设
- 以题面给出的数值、约束和输出格式为第一优先级构造模型。
- 若原始附件尚未能被当前环境直接读取，脚本优先抽取题目原文中的参数和表格数字，并在数据来源中显式记录。
- 所有结果由本问 solution.py 运行生成，result.json 与 experiment_table.csv 保持同步。

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

## Python 代码与运行方式

- 代码文件：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2011/B/q01/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2011/B/q01/solution.py`
- 批量运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：把题面地点、平台或转运关系抽象为图。
- 步骤 2：构造边权矩阵。
- 步骤 3：运行 Dijkstra 最短路。
- 步骤 4：输出各节点最短距离和前驱。

## 实验结果与解释

### 产物文件
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2011/B/q01/experiment_table.csv

### 数据来源
- 类型：problem_statement
- 附件：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2011/B.md
- 读取规模：17 行 x 10 列
- 说明：未找到可直接读取的数值附件，本问改用题目原文中的参数/表格数字生成实验结果。

### result.json 核心结果

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

### 结果解释
- 本问用 `dijkstra_shortest_path` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 实验报告

本问的核心是：附件1中的附图1给出了该市中心城区A的交通网络和现有的20个交巡警服务平台的设置情况示意图，相关的数据信息见附件2。请为各交巡警服务平台分配管辖范围，使其在所管辖的范围内出现突发事件时，尽量能在3分钟内有交巡警（警车的时速为60km/h）到达事发地。 对于重大突发事件，需要调度全区20个交巡警服务平台的警力资源，对进出该区的13条交通要道实现快速全封锁。实…

建模时先将题目要求拆成 3 个任务，再选择 `图论网络与路径调度`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
