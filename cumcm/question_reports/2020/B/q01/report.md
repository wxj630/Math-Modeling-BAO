# 2020-B 问题 1 建模求解实验报告

## 题目原文与任务拆解

- 题目：2020年 CUMCM B题：穿越沙漠
- 问题：问题 1
- 原问：以天为基本时间单位，游戏的开始时间为第0天，玩家位于起点。玩家必须在截止日期或之前到达终点，到达终点后该玩家的游戏结束。

### 本问需要完成什么
- 任务 1：以天为基本时间单位，游戏的开始时间为第0天，玩家位于起点
- 任务 2：玩家必须在截止日期或之前到达终点，到达终点后该玩家的游戏结束

## 适配模型

- 主模型：沙漠穿越动态规划与资源路径策略（CH3：函数极值与规划模型）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md

### 候选模型与适配理由
- 时间序列预测（CH8）：日期；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH8/第8章-时间序列.md

## 变量、约束与公式

### 建模假设
- 把附件地图抽象为无向图 G=(V,E)，节点为区域，边表示有公共边界且可一天到达。
- 晴朗、高温、沙暴三种天气决定水和食物的基础消耗量；行走消耗为基础消耗的2倍，挖矿消耗为基础消耗的3倍。
- 玩家第0天在起点一次性购买计划所需资源；到达村庄后可按2倍基准价补给，本实验优先选择不触发村庄补给的可行策略。
- 挖矿只能在矿山连续停留的次日开始；沙暴日不能移动但可以停留或挖矿。
- 附件地图图形在 docx 中以 VML 组合图保存；本实验用节点编号的行列网格/链式近似重建相邻关系，并在报告中显式记录。

### 变量定义
- v_t: 第 t 天结束后所在区域节点
- a_t ∈ {move, stay, mine}: 第 t 天行动
- w_t, f_t: 第 t 天消耗后剩余水和食物箱数
- m_t: 第 t 天消耗后剩余资金
- P: 从起点到终点并可能经过矿山/村庄的行动序列

### 约束条件
- v_0=start, v_t=finish 后游戏结束。
- 若天气为沙暴，则 a_t 不能为 move。
- 若 a_t=move，则 (v_{t-1},v_t) ∈ E；若 a_t=stay/mine，则 v_t=v_{t-1}。
- 3*w_t + 2*f_t <= 1200 且 w_t,f_t >= 0。
- 到达矿山当天不能挖矿，只有前一日已经在同一矿山时才允许 a_t=mine。

### 模型公式 / 目标函数
- `max m_T + 0.5*(price_water*w_T + price_food*f_T)`
- `consumption(a,weather)=base(weather)*multiplier(a), multiplier(stay)=1, multiplier(move)=2, multiplier(mine)=3`
- `DP[t,node,can_mine] = best cash proxy after day t at node`
- `known-weather uses deterministic DP; current-weather/adaptive questions compare scenario policies.`

## Python 代码与运行方式

- 代码文件：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2020/B/q01/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2020/B/q01/solution.py`
- 批量运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：从附件文本中读取各关负重、资金、截止日期、基础收益、资源参数和天气序列。
- 步骤 2：为每关构建地图图：第一/二关用行列网格近似，第三/五关用链式加矿山支路，第四/六关用5x5网格。
- 步骤 3：按天、节点、是否可挖矿做动态规划，逐日枚举停留、移动、挖矿行动。
- 步骤 4：回溯最优行动序列，计算总水/食物消耗、采购成本、挖矿收益、剩余资金和每日结果表。
- 步骤 5：对未知天气题生成保守天气场景，并与已知天气题共用同一资源可行性检查。

## 实验结果与解释

### 产物文件
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2020/B/q01/desert_strategy.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2020/B/q01/experiment_table.csv

### 数据来源
- 类型：attachment
- 附件：/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/B/2020B-穿越沙漠.docx; /Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/B/Result.xlsx; /Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/B/附件.docx
- 读取规模：6 行 x 30 列
- 说明：本题专用算法读取附件.docx中的六关参数/天气，按节点编号重建地图近似图，并为第一、二关写出Result.xlsx填报版。

### result.json 核心结果

```json
{
  "method": "desert_rule_component_dynamic_programming",
  "levels_solved": [
    "第一关"
  ],
  "cooperative_players": 1,
  "level_summaries": [
    {
      "level": "第一关",
      "reached_finish": true,
      "finish_day": 16,
      "final_cash": 9700.0,
      "initial_water_boxes": 232,
      "initial_food_boxes": 214,
      "initial_load_kg": 1124,
      "load_feasible": true,
      "purchase_cost": 3300,
      "mining_days": 3,
      "mining_income_total": 3000.0,
      "route_days": [
        2,
        3,
        12,
        12,
        12,
        12,
        12,
        12,
        13,
        14,
        14,
        15,
        16,
        17,
        18,
        27
      ],
      "map_note": "27节点按3x9行列网格近似重建。"
    }
  ],
  "graph_reconstruction_note": "附件地图为Word VML组合图，本实验按节点编号近似重建邻接图；通用基线仍保留在 generic_baselines 作为旧版对照。",
  "report": [
    "本问使用 `desert_rule_component_dynamic_programming`，把穿越沙漠转化为按天展开的图上动态规划。",
    "状态记录所在节点和是否允许挖矿，转移枚举停留、移动、挖矿，并按天气扣减水和食物。",
    "策略表 `desert_strategy.csv` 给出每天区域、行动、天气、消耗后剩余资金/水/食物。",
    "由于附件地图图形不是结构化边表，当前版本采用节点编号网格/链式近似；后续若人工标注完整邻接边，可直接替换 graph 字段得到更接近官方地图的结果。"
  ]
}
```

### 结果解释
- 本问用 `desert_rule_component_dynamic_programming` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 专用实验报告

- 本问使用 `desert_rule_component_dynamic_programming`，把穿越沙漠转化为按天展开的图上动态规划。
- 状态记录所在节点和是否允许挖矿，转移枚举停留、移动、挖矿，并按天气扣减水和食物。
- 策略表 `desert_strategy.csv` 给出每天区域、行动、天气、消耗后剩余资金/水/食物。
- 由于附件地图图形不是结构化边表，当前版本采用节点编号网格/链式近似；后续若人工标注完整邻接边，可直接替换 graph 字段得到更接近官方地图的结果。

## 实验报告

本问的核心是：以天为基本时间单位，游戏的开始时间为第0天，玩家位于起点。玩家必须在截止日期或之前到达终点，到达终点后该玩家的游戏结束。

建模时先将题目要求拆成 2 个任务，再选择 `沙漠穿越动态规划与资源路径策略`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
