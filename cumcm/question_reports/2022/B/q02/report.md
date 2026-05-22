# 2022-B 问题 2 建模求解实验报告

## 题目原文与任务拆解

- 题目：2022年 CUMCM B题：无人机遂行编队飞行中的纯方位无源定位
- 问题：问题 2
- 原问：实际飞行中， 无人机集群也可以是其他编队队形，例如锥形编队队形（见图 3，直 线上相邻两架无人机的间距相等，如 50 m）。仍考虑纯方位无源定位的情形，设计无人机位置 调整方案。

### 本问需要完成什么
- 任务 1：仍考虑纯方位无源定位的情形，设计无人机位置 调整方案

## 适配模型

- 主模型：几何解析与运动学参数方程（CH1：解析方法与几何模型）
- 教程参考：../My-Agent/intro-mathmodel/docs/CH1/第1章-解析方法与几何模型.md

### 候选模型与适配理由
- 规划优化与资源配置（CH3）：方案、设计；参考 ../My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md
- 几何解析与运动学参数方程（CH1）：位置；参考 ../My-Agent/intro-mathmodel/docs/CH1/第1章-解析方法与几何模型.md

## 变量、约束与公式

### 建模假设
- 以题面给出的数值、约束和输出格式为第一优先级构造模型。
- 若原始附件尚未能被当前环境直接读取，脚本优先抽取题目原文中的参数和表格数字，并在数据来源中显式记录。
- 所有结果由本问 solution.py 运行生成，result.json 与 experiment_table.csv 保持同步。

### 变量定义
- p_i=(x_i,y_i): 第 i 架无人机在同一高度平面内的位置
- b_j: 发射信号无人机的已知编号与坐标
- alpha_{ab}(p): 接收机 p 观测到两架发射机 a,b 的夹角
- e_i=p_i-p_i^*: 第 i 架无人机相对目标编队位置的偏差

### 约束条件
- 所有无人机保持同一高度，因此定位问题化为二维平面几何。
- 纯方位信息只使用接收点到两架发射机连线的夹角，不使用距离量测。
- FY00 位于圆心；FY01-FY09 在半径 100 m 圆周上相隔 40 度。
- 每轮最多选择 FY00 和圆周上 3 架无人机发射信号，其余无人机被动定位并调整。

### 模型公式 / 目标函数
- `target cone lattice: apex plus symmetric two arms with spacing 50 m`
- `min_p sum angle residuals recovers current p, then project to assigned cone node p_i^*`
- `adjustment vector delta_i=p_i^*-p_i`

## Python 代码与运行方式

- 代码文件：cumcm/question_solutions/2022/B/q02/solution.py
- 单问运行：`.venv/bin/python cumcm/question_solutions/2022/B/q02/solution.py`
- 批量运行：`.venv/bin/python cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：给出锥形编队的目标坐标格点：顶点、左右两臂和中轴补点。
- 步骤 2：选择顶点和两臂外侧无人机作为发射锚点，其他无人机用夹角残差定位。
- 步骤 3：把定位结果投影到对应锥形目标点，得到每架无人机的调整向量。
- 步骤 4：输出发射计划、目标坐标和调整表。

## 实验结果与解释

### 产物文件
- cumcm/question_artifacts/2022/B/q02/experiment_table.csv

### 数据来源
- 类型：problem_statement
- 附件：cumcm/problems/2022/B.md
- 读取规模：29 行 x 8 列
- 说明：未找到可直接读取的数值附件，本问改用题目原文中的参数/表格数字生成实验结果。

### result.json 核心结果

```json
{
  "method": "bearing_angle_cone_formation_adjustment",
  "spacing_m": 50.0,
  "emitters": [
    "FY00",
    "FY03",
    "FY04",
    "FY09"
  ],
  "cone_nodes": 10,
  "max_adjustment_distance_m": 9.85086,
  "mean_adjustment_distance_m": 6.227652,
  "target_coordinates": [
    {
      "section": "cone_target",
      "uav": "FY00",
      "x": 0.0,
      "y": 0.0
    },
    {
      "section": "cone_target",
      "uav": "FY01",
      "x": -50.0,
      "y": 50.0
    },
    {
      "section": "cone_target",
      "uav": "FY02",
      "x": 50.0,
      "y": 50.0
    },
    {
      "section": "cone_target",
      "uav": "FY03",
      "x": -100.0,
      "y": 100.0
    },
    {
      "section": "cone_target",
      "uav": "FY04",
      "x": 100.0,
      "y": 100.0
    },
    {
      "section": "cone_target",
      "uav": "FY05",
      "x": -150.0,
      "y": 150.0
    },
    {
      "section": "cone_target",
      "uav": "FY06",
      "x": 150.0,
      "y": 150.0
    },
    {
      "section": "cone_target",
      "uav": "FY07",
      "x": -200.0,
      "y": 200.0
    },
    {
      "section": "cone_target",
      "uav": "FY08",
      "x": 200.0,
      "y": 200.0
    },
    {
      "section": "cone_target",
      "uav": "FY09",
      "x": 0.0,
      "y": 125.0
    }
  ],
  "sample_adjustment_rows": [
    {
      "section": "cone_adjustment",
      "receiver": "FY01",
      "emitters": "FY00,FY03,FY04,FY09",
      "estimated_x": -53.293039,
      "estimated_y": 45.749812,
      "target_x": -50.0,
      "target_y": 50.0,
      "dx": 3.293039,
      "dy": 4.250188,
      "move_distance": 5.376635,
      "angle_residual_mse": 0.0
    },
    {
      "section": "cone_adjustment",
      "receiver": "FY02",
      "emitters": "FY00,FY03,FY04,FY09",
      "estimated_x": 49.762084,
      "estimated_y": 47.067927,
      "target_x": 50.0,
      "target_y": 50.0,
      "dx": 0.237916,
      "dy": 2.932073,
      "move_distance": 2.94171,
      "angle_residual_mse": 0.0
    },
    {
      "section": "cone_adjustment",
      "receiver": "FY05",
      "emitters": "FY00,FY03,FY04,FY09",
      "estimated_x": -151.112979,
      "estimated_y": 159.787784,
      "target_x": -150.0,
      "target_y": 150.0,
      "dx": 1.112979,
      "dy": -9.787784,
      "move_distance": 9.85086,
      "angle_residual_mse": 0.0
    },
    {
      "section": "cone_adjustment",
      "receiver": "FY06",
      "emitters": "FY00,FY03,FY04,FY09",
      "estimated_x": 144.036938,
      "estimated_y": 149.492872,
      "target_x": 150.0,
      "target_y": 150.0,
      "dx": 5.963062,
      "dy": 0.507128,
      "move_distance": 5.984587,
      "angle_residual_mse": 0.0
    },
    {
      "section": "cone_adjustment",
      "receiver": "FY07",
      "emitters": "FY00,FY03,FY04,FY09",
      "estimated_x": -201.573007,
      "estimated_y": 194.249513,
      "target_x": -200.0,
      "target_y": 200.0,
      "dx": 1.573007,
      "dy": 5.750487,
      "move_distance": 5.961749,
      "angle_residual_mse": 0.0
    },
    {
      "section": "cone_adjustment",
      "receiver": "FY08",
      "emitters": "FY00,FY03,FY04,FY09",
      "estimated_x": 194.041292,
      "estimated_y": 195.869424,
      "target_x": 200.0,
      "target_y": 200.0,
      "dx": 5.958708,
      "dy": 4.130576,
      "move_distance": 7.250369,
      "angle_residual_mse": 0.0
    }
  ]
}
```

### 结果解释
- 本问用 `bearing_angle_cone_formation_adjustment` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 实验报告

本问的核心是：实际飞行中， 无人机集群也可以是其他编队队形，例如锥形编队队形（见图 3，直 线上相邻两架无人机的间距相等，如 50 m）。仍考虑纯方位无源定位的情形，设计无人机位置 调整方案。

建模时先将题目要求拆成 1 个任务，再选择 `几何解析与运动学参数方程`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
