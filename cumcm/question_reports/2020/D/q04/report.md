# 2020-D 问题4 建模求解实验报告

## 题目原文与任务拆解

- 题目：2020年 CUMCM D题：接触式轮廓仪的自动标注
- 问题：问题4
- 原问：为了更准确地标注出工件2的各项参数值，附件3和附件4分别提供了工件2关于圆和角的9次局部测量数据，请利用这些数据修正问题3的结论，并对该工件的完整轮廓线作进一步修正。

### 本问需要完成什么
- 任务 1：为了更准确地标注出工件2的各项参数值，附件3和附件4分别提供了工件2关于圆和角的9次局部测量数据，请利用这些数据修正问题3的结论，并对该工件的完整轮廓线作进一步修正

## 适配模型

- 主模型：轮廓仪点云分段拟合与自动标注（CH6：数据处理与拟合模型）
- 教程参考：../My-Agent/intro-mathmodel/docs/CH6/第六章-数据处理与拟合模型.md

### 候选模型与适配理由
- 数据拟合与回归分析（CH6）：数据、参数、测量；参考 ../My-Agent/intro-mathmodel/docs/CH6/第六章-数据处理与拟合模型.md
- 几何解析与运动学参数方程（CH1）：圆、轮廓；参考 ../My-Agent/intro-mathmodel/docs/CH1/第1章-解析方法与几何模型.md

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

- 代码文件：cumcm/question_solutions/2020/D/q04/solution.py
- 单问运行：`.venv/bin/python cumcm/question_solutions/2020/D/q04/solution.py`
- 批量运行：`.venv/bin/python cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：读取官方 Excel 附件中的 x-z 点列，并记录真实采样点数。
- 步骤 2：用首尾边缘点拟合整体基线，计算倾斜角并扣除线性倾斜项。
- 步骤 3：对校正后的轮廓做平滑、曲率峰值检测和分段。
- 步骤 4：每段同时拟合直线和圆，根据残差与斜率稳定性标注为 line/arc。
- 步骤 5：用附件3圆弧局部测量和附件4角点局部测量修正第3问整体轮廓参数，并导出修正表。

## 实验结果与解释

### 产物文件
- cumcm/question_artifacts/2020/D/q04/measurement_tilts.csv
- cumcm/question_artifacts/2020/D/q04/reconstructed_full_profile.csv
- cumcm/question_artifacts/2020/D/q04/merged_contour_segments.csv
- cumcm/question_artifacts/2020/D/q04/workpiece2_profile_parameters.csv
- cumcm/question_artifacts/2020/D/q04/local_circle_refinement.csv
- cumcm/question_artifacts/2020/D/q04/local_angle_refinement.csv
- cumcm/question_artifacts/2020/D/q04/refined_profile_parameters.csv
- cumcm/question_artifacts/2020/D/q04/experiment_table.csv

### 数据来源
- 类型：attachment
- 附件：../../Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/D/附件2_工件2的整体测量数据.xlsx; ../../Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/D/附件3_工件2的局部测量数据（圆）.xlsx; ../../Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/D/附件4_工件2的局部测量数据（角）.xlsx
- 读取规模：1502138 行 x 2 列
- 说明：本题专用算法读取附件1-4的轮廓仪x-z点列，进行倾斜估计、水平校正、平滑分段、直线/圆弧拟合和局部测量修正。

### result.json 核心结果

```json
{
  "method": "profile_local_refinement",
  "whole_measurement_count": 10,
  "local_circle_measurement_count": 9,
  "local_angle_measurement_count": 9,
  "whole_parameters_before_refinement": {
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
  "refined_parameters": {
    "x_span": 16.686953,
    "z_span": 14.643482,
    "slot_width": 14.002957,
    "arc_radius_mean": 7.491672,
    "arc_radius_min": 6.986378,
    "arc_radius_max": 7.999478,
    "center_distance_mean": 1.076689,
    "arc_length_total": 33.186135,
    "horizontal_line_length_total": 1.007106,
    "slant_line_length_total": 4.351462,
    "line_length_total": 5.358568,
    "slant_angle_deg": 55.958764,
    "herringbone_height": 5.721125
  },
  "circle_radius_median": 7.491672,
  "included_angle_median_deg": 55.958764,
  "report": [
    "先复用第3问得到工件2整体轮廓，再读取附件3的9次局部圆弧测量拟合半径。",
    "附件4的9次局部角点测量通过曲率最大点切分左右直线，计算夹角中位数。",
    "最终 `refined_profile_parameters.csv` 用局部重复测量修正整体轮廓的半径和角度参数。"
  ]
}
```

### 结果解释
- 本问用 `profile_local_refinement` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 专用实验报告

- 先复用第3问得到工件2整体轮廓，再读取附件3的9次局部圆弧测量拟合半径。
- 附件4的9次局部角点测量通过曲率最大点切分左右直线，计算夹角中位数。
- 最终 `refined_profile_parameters.csv` 用局部重复测量修正整体轮廓的半径和角度参数。

## 实验报告

本问的核心是：为了更准确地标注出工件2的各项参数值，附件3和附件4分别提供了工件2关于圆和角的9次局部测量数据，请利用这些数据修正问题3的结论，并对该工件的完整轮廓线作进一步修正。

建模时先将题目要求拆成 1 个任务，再选择 `轮廓仪点云分段拟合与自动标注`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
