# 2020-E 问题 2 建模求解实验报告

## 题目原文与任务拆解

- 题目：2020年 CUMCM E题：校园供水系统智能管理
- 问题：问题 2
- 原问：地下水管暗漏不容易被发现，需要花费大量人力对供水管道的漏损进行检测及定位，如果能够从水表的实时数据及时发现并确定发生漏损的位置，将极为有益。请帮助学校解决这个问题

### 本问需要完成什么
- 任务 1：地下水管暗漏不容易被发现，需要花费大量人力对供水管道的漏损进行检测及定位，如果能够从水表的实时数据及时发现并确定发生漏损的位置，将极为有益

## 适配模型

- 主模型：校园供水层级平衡、暗漏定位与维修决策（CH4：复杂网络与图论模型）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH4/第4章-复杂网络与图论模型.md

### 候选模型与适配理由
- 机器学习与统计识别（CH9）：检测；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH9/第九章-机器学习与统计模型.md
- 几何解析与运动学参数方程（CH1）：位置；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH1/第1章-解析方法与几何模型.md
- 数据拟合与回归分析（CH6）：数据；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH6/第六章-数据处理与拟合模型.md

## 变量、约束与公式

### 建模假设
- 附件四个季度的15分钟水表用量为校区供水系统实测运行数据，负用量视为抄表回退或换表异常并在漏损统计中截断为0。
- 水表层级编码按最长前缀建立父子关系；父表用量与直接子表用量之差作为该分支表观漏损或未计量用水。
- 夜间0:00-5:00用水应接近低负荷，持续夜间流量偏高是暗漏或异常用水的重要信号。
- 维修决策用水价、人工材料费和漏损下降比例的工程假设做经济性排序，目标是选择净收益为正且收益成本比高的分支。
- 通用基线保留在 `cumcm/generic_baselines`，当前结果从通用拟合/分类/线性规划推进为真实附件驱动的供水网络模型。

### 变量定义
- u_{m,t}: 水表m在15分钟时段t的用水量
- G=(V,E): 水表层级树，节点为水表编码，边为父子层级关系
- L_b: 分支b的表观漏损量或未计量水量
- r_b: 分支b的漏损率
- s_m: 水表m的夜间暗漏可疑评分
- x_b in {0,1}: 是否维修分支b

### 约束条件
- u_{m,t} >= 0，异常负读数不用于漏损收益计算。
- parent(b)由层级编码最长前缀确定，只有父表和至少一个子表均有读数时计算平衡。
- L_b=max(U_parent - sum U_child, 0)，r_b=L_b/max(U_parent, eps)。
- 暗漏候选优先选择夜间用水占比高、夜间均值高且处在高漏损分支上的水表。
- 维修方案仅选择预计年节水收益大于维修成本的候选项。

### 模型公式 / 目标函数
- `U_m=sum_t max(u_{m,t},0)`
- `night_share_m=sum_{hour(t)<5}u_{m,t}/U_m`
- `leak_score_m=0.40*z(night_share)+0.30*z(night_mean)+0.20*z(branch_loss_rate)+0.10*z(total_usage)`
- `annual_saving_b = excess_loss_b * 365/observed_days * water_price * repair_effect`
- `max sum_b x_b(annual_saving_b - repair_cost_b), subject to benefit_cost_ratio_b > 1`

## Python 代码与运行方式

- 代码文件：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2020/E/q02/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2020/E/q02/solution.py`
- 批量运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：复用问题1的层级平衡和水表用水特征。
- 步骤 2：提取0:00-5:00夜间低负荷时段的均值、占比和持续性特征。
- 步骤 3：结合水表所在分支的漏损率生成暗漏可疑评分，并按评分排序定位候选水表/分支。
- 步骤 4：输出暗漏候选表和夜间流量特征表。

## 实验结果与解释

### 产物文件
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2020/E/q02/dark_leak_candidates.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2020/E/q02/night_flow_features.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2020/E/q02/experiment_table.csv

### 数据来源
- 类型：attachment
- 附件：/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/E/附件_一季度.xlsx; /Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/E/附件_三季度.xlsx; /Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/E/附件_二季度.xlsx; /Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/E/附件_四季度.xlsx; /Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/E/附件_水表层级.xlsx
- 读取规模：3086881 行 x 15 列
- 说明：本题专用算法读取四个季度15分钟水表用量和水表层级关系，完成功能区用水特征、层级漏损平衡、暗漏定位和维修经济性决策。

### result.json 核心结果

```json
{
  "method": "campus_water_dark_leakage_localization",
  "record_count": 3086788,
  "candidate_count": 30,
  "night_flow_meter_count": 90,
  "top_candidate": {
    "meter_no": "3620300300",
    "meter_name": "64397副表",
    "function_zone": "其他区域",
    "total_usage_m3": 185988.92,
    "night_usage_m3": 26346.35,
    "night_usage_share": 0.141655,
    "night_mean_interval_m3": 3.638999,
    "night_active_interval_share": 0.998895,
    "branch_loss_rate": 0.0,
    "leak_score": 2.834522
  },
  "report": [
    "暗漏定位以夜间低负荷时段为主信号，并叠加水表所在分支的层级漏损率。",
    "候选表按可疑评分排序，包含夜间用水占比、夜间均值、分支漏损率和功能区。",
    "输出 `dark_leak_candidates.csv` 与 `night_flow_features.csv`，用于后勤巡检定位。"
  ]
}
```

### 结果解释
- 本问用 `campus_water_dark_leakage_localization` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 专用实验报告

- 暗漏定位以夜间低负荷时段为主信号，并叠加水表所在分支的层级漏损率。
- 候选表按可疑评分排序，包含夜间用水占比、夜间均值、分支漏损率和功能区。
- 输出 `dark_leak_candidates.csv` 与 `night_flow_features.csv`，用于后勤巡检定位。

## 实验报告

本问的核心是：地下水管暗漏不容易被发现，需要花费大量人力对供水管道的漏损进行检测及定位，如果能够从水表的实时数据及时发现并确定发生漏损的位置，将极为有益。请帮助学校解决这个问题

建模时先将题目要求拆成 1 个任务，再选择 `校园供水层级平衡、暗漏定位与维修决策`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
