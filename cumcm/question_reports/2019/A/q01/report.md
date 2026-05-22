# 2019-A 问题1 建模求解实验报告

## 题目原文与任务拆解

- 题目：2019年 CUMCM A题：高压油管的压力控制
- 问题：问题1
- 原问：某型号高压油管的内腔长度为500mm，内直径为10mm，供油入口A处小孔的直径为1.4mm，通过单向阀开关控制供油时间的长短，单向阀每打开一次后就要关闭10ms。喷油器每秒工作10次，每次工作时喷油时间为2.4ms，喷油器工作时从喷油嘴B处向外喷油的速率如图2所示。高压油泵在入口A处提供的压力恒为160 MPa，高压油管内的初始压力为100 MPa。如果要将高压油管内的压力尽可能稳定在100 MPa左右，如何设置单向阀每次开启的时长？如果要将高压油管内的压力从100 MPa增加到150 MPa，且分别经过约2 s、5 s和10 s的调整过程后稳定在150 MPa，单向阀开启的时长应如何调整？

### 本问需要完成什么
- 任务 1：某型号高压油管的内腔长度为500mm，内直径为10mm，供油入口A处小孔的直径为1.4mm，通过单向阀开关控制供油时间的长短，单向阀每打开一次后就要关闭10ms
- 任务 2：喷油器每秒工作10次，每次工作时喷油时间为2.4ms，喷油器工作时从喷油嘴B处向外喷油的速率如图2所示
- 任务 3：高压油泵在入口A处提供的压力恒为160 MPa，高压油管内的初始压力为100 MPa
- 任务 4：如果要将高压油管内的压力尽可能稳定在100 MPa左右，如何设置单向阀每次开启的时长？
- 任务 5：如果要将高压油管内的压力从100 MPa增加到150 MPa，且分别经过约2 s、5 s和10 s的调整过程后稳定在150 MPa，单向阀开启的时长应如何调整？

## 适配模型

- 主模型：高压油管质量守恒与压力控制仿真（CH2：微分方程与动力系统）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH2/第2章-微分方程与动力系统.md

### 候选模型与适配理由
- 微分方程与动态仿真（CH2）：油管压力由进油、喷油、减压阀回流和燃油弹性共同驱动，核心是连续时间动态仿真。；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH2/第2章-微分方程与动力系统.md
- 数据拟合与回归分析（CH6）：附件1-3需要插值拟合为凸轮导数、针阀升程和弹性模量函数后才能进入方程。；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH6/第六章-数据处理与拟合模型.md
- 规划优化与资源配置（CH3）：阀开时长、凸轮角速度和减压阀阈值都通过枚举/搜索最小化压力误差。；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md

## 变量、约束与公式

### 建模假设
- 高压油管视为等容腔体，内腔体积由题面500mm长度和10mm内径计算。
- 燃油密度随压力变化，按附件3弹性模量积分 d ln rho / dP = 1/E(P)，并以 rho(100MPa)=0.850 mg/mm3 定标。
- 进出流量采用题面小孔流量公式，流量系数取0.85，孔径和针阀几何参数来自题面。
- 喷油嘴针阀升程使用附件2；问题1缺少图2结构化数据时，用附件2升程曲线生成可复现喷油流量近似。
- 凸轮-柱塞供油使用附件1极径曲线，极径上升阶段折算为柱塞压油体积流量。
- 通用基线仍保留在 cumcm/generic_baselines，当前结果为附件驱动的机理仿真版本。

### 变量定义
- P(t): 高压油管压力(MPa)
- rho(P): 燃油密度(mg/mm3)
- E(P): 附件3给出的弹性模量(MPa)
- tau: 问题1单向阀每周期开启时长(ms)
- omega: 问题2/3凸轮角速度(rad/ms)
- h(t): 附件2针阀升程(mm)
- P_relief: 问题3减压阀开启压力阈值(MPa)

### 约束条件
- 单喷嘴喷油周期为100ms，针阀升程超过附件2末端后喷油流量为0。
- 入口A和减压阀D直径均按1.4mm计算，喷嘴有效面积取喷孔面积与针阀圆锥环隙面积的较小值。
- 问题1高压油泵入口压力固定为160MPa，搜索tau时保持每100ms一次供油。
- 问题2凸轮每2π为一个压油周期，柱塞直径5mm，残余体积20mm3。
- 问题3两个喷嘴采用相同喷油规律并错开50ms，以减小压力脉动；减压阀仅在压力超过阈值时开启。

### 模型公式 / 目标函数
- `V_pipe = pi*(10/2)^2*500`
- `d ln rho / dP = 1/E(P)`
- `Q = C*A*sqrt(2*DeltaP/rho_high)`
- `dP/dt = E(P)/(rho(P)*V_pipe) * (rho_in*Q_in - rho(P)*Q_out - rho(P)*Q_relief)`
- `minimize RMS(P(t)-P_target) over the final stable window`

## Python 代码与运行方式

- 代码文件：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2019/A/q01/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2019/A/q01/solution.py`
- 批量运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：读取附件3和附件2，建立密度-压力插值与喷油流量曲线。
- 步骤 2：枚举单向阀开启时长tau，仿真100MPa目标下3秒压力轨迹并选择稳态RMS误差最小者。
- 步骤 3：对150MPa目标先求稳态tau，再分别为2s、5s、10s过渡过程搜索过渡开启时长。
- 步骤 4：输出阀开时长搜索表、100MPa压力轨迹和升压控制计划。

## 实验结果与解释

### 产物文件
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2019/A/q01/valve_duration_search.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2019/A/q01/pressure_trace_100mpa.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2019/A/q01/ramp_control_plan.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2019/A/q01/experiment_table.csv

### 数据来源
- 类型：attachment
- 附件：/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/A-2019中文/附件1-凸轮边缘曲线.xlsx; /Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/A-2019中文/附件2-针阀运动曲线.xlsx; /Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/A-2019中文/附件3-弹性模量与压力.xlsx
- 读取规模：1125 行 x 2 列
- 说明：本题专用算法读取凸轮极径曲线、针阀升程曲线和弹性模量-压力表，建立燃油密度、进出流量和高压油管压力控制仿真。

### result.json 核心结果

```json
{
  "method": "fuel_pipe_valve_duration_pressure_control",
  "elastic_modulus_rows": 401,
  "needle_profile_rows": 90,
  "stable_100mpa_open_ms": 2.012245,
  "stable_100mpa_rms_error_mpa": 0.816395,
  "stable_150mpa_open_ms": 7.152853,
  "ramp_control_plan": [
    {
      "transition_seconds": 2.0,
      "transition_open_ms": 7.152853,
      "stable_150mpa_open_ms": 7.152853,
      "post_ramp_rms_error_mpa": 0.875691,
      "mean_final_pressure_mpa": 150.754314
    },
    {
      "transition_seconds": 5.0,
      "transition_open_ms": 7.152853,
      "stable_150mpa_open_ms": 7.152853,
      "post_ramp_rms_error_mpa": 1.363672,
      "mean_final_pressure_mpa": 151.325742
    },
    {
      "transition_seconds": 10.0,
      "transition_open_ms": 7.152853,
      "stable_150mpa_open_ms": 7.152853,
      "post_ramp_rms_error_mpa": 1.365538,
      "mean_final_pressure_mpa": 151.32767
    }
  ],
  "report": [
    "问题1用附件3建立密度-压力关系，并用附件2针阀升程近似喷油速率，枚举单向阀开启时长。",
    "100MPa稳压方案输出 `valve_duration_search.csv` 和 `pressure_trace_100mpa.csv`，升至150MPa的2/5/10秒控制写入 `ramp_control_plan.csv`。",
    "该模型保留质量守恒、弹性模量和小孔流量三个核心机理；通用基线仍保留作为第一轮粗模型对照。"
  ]
}
```

### 结果解释
- 本问用 `fuel_pipe_valve_duration_pressure_control` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 专用实验报告

- 问题1用附件3建立密度-压力关系，并用附件2针阀升程近似喷油速率，枚举单向阀开启时长。
- 100MPa稳压方案输出 `valve_duration_search.csv` 和 `pressure_trace_100mpa.csv`，升至150MPa的2/5/10秒控制写入 `ramp_control_plan.csv`。
- 该模型保留质量守恒、弹性模量和小孔流量三个核心机理；通用基线仍保留作为第一轮粗模型对照。

## 实验报告

本问的核心是：某型号高压油管的内腔长度为500mm，内直径为10mm，供油入口A处小孔的直径为1.4mm，通过单向阀开关控制供油时间的长短，单向阀每打开一次后就要关闭10ms。喷油器每秒工作10次，每次工作时喷油时间为2.4ms，喷油器工作时从喷油嘴B处向外喷油的速率如图2所示。高压油泵在入口A处提供的压力恒为160 MPa，高压油管内的初始压力为100 MPa。如果要…

建模时先将题目要求拆成 5 个任务，再选择 `高压油管质量守恒与压力控制仿真`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
