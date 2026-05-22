# 2024-E 问题 4 建模求解实验报告

## 题目原文与任务拆解

- 题目：2024年 CUMCM E题：交通流量管控
- 问题：问题 4
- 原问：五一黄金周期间，该小镇对景区周边道路实行了临时性交通管理措施，具体 管控措施见附件 3。请结合数据评价临时管控措施在两条主路上的效果。 附件 1 路段行驶方向编号及交叉口之间的距离 附件 2 纬中路各交叉口车辆信息 附件 3 五一黄金周期间交通管控措施

### 本问需要完成什么
- 任务 1：请结合数据评价临时管控措施在两条主路上的效果

## 适配模型

- 主模型：图论网络与路径调度（CH4：复杂网络与图论模型）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH4/第4章-复杂网络与图论模型.md

### 候选模型与适配理由
- 图论网络与路径调度（CH4）：交通、交叉口；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH4/第4章-复杂网络与图论模型.md
- 几何解析与运动学参数方程（CH1）：距离；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH1/第1章-解析方法与几何模型.md
- 数据拟合与回归分析（CH6）：数据；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH6/第六章-数据处理与拟合模型.md

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
- `effect = control_period_metric - baseline_period_metric`
- `baseline: 2024-04-24 to 2024-04-30; control: 2024-05-01 to 2024-05-05`
- `score = speed_improvement - congestion_penalty - cruising_penalty`

## Python 代码与运行方式

- 代码文件：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2024/E/q04/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2024/E/q04/solution.py`
- 批量运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：构造管控前基线窗口和五一管控窗口。
- 步骤 2：比较总流量、峰值小时流量、速度指数和巡游车辆占比。
- 步骤 3：按两条主路和整体给出管控效果评价。
- 步骤 4：输出 before-after 指标表和综合评价结论。

## 实验结果与解释

### 产物文件
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2024/E/q04/experiment_table.csv

### 数据来源
- 类型：attachment
- 附件：/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/E题/附件1.xlsx; /Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/E题/附件2.csv; /Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/E题/附件3.pdf
- 读取规模：8844996 行 x 4 列
- 说明：本题专用算法分块读取附件2的884万条车辆记录，结合附件1方向/距离信息构建交通流量、信号配时、巡游车和管控效果摘要。

### result.json 核心结果

```json
{
  "method": "temporary_control_before_after_effect_evaluation",
  "baseline_period": {
    "start_date": "2024-04-24",
    "end_date": "2024-04-30",
    "total_vehicle_records": 1808261,
    "peak_hour_records": 20377,
    "average_speed_index_kmh": 35.9523,
    "peak_active_cruising_vehicles": 0,
    "cruising_peak_rate": 0.0
  },
  "control_period": {
    "start_date": "2024-05-01",
    "end_date": "2024-05-05",
    "total_vehicle_records": 1412072,
    "peak_hour_records": 23959,
    "average_speed_index_kmh": 35.7961,
    "peak_active_cruising_vehicles": 10391,
    "cruising_peak_rate": 0.433699
  },
  "speed_delta_kmh": -0.1562,
  "peak_hour_delta_pct": 17.5786,
  "cruising_peak_rate_delta": 0.433699,
  "effect_score": -9.1818,
  "interpretation": "score>0 表示速度改善能覆盖峰值流量和巡游占比上升带来的压力；score<=0 表示管控效果需谨慎评价。"
}
```

### 结果解释
- 本问用 `temporary_control_before_after_effect_evaluation` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 实验报告

本问的核心是：五一黄金周期间，该小镇对景区周边道路实行了临时性交通管理措施，具体 管控措施见附件 3。请结合数据评价临时管控措施在两条主路上的效果。 附件 1 路段行驶方向编号及交叉口之间的距离 附件 2 纬中路各交叉口车辆信息 附件 3 五一黄金周期间交通管控措施

建模时先将题目要求拆成 1 个任务，再选择 `图论网络与路径调度`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
