# 2024-E 问题 3 建模求解实验报告

## 题目原文与任务拆解

- 题目：2024年 CUMCM E题：交通流量管控
- 问题：问题 3
- 原问：对五一黄金周期间的数据进行分析，判定寻找停车位的巡游车辆，并估算假 期景区需要临时征用多少停车位才能满足需求？

### 本问需要完成什么
- 任务 1：对五一黄金周期间的数据进行分析，判定寻找停车位的巡游车辆，并估算假 期景区需要临时征用多少停车位才能满足需求？

## 适配模型

- 主模型：图论网络与路径调度（CH4：复杂网络与图论模型）
- 教程参考：../My-Agent/intro-mathmodel/docs/CH4/第4章-复杂网络与图论模型.md

### 候选模型与适配理由
- 数据拟合与回归分析（CH6）：数据、分析；参考 ../My-Agent/intro-mathmodel/docs/CH6/第六章-数据处理与拟合模型.md

## 变量、约束与公式

### 建模假设
- 以题面给出的数值、约束和输出格式为第一优先级构造模型。
- 若原始附件尚未能被当前环境直接读取，脚本优先抽取题目原文中的参数和表格数字，并在数据来源中显式记录。
- 所有结果由本问 solution.py 运行生成，result.json 与 experiment_table.csv 保持同步。

### 变量定义
- n_{t,i,d}: 时段 t、交叉口 i、方向 d 的车辆通过数
- q_{t,i,p}: 时段 t、交叉口 i、相位 p 的估计流率
- g_{i,p}: 交叉口 i 的相位 p 绿灯时间
- v_i: 交叉口 i 所属路段的速度指数
- z_m: 车牌 m 是否判定为五一巡游车辆

### 约束条件
- 附件 2 记录的是停车线后方监控点，不直接给出左转/直行/右转，转向比例需由方向流量做可解释估计。
- 信号周期固定为 120 s，每个主相位最小绿灯 25 s，最大绿灯 90 s。
- 车辆通行能力用饱和流率和绿信比估计，速度指数用 BPR 型流量-速度关系近似。
- 巡游车辆需在五一期间出现次数、活动时长、覆盖交叉口数和景区出入口出现次数同时达到阈值。

### 模型公式 / 目标函数
- `z_m=1 if count_m>=6 and unique_intersections_m>=4 and duration_m>=30min and scenic_count_m>=1`
- `temporary_spaces = ceil(0.75 * peak_active_cruising_vehicles)`
- `active hour is counted when a cruising plate appears in that hour during May 1-5`

## Python 代码与运行方式

- 代码文件：cumcm/question_solutions/2024/E/q03/solution.py
- 单问运行：`.venv/bin/python cumcm/question_solutions/2024/E/q03/solution.py`
- 批量运行：`.venv/bin/python cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：在五一黄金周日期内按车牌聚合出现次数、活动时长、经过交叉口数和景区出入口出现次数。
- 步骤 2：用规则识别寻找停车位的低速绕行/反复出现车辆。
- 步骤 3：按小时统计活跃巡游车辆数，并用峰值折算临时停车泊位需求。
- 步骤 4：输出巡游车判定阈值、每日数量、峰值小时和泊位估计。

## 实验结果与解释

### 产物文件
- cumcm/question_artifacts/2024/E/q03/experiment_table.csv
- cumcm/question_artifacts/2024/E/q03/cruising_vehicle_samples.csv

### 数据来源
- 类型：attachment
- 附件：../../Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/E题/附件1.xlsx; ../../Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/E题/附件2.csv; ../../Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/E题/附件3.pdf
- 读取规模：8844996 行 x 4 列
- 说明：本题专用算法分块读取附件2的884万条车辆记录，结合附件1方向/距离信息构建交通流量、信号配时、巡游车和管控效果摘要。

### result.json 核心结果

```json
{
  "method": "holiday_cruising_vehicle_parking_demand_estimation",
  "holiday_window": "2024-05-01 to 2024-05-05",
  "cruising_vehicle_count": 42436,
  "peak_hour": {
    "date": "2024-05-01",
    "hour": 19,
    "active_cruising_vehicles": 10391
  },
  "temporary_parking_spaces_estimate": 7794,
  "criteria": "count>=6, unique intersections>=4, duration>=30min, scenic_count>=1; or stronger loop rule count>=10",
  "daily_peak_cruising": [
    {
      "date": "2024-05-01",
      "peak_active_cruising_vehicles": 10391
    },
    {
      "date": "2024-05-02",
      "peak_active_cruising_vehicles": 9881
    },
    {
      "date": "2024-05-03",
      "peak_active_cruising_vehicles": 10319
    },
    {
      "date": "2024-05-04",
      "peak_active_cruising_vehicles": 8819
    },
    {
      "date": "2024-05-05",
      "peak_active_cruising_vehicles": 9842
    }
  ],
  "sample_cruising_vehicles": [
    {
      "plate": "无车牌",
      "count": 30916,
      "unique_intersections": 12,
      "duration_min": 7198.98,
      "scenic_count": 1139,
      "first": "2024-05-01 00:00:40",
      "last": "2024-05-05 23:59:39"
    },
    {
      "plate": "unnnowk",
      "count": 3153,
      "unique_intersections": 5,
      "duration_min": 7199.12,
      "scenic_count": 0,
      "first": "2024-05-01 00:00:44",
      "last": "2024-05-05 23:59:51"
    },
    {
      "plate": "AFF35767",
      "count": 481,
      "unique_intersections": 9,
      "duration_min": 6446.6,
      "scenic_count": 64,
      "first": "2024-05-01 06:29:31",
      "last": "2024-05-05 17:56:07"
    },
    {
      "plate": "AF8AA67K",
      "count": 461,
      "unique_intersections": 12,
      "duration_min": 6496.58,
      "scenic_count": 60,
      "first": "2024-05-01 05:41:46",
      "last": "2024-05-05 17:58:21"
    },
    {
      "plate": "AFFB5EF7",
      "count": 459,
      "unique_intersections": 9,
      "duration_min": 6364.98,
      "scenic_count": 61,
      "first": "2024-05-01 06:43:53",
      "last": "2024-05-05 16:48:52"
    },
    {
      "plate": "AFF85677",
      "count": 398,
      "unique_intersections": 9,
      "duration_min": 4996.58,
      "scenic_count": 58,
      "first": "2024-05-02 06:29:25",
      "last": "2024-05-05 17:46:00"
    },
    {
      "plate": "AFFB5EE7",
      "count": 386,
      "unique_intersections": 9,
      "duration_min": 6659.77,
      "scenic_count": 54,
      "first": "2024-05-01 06:58:03",
      "last": "2024-05-05 21:57:49"
    },
    {
      "plate": "AFBM4DFK",
      "count": 385,
      "unique_intersections": 12,
      "duration_min": 6512.33,
      "scenic_count": 28,
      "first": "2024-05-01 07:58:12",
      "last": "2024-05-05 20:30:32"
    },
    {
      "plate": "AFF39767",
      "count": 382,
      "unique_intersections": 11,
      "duration_min": 5776.02,
      "scenic_count": 54,
      "first": "2024-05-01 17:16:46",
      "last": "2024-05-05 17:32:47"
    },
    {
      "plate": "AF3NA8EK",
      "count": 378,
      "unique_intersections": 12,
      "duration_min": 7185.58,
      "scenic_count": 40,
      "first": "2024-05-01 00:04:41",
      "last": "2024-05-05 23:50:16"
    }
  ]
}
```

### 结果解释
- 本问用 `holiday_cruising_vehicle_parking_demand_estimation` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 实验报告

本问的核心是：对五一黄金周期间的数据进行分析，判定寻找停车位的巡游车辆，并估算假 期景区需要临时征用多少停车位才能满足需求？

建模时先将题目要求拆成 1 个任务，再选择 `图论网络与路径调度`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
