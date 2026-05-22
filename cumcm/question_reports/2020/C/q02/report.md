# 2020-C 问题 2 建模求解实验报告

## 题目原文与任务拆解

- 题目：2020年 CUMCM C题：中小微企业的信贷决策
- 问题：问题 2
- 原问：在问题1的基础上，对附件2中302家企业的信贷风险进行量化分析，并给出该银行在年度信贷总额为1亿元时对这些企业的信贷策略。

### 本问需要完成什么
- 任务 1：在问题1的基础上，对附件2中302家企业的信贷风险进行量化分析，并给出该银行在年度信贷总额为1亿元时对这些企业的信贷策略

## 适配模型

- 主模型：企业信用风险评分与授信组合优化（CH9：机器学习与统计模型）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH9/第九章-机器学习与统计模型.md

### 候选模型与适配理由
- 时间序列预测（CH8）：年度；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH8/第8章-时间序列.md
- 概率统计与抽样检验（CH9）：风险；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH9/第九章-机器学习与统计模型.md
- 规划优化与资源配置（CH3）：策略；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md

## 变量、约束与公式

### 建模假设
- 有效发票反映真实经营活动，作废发票和负数发票反映交易稳定性与退货/冲销风险。
- 销项发票金额刻画销售规模，进项发票金额刻画采购规模，二者差额可作为毛利能力代理指标。
- 附件1企业的信誉评级和是否违约用于校准风险分；附件2企业无信贷记录时用附件1的特征分布作参照。
- 贷款额在10万到100万元之间，信誉评级D或风险过高企业原则上不予授信。
- 客户流失率由附件3的利率-流失率曲线估计，利率选择以风险调整后期望收益最大为准。

### 变量定义
- r_i: 企业 i 的信用风险分，取值越大表示违约或拒贷风险越高
- s_i: 企业 i 的经营规模评分，由销项/进项有效发票金额归一化得到
- m_i: 企业 i 的毛利能力代理指标
- u_i: 企业 i 的作废发票比例，反映交易稳定性
- a_i: 企业 i 是否获批授信的0-1决策
- L_i: 企业 i 的授信额度
- rho_i: 企业 i 的贷款年利率
- lambda_i(rho_i): 附件3曲线给出的客户流失率

### 约束条件
- 0 <= r_i <= 1，风险分由规模、毛利、作废率、负数率、客户集中度和增长率加权合成。
- 100000 <= L_i <= 1000000；若 a_i=0，则 L_i=0。
- sum_i L_i <= B，其中问题1用5000万元情景，问题2/3用1亿元情景。
- 信誉评级D或 r_i >= 0.74 的企业不予放贷。
- 突发因素情景下，客户集中度高且近期增长弱的企业风险上调。

### 模型公式 / 目标函数
- `risk_i = w1*(1-scale_i)+w2*(1-margin_i)+w3*invalid_i+w4*negative_i+w5*concentration_i+w6*(1-partner_i)+w7*(1-growth_i)`
- `known_risk_i = 0.70*risk_i + 0.30*rating_risk_i`
- `expected_yield_i = rho_i*(1-lambda_i)*(1-r_i) - 0.08*r_i`
- `priority_i = expected_yield_i * log(1+business_scale_i)`
- `max sum_i L_i*expected_yield_i, s.t. sum_i L_i <= B and lending rules.`

## Python 代码与运行方式

- 代码文件：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2020/C/q02/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2020/C/q02/solution.py`
- 批量运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：读取附件2的302家无信贷记录企业发票数据，使用附件1企业特征分布作为风险参照。
- 步骤 2：由经营规模、毛利、作废率、负数率、客户集中度和增长率推断隐含信誉等级。
- 步骤 3：使用附件3利率-流失率曲线逐企业选择利率。
- 步骤 4：在1亿元预算内输出授信企业、额度、利率和期望收益。

## 实验结果与解释

### 产物文件
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2020/C/q02/credit_risk_scores.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2020/C/q02/loan_strategy.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2020/C/q02/experiment_table.csv

### 数据来源
- 类型：attachment
- 附件：/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/C/附件1：123家有信贷记录企业的相关数据.xlsx; /Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/C/附件2：302家无信贷记录企业的相关数据.xlsx; /Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/C/附件3：银行贷款年利率与客户流失率关系的统计数据.xlsx
- 读取规模：1099896 行 x 42 列
- 说明：本题专用算法读取附件1/2企业信息和进销项发票，聚合经营特征；读取附件3利率-客户流失率曲线，用于风险评分、利率选择和年度授信额度分配。

### result.json 核心结果

```json
{
  "method": "unlabeled_enterprise_credit_strategy",
  "enterprise_count": 302,
  "loan_strategy_summary": {
    "approved_count": 25,
    "rejected_count": 277,
    "total_credit_yuan": 25000000.0,
    "budget_yuan": 100000000.0,
    "mean_risk_approved": 0.272162,
    "expected_interest_income_yuan": 196244.81,
    "mean_loan_rate_approved": 0.05706
  },
  "top_approved_enterprises": [
    {
      "企业代号": "E127",
      "企业名称": "个体经营E127 ",
      "inferred_rating": "A",
      "approved": true,
      "credit_yuan": 1000000.0,
      "loan_rate": 0.0465,
      "customer_loss_rate": 0.135727,
      "risk_score": 0.156247,
      "shock_risk_delta": 0.0,
      "expected_yield": 0.02141,
      "expected_interest_income_yuan": 21409.51,
      "priority": 1.043562
    },
    {
      "企业代号": "E129",
      "企业名称": "个体经营E129 ",
      "inferred_rating": "A",
      "approved": true,
      "credit_yuan": 1000000.0,
      "loan_rate": 0.0465,
      "customer_loss_rate": 0.135727,
      "risk_score": 0.157653,
      "shock_risk_delta": 0.0,
      "expected_yield": 0.021241,
      "expected_interest_income_yuan": 21240.61,
      "priority": 1.011938
    },
    {
      "企业代号": "E125",
      "企业名称": "个体经营E125 ",
      "inferred_rating": "A",
      "approved": true,
      "credit_yuan": 1000000.0,
      "loan_rate": 0.0465,
      "customer_loss_rate": 0.135727,
      "risk_score": 0.177145,
      "shock_risk_delta": 0.0,
      "expected_yield": 0.018898,
      "expected_interest_income_yuan": 18897.81,
      "priority": 1.034722
    },
    {
      "企业代号": "E124",
      "企业名称": "个体经营E124 ",
      "inferred_rating": "B",
      "approved": true,
      "credit_yuan": 1000000.0,
      "loan_rate": 0.0585,
      "customer_loss_rate": 0.302883,
      "risk_score": 0.194708,
      "shock_risk_delta": 0.0,
      "expected_yield": 0.017264,
      "expected_interest_income_yuan": 17264.18,
      "priority": 0.990354
    },
    {
      "企业代号": "E126",
      "企业名称": "个体经营E126 ",
      "inferred_rating": "B",
      "approved": true,
      "credit_yuan": 1000000.0,
      "loan_rate": 0.0585,
      "customer_loss_rate": 0.302883,
      "risk_score": 0.228786,
      "shock_risk_delta": 0.0,
      "expected_yield": 0.013148,
      "expected_interest_income_yuan": 13148.28,
      "priority": 0.872539
    },
    {
      "企业代号": "E131",
      "企业名称": "个体经营E131 ",
      "inferred_rating": "B",
      "approved": true,
      "credit_yuan": 1000000.0,
      "loan_rate": 0.0585,
      "customer_loss_rate": 0.302883,
      "risk_score": 0.237079,
      "shock_risk_delta": 0.0,
      "expected_yield": 0.012147,
      "expected_interest_income_yuan": 12146.55,
      "priority": 0.819678
    },
    {
      "企业代号": "E147",
      "企业名称": "***装饰工程有限责任公司",
      "inferred_rating": "B",
      "approved": true,
      "credit_yuan": 1000000.0,
      "loan_rate": 0.0585,
      "customer_loss_rate": 0.302883,
      "risk_score": 0.253493,
      "shock_risk_delta": 0.0,
      "expected_yield": 0.010164,
      "expected_interest_income_yuan": 10164.06,
      "priority": 0.780982
    },
    {
      "企业代号": "E197",
      "企业名称": "***医疗设备有限公司",
      "inferred_rating": "B",
      "approved": true,
      "credit_yuan": 1000000.0,
      "loan_rate": 0.0585,
      "customer_loss_rate": 0.302883,
      "risk_score": 0.258806,
      "shock_risk_delta": 0.0,
      "expected_yield": 0.009522,
      "expected_interest_income_yuan": 9522.41,
      "priority": 0.763446
    },
    {
      "企业代号": "E141",
      "企业名称": "***食品有限公司",
      "inferred_rating": "B",
      "approved": true,
      "credit_yuan": 1000000.0,
      "loan_rate": 0.0585,
      "customer_loss_rate": 0.302883,
      "risk_score": 0.262635,
      "shock_risk_delta": 0.0,
      "expected_yield": 0.00906,
      "expected_interest_income_yuan": 9059.98,
      "priority": 0.74394
    },
    {
      "企业代号": "E134",
      "企业名称": "***工程咨询有限公司",
      "inferred_rating": "B",
      "approved": true,
      "credit_yuan": 1000000.0,
      "loan_rate": 0.0585,
      "customer_loss_rate": 0.302883,
      "risk_score": 0.265331,
      "shock_risk_delta": 0.0,
      "expected_yield": 0.008734,
      "expected_interest_income_yuan": 8734.3,
      "priority": 0.723098
    }
  ],
  "risk_score_quantiles": {
    "p10": 0.344981,
    "p50": 0.45526,
    "p90": 0.53578
  },
  "report": [
    "本问使用 `unlabeled_enterprise_credit_strategy`，逐企业从发票流水聚合经营规模、毛利代理、作废率、负数率、客户集中度和增长率。",
    "附件1的信誉评级/违约标签用于校准风险；附件2无标签企业则用附件1特征分布推断隐含评级。",
    "附件3的利率-客户流失率表用于选择风险调整期望收益最高的贷款年利率。",
    "授信策略表 `loan_strategy.csv` 给出是否放贷、额度、利率、流失率、风险分和期望收益；风险明细表 `credit_risk_scores.csv` 可直接用于论文表格和敏感性分析。",
    "通用基线没有删除，仍保留在 `cumcm/generic_baselines` 作为第一轮粗模型对照。"
  ]
}
```

### 结果解释
- 本问用 `unlabeled_enterprise_credit_strategy` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 专用实验报告

- 本问使用 `unlabeled_enterprise_credit_strategy`，逐企业从发票流水聚合经营规模、毛利代理、作废率、负数率、客户集中度和增长率。
- 附件1的信誉评级/违约标签用于校准风险；附件2无标签企业则用附件1特征分布推断隐含评级。
- 附件3的利率-客户流失率表用于选择风险调整期望收益最高的贷款年利率。
- 授信策略表 `loan_strategy.csv` 给出是否放贷、额度、利率、流失率、风险分和期望收益；风险明细表 `credit_risk_scores.csv` 可直接用于论文表格和敏感性分析。
- 通用基线没有删除，仍保留在 `cumcm/generic_baselines` 作为第一轮粗模型对照。

## 实验报告

本问的核心是：在问题1的基础上，对附件2中302家企业的信贷风险进行量化分析，并给出该银行在年度信贷总额为1亿元时对这些企业的信贷策略。

建模时先将题目要求拆成 1 个任务，再选择 `企业信用风险评分与授信组合优化`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
