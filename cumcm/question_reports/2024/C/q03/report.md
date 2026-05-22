# 2024-C 问题 3 建模求解实验报告

## 题目原文与任务拆解

- 题目：2024年 CUMCM C题：农作物的种植策略
- 问题：问题 3
- 原问：在现实生活中，各种农作物之间可能存在一定的可替代性和互补性，预期销售量与销 售价格、种植成本之间也存在一定的相关性。请在问题 2 的基础上综合考虑相关因素，给出该乡村 2024~2030 年农作物的最优种植策略，通过模拟数据进行求解，并与问题 2 的结果作比较分析。 附件 1 乡村现有耕地和农作物的基本情况 附件 2 2023 年乡村农作物种植和相关统计数据 附件 3 须提交结果的模板文件（result1_1.xlsx，result1_2.xlsx，result2.xlsx）

### 本问需要完成什么
- 任务 1：请在问题 2 的基础上综合考虑相关因素，给出该乡村 2024~2030 年农作物的最优种植策略，通过模拟数据进行求解，并与问题 2 的结果作比较分析

## 适配模型

- 主模型：规划优化与资源配置（CH3：函数极值与规划模型）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md

### 候选模型与适配理由
- 规划优化与资源配置（CH3）：最优、成本、策略；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md
- 数据拟合与回归分析（CH6）：数据、分析；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH6/第六章-数据处理与拟合模型.md
- 综合评价与权重决策（CH7）：综合、比较；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH7/第7章-权重生成与评价模型.md

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
- `generate correlated scenarios for demand, yield, price, and cost shocks`
- `score=mean(profit)-lambda*std(profit)-gamma*crop_type_concentration`
- `compare q2 baseline plan and correlated robust plan by Monte Carlo mean/std/CVaR`

## Python 代码与运行方式

- 代码文件：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2024/C/q03/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2024/C/q03/solution.py`
- 批量运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：生成带相关性的模拟情景：同类作物需求/价格正相关，替代作物销售量负向扰动。
- 步骤 2：在问题 2 趋势基础上加入作物类型集中度惩罚和豆类互补增益。
- 步骤 3：得到相关性鲁棒种植策略，并用同一批模拟情景与问题 2 策略对比。
- 步骤 4：输出鲁棒策略、模拟收益分布和比较指标。

## 实验结果与解释

### 产物文件
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2024/C/q03/experiment_table.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2024/C/q03/correlated_robust_plan.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2024/C/q03/result2_correlated_robust.xlsx

### 数据来源
- 类型：attachment
- 附件：/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/C题/附件1.xlsx; /Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/C题/附件2.xlsx
- 读取规模：289 行 x 23 列
- 说明：本题专用算法使用附件1的地块/作物清单、附件2的2023种植情况和亩产成本价格，并按附件3模板导出 result*.xlsx。

### result.json 核心结果

```json
{
  "method": "correlated_monte_carlo_crop_strategy_selection",
  "years": "2024-2030",
  "scenario_count": 96,
  "selected_plan": "correlated_balanced",
  "baseline_q2_plan_eval": {
    "scenario_count": 96,
    "mean_profit_yuan": 71233445.78,
    "std_profit_yuan": 1199933.1,
    "p05_profit_yuan": 69408142.57,
    "p50_profit_yuan": 71268389.59,
    "p95_profit_yuan": 73290201.58
  },
  "correlated_robust_plan_eval": {
    "scenario_count": 96,
    "mean_profit_yuan": 71110653.44,
    "std_profit_yuan": 1148570.45,
    "p05_profit_yuan": 69495235.16,
    "p50_profit_yuan": 70985727.19,
    "p95_profit_yuan": 72950257.76
  },
  "mean_profit_improvement_yuan": -122792.34,
  "p05_profit_improvement_yuan": 87092.59,
  "candidate_evaluations": [
    {
      "plan": "q2_baseline",
      "scenario_count": 96,
      "mean_profit_yuan": 71233445.78,
      "std_profit_yuan": 1199933.1,
      "p05_profit_yuan": 69408142.57,
      "p50_profit_yuan": 71268389.59,
      "p95_profit_yuan": 73290201.58
    },
    {
      "plan": "low_risk_trend",
      "scenario_count": 96,
      "mean_profit_yuan": 70988842.12,
      "std_profit_yuan": 1366522.15,
      "p05_profit_yuan": 68862428.01,
      "p50_profit_yuan": 70805462.58,
      "p95_profit_yuan": 73195094.51
    },
    {
      "plan": "correlated_mild",
      "scenario_count": 96,
      "mean_profit_yuan": 70950063.48,
      "std_profit_yuan": 1354097.42,
      "p05_profit_yuan": 68762092.15,
      "p50_profit_yuan": 70959759.79,
      "p95_profit_yuan": 73015413.74
    },
    {
      "plan": "correlated_balanced",
      "scenario_count": 96,
      "mean_profit_yuan": 71110653.44,
      "std_profit_yuan": 1148570.45,
      "p05_profit_yuan": 69495235.16,
      "p50_profit_yuan": 70985727.19,
      "p95_profit_yuan": 72950257.76
    },
    {
      "plan": "correlated_conservative",
      "scenario_count": 96,
      "mean_profit_yuan": 70823115.76,
      "std_profit_yuan": 1262581.34,
      "p05_profit_yuan": 68712197.28,
      "p50_profit_yuan": 70691391.39,
      "p95_profit_yuan": 72804649.62
    }
  ],
  "robust_yearly_summary": [
    {
      "year": 2024,
      "profit_yuan": 7048947.0,
      "planted_area_mu": 1334.0,
      "production_jin": 1806355.0,
      "surplus_jin": 1073700.0,
      "legume_area_mu": 812.2
    },
    {
      "year": 2025,
      "profit_yuan": 10399520.9,
      "planted_area_mu": 1334.0,
      "production_jin": 2717820.0,
      "surplus_jin": 1849755.78,
      "legume_area_mu": 270.0
    },
    {
      "year": 2026,
      "profit_yuan": 9909187.63,
      "planted_area_mu": 1334.0,
      "production_jin": 2448905.0,
      "surplus_jin": 1535775.09,
      "legume_area_mu": 341.8
    },
    {
      "year": 2027,
      "profit_yuan": 7401442.73,
      "planted_area_mu": 1334.0,
      "production_jin": 1805750.0,
      "surplus_jin": 1024395.0,
      "legume_area_mu": 753.2
    },
    {
      "year": 2028,
      "profit_yuan": 11149444.25,
      "planted_area_mu": 1334.0,
      "production_jin": 2690070.0,
      "surplus_jin": 1843175.0,
      "legume_area_mu": 342.0
    },
    {
      "year": 2029,
      "profit_yuan": 10619795.14,
      "planted_area_mu": 1334.0,
      "production_jin": 2410005.0,
      "surplus_jin": 1514580.0,
      "legume_area_mu": 339.8
    },
    {
      "year": 2030,
      "profit_yuan": 7838442.62,
      "planted_area_mu": 1334.0,
      "production_jin": 1773525.0,
      "surplus_jin": 988320.0,
      "legume_area_mu": 685.2
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
      "crop_id": 10,
      "crop_name": "黍子",
      "crop_type": "粮食",
      "area_mu": 60.0,
      "yield_jin_per_mu": 500.0,
      "production_jin": 30000.0,
      "expected_sales_cap_jin": 12500.0,
      "normal_sales_jin": 12500.0,
      "surplus_jin": 17500.0,
      "price_yuan_per_jin": 7.5,
      "cost_yuan": 22680.0,
      "profit_yuan": 136695.0,
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
    "result2_correlated_robust.xlsx",
    "correlated_robust_plan.csv",
    "experiment_table.csv"
  ]
}
```

### 结果解释
- 本问用 `correlated_monte_carlo_crop_strategy_selection` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 实验报告

本问的核心是：在现实生活中，各种农作物之间可能存在一定的可替代性和互补性，预期销售量与销 售价格、种植成本之间也存在一定的相关性。请在问题 2 的基础上综合考虑相关因素，给出该乡村 2024~2030 年农作物的最优种植策略，通过模拟数据进行求解，并与问题 2 的结果作比较分析。 附件 1 乡村现有耕地和农作物的基本情况 附件 2 2023 年乡村农作物种植和相关统计数…

建模时先将题目要求拆成 1 个任务，再选择 `规划优化与资源配置`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
