# 2018-B 问题 3 建模求解实验报告

## 题目原文与任务拆解

- 题目：2018年 CUMCM B题：赛题
- 问题：问题 3
- 原问：CNC在加工过程中可能发生故障（据统计：故障的发生概率约为1%）的情况，每次故障排除（人工处理，未完成的物料报废）时间介于10~20分钟之间，故障排除后即刻加入作业序列。要求分别考虑一道工序和两道工序的物料加工作业情况。 请你们团队完成下列两项任务： 任务1：对一般问题进行研究，给出RGV动态调度模型和相应的求解算法； 任务2：利用表1中系统作业参数的3组数据分别检验模型的实用性和算法的有效性，给出RGV的调度策略和系统的作业效率，并将具体的结果分别填入附件2的EXCEL表中。

### 本问需要完成什么
- 任务 1：请你们团队完成下列两项任务： 任务1：对一般问题进行研究，给出RGV动态调度模型和相应的求解算法
- 任务 2：任务2：利用表1中系统作业参数的3组数据分别检验模型的实用性和算法的有效性，给出RGV的调度策略和系统的作业效率，并将具体的结果分别填入附件2的EXCEL表中

## 适配模型

- 主模型：RGV离散事件仿真与动态调度（CH2：微分方程与动力系统）
- 教程参考：../My-Agent/intro-mathmodel/docs/CH2/第2章-微分方程与动力系统.md

### 候选模型与适配理由
- 概率统计与抽样检验（CH9）：概率、检验；参考 ../My-Agent/intro-mathmodel/docs/CH9/第九章-机器学习与统计模型.md
- 规划优化与资源配置（CH3）：策略、调度；参考 ../My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md
- 数据拟合与回归分析（CH6）：数据、参数；参考 ../My-Agent/intro-mathmodel/docs/CH6/第六章-数据处理与拟合模型.md

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

- 代码文件：cumcm/question_solutions/2018/B/q03/solution.py
- 单问运行：`.venv/bin/python cumcm/question_solutions/2018/B/q03/solution.py`
- 批量运行：`.venv/bin/python cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：在一道工序和两道工序最优/准最优调度基础上加入1%故障概率。
- 步骤 2：用固定随机种子为三组参数分别生成可复现故障事件，维修时间在10至20分钟内抽样。
- 步骤 3：故障发生后报废当前物料，CNC维修结束后重新参与调度。
- 步骤 4：输出6个场景的完成数、故障数、报废数和故障事件表。

## 实验结果与解释

### 产物文件
- cumcm/question_artifacts/2018/B/q03/fault_scenario_summary.csv
- cumcm/question_artifacts/2018/B/q03/fault_events.csv
- cumcm/question_artifacts/2018/B/q03/fault_single_process_schedule.csv
- cumcm/question_artifacts/2018/B/q03/fault_two_process_schedule.csv
- cumcm/question_artifacts/2018/B/q03/experiment_table.csv

### 数据来源
- 类型：problem_statement_and_output_templates
- 附件：../../Documents/Playground/cumcm_unzipped/2018_lcGi8NeCd14458641de55ec1d705ea01714ff2dd/2018-B-Chinese/CUMCM-2018-Problem-B-Chinese-Appendix-2/Case_1_result.xls; ../../Documents/Playground/cumcm_unzipped/2018_lcGi8NeCd14458641de55ec1d705ea01714ff2dd/2018-B-Chinese/CUMCM-2018-Problem-B-Chinese-Appendix-2/Case_2_result.xls; ../../Documents/Playground/cumcm_unzipped/2018_lcGi8NeCd14458641de55ec1d705ea01714ff2dd/2018-B-Chinese/CUMCM-2018-Problem-B-Chinese-Appendix-2/Case_3_result_1.xls; ../../Documents/Playground/cumcm_unzipped/2018_lcGi8NeCd14458641de55ec1d705ea01714ff2dd/2018-B-Chinese/CUMCM-2018-Problem-B-Chinese-Appendix-2/Case_3_result_2.xls
- 读取规模：33 行 x 11 列
- 说明：本题专用算法使用题面表1三组RGV/CNC作业参数进行离散事件仿真；附件2的Case_*.xls为空白结果模板，用于确定输出字段。

### result.json 核心结果

```json
{
  "method": "rgv_fault_tolerant_discrete_event_schedule",
  "scenario_count": 6,
  "fault_probability": 0.01,
  "total_finished_count": 1800,
  "total_fault_count": 30,
  "total_scrap_count": 30,
  "case_summaries": [
    {
      "case": 1,
      "mode": "single_process",
      "finished_count": 376,
      "fault_count": 4,
      "scrap_count": 4,
      "efficiency": 0.914842,
      "rgv_busy_rate": 0.595,
      "last_unload_start_s": 28757.0
    },
    {
      "case": 1,
      "mode": "two_process",
      "stage1_cnc": "1,3,5,7",
      "stage2_cnc": "2,4,6,8",
      "finished_count": 245,
      "fault_count": 7,
      "scrap_count": 7,
      "efficiency": 0.850694,
      "rgv_busy_rate": 0.795764,
      "last_unload_start_s": 28769.030141
    },
    {
      "case": 2,
      "mode": "single_process",
      "finished_count": 369,
      "fault_count": 0,
      "scrap_count": 0,
      "efficiency": 0.929471,
      "rgv_busy_rate": 0.634236,
      "last_unload_start_s": 28678.0
    },
    {
      "case": 2,
      "mode": "two_process",
      "stage1_cnc": "1,2,7,8",
      "stage2_cnc": "3,4,5,6",
      "finished_count": 202,
      "fault_count": 10,
      "scrap_count": 10,
      "efficiency": 0.878261,
      "rgv_busy_rate": 0.897465,
      "last_unload_start_s": 28775.326307
    },
    {
      "case": 3,
      "mode": "single_process",
      "finished_count": 384,
      "fault_count": 5,
      "scrap_count": 5,
      "efficiency": 0.909953,
      "rgv_busy_rate": 0.663646,
      "last_unload_start_s": 28791.109077
    },
    {
      "case": 3,
      "mode": "two_process",
      "stage1_cnc": "2,5,6,8",
      "stage2_cnc": "1,3,4,7",
      "finished_count": 224,
      "fault_count": 4,
      "scrap_count": 4,
      "efficiency": 0.885375,
      "rgv_busy_rate": 0.978264,
      "last_unload_start_s": 28796.398507
    }
  ],
  "report": [
    "问题3在一道工序和两道工序调度上加入CNC随机故障事件，并使用固定种子保证结果可复现。",
    "故障件按题意报废，CNC在10至20分钟维修完成后重新进入调度；`fault_events.csv` 给出每次故障的CNC、时间和维修时长。",
    "输出6个场景的汇总表，并分别保留故障下一道工序和两道工序的调度明细。",
    "通用线性规划基线保留在 `cumcm/generic_baselines`，本问专用结果展示了从无故障调度到随机故障仿真的推进过程。"
  ]
}
```

### 结果解释
- 本问用 `rgv_fault_tolerant_discrete_event_schedule` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 专用实验报告

- 问题3在一道工序和两道工序调度上加入CNC随机故障事件，并使用固定种子保证结果可复现。
- 故障件按题意报废，CNC在10至20分钟维修完成后重新进入调度；`fault_events.csv` 给出每次故障的CNC、时间和维修时长。
- 输出6个场景的汇总表，并分别保留故障下一道工序和两道工序的调度明细。
- 通用线性规划基线保留在 `cumcm/generic_baselines`，本问专用结果展示了从无故障调度到随机故障仿真的推进过程。

## 实验报告

本问的核心是：CNC在加工过程中可能发生故障（据统计：故障的发生概率约为1%）的情况，每次故障排除（人工处理，未完成的物料报废）时间介于10~20分钟之间，故障排除后即刻加入作业序列。要求分别考虑一道工序和两道工序的物料加工作业情况。 请你们团队完成下列两项任务： 任务1：对一般问题进行研究，给出RGV动态调度模型和相应的求解算法； 任务2：利用表1中系统作业参数的3组…

建模时先将题目要求拆成 2 个任务，再选择 `RGV离散事件仿真与动态调度`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
