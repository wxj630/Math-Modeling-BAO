# 2020-C 问题 3 建模求解实验报告

## 题目原文与任务拆解

- 题目：2020年 CUMCM C题：中小微企业的信贷决策
- 问题：问题 3
- 原问：企业的生产经营和经济效益可能会受到一些突发因素影响，而且突发因素往往对不同行业、不同类别的企业会有不同的影响。综合考虑附件2中各企业的信贷风险和可能的突发因素（例如：新冠病毒疫情）对各企业的影响，给出该银行在年度信贷总额为1亿元时的信贷调整策略。 附件1 123家有信贷记录企业的相关数据 附件2 302家无信贷记录企业的相关数据 附件3 银行贷款年利率与客户流失率关系的2019年统计数据 附件中数据说明：

### 本问需要完成什么
- 任务 1：综合考虑附件2中各企业的信贷风险和可能的突发因素（例如：新冠病毒疫情）对各企业的影响，给出该银行在年度信贷总额为1亿元时的信贷调整策略

## 适配模型

- 主模型：企业信用风险评分与授信组合优化（CH9：机器学习与统计模型）
- 教程参考：../My-Agent/intro-mathmodel/docs/CH9/第九章-机器学习与统计模型.md

### 候选模型与适配理由
- 机器学习与统计识别（CH9）：客户、风险；参考 ../My-Agent/intro-mathmodel/docs/CH9/第九章-机器学习与统计模型.md
- 时间序列预测（CH8）：年度；参考 ../My-Agent/intro-mathmodel/docs/CH8/第8章-时间序列.md
- 概率统计与抽样检验（CH9）：风险；参考 ../My-Agent/intro-mathmodel/docs/CH9/第九章-机器学习与统计模型.md

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

- 代码文件：cumcm/question_solutions/2020/C/q03/solution.py
- 单问运行：`.venv/bin/python cumcm/question_solutions/2020/C/q03/solution.py`
- 批量运行：`.venv/bin/python cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：先复用问题2的基础风险评分和授信策略。
- 步骤 2：加入突发因素压力：客户集中度越高、增长越弱，风险上调越明显。
- 步骤 3：重新计算利率、流失率、获批集合与授信额度。
- 步骤 4：比较冲击前后的获批数量、总授信额和期望利息收入。

## 实验结果与解释

### 产物文件
- cumcm/question_artifacts/2020/C/q03/credit_risk_scores.csv
- cumcm/question_artifacts/2020/C/q03/loan_strategy.csv
- cumcm/question_artifacts/2020/C/q03/experiment_table.csv

### 数据来源
- 类型：attachment
- 附件：../../Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/C/附件1：123家有信贷记录企业的相关数据.xlsx; ../../Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/C/附件2：302家无信贷记录企业的相关数据.xlsx; ../../Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/C/附件3：银行贷款年利率与客户流失率关系的统计数据.xlsx
- 读取规模：1099896 行 x 42 列
- 说明：本题专用算法读取附件1/2企业信息和进销项发票，聚合经营特征；读取附件3利率-客户流失率曲线，用于风险评分、利率选择和年度授信额度分配。

### result.json 核心结果

```json
{
  "method": "shock_adjusted_credit_strategy",
  "enterprise_count": 302,
  "loan_strategy_summary": {
    "approved_count": 14,
    "rejected_count": 288,
    "total_credit_yuan": 14000000.0,
    "budget_yuan": 100000000.0,
    "mean_risk_approved": 0.270379,
    "expected_interest_income_yuan": 113744.04,
    "mean_loan_rate_approved": 0.0585
  },
  "top_approved_enterprises": [
    {
      "企业代号": "E127",
      "企业名称": "个体经营E127 ",
      "inferred_rating": "B",
      "approved": true,
      "credit_yuan": 1000000.0,
      "loan_rate": 0.0585,
      "customer_loss_rate": 0.302883,
      "risk_score": 0.183219,
      "shock_risk_delta": 0.026971,
      "expected_yield": 0.018652,
      "expected_interest_income_yuan": 18651.92,
      "priority": 0.987586
    },
    {
      "企业代号": "E125",
      "企业名称": "个体经营E125 ",
      "inferred_rating": "B",
      "approved": true,
      "credit_yuan": 1000000.0,
      "loan_rate": 0.0585,
      "customer_loss_rate": 0.302883,
      "risk_score": 0.195876,
      "shock_risk_delta": 0.018731,
      "expected_yield": 0.017123,
      "expected_interest_income_yuan": 17123.17,
      "priority": 0.997169
    },
    {
      "企业代号": "E129",
      "企业名称": "个体经营E129 ",
      "inferred_rating": "B",
      "approved": true,
      "credit_yuan": 1000000.0,
      "loan_rate": 0.0585,
      "customer_loss_rate": 0.302883,
      "risk_score": 0.20199,
      "shock_risk_delta": 0.044337,
      "expected_yield": 0.016385,
      "expected_interest_income_yuan": 16384.75,
      "priority": 0.916041
    },
    {
      "企业代号": "E124",
      "企业名称": "个体经营E124 ",
      "inferred_rating": "B",
      "approved": true,
      "credit_yuan": 1000000.0,
      "loan_rate": 0.0585,
      "customer_loss_rate": 0.302883,
      "risk_score": 0.213823,
      "shock_risk_delta": 0.019114,
      "expected_yield": 0.014956,
      "expected_interest_income_yuan": 14955.52,
      "priority": 0.941979
    },
    {
      "企业代号": "E131",
      "企业名称": "个体经营E131 ",
      "inferred_rating": "B",
      "approved": true,
      "credit_yuan": 1000000.0,
      "loan_rate": 0.0585,
      "customer_loss_rate": 0.302883,
      "risk_score": 0.266747,
      "shock_risk_delta": 0.029667,
      "expected_yield": 0.008563,
      "expected_interest_income_yuan": 8563.3,
      "priority": 0.74999
    },
    {
      "企业代号": "E147",
      "企业名称": "***装饰工程有限责任公司",
      "inferred_rating": "B",
      "approved": true,
      "credit_yuan": 1000000.0,
      "loan_rate": 0.0585,
      "customer_loss_rate": 0.302883,
      "risk_score": 0.274061,
      "shock_risk_delta": 0.020568,
      "expected_yield": 0.00768,
      "expected_interest_income_yuan": 7679.82,
      "priority": 0.732676
    },
    {
      "企业代号": "E126",
      "企业名称": "个体经营E126 ",
      "inferred_rating": "B",
      "approved": true,
      "credit_yuan": 1000000.0,
      "loan_rate": 0.0585,
      "customer_loss_rate": 0.302883,
      "risk_score": 0.279041,
      "shock_risk_delta": 0.050255,
      "expected_yield": 0.007078,
      "expected_interest_income_yuan": 7078.41,
      "priority": 0.749795
    },
    {
      "企业代号": "E197",
      "企业名称": "***医疗设备有限公司",
      "inferred_rating": "B",
      "approved": true,
      "credit_yuan": 1000000.0,
      "loan_rate": 0.0585,
      "customer_loss_rate": 0.302883,
      "risk_score": 0.293061,
      "shock_risk_delta": 0.034255,
      "expected_yield": 0.005385,
      "expected_interest_income_yuan": 5385.03,
      "priority": 0.683525
    },
    {
      "企业代号": "E134",
      "企业名称": "***工程咨询有限公司",
      "inferred_rating": "B",
      "approved": true,
      "credit_yuan": 1000000.0,
      "loan_rate": 0.0585,
      "customer_loss_rate": 0.302883,
      "risk_score": 0.302586,
      "shock_risk_delta": 0.037255,
      "expected_yield": 0.004235,
      "expected_interest_income_yuan": 4234.55,
      "priority": 0.639096
    },
    {
      "企业代号": "E132",
      "企业名称": "个体经营E132 ",
      "inferred_rating": "B",
      "approved": true,
      "credit_yuan": 1000000.0,
      "loan_rate": 0.0585,
      "customer_loss_rate": 0.302883,
      "risk_score": 0.309228,
      "shock_risk_delta": 0.029171,
      "expected_yield": 0.003432,
      "expected_interest_income_yuan": 3432.32,
      "priority": 0.645755
    }
  ],
  "risk_score_quantiles": {
    "p10": 0.405144,
    "p50": 0.539063,
    "p90": 0.677634
  },
  "report": [
    "本问使用 `shock_adjusted_credit_strategy`，逐企业从发票流水聚合经营规模、毛利代理、作废率、负数率、客户集中度和增长率。",
    "附件1的信誉评级/违约标签用于校准风险；附件2无标签企业则用附件1特征分布推断隐含评级。",
    "附件3的利率-客户流失率表用于选择风险调整期望收益最高的贷款年利率。",
    "授信策略表 `loan_strategy.csv` 给出是否放贷、额度、利率、流失率、风险分和期望收益；风险明细表 `credit_risk_scores.csv` 可直接用于论文表格和敏感性分析。",
    "通用基线没有删除，仍保留在 `cumcm/generic_baselines` 作为第一轮粗模型对照。"
  ]
}
```

### 结果解释
- 本问用 `shock_adjusted_credit_strategy` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 专用实验报告

- 本问使用 `shock_adjusted_credit_strategy`，逐企业从发票流水聚合经营规模、毛利代理、作废率、负数率、客户集中度和增长率。
- 附件1的信誉评级/违约标签用于校准风险；附件2无标签企业则用附件1特征分布推断隐含评级。
- 附件3的利率-客户流失率表用于选择风险调整期望收益最高的贷款年利率。
- 授信策略表 `loan_strategy.csv` 给出是否放贷、额度、利率、流失率、风险分和期望收益；风险明细表 `credit_risk_scores.csv` 可直接用于论文表格和敏感性分析。
- 通用基线没有删除，仍保留在 `cumcm/generic_baselines` 作为第一轮粗模型对照。

## 实验报告

本问的核心是：企业的生产经营和经济效益可能会受到一些突发因素影响，而且突发因素往往对不同行业、不同类别的企业会有不同的影响。综合考虑附件2中各企业的信贷风险和可能的突发因素（例如：新冠病毒疫情）对各企业的影响，给出该银行在年度信贷总额为1亿元时的信贷调整策略。 附件1 123家有信贷记录企业的相关数据 附件2 302家无信贷记录企业的相关数据 附件3 银行贷款年利率与客…

建模时先将题目要求拆成 1 个任务，再选择 `企业信用风险评分与授信组合优化`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
