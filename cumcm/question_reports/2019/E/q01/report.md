# 2019-E 问题 1 建模求解实验报告

## 题目原文与任务拆解

- 题目：2019年 CUMCM E题：薄利多销”分析
- 问题：问题 1
- 原问：计算该商场从2016年11月30日到2019年1月2日每天的营业额和利润率（注意：由于未知原因，数据中非打折商品的成本价缺失。一般情况下，零售商的利润率在20%-40%之间)

### 本问需要完成什么
- 任务 1：计算该商场从2016年11月30日到2019年1月2日每天的营业额和利润率（注意：由于未知原因，数据中非打折商品的成本价缺失

## 适配模型

- 主模型：薄利多销销售流水与折扣弹性分析模型（CH6：数据处理与拟合模型）
- 教程参考：../My-Agent/intro-mathmodel/docs/CH6/第六章-数据处理与拟合模型.md

### 候选模型与适配理由
- 规划优化与资源配置（CH3）：成本、利润；参考 ../My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md
- 时间序列预测（CH8）：每天；参考 ../My-Agent/intro-mathmodel/docs/CH8/第8章-时间序列.md
- 数据拟合与回归分析（CH6）：数据；参考 ../My-Agent/intro-mathmodel/docs/CH6/第六章-数据处理与拟合模型.md

## 变量、约束与公式

### 建模假设
- 附件1和附件2均为销售流水，合并后仅保留已完成订单、正销售数量和正销售价记录。
- 营业额按 sku_cnt * sku_sale_prc 计算，标价额按 sku_cnt * sku_prc 计算。
- sku_cost_prc为单品直降商品成本价；缺失成本先按一级品类有成本样本的中位利润率填补，再回退到题面20%-40%区间中值30%。
- 每日折扣力度用销售额加权折扣率、折扣覆盖率和促销活动覆盖率共同刻画。
- 关系分析在日级样本上控制星期和月份，并在一级品类层面复核折扣-销售额/利润率关系变化。
- 通用基线保留在 `cumcm/generic_baselines`，当前结果是从LP/TOPSIS粗模型推进到真实销售流水分析的专用版本。

### 变量定义
- R_d: 第d天营业额
- M_d: 第d天利润率
- D_d: 第d天折扣力度
- C_i: 第i个SKU的估计成本
- beta: 折扣力度对销售额/利润率的回归系数

### 约束条件
- 完成订单 is_finished=1；退货或负数量记录不计入正向销售分析。
- 估计利润率限制在题面给出的20%-40%经验区间内。
- 折扣率 clip(1-sale_price/list_price, 0, 1)。

### 模型公式 / 目标函数
- `revenue = sku_cnt * sku_sale_prc。`
- `profit = revenue - sku_cnt * estimated_cost。`
- `discount_intensity = 0.7*revenue_weighted_discount + 0.2*discount_revenue_share + 0.1*promotion_revenue_share。`
- `log(revenue_d)=alpha+beta*D_d+weekday+month+epsilon。`
- `profit_rate_d=alpha+gamma*D_d+weekday+month+epsilon。`

## Python 代码与运行方式

- 代码文件：cumcm/question_solutions/2019/E/q01/solution.py
- 单问运行：`.venv/bin/python cumcm/question_solutions/2019/E/q01/solution.py`
- 批量运行：`.venv/bin/python cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：读取附件1/2销售流水、附件3促销信息、附件4商品品类表。
- 步骤 2：清洗日期、价格、数量并合并品类；用有成本样本估计品类利润率并填补非打折商品成本。
- 步骤 3：输出每日营业额、利润、利润率、订单数和销量。
- 步骤 4：构建每日折扣力度指标并输出日级折扣表。
- 步骤 5：对日级和品类-日级样本分别回归，分析折扣力度与销售额、利润率关系。

## 实验结果与解释

### 产物文件
- cumcm/question_artifacts/2019/E/q01/daily_revenue_profit.csv
- cumcm/question_artifacts/2019/E/q01/category_margin_imputation.csv
- cumcm/question_artifacts/2019/E/q01/experiment_table.csv

### 数据来源
- 类型：attachment
- 附件：../../Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/E-2019中文/data/附件1.csv; ../../Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/E-2019中文/data/附件2.csv; ../../Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/E-2019中文/data/附件3.csv; ../../Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/E-2019中文/data/附件4.csv; ../../Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/E-2019中文/data/附件5.xlsx
- 读取规模：1239845 行 x 55 列
- 说明：本题专用算法读取两份销售流水、促销信息和商品品类表，计算每日营业额/利润率、折扣力度及折扣-销售/利润关系。

### result.json 核心结果

```json
{
  "method": "discount_sales_daily_revenue_profit",
  "transaction_count": 1221855,
  "analyzed_transaction_count": 562685,
  "day_count": 747,
  "total_revenue": 9816226.56,
  "total_profit": 2944867.968,
  "mean_profit_rate": 0.3,
  "report": [
    "合并附件1/2销售流水后过滤完成订单、正销量和正销售价记录。",
    "有成本价的单品直降商品直接使用成本；缺失成本按一级品类中位利润率填补，并约束在20%-40%。",
    "输出每日营业额、利润、利润率和品类毛利率填补表。"
  ]
}
```

### 结果解释
- 本问用 `discount_sales_daily_revenue_profit` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 专用实验报告

- 合并附件1/2销售流水后过滤完成订单、正销量和正销售价记录。
- 有成本价的单品直降商品直接使用成本；缺失成本按一级品类中位利润率填补，并约束在20%-40%。
- 输出每日营业额、利润、利润率和品类毛利率填补表。

## 实验报告

本问的核心是：计算该商场从2016年11月30日到2019年1月2日每天的营业额和利润率（注意：由于未知原因，数据中非打折商品的成本价缺失。一般情况下，零售商的利润率在20%-40%之间)

建模时先将题目要求拆成 1 个任务，再选择 `薄利多销销售流水与折扣弹性分析模型`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
