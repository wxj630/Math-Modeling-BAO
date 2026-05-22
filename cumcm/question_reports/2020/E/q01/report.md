# 2020-E 问题 1 建模求解实验报告

## 题目原文与任务拆解

- 题目：2020年 CUMCM E题：校园供水系统智能管理
- 问题：问题 1
- 原问：输水管网的漏损是一个严重问题。资料显示，在维护良好的公共供水网络中，平均失水在5%左右；而在比较老旧的管网中，失水则会更多。请利用附件提供的数据，建立数学模型，分析该校园供水管网的漏损情况

### 本问需要完成什么
- 任务 1：而在比较老旧的管网中，失水则会更多
- 任务 2：请利用附件提供的数据，建立数学模型，分析该校园供水管网的漏损情况

## 适配模型

- 主模型：校园供水层级平衡、暗漏定位与维修决策（CH4：复杂网络与图论模型）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH4/第4章-复杂网络与图论模型.md

### 候选模型与适配理由
- 数据拟合与回归分析（CH6）：数据、分析；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH6/第六章-数据处理与拟合模型.md
- 图论网络与路径调度（CH4）：网络；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH4/第4章-复杂网络与图论模型.md
- 综合评价与权重决策（CH7）：比较；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH7/第7章-权重生成与评价模型.md

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

- 代码文件：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2020/E/q01/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2020/E/q01/solution.py`
- 批量运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：读取四个季度水表用量和水表层级关系表，清洗水表号、时间和用量字段。
- 步骤 2：按水表和功能区统计总用量、夜间用量、峰值和季度变化特征。
- 步骤 3：按层级编码重建父子关系，对可比父子节点计算父表-子表用量平衡和漏损率。
- 步骤 4：输出水表用水特征表、功能区汇总表和层级漏损平衡表。

## 实验结果与解释

### 产物文件
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2020/E/q01/meter_usage_features.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2020/E/q01/hierarchy_loss_balance.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2020/E/q01/functional_zone_usage.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2020/E/q01/experiment_table.csv

### 数据来源
- 类型：attachment
- 附件：/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/E/附件_一季度.xlsx; /Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/E/附件_三季度.xlsx; /Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/E/附件_二季度.xlsx; /Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/E/附件_四季度.xlsx; /Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/E/附件_水表层级.xlsx
- 读取规模：3086881 行 x 15 列
- 说明：本题专用算法读取四个季度15分钟水表用量和水表层级关系，完成功能区用水特征、层级漏损平衡、暗漏定位和维修经济性决策。

### result.json 核心结果

```json
{
  "method": "campus_water_network_loss_balance",
  "record_count": 3086788,
  "meter_count": 92,
  "hierarchy_node_count": 93,
  "parent_balance_count": 15,
  "overall_loss_volume_m3": 161292.4,
  "overall_loss_rate": 0.282982,
  "top_loss_branches": [
    {
      "code": "416X",
      "meter_no": "3620300500",
      "meter_name": "校医院南+",
      "level": 1,
      "child_count": 1,
      "parent_usage_m3": 24145.4,
      "child_usage_m3": 2034.36,
      "residual_m3": 22111.04,
      "loss_volume_m3": 22111.04,
      "loss_rate": 0.915745,
      "child_codes": "41601X",
      "function_zone": "办公服务区",
      "caliber_mm": 100.0
    },
    {
      "code": "40405T",
      "meter_no": "3320100600",
      "meter_name": "XXX第八学生宿舍",
      "level": 2,
      "child_count": 1,
      "parent_usage_m3": 9416.71,
      "child_usage_m3": 1683.12,
      "residual_m3": 7733.59,
      "loss_volume_m3": 7733.59,
      "loss_rate": 0.821262,
      "child_codes": "4040501T",
      "function_zone": "宿舍生活区",
      "caliber_mm": 50.0
    },
    {
      "code": "41601X",
      "meter_no": "3290100100",
      "meter_name": "XXX校医院",
      "level": 2,
      "child_count": 1,
      "parent_usage_m3": 2034.36,
      "child_usage_m3": 420.63,
      "residual_m3": 1613.73,
      "loss_volume_m3": 1613.73,
      "loss_rate": 0.793237,
      "child_codes": "4160101T",
      "function_zone": "办公服务区",
      "caliber_mm": 50.0
    },
    {
      "code": "4033501T",
      "meter_no": "3320100300",
      "meter_name": "XXX第三学生宿舍",
      "level": 3,
      "child_count": 1,
      "parent_usage_m3": 11512.09,
      "child_usage_m3": 2963.81,
      "residual_m3": 8548.28,
      "loss_volume_m3": 8548.28,
      "loss_rate": 0.742548,
      "child_codes": "403350101T",
      "function_zone": "宿舍生活区",
      "caliber_mm": 80.0
    },
    {
      "code": "40337X",
      "meter_no": "3620301400",
      "meter_name": "区域4+",
      "level": 2,
      "child_count": 4,
      "parent_usage_m3": 109700.91,
      "child_usage_m3": 30212.47,
      "residual_m3": 79488.44,
      "loss_volume_m3": 79488.44,
      "loss_rate": 0.724592,
      "child_codes": "4033726T;4033725T;4033723T;4033720T",
      "function_zone": "其他区域",
      "caliber_mm": 150.0
    },
    {
      "code": "4033502T",
      "meter_no": "3320100400",
      "meter_name": "XXX第四学生宿舍",
      "level": 3,
      "child_count": 2,
      "parent_usage_m3": 18459.58,
      "child_usage_m3": 5804.05,
      "residual_m3": 12655.53,
      "loss_volume_m3": 12655.53,
      "loss_rate": 0.685581,
      "child_codes": "403350202T;403350201T",
      "function_zone": "宿舍生活区",
      "caliber_mm": 80.0
    },
    {
      "code": "4033503T",
      "meter_no": "3320100500",
      "meter_name": "XXX第五学生宿舍",
      "level": 3,
      "child_count": 1,
      "parent_usage_m3": 18745.84,
      "child_usage_m3": 5983.49,
      "residual_m3": 12762.35,
      "loss_volume_m3": 12762.35,
      "loss_rate": 0.68081,
      "child_codes": "403350301T",
      "function_zone": "宿舍生活区",
      "caliber_mm": 80.0
    },
    {
      "code": "40134X",
      "meter_no": "3000000001",
      "meter_name": "区域2",
      "level": 2,
      "child_count": 6,
      "parent_usage_m3": 16256.67,
      "child_usage_m3": 8087.28,
      "residual_m3": 8169.39,
      "loss_volume_m3": 8169.39,
      "loss_rate": 0.502525,
      "child_codes": "4013407X;4013406T;4013404T;4013403T;4013402T;4013401T",
      "function_zone": "其他区域",
      "caliber_mm": 150.0
    },
    {
      "code": "40135X",
      "meter_no": "3315400100",
      "meter_name": "XXX国际纳米研究所",
      "level": 2,
      "child_count": 2,
      "parent_usage_m3": 1075.85,
      "child_usage_m3": 661.53,
      "residual_m3": 414.32,
      "loss_volume_m3": 414.32,
      "loss_rate": 0.385109,
      "child_codes": "4013502T;4013501T",
      "function_zone": "教学科研区",
      "caliber_mm": 50.0
    },
    {
      "code": "40335X",
      "meter_no": "3620300400",
      "meter_name": "区域3+",
      "level": 2,
      "child_count": 4,
      "parent_usage_m3": 57152.87,
      "child_usage_m3": 50616.09,
      "residual_m3": 6536.78,
      "loss_volume_m3": 6536.78,
      "loss_rate": 0.114374,
      "child_codes": "4033506T;4033503T;4033502T;4033501T",
      "function_zone": "其他区域",
      "caliber_mm": 150.0
    }
  ],
  "report": [
    "本问读取四个季度约300万条15分钟水表记录，并重建水表层级父子关系。",
    "按功能区输出季度用水特征，按父表-子表平衡计算表观漏损率。",
    "输出 `meter_usage_features.csv`、`functional_zone_usage.csv` 和 `hierarchy_loss_balance.csv`。"
  ]
}
```

### 结果解释
- 本问用 `campus_water_network_loss_balance` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 专用实验报告

- 本问读取四个季度约300万条15分钟水表记录，并重建水表层级父子关系。
- 按功能区输出季度用水特征，按父表-子表平衡计算表观漏损率。
- 输出 `meter_usage_features.csv`、`functional_zone_usage.csv` 和 `hierarchy_loss_balance.csv`。

## 实验报告

本问的核心是：输水管网的漏损是一个严重问题。资料显示，在维护良好的公共供水网络中，平均失水在5%左右；而在比较老旧的管网中，失水则会更多。请利用附件提供的数据，建立数学模型，分析该校园供水管网的漏损情况

建模时先将题目要求拆成 2 个任务，再选择 `校园供水层级平衡、暗漏定位与维修决策`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
