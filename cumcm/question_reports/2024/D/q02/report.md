# 2024-D 问题 2 建模求解实验报告

## 题目原文与任务拆解

- 题目：2024年 CUMCM D题：反潜航空深弹命中概率
- 问题：问题 2
- 原问：仍投射一枚深弹，潜艇中心位置各方向的定位均有误差。 请给出投弹命中概率 的表达式。 针对以下参数，设计定深引信引爆深度， 使得投弹命中概率最大： 潜艇中心位置的深度 定位值为 150 m，标准差 𝜎𝑧 = 40 m，潜艇中心位置实际深度的最小值为 120 m，其他参 数同问题 1。

### 本问需要完成什么
- 任务 1：请给出投弹命中概率 的表达式
- 任务 2：针对以下参数，设计定深引信引爆深度， 使得投弹命中概率最大： 潜艇中心位置的深度 定位值为 150 m，标准差 𝜎𝑧 = 40 m，潜艇中心位置实际深度的最小值为 120 m，其他参 数同问题 1

## 适配模型

- 主模型：概率统计与抽样检验（CH9：机器学习与统计模型）
- 教程参考：../My-Agent/intro-mathmodel/docs/CH9/第九章-机器学习与统计模型.md

### 候选模型与适配理由
- 概率统计与抽样检验（CH9）：概率、命中、误差；参考 ../My-Agent/intro-mathmodel/docs/CH9/第九章-机器学习与统计模型.md
- 规划优化与资源配置（CH3）：最大、最小、设计；参考 ../My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md
- 几何解析与运动学参数方程（CH1）：位置；参考 ../My-Agent/intro-mathmodel/docs/CH1/第1章-解析方法与几何模型.md

## 变量、约束与公式

### 建模假设
- 以题面给出的数值、约束和输出格式为第一优先级构造模型。
- 若原始附件尚未能被当前环境直接读取，脚本优先抽取题目原文中的参数和表格数字，并在数据来源中显式记录。
- 所有结果由本问 solution.py 运行生成，result.json 与 experiment_table.csv 保持同步。

### 变量定义
- (x_b,y_b): 航空深弹平面投弹落点
- d: 定深引信引爆深度
- (X,Y,Z): 潜艇中心真实位置随机变量
- L,W,H: 潜艇长、宽、高
- R: 深弹杀伤半径
- P_hit: 命中概率

### 约束条件
- X,Y 独立服从 N(0,sigma^2)。
- 问题 1 中 Z=h0；问题 2 和 3 中 Z 服从下截尾正态分布。
- 触发引信命中：落点在潜艇水平投影内，且定深不浅于潜艇上表面。
- 定深引信命中：引爆点到潜艇长方体的最短距离不超过杀伤半径 R。

### 模型公式 / 目标函数
- `P_hit(x_b,y_b,d)=integral 1{trigger_hit or distance_to_box<=R} f_X f_Y f_Z dX dY dZ`
- `distance_to_box 使用长方体外部欧氏距离；长方体内部距离为 0。`
- `max_{x_b,y_b,d} P_hit(x_b,y_b,d)`

## Python 代码与运行方式

- 代码文件：cumcm/question_solutions/2024/D/q02/solution.py
- 单问运行：`.venv/bin/python cumcm/question_solutions/2024/D/q02/solution.py`
- 批量运行：`.venv/bin/python cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：将潜艇主体表示为随航向旋转的长方体。
- 步骤 2：把触发引信和定深引信命中条件写成两个布尔事件的并集。
- 步骤 3：利用正态/截尾正态密度网格做数值积分。
- 步骤 4：对投弹点和定深引信深度搜索最大命中概率。

## 实验结果与解释

### 产物文件
- cumcm/question_artifacts/2024/D/q02/experiment_table.csv

### 数据来源
- 类型：problem_statement
- 附件：cumcm/problems/2024/D.md
- 读取规模：21 行 x 7 列
- 说明：未找到可直接读取的数值附件，本问改用题目原文中的参数/表格数字生成实验结果。

### result.json 核心结果

```json
{
  "method": "truncated_normal_depth_fuze_optimization",
  "parameters": {
    "length": 100.0,
    "width": 20.0,
    "height": 25.0,
    "heading_deg": 90.0,
    "kill_radius": 20.0,
    "sigma_xy": 120.0,
    "depth_mean": 150.0,
    "sigma_z": 40.0,
    "depth_min": 120.0
  },
  "best_plan": {
    "bomb_x_m": 0.0,
    "bomb_y_m": 0.0,
    "detonation_depth_m": 159.0,
    "hit_probability": 0.05773926
  },
  "max_hit_probability": 0.05773926,
  "expression": "P_hit(d)=integral_l^inf integral integral 1{hit(x,y,z;0,0,d)} f_X(x)f_Y(y)f_Z(z) dx dy dz。",
  "truncated_depth_model": {
    "mean_m": 150.0,
    "sigma_m": 40.0,
    "lower_bound_m": 120.0
  }
}
```

### 结果解释
- 本问用 `truncated_normal_depth_fuze_optimization` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 实验报告

本问的核心是：仍投射一枚深弹，潜艇中心位置各方向的定位均有误差。 请给出投弹命中概率 的表达式。 针对以下参数，设计定深引信引爆深度， 使得投弹命中概率最大： 潜艇中心位置的深度 定位值为 150 m，标准差 𝜎𝑧 = 40 m，潜艇中心位置实际深度的最小值为 120 m，其他参 数同问题 1。

建模时先将题目要求拆成 2 个任务，再选择 `概率统计与抽样检验`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
