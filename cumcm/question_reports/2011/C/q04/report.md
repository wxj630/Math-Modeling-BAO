# 2011-C 问题四 建模求解实验报告

## 题目原文与任务拆解

- 题目：2011年 CUMCM C题：企业退休职工养老金制度的改革
- 问题：问题四
- 原问：如果既要达到目标替代率，又要维持养老保险基金收支平衡，你认为可以采取什么措施。请给出你的理由。

### 本问需要完成什么
- 任务 1：请给出你的理由

## 适配模型

- 主模型：养老金工资预测与基金收支平衡模型（CH3：函数极值与规划模型）
- 教程参考：../My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md

### 候选模型与适配理由
- 规划优化与资源配置（CH3）：通用优化建模；参考 ../My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md
- 数据拟合与回归分析（CH6）：通用数据建模；参考 ../My-Agent/intro-mathmodel/docs/CH6/第六章-数据处理与拟合模型.md

## 变量、约束与公式

### 建模假设
- 附件1的山东省职工平均工资可代表社平工资变化趋势，2011-2035年工资增长率逐步从高速增长收敛到中等发达经济体水平。
- 个人账户缴费率为8%，企业统筹缴费率为20%，个人账户年利率按题面取3%。
- 基础养老金按退休前一年社平工资、本人平均缴费指数和缴费年限计算；个人账户养老金按账户余额除以计发月数估算。
- 基金缺口以统筹和个人账户缴存总额与退休后领取养老金累计额之差衡量，正值为缺口。
- 通用基线保留在 `cumcm/generic_baselines`，当前专用模型用于从粗趋势拟合推进到制度参数现金流分析。

### 变量定义
- W_t: 第t年山东省职工平均工资
- g_t: 年工资增长率
- I_a: 企业a年龄段职工缴费指数
- A: 个人账户累计余额
- R: 退休时养老金替代率
- G(age): 领取到指定年龄时基金缺口

### 约束条件
- 工资预测序列单调为正，增长率逐步收敛。
- 缴费起始年龄为30或40岁，退休年龄为55、60、65岁。
- 个人账户利息按3%年复利滚存。
- 目标替代率为58.5%，政策方案需同时降低基金缺口。

### 模型公式 / 目标函数
- `log(W_t)=alpha+beta*t+epsilon_t, with damped growth for future years`
- `basic_pension = retire_wage*(1+avg_index)/2*contribution_years*1%`
- `personal_pension = account_balance / actuarial_months`
- `replacement_rate = annual_pension / final_wage`
- `fund_gap = cumulative_pension_paid - cumulative_contribution`

## Python 代码与运行方式

- 代码文件：cumcm/question_solutions/2011/C/q04/solution.py
- 单问运行：`.venv/bin/python cumcm/question_solutions/2011/C/q04/solution.py`
- 批量运行：`.venv/bin/python cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：读取附件1，拟合对数工资趋势并计算历史增长率。
- 步骤 2：用衰减增长率预测2011-2035年社平工资。
- 步骤 3：读取附件2，按收入区间中点计算各年龄段平均工资和缴费指数。
- 步骤 4：枚举缴费起始年龄与退休年龄，计算基础养老金、个人账户养老金和替代率。
- 步骤 5：模拟缴费和领取现金流，计算75岁缺口、收支平衡年龄，并搜索延迟退休/提高缴费/降低目标替代率组合。

## 实验结果与解释

### 产物文件
- cumcm/question_artifacts/2011/C/q04/wage_forecast_2011_2035.csv
- cumcm/question_artifacts/2011/C/q04/wage_model_fit.csv
- cumcm/question_artifacts/2011/C/q04/age_wage_index.csv
- cumcm/question_artifacts/2011/C/q04/replacement_rate_scenarios.csv
- cumcm/question_artifacts/2011/C/q04/fund_gap_cashflow.csv
- cumcm/question_artifacts/2011/C/q04/break_even_summary.csv
- cumcm/question_artifacts/2011/C/q04/policy_scenarios.csv
- cumcm/question_artifacts/2011/C/q04/experiment_table.csv

### 数据来源
- 类型：attachment
- 附件：../../Documents/Playground/cumcm_unzipped/2011_LOsf8a1w1cfbe73ef037f2f60e5c144c0f96a94f/C/cumcm2011C.doc; ../../Documents/Playground/cumcm_unzipped/2011_LOsf8a1w1cfbe73ef037f2f60e5c144c0f96a94f/C/cumcm2011C附件1_山东省职工平均工资.xls; ../../Documents/Playground/cumcm_unzipped/2011_LOsf8a1w1cfbe73ef037f2f60e5c144c0f96a94f/C/cumcm2011C附件2_某企业分年龄职工数量及薪酬分布表.xls; ../../Documents/Playground/cumcm_unzipped/2011_LOsf8a1w1cfbe73ef037f2f60e5c144c0f96a94f/C/cumcm2011C附件3_养老金的计算办法.doc
- 读取规模：43 行 x 9 列
- 说明：本题专用算法读取山东省职工平均工资和企业年龄段薪酬分布，按养老金计算办法进行工资预测、替代率、基金缺口和政策方案分析。

### result.json 核心结果

```json
{
  "method": "pension_policy_balance_search",
  "historical_year_count": 33,
  "forecast_start_year": 2011,
  "forecast_end_year": 2035,
  "forecast_2011": 36377.44,
  "forecast_2035": 270521.42,
  "recent_growth_rate": 0.141196,
  "long_run_growth_rate": 0.055,
  "log_trend_r2": 0.995125,
  "enterprise_average_monthly_wage": 2579.732,
  "replacement_rate_scenarios": [
    {
      "start_age": 30,
      "retirement_age": 55,
      "contribution_years": 25,
      "avg_contribution_index": 1.139455,
      "basic_pension_annual": 33910.64,
      "personal_pension_annual": 10665.44,
      "annual_pension_at_retirement": 44576.08,
      "replacement_rate": 0.308519
    },
    {
      "start_age": 30,
      "retirement_age": 60,
      "contribution_years": 30,
      "avg_contribution_index": 1.142053,
      "basic_pension_annual": 58617.19,
      "personal_pension_annual": 21829.57,
      "annual_pension_at_retirement": 80446.76,
      "replacement_rate": 0.386117
    },
    {
      "start_age": 30,
      "retirement_age": 65,
      "contribution_years": 35,
      "avg_contribution_index": 1.143909,
      "basic_pension_annual": 95274.4,
      "personal_pension_annual": 47828.11,
      "annual_pension_at_retirement": 143102.51,
      "replacement_rate": 0.492634
    },
    {
      "start_age": 40,
      "retirement_age": 55,
      "contribution_years": 15,
      "avg_contribution_index": 1.216032,
      "basic_pension_annual": 8538.57,
      "personal_pension_annual": 3026.23,
      "annual_pension_at_retirement": 11564.8,
      "replacement_rate": 0.185117
    },
    {
      "start_age": 40,
      "retirement_age": 60,
      "contribution_years": 20,
      "avg_contribution_index": 1.200784,
      "basic_pension_annual": 18448.05,
      "personal_pension_annual": 7241.36,
      "annual_pension_at_retirement": 25689.41,
      "replacement_rate": 0.255221
    },
    {
      "start_age": 40,
      "retirement_age": 65,
      "contribution_years": 25,
      "avg_contribution_index": 1.191636,
      "basic_pension_annual": 34737.7,
      "personal_pension_annual": 17858.42,
      "annual_pension_at_retirement": 52596.12,
      "replacement_rate": 0.348087
    }
  ],
  "fund_gap_by_retirement_age": [
    {
      "retirement_age": 55,
      "fund_gap_to_age_75": 1258271.32,
      "break_even_age": 62
    },
    {
      "retirement_age": 60,
      "fund_gap_to_age_75": 1299011.96,
      "break_even_age": 67
    },
    {
      "retirement_age": 65,
      "fund_gap_to_age_75": 1041576.95,
      "break_even_age": 71
    }
  ],
  "best_policy_scenarios": [
    {
      "retirement_age": 67,
      "contribution_rate": 0.32,
      "target_replacement_rate": 0.52,
      "annual_pension_at_retirement": 169765.24,
      "fund_gap_to_age_75": 716226.46,
      "break_even_age": 73,
      "recommendation_score": 722726.46,
      "reason": "延迟退休、适度提高缴费率或分阶段降低替代率可共同改善基金缺口。"
    },
    {
      "retirement_age": 67,
      "contribution_rate": 0.3,
      "target_replacement_rate": 0.52,
      "annual_pension_at_retirement": 169765.24,
      "fund_gap_to_age_75": 790894.91,
      "break_even_age": 72,
      "recommendation_score": 797394.91,
      "reason": "延迟退休、适度提高缴费率或分阶段降低替代率可共同改善基金缺口。"
    },
    {
      "retirement_age": 67,
      "contribution_rate": 0.32,
      "target_replacement_rate": 0.55,
      "annual_pension_at_retirement": 179559.39,
      "fund_gap_to_age_75": 826471.94,
      "break_even_age": 72,
      "recommendation_score": 829971.94,
      "reason": "延迟退休、适度提高缴费率或分阶段降低替代率可共同改善基金缺口。"
    },
    {
      "retirement_age": 67,
      "contribution_rate": 0.28,
      "target_replacement_rate": 0.52,
      "annual_pension_at_retirement": 169765.24,
      "fund_gap_to_age_75": 865563.36,
      "break_even_age": 72,
      "recommendation_score": 872063.36,
      "reason": "延迟退休、适度提高缴费率或分阶段降低替代率可共同改善基金缺口。"
    },
    {
      "retirement_age": 67,
      "contribution_rate": 0.3,
      "target_replacement_rate": 0.55,
      "annual_pension_at_retirement": 179559.39,
      "fund_gap_to_age_75": 901140.39,
      "break_even_age": 72,
      "recommendation_score": 904640.39,
      "reason": "延迟退休、适度提高缴费率或分阶段降低替代率可共同改善基金缺口。"
    }
  ],
  "report": [
    "本题读取附件1的1978-2010年山东职工平均工资，使用对数趋势和增长率收敛假设预测2011-2035年工资。",
    "附件2按收入区间中点计算各年龄段平均工资和缴费指数，并枚举缴费起始年龄与退休年龄计算替代率。",
    "基金缺口实验按缴费阶段28%总缴费、个人账户8%和3%年利率模拟，退休后按养老金增长率领取至75岁。",
    "政策搜索比较延迟退休、提高缴费率和调整目标替代率的组合，输出兼顾58.5%目标与基金平衡的方案。"
  ]
}
```

### 结果解释
- 本问用 `pension_policy_balance_search` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 专用实验报告

- 本题读取附件1的1978-2010年山东职工平均工资，使用对数趋势和增长率收敛假设预测2011-2035年工资。
- 附件2按收入区间中点计算各年龄段平均工资和缴费指数，并枚举缴费起始年龄与退休年龄计算替代率。
- 基金缺口实验按缴费阶段28%总缴费、个人账户8%和3%年利率模拟，退休后按养老金增长率领取至75岁。
- 政策搜索比较延迟退休、提高缴费率和调整目标替代率的组合，输出兼顾58.5%目标与基金平衡的方案。

## 实验报告

本问的核心是：如果既要达到目标替代率，又要维持养老保险基金收支平衡，你认为可以采取什么措施。请给出你的理由。

建模时先将题目要求拆成 1 个任务，再选择 `养老金工资预测与基金收支平衡模型`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
