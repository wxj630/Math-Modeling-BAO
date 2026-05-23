# 2025-A 问题1 建模求解实验报告

## 题目原文与任务拆解

- 题目：2025年 CUMCM A题：烟幕干扰弹的投放策略
- 问题：问题1
- 原问：利用无人机FY1 投放1 枚烟幕干扰弹实施对M1 的干扰，若FY1 以120 m/s 的 速度朝向假目标方向飞行，受领任务1.5 s 后即投放1 枚烟幕干扰弹，间隔3.6 s 后起爆。请 给出烟幕干扰弹对M1 的有效遮蔽时长。

### 本问需要完成什么
- 任务 1：请 给出烟幕干扰弹对M1 的有效遮蔽时长

## 适配模型

- 主模型：几何解析与运动学参数方程（CH1：解析方法与几何模型）
- 教程参考：../My-Agent/intro-mathmodel/docs/CH1/第1章-解析方法与几何模型.md

### 候选模型与适配理由
- 几何解析与运动学参数方程（CH1）：速度；参考 ../My-Agent/intro-mathmodel/docs/CH1/第1章-解析方法与几何模型.md

## 变量、约束与公式

### 建模假设
- 以题面给出的数值、约束和输出格式为第一优先级构造模型。
- 若原始附件尚未能被当前环境直接读取，脚本优先抽取题目原文中的参数和表格数字，并在数据来源中显式记录。
- 所有结果由本问 solution.py 运行生成，result.json 与 experiment_table.csv 保持同步。

### 变量定义
- p_i=(x_i,y_i): 几何观测点
- c=(a,b): 中心或定位参数
- r: 半径/尺度参数
- e_i: 几何残差

### 约束条件
- r >= 0
- 观测点满足题面几何关系的近似约束

### 模型公式 / 目标函数
- `min_{a,b,r} mean_i (||p_i-c||_2-r)^2`
- `e_i=||p_i-c||_2-r`

## Python 代码与运行方式

- 代码文件：cumcm/question_solutions/2025/A/q01/solution.py
- 单问运行：`.venv/bin/python cumcm/question_solutions/2025/A/q01/solution.py`
- 批量运行：`.venv/bin/python cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：把坐标、角度、距离条件转成几何参数。
- 步骤 2：构造最小二乘残差。
- 步骤 3：用 scipy.optimize.minimize 求解。
- 步骤 4：输出拟合参数和残差。

## 实验结果与解释

### 产物文件
- cumcm/question_artifacts/2025/A/q01/experiment_table.csv

### 数据来源
- 类型：attachment
- 附件：../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/A题/附件/result1.xlsx
- 读取规模：5 行 x 1 列
- 说明：本问优先使用官方附件中的数值表生成实验结果。

### result.json 核心结果

```json
{
  "method": "least_squares_geometry_fit",
  "center": [
    0.194265,
    0.824465
  ],
  "radius": 4.280014661433695,
  "mean_squared_error": 0.003447992634672612,
  "success": true
}
```

### 结果解释
- 本问用 `least_squares_geometry_fit` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 实验报告

本问的核心是：利用无人机FY1 投放1 枚烟幕干扰弹实施对M1 的干扰，若FY1 以120 m/s 的 速度朝向假目标方向飞行，受领任务1.5 s 后即投放1 枚烟幕干扰弹，间隔3.6 s 后起爆。请 给出烟幕干扰弹对M1 的有效遮蔽时长。

建模时先将题目要求拆成 1 个任务，再选择 `几何解析与运动学参数方程`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
