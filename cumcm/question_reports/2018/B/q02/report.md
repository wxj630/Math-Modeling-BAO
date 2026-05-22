# 2018-B 问题 2 建模求解实验报告

## 题目原文与任务拆解

- 题目：2018年 CUMCM B题：赛题
- 问题：问题 2
- 原问：两道工序的物料加工作业情况，每个物料的第一和第二道工序分别由两台不同的CNC依次加工完成；

### 本问需要完成什么
- 任务 1：两道工序的物料加工作业情况，每个物料的第一和第二道工序分别由两台不同的CNC依次加工完成

## 适配模型

- 主模型：RGV离散事件仿真与动态调度（CH3：函数极值与规划模型）
- 教程参考：../My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md

### 候选模型与适配理由
- 规划优化与资源配置（CH3）：通用优化建模；参考 ../My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md
- 数据拟合与回归分析（CH6）：通用数据建模；参考 ../My-Agent/intro-mathmodel/docs/CH6/第六章-数据处理与拟合模型.md

## 变量、约束与公式

### 建模假设
- 8台CNC按1/2、3/4、5/6、7/8成对分布在4个轨道站位，RGV初始位于CNC1/2站位。
- RGV移动1/2/3个站位的时间、奇偶号CNC上下料时间、清洗时间和加工时间均采用题面表1的三组参数。
- 一道工序中所有CNC等价；两道工序中枚举4台CNC执行工序1、其余4台执行工序2，并用完成件队列连接两道工序。
- 调度采用滚动贪心：在当前时刻选择可服务或最早可服务的CNC，使服务开始时间最早；同一CNC完成件下料和下一件上料合并为一次上下料作业。
- 故障情形使用固定随机种子的离散事件仿真；每次装入CNC的加工任务以1%概率在加工期间故障，故障件报废，维修时间在10至20分钟内均匀取样。

### 变量定义
- x_k: 第k次RGV服务选择的CNC编号
- p_i: CNC i所在轨道站位
- s_k: 第k次上/下料开始时间
- r_i(t): CNC i在时刻t的可服务状态（空闲、加工、待下料、维修）
- Q(t): 两道工序中等待进入工序2的半成品队列
- F_j: 第j次故障事件的CNC、开始时间、结束时间和报废物料编号

### 约束条件
- 0 <= s_k <= 28800秒，班次连续作业8小时。
- RGV从站位a到b的移动时间为题面表1中 |a-b| 对应移动时间。
- CNC加工任务必须先上料，经过上下料时间和加工时间后才可下料。
- 两道工序物料必须先完成工序1并进入等待队列，再由不同CNC完成工序2。
- 故障任务不产生合格成品，维修结束后CNC重新进入可调度序列。

### 模型公式 / 目标函数
- `travel(a,b)=T_{|a-b|}`
- `ready_i = load_start_i + service_i + process_time_i`
- `single-process objective: max N_finished over 0<=t<=28800`
- `two-process objective: max N_finished with stage1/stage2 partition and FIFO semi-finished queue`
- `efficiency = N_finished / floor(8*28800 / process_time_bottleneck)`
- `fault repair time U(600,1200), P(fault per loaded job)=0.01`

## Python 代码与运行方式

- 代码文件：cumcm/question_solutions/2018/B/q02/solution.py
- 单问运行：`.venv/bin/python cumcm/question_solutions/2018/B/q02/solution.py`
- 批量运行：`.venv/bin/python cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：枚举8台CNC中4台承担工序1、4台承担工序2的所有划分。
- 步骤 2：对每个划分运行两道工序离散事件仿真，用FIFO队列传递半成品。
- 步骤 3：按班次完成成品数选择最优划分，输出每个成品两道工序的CNC与上下料时间。
- 步骤 4：比较三组参数下的瓶颈工序、完成数和设备效率。

## 实验结果与解释

### 产物文件
- cumcm/question_artifacts/2018/B/q02/two_process_schedule_all_cases.csv
- cumcm/question_artifacts/2018/B/q02/two_process_summary.csv
- cumcm/question_artifacts/2018/B/q02/experiment_table.csv

### 数据来源
- 类型：problem_statement_and_output_templates
- 附件：../../Documents/Playground/cumcm_unzipped/2018_lcGi8NeCd14458641de55ec1d705ea01714ff2dd/2018-B-Chinese/CUMCM-2018-Problem-B-Chinese-Appendix-2/Case_1_result.xls; ../../Documents/Playground/cumcm_unzipped/2018_lcGi8NeCd14458641de55ec1d705ea01714ff2dd/2018-B-Chinese/CUMCM-2018-Problem-B-Chinese-Appendix-2/Case_2_result.xls; ../../Documents/Playground/cumcm_unzipped/2018_lcGi8NeCd14458641de55ec1d705ea01714ff2dd/2018-B-Chinese/CUMCM-2018-Problem-B-Chinese-Appendix-2/Case_3_result_1.xls; ../../Documents/Playground/cumcm_unzipped/2018_lcGi8NeCd14458641de55ec1d705ea01714ff2dd/2018-B-Chinese/CUMCM-2018-Problem-B-Chinese-Appendix-2/Case_3_result_2.xls
- 读取规模：33 行 x 11 列
- 说明：本题专用算法使用题面表1三组RGV/CNC作业参数进行离散事件仿真；附件2的Case_*.xls为空白结果模板，用于确定输出字段。

### result.json 核心结果

```json
{
  "method": "rgv_two_process_discrete_event_schedule",
  "scenario_count": 3,
  "best_case": 1,
  "best_finished_count": 262,
  "best_stage1_cnc": [
    1,
    3,
    5,
    7
  ],
  "best_stage2_cnc": [
    2,
    4,
    6,
    8
  ],
  "case_summaries": [
    {
      "case": 1,
      "mode": "two_process",
      "stage1_cnc": "1,3,5,7",
      "stage2_cnc": "2,4,6,8",
      "finished_count": 262,
      "fault_count": 0,
      "scrap_count": 0,
      "efficiency": 0.909722,
      "rgv_busy_rate": 0.796111,
      "last_unload_start_s": 28783.0
    },
    {
      "case": 2,
      "mode": "two_process",
      "stage1_cnc": "1,2,7,8",
      "stage2_cnc": "3,4,5,6",
      "finished_count": 210,
      "fault_count": 0,
      "scrap_count": 0,
      "efficiency": 0.913043,
      "rgv_busy_rate": 0.956771,
      "last_unload_start_s": 28788.0
    },
    {
      "case": 3,
      "mode": "two_process",
      "stage1_cnc": "2,5,6,8",
      "stage2_cnc": "1,3,4,7",
      "finished_count": 231,
      "fault_count": 0,
      "scrap_count": 0,
      "efficiency": 0.913043,
      "rgv_busy_rate": 0.978507,
      "last_unload_start_s": 28682.0
    }
  ],
  "report": [
    "两道工序先枚举CNC分工，再用离散事件仿真评价每种分工在8小时内的成品数。",
    "半成品按FIFO队列进入工序2，保证每件物料先完成工序1再进入不同CNC执行工序2。",
    "输出 `two_process_schedule_all_cases.csv`，包含每件成品两道工序的CNC编号、上料和下料开始时间。",
    "该专用模型对应教程中的规划优化和离散仿真思路，通用基线继续集中保留在 `cumcm/generic_baselines`。"
  ]
}
```

### 结果解释
- 本问用 `rgv_two_process_discrete_event_schedule` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 专用实验报告

- 两道工序先枚举CNC分工，再用离散事件仿真评价每种分工在8小时内的成品数。
- 半成品按FIFO队列进入工序2，保证每件物料先完成工序1再进入不同CNC执行工序2。
- 输出 `two_process_schedule_all_cases.csv`，包含每件成品两道工序的CNC编号、上料和下料开始时间。
- 该专用模型对应教程中的规划优化和离散仿真思路，通用基线继续集中保留在 `cumcm/generic_baselines`。

## 实验报告

本问的核心是：两道工序的物料加工作业情况，每个物料的第一和第二道工序分别由两台不同的CNC依次加工完成；

建模时先将题目要求拆成 1 个任务，再选择 `RGV离散事件仿真与动态调度`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
