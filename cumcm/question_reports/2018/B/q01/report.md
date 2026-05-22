# 2018-B 问题 1 建模求解实验报告

## 题目原文与任务拆解

- 题目：2018年 CUMCM B题：赛题
- 问题：问题 1
- 原问：一道工序的物料加工作业情况，每台CNC安装同样的刀具，物料可以在任一台CNC上加工完成；

### 本问需要完成什么
- 任务 1：一道工序的物料加工作业情况，每台CNC安装同样的刀具，物料可以在任一台CNC上加工完成

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

- 代码文件：cumcm/question_solutions/2018/B/q01/solution.py
- 单问运行：`.venv/bin/python cumcm/question_solutions/2018/B/q01/solution.py`
- 批量运行：`.venv/bin/python cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：读取附件2空白模板并确认需要填报的列；实际参数使用题面表1三组作业参数。
- 步骤 2：对每组参数运行一道工序离散事件仿真，RGV每步选择最早可开始服务的CNC。
- 步骤 3：记录每个完成物料的CNC编号、上料开始时间、下料开始时间，并计算作业效率。
- 步骤 4：输出三组参数的调度明细和汇总表。

## 实验结果与解释

### 产物文件
- cumcm/question_artifacts/2018/B/q01/single_process_schedule_all_cases.csv
- cumcm/question_artifacts/2018/B/q01/single_process_summary.csv
- cumcm/question_artifacts/2018/B/q01/experiment_table.csv

### 数据来源
- 类型：problem_statement_and_output_templates
- 附件：../../Documents/Playground/cumcm_unzipped/2018_lcGi8NeCd14458641de55ec1d705ea01714ff2dd/2018-B-Chinese/CUMCM-2018-Problem-B-Chinese-Appendix-2/Case_1_result.xls; ../../Documents/Playground/cumcm_unzipped/2018_lcGi8NeCd14458641de55ec1d705ea01714ff2dd/2018-B-Chinese/CUMCM-2018-Problem-B-Chinese-Appendix-2/Case_2_result.xls; ../../Documents/Playground/cumcm_unzipped/2018_lcGi8NeCd14458641de55ec1d705ea01714ff2dd/2018-B-Chinese/CUMCM-2018-Problem-B-Chinese-Appendix-2/Case_3_result_1.xls; ../../Documents/Playground/cumcm_unzipped/2018_lcGi8NeCd14458641de55ec1d705ea01714ff2dd/2018-B-Chinese/CUMCM-2018-Problem-B-Chinese-Appendix-2/Case_3_result_2.xls
- 读取规模：33 行 x 11 列
- 说明：本题专用算法使用题面表1三组RGV/CNC作业参数进行离散事件仿真；附件2的Case_*.xls为空白结果模板，用于确定输出字段。

### result.json 核心结果

```json
{
  "method": "rgv_single_process_discrete_event_schedule",
  "scenario_count": 3,
  "best_case": 3,
  "best_finished_count": 393,
  "best_utilization": 0.93128,
  "case_summaries": [
    {
      "case": 1,
      "mode": "single_process",
      "finished_count": 384,
      "fault_count": 0,
      "scrap_count": 0,
      "efficiency": 0.934307,
      "rgv_busy_rate": 0.580278,
      "last_unload_start_s": 28633.0
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
      "case": 3,
      "mode": "single_process",
      "finished_count": 393,
      "fault_count": 0,
      "scrap_count": 0,
      "efficiency": 0.93128,
      "rgv_busy_rate": 0.584271,
      "last_unload_start_s": 28609.0
    }
  ],
  "report": [
    "题面表1的三组参数全部进入离散事件仿真，附件2空白Excel模板只作为输出字段参照。",
    "一道工序把所有CNC视为同质并行机，RGV每步选择最早可开始上下料的CNC。",
    "输出 `single_process_schedule_all_cases.csv` 可直接填入附件2中每组参数的CNC编号、上料开始时间和下料开始时间。",
    "通用基线仍保留在 `cumcm/generic_baselines`，本结果是从粗二次拟合推进到RGV动态调度仿真的专用版本。"
  ]
}
```

### 结果解释
- 本问用 `rgv_single_process_discrete_event_schedule` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 专用实验报告

- 题面表1的三组参数全部进入离散事件仿真，附件2空白Excel模板只作为输出字段参照。
- 一道工序把所有CNC视为同质并行机，RGV每步选择最早可开始上下料的CNC。
- 输出 `single_process_schedule_all_cases.csv` 可直接填入附件2中每组参数的CNC编号、上料开始时间和下料开始时间。
- 通用基线仍保留在 `cumcm/generic_baselines`，本结果是从粗二次拟合推进到RGV动态调度仿真的专用版本。

## 实验报告

本问的核心是：一道工序的物料加工作业情况，每台CNC安装同样的刀具，物料可以在任一台CNC上加工完成；

建模时先将题目要求拆成 1 个任务，再选择 `RGV离散事件仿真与动态调度`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
