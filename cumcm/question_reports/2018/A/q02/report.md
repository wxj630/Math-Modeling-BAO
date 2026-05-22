# 2018-A 问题 3 建模求解实验报告

## 题目原文与任务拆解

- 题目：2018年 CUMCM A题：高温作业专用服装设计
- 问题：问题 3
- 原问：当环境温度为80时，确定II层和IV层的最优厚度，确保工作30分钟时，假人皮肤外侧温度不超过47ºC，且超过44ºC的时间不超过5分钟。 附件1. 专用服装材料的参数值 附件2. 假人皮肤外侧的测量温度

### 本问需要完成什么
- 任务 1：当环境温度为80时，确定II层和IV层的最优厚度，确保工作30分钟时，假人皮肤外侧温度不超过47ºC，且超过44ºC的时间不超过5分钟

## 适配模型

- 主模型：多层服装热阻-热容传热与厚度优化模型（CH2：微分方程与动力系统）
- 教程参考：../My-Agent/intro-mathmodel/docs/CH2/第2章-微分方程与动力系统.md

### 候选模型与适配理由
- 数据拟合与回归分析（CH6）：参数、测量；参考 ../My-Agent/intro-mathmodel/docs/CH6/第六章-数据处理与拟合模型.md
- 规划优化与资源配置（CH3）：最优；参考 ../My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md
- 微分方程与动态仿真（CH2）：温度；参考 ../My-Agent/intro-mathmodel/docs/CH2/第2章-微分方程与动力系统.md

## 变量、约束与公式

### 建模假设
- 服装沿厚度方向一维传热，I/II/III/IV层材料均匀，横向热流忽略。
- 人体侧维持37摄氏度，皮肤外侧温度用等效热阻-热容模型描述。
- 附件2的75摄氏度、II层6mm、IV层5mm实验用于标定人体侧等效热阻和时间常数比例。
- 厚度优化目标是在满足最高温度不超过47摄氏度、超过44摄氏度时间不超过5分钟的前提下尽量减小厚度。
- 通用基线仍保留在 `cumcm/generic_baselines`，当前结果是从一阶/二次通用模型推进到附件驱动传热设计模型的专用版本。

### 变量定义
- d_II: II层厚度(mm)
- d_IV: IV层厚度(mm)
- T_s(t): 皮肤外侧温度
- R_skin: 人体侧等效热阻
- eta_tau: 热容时间常数比例

### 约束条件
- max_t T_s(t) <= 47摄氏度。
- measure({t: T_s(t)>44摄氏度}) <= 5分钟。
- 第2问固定 d_IV=5.5mm；第3问 d_IV 在附件给定0.6-6.4mm范围内搜索。

### 模型公式 / 目标函数
- `R_layers=sum_i d_i/k_i，C_layers=sum_i rho_i c_i d_i。`
- `T_s(t)=37+(T_env-37)*R_skin/(R_layers+R_skin)*(1-exp(-t/tau))。`
- `tau=eta_tau*C_layers*(R_layers*R_skin/(R_layers+R_skin))。`
- `min d_II for q1; min d_II+d_IV for q2 subject to safety constraints。`

## Python 代码与运行方式

- 代码文件：cumcm/question_solutions/2018/A/q02/solution.py
- 单问运行：`.venv/bin/python cumcm/question_solutions/2018/A/q02/solution.py`
- 批量运行：`.venv/bin/python cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：读取附件1材料热物性参数和附件2实测皮肤外侧温度。
- 步骤 2：用75摄氏度实验标定R_skin和eta_tau，并输出拟合误差。
- 步骤 3：对候选厚度逐秒模拟温度曲线，计算最高温和超过44摄氏度时间。
- 步骤 4：选择满足约束的最小厚度方案，输出搜索表、最优温度曲线和Excel温度文件。

## 实验结果与解释

### 产物文件
- cumcm/question_artifacts/2018/A/q02/thermal_calibration.csv
- cumcm/question_artifacts/2018/A/q02/joint_thickness_search.csv
- cumcm/question_artifacts/2018/A/q02/optimized_temperature_profile.csv
- cumcm/question_artifacts/2018/A/q02/optimized_temperature_profile.xlsx
- cumcm/question_artifacts/2018/A/q02/experiment_table.csv

### 数据来源
- 类型：attachment
- 附件：../../Documents/Playground/cumcm_unzipped/2018_lcGi8NeCd14458641de55ec1d705ea01714ff2dd/2018-A-Chinese/CUMCM-2018-Problem-A-Chinese-Appendix.xlsx; ../../Documents/Playground/cumcm_unzipped/2018_lcGi8NeCd14458641de55ec1d705ea01714ff2dd/2018-A-Chinese/CUMCM-2018-Problem-A-Chinese.docx
- 读取规模：5405 行 x 7 列
- 说明：本题专用算法读取附件1四层材料热物性参数和附件2皮肤外侧实测温度，标定热阻-热容模型并搜索II/IV层厚度。

### result.json 核心结果

```json
{
  "method": "heat_clothing_layer2_layer4_joint_optimization",
  "environment_temperature_c": 80.0,
  "duration_min": 30.0,
  "optimal_layer_ii_thickness_mm": 26.1,
  "optimal_layer_iv_thickness_mm": 6.4,
  "total_variable_thickness_mm": 32.5,
  "max_skin_temperature_c": 44.622524,
  "minutes_above_44_c": 4.9,
  "final_temperature_c": 44.622524,
  "calibration_mae_c": 0.08223,
  "calibration_rmse_c": 0.188948,
  "calibrated_r_skin_m2k_w": 0.116550437,
  "calibrated_tau_scale": 0.289403597,
  "layer_ii_nominal_upper_mm": 25.0,
  "layer_iv_upper_mm": 6.4,
  "report": [
    "第3问在80摄氏度、30分钟条件下联合搜索II层和IV层厚度。",
    "IV层按附件范围0.6-6.4mm搜索；若标定模型显示II层需要略超附件名义上限，结果中保留名义上限字段以便论文中讨论安全裕量。",
    "输出联合搜索表和最优温度曲线Excel，可直接用于实验报告和复核。"
  ]
}
```

### 结果解释
- 本问用 `heat_clothing_layer2_layer4_joint_optimization` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 专用实验报告

- 第3问在80摄氏度、30分钟条件下联合搜索II层和IV层厚度。
- IV层按附件范围0.6-6.4mm搜索；若标定模型显示II层需要略超附件名义上限，结果中保留名义上限字段以便论文中讨论安全裕量。
- 输出联合搜索表和最优温度曲线Excel，可直接用于实验报告和复核。

## 实验报告

本问的核心是：当环境温度为80时，确定II层和IV层的最优厚度，确保工作30分钟时，假人皮肤外侧温度不超过47ºC，且超过44ºC的时间不超过5分钟。 附件1. 专用服装材料的参数值 附件2. 假人皮肤外侧的测量温度

建模时先将题目要求拆成 1 个任务，再选择 `多层服装热阻-热容传热与厚度优化模型`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
