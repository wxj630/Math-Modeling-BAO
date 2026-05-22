# 2016-C 问题1 建模求解实验报告

## 题目原文与任务拆解

- 题目：2016年 CUMCM C题：电池剩余放电时间预测
- 问题：问题1
- 原问：附件1是同一生产批次电池出厂时以不同电流强度放电测试的完整放电曲线的采样数据。请根据附件1用初等函数表示各放电曲线，并分别给出各放电曲线的平均相对误差（MRE，定义见附件1）。如果在新电池使用中，分别以30A、40A、50A、60A和70A电流强度放电，测得电压都为9.8伏时，根据你获得的模型，电池的剩余放电时间分别是多少？

### 本问需要完成什么
- 任务 1：请根据附件1用初等函数表示各放电曲线，并分别给出各放电曲线的平均相对误差（MRE，定义见附件1）

## 适配模型

- 主模型：铅酸电池放电曲线与剩余时间预测模型（CH6：数据处理与拟合模型）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH6/第六章-数据处理与拟合模型.md

### 候选模型与适配理由
- 数据拟合与回归分析（CH6）：数据、曲线；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH6/第六章-数据处理与拟合模型.md
- 概率统计与抽样检验（CH9）：误差；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH9/第九章-机器学习与统计模型.md
- 微分方程与动态仿真（CH2）：放电；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH2/第2章-微分方程与动力系统.md

## 变量、约束与公式

### 建模假设
- 放电电压总体随时间下降，早期平台小幅波动用单调交叉时间而不是简单全局多项式处理。
- 最低保护电压 Um=9V，剩余放电时间定义为到达9V的预计时间减去当前电压对应的已放电时间。
- 附件1各电流曲线互为同批次新电池样本，20A到100A之间的任意电流可按电流方向插值。
- 附件2衰减状态3低电压段缺失，用其已观测段相对衰减状态2的时间比例外推到9V。
- 通用基线保留在 `cumcm/generic_baselines`，当前结果是从粗拟合推进到附件驱动放电曲线预测的专用版本。

### 变量定义
- I: 恒定放电电流(A)
- U_I(t): 电流I下的端电压曲线
- T_I(U): 到达电压U的已放电时间
- R_I(U)=T_I(9V)-T_I(U): 剩余放电时间
- lambda_3(U): 衰减状态3相对状态2的时间比例

### 约束条件
- 仅使用附件1/2真实采样数据构建曲线。
- 到达9V后放电终止；预测剩余时间必须非负。
- 55A曲线由相邻电流曲线在相同电压水平上的到达时间插值得到。

### 模型公式 / 目标函数
- `T_I(U*) = first crossing time of U_I(t)<=U* with linear interpolation。`
- `MRE = mean(|T_pred(U_k)-T_obs(U_k)|/(T_end-T_obs(U_k)+eps)) on held-out voltage samples。`
- `T_55(U)=interp_I(T_I(U), I=55)。`
- `T_state3(9V)=median_tail(T_state3(U)/T_state2(U))*T_state2(9V)。`

## Python 代码与运行方式

- 代码文件：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2016/C/q01/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2016/C/q01/solution.py`
- 批量运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：读取附件1完整放电曲线，按电流分别提取有效时间-电压样本。
- 步骤 2：对每条曲线构造到达电压的交叉时间函数，计算9.8V剩余时间和MRE。
- 步骤 3：在固定电压网格上沿电流方向插值，生成55A放电曲线并做留一电流误差评估。
- 步骤 4：读取附件2衰减状态数据，用状态3已观测段与状态2的低电压比例外推状态3到9V的终止时间。

## 实验结果与解释

### 产物文件
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2016/C/q01/curve_fit_mre_by_current.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2016/C/q01/remaining_time_at_9_8v.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2016/C/q01/experiment_table.csv

### 数据来源
- 类型：attachment
- 附件：/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016C-Chinese/CUMCM2016-C-Appendix-Chinese.xlsx; /Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016C-Chinese/CUMCM2016-Problem-C-Chinese-version.docx
- 读取规模：2188 行 x 17 列
- 说明：本题专用算法读取附件1九条新电池放电曲线和附件2衰减状态电压-时间表，完成剩余时间预测、电流插值曲线和状态3寿命外推。

### result.json 核心结果

```json
{
  "method": "battery_discharge_curve_fit_remaining_time",
  "curve_count": 9,
  "mean_mre_percent": 1.052895,
  "remaining_time_at_9_8v_min": {
    "30A": 593.0,
    "40A": 429.72,
    "50A": 326.5,
    "60A": 277.0,
    "70A": 254.5
  },
  "report": [
    "附件1按20A到100A分别提取完整放电曲线，用首次到达电压的交叉时间表示T_I(U)。",
    "MRE基于留出电压样本的到达时间误差计算，避免只报告原始采样点的零误差。",
    "对30A、40A、50A、60A、70A在9.8V时计算到9V的剩余放电时间。"
  ]
}
```

### 结果解释
- 本问用 `battery_discharge_curve_fit_remaining_time` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 专用实验报告

- 附件1按20A到100A分别提取完整放电曲线，用首次到达电压的交叉时间表示T_I(U)。
- MRE基于留出电压样本的到达时间误差计算，避免只报告原始采样点的零误差。
- 对30A、40A、50A、60A、70A在9.8V时计算到9V的剩余放电时间。

## 实验报告

本问的核心是：附件1是同一生产批次电池出厂时以不同电流强度放电测试的完整放电曲线的采样数据。请根据附件1用初等函数表示各放电曲线，并分别给出各放电曲线的平均相对误差（MRE，定义见附件1）。如果在新电池使用中，分别以30A、40A、50A、60A和70A电流强度放电，测得电压都为9.8伏时，根据你获得的模型，电池的剩余放电时间分别是多少？

建模时先将题目要求拆成 1 个任务，再选择 `铅酸电池放电曲线与剩余时间预测模型`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
