# 2020-D 问题2 建模求解实验报告

## 题目原文与任务拆解

- 题目：2020年 CUMCM D题：接触式轮廓仪的自动标注
- 问题：问题2
- 原问：同一工件在不同次测量时，由于工件放置的角度和位置不同，轮廓线参数的计算值也会存在差异。附件1中的表down给出了工件1在倾斜一个角度和有一些水平位移状态下轮廓线的测量数据。请计算该工件测量时的倾斜角度，并作水平校正。在数据校正后，完成问题1的任务，并比较两种测量状态下工件1各项参数计算值之间的差异。

### 本问需要完成什么
- 任务 1：同一工件在不同次测量时，由于工件放置的角度和位置不同，轮廓线参数的计算值也会存在差异
- 任务 2：附件1中的表down给出了工件1在倾斜一个角度和有一些水平位移状态下轮廓线的测量数据
- 任务 3：请计算该工件测量时的倾斜角度，并作水平校正
- 任务 4：在数据校正后，完成问题1的任务，并比较两种测量状态下工件1各项参数计算值之间的差异

## 适配模型

- 主模型：轮廓仪点云分段拟合与自动标注（CH6：数据处理与拟合模型）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH6/第六章-数据处理与拟合模型.md

### 候选模型与适配理由
- 几何解析与运动学参数方程（CH1）：位置、角度、轮廓；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH1/第1章-解析方法与几何模型.md
- 数据拟合与回归分析（CH6）：数据、参数、测量；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH6/第六章-数据处理与拟合模型.md
- 综合评价与权重决策（CH7）：比较；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH7/第7章-权重生成与评价模型.md

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

- 代码文件：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2020/D/q02/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2020/D/q02/solution.py`
- 批量运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：读取官方 Excel 附件中的 x-z 点列，并记录真实采样点数。
- 步骤 2：用首尾边缘点拟合整体基线，计算倾斜角并扣除线性倾斜项。
- 步骤 3：对校正后的轮廓做平滑、曲率峰值检测和分段。
- 步骤 4：每段同时拟合直线和圆，根据残差与斜率稳定性标注为 line/arc。
- 步骤 5：汇总几何参数并导出校正点云、分段表、参数表和本问实验报告。

## 实验结果与解释

### 产物文件
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2020/D/q02/level_corrected_profile.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2020/D/q02/level_contour_segments.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2020/D/q02/level_profile_parameters.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2020/D/q02/down_corrected_profile.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2020/D/q02/down_contour_segments.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2020/D/q02/down_profile_parameters.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2020/D/q02/level_down_parameter_comparison.csv

### 数据来源
- 类型：attachment
- 附件：/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/D/附件1_工件1的测量数据.xlsx
- 读取规模：284627 行 x 2 列
- 说明：本题专用算法读取附件1-4的轮廓仪x-z点列，进行倾斜估计、水平校正、平滑分段、直线/圆弧拟合和局部测量修正。

### result.json 核心结果

```json
{
  "method": "profile_tilt_correction_and_comparison",
  "level_point_count": 143043,
  "down_point_count": 141584,
  "estimated_down_tilt_angle_deg": -7.448502,
  "level_parameters": {
    "x_span": 71.528094,
    "z_span": 5.30089,
    "slot_width": 47.957444,
    "arc_radius_mean": 3.686838,
    "arc_radius_min": 3.066273,
    "arc_radius_max": 13.247486,
    "center_distance_mean": 12.716152,
    "arc_length_total": 44.940977,
    "horizontal_line_length_total": 14.196941,
    "slant_line_length_total": 20.643204,
    "line_length_total": 34.840145,
    "slant_angle_deg": 12.547916,
    "herringbone_height": 4.171766
  },
  "corrected_down_parameters": {
    "x_span": 70.904678,
    "z_span": 5.346733,
    "slot_width": 47.542093,
    "arc_radius_mean": 3.959521,
    "arc_radius_min": 2.251537,
    "arc_radius_max": 20.612843,
    "center_distance_mean": 10.097633,
    "arc_length_total": 54.995606,
    "horizontal_line_length_total": 14.043205,
    "slant_line_length_total": 9.903794,
    "line_length_total": 23.946999,
    "slant_angle_deg": 12.721305,
    "herringbone_height": 4.213814
  },
  "report": [
    "分别读取 level 与 down，利用首尾边缘点估计 down 的整体倾斜角并做水平校正。",
    "校正后复用第1问的分段拟合流程，并用 `level_down_parameter_comparison.csv` 对比两种放置状态下的参数差异。"
  ]
}
```

### 结果解释
- 本问用 `profile_tilt_correction_and_comparison` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 专用实验报告

- 分别读取 level 与 down，利用首尾边缘点估计 down 的整体倾斜角并做水平校正。
- 校正后复用第1问的分段拟合流程，并用 `level_down_parameter_comparison.csv` 对比两种放置状态下的参数差异。

## 实验报告

本问的核心是：同一工件在不同次测量时，由于工件放置的角度和位置不同，轮廓线参数的计算值也会存在差异。附件1中的表down给出了工件1在倾斜一个角度和有一些水平位移状态下轮廓线的测量数据。请计算该工件测量时的倾斜角度，并作水平校正。在数据校正后，完成问题1的任务，并比较两种测量状态下工件1各项参数计算值之间的差异。

建模时先将题目要求拆成 4 个任务，再选择 `轮廓仪点云分段拟合与自动标注`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
