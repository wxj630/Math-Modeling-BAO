# 2024-E 问题 2 建模求解实验报告

## 题目原文与任务拆解

- 题目：2024年 CUMCM E题：交通流量管控
- 问题：问题 2
- 原问：根据所给数据和上述模型，对经中路和纬中路上所有交叉口的信号灯进行优 化配置，在保证车辆通行的前提下，使得两条主路上的车流平均速度最大。

### 本问需要完成什么
- 任务 1：根据所给数据和上述模型，对经中路和纬中路上所有交叉口的信号灯进行优 化配置，在保证车辆通行的前提下，使得两条主路上的车流平均速度最大

## 适配模型

- 主模型：图论网络与路径调度（CH4：复杂网络与图论模型）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH4/第4章-复杂网络与图论模型.md

### 候选模型与适配理由
- 规划优化与资源配置（CH3）：最大、配置；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md
- 图像文本与信号特征（CH10）：信号；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH10/第10章-图像、文本与信号数据.md
- 图论网络与路径调度（CH4）：交叉口；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH4/第4章-复杂网络与图论模型.md

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
- `g_EW=(C-L)*Q_EW/(Q_EW+Q_NS), g_NS=(C-L)-g_EW`
- `speed = v_free / (1 + alpha*(flow/capacity)^beta)`
- `maximize weighted_average_speed subject to min_green <= g <= max_green`

## Python 代码与运行方式

- 代码文件：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2024/E/q02/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2024/E/q02/solution.py`
- 批量运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：用问题 1 的小时流量摘要计算每个交叉口东西向和南北向关键流率。
- 步骤 2：按 Webster/比例分配思想给出两相位绿灯配置，并施加最小/最大绿灯约束。
- 步骤 3：用 BPR 型速度指数比较优化前后两条主路的平均速度。
- 步骤 4：输出每个交叉口的周期、绿灯时间、关键流率和速度改善估计。

## 实验结果与解释

### 产物文件
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2024/E/q02/experiment_table.csv

### 数据来源
- 类型：attachment
- 附件：/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/E题/附件1.xlsx; /Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/E题/附件2.csv; /Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/E题/附件3.pdf
- 读取规模：8844996 行 x 4 列
- 说明：本题专用算法分块读取附件2的884万条车辆记录，结合附件1方向/距离信息构建交通流量、信号配时、巡游车和管控效果摘要。

### result.json 核心结果

```json
{
  "method": "network_signal_timing_webster_optimization",
  "intersections": 12,
  "cycle_s": 120.0,
  "average_speed_before_index_kmh": 34.4306,
  "average_speed_after_index_kmh": 37.316,
  "average_speed_improvement_pct": 8.3801,
  "sample_signal_rows": [
    {
      "intersection": "环东路-纬中路",
      "cycle_s": 120.0,
      "green_EW_s": 30.85,
      "green_NS_s": 81.15,
      "avg_EW_flow_veh_per_hour": 47.662,
      "avg_NS_flow_veh_per_hour": 125.3727,
      "speed_before_index_kmh": 37.9995,
      "speed_after_index_kmh": 40.4396,
      "speed_improvement_pct": 6.4215
    },
    {
      "intersection": "环西路-纬中路",
      "cycle_s": 120.0,
      "green_EW_s": 66.83,
      "green_NS_s": 45.17,
      "avg_EW_flow_veh_per_hour": 1456.2431,
      "avg_NS_flow_veh_per_hour": 984.39,
      "speed_before_index_kmh": 25.2156,
      "speed_after_index_kmh": 27.5061,
      "speed_improvement_pct": 9.0838
    },
    {
      "intersection": "纬中路-景区出入口",
      "cycle_s": 120.0,
      "green_EW_s": 87.0,
      "green_NS_s": 25.0,
      "avg_EW_flow_veh_per_hour": 602.066,
      "avg_NS_flow_veh_per_hour": 14.8866,
      "speed_before_index_kmh": 37.9215,
      "speed_after_index_kmh": 40.0399,
      "speed_improvement_pct": 5.5862
    },
    {
      "intersection": "经一路-纬中路",
      "cycle_s": 120.0,
      "green_EW_s": 74.29,
      "green_NS_s": 37.71,
      "avg_EW_flow_veh_per_hour": 582.3981,
      "avg_NS_flow_veh_per_hour": 295.6528,
      "speed_before_index_kmh": 37.68,
      "speed_after_index_kmh": 40.5319,
      "speed_improvement_pct": 7.5688
    },
    {
      "intersection": "经三路-纬中路",
      "cycle_s": 120.0,
      "green_EW_s": 67.64,
      "green_NS_s": 44.36,
      "avg_EW_flow_veh_per_hour": 568.6215,
      "avg_NS_flow_veh_per_hour": 372.8646,
      "speed_before_index_kmh": 37.5781,
      "speed_after_index_kmh": 40.9232,
      "speed_improvement_pct": 8.9016
    },
    {
      "intersection": "经中路-环北路",
      "cycle_s": 120.0,
      "green_EW_s": 36.47,
      "green_NS_s": 75.53,
      "avg_EW_flow_veh_per_hour": 292.0648,
      "avg_NS_flow_veh_per_hour": 604.853,
      "speed_before_index_kmh": 37.6518,
      "speed_after_index_kmh": 40.4177,
      "speed_improvement_pct": 7.3458
    },
    {
      "intersection": "经中路-环南路",
      "cycle_s": 120.0,
      "green_EW_s": 55.44,
      "green_NS_s": 56.56,
      "avg_EW_flow_veh_per_hour": 660.6123,
      "avg_NS_flow_veh_per_hour": 673.8785,
      "speed_before_index_kmh": 36.3526,
      "speed_after_index_kmh": 40.6505,
      "speed_improvement_pct": 11.8228
    },
    {
      "intersection": "经中路-纬一路",
      "cycle_s": 120.0,
      "green_EW_s": 27.1,
      "green_NS_s": 84.9,
      "avg_EW_flow_veh_per_hour": 204.6377,
      "avg_NS_flow_veh_per_hour": 641.1609,
      "speed_before_index_kmh": 37.7241,
      "speed_after_index_kmh": 39.9395,
      "speed_improvement_pct": 5.8725
    }
  ]
}
```

### 结果解释
- 本问用 `network_signal_timing_webster_optimization` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 实验报告

本问的核心是：根据所给数据和上述模型，对经中路和纬中路上所有交叉口的信号灯进行优 化配置，在保证车辆通行的前提下，使得两条主路上的车流平均速度最大。

建模时先将题目要求拆成 1 个任务，再选择 `图论网络与路径调度`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
