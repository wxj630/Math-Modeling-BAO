# 2017-B 问题 5 建模求解实验报告

## 题目原文与任务拆解

- 题目：2017年 CUMCM B题：拍照赚钱”的任务定价
- 问题：问题 5
- 原问：对附件三中的新项目给出你的任务定价方案，并评价该方案的实施效果

### 本问需要完成什么
- 任务 1：对附件三中的新项目给出你的任务定价方案，并评价该方案的实施效果

## 适配模型

- 主模型：众包任务地理供需定价与完成概率模型（CH3：函数极值与规划模型）
- 教程参考：../My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md

### 候选模型与适配理由
- 规划优化与资源配置（CH3）：方案；参考 ../My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md
- 综合评价与权重决策（CH7）：评价；参考 ../My-Agent/intro-mathmodel/docs/CH7/第7章-权重生成与评价模型.md

## 变量、约束与公式

### 建模假设
- 任务是否完成主要受任务标价、周边会员供给能力、会员信誉、任务密集度和地理距离共同影响。
- 会员预订限额近似表示可承接能力；信誉越高、距离越近，对任务完成概率贡献越大。
- 新项目没有完成标签，使用附件一训练的完成概率模型迁移到附件三，并通过价格网格搜索给出可复现报价。
- 集中任务打包时，用空间聚类识别近邻任务组，打包价格在单任务报价基础上给予效率折扣并提高预期完成概率。
- 通用基线继续保留在 `cumcm/generic_baselines`，本专用解法保留从通用LP/TOPSIS到真实附件驱动模型的进步轨迹。

### 变量定义
- p_i: 第 i 个任务的定价
- y_i in {0,1}: 历史任务完成状态
- d_i: 第 i 个任务到最近会员的距离
- m_i, c_i, r_i: 任务周边会员数、预订能力和信誉供给
- rho_i: 任务周边竞争密度
- P_i = P(y_i=1 | p_i,d_i,m_i,c_i,r_i,rho_i): 完成概率

### 约束条件
- 历史任务使用附件一原始标价和完成状态训练模型。
- 推荐价格限定在历史价格范围附近，且以0.5元为步长便于平台执行。
- 打包任务只合并空间距离较近的任务，单任务仍保留可拆分报价作为对照。
- 新项目评价以预测完成率、预算和高风险任务比例为核心指标。

### 模型公式 / 目标函数
- `logit(P_i)=beta0+beta1*p_i+beta2*d_i+beta3*m_i+beta4*c_i+beta5*r_i+beta6*rho_i`
- `p_i^*=min p subject to P_i(p)>=target_probability`
- `bundle_price_g = discount * sum_{i in g} p_i^* + density_bonus_g`
- `expected_completion_rate = mean_i P_i(p_i^*)`

## Python 代码与运行方式

- 代码文件：cumcm/question_solutions/2017/B/q05/solution.py
- 单问运行：`.venv/bin/python cumcm/question_solutions/2017/B/q05/solution.py`
- 批量运行：`.venv/bin/python cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：读取附件一历史任务、附件二会员和附件三新任务，并清洗GPS坐标。
- 步骤 2：计算每个任务的最近会员距离、3公里会员数、3公里能力/信誉供给和1公里任务密度。
- 步骤 3：用逻辑回归拟合完成概率，解释未完成原因。
- 步骤 4：对历史任务和新任务做价格网格搜索，得到满足目标完成概率的最小推荐价。
- 步骤 5：用空间聚类识别集中任务，生成打包价格、预期完成率和实施效果评价表。

## 实验结果与解释

### 产物文件
- cumcm/question_artifacts/2017/B/q05/historical_task_features.csv
- cumcm/question_artifacts/2017/B/q05/unfinished_reason_summary.csv
- cumcm/question_artifacts/2017/B/q05/repricing_scheme.csv
- cumcm/question_artifacts/2017/B/q05/pricing_comparison.csv
- cumcm/question_artifacts/2017/B/q05/bundle_pricing.csv
- cumcm/question_artifacts/2017/B/q05/new_project_pricing.csv
- cumcm/question_artifacts/2017/B/q05/new_project_effect_evaluation.csv
- cumcm/question_artifacts/2017/B/q05/completion_model_coefficients.csv
- cumcm/question_artifacts/2017/B/q05/experiment_table.csv

### 数据来源
- 类型：attachment
- 附件：../../Documents/Playground/cumcm_unzipped/2017_IqAO5Qqi8f23d8738a07a0604b8629ce9bb061ad/CUMCM2017Problems/B/附件一：已结束项目任务数据.xls; ../../Documents/Playground/cumcm_unzipped/2017_IqAO5Qqi8f23d8738a07a0604b8629ce9bb061ad/CUMCM2017Problems/B/附件三：新项目任务数据.xls; ../../Documents/Playground/cumcm_unzipped/2017_IqAO5Qqi8f23d8738a07a0604b8629ce9bb061ad/CUMCM2017Problems/B/附件二：会员信息数据.xlsx
- 读取规模：4778 行 x 5 列
- 说明：本题专用算法读取历史任务、会员信息和新项目任务，构建地理供需特征、完成概率模型、重定价方案、打包聚类和新项目定价评估。

### result.json 核心结果

```json
{
  "method": "crowdsourcing_new_project_pricing",
  "historical_task_count": 835,
  "member_count": 1877,
  "new_task_count": 2066,
  "priced_task_count": 2066,
  "observed_completion_rate": 0.62515,
  "completion_model_auc": 0.69251,
  "average_original_price": 69.1108,
  "average_recommended_price": 85.9431,
  "expected_completion_rate_after_repricing": 0.690689,
  "unfinished_reason_summary": [
    {
      "reason": "price_too_low",
      "task_count": 161,
      "share_of_unfinished": 0.514377,
      "explanation": "标价处于历史低位，价格激励不足。"
    },
    {
      "reason": "far_from_members",
      "task_count": 59,
      "share_of_unfinished": 0.188498,
      "explanation": "距离附近会员较远，可承接人群少。"
    },
    {
      "reason": "weak_nearby_capacity",
      "task_count": 58,
      "share_of_unfinished": 0.185304,
      "explanation": "3公里范围预订能力低，供给不足。"
    },
    {
      "reason": "high_task_density",
      "task_count": 129,
      "share_of_unfinished": 0.412141,
      "explanation": "周边任务密集，存在竞争分流。"
    },
    {
      "reason": "low_model_probability",
      "task_count": 167,
      "share_of_unfinished": 0.533546,
      "explanation": "综合完成概率偏低，需提价或打包。"
    }
  ],
  "pricing_comparison": [
    {
      "scenario": "original",
      "completion_rate": 0.6251497005988024,
      "average_price": 69.11077844311377,
      "total_budget": 57707.5
    },
    {
      "scenario": "optimized",
      "completion_rate": 0.6906893461077844,
      "average_price": 85.94311377245509,
      "total_budget": 71762.5
    }
  ],
  "bundle_count": 610,
  "clustered_bundle_count": 77,
  "bundle_expected_completion_rate": 0.702582,
  "expected_completion_rate": 0.742044,
  "new_project_average_price": 69.6776,
  "total_budget": 143954.0,
  "high_risk_task_count": 94,
  "report": [
    "本题用附件一的历史任务训练地理供需完成概率模型，附件二会员数据提供周边会员数量、限额和信誉供给。",
    "未完成原因按低价格、远离会员、附近能力不足、任务密集竞争和模型低概率五类归因。",
    "历史重定价和新项目定价均通过价格网格搜索得到满足目标完成概率的最低可执行报价。",
    "密集任务用DBSCAN空间聚类打包，输出打包价格和预期完成率，通用基线仍保留作对照。"
  ]
}
```

### 结果解释
- 本问用 `crowdsourcing_new_project_pricing` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 专用实验报告

- 本题用附件一的历史任务训练地理供需完成概率模型，附件二会员数据提供周边会员数量、限额和信誉供给。
- 未完成原因按低价格、远离会员、附近能力不足、任务密集竞争和模型低概率五类归因。
- 历史重定价和新项目定价均通过价格网格搜索得到满足目标完成概率的最低可执行报价。
- 密集任务用DBSCAN空间聚类打包，输出打包价格和预期完成率，通用基线仍保留作对照。

## 实验报告

本问的核心是：对附件三中的新项目给出你的任务定价方案，并评价该方案的实施效果

建模时先将题目要求拆成 1 个任务，再选择 `众包任务地理供需定价与完成概率模型`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
