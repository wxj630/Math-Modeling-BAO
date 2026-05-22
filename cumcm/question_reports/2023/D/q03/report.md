# 2023-D 问题 3 建模求解实验报告

## 题目原文与任务拆解

- 题目：2023年 CUMCM D题：圈养湖羊的空间利用率
- 问题：问题 3
- 原问：问题 1 和问题 2 中用到的数据都没有考虑不确定性，一旦决定了什么时间开始对 多少可配种的基础母羊进行配种，后续对羊栏的安排和需求也就随之确定。例如，用 3 个羊栏 给 42 只母羊进行配种，孕期需要 6 个羊栏，哺乳期需要 7 个羊栏给怀孕母羊分娩和哺乳， 哺乳 期结束就需要给 84 只断奶羔羊和 42 只母羊共安排 9 个羊栏进行育肥和休整。但实际情况并非 如此，配种成功率、分娩羔羊的数目和死亡率等都有不确定性，哺乳时间也可以调控，这些都 会影响空间需求。 现根据经验作以下考虑： (1) 母羊通过自然交配受孕率为 85%，交配期结束后 30 天可识别出是否成功受孕； (2) 在自然交配的 20 天中受孕母羊的受孕时间并不确知，而孕期会在 147-150 天内波动， 这些因素将影响到预产期范围； (3) 怀孕母羊分娩时一般每胎产羔 2 只，少部分每胎产羔 1 只或 3 只及以上，目前尚没有 实用手段控制或提前得知产羔数。羔羊出生时，有夭折的可能，多羔死亡率高于正常。通常可 以按平均每胎产羔 2.2 只、羔羊平均死亡率 3%估算。 (4) 母羊哺乳期过短不利于羔羊后期的生长，通常是羔羊体重达到一定标准后断奶；而哺乳 期过长，母羊的身体消耗就越大，早点断奶，有利于早恢复、早发情配种。一种经验做法是将 哺乳期控制在 35-45 天内，以 40 天为基准，哺乳期每减少1 天，羔羊的育肥期增加2 天；哺乳 期每增加 1 天， 羔羊的育肥期减少2 天。除此之外， 母羊的空怀休整期可在不少于18 天的前提 下灵活调控。 此外，如有必要，允许分娩日期相差不超过 7 天的哺乳期母羊及所产羔羊同栏，允许断奶 日期相差不超过 7 天的育肥期羔羊同栏，允许断奶日期相差不超过 7 天的休整期母羊同栏。为 简化问题，不考虑母羊流产、死亡以及羔羊在哺乳期或育肥期夭折和个体发育快慢等情况。 在以上不确定性的考虑下，生产计划的制定与问题 1 和问题 2 将有较大的不同：一旦作出 了“什么时间开始对多少可配种的基础母羊进行配种”的决定，后续羊栏的需求和安排不再是 随之确定的， 而是每一步都会出现若干种可能的情况需要作相应的并遵从基本规则的安排处理， 但无法改变或调整上一步。因此，某种意义上，本问题要讨论研究的生产计划将是一个应对多 种可能情况的“预案集”。 请综合考虑可行性和年化出栏羊只数量，制定具体的生产计划，使得整体方案的期望损失 最小。其中整体方案的损失由羊栏使用情况决定，当羊栏空置时， 每栏每天的损失为1； 当羊栏 数量不够时，所缺的羊栏每栏每天的损失（即租用费）为 3。

### 本问需要完成什么
- 任务 1：问题 1 和问题 2 中用到的数据都没有考虑不确定性，一旦决定了什么时间开始对 多少可配种的基础母羊进行配种，后续对羊栏的安排和需求也就随之确定。例如，用 3 个羊栏 给 42 只母羊进行配种，孕期需要 6 个羊栏，哺乳期需要 7 个羊栏给怀孕母羊分娩和哺乳， 哺乳 期结束就需要给 84 只断奶羔羊和 42 只母羊共安排 9 个羊栏进行育肥和休整。但实际情况并非 如此，配种成功率、分娩羔羊的数目和死亡率等都有不确定性，哺乳时间也可以调控，这些都 会影响空间需求。 现根据经验作以下考虑：
- 任务 2：(4) 母羊哺乳期过短不利于羔羊后期的生长，通常是羔羊体重达到一定标准后断奶；而哺乳 期过长，母羊的身体消耗就越大，早点断奶，有利于早恢复、早发情配种。一种经验做法是将 哺乳期控制在 35-45 天内，以 40 天为基准，哺乳期每减少1 天，羔羊的育肥期增加2 天；哺乳 期每增加 1 天， 羔羊的育肥期减少2 天。除此之外， 母羊的空怀休整期可在不少于18 天的前提 下灵活调控。 此外，如有必要，允许分娩日期相差不超过 7 天的哺乳期母羊及所产羔羊同栏，允许断奶 日期相差不超过 7 天的育肥期羔羊同栏，允许断奶日期相差不超过 7 天的休整期母羊同栏。为 简化问题，不考虑母羊流产、死亡以及羔羊在哺乳期或育肥期夭折和个体发育快慢等情况。 在以上不确定性的考虑下，生产计划的制定与问题 1 和问题 2 将有较大的不同：一旦作出 了“什么时间开始对多少可配种的基础母羊进行配种”的决定，后续羊栏的需求和安排不再是 随之确定的， 而是每一步都会出现若干种可能的情况需要作相应的并遵从基本规则的安排处理， 但无法改变或调整上一步。因此，某种意义上，本问题要讨论研究的生产计划将是一个应对多 种可能情况的“预案集”。 请综合考虑可行性和年化出栏羊只数量，制定具体的生产计划，使得整体方案的期望损失 最小。其中整体方案的损失由羊栏使用情况决定，当羊栏空置时， 每栏每天的损失为1； 当羊栏 数量不够时，所缺的羊栏每栏每天的损失（即租用费）为 3

## 适配模型

- 主模型：规划优化与资源配置（CH3：函数极值与规划模型）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md

### 候选模型与适配理由
- 时间序列预测（CH8）：日期、每天；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH8/第8章-时间序列.md
- 规划优化与资源配置（CH3）：最小、方案；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md
- 概率统计与抽样检验（CH9）：不确定；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH9/第九章-机器学习与统计模型.md

## 变量、约束与公式

### 建模假设
- 以题面给出的数值、约束和输出格式为第一优先级构造模型。
- 若原始附件尚未能被当前环境直接读取，脚本优先抽取题目原文中的参数和表格数字，并在数据来源中显式记录。
- 所有结果由本问 solution.py 运行生成，result.json 与 experiment_table.csv 保持同步。

### 变量定义
- b: 每批开始配种的基础母羊数量
- tau: 相邻批次开始配种的间隔天数
- M: 基础母羊存栏数，约为 b*C/tau
- R: 种公羊数量，满足不低于 1:50 且覆盖同时配种羊栏
- P_t: 第 t 天总羊栏需求
- Y: 年化出栏羔羊数量

### 约束条件
- 自然交配期每栏 1 只种公羊且不超过 14 只基础母羊。
- 怀孕期每栏不超过 8 只待产母羊。
- 哺乳期每栏不超过 6 只母羊及其羔羊。
- 育肥期每栏不超过 14 只羔羊，空怀休整期每栏不超过 14 只母羊。
- 确定性问题要求 max_t P_t <= 112；缺口估算用 max_t P_t - 112。

### 模型公式 / 目标函数
- `E[loss]=sum_t max(112-E[P_t],0)*1 + max(E[P_t]-112,0)*3`
- `E[Y] = 出栏批次数 * b * 受孕率 * 平均产羔数 * (1-死亡率)`
- `min E[loss]，同时报告年化出栏量和最大期望羊栏需求`

## Python 代码与运行方式

- 代码文件：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2023/D/q03/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2023/D/q03/solution.py`
- 批量运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：用问题 2 的批次排程作为候选框架。
- 步骤 2：把受孕率、平均产羔数、死亡率、哺乳期和休整期调控纳入期望羊栏需求。
- 步骤 3：枚举批次规模、批次间隔、哺乳期和休整期组合。
- 步骤 4：按空栏损失和租栏损失计算期望损失，输出最优预案集。

## 实验结果与解释

### 产物文件
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2023/D/q03/experiment_table.csv

### 数据来源
- 类型：problem_statement
- 附件：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2023/D.md
- 读取规模：36 行 x 38 列
- 说明：未找到可直接读取的数值附件，本问改用题目原文中的参数/表格数字生成实验结果。

### result.json 核心结果

```json
{
  "method": "uncertain_hu_sheep_expected_loss_plan_search",
  "best_preplan": {
    "batch_ewes": 42,
    "interval_days": 20,
    "lactation_days": 35,
    "rest_days": 20,
    "base_ewes": 471,
    "rams": 10,
    "expected_annual_output": 1371.3084,
    "max_expected_pens": 112.0,
    "mean_expected_pens": 110.273973,
    "utilization": 0.984589,
    "expected_loss": 630.0
  },
  "top_5_preplans": [
    {
      "batch_ewes": 42,
      "interval_days": 20,
      "lactation_days": 35,
      "rest_days": 20,
      "base_ewes": 471,
      "rams": 10,
      "expected_annual_output": 1371.3084,
      "max_expected_pens": 112.0,
      "mean_expected_pens": 110.273973,
      "utilization": 0.984589,
      "expected_loss": 630.0
    },
    {
      "batch_ewes": 42,
      "interval_days": 20,
      "lactation_days": 35,
      "rest_days": 24,
      "base_ewes": 479,
      "rams": 10,
      "expected_annual_output": 1371.3084,
      "max_expected_pens": 113.0,
      "mean_expected_pens": 111.073973,
      "utilization": 0.991732,
      "expected_loss": 642.0
    },
    {
      "batch_ewes": 42,
      "interval_days": 20,
      "lactation_days": 35,
      "rest_days": 18,
      "base_ewes": 467,
      "rams": 10,
      "expected_annual_output": 1371.3084,
      "max_expected_pens": 112.0,
      "mean_expected_pens": 110.076712,
      "utilization": 0.982828,
      "expected_loss": 702.0
    },
    {
      "batch_ewes": 35,
      "interval_days": 16,
      "lactation_days": 45,
      "rest_days": 18,
      "base_ewes": 508,
      "rams": 11,
      "expected_annual_output": 1460.1895,
      "max_expected_pens": 114.0,
      "mean_expected_pens": 112.567123,
      "utilization": 1.005064,
      "expected_loss": 713.0
    },
    {
      "batch_ewes": 42,
      "interval_days": 20,
      "lactation_days": 38,
      "rest_days": 20,
      "base_ewes": 477,
      "rams": 10,
      "expected_annual_output": 1371.3084,
      "max_expected_pens": 112.0,
      "mean_expected_pens": 109.682192,
      "utilization": 0.979305,
      "expected_loss": 846.0
    }
  ],
  "uncertainty_assumptions": {
    "pregnancy_rate": 0.85,
    "mean_lambs_per_pregnancy": 2.2,
    "lamb_mortality": 0.03,
    "lactation_days_candidates": [
      35,
      38,
      40,
      42,
      45
    ],
    "rest_days_candidates": [
      18,
      20,
      24
    ],
    "idle_pen_loss_per_day": 1,
    "shortage_pen_loss_per_day": 3
  },
  "note": "以期望羊栏需求近似预案集表现，按空栏损失和缺栏租用损失的期望和排序。"
}
```

### 结果解释
- 本问用 `uncertain_hu_sheep_expected_loss_plan_search` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 实验报告

本问的核心是：问题 1 和问题 2 中用到的数据都没有考虑不确定性，一旦决定了什么时间开始对 多少可配种的基础母羊进行配种，后续对羊栏的安排和需求也就随之确定。例如，用 3 个羊栏 给 42 只母羊进行配种，孕期需要 6 个羊栏，哺乳期需要 7 个羊栏给怀孕母羊分娩和哺乳， 哺乳 期结束就需要给 84 只断奶羔羊和 42 只母羊共安排 9 个羊栏进行育肥和休整。但实际情…

建模时先将题目要求拆成 2 个任务，再选择 `规划优化与资源配置`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
