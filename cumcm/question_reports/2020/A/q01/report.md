# 2020-A 问题1 建模求解实验报告

## 题目原文与任务拆解

- 题目：2020年 CUMCM A题：炉温曲线
- 问题：问题1
- 原问：请对焊接区域的温度变化规律建立数学模型。假设传送带过炉速度为78 cm/min，各温区温度的设定值分别为173ºC（小温区1~5）、198ºC（小温区6）、230ºC（小温区7）和257ºC（小温区8~9），请给出焊接区域中心的温度变化情况，列出小温区3、6、7中点及小温区8结束处焊接区域中心的温度，画出相应的炉温曲线，并将每隔0.5 s焊接区域中心的温度存放在提供的result.csv中。

### 本问需要完成什么
- 任务 1：请对焊接区域的温度变化规律建立数学模型
- 任务 2：假设传送带过炉速度为78 cm/min，各温区温度的设定值分别为173ºC（小温区1~5）、198ºC（小温区6）、230ºC（小温区7）和257ºC（小温区8~9），请给出焊接区域中心的温度变化情况，列出小温区3、6、7中点及小温区8结束处焊接区域中心的温度，画出相应的炉温曲线
- 任务 3：将每隔0.5 s焊接区域中心的温度存放在提供的result.csv中

## 适配模型

- 主模型：回焊炉温度曲线机理模型与制程优化（CH2：微分方程与动力系统）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH2/第2章-微分方程与动力系统.md

### 候选模型与适配理由
- 微分方程与动态仿真（CH2）：温度、变化规律、炉温；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH2/第2章-微分方程与动力系统.md
- 几何解析与运动学参数方程（CH1）：速度；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH1/第1章-解析方法与几何模型.md
- 数据拟合与回归分析（CH6）：曲线；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH6/第六章-数据处理与拟合模型.md

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

- 代码文件：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2020/A/q01/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2020/A/q01/solution.py`
- 批量运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：读取附件.xlsx实测炉温曲线，用实验设定175/195/235/255摄氏度和70 cm/min标定tau。
- 步骤 2：把问题1给定的173/198/230/257摄氏度与78 cm/min代入模型，按0.5秒步长仿真。
- 步骤 3：提取小温区3、6、7中点和小温区8结束处的温度。
- 步骤 4：输出炉温曲线、制程指标和按result.csv模板填充的结果文件。

## 实验结果与解释

### 产物文件
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2020/A/q01/reflow_curve.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2020/A/q01/process_metrics.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2020/A/q01/result_filled.csv

### 数据来源
- 类型：attachment
- 附件：/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/A/result.csv; /Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/A/附件.xlsx
- 读取规模：709 行 x 2 列
- 说明：本题专用算法读取附件.xlsx的实测炉温曲线标定一阶热惯性模型，并按result.csv模板输出0.5秒采样的炉温曲线。

### result.json 核心结果

```json
{
  "method": "reflow_oven_thermal_model",
  "calibration_sample_count": 709,
  "calibrated_tau_s": 109.09428,
  "calibrated_air_gain": 1.29237,
  "calibration_rmse_c": 11.42512,
  "settings_c": {
    "zone1_5": 173.0,
    "zone6": 198.0,
    "zone7": 230.0,
    "zone8_9": 257.0,
    "zone10_11": 25.0
  },
  "speed_cm_min": 78.0,
  "curve_sample_count": 671,
  "peak_temperature_c": 251.032865,
  "process_metrics": {
    "peak_temperature_c": 251.03286484479997,
    "peak_time_s": 262.5,
    "time_150_190_s": 87.0,
    "time_above_217_s": 61.0,
    "max_heating_slope_c_per_s": 1.7492427646652295,
    "max_cooling_slope_c_per_s": 2.044425711005516,
    "area_217_to_peak": 767.9831689480645,
    "symmetry_metric_c": 9.903841493519781,
    "process_feasible": false
  },
  "checkpoint_temperatures_c": {
    "zone3_mid": 112.039403,
    "zone6_mid": 170.907427,
    "zone7_mid": 192.933087,
    "zone8_end": 229.361562
  },
  "report": [
    "本问用附件实测炉温曲线标定一阶热惯性时间常数，再预测给定温区和速度下的炉温曲线。",
    "空气温度场按炉前/炉后25摄氏度、小温区设定温度和相邻温区线性过渡构造。",
    "输出 `reflow_curve.csv`、`process_metrics.csv`，并把0.5秒采样温度写入 `result_filled.csv`。",
    "通用基线保留在 `cumcm/generic_baselines`，当前结果是附件驱动的专用机理模型。"
  ]
}
```

### 结果解释
- 本问用 `reflow_oven_thermal_model` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 专用实验报告

- 本问用附件实测炉温曲线标定一阶热惯性时间常数，再预测给定温区和速度下的炉温曲线。
- 空气温度场按炉前/炉后25摄氏度、小温区设定温度和相邻温区线性过渡构造。
- 输出 `reflow_curve.csv`、`process_metrics.csv`，并把0.5秒采样温度写入 `result_filled.csv`。
- 通用基线保留在 `cumcm/generic_baselines`，当前结果是附件驱动的专用机理模型。

## 实验报告

本问的核心是：请对焊接区域的温度变化规律建立数学模型。假设传送带过炉速度为78 cm/min，各温区温度的设定值分别为173ºC（小温区1~5）、198ºC（小温区6）、230ºC（小温区7）和257ºC（小温区8~9），请给出焊接区域中心的温度变化情况，列出小温区3、6、7中点及小温区8结束处焊接区域中心的温度，画出相应的炉温曲线，并将每隔0.5 s焊接区域中心的温度…

建模时先将题目要求拆成 3 个任务，再选择 `回焊炉温度曲线机理模型与制程优化`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
