# 2015-A 问题 3 建模求解实验报告

## 题目原文与任务拆解

- 题目：2015年 CUMCM A题：太阳影子定位
- 问题：问题 3
- 原问：根据某固定直杆在水平地面上的太阳影子顶点坐标数据，建立数学模型确定直杆所处的地点和日期。将你们的模型分别应用于附件2和附件3的影子顶点坐标数据，给出若干个可能的地点与日期。

### 本问需要完成什么
- 任务 1：根据某固定直杆在水平地面上的太阳影子顶点坐标数据，建立数学模型确定直杆所处的地点和日期
- 任务 2：将你们的模型分别应用于附件2和附件3的影子顶点坐标数据，给出若干个可能的地点与日期

## 适配模型

- 主模型：太阳高度角-方位角影子定位模型（CH6：数据处理与拟合模型）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH6/第六章-数据处理与拟合模型.md

### 候选模型与适配理由
- 几何解析与运动学参数方程（CH1）：直杆影长由太阳高度角决定，影尖方向由太阳方位角决定，是典型几何解析模型。；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH1/第1章-解析方法与几何模型.md
- 数据拟合与回归分析（CH6）：附件影尖坐标需要与理论曲线拟合，并估计坐标轴旋转、比例和残差。；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH6/第六章-数据处理与拟合模型.md
- 时间序列预测（CH8）：未知日期和视频问题都依赖影尖随时间变化的序列特征。；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH8/第8章-时间序列.md

## 变量、约束与公式

### 建模假设
- 直杆垂直于水平地面，影尖坐标以杆底为原点。
- 北京时间按东八区中央经线120E换算为当地真太阳时，并加入近似时差方程修正。
- 太阳赤纬、时差、太阳高度角和方位角采用常用天文近似公式，满足数学建模竞赛精度需求。
- 附件影尖坐标的xy轴方向可能与正东/正北存在旋转差异，因此地点搜索时对模型影子向量拟合最优比例和旋转。
- 附件4视频本体未随当前可读附件落盘；问题4保留视频处理流程，并用附件2/3影尖序列演示同一定位算法的可复现实验。
- 通用基线继续保留在 cumcm/generic_baselines，本专用结果是从通用曲线拟合推进到太阳几何定位模型的版本。

### 变量定义
- phi: 拍摄地纬度
- lambda: 拍摄地经度
- n: 年积日或候选日期
- H(t): 太阳时角
- alpha(t): 太阳高度角
- A(t): 太阳方位角
- L(t): 直杆影长
- s,theta: 影尖坐标与理论东西-南北坐标之间的比例和旋转

### 约束条件
- 太阳高度角 alpha(t)>0 时才产生可用影子。
- 影长 L=h/tan(alpha)，h为杆高；未知杆高时由相似变换比例s吸收。
- 地点搜索限制在常见中国及周边经纬度网格：15N-55N、70E-140E。
- 已知日期问题固定为2015-04-18；未知日期问题枚举2015全年候选日期。
- 视频缺失时不能伪造帧级测量，只能输出可复用流程和基于已有影尖序列的替代实验。

### 模型公式 / 目标函数
- `B = 2*pi*(N-81)/364`
- `EoT = 9.87*sin(2B)-7.53*cos(B)-1.5*sin(B)`
- `solar_time = Beijing_time + EoT/60 + (longitude-120)/15`
- `sin(alpha)=sin(phi)sin(delta)+cos(phi)cos(delta)cos(H)`
- `shadow_vector = -h*(sun_east,sun_north)/sun_up`
- `min RMSE || observed_xy - s R(theta) model_shadow ||`

## Python 代码与运行方式

- 代码文件：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2015/A/q03/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2015/A/q03/solution.py`
- 批量运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：分别读取附件2和附件3影尖坐标。
- 步骤 2：枚举候选日期和经纬度网格，对每组日期-地点拟合比例和旋转。
- 步骤 3：按每个附件的RMSE给出若干可能地点与日期。
- 步骤 4：输出综合候选表和两个附件的最优拟合轨迹。

## 实验结果与解释

### 产物文件
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2015/A/q03/unknown_date_location_candidates.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2015/A/q03/unknown_date_best_fit_traces.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2015/A/q03/experiment_table.csv

### 数据来源
- 类型：attachment
- 附件：/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2015_m00L7uGp5743fadb9289f545d4ed5a1b300622fa/A/附件1-3.xls; /Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2015_m00L7uGp5743fadb9289f545d4ed5a1b300622fa/A/附件4下载说明.doc; /Users/wuxiaojun/Documents/Playground/cumcm_reextract/2015/2015_m00L7uGp5743fadb9289f545d4ed5a1b300622fa/A/附件1-3.xls; /Users/wuxiaojun/Documents/Playground/cumcm_reextract/2015/2015_m00L7uGp5743fadb9289f545d4ed5a1b300622fa/A/附件4下载说明.doc
- 读取规模：63 行 x 3 列
- 说明：本题专用算法读取附件1-3影尖坐标，结合太阳赤纬、时差和高度角/方位角模型完成影长曲线、已知日期定位、未知日期定位；附件4当前只有下载说明，因此问题4输出视频处理流程和替代影尖序列实验。

### result.json 核心结果

```json
{
  "method": "solar_shadow_unknown_date_location_date_search",
  "dataset_count": 2,
  "candidate_count": 24,
  "best_by_dataset": {
    "附件2": {
      "date": "2015-07-21",
      "latitude_deg": 40.0,
      "longitude_deg": 81.0,
      "rmse_m": 0.002097,
      "scale_or_height_m": 1.961732,
      "axis_rotation_deg": 20.124533
    },
    "附件3": {
      "date": "2015-02-03",
      "latitude_deg": 34.0,
      "longitude_deg": 114.0,
      "rmse_m": 0.002001,
      "scale_or_height_m": 2.811798,
      "axis_rotation_deg": -9.737309
    }
  },
  "report": [
    "问题3同时搜索日期和地点：日期按2015全年每7天粗网格枚举，地点按经纬度网格枚举。",
    "对每个候选日期-地点拟合最佳比例和旋转，按RMSE给出附件2和附件3的若干可能地点与日期。",
    "输出的拟合轨迹表可用于论文中展示影尖曲线与理论曲线的重合程度。"
  ]
}
```

### 结果解释
- 本问用 `solar_shadow_unknown_date_location_date_search` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 专用实验报告

- 问题3同时搜索日期和地点：日期按2015全年每7天粗网格枚举，地点按经纬度网格枚举。
- 对每个候选日期-地点拟合最佳比例和旋转，按RMSE给出附件2和附件3的若干可能地点与日期。
- 输出的拟合轨迹表可用于论文中展示影尖曲线与理论曲线的重合程度。

## 实验报告

本问的核心是：根据某固定直杆在水平地面上的太阳影子顶点坐标数据，建立数学模型确定直杆所处的地点和日期。将你们的模型分别应用于附件2和附件3的影子顶点坐标数据，给出若干个可能的地点与日期。

建模时先将题目要求拆成 2 个任务，再选择 `太阳高度角-方位角影子定位模型`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
