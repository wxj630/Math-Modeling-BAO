# 2024-C 问题 1 建模求解实验报告

## 题目原文与任务拆解

- 题目：2024年 CUMCM C题：农作物的种植策略
- 问题：问题 1
- 原问：假定各种农作物未来的预期销售量、种植成本、亩产量和销售价格相对于 2023 年保持 稳定，每季种植的农作物在当季销售。如果某种作物每季的总产量超过相应的预期销售量，超过部 分不能正常销售。请针对以下两种情况，分别给出该乡村 2024~2030 年农作物的最优种植方案，将 结果分别填入 result1_1.xlsx 和 result1_2.xlsx 中（模板文件见附件 3）。 (1) 超过部分滞销，造成浪费； (2) 超过部分按 2023 年销售价格的 50%降价出售。

### 本问需要完成什么
- 任务 1：假定各种农作物未来的预期销售量、种植成本、亩产量和销售价格相对于 2023 年保持 稳定，每季种植的农作物在当季销售。如果某种作物每季的总产量超过相应的预期销售量，超过部 分不能正常销售。请针对以下两种情况，分别给出该乡村 2024~2030 年农作物的最优种植方案，将 结果分别填入 result1_1.xlsx 和 result1_2.xlsx 中（模板文件见附件 3）

## 适配模型

- 主模型：规划优化与资源配置（CH3：函数极值与规划模型）
- 教程参考：../My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md

### 候选模型与适配理由
- 规划优化与资源配置（CH3）：最优、成本、方案；参考 ../My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md
- 时间序列预测（CH8）：未来；参考 ../My-Agent/intro-mathmodel/docs/CH8/第8章-时间序列.md

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
- `profit=sum(normal_sales*price + surplus_sales*discount*price - planted_area*cost)`
- `case1: discount=0；case2: discount=0.5`
- `expected_sales_{c}=2023 年该作物估计产量，2024-2030 保持稳定`

## Python 代码与运行方式

- 代码文件：cumcm/question_solutions/2024/C/q01/solution.py
- 单问运行：`.venv/bin/python cumcm/question_solutions/2024/C/q01/solution.py`
- 批量运行：`.venv/bin/python cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：读取附件 1 的地块面积/类型和作物适宜地，读取附件 2 的 2023 种植与亩产成本价格。
- 步骤 2：根据地块类型生成每年可行的作物-季次候选模式。
- 步骤 3：以 2023 年产量估计每种作物的预期销售上限。
- 步骤 4：分别按滞销浪费和 50% 折价规则逐年构造收益最大的轮作方案。
- 步骤 5：输出 result1_1/result1_2 对应的 Excel、明细 CSV 和年度利润汇总。

## 实验结果与解释

### 产物文件
- cumcm/question_artifacts/2024/C/q01/experiment_table.csv
- cumcm/question_artifacts/2024/C/q01/result1_1_plan.csv
- cumcm/question_artifacts/2024/C/q01/result1_2_plan.csv
- cumcm/question_artifacts/2024/C/q01/result1_1.xlsx
- cumcm/question_artifacts/2024/C/q01/result1_2.xlsx

### 数据来源
- 类型：attachment
- 附件：../../Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/C题/附件1.xlsx; ../../Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/C题/附件2.xlsx
- 读取规模：289 行 x 23 列
- 说明：本题专用算法使用附件1的地块/作物清单、附件2的2023种植情况和亩产成本价格，并按附件3模板导出 result*.xlsx。

### result.json 核心结果

```json
{
  "method": "rotation_constrained_crop_strategy_greedy_search",
  "years": "2024-2030",
  "plots": 54,
  "crops": 41,
  "case_waste_total_profit_yuan": 36745225.25,
  "case_half_price_total_profit_yuan": 59918902.5,
  "case_waste_total_surplus_jin": 3402175.0,
  "case_half_price_total_surplus_jin": 10098050.0,
  "top_years_waste": [
    {
      "year": 2024,
      "profit_yuan": 4413495.75,
      "planted_area_mu": 1334.0,
      "production_jin": 1498295.0,
      "surplus_jin": 531170.0,
      "legume_area_mu": 812.2
    },
    {
      "year": 2025,
      "profit_yuan": 5520811.25,
      "planted_area_mu": 1334.0,
      "production_jin": 1707990.0,
      "surplus_jin": 510305.0,
      "legume_area_mu": 353.8
    },
    {
      "year": 2026,
      "profit_yuan": 5478363.25,
      "planted_area_mu": 1334.0,
      "production_jin": 1700725.0,
      "surplus_jin": 512670.0,
      "legume_area_mu": 372.2
    }
  ],
  "top_years_half_price": [
    {
      "year": 2024,
      "profit_yuan": 7007707.5,
      "planted_area_mu": 1334.0,
      "production_jin": 1840555.0,
      "surplus_jin": 1100950.0,
      "legume_area_mu": 812.2
    },
    {
      "year": 2025,
      "profit_yuan": 9997076.25,
      "planted_area_mu": 1334.0,
      "production_jin": 2801375.0,
      "surplus_jin": 1889675.0,
      "legume_area_mu": 260.0
    },
    {
      "year": 2026,
      "profit_yuan": 9326353.12,
      "planted_area_mu": 1334.0,
      "production_jin": 2512650.0,
      "surplus_jin": 1562445.0,
      "legume_area_mu": 365.8
    }
  ],
  "sample_plan_rows": [
    {
      "year": 2024,
      "season": "单季",
      "crop_id": 4,
      "crop_name": "绿豆",
      "crop_type": "粮食（豆类）",
      "area_mu": 86.0,
      "yield_jin_per_mu": 330.0,
      "production_jin": 28380.0,
      "expected_sales_cap_jin": 33040.0,
      "normal_sales_jin": 28380.0,
      "surplus_jin": 0.0,
      "price_yuan_per_jin": 7.0,
      "cost_yuan": 30100.0,
      "profit_yuan": 168560.0,
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
      "cost_yuan": 28000.0,
      "profit_yuan": 156800.0,
      "plot": "A1",
      "land_type": "平旱地"
    },
    {
      "year": 2024,
      "season": "单季",
      "crop_id": 7,
      "crop_name": "玉米",
      "crop_type": "粮食",
      "area_mu": 72.0,
      "yield_jin_per_mu": 1000.0,
      "production_jin": 72000.0,
      "expected_sales_cap_jin": 132750.0,
      "normal_sales_jin": 72000.0,
      "surplus_jin": 0.0,
      "price_yuan_per_jin": 3.0,
      "cost_yuan": 36000.0,
      "profit_yuan": 180000.0,
      "plot": "A4",
      "land_type": "平旱地"
    },
    {
      "year": 2024,
      "season": "单季",
      "crop_id": 6,
      "crop_name": "小麦",
      "crop_type": "粮食",
      "area_mu": 68.0,
      "yield_jin_per_mu": 800.0,
      "production_jin": 54400.0,
      "expected_sales_cap_jin": 170840.0,
      "normal_sales_jin": 54400.0,
      "surplus_jin": 0.0,
      "price_yuan_per_jin": 3.5,
      "cost_yuan": 30600.0,
      "profit_yuan": 159800.0,
      "plot": "A5",
      "land_type": "平旱地"
    },
    {
      "year": 2024,
      "season": "单季",
      "crop_id": 2,
      "crop_name": "黑豆",
      "crop_type": "粮食（豆类）",
      "area_mu": 60.0,
      "yield_jin_per_mu": 475.0,
      "production_jin": 28500.0,
      "expected_sales_cap_jin": 21850.0,
      "normal_sales_jin": 21850.0,
      "surplus_jin": 6650.0,
      "price_yuan_per_jin": 7.5,
      "cost_yuan": 24000.0,
      "profit_yuan": 139875.0,
      "plot": "B1",
      "land_type": "梯田"
    },
    {
      "year": 2024,
      "season": "单季",
      "crop_id": 9,
      "crop_name": "高粱",
      "crop_type": "粮食",
      "area_mu": 60.0,
      "yield_jin_per_mu": 600.0,
      "production_jin": 36000.0,
      "expected_sales_cap_jin": 30000.0,
      "normal_sales_jin": 30000.0,
      "surplus_jin": 6000.0,
      "price_yuan_per_jin": 6.0,
      "cost_yuan": 24000.0,
      "profit_yuan": 156000.0,
      "plot": "B11",
      "land_type": "梯田"
    },
    {
      "year": 2024,
      "season": "单季",
      "crop_id": 1,
      "crop_name": "黄豆",
      "crop_type": "粮食（豆类）",
      "area_mu": 55.0,
      "yield_jin_per_mu": 400.0,
      "production_jin": 22000.0,
      "expected_sales_cap_jin": 57000.0,
      "normal_sales_jin": 22000.0,
      "surplus_jin": 0.0,
      "price_yuan_per_jin": 3.25,
      "cost_yuan": 22000.0,
      "profit_yuan": 49500.0,
      "plot": "A2",
      "land_type": "平旱地"
    },
    {
      "year": 2024,
      "season": "单季",
      "crop_id": 1,
      "crop_name": "黄豆",
      "crop_type": "粮食（豆类）",
      "area_mu": 55.0,
      "yield_jin_per_mu": 400.0,
      "production_jin": 22000.0,
      "expected_sales_cap_jin": 57000.0,
      "normal_sales_jin": 22000.0,
      "surplus_jin": 0.0,
      "price_yuan_per_jin": 3.25,
      "cost_yuan": 22000.0,
      "profit_yuan": 49500.0,
      "plot": "A6",
      "land_type": "平旱地"
    },
    {
      "year": 2024,
      "season": "单季",
      "crop_id": 5,
      "crop_name": "爬豆",
      "crop_type": "粮食（豆类）",
      "area_mu": 55.0,
      "yield_jin_per_mu": 395.0,
      "production_jin": 21725.0,
      "expected_sales_cap_jin": 9875.0,
      "normal_sales_jin": 9875.0,
      "surplus_jin": 11850.0,
      "price_yuan_per_jin": 6.75,
      "cost_yuan": 19250.0,
      "profit_yuan": 47406.25,
      "plot": "B7",
      "land_type": "梯田"
    },
    {
      "year": 2024,
      "season": "单季",
      "crop_id": 1,
      "crop_name": "黄豆",
      "crop_type": "粮食（豆类）",
      "area_mu": 50.0,
      "yield_jin_per_mu": 380.0,
      "production_jin": 19000.0,
      "expected_sales_cap_jin": 57000.0,
      "normal_sales_jin": 13000.0,
      "surplus_jin": 6000.0,
      "price_yuan_per_jin": 3.25,
      "cost_yuan": 20000.0,
      "profit_yuan": 22250.0,
      "plot": "B9",
      "land_type": "梯田"
    }
  ],
  "deliverables": [
    "result1_1.xlsx",
    "result1_2.xlsx",
    "result1_1_plan.csv",
    "result1_2_plan.csv"
  ]
}
```

### 结果解释
- 本问用 `rotation_constrained_crop_strategy_greedy_search` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 实验报告

本问的核心是：假定各种农作物未来的预期销售量、种植成本、亩产量和销售价格相对于 2023 年保持 稳定，每季种植的农作物在当季销售。如果某种作物每季的总产量超过相应的预期销售量，超过部 分不能正常销售。请针对以下两种情况，分别给出该乡村 2024~2030 年农作物的最优种植方案，将 结果分别填入 result1_1.xlsx 和 result1_2.xlsx 中（模板…

建模时先将题目要求拆成 1 个任务，再选择 `规划优化与资源配置`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
