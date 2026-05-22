# 2018-D 问题 2 建模求解实验报告

## 题目原文与任务拆解

- 题目：2018年 CUMCM D题：汽车总装线的配置
- 问题：问题 2
- 原问：根据（1）中的数学模型或算法，针对附件中的数据，给出你们的计算结果： （a）将9月20日的装配顺序按照下表格式填写在表中，并将此表放在论文的附录中。 9月20日的装配顺序 （b）按照上表的格式给出9月17日至9月23日每天的装配顺序，文件以“schedule.xlsx”命名，作为论文的支撑材料与论文同时提交。

### 本问需要完成什么
- 任务 1：根据（1）中的数学模型或算法，针对附件中的数据，给出你们的计算结果： （a）将9月20日的装配顺序按照下表格式填写在表中，并将此表放在论文的附录中
- 任务 2：9月20日的装配顺序 （b）按照上表的格式给出9月17日至9月23日每天的装配顺序，文件以“schedule.xlsx”命名，作为论文的支撑材料与论文同时提交

## 适配模型

- 主模型：汽车总装线约束排产与喷涂线分配（CH3：函数极值与规划模型）
- 教程参考：../My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md

### 候选模型与适配理由
- 时间序列预测（CH8）：每天；参考 ../My-Agent/intro-mathmodel/docs/CH8/第8章-时间序列.md
- 数据拟合与回归分析（CH6）：数据；参考 ../My-Agent/intro-mathmodel/docs/CH6/第六章-数据处理与拟合模型.md

## 变量、约束与公式

### 建模假设
- 附件中的每日车型数量是必须全部完成的刚性需求，每天总装460辆，白班和晚班各230辆。
- 每班均先安排A1再安排A2，且每个品牌每日数量均分到两个班次；若某车型数量为奇数，用前半班优先分配余数。
- 四驱、柴油、颜色搭配和黑色批次约束用带罚分的贪心启发式处理；不可完全满足时输出违约计数和代价，保留可复现实验轨迹。
- 喷涂线分配遵守蓝/黄/红只能C1、金只能C2的硬约束，其他颜色按减少颜色切换和线体负载平衡贪心选择。
- 通用基线继续保留在 `cumcm/generic_baselines`，本专用求解器把粗LP/拟合结果推进为附件驱动的一周排程。

### 变量定义
- x_{t,k}: 第 t 个总装位置选择第 k 类车型
- l_t in {C1,C2}: 第 t 辆车分配到的喷涂线
- brand, config, power, drive, color: 车型五属性
- P(schedule): 四驱/柴油间隔、配置切换、颜色切换和搭配违约的综合罚分

### 约束条件
- 每天排产数量等于附件计划，且一周合计3220辆。
- 每班230辆，先A1后A2；A1/A2在每天两个班次中各占当日品牌数量的一半。
- 四驱/柴油连续批次尽量不超过2辆，相邻批次之间尽量间隔至少10辆普通车辆。
- 蓝、黄、红分配到C1，金色分配到C2；其他颜色可分配到任一喷涂线。
- 同品牌相同配置尽量连续，非黑非白颜色在喷涂线上尽量同色连续。

### 模型公式 / 目标函数
- `min P = 1000*hard_spacing_violations + 100*black_run_violations + 50*color_pair_violations + 20*black_color_switches + 5*config_switches + 2*paint_color_switches`
- `sum_k x_{d,k}=460, sum_k x_{d,shift,k}=230`
- `paint_line(color)=C1 for color in {蓝,黄,红}; paint_line(金)=C2`
- `brand_order(d,shift)=A1 block followed by A2 block`

## Python 代码与运行方式

- 代码文件：cumcm/question_solutions/2018/D/q08/solution.py
- 单问运行：`.venv/bin/python cumcm/question_solutions/2018/D/q08/solution.py`
- 批量运行：`.venv/bin/python cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：解析附件中7天A1/A2左右两块生产计划，把颜色、配置、动力、驱动转换为车型需求表。
- 步骤 2：按日期、班次和品牌拆分需求，构造必须排入的车辆多重集合。
- 步骤 3：在每个品牌块内用增量罚分贪心选择下一辆车，优先降低配置切换、四驱/柴油间隔和颜色搭配代价。
- 步骤 4：总装顺序确定后，按颜色硬约束和线体颜色切换成本分配C1/C2喷涂线。
- 步骤 5：输出一周排程、9月20日排程、成本审计、间隔审计、颜色喷涂审计和schedule.xlsx。

## 实验结果与解释

### 产物文件
- cumcm/question_artifacts/2018/D/q08/production_plan_summary.csv
- cumcm/question_artifacts/2018/D/q08/brand_shift_split.csv
- cumcm/question_artifacts/2018/D/q08/spacing_audit.csv
- cumcm/question_artifacts/2018/D/q08/color_paint_audit.csv
- cumcm/question_artifacts/2018/D/q08/cost_audit.csv
- cumcm/question_artifacts/2018/D/q08/weekly_schedule.csv
- cumcm/question_artifacts/2018/D/q08/schedule_2018-09-20.csv
- cumcm/question_artifacts/2018/D/q08/schedule.xlsx
- cumcm/question_artifacts/2018/D/q08/experiment_table.csv

### 数据来源
- 类型：attachment
- 附件：../../Documents/Playground/cumcm_unzipped/2018_lcGi8NeCd14458641de55ec1d705ea01714ff2dd/2018-D-Chinese/CUMCM-2018-Problem-D-Chinese-Appendix.xlsx
- 读取规模：111 行 x 15 列
- 说明：本题专用算法读取附件中的9月17日至9月23日车型计划，按品牌/配置/动力/驱动/颜色生成一周总装顺序、喷涂线分配和schedule.xlsx。

### result.json 核心结果

```json
{
  "method": "assembly_schedule_export",
  "total_vehicle_count": 3220,
  "day_count": 7,
  "model_type_count": 269,
  "september_20_vehicle_count": 460,
  "schedule_workbook_rows": 3220,
  "objective_cost": 54381,
  "spacing_summary": {
    "four_drive_run_violations": 15,
    "four_drive_gap_lt_5": 15,
    "four_drive_gap_5_to_9": 7,
    "diesel_run_violations": 6,
    "diesel_gap_lt_5": 8,
    "diesel_gap_5_to_9": 4
  },
  "switch_summary": {
    "config_switches": 233,
    "paint_color_switches": 233,
    "black_color_switches": 75,
    "color_pair_violations": 44,
    "black_run_violations": 23
  },
  "brand_shift_split_sample": [
    {
      "date": "2018-09-17",
      "shift": "晚班",
      "brand": "A1",
      "vehicle_count": 175
    },
    {
      "date": "2018-09-17",
      "shift": "晚班",
      "brand": "A2",
      "vehicle_count": 41
    },
    {
      "date": "2018-09-17",
      "shift": "白班",
      "brand": "A1",
      "vehicle_count": 189
    },
    {
      "date": "2018-09-17",
      "shift": "白班",
      "brand": "A2",
      "vehicle_count": 55
    },
    {
      "date": "2018-09-18",
      "shift": "晚班",
      "brand": "A1",
      "vehicle_count": 172
    },
    {
      "date": "2018-09-18",
      "shift": "晚班",
      "brand": "A2",
      "vehicle_count": 46
    },
    {
      "date": "2018-09-18",
      "shift": "白班",
      "brand": "A1",
      "vehicle_count": 184
    },
    {
      "date": "2018-09-18",
      "shift": "白班",
      "brand": "A2",
      "vehicle_count": 58
    }
  ],
  "report": [
    "本题把附件生产计划解析为车型多重集合，并在每个班次中强制先A1后A2。",
    "启发式排程以综合罚分为目标，优先降低四驱/柴油间隔违约、配置切换、颜色切换和黑色切换代价。",
    "输出 `weekly_schedule.csv`、`schedule_2018-09-20.csv` 与 `schedule.xlsx`，可直接作为论文附录和支撑材料的基础。",
    "通用基线未删除，当前结果展示从粗通用模型到可复现实排程算法的进步过程。"
  ]
}
```

### 结果解释
- 本问用 `assembly_schedule_export` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 专用实验报告

- 本题把附件生产计划解析为车型多重集合，并在每个班次中强制先A1后A2。
- 启发式排程以综合罚分为目标，优先降低四驱/柴油间隔违约、配置切换、颜色切换和黑色切换代价。
- 输出 `weekly_schedule.csv`、`schedule_2018-09-20.csv` 与 `schedule.xlsx`，可直接作为论文附录和支撑材料的基础。
- 通用基线未删除，当前结果展示从粗通用模型到可复现实排程算法的进步过程。

## 实验报告

本问的核心是：根据（1）中的数学模型或算法，针对附件中的数据，给出你们的计算结果： （a）将9月20日的装配顺序按照下表格式填写在表中，并将此表放在论文的附录中。 9月20日的装配顺序 （b）按照上表的格式给出9月17日至9月23日每天的装配顺序，文件以“schedule.xlsx”命名，作为论文的支撑材料与论文同时提交。

建模时先将题目要求拆成 2 个任务，再选择 `汽车总装线约束排产与喷涂线分配`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
