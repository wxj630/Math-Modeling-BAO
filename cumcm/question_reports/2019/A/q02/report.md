# 2019-A 问题2 建模求解实验报告

## 题目原文与任务拆解

- 题目：2019年 CUMCM A题：高压油管的压力控制
- 问题：问题2
- 原问：在实际工作过程中，高压油管A处的燃油来自高压油泵的柱塞腔出口，喷油由喷油嘴的针阀控制。高压油泵柱塞的压油过程如图3所示，凸轮驱动柱塞上下运动，凸轮边缘曲线与角度的关系见附件1。柱塞向上运动时压缩柱塞腔内的燃油，当柱塞腔内的压力大于高压油管内的压力时，柱塞腔与高压油管连接的单向阀开启，燃油进入高压油管内。柱塞腔内直径为5mm，柱塞运动到上止点位置时，柱塞腔残余容积为20mm3。柱塞运动到下止点时，低压燃油会充满柱塞腔（包括残余容积），低压燃油的压力为0.5 MPa。喷油器喷嘴结构如图4所示，针阀直径为2.5mm、密封座是半角为9°的圆锥，最下端喷孔的直径为1.4mm。针阀升程为0时，针阀关闭；针阀升程大于0时，针阀开启，燃油向喷孔流动，通过喷孔喷出。在一个喷油周期内针阀升程与时间的关系由附件2给出。在问题1中给出的喷油器工作次数、高压油管尺寸和初始压力下，确定凸轮的角速度，使得高压油管内的压力尽量稳定在100 MPa左右。

### 本问需要完成什么
- 任务 1：在一个喷油周期内针阀升程与时间的关系由附件2给出
- 任务 2：在问题1中给出的喷油器工作次数、高压油管尺寸和初始压力下，确定凸轮的角速度，使得高压油管内的压力尽量稳定在100 MPa左右

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

- 代码文件：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2019/A/q02/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2019/A/q02/solution.py`
- 批量运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：读取附件1凸轮极径曲线并计算极径对角度的导数。
- 步骤 2：将凸轮极径上升阶段折算为柱塞压油流量，和附件2喷油流量一起进入油管压力方程。
- 步骤 3：枚举凸轮角速度omega，选择压力围绕100MPa波动RMS最小的方案。
- 步骤 4：输出角速度搜索表和最优角速度压力轨迹。

## 实验结果与解释

### 产物文件
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2019/A/q02/cam_speed_search.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2019/A/q02/cam_pressure_trace.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2019/A/q02/experiment_table.csv

### 数据来源
- 类型：attachment
- 附件：/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/A-2019中文/附件1-凸轮边缘曲线.xlsx; /Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/A-2019中文/附件2-针阀运动曲线.xlsx; /Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/A-2019中文/附件3-弹性模量与压力.xlsx
- 读取规模：1125 行 x 2 列
- 说明：本题专用算法读取凸轮极径曲线、针阀升程曲线和弹性模量-压力表，建立燃油密度、进出流量和高压油管压力控制仿真。

### result.json 核心结果

```json
{
  "method": "fuel_pipe_cam_plunger_speed_search",
  "cam_profile_rows": 628,
  "needle_profile_rows": 90,
  "best_omega_rad_per_ms": 0.027,
  "best_omega_rad_per_s": 27.0,
  "best_rms_error_mpa": 1.607503,
  "best_mean_pressure_mpa": 98.920198,
  "best_pressure_span_mpa": 5.207542,
  "report": [
    "问题2读取附件1凸轮极径曲线，把极径上升折算为柱塞压油体积流量，并与针阀喷油流量共同驱动油管压力方程。",
    "枚举凸轮角速度后，以稳态压力RMS误差选择最优角速度；搜索明细和最优压力轨迹分别写入CSV。",
    "这是从通用几何拟合推进到附件凸轮-柱塞-油管耦合仿真的专用版本。"
  ]
}
```

### 结果解释
- 本问用 `fuel_pipe_cam_plunger_speed_search` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 专用实验报告

- 问题2读取附件1凸轮极径曲线，把极径上升折算为柱塞压油体积流量，并与针阀喷油流量共同驱动油管压力方程。
- 枚举凸轮角速度后，以稳态压力RMS误差选择最优角速度；搜索明细和最优压力轨迹分别写入CSV。
- 这是从通用几何拟合推进到附件凸轮-柱塞-油管耦合仿真的专用版本。

## 实验报告

本问的核心是：在实际工作过程中，高压油管A处的燃油来自高压油泵的柱塞腔出口，喷油由喷油嘴的针阀控制。高压油泵柱塞的压油过程如图3所示，凸轮驱动柱塞上下运动，凸轮边缘曲线与角度的关系见附件1。柱塞向上运动时压缩柱塞腔内的燃油，当柱塞腔内的压力大于高压油管内的压力时，柱塞腔与高压油管连接的单向阀开启，燃油进入高压油管内。柱塞腔内直径为5mm，柱塞运动到上止点位置时，柱塞腔残…

建模时先将题目要求拆成 2 个任务，再选择 `高压油管质量守恒与压力控制仿真`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
