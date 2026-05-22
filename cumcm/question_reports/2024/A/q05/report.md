# 2024-A 问题 5 建模求解实验报告

## 题目原文与任务拆解

- 题目：2024年 CUMCM A题：板凳龙”  闹元宵
- 问题：问题 5
- 原问：舞龙队沿问题 4 设定的路径行进，龙头行进速度保持不变， 请确定龙头的最大 行进速度，使得舞龙队各把手的速度均不超过 2 m/s。 调头空间

### 本问需要完成什么
- 任务 1：舞龙队沿问题 4 设定的路径行进，龙头行进速度保持不变， 请确定龙头的最大 行进速度，使得舞龙队各把手的速度均不超过 2 m/s

## 适配模型

- 主模型：几何解析与运动学参数方程（CH1：解析方法与几何模型）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH1/第1章-解析方法与几何模型.md

### 候选模型与适配理由
- 几何解析与运动学参数方程（CH1）：把手、速度、空间；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH1/第1章-解析方法与几何模型.md
- 规划优化与资源配置（CH3）：最大；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md
- 图论网络与路径调度（CH4）：路径；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH4/第4章-复杂网络与图论模型.md

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

- 代码文件：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2024/A/q05/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2024/A/q05/solution.py`
- 批量运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：用曲率放大系数近似调头段各把手速度。
- 步骤 2：约束所有把手速度不超过 2 m/s。
- 步骤 3：扫描并解析计算最大龙头速度。

## 实验结果与解释

### 产物文件
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2024/A/q05/experiment_table.csv

### 数据来源
- 类型：problem_statement
- 说明：本题专用算法直接使用题面给出的螺距、孔距、速度和调头空间参数；附件中的 result*.xlsx 是输出模板，不作为输入数据。

### result.json 核心结果

```json
{
  "method": "curvature_speed_amplification_bound",
  "max_speed_limit_m_s": 2.0,
  "max_gain": 1.1763286650774734,
  "estimated_max_head_speed_m_s": 1.7002051037056718
}
```

### 结果解释
- 本问用 `curvature_speed_amplification_bound` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 实验报告

本问的核心是：舞龙队沿问题 4 设定的路径行进，龙头行进速度保持不变， 请确定龙头的最大 行进速度，使得舞龙队各把手的速度均不超过 2 m/s。 调头空间

建模时先将题目要求拆成 1 个任务，再选择 `几何解析与运动学参数方程`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
