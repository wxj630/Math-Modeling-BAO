# 2014-D 问题 4 建模求解实验报告

## 题目原文与任务拆解

- 题目：2014年 CUMCM D题：储药柜的设计
- 问题：问题 4
- 原问：附件2给出了每一种药品编号对应的最大日需求量。在储药槽的长度为1.5m、每天仅集中补药一次的情况下，请计算每一种药品需要的储药槽个数。为保证药房储药满足需求，根据问题3中单个储药柜的规格，计算最少需要多少个储药柜。

### 本问需要完成什么
- 任务 1：附件2给出了每一种药品编号对应的最大日需求量
- 任务 2：在储药槽的长度为1.5m、每天仅集中补药一次的情况下，请计算每一种药品需要的储药槽个数
- 任务 3：为保证药房储药满足需求，根据问题3中单个储药柜的规格，计算最少需要多少个储药柜

## 适配模型

- 主模型：储药柜隔板间距聚类与容量规划模型（CH3：函数极值与规划模型）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md

### 候选模型与适配理由
- 时间序列预测（CH8）：每天；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH8/第8章-时间序列.md
- 规划优化与资源配置（CH3）：最大；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md

## 变量、约束与公式

### 建模假设
- 竖向隔板间距至少为药盒宽度加两侧2mm间隙；横向隔板间距至少为药盒高度加上下2mm间隙。
- 同一间距类型可服务不超过该间距的多种药盒，冗余为间距减去药盒尺寸与必要间隙后的剩余量。
- 间距类型数量与冗余之间存在权衡；本模型用一维动态规划在给定类型数下最小化组内冗余，再用肘部准则选择合理类型数。
- 储药槽长度为1500mm，每个槽沿长度方向顺序存放同一种药品，槽容量为floor(1500/药盒长度)。
- 单个储药柜有效宽度2500mm、有效高度1500mm；以选定宽/高间距类型估计单柜槽位能力。

### 变量定义
- w_i,h_i,l_i: 第i种药盒宽、高、长
- a_k: 第k类竖向隔板间距
- b_m: 第m类横向隔板间距
- x_{ik}, y_{im}: 药品到宽度/高度类型的分配
- s_i: 第i种药品所需储药槽个数
- N: 所需储药柜数量

### 约束条件
- a_k >= w_i + 4mm for assigned medicines
- b_m >= h_i + 4mm for assigned medicines
- sum_k x_{ik}=1, sum_m y_{im}=1
- 单柜宽度不超过2500mm，有效高度不超过1500mm，槽长固定1500mm。
- s_i >= ceil(日最大需求量_i / floor(1500/l_i))

### 模型公式 / 目标函数
- `min sum_i (a_{g(i)} - w_i - 4) for fixed width type count`
- `min sum_i (b_{r(i)} - h_i - 4)*(a_{g(i)} - w_i - 4) for fixed height type count`
- `choose K by elbow: marginal_redundancy_reduction < threshold`
- `N = ceil(sum_i s_i / estimated_slots_per_cabinet)`

## Python 代码与运行方式

- 代码文件：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2014/D/q04/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2014/D/q04/solution.py`
- 批量运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：读取附件1药盒长高宽和附件2日最大需求量。
- 步骤 2：对宽度和高度分别做排序动态规划，枚举类型数并计算最小冗余。
- 步骤 3：用冗余下降肘部准则选取合理宽度/高度类型数，并导出药品到类型的分配。
- 步骤 4：根据1500mm槽长计算每个槽可存盒数和各药品所需槽数。
- 步骤 5：按单柜2500mm×1500mm有效尺寸估计单柜槽位能力，计算最少储药柜数量。

## 实验结果与解释

### 产物文件
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2014/D/q04/width_spacing_types.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2014/D/q04/medicine_width_assignment.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2014/D/q04/width_type_tradeoff.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2014/D/q04/height_spacing_types.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2014/D/q04/medicine_height_assignment.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2014/D/q04/plane_redundancy_summary.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2014/D/q04/slot_requirement_by_medicine.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2014/D/q04/cabinet_capacity_summary.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2014/D/q04/experiment_table.csv

### 数据来源
- 类型：attachment
- 附件：/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2014_cumcm2014problems/D/CUMCM-2014D-Chinese.doc; /Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2014_cumcm2014problems/D/附件1-药盒型号.xls; /Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2014_cumcm2014problems/D/附件2-药品需求量.xls; /Users/wuxiaojun/Documents/Playground/cumcm_reextract/2014/2014_cumcm2014problems/D/CUMCM-2014D-Chinese.doc; /Users/wuxiaojun/Documents/Playground/cumcm_reextract/2014/2014_cumcm2014problems/D/附件1-药盒型号.xls; /Users/wuxiaojun/Documents/Playground/cumcm_reextract/2014/2014_cumcm2014problems/D/附件2-药品需求量.xls
- 读取规模：3838 行 x 4 列
- 说明：本题专用算法读取药盒长高宽和日最大需求量，完成隔板间距类型设计、宽高冗余、储药槽数量和最少储药柜数量计算。

### result.json 核心结果

```json
{
  "method": "medicine_cabinet_slot_capacity_planning",
  "medicine_count": 1919,
  "width_type_count": 12,
  "minimum_feasible_width_type_count": 3,
  "height_type_count": 10,
  "minimum_feasible_height_type_count": 3,
  "total_width_redundancy_mm": 3224.0,
  "mean_width_redundancy_mm": 1.680042,
  "total_height_redundancy_mm": 8128.0,
  "mean_height_redundancy_mm": 4.235539,
  "total_plane_redundancy_mm2": 15194.0,
  "slot_length_mm": 1500,
  "total_required_slots": 2457,
  "slots_per_cabinet": 1617,
  "minimum_cabinet_count": 2,
  "cabinet_capacity_summary": {
    "total_required_slots": 2457,
    "average_width_spacing_mm": 32.127391,
    "average_height_spacing_mm": 71.128612,
    "columns_per_cabinet": 77,
    "rows_per_cabinet": 21,
    "slots_per_cabinet": 1617,
    "minimum_cabinet_count": 2
  },
  "report": [
    "本题读取附件1的1919种药盒长高宽和附件2日最大需求量。",
    "宽度/高度间距类型先按单盒可放入、双盒不能并排的区间约束分组；不交换长宽，因此不把水平旋转作为可行摆放。",
    "第4问按1500mm槽长计算每种药品的单槽容量和所需槽数，并基于2500mm×1500mm有效柜体估计最少储药柜数。",
    "通用基线仍保留在 `cumcm/generic_baselines`，当前结果是从通用LP到附件驱动柜体设计的专用版本。"
  ]
}
```

### 结果解释
- 本问用 `medicine_cabinet_slot_capacity_planning` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 专用实验报告

- 本题读取附件1的1919种药盒长高宽和附件2日最大需求量。
- 宽度/高度间距类型先按单盒可放入、双盒不能并排的区间约束分组；不交换长宽，因此不把水平旋转作为可行摆放。
- 第4问按1500mm槽长计算每种药品的单槽容量和所需槽数，并基于2500mm×1500mm有效柜体估计最少储药柜数。
- 通用基线仍保留在 `cumcm/generic_baselines`，当前结果是从通用LP到附件驱动柜体设计的专用版本。

## 实验报告

本问的核心是：附件2给出了每一种药品编号对应的最大日需求量。在储药槽的长度为1.5m、每天仅集中补药一次的情况下，请计算每一种药品需要的储药槽个数。为保证药房储药满足需求，根据问题3中单个储药柜的规格，计算最少需要多少个储药柜。

建模时先将题目要求拆成 3 个任务，再选择 `储药柜隔板间距聚类与容量规划模型`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
