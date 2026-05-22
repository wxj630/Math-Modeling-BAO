# 2024-E 问题 1 建模求解实验报告

## 题目原文与任务拆解

- 题目：2024年 CUMCM E题：交通流量管控
- 问题：问题 1
- 原问：对经中路-纬中路交叉口，根据车流量的差异，可将一天分成若干个时段，估 计不同时段各个相位（包括四个方向直行、转弯）车流量。

### 本问需要完成什么
- 任务 1：对经中路-纬中路交叉口，根据车流量的差异，可将一天分成若干个时段，估 计不同时段各个相位（包括四个方向直行、转弯）车流量

## 适配模型

- 主模型：图论网络与路径调度（CH4：复杂网络与图论模型）
- 教程参考：../My-Agent/intro-mathmodel/docs/CH4/第4章-复杂网络与图论模型.md

### 候选模型与适配理由
- 时间序列预测（CH8）：时段；参考 ../My-Agent/intro-mathmodel/docs/CH8/第8章-时间序列.md
- 图论网络与路径调度（CH4）：交叉口；参考 ../My-Agent/intro-mathmodel/docs/CH4/第4章-复杂网络与图论模型.md

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
- `hourly_count = groupby(date,hour,intersection,direction).size()`
- `segment(hour)=low/offpeak/peak by central-intersection hourly total quantiles`
- `phase_flow = approach_flow * turn_split, turn_split=(straight 0.65, left 0.18, right 0.17)`

## Python 代码与运行方式

- 代码文件：cumcm/question_solutions/2024/E/q01/solution.py
- 单问运行：`.venv/bin/python cumcm/question_solutions/2024/E/q01/solution.py`
- 批量运行：`.venv/bin/python cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：分块读取 884 万行官方 CSV，构建交叉口-小时-方向流量摘要缓存。
- 步骤 2：筛选经中路-纬中路交叉口，按小时平均流量的分位数划分低谷、平峰和高峰。
- 步骤 3：在缺少转向记录的前提下，用可解释固定转向比例把方向流量拆成直行、左转和右转相位。
- 步骤 4：输出各时段、各方向、各转向的估计车流量表。

## 实验结果与解释

### 产物文件
- cumcm/question_artifacts/2024/E/q01/experiment_table.csv

### 数据来源
- 类型：attachment
- 附件：../../Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/E题/附件1.xlsx; ../../Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/E题/附件2.csv; ../../Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/E题/附件3.pdf
- 读取规模：8844996 行 x 4 列
- 说明：本题专用算法分块读取附件2的884万条车辆记录，结合附件1方向/距离信息构建交通流量、信号配时、巡游车和管控效果摘要。

### result.json 核心结果

```json
{
  "method": "time_segment_phase_flow_estimation",
  "source_rows": 8844996,
  "central_intersection": "经中路-纬中路",
  "observed_days": 36,
  "segment_thresholds_avg_hourly_records": {
    "low_q": 944.6378,
    "high_q": 1828.8972
  },
  "hour_segments": {
    "00": "低谷",
    "01": "低谷",
    "02": "低谷",
    "03": "低谷",
    "04": "低谷",
    "05": "低谷",
    "06": "平峰",
    "07": "平峰",
    "08": "平峰",
    "09": "平峰",
    "10": "平峰",
    "11": "高峰",
    "12": "高峰",
    "13": "高峰",
    "14": "高峰",
    "15": "高峰",
    "16": "高峰",
    "17": "平峰",
    "18": "高峰",
    "19": "高峰",
    "20": "平峰",
    "21": "平峰",
    "22": "低谷",
    "23": "低谷"
  },
  "turn_split_assumption": {
    "straight": 0.65,
    "left": 0.18,
    "right": 0.17
  },
  "sample_phase_rows": [
    {
      "segment": "低谷",
      "hours": "00,01,02,03,04,05,22,23",
      "direction": 1,
      "direction_name": "east-west",
      "movement": "直行",
      "estimated_flow_veh_per_hour": 73.2627,
      "approach_flow_veh_per_hour": 112.7118
    },
    {
      "segment": "低谷",
      "hours": "00,01,02,03,04,05,22,23",
      "direction": 1,
      "direction_name": "east-west",
      "movement": "左转",
      "estimated_flow_veh_per_hour": 20.2881,
      "approach_flow_veh_per_hour": 112.7118
    },
    {
      "segment": "低谷",
      "hours": "00,01,02,03,04,05,22,23",
      "direction": 1,
      "direction_name": "east-west",
      "movement": "右转",
      "estimated_flow_veh_per_hour": 19.161,
      "approach_flow_veh_per_hour": 112.7118
    },
    {
      "segment": "低谷",
      "hours": "00,01,02,03,04,05,22,23",
      "direction": 2,
      "direction_name": "west-east",
      "movement": "直行",
      "estimated_flow_veh_per_hour": 28.0403,
      "approach_flow_veh_per_hour": 43.1389
    },
    {
      "segment": "低谷",
      "hours": "00,01,02,03,04,05,22,23",
      "direction": 2,
      "direction_name": "west-east",
      "movement": "左转",
      "estimated_flow_veh_per_hour": 7.765,
      "approach_flow_veh_per_hour": 43.1389
    },
    {
      "segment": "低谷",
      "hours": "00,01,02,03,04,05,22,23",
      "direction": 2,
      "direction_name": "west-east",
      "movement": "右转",
      "estimated_flow_veh_per_hour": 7.3336,
      "approach_flow_veh_per_hour": 43.1389
    },
    {
      "segment": "低谷",
      "hours": "00,01,02,03,04,05,22,23",
      "direction": 3,
      "direction_name": "south-north",
      "movement": "直行",
      "estimated_flow_veh_per_hour": 42.399,
      "approach_flow_veh_per_hour": 65.2292
    },
    {
      "segment": "低谷",
      "hours": "00,01,02,03,04,05,22,23",
      "direction": 3,
      "direction_name": "south-north",
      "movement": "左转",
      "estimated_flow_veh_per_hour": 11.7413,
      "approach_flow_veh_per_hour": 65.2292
    },
    {
      "segment": "低谷",
      "hours": "00,01,02,03,04,05,22,23",
      "direction": 3,
      "direction_name": "south-north",
      "movement": "右转",
      "estimated_flow_veh_per_hour": 11.089,
      "approach_flow_veh_per_hour": 65.2292
    },
    {
      "segment": "低谷",
      "hours": "00,01,02,03,04,05,22,23",
      "direction": 4,
      "direction_name": "north-south",
      "movement": "直行",
      "estimated_flow_veh_per_hour": 84.0554,
      "approach_flow_veh_per_hour": 129.316
    },
    {
      "segment": "低谷",
      "hours": "00,01,02,03,04,05,22,23",
      "direction": 4,
      "direction_name": "north-south",
      "movement": "左转",
      "estimated_flow_veh_per_hour": 23.2769,
      "approach_flow_veh_per_hour": 129.316
    },
    {
      "segment": "低谷",
      "hours": "00,01,02,03,04,05,22,23",
      "direction": 4,
      "direction_name": "north-south",
      "movement": "右转",
      "estimated_flow_veh_per_hour": 21.9837,
      "approach_flow_veh_per_hour": 129.316
    }
  ]
}
```

### 结果解释
- 本问用 `time_segment_phase_flow_estimation` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 实验报告

本问的核心是：对经中路-纬中路交叉口，根据车流量的差异，可将一天分成若干个时段，估 计不同时段各个相位（包括四个方向直行、转弯）车流量。

建模时先将题目要求拆成 1 个任务，再选择 `图论网络与路径调度`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
