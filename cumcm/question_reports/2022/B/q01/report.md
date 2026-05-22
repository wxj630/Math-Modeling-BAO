# 2022-B 问题 1 建模求解实验报告

## 题目原文与任务拆解

- 题目：2022年 CUMCM B题：无人机遂行编队飞行中的纯方位无源定位
- 问题：问题 1
- 原问：编队由 10 架无人机组成，形成圆形编队，其中 9 架无人机（编号 FY01~FY09）均 匀分布在某一圆周上，另 1 架无人机（编号 FY00）位于圆心（见图 2）。无人机基于自身感知 的高度信息，均保持在同一个高度上飞行。

### 本问需要完成什么
- 任务 1：编队由 10 架无人机组成，形成圆形编队，其中 9 架无人机（编号 FY01~FY09）均 匀分布在某一圆周上，另 1 架无人机（编号 FY00）位于圆心（见图 2）
- 任务 2：无人机基于自身感知 的高度信息，均保持在同一个高度上飞行

## 适配模型

- 主模型：几何解析与运动学参数方程（CH1：解析方法与几何模型）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH1/第1章-解析方法与几何模型.md

### 候选模型与适配理由
- 几何解析与运动学参数方程（CH1）：圆；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH1/第1章-解析方法与几何模型.md

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
- `alpha_{ab}(p)=acos(((b_a-p)·(b_b-p))/(||b_a-p||||b_b-p||))`
- `min_p sum_{a<b} wrap(alpha_{ab}(p)-alpha_hat_{ab})^2`
- `p_i^{new}=p_i + lambda*(p_i^*-p_i), 本实验取 lambda=1 给出离散调整表`

## Python 代码与运行方式

- 代码文件：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2022/B/q01/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2022/B/q01/solution.py`
- 批量运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：建立由夹角观测反解接收机平面坐标的非线性最小二乘模型。
- 步骤 2：用 FY00 和两个已知圆周发射机模拟定位，验证可恢复偏差位置。
- 步骤 3：枚举 FY00、FY01 和若干未知编号圆周发射机的候选集合，判断有效定位所需数量。
- 步骤 4：按 3 轮发射计划生成 FY01-FY09 从表 1 初始位置到理想圆周位置的调整表。

## 实验结果与解释

### 产物文件
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2022/B/q01/experiment_table.csv

### 数据来源
- 类型：problem_statement
- 附件：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2022/B.md
- 读取规模：29 行 x 8 列
- 说明：未找到可直接读取的数值附件，本问改用题目原文中的参数/表格数字生成实验结果。

### result.json 核心结果

```json
{
  "method": "bearing_angle_circle_formation_localization",
  "known_beacon_localization": {
    "receiver": "FY04",
    "beacons": [
      "FY00",
      "FY01",
      "FY03"
    ],
    "localization_error_m": 0.0,
    "angle_residual_mse": 0.0
  },
  "unknown_transmitter_conclusion": "按未标号夹角集合枚举，除 FY00、FY01 外 1 架未知圆周发射机仍可能产生多个零残差候选；增加到 2 架可显著增强唯一性与抗噪冗余。",
  "ambiguity_analysis": [
    {
      "section": "unknown_transmitter_count",
      "extra_unknown_transmitters": 1,
      "candidate_sets_checked": 8,
      "zero_residual_candidate_sets": 8,
      "example_valid_set": "[[2], [3], [4], [5], [6]]",
      "conclusion": "ambiguous",
      "matching_note": "one-extra case enumerates unlabeled angle permutations; two-extra case uses sorted angle fingerprint as a fast redundancy check"
    },
    {
      "section": "unknown_transmitter_count",
      "extra_unknown_transmitters": 2,
      "candidate_sets_checked": 28,
      "zero_residual_candidate_sets": 0,
      "example_valid_set": "[]",
      "conclusion": "overdetermined_no_exact_alias",
      "matching_note": "one-extra case enumerates unlabeled angle permutations; two-extra case uses sorted angle fingerprint as a fast redundancy check"
    }
  ],
  "adjustment_rounds": [
    {
      "round": 1,
      "emitters": [
        "FY00",
        "FY01",
        "FY04",
        "FY07"
      ]
    },
    {
      "round": 2,
      "emitters": [
        "FY00",
        "FY02",
        "FY05",
        "FY08"
      ]
    },
    {
      "round": 3,
      "emitters": [
        "FY00",
        "FY03",
        "FY06",
        "FY09"
      ]
    }
  ],
  "max_final_position_error_m": 0.0,
  "sample_adjustment_rows": [
    {
      "section": "circle_adjustment",
      "round": 1,
      "emitters": "FY00,FY01,FY04,FY07",
      "receiver": "FY02",
      "estimated_x": 74.962297,
      "estimated_y": 63.124116,
      "angle_residual_mse": 0.0,
      "target_x": 76.604444,
      "target_y": 64.278761,
      "move_distance": 2.007449
    },
    {
      "section": "circle_adjustment",
      "round": 1,
      "emitters": "FY00,FY01,FY04,FY07",
      "receiver": "FY03",
      "estimated_x": 19.044201,
      "estimated_y": 110.36901,
      "angle_residual_mse": 0.0,
      "target_x": 17.364818,
      "target_y": 98.480775,
      "move_distance": 12.006267
    },
    {
      "section": "circle_adjustment",
      "round": 1,
      "emitters": "FY00,FY01,FY04,FY07",
      "receiver": "FY05",
      "estimated_x": -92.007702,
      "estimated_y": 33.742892,
      "angle_residual_mse": 0.0,
      "target_x": -93.969262,
      "target_y": 34.202014,
      "move_distance": 2.014575
    },
    {
      "section": "circle_adjustment",
      "round": 1,
      "emitters": "FY00,FY01,FY04,FY07",
      "receiver": "FY06",
      "estimated_x": -105.272291,
      "estimated_y": -38.232771,
      "angle_residual_mse": 0.0,
      "target_x": -93.969262,
      "target_y": -34.202014,
      "move_distance": 12.000227
    },
    {
      "section": "circle_adjustment",
      "round": 1,
      "emitters": "FY00,FY01,FY04,FY07",
      "receiver": "FY08",
      "estimated_x": 17.3038,
      "estimated_y": -96.460243,
      "angle_residual_mse": 0.0,
      "target_x": 17.364818,
      "target_y": -98.480775,
      "move_distance": 2.021453
    },
    {
      "section": "circle_adjustment",
      "round": 1,
      "emitters": "FY00,FY01,FY04,FY07",
      "receiver": "FY09",
      "estimated_x": 86.147772,
      "estimated_y": -71.572071,
      "angle_residual_mse": 0.0,
      "target_x": 76.604444,
      "target_y": -64.278761,
      "move_distance": 12.01114
    },
    {
      "section": "circle_adjustment",
      "round": 2,
      "emitters": "FY00,FY02,FY05,FY08",
      "receiver": "FY01",
      "estimated_x": 100.0,
      "estimated_y": 0.0,
      "angle_residual_mse": 0.0,
      "target_x": 100.0,
      "target_y": 0.0,
      "move_distance": 0.0
    },
    {
      "section": "circle_adjustment",
      "round": 2,
      "emitters": "FY00,FY02,FY05,FY08",
      "receiver": "FY03",
      "estimated_x": 17.364818,
      "estimated_y": 98.480775,
      "angle_residual_mse": 0.0,
      "target_x": 17.364818,
      "target_y": 98.480775,
      "move_distance": 0.0
    },
    {
      "section": "circle_adjustment",
      "round": 2,
      "emitters": "FY00,FY02,FY05,FY08",
      "receiver": "FY04",
      "estimated_x": -52.102733,
      "estimated_y": 91.160876,
      "angle_residual_mse": 0.0,
      "target_x": -50.0,
      "target_y": 86.60254,
      "move_distance": 5.019951
    },
    {
      "section": "circle_adjustment",
      "round": 2,
      "emitters": "FY00,FY02,FY05,FY08",
      "receiver": "FY06",
      "estimated_x": -93.969262,
      "estimated_y": -34.202014,
      "angle_residual_mse": 0.0,
      "target_x": -93.969262,
      "target_y": -34.202014,
      "move_distance": 0.0
    }
  ]
}
```

### 结果解释
- 本问用 `bearing_angle_circle_formation_localization` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 实验报告

本问的核心是：编队由 10 架无人机组成，形成圆形编队，其中 9 架无人机（编号 FY01~FY09）均 匀分布在某一圆周上，另 1 架无人机（编号 FY00）位于圆心（见图 2）。无人机基于自身感知 的高度信息，均保持在同一个高度上飞行。

建模时先将题目要求拆成 2 个任务，再选择 `几何解析与运动学参数方程`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
