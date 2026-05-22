# 2020-C 问题 4 建模求解实验报告

## 题目原文与任务拆解

- 题目：2020年 CUMCM C题：中小微企业的信贷决策
- 问题：问题 4
- 原问：作废发票：在为交易活动开具发票后，因故取消了该项交易，使发票作废。

### 本问需要完成什么
- 任务 1：作废发票：在为交易活动开具发票后，因故取消了该项交易，使发票作废

## 适配模型

- 主模型：企业信用风险评分与授信组合优化（CH9：机器学习与统计模型）
- 教程参考：../My-Agent/intro-mathmodel/docs/CH9/第九章-机器学习与统计模型.md

### 候选模型与适配理由
- 规划优化与资源配置（CH3）：通用优化建模；参考 ../My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md
- 数据拟合与回归分析（CH6）：通用数据建模；参考 ../My-Agent/intro-mathmodel/docs/CH6/第六章-数据处理与拟合模型.md

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

- 代码文件：cumcm/question_solutions/2020/C/q07/solution.py
- 单问运行：`.venv/bin/python cumcm/question_solutions/2020/C/q07/solution.py`
- 批量运行：`.venv/bin/python cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：将解析器拆出的附件说明段落作为数据字典条目处理，而不是误当作官方新增问。
- 步骤 2：读取三份附件并统计企业数、发票数、有效/作废/负数记录数和利率曲线行数。
- 步骤 3：说明该术语如何进入前三问的风险评分或授信优化模型。
- 步骤 4：输出附件数据字典审计表，保持逐条解析过程可追溯。

## 实验结果与解释

### 产物文件
- cumcm/question_artifacts/2020/C/q07/attachment_data_dictionary.csv
- cumcm/question_artifacts/2020/C/q07/experiment_table.csv

### 数据来源
- 类型：attachment
- 附件：../../Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/C/附件1：123家有信贷记录企业的相关数据.xlsx; ../../Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/C/附件2：302家无信贷记录企业的相关数据.xlsx; ../../Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/C/附件3：银行贷款年利率与客户流失率关系的统计数据.xlsx
- 读取规模：1099896 行 x 42 列
- 说明：本题专用算法读取附件1/2企业信息和进销项发票，聚合经营特征；读取附件3利率-客户流失率曲线，用于风险评分、利率选择和年度授信额度分配。

### result.json 核心结果

```json
{
  "method": "credit_attachment_data_dictionary_audit",
  "parsed_fragment_note": "本条来自题面附件数据说明，不是官方独立问题；保留该条是为了让题目原文解析过程可追溯。",
  "enterprise_count": 425,
  "attachment_audit_rows": [
    {
      "dataset": "附件1-企业信息",
      "rows": 123,
      "columns": 4,
      "column_names": "企业代号;企业名称;信誉评级;是否违约",
      "valid_invoice_count": 0,
      "void_invoice_count": 0,
      "negative_invoice_count": 0
    },
    {
      "dataset": "附件1-进项发票",
      "rows": 210947,
      "columns": 8,
      "column_names": "企业代号;发票号码;开票日期;销方单位代号;金额;税额;价税合计;发票状态",
      "valid_invoice_count": 203339,
      "void_invoice_count": 7608,
      "negative_invoice_count": 1881
    },
    {
      "dataset": "附件1-销项发票",
      "rows": 162484,
      "columns": 8,
      "column_names": "企业代号;发票号码;开票日期;购方单位代号;金额;税额;价税合计;发票状态",
      "valid_invoice_count": 151278,
      "void_invoice_count": 11206,
      "negative_invoice_count": 8556
    },
    {
      "dataset": "附件2-企业信息",
      "rows": 302,
      "columns": 2,
      "column_names": "企业代号;企业名称",
      "valid_invoice_count": 0,
      "void_invoice_count": 0,
      "negative_invoice_count": 0
    },
    {
      "dataset": "附件2-进项发票",
      "rows": 395175,
      "columns": 8,
      "column_names": "企业代号;发票号码;开票日期;销方单位代号;金额;税额;价税合计;发票状态",
      "valid_invoice_count": 377939,
      "void_invoice_count": 17236,
      "negative_invoice_count": 3630
    },
    {
      "dataset": "附件2-销项发票",
      "rows": 330835,
      "columns": 8,
      "column_names": "企业代号;发票号码;开票日期;购方单位代号;金额;税额;价税合计;发票状态",
      "valid_invoice_count": 303280,
      "void_invoice_count": 27555,
      "negative_invoice_count": 5697
    },
    {
      "dataset": "附件3-利率流失率",
      "rows": 30,
      "columns": 4,
      "column_names": "贷款年利率;客户流失率;Unnamed: 2;Unnamed: 3",
      "valid_invoice_count": 0,
      "void_invoice_count": 0,
      "negative_invoice_count": 0
    }
  ],
  "report": [
    "本条是附件术语或字段说明，当前输出将其整理为数据字典审计，而不是硬套一个无意义的优化题。",
    "前三个正式问题已经使用这些字段：有效/作废/负数发票进入风险分，信誉评级校准风险，客户流失率进入利率选择。",
    "这类过程稿保留在逐问目录中，通用基线也保留在 `cumcm/generic_baselines`，便于看到从粗糙解析到专业建模的进步轨迹。"
  ]
}
```

### 结果解释
- 本问用 `credit_attachment_data_dictionary_audit` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 专用实验报告

- 本条是附件术语或字段说明，当前输出将其整理为数据字典审计，而不是硬套一个无意义的优化题。
- 前三个正式问题已经使用这些字段：有效/作废/负数发票进入风险分，信誉评级校准风险，客户流失率进入利率选择。
- 这类过程稿保留在逐问目录中，通用基线也保留在 `cumcm/generic_baselines`，便于看到从粗糙解析到专业建模的进步轨迹。

## 实验报告

本问的核心是：作废发票：在为交易活动开具发票后，因故取消了该项交易，使发票作废。

建模时先将题目要求拆成 1 个任务，再选择 `企业信用风险评分与授信组合优化`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
