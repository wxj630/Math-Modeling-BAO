# 2020-A 问题2 建模求解实验报告

## 题目原文与任务拆解

- 题目：2020年 CUMCM A题：炉温曲线
- 问题：问题2
- 原问：假设各温区温度的设定值分别为182ºC（小温区1~5）、203ºC（小温区6）、237ºC（小温区7）、254ºC（小温区8~9），请确定允许的最大传送带过炉速度。

### 本问需要完成什么
- 任务 1：假设各温区温度的设定值分别为182ºC（小温区1~5）、203ºC（小温区6）、237ºC（小温区7）、254ºC（小温区8~9），请确定允许的最大传送带过炉速度

## 适配模型

- 主模型：回焊炉温度曲线机理模型与制程优化（CH2：微分方程与动力系统）
- 教程参考：../My-Agent/intro-mathmodel/docs/CH2/第2章-微分方程与动力系统.md

### 候选模型与适配理由
- 规划优化与资源配置（CH3）：最大；参考 ../My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md
- 微分方程与动态仿真（CH2）：温度；参考 ../My-Agent/intro-mathmodel/docs/CH2/第2章-微分方程与动力系统.md
- 几何解析与运动学参数方程（CH1）：速度；参考 ../My-Agent/intro-mathmodel/docs/CH1/第1章-解析方法与几何模型.md

## 变量、约束与公式

### 建模假设
- 焊接区域中心温度满足一阶热惯性模型，向当前位置炉内空气温度指数逼近。
- 炉内空气温度沿传送带方向由各小温区设定温度、炉前/炉后25摄氏度和相邻温区线性过渡插值得到。
- 附件实测曲线对应题面给定实验设定：速度70 cm/min，温区175/195/235/255/25摄氏度。
- 制程界限采用常见回流焊约束：升温/降温斜率不超过3摄氏度/秒，150-190摄氏度时间60-120秒，超过217摄氏度时间40-90秒，峰值240-250摄氏度。
- 温区1-5同温、8-9同温，10-11保持25摄氏度；优化时各加热温区相对基准设定允许上下10摄氏度调整，传送带速度65-100 cm/min。

### 变量定义
- T(t): 焊接区域中心温度
- A(x): 炉内空气温度场，随传送带位置x变化
- v: 传送带速度，单位cm/min
- tau: 焊接区域等效热时间常数
- theta=(T1_5,T6,T7,T8_9): 四组可调温区设定温度
- S(T): 制程约束指标集合
- J_area: 超过217摄氏度至峰值之间的面积
- J_sym: 峰值两侧超过217摄氏度曲线的不对称指标

### 约束条件
- dT/dt = (A(vt/60)-T)/tau, tau>0。
- 65 <= v <= 100。
- 165<=T1_5<=185, 185<=T6<=205, 225<=T7<=245, 245<=T8_9<=265。
- max dT/dt <= 3 且 max -dT/dt <= 3。
- 60 <= time(150<=T<=190) <= 120。
- 40 <= time(T>217) <= 90。
- 240 <= peak(T) <= 250。

### 模型公式 / 目标函数
- `calibrate tau = argmin_tau mean_k (T_model(t_k;tau)-T_measured(t_k))^2`
- `A(x)=linear_interpolation(zone_centers, zone_setpoints)`
- `J_area = integral_{t_first217}^{t_peak} max(T(t)-217,0) dt`
- `J_sym = mean_s |T(t_peak-s)-T(t_peak+s)| over both sides above 217`
- `Q3: min J_area subject to process constraints`
- `Q4: min J_area + 100*J_sym subject to process constraints`

## Python 代码与运行方式

- 代码文件：cumcm/question_solutions/2020/A/q02/solution.py
- 单问运行：`.venv/bin/python cumcm/question_solutions/2020/A/q02/solution.py`
- 批量运行：`.venv/bin/python cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：固定题给182/203/237/254摄氏度温区组合。
- 步骤 2：在65-100 cm/min范围内枚举速度，计算炉温曲线和制程约束。
- 步骤 3：选择满足所有制程界限的最大速度。
- 步骤 4：输出速度-指标扫描表和最大可行速度。

## 实验结果与解释

### 产物文件
- cumcm/question_artifacts/2020/A/q02/reflow_curve.csv
- cumcm/question_artifacts/2020/A/q02/process_metrics.csv
- cumcm/question_artifacts/2020/A/q02/speed_scan.csv

### 数据来源
- 类型：attachment
- 附件：../../Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/A/result.csv; ../../Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/A/附件.xlsx
- 读取规模：709 行 x 2 列
- 说明：本题专用算法读取附件.xlsx的实测炉温曲线标定一阶热惯性模型，并按result.csv模板输出0.5秒采样的炉温曲线。

### result.json 核心结果

```json
{
  "method": "reflow_max_conveyor_speed_search",
  "calibrated_tau_s": 109.09428,
  "calibrated_air_gain": 1.29237,
  "settings_c": {
    "zone1_5": 182.0,
    "zone6": 203.0,
    "zone7": 237.0,
    "zone8_9": 254.0,
    "zone10_11": 25.0
  },
  "max_feasible_speed_cm_min": 92.5,
  "selected_speed_cm_min": 92.5,
  "feasible_speed_count": 21,
  "selected_metrics": {
    "peak_temperature_c": 240.055744,
    "peak_time_s": 221.5,
    "time_150_190_s": 76.5,
    "time_above_217_s": 41.0,
    "max_heating_slope_c_per_s": 1.855616,
    "max_cooling_slope_c_per_s": 1.94929,
    "area_217_to_peak": 341.530935,
    "symmetry_metric_c": 5.981829,
    "process_feasible": true
  },
  "report": [
    "本问固定题给温区设定，在65-100 cm/min中按0.5 cm/min枚举速度。",
    "每个速度均仿真炉温曲线并检查制程界限，选取满足约束的最大速度。",
    "扫描表 `speed_scan.csv` 给出所有速度的峰值、回流时间、恒温时间和斜率指标。"
  ]
}
```

### 结果解释
- 本问用 `reflow_max_conveyor_speed_search` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 专用实验报告

- 本问固定题给温区设定，在65-100 cm/min中按0.5 cm/min枚举速度。
- 每个速度均仿真炉温曲线并检查制程界限，选取满足约束的最大速度。
- 扫描表 `speed_scan.csv` 给出所有速度的峰值、回流时间、恒温时间和斜率指标。

## 实验报告

本问的核心是：假设各温区温度的设定值分别为182ºC（小温区1~5）、203ºC（小温区6）、237ºC（小温区7）、254ºC（小温区8~9），请确定允许的最大传送带过炉速度。

建模时先将题目要求拆成 1 个任务，再选择 `回焊炉温度曲线机理模型与制程优化`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
