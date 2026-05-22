# 2024-C 问题 2 建模求解实验报告

## 题目原文与任务拆解

- 题目：2024年 CUMCM C题：农作物的种植策略
- 问题：问题 2
- 原问：根据经验，小麦和玉米未来的预期销售量有增长的趋势，平均年增长率介于5%~10% 之间， 其他农作物未来每年的预期销售量相对于 2023 年大约有±5%的变化。农作物的亩产量往往会 受气候等因素的影响， 每年会有±10%的变化。因受市场条件影响，农作物的种植成本平均每年增长 5%左右。粮食类作物的销售价格基本稳定；蔬菜类作物的销售价格有增长的趋势， 平均每年增长5% 左右。食用菌的销售价格稳中有降， 大约每年可下降1%~5%， 特别是羊肚菌的销售价格每年下降幅 度为5%。 请综合考虑各种农作物的预期销售量、亩产量、种植成本和销售价格的不确定性以及潜在的种 植风险，给出该乡村 2024~2030 年农作物的最优种植方案，将结果填入 result2.xlsx 中（模板文件见 附件 3）。

### 本问需要完成什么
- 任务 1：请综合考虑各种农作物的预期销售量、亩产量、种植成本和销售价格的不确定性以及潜在的种 植风险，给出该乡村 2024~2030 年农作物的最优种植方案，将结果填入 result2.xlsx 中（模板文件见 附件 3）

## 适配模型

- 主模型：规划优化与资源配置（CH3：函数极值与规划模型）
- 教程参考：../My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md

### 候选模型与适配理由
- 时间序列预测（CH8）：未来、趋势、增长；参考 ../My-Agent/intro-mathmodel/docs/CH8/第8章-时间序列.md
- 规划优化与资源配置（CH3）：最优、成本、方案；参考 ../My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md
- 概率统计与抽样检验（CH9）：风险、不确定；参考 ../My-Agent/intro-mathmodel/docs/CH9/第九章-机器学习与统计模型.md

## 变量、约束与公式

### 建模假设
- 以题面给出的数值、约束和输出格式为第一优先级构造模型。
- 若原始附件尚未能被当前环境直接读取，脚本优先抽取题目原文中的参数和表格数字，并在数据来源中显式记录。
- 所有结果由本问 solution.py 运行生成，result.json 与 experiment_table.csv 保持同步。

### 变量定义
- x_{y,l,s,c}: 第 y 年地块 l 在季次 s 种植作物 c 的面积
- Y_{l,c,s}: 附件 2 给出的地块类型-作物-季次亩产量
- C_{l,c,s}: 附件 2 给出的种植成本
- P_{c,s}: 销售单价区间中点
- D_{y,c,s}: 第 y 年作物 c 在季次 s 的预期销售量上限
- R_{y,c,s}: 超出销售量后的滞销或折价收益规则

### 约束条件
- 每个地块每个可种植季次只安排一种主作物，面积等于该地块面积。
- 平旱地、梯田、山坡地每年单季种粮食类作物；水浇地可单季水稻或两季蔬菜。
- 普通大棚第一季种蔬菜、第二季种食用菌；智慧大棚两季均种蔬菜。
- 同一地块相邻种植季次不重茬，同一作物不能连续出现在同一地块的相邻季次。
- 从 2023 年起，每个地块任意连续三年窗口内至少安排一次豆类作物。
- 按作物年度销售上限计算正常销售、滞销浪费或 50% 折价销售收益。

### 模型公式 / 目标函数
- `wheat/corn demand grows by 7.5% annually; other crop demand uses 2023 baseline in expectation`
- `cost_y=cost_2023*1.05^(y-2023)`
- `vegetable price_y=price_2023*1.05^(y-2023); fungi price declines; grain price is stable`
- `score=expected_profit - risk_aversion*risk_exposure`

## Python 代码与运行方式

- 代码文件：cumcm/question_solutions/2024/C/q02/solution.py
- 单问运行：`.venv/bin/python cumcm/question_solutions/2024/C/q02/solution.py`
- 批量运行：`.venv/bin/python cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：在问题 1 数据结构上叠加销售量、亩产、成本和价格的年度趋势。
- 步骤 2：用风险惩罚项近似 ±5% 销售量、±10% 亩产和价格波动带来的利润不确定性。
- 步骤 3：逐年选择风险调整收益最高且满足轮作/豆类窗口约束的地块模式。
- 步骤 4：输出 result2 风格 Excel、逐地块策略 CSV 和年度风险收益表。

## 实验结果与解释

### 产物文件
- cumcm/question_artifacts/2024/C/q02/experiment_table.csv
- cumcm/question_artifacts/2024/C/q02/result2_plan.csv
- cumcm/question_artifacts/2024/C/q02/result2.xlsx

### 数据来源
- 类型：attachment
- 附件：../../Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/C题/附件1.xlsx; ../../Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/C题/附件2.xlsx
- 读取规模：289 行 x 23 列
- 说明：本题专用算法使用附件1的地块/作物清单、附件2的2023种植情况和亩产成本价格，并按附件3模板导出 result*.xlsx。

### result.json 核心结果

```json
{
  "method": "risk_adjusted_crop_strategy_with_market_trends",
  "years": "2024-2030",
  "total_profit_yuan": 64524300.11,
  "total_surplus_jin": 9907354.53,
  "risk_aversion": 0.14,
  "trend_assumptions": {
    "wheat_corn_sales_growth": "7.5% annual midpoint",
    "other_sales": "2023 baseline in expectation",
    "yield_uncertainty": "±10% represented by risk penalty",
    "cost_growth": "5% annual",
    "vegetable_price_growth": "5% annual",
    "fungi_price_decline": "3% annual except morel 5%"
  },
  "yearly_summary": [
    {
      "year": 2024,
      "profit_yuan": 7076137.88,
      "planted_area_mu": 1334.0,
      "production_jin": 1834695.0,
      "surplus_jin": 1078833.75,
      "legume_area_mu": 812.2
    },
    {
      "year": 2025,
      "profit_yuan": 10452798.83,
      "planted_area_mu": 1334.0,
      "production_jin": 2791405.0,
      "surplus_jin": 1858575.78,
      "legume_area_mu": 223.0
    },
    {
      "year": 2026,
      "profit_yuan": 9901335.17,
      "planted_area_mu": 1334.0,
      "production_jin": 2475950.0,
      "surplus_jin": 1562995.0,
      "legume_area_mu": 371.8
    },
    {
      "year": 2027,
      "profit_yuan": 7387554.11,
      "planted_area_mu": 1334.0,
      "production_jin": 1814975.0,
      "surplus_jin": 1050170.0,
      "legume_area_mu": 770.2
    },
    {
      "year": 2028,
      "profit_yuan": 11236670.36,
      "planted_area_mu": 1334.0,
      "production_jin": 2758055.0,
      "surplus_jin": 1831585.0,
      "legume_area_mu": 283.0
    },
    {
      "year": 2029,
      "profit_yuan": 10652438.44,
      "planted_area_mu": 1334.0,
      "production_jin": 2458320.0,
      "surplus_jin": 1519775.0,
      "legume_area_mu": 349.8
    },
    {
      "year": 2030,
      "profit_yuan": 7817365.32,
      "planted_area_mu": 1334.0,
      "production_jin": 1787885.0,
      "surplus_jin": 1005420.0,
      "legume_area_mu": 734.2
    }
  ],
  "sample_plan_rows": [
    {
      "year": 2024,
      "season": "单季",
      "crop_id": 2,
      "crop_name": "黑豆",
      "crop_type": "粮食（豆类）",
      "area_mu": 86.0,
      "yield_jin_per_mu": 475.0,
      "production_jin": 40850.0,
      "expected_sales_cap_jin": 21850.0,
      "normal_sales_jin": 21850.0,
      "surplus_jin": 19000.0,
      "price_yuan_per_jin": 7.5,
      "cost_yuan": 36120.0,
      "profit_yuan": 199005.0,
      "plot": "B6",
      "land_type": "梯田"
    },
    {
      "year": 2024,
      "season": "单季",
      "crop_id": 3,
      "crop_name": "红豆",
      "crop_type": "粮食（豆类）",
      "area_mu": 80.0,
      "yield_jin_per_mu": 400.0,
      "production_jin": 32000.0,
      "expected_sales_cap_jin": 22400.0,
      "normal_sales_jin": 22400.0,
      "surplus_jin": 9600.0,
      "price_yuan_per_jin": 8.25,
      "cost_yuan": 29400.0,
      "profit_yuan": 195000.0,
      "plot": "A1",
      "land_type": "平旱地"
    },
    {
      "year": 2024,
      "season": "单季",
      "crop_id": 9,
      "crop_name": "高粱",
      "crop_type": "粮食",
      "area_mu": 72.0,
      "yield_jin_per_mu": 630.0,
      "production_jin": 45360.0,
      "expected_sales_cap_jin": 30000.0,
      "normal_sales_jin": 30000.0,
      "surplus_jin": 15360.0,
      "price_yuan_per_jin": 6.0,
      "cost_yuan": 30240.0,
      "profit_yuan": 195840.0,
      "plot": "A4",
      "land_type": "平旱地"
    },
    {
      "year": 2024,
      "season": "单季",
      "crop_id": 7,
      "crop_name": "玉米",
      "crop_type": "粮食",
      "area_mu": 68.0,
      "yield_jin_per_mu": 1000.0,
      "production_jin": 68000.0,
      "expected_sales_cap_jin": 142706.25,
      "normal_sales_jin": 68000.0,
      "surplus_jin": 0.0,
      "price_yuan_per_jin": 3.0,
      "cost_yuan": 35700.0,
      "profit_yuan": 168300.0,
      "plot": "A5",
      "land_type": "平旱地"
    },
    {
      "year": 2024,
      "season": "单季",
      "crop_id": 4,
      "crop_name": "绿豆",
      "crop_type": "粮食（豆类）",
      "area_mu": 60.0,
      "yield_jin_per_mu": 330.0,
      "production_jin": 19800.0,
      "expected_sales_cap_jin": 33040.0,
      "normal_sales_jin": 19800.0,
      "surplus_jin": 0.0,
      "price_yuan_per_jin": 7.0,
      "cost_yuan": 22050.0,
      "profit_yuan": 116550.0,
      "plot": "B1",
      "land_type": "梯田"
    },
    {
      "year": 2024,
      "season": "单季",
      "crop_id": 7,
      "crop_name": "玉米",
      "crop_type": "粮食",
      "area_mu": 60.0,
      "yield_jin_per_mu": 950.0,
      "production_jin": 57000.0,
      "expected_sales_cap_jin": 142706.25,
      "normal_sales_jin": 57000.0,
      "surplus_jin": 0.0,
      "price_yuan_per_jin": 3.0,
      "cost_yuan": 31500.0,
      "profit_yuan": 139500.0,
      "plot": "B11",
      "land_type": "梯田"
    },
    {
      "year": 2024,
      "season": "单季",
      "crop_id": 4,
      "crop_name": "绿豆",
      "crop_type": "粮食（豆类）",
      "area_mu": 55.0,
      "yield_jin_per_mu": 350.0,
      "production_jin": 19250.0,
      "expected_sales_cap_jin": 33040.0,
      "normal_sales_jin": 13240.0,
      "surplus_jin": 6010.0,
      "price_yuan_per_jin": 7.0,
      "cost_yuan": 20212.5,
      "profit_yuan": 93502.5,
      "plot": "A2",
      "land_type": "平旱地"
    },
    {
      "year": 2024,
      "season": "单季",
      "crop_id": 5,
      "crop_name": "爬豆",
      "crop_type": "粮食（豆类）",
      "area_mu": 55.0,
      "yield_jin_per_mu": 415.0,
      "production_jin": 22825.0,
      "expected_sales_cap_jin": 9875.0,
      "normal_sales_jin": 9875.0,
      "surplus_jin": 12950.0,
      "price_yuan_per_jin": 6.75,
      "cost_yuan": 20212.5,
      "profit_yuan": 90150.0,
      "plot": "A6",
      "land_type": "平旱地"
    },
    {
      "year": 2024,
      "season": "单季",
      "crop_id": 2,
      "crop_name": "黑豆",
      "crop_type": "粮食（豆类）",
      "area_mu": 55.0,
      "yield_jin_per_mu": 475.0,
      "production_jin": 26125.0,
      "expected_sales_cap_jin": 21850.0,
      "normal_sales_jin": 0.0,
      "surplus_jin": 26125.0,
      "price_yuan_per_jin": 7.5,
      "cost_yuan": 23100.0,
      "profit_yuan": 74868.75,
      "plot": "B7",
      "land_type": "梯田"
    },
    {
      "year": 2024,
      "season": "单季",
      "crop_id": 2,
      "crop_name": "黑豆",
      "crop_type": "粮食（豆类）",
      "area_mu": 50.0,
      "yield_jin_per_mu": 475.0,
      "production_jin": 23750.0,
      "expected_sales_cap_jin": 21850.0,
      "normal_sales_jin": 0.0,
      "surplus_jin": 23750.0,
      "price_yuan_per_jin": 7.5,
      "cost_yuan": 21000.0,
      "profit_yuan": 68062.5,
      "plot": "B9",
      "land_type": "梯田"
    }
  ],
  "deliverables": [
    "result2.xlsx",
    "result2_plan.csv"
  ]
}
```

### 结果解释
- 本问用 `risk_adjusted_crop_strategy_with_market_trends` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 实验报告

本问的核心是：根据经验，小麦和玉米未来的预期销售量有增长的趋势，平均年增长率介于5%~10% 之间， 其他农作物未来每年的预期销售量相对于 2023 年大约有±5%的变化。农作物的亩产量往往会 受气候等因素的影响， 每年会有±10%的变化。因受市场条件影响，农作物的种植成本平均每年增长 5%左右。粮食类作物的销售价格基本稳定；蔬菜类作物的销售价格有增长的趋势， 平均每年…

建模时先将题目要求拆成 1 个任务，再选择 `规划优化与资源配置`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
