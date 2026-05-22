# 2022-D 问题 1 建模求解实验报告

## 题目原文与任务拆解

- 题目：2022年 CUMCM D题：气象报文信息卫星通信传输
- 问题：问题 1
- 原问：(1) 要求在 𝐾 分钟内完成 𝑁 (≥ 5) 支分队主站间气象报文的信息共享，请研究 𝐾 的最小值与 𝑁 的关系，并建立 𝐾 分钟内实现 𝑁 个主站间气象报文信息共享的一般传输 模型。 (2) 在上述模型中， 取 𝑁 = 9， 给出 𝐾 的相应最小值， 并根据一般传输模型给出此时主站 间气象报文的信息共享方案，将结果按表 1 的格式填报。填报结果时，注意消息的完整性，例 如：在“发送信息所属站点序号”一栏中填写“5”，表示本轮所发送消息来自于第 5 号主站，

### 本问需要完成什么
- 任务 1：(1) 要求在 𝐾 分钟内完成 𝑁 (≥ 5) 支分队主站间气象报文的信息共享，请研究 𝐾 的最小值与 𝑁 的关系，并建立 𝐾 分钟内实现 𝑁 个主站间气象报文信息共享的一般传输 模型
- 任务 2：(2) 在上述模型中， 取 𝑁 = 9， 给出 𝐾 的相应最小值， 并根据一般传输模型给出此时主站 间气象报文的信息共享方案，将结果按表 1 的格式填报。填报结果时，注意消息的完整性，例 如：在“发送信息所属站点序号”一栏中填写“5”，表示本轮所发送消息来自于第 5 号主站，

## 适配模型

- 主模型：规划优化与资源配置（CH3：函数极值与规划模型）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md

### 候选模型与适配理由
- 规划优化与资源配置（CH3）：最小、方案；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md

## 变量、约束与公式

### 建模假设
- 以题面给出的数值、约束和输出格式为第一优先级构造模型。
- 若原始附件尚未能被当前环境直接读取，脚本优先抽取题目原文中的参数和表格数字，并在数据来源中显式记录。
- 所有结果由本问 solution.py 运行生成，result.json 与 experiment_table.csv 保持同步。

### 变量定义
- N: 气象分队数量，也是主站数量
- K: 可用传输轮数/分钟数
- r: 传输轮数序号
- s_i: 第 i 个主站或副站
- m_j: 来源于第 j 个站点的气象报文
- p=0.8: 便携型卫星设备单次发送成功概率

### 约束条件
- 每个设备每分钟最多发送 1 条消息。
- 车载型主站收发成功率为 1；便携型副站发送成功率为 0.8。
- 主站间共享要求每个主站最终拥有所有 N 个主站报文。
- 副站补充要求每个主站对每支分队至少成功接收一个副站报文的概率达到阈值。

### 模型公式 / 目标函数
- `K_min(N)=N-1`
- `round r: 主站 i 将本站报文发送给 ((i+r-1) mod N)+1`
- `总发送次数 N(N-1)，每轮最多 N 次，因此下界 N-1 可由循环方案达到。`

## Python 代码与运行方式

- 代码文件：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2022/D/q01/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2022/D/q01/solution.py`
- 批量运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：建立主站完全信息共享的轮转传输模型。
- 步骤 2：证明每个主站需收到其余 N-1 个报文，因此 K>=N-1。
- 步骤 3：用循环接收者构造达到下界的传输方案。
- 步骤 4：对 N=9 输出表 1 形式的 8 轮传输计划。

## 实验结果与解释

### 产物文件
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2022/D/q01/experiment_table.csv

### 数据来源
- 类型：problem_statement
- 附件：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2022/D.md
- 读取规模：28 行 x 7 列
- 说明：未找到可直接读取的数值附件，本问改用题目原文中的参数/表格数字生成实验结果。

### result.json 核心结果

```json
{
  "method": "round_robin_main_station_broadcast",
  "N": 9,
  "K_min": 8,
  "general_relation": "K_min(N)=N-1",
  "proof": "每个主站必须接收其余 N-1 个主站报文；循环轮转每轮让每个主站发送一次，N-1 轮后每个主站恰好收到所有其他报文。",
  "table1_rows": 72,
  "sample_rows": [
    {
      "round": 1,
      "sender": 1,
      "receiver": 2,
      "message_origin": "1",
      "receiver_has_after_round": "2, plus message 1"
    },
    {
      "round": 1,
      "sender": 2,
      "receiver": 3,
      "message_origin": "2",
      "receiver_has_after_round": "3, plus message 2"
    },
    {
      "round": 1,
      "sender": 3,
      "receiver": 4,
      "message_origin": "3",
      "receiver_has_after_round": "4, plus message 3"
    },
    {
      "round": 1,
      "sender": 4,
      "receiver": 5,
      "message_origin": "4",
      "receiver_has_after_round": "5, plus message 4"
    },
    {
      "round": 1,
      "sender": 5,
      "receiver": 6,
      "message_origin": "5",
      "receiver_has_after_round": "6, plus message 5"
    },
    {
      "round": 1,
      "sender": 6,
      "receiver": 7,
      "message_origin": "6",
      "receiver_has_after_round": "7, plus message 6"
    },
    {
      "round": 1,
      "sender": 7,
      "receiver": 8,
      "message_origin": "7",
      "receiver_has_after_round": "8, plus message 7"
    },
    {
      "round": 1,
      "sender": 8,
      "receiver": 9,
      "message_origin": "8",
      "receiver_has_after_round": "9, plus message 8"
    },
    {
      "round": 1,
      "sender": 9,
      "receiver": 1,
      "message_origin": "9",
      "receiver_has_after_round": "1, plus message 9"
    },
    {
      "round": 2,
      "sender": 1,
      "receiver": 3,
      "message_origin": "1",
      "receiver_has_after_round": "3, plus message 1"
    },
    {
      "round": 2,
      "sender": 2,
      "receiver": 4,
      "message_origin": "2",
      "receiver_has_after_round": "4, plus message 2"
    },
    {
      "round": 2,
      "sender": 3,
      "receiver": 5,
      "message_origin": "3",
      "receiver_has_after_round": "5, plus message 3"
    }
  ]
}
```

### 结果解释
- 本问用 `round_robin_main_station_broadcast` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 实验报告

本问的核心是：(1) 要求在 𝐾 分钟内完成 𝑁 (≥ 5) 支分队主站间气象报文的信息共享，请研究 𝐾 的最小值与 𝑁 的关系，并建立 𝐾 分钟内实现 𝑁 个主站间气象报文信息共享的一般传输 模型。 (2) 在上述模型中， 取 𝑁 = 9， 给出 𝐾 的相应最小值， 并根据一般传输模型给出此时主站 间气象报文的信息共享方案，将结果按表 1 的格式填报。填报结果时，注意…

建模时先将题目要求拆成 2 个任务，再选择 `规划优化与资源配置`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
