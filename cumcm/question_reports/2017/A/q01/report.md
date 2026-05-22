# 2017-A 问题 1 建模求解实验报告

## 题目原文与任务拆解

- 题目：2017年 CUMCM A题：CT系统参数标定及成像
- 问题：问题 1
- 原问：在正方形托盘上放置两个均匀固体介质组成的标定模板，模板的几何信息如图2所示，相应的数据文件见附件1，其中每一点的数值反映了该点的吸收强度，这里称为“吸收率”。对应于该模板的接收信息见附件2。请根据这一模板及其接收信息，确定CT系统旋转中心在正方形托盘中的位置、探测器单元之间的距离以及该CT系统使用的X射线的180个方向。

### 本问需要完成什么
- 任务 1：请根据这一模板及其接收信息，确定CT系统旋转中心在正方形托盘中的位置、探测器单元之间的距离以及该CT系统使用的X射线的180个方向

## 适配模型

- 主模型：CT系统投影标定与滤波反投影重建（CH6：数据处理与拟合模型）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH6/第六章-数据处理与拟合模型.md

### 候选模型与适配理由
- 几何解析与运动学参数方程（CH1）：位置、几何、距离；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH1/第1章-解析方法与几何模型.md
- 数据拟合与回归分析（CH6）：数据、标定；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH6/第六章-数据处理与拟合模型.md

## 变量、约束与公式

### 建模假设
- 附件1的256×256模板吸收率矩阵与附件2的512×180模板投影来自同一平行束CT系统。
- 探测器等距排列，180个方向近似覆盖0到179度；安装误差用角度整体偏移、探测器中心偏移和尺度因子表示。
- 未知介质重建采用可复现实验基线：对512维投影重采样到256维，做ramp滤波后反投影到256×256网格。
- 输出文件保留4位小数；通用基线保留在 `cumcm/generic_baselines`，当前结果作为附件驱动CT建模版本。

### 变量定义
- I(x,y): 托盘网格上的吸收率
- s_k(theta_j): 第j个方向第k个探测器单元的投影值
- c=(c_x,c_y): 旋转中心像素坐标
- d: 探测器单元间距的像素尺度
- theta_j: 第j个X射线方向角

### 约束条件
- 重建网格固定为256×256，与题目要求problem2/problem3文件一致。
- 探测器方向单调覆盖180个方向，探测器间距为正。
- 吸收率非负，重建后用非负截断抑制滤波反投影振铃。
- 10个查询点按附件4给出的托盘坐标映射到256×256像素网格并做双线性插值。

### 模型公式 / 目标函数
- `calibration = argmax_shift corr(Radon(template, theta), measured_template_sinogram)`
- `S_f(omega,theta)=|omega| FFT_s(S(s,theta))`
- `I_hat(x,y)=int_0^pi S_f(x cos theta + y sin theta, theta) dtheta`
- `query_value(p)=bilinear(I_hat, p_x, p_y)`

## Python 代码与运行方式

- 代码文件：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2017/A/q01/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2017/A/q01/solution.py`
- 批量运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：读取附件1-5，识别模板、模板投影、两个未知体投影和10个查询点。
- 步骤 2：从模板矩阵生成180个模拟投影，与附件2逐角度互相关，估计角度偏移、旋转中心和探测器间距。
- 步骤 3：对附件3和附件5做ramp滤波反投影，得到两个256×256吸收率矩阵。
- 步骤 4：把附件4的10个位置映射到重建网格，输出两个未知介质在这些位置处的吸收率。
- 步骤 5：导出标定参数、重建摘要、查询点表、problem2.xls和problem3.xls。

## 实验结果与解释

### 产物文件
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2017/A/q01/ct_calibration_parameters.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2017/A/q01/template_projection_match.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2017/A/q01/reconstruction_summary.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2017/A/q01/query_absorption_values.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2017/A/q01/problem2.xls
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2017/A/q01/problem3.xls
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2017/A/q01/improved_template_design.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2017/A/q01/calibration_stability_audit.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2017/A/q01/experiment_table.csv

### 数据来源
- 类型：attachment
- 附件：/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2017_IqAO5Qqi8f23d8738a07a0604b8629ce9bb061ad/CUMCM2017Problems/A/A题附件.xls
- 读取规模：342026 行 x 180 列
- 说明：本题专用算法读取A题附件中的模板矩阵、模板投影、两个未知介质投影和10个查询点，完成CT标定、滤波反投影重建与problem2/problem3文件导出。

### result.json 核心结果

```json
{
  "method": "ct_template_projection_calibration",
  "template_shape": [
    256,
    256
  ],
  "sinogram_shape": [
    512,
    180
  ],
  "problem2_shape": [
    256,
    256
  ],
  "problem3_shape": [
    256,
    256
  ],
  "rotation_center_pixel": [
    126.8926,
    127.5
  ],
  "template_centroid_pixel": [
    130.4604,
    127.5
  ],
  "detector_spacing_pixel": 0.5,
  "detector_center_index": 231.2051,
  "angle_shift_deg": 161,
  "xray_directions_deg_sample": [
    161.0,
    162.0,
    163.0,
    164.0,
    165.0,
    166.0,
    167.0,
    168.0,
    169.0,
    170.0
  ],
  "best_projection_correlation": 0.793531,
  "problem2_summary": {
    "absorption_mean": 0.23737,
    "absorption_max": 1.16557,
    "support_threshold": 0.19828,
    "support_pixel_count": 19464,
    "bbox_x_min": 0,
    "bbox_y_min": 0,
    "bbox_x_max": 255,
    "bbox_y_max": 255
  },
  "problem3_summary": {
    "absorption_mean": 0.236658,
    "absorption_max": 1.522363,
    "support_threshold": 0.225602,
    "support_pixel_count": 19464,
    "bbox_x_min": 0,
    "bbox_y_min": 0,
    "bbox_x_max": 254,
    "bbox_y_max": 250
  },
  "problem2_query_absorption": [
    0.1184,
    0.9724,
    0.8,
    0.2264,
    0.7964,
    0.1241,
    0.1381,
    0.7488,
    0.1616,
    0.1281
  ],
  "problem3_query_absorption": [
    0.1979,
    0.1907,
    0.2881,
    0.3422,
    0.3299,
    0.417,
    0.4203,
    0.2631,
    0.1115,
    0.1203
  ],
  "stability_scenarios": [
    {
      "scenario": "angle_shift_minus_1",
      "parameter": "angle_shift_deg",
      "value": 160,
      "expected_effect": "边缘轻微模糊，中心和间距基本稳定"
    },
    {
      "scenario": "angle_shift_plus_1",
      "parameter": "angle_shift_deg",
      "value": 162,
      "expected_effect": "方向偏差使细节旋转，查询点吸收率变化"
    },
    {
      "scenario": "detector_noise_1pct",
      "parameter": "sinogram_noise",
      "value": 0.01,
      "expected_effect": "ramp滤波放大高频噪声，需平滑或正则化"
    }
  ],
  "report": [
    "本问读取官方A题附件，使用模板矩阵和模板投影做角度偏移、探测器中心与间距的可复现实验标定。",
    "附件3和附件5通过ramp滤波反投影重建为256×256吸收率矩阵，并输出题目要求的problem2.xls/problem3.xls。",
    "附件4的10个坐标点用双线性插值得到吸收率表，写入 `query_absorption_values.csv`。",
    "第4问给出角度扰动、噪声扰动的稳定性审计和非对称多圆点阵新模板设计。"
  ]
}
```

### 结果解释
- 本问用 `ct_template_projection_calibration` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 专用实验报告

- 本问读取官方A题附件，使用模板矩阵和模板投影做角度偏移、探测器中心与间距的可复现实验标定。
- 附件3和附件5通过ramp滤波反投影重建为256×256吸收率矩阵，并输出题目要求的problem2.xls/problem3.xls。
- 附件4的10个坐标点用双线性插值得到吸收率表，写入 `query_absorption_values.csv`。
- 第4问给出角度扰动、噪声扰动的稳定性审计和非对称多圆点阵新模板设计。

## 实验报告

本问的核心是：在正方形托盘上放置两个均匀固体介质组成的标定模板，模板的几何信息如图2所示，相应的数据文件见附件1，其中每一点的数值反映了该点的吸收强度，这里称为“吸收率”。对应于该模板的接收信息见附件2。请根据这一模板及其接收信息，确定CT系统旋转中心在正方形托盘中的位置、探测器单元之间的距离以及该CT系统使用的X射线的180个方向。

建模时先将题目要求拆成 1 个任务，再选择 `CT系统投影标定与滤波反投影重建`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
