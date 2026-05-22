# 2020-D 问题3 建模求解实验报告

## 题目原文与任务拆解

- 题目：2020年 CUMCM D题：接触式轮廓仪的自动标注
- 问题：问题3
- 原问：在对工件作多次检测时，工件每次放置的角度、测量的起点和终点都会有偏差，这导致了每次测量实际是对整个工件中的某一部分进行检测。附件2提供了对工件2的10次测量数据，请基于这些数据完成：(1) 每次测量时工件2的倾斜角度；(2) 标注出工件2轮廓线的各项参数值（同问题1）；(3) 画出工件2的完整轮廓线。

### 本问需要完成什么
- 任务 1：(2) 标注出工件2轮廓线的各项参数值（同问题1）
- 任务 2：(3) 画出工件2的完整轮廓线

## 适配模型

- 主模型：轮廓仪点云分段拟合与自动标注（CH6：数据处理与拟合模型）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH6/第六章-数据处理与拟合模型.md

### 候选模型与适配理由
- 数据拟合与回归分析（CH6）：数据、参数、测量；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH6/第六章-数据处理与拟合模型.md
- 几何解析与运动学参数方程（CH1）：角度、轮廓；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH1/第1章-解析方法与几何模型.md
- 机器学习与统计识别（CH9）：检测；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH9/第九章-机器学习与统计模型.md

## 变量、约束与公式

### 建模假设
- 接触式轮廓仪输出的 x-z 序列按扫描顺序排列，轮廓由直线段与圆弧段近似拼接而成。
- 单次测量的放置误差可用整体线性倾斜项近似，先估计并扣除基线斜率，再做几何标注。
- 粗糙噪声通过滑动均值平滑和分位数稳健统计抑制；通用基线仍保留在 cumcm/generic_baselines 作为进步过程记录。
- 工件2的十次整体测量先分别水平校正并平移对齐，第4问再用局部圆弧和角点数据修正半径、角度等关键参数。

### 变量定义
- p_i=(x_i,z_i): 轮廓仪采样点
- theta_j: 第 j 次测量的倾斜角
- S_k: 自动分段后的第 k 条直线或圆弧
- (a_k,b_k,r_k): 圆弧段的圆心与半径
- L_k, alpha_k: 线段长度和相对水平夹角

### 约束条件
- 每个分段至少包含足够采样点，避免把局部噪声误判为轮廓结构。
- 圆弧半径取正，且只统计与轮廓尺度同量级的有效圆弧。
- 水平校正只移除整体倾斜，不改变局部轮廓的相对几何形状。
- 第4问修正值优先采用局部附件中多次重复测量的中位数，降低单次异常的影响。

### 模型公式 / 目标函数
- `theta = arctan(argmin_m,b sum_{i in edge}(z_i-m x_i-b)^2)`
- `z_i^c = z_i - (m x_i + b)`
- `line: min_{a,b} sum_i (z_i^c-a x_i-b)^2`
- `circle: min_{a,b,r} sum_i (sqrt((x_i-a)^2+(z_i^c-b)^2)-r)^2`
- `参数表 = 槽宽、圆弧半径、圆心距、圆弧长、水平/斜线长、夹角、人字形高度的稳健汇总`

## Python 代码与运行方式

- 代码文件：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2020/D/q03/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2020/D/q03/solution.py`
- 批量运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：读取官方 Excel 附件中的 x-z 点列，并记录真实采样点数。
- 步骤 2：用首尾边缘点拟合整体基线，计算倾斜角并扣除线性倾斜项。
- 步骤 3：对校正后的轮廓做平滑、曲率峰值检测和分段。
- 步骤 4：每段同时拟合直线和圆，根据残差与斜率稳定性标注为 line/arc。
- 步骤 5：汇总几何参数并导出校正点云、分段表、参数表和本问实验报告。

## 实验结果与解释

### 产物文件
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2020/D/q03/measurement_tilts.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2020/D/q03/reconstructed_full_profile.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2020/D/q03/merged_contour_segments.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2020/D/q03/workpiece2_profile_parameters.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2020/D/q03/experiment_table.csv

### 数据来源
- 类型：attachment
- 附件：/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/D/附件2_工件2的整体测量数据.xlsx
- 读取规模：748657 行 x 2 列
- 说明：本题专用算法读取附件1-4的轮廓仪x-z点列，进行倾斜估计、水平校正、平滑分段、直线/圆弧拟合和局部测量修正。

### result.json 核心结果

```json
{
  "method": "profile_multi_measurement_reconstruction",
  "whole_measurement_count": 10,
  "measurement_tilts": [
    {
      "sheet": "25-1",
      "tilt_angle_deg": 16.740227
    },
    {
      "sheet": "25-2",
      "tilt_angle_deg": 10.429128
    },
    {
      "sheet": "26-1",
      "tilt_angle_deg": 11.193826
    },
    {
      "sheet": "26-2",
      "tilt_angle_deg": 18.234969
    },
    {
      "sheet": "27-1",
      "tilt_angle_deg": 12.005435
    },
    {
      "sheet": "27-2",
      "tilt_angle_deg": -5.696878
    },
    {
      "sheet": "28-1",
      "tilt_angle_deg": 19.002375
    },
    {
      "sheet": "28-2",
      "tilt_angle_deg": 18.170854
    },
    {
      "sheet": "29-1",
      "tilt_angle_deg": -3.982921
    },
    {
      "sheet": "29-2",
      "tilt_angle_deg": -3.547164
    }
  ],
  "segment_count": 14,
  "profile_parameters": {
    "x_span": 16.686953,
    "z_span": 14.643482,
    "slot_width": 14.002957,
    "arc_radius_mean": 0.420571,
    "arc_radius_min": 0.338626,
    "arc_radius_max": 3.370798,
    "center_distance_mean": 1.076689,
    "arc_length_total": 33.186135,
    "horizontal_line_length_total": 1.007106,
    "slant_line_length_total": 4.351462,
    "line_length_total": 5.358568,
    "slant_angle_deg": 36.228164,
    "herringbone_height": 5.721125
  },
  "report": [
    "附件2的10次测量先逐次估计倾斜角并校正，再按扫描起点平移对齐。",
    "合并后的点云输出为 `reconstructed_full_profile.csv`，分段拟合结果输出为 `merged_contour_segments.csv`。",
    "各次倾斜角与参数摘要写入 `measurement_tilts.csv`，用于论文说明重复测量误差。"
  ]
}
```

### 结果解释
- 本问用 `profile_multi_measurement_reconstruction` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 专用实验报告

- 附件2的10次测量先逐次估计倾斜角并校正，再按扫描起点平移对齐。
- 合并后的点云输出为 `reconstructed_full_profile.csv`，分段拟合结果输出为 `merged_contour_segments.csv`。
- 各次倾斜角与参数摘要写入 `measurement_tilts.csv`，用于论文说明重复测量误差。

## 实验报告

本问的核心是：在对工件作多次检测时，工件每次放置的角度、测量的起点和终点都会有偏差，这导致了每次测量实际是对整个工件中的某一部分进行检测。附件2提供了对工件2的10次测量数据，请基于这些数据完成：(1) 每次测量时工件2的倾斜角度；(2) 标注出工件2轮廓线的各项参数值（同问题1）；(3) 画出工件2的完整轮廓线。

建模时先将题目要求拆成 2 个任务，再选择 `轮廓仪点云分段拟合与自动标注`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
