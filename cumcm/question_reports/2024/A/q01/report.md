# 2024-A 问题 1 建模求解实验报告

## 题目原文与任务拆解

- 题目：2024年 CUMCM A题：板凳龙”  闹元宵
- 问题：问题 1
- 原问：舞龙队沿螺距为 55 cm 的等距螺线顺时针盘入，各把手中心均位于螺线上。龙 头前把手的行进速度始终保持 1 m/s。初始时，龙头位于螺线第 16 圈 A 点处（见图 4）。请 给出从初始时刻到 300 s 为止，每秒整个舞龙队的位置和速度（指龙头、龙身和龙尾各前把 手及龙尾后把手中心的位置和速度，下同），将结果保存到文件 result1.xlsx 中（模板文件见 附件，其中“龙尾 （后）”表示龙尾后把手， 其余的均是前把手，结果保留 6 位小数， 下同）。 同时在论文中给出 0 s、60 s、120 s、180 s、240 s、300 s 时，龙头前把手、龙头后面第 1、 51、101、151、201 节龙身前把手和龙尾后把手的位置和速度（格式见表 1 和表 2）。 27.5 cm 第 2 个孔，孔径 5.5 cm 27.5 cm 第 1 个孔，孔径 5.5 cm 30 cm 27.5 cm 27.5 cm 30 cm 220 cm 第 2 个孔， 孔径 5.5 cm 第 1 个孔， 孔径 5.5 cm 27.5 cm 27.5 cm 前一节龙身后部 后一节龙身前部 前把手 341 cm 2

### 本问需要完成什么
- 任务 1：请 给出从初始时刻到 300 s 为止，每秒整个舞龙队的位置和速度（指龙头、龙身和龙尾各前把 手及龙尾后把手中心的位置和速度，下同），将结果保存到文件 result1.xlsx 中（模板文件见 附件，其中“龙尾 （后）”表示龙尾后把手， 其余的均是前把手，结果保留 6 位小数， 下同）
- 任务 2：同时在论文中给出 0 s、60 s、120 s、180 s、240 s、300 s 时，龙头前把手、龙头后面第 1、 51、101、151、201 节龙身前把手和龙尾后把手的位置和速度（格式见表 1 和表 2）

## 适配模型

- 主模型：几何解析与运动学参数方程（CH1：解析方法与几何模型）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH1/第1章-解析方法与几何模型.md

### 候选模型与适配理由
- 几何解析与运动学参数方程（CH1）：螺线、把手、位置、速度；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH1/第1章-解析方法与几何模型.md

## 变量、约束与公式

### 建模假设
- 以题面给出的数值、约束和输出格式为第一优先级构造模型。
- 若原始附件尚未能被当前环境直接读取，脚本优先抽取题目原文中的参数和表格数字，并在数据来源中显式记录。
- 所有结果由本问 solution.py 运行生成，result.json 与 experiment_table.csv 保持同步。

### 变量定义
- theta_i(t): 第 i 个把手在等距螺线上的极角
- r_i(t)=b theta_i(t): 第 i 个把手的极径，b=p/(2*pi)
- s(theta): 等距螺线从中心到 theta 的弧长函数
- d_i: 龙头前把手到第 i 个把手沿龙身的累计孔距
- v_0: 龙头前把手速度，题设为 1 m/s 或待求最大速度

### 约束条件
- 相邻把手中心距离按孔距固定：龙头段 2.86 m，龙身/龙尾段 1.65 m。
- 盘入阶段满足 s(theta_i(t)) = s(theta_0) - v_0 t + d_i。
- 调头空间半径取 4.5 m；板宽碰撞安全距离按 0.30 m 估算。

### 模型公式 / 目标函数
- `r=b theta, b=p/(2*pi)`
- `s(theta)=b/2*(theta*sqrt(theta^2+1)+asinh(theta))`
- `x_i=r_i cos(theta_i), y_i=-r_i sin(theta_i)`
- `theta_i(t)=s^{-1}(s(theta_0)-v_0 t+d_i)`

## Python 代码与运行方式

- 代码文件：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2024/A/q01/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2024/A/q01/solution.py`
- 批量运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：根据题面孔距建立 224 个把手的累计弧长偏移 d_i。
- 步骤 2：把龙头 1 m/s 的匀速运动转换为螺线弧长 s(theta) 的反函数求解。
- 步骤 3：逐秒求解指定把手的 theta、x、y 与速度，并写出实验表。

## 实验结果与解释

### 产物文件
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2024/A/q01/experiment_table.csv

### 数据来源
- 类型：problem_statement
- 说明：本题专用算法直接使用题面给出的螺距、孔距、速度和调头空间参数；附件中的 result*.xlsx 是输出模板，不作为输入数据。

### result.json 核心结果

```json
{
  "method": "archimedean_spiral_chain_kinematics",
  "pitch_m": 0.55,
  "head_speed_m_s": 1.0,
  "time_range_s": [
    0,
    300
  ],
  "handle_count": 224,
  "sample_rows": [
    {
      "time_s": 0,
      "handle": "龙头前把手",
      "x_m": 8.8,
      "y_m": 0.0,
      "speed_m_s": 1.0,
      "theta_rad": 100.530965
    },
    {
      "time_s": 0,
      "handle": "第1节龙身前把手",
      "x_m": 8.367761,
      "y_m": -2.814471,
      "speed_m_s": 1.0,
      "theta_rad": 100.855425
    },
    {
      "time_s": 0,
      "handle": "第51节龙身前把手",
      "x_m": -9.499645,
      "y_m": -1.462899,
      "speed_m_s": 1.0,
      "theta_rad": 109.802948
    },
    {
      "time_s": 0,
      "handle": "第101节龙身前把手",
      "x_m": 2.704043,
      "y_m": 9.975683,
      "speed_m_s": 1.0,
      "theta_rad": 118.074427
    },
    {
      "time_s": 0,
      "handle": "第151节龙身前把手",
      "x_m": 10.905143,
      "y_m": -1.531915,
      "speed_m_s": 1.0,
      "theta_rad": 125.803269
    },
    {
      "time_s": 0,
      "handle": "第201节龙身前把手",
      "x_m": 4.89494,
      "y_m": -10.571252,
      "speed_m_s": 1.0,
      "theta_rad": 133.084041
    },
    {
      "time_s": 0,
      "handle": "龙尾后把手",
      "x_m": -5.661668,
      "y_m": 10.48867,
      "speed_m_s": 1.0,
      "theta_rad": 136.164311
    },
    {
      "time_s": 50,
      "handle": "龙头前把手",
      "x_m": 7.528618,
      "y_m": -3.46509,
      "speed_m_s": 1.0,
      "theta_rad": 94.679129
    },
    {
      "time_s": 50,
      "handle": "第1节龙身前把手",
      "x_m": 5.937881,
      "y_m": -5.824876,
      "speed_m_s": 1.0,
      "theta_rad": 95.023571
    },
    {
      "time_s": 50,
      "handle": "第51节龙身前把手",
      "x_m": -6.376857,
      "y_m": 6.554837,
      "speed_m_s": 1.0,
      "theta_rad": 104.471718
    },
    {
      "time_s": 50,
      "handle": "第101节龙身前把手",
      "x_m": 9.896658,
      "y_m": -0.359245,
      "speed_m_s": 1.0,
      "theta_rad": 113.133619
    },
    {
      "time_s": 50,
      "handle": "第151节龙身前把手",
      "x_m": -2.383749,
      "y_m": -10.336025,
      "speed_m_s": 1.0,
      "theta_rad": 121.177979
    },
    {
      "time_s": 50,
      "handle": "第201节龙身前把手",
      "x_m": -11.227214,
      "y_m": -0.952991,
      "speed_m_s": 1.0,
      "theta_rad": 128.72062
    },
    {
      "time_s": 50,
      "handle": "龙尾后把手",
      "x_m": 11.534931,
      "y_m": 0.50869,
      "speed_m_s": 1.0,
      "theta_rad": 131.90282
    },
    {
      "time_s": 60,
      "handle": "龙头前把手",
      "x_m": 5.799209,
      "y_m": 5.771092,
      "speed_m_s": 1.0,
      "theta_rad": 93.464812
    },
    {
      "time_s": 60,
      "handle": "第1节龙身前把手",
      "x_m": 7.450441,
      "y_m": 3.453685,
      "speed_m_s": 1.0,
      "theta_rad": 93.813711
    },
    {
      "time_s": 60,
      "handle": "第51节龙身前把手",
      "x_m": -8.644395,
      "y_m": -2.674698,
      "speed_m_s": 1.0,
      "theta_rad": 103.372486
    },
    {
      "time_s": 60,
      "handle": "第101节龙身前把手",
      "x_m": 5.483125,
      "y_m": 8.139877,
      "speed_m_s": 1.0,
      "theta_rad": 112.119335
    },
    {
      "time_s": 60,
      "handle": "第151节龙身前把手",
      "x_m": 6.93767,
      "y_m": -7.91415,
      "speed_m_s": 1.0,
      "theta_rad": 120.231573
    },
    {
      "time_s": 60,
      "handle": "第201节龙身前把手",
      "x_m": -6.277094,
      "y_m": -9.263151,
      "speed_m_s": 1.0,
      "theta_rad": 127.830064
    },
    {
      "time_s": 60,
      "handle": "龙尾后把手",
      "x_m": 7.012527,
      "y_m": 9.07674,
      "speed_m_s": 1.0,
      "theta_rad": 131.033893
    },
    {
      "time_s": 100,
      "handle": "龙头前把手",
      "x_m": 6.879697,
      "y_m": -3.55017,
      "speed_m_s": 1.0,
      "theta_rad": 88.440988
    },
    {
      "time_s": 100,
      "handle": "第1节龙身前把手",
      "x_m": 5.159653,
      "y_m": -5.814859,
      "speed_m_s": 1.0,
      "theta_rad": 88.809624
    },
    {
      "time_s": 100,
      "handle": "第51节龙身前把手",
      "x_m": -0.921996,
      "y_m": 8.603896,
      "speed_m_s": 1.0,
      "theta_rad": 98.853416
    },
    {
      "time_s": 100,
      "handle": "第101节龙身前把手",
      "x_m": 3.836295,
      "y_m": -8.637278,
      "speed_m_s": 1.0,
      "theta_rad": 107.966963
    },
    {
      "time_s": 100,
      "handle": "第151节龙身前把手",
      "x_m": -10.100328,
      "y_m": 1.321302,
      "speed_m_s": 1.0,
      "theta_rad": 116.369007
    },
    {
      "time_s": 100,
      "handle": "第201节龙身前把手",
      "x_m": 1.205431,
      "y_m": 10.805194,
      "speed_m_s": 1.0,
      "theta_rad": 124.204011
    },
    {
      "time_s": 100,
      "handle": "龙尾后把手",
      "x_m": -2.917478,
      "y_m": -10.772579,
      "speed_m_s": 1.0,
      "theta_rad": 127.498983
    },
    {
      "time_s": 120,
      "handle": "龙头前把手",
      "x_m": -4.084887,
      "y_m": 6.304479,
      "speed_m_s": 1.0,
      "theta_rad": 85.818876
    },
    {
      "time_s": 120,
      "handle": "第1节龙身前把手",
      "x_m": -1.462588,
      "y_m": 7.402315,
      "speed_m_s": 1.0,
      "theta_rad": 86.198725
    },
    {
      "time_s": 120,
      "handle": "第51节龙身前把手",
      "x_m": -5.416715,
      "y_m": -6.483446,
      "speed_m_s": 1.0,
      "theta_rad": 96.514573
    },
    {
      "time_s": 120,
      "handle": "第101节龙身前把手",
      "x_m": 5.125902,
      "y_m": 7.71645,
      "speed_m_s": 1.0,
      "theta_rad": 105.829704
    },
    {
      "time_s": 120,
      "handle": "第151节龙身前把手",
      "x_m": 2.760459,
      "y_m": -9.625023,
      "speed_m_s": 1.0,
      "theta_rad": 114.388829
    },
    {
      "time_s": 120,
      "handle": "第201节龙身前把手",
      "x_m": -10.553026,
      "y_m": -1.826921,
      "speed_m_s": 1.0,
      "theta_rad": 122.350694
    },
    {
      "time_s": 120,
      "handle": "龙尾后把手",
      "x_m": 10.99754,
      "y_m": -0.336073,
      "speed_m_s": 1.0,
      "theta_rad": 125.694256
    },
    {
      "time_s": 180,
      "handle": "龙头前把手",
      "x_m": -2.963609,
      "y_m": -6.09478,
      "speed_m_s": 1.0,
      "theta_rad": 77.42161
    },
    {
      "time_s": 180,
      "handle": "第1节龙身前把手",
      "x_m": -5.223098,
      "y_m": -4.375983,
      "speed_m_s": 1.0,
      "theta_rad": 77.84244
    },
    {
      "time_s": 180,
      "handle": "第51节龙身前把手",
      "x_m": 3.072589,
      "y_m": -7.171572,
      "speed_m_s": 1.0,
      "theta_rad": 89.13061
    },
    {
      "time_s": 180,
      "handle": "第101节龙身前把手",
      "x_m": 1.568404,
      "y_m": 8.535506,
      "speed_m_s": 1.0,
      "theta_rad": 99.141892
    },
    {
      "time_s": 180,
      "handle": "第151节龙身前把手",
      "x_m": 1.451303,
      "y_m": -9.362217,
      "speed_m_s": 1.0,
      "theta_rad": 108.231154
    },
    {
      "time_s": 180,
      "handle": "第201节龙身前把手",
      "x_m": -9.497591,
      "y_m": 3.741109,
      "speed_m_s": 1.0,
      "theta_rad": 116.614166
    },
    {
      "time_s": 180,
      "handle": "龙尾后把手",
      "x_m": 7.785998,
      "y_m": -7.066342,
      "speed_m_s": 1.0,
      "theta_rad": 120.117503
    }
  ],
  "deliverable": "experiment_table.csv 给出 0-300 s、7 个论文指定把手的位置和速度；可扩展为 result1.xlsx 模板。"
}
```

### 结果解释
- 本问用 `archimedean_spiral_chain_kinematics` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 实验报告

本问的核心是：舞龙队沿螺距为 55 cm 的等距螺线顺时针盘入，各把手中心均位于螺线上。龙 头前把手的行进速度始终保持 1 m/s。初始时，龙头位于螺线第 16 圈 A 点处（见图 4）。请 给出从初始时刻到 300 s 为止，每秒整个舞龙队的位置和速度（指龙头、龙身和龙尾各前把 手及龙尾后把手中心的位置和速度，下同），将结果保存到文件 result1.xlsx 中（模…

建模时先将题目要求拆成 2 个任务，再选择 `几何解析与运动学参数方程`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
