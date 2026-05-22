# 2017-D 问题1 建模求解实验报告

## 题目原文与任务拆解

- 题目：2017年 CUMCM D题：巡检线路的排班
- 问题：问题1
- 原问：如果采用固定上班时间，不考虑巡检人员的休息时间，采用每天三班倒，每班工作8小时左右，每班需要多少人，巡检线路如何安排，并给出巡检人员的巡检线路和巡检的时间表。

### 本问需要完成什么
- 任务 1：如果采用固定上班时间，不考虑巡检人员的休息时间，采用每天三班倒，每班工作8小时左右，每班需要多少人，巡检线路如何安排，并给出巡检人员的巡检线路和巡检的时间表

## 适配模型

- 主模型：周期巡检路径排班与人员优化（CH4：复杂网络与图论模型）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH4/第4章-复杂网络与图论模型.md

### 候选模型与适配理由
- 图论网络与路径调度（CH4）：附件给出巡检点连通关系，必须先用最短路把厂区路网转化为任意点间通行时间。；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH4/第4章-复杂网络与图论模型.md
- 规划优化与资源配置（CH3）：每问都要在周期、班次、休息和人员数量约束下安排路线，本质是资源配置与排班优化。；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md

## 变量、约束与公式

### 建模假设
- 调度中心为题面给定的 XJ-0022，巡检人员每次从调度中心领取任务后出发，完成后返回调度中心。
- 附件的连通关系为无向通行边，任意两点通行时间用 Floyd 最短路折算。
- 每个巡检点的周期约束按24小时循环检查：相邻两次实际巡检间隔不能超过附件给出的周期。
- 固定三班倒采用 00:00-08:00、08:00-16:00、16:00-24:00 三个8小时班次。
- 错时上班允许工人按任务出发时间滚动开班，但单名工人连续工作窗口不超过8小时。
- 问题2的休息与进餐作为工人时间表中的独立事件记录；通用基线仍保留在 cumcm/generic_baselines 中作对照。

### 变量定义
- G=(V,E): 26个巡检点和31条连通边构成的厂区通行图
- d_ij: 点i到点j的最短通行时间
- c_i: 巡检点i的最大巡检周期
- s_i: 巡检点i单次巡检耗时
- t_{i,k}: 巡检点i第k次巡检开始时间
- x_{w,r}: 工人w在路线r中服务的巡检任务序列
- m_b: 班次b需要的巡检人数

### 约束条件
- 0 <= t_{i,k} < 1440，所有时间以当天分钟计。
- t_{i,k+1}-t_{i,k} <= c_i，跨日间隔 1440-t_{i,last}+t_{i,first} <= c_i。
- 每次巡检需要一名工人，服务区间为 [t_{i,k}, t_{i,k}+s_i]。
- 工人相邻任务之间必须满足最短路通行时间；班次按8小时左右执行，首尾允许少量交接弹性以优先满足巡检周期。
- 问题2中每名工人约2小时安排一次5-10分钟休息，12:00和18:00左右安排30分钟进餐。
- 问题3中错峰方案的单人工作窗口不超过8小时，并与固定三班倒人数做同口径比较。

### 模型公式 / 目标函数
- `minimize sum_b m_b subject to all periodic inspection constraints`
- `d_ij = shortest_path_time(i,j; G)`
- `route_time = d_{22,i_1}+s_{i_1}+sum_h(d_{i_h,i_{h+1}}+s_{i_{h+1}})+d_{i_last,22}`
- `cycle_violation_i=max(0, max_gap_i-c_i)`
- `workload_balance = std(worker_service_minutes)`

## Python 代码与运行方式

- 代码文件：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2017/D/q01/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2017/D/q01/solution.py`
- 批量运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：读取附件基本信息和连通关系，构建26点31边无向图。
- 步骤 2：对路网运行 Floyd 最短路，得到调度中心到每个巡检点以及点间通行时间。
- 步骤 3：在每个8小时班次内按周期把巡检任务均匀展开，形成带出发/返回时间的中心往返巡检区间。
- 步骤 4：用区间分配贪心法给每个班次安排最少可行工人，并输出每名工人的巡检路线与时间表。

## 实验结果与解释

### 产物文件
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2017/D/q01/inspection_fixed_shift_timetable.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2017/D/q01/inspection_fixed_shift_summary.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2017/D/q01/inspection_cycle_check.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2017/D/q01/experiment_table.csv

### 数据来源
- 类型：attachment
- 附件：/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2017_IqAO5Qqi8f23d8738a07a0604b8629ce9bb061ad/CUMCM2017Problems/D/CUMCM-2017-appendix-D.xlsx
- 读取规模：58 行 x 6 列
- 说明：本题专用算法读取26个巡检点的周期/耗时和31条连通边，构建最短路网络并生成固定班次、带休息班次和错峰班次巡检时间表。

### result.json 核心结果

```json
{
  "method": "inspection_fixed_shift_route_schedule",
  "point_count": 26,
  "edge_count": 31,
  "shift_count": 3,
  "total_workers": 72,
  "workers_by_shift": {
    "B1:00:00-08:00": 24,
    "B2:08:00-16:00": 24,
    "B3:16:00-00:00": 24
  },
  "scheduled_visit_count": 948,
  "rest_event_count": 0,
  "meal_event_count": 0,
  "mean_service_minutes_per_worker": 34.375,
  "service_workload_std": 13.17451,
  "max_cycle_gap_minutes": 240.0,
  "max_cycle_violation_minutes": 0.0,
  "report": [
    "问题1把26个巡检点按附件周期在三个固定8小时班次内均匀展开，并用调度中心往返的最短路径形成可执行时间表。",
    "每条记录给出出发、到点、巡检、返回中心时间，以及中心到巡检点的最短路节点序列。",
    "周期检查表显示24小时循环最大间隔不超过附件周期，满足所有点按要求巡检。",
    "通用基线保留在 `cumcm/generic_baselines`，当前结果是从通用时间序列推进到附件路网排班模型的专用版本。"
  ]
}
```

### 结果解释
- 本问用 `inspection_fixed_shift_route_schedule` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 专用实验报告

- 问题1把26个巡检点按附件周期在三个固定8小时班次内均匀展开，并用调度中心往返的最短路径形成可执行时间表。
- 每条记录给出出发、到点、巡检、返回中心时间，以及中心到巡检点的最短路节点序列。
- 周期检查表显示24小时循环最大间隔不超过附件周期，满足所有点按要求巡检。
- 通用基线保留在 `cumcm/generic_baselines`，当前结果是从通用时间序列推进到附件路网排班模型的专用版本。

## 实验报告

本问的核心是：如果采用固定上班时间，不考虑巡检人员的休息时间，采用每天三班倒，每班工作8小时左右，每班需要多少人，巡检线路如何安排，并给出巡检人员的巡检线路和巡检的时间表。

建模时先将题目要求拆成 1 个任务，再选择 `周期巡检路径排班与人员优化`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
