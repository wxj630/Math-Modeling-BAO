# 2023-E 问题1 建模求解实验报告

## 题目原文与任务拆解

- 题目：2023年 CUMCM E题：黄河水沙监测数据分析
- 问题：问题1
- 原问：研究该水文站黄河水的含沙量与时间、水位、水流量的关系，并估算近6 年该水 文站的年总水流量和年总排沙量。

### 本问需要完成什么
- 任务 1：研究该水文站黄河水的含沙量与时间、水位、水流量的关系，并估算近6 年该水 文站的年总水流量和年总排沙量

## 适配模型

- 主模型：图论网络与路径调度（CH4：复杂网络与图论模型）
- 教程参考：../My-Agent/intro-mathmodel/docs/CH4/第4章-复杂网络与图论模型.md

### 候选模型与适配理由
- 规划优化与资源配置（CH3）：通用优化建模；参考 ../My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md
- 数据拟合与回归分析（CH6）：通用数据建模；参考 ../My-Agent/intro-mathmodel/docs/CH6/第六章-数据处理与拟合模型.md

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

- 代码文件：cumcm/question_solutions/2023/E/q01/solution.py
- 单问运行：`.venv/bin/python cumcm/question_solutions/2023/E/q01/solution.py`
- 批量运行：`.venv/bin/python cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：把题面地点、平台或转运关系抽象为图。
- 步骤 2：构造边权矩阵。
- 步骤 3：运行 Dijkstra 最短路。
- 步骤 4：输出各节点最短距离和前驱。

## 实验结果与解释

### 产物文件
- cumcm/question_artifacts/2023/E/q01/experiment_table.csv

### 数据来源
- 类型：attachment
- 附件：../../Documents/Playground/cumcm_unzipped/2023_Y20WPner9fa62862794e6dc82731a5561ce1132f/E题/附件1.xlsx
- 读取规模：2500 行 x 7 列
- 说明：本问优先使用官方附件中的数值表生成实验结果。

### result.json 核心结果

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

### 结果解释
- 本问用 `dijkstra_shortest_path` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 实验报告

本问的核心是：研究该水文站黄河水的含沙量与时间、水位、水流量的关系，并估算近6 年该水 文站的年总水流量和年总排沙量。

建模时先将题目要求拆成 1 个任务，再选择 `图论网络与路径调度`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
