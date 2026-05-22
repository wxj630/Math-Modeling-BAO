# 2022-D 问题 2 建模求解实验报告

## 题目原文与任务拆解

- 题目：2022年 CUMCM D题：气象报文信息卫星通信传输
- 问题：问题 2
- 原问：为了提高气象信息的地理密度，除了实现主站间气象报文的信息共享外，还需要 使用副站气象信息加以补充。 (1) 若要求在 𝐾 分钟内完成 𝑁 个主站间气象报文的信息共享，且每个主站满足条件：对 每支分队， 成功接收该分队至少一个副站的气象报文的概率不低于0.9。 请就 𝐾 (≥ 5) 的情形， 研究 𝑁 的最大值与 𝐾 的关系，并建立 𝐾 分钟内满足以上条件的信息传输的一般模型。若主 站间气象报文信息共享的传输方案与问题 1 相同，则只需给出副站气象报文的传输方案。 (2) 对于 𝐾 = 7， 给出 𝑁 的最大值， 并根据一般传输模型给出此时副站气象报文的传输方 案，将结果按表 2 的格式填报。求出在你们的传输方案下平均有多少个主站能成功接收每支分 队至少一个副站的气象报文，以及任一主站平均能成功接收多少个副站的气象报文。

### 本问需要完成什么
- 任务 1：(1) 若要求在 𝐾 分钟内完成 𝑁 个主站间气象报文的信息共享，且每个主站满足条件：对 每支分队， 成功接收该分队至少一个副站的气象报文的概率不低于0.9。 请就 𝐾 (≥ 5) 的情形， 研究 𝑁 的最大值与 𝐾 的关系，并建立 𝐾 分钟内满足以上条件的信息传输的一般模型。若主 站间气象报文信息共享的传输方案与问题 1 相同，则只需给出副站气象报文的传输方案
- 任务 2：(2) 对于 𝐾 = 7， 给出 𝑁 的最大值， 并根据一般传输模型给出此时副站气象报文的传输方 案，将结果按表 2 的格式填报。求出在你们的传输方案下平均有多少个主站能成功接收每支分 队至少一个副站的气象报文，以及任一主站平均能成功接收多少个副站的气象报文

## 适配模型

- 主模型：规划优化与资源配置（CH3：函数极值与规划模型）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md

### 候选模型与适配理由
- 规划优化与资源配置（CH3）：最大、方案；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md
- 概率统计与抽样检验（CH9）：概率；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH9/第九章-机器学习与统计模型.md

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
- `q(t)=1-(1-p)^t，其中 t 为某分队副站对某主站的独立发送次数。`
- `q(t)>=threshold => t>=ceil(log(1-threshold)/log(1-p))`
- `2K >= tN => N_max=floor(2K/t)`
- `slot=(receiver-1)t+(repeat-1), round=floor(slot/2)+1, substation=a/b 按 slot 奇偶分配。`

## Python 代码与运行方式

- 代码文件：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2022/D/q02/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2022/D/q02/solution.py`
- 批量运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：先沿用问题 1 的主站轮转方案完成主站间报文共享。
- 步骤 2：计算达到概率阈值所需的副站重复发送次数 t。
- 步骤 3：用每支分队两个副站共 2K 次发送容量推导 N 最大值。
- 步骤 4：按时隙构造副站发送表，并校验每个便携副站每分钟最多发送 1 条消息。
- 步骤 5：计算期望成功主站数和任一主站期望收到的副站报文数。

## 实验结果与解释

### 产物文件
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2022/D/q02/experiment_table.csv

### 数据来源
- 类型：problem_statement
- 附件：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2022/D.md
- 读取规模：28 行 x 7 列
- 说明：未找到可直接读取的数值附件，本问改用题目原文中的参数/表格数字生成实验结果。

### result.json 核心结果

```json
{
  "method": "portable_substation_repeated_transmission_plan",
  "K": 7,
  "threshold": 0.9,
  "portable_success_probability": 0.8,
  "required_repeats_per_team_receiver": 2,
  "N_max": 7,
  "probability_at_least_one_sub_report": 0.96,
  "expected_successful_main_stations_per_team": 6.72,
  "expected_substation_reports_per_main": 11.2,
  "schedule_feasibility": {
    "feasible": true,
    "sender_minute_conflicts": 0,
    "team_receiver_repeat_mismatches": 0,
    "max_round_used": 7,
    "round_limit": 7,
    "transmissions_per_team": 14,
    "capacity_per_team": 14
  },
  "table2_rows": 98,
  "sample_rows": [
    {
      "round": 1,
      "sender": "1a",
      "receiver": 1,
      "message_origin": "1a",
      "team": 1,
      "repeat_index": 1,
      "slot_index": 1
    },
    {
      "round": 1,
      "sender": "1b",
      "receiver": 1,
      "message_origin": "1b",
      "team": 1,
      "repeat_index": 2,
      "slot_index": 2
    },
    {
      "round": 1,
      "sender": "2a",
      "receiver": 1,
      "message_origin": "2a",
      "team": 2,
      "repeat_index": 1,
      "slot_index": 1
    },
    {
      "round": 1,
      "sender": "2b",
      "receiver": 1,
      "message_origin": "2b",
      "team": 2,
      "repeat_index": 2,
      "slot_index": 2
    },
    {
      "round": 1,
      "sender": "3a",
      "receiver": 1,
      "message_origin": "3a",
      "team": 3,
      "repeat_index": 1,
      "slot_index": 1
    },
    {
      "round": 1,
      "sender": "3b",
      "receiver": 1,
      "message_origin": "3b",
      "team": 3,
      "repeat_index": 2,
      "slot_index": 2
    },
    {
      "round": 1,
      "sender": "4a",
      "receiver": 1,
      "message_origin": "4a",
      "team": 4,
      "repeat_index": 1,
      "slot_index": 1
    },
    {
      "round": 1,
      "sender": "4b",
      "receiver": 1,
      "message_origin": "4b",
      "team": 4,
      "repeat_index": 2,
      "slot_index": 2
    },
    {
      "round": 1,
      "sender": "5a",
      "receiver": 1,
      "message_origin": "5a",
      "team": 5,
      "repeat_index": 1,
      "slot_index": 1
    },
    {
      "round": 1,
      "sender": "5b",
      "receiver": 1,
      "message_origin": "5b",
      "team": 5,
      "repeat_index": 2,
      "slot_index": 2
    },
    {
      "round": 1,
      "sender": "6a",
      "receiver": 1,
      "message_origin": "6a",
      "team": 6,
      "repeat_index": 1,
      "slot_index": 1
    },
    {
      "round": 1,
      "sender": "6b",
      "receiver": 1,
      "message_origin": "6b",
      "team": 6,
      "repeat_index": 2,
      "slot_index": 2
    }
  ]
}
```

### 结果解释
- 本问用 `portable_substation_repeated_transmission_plan` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 实验报告

本问的核心是：为了提高气象信息的地理密度，除了实现主站间气象报文的信息共享外，还需要 使用副站气象信息加以补充。 (1) 若要求在 𝐾 分钟内完成 𝑁 个主站间气象报文的信息共享，且每个主站满足条件：对 每支分队， 成功接收该分队至少一个副站的气象报文的概率不低于0.9。 请就 𝐾 (≥ 5) 的情形， 研究 𝑁 的最大值与 𝐾 的关系，并建立 𝐾 分钟内满足以上条件的…

建模时先将题目要求拆成 2 个任务，再选择 `规划优化与资源配置`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
