# 2024-C 问题 2 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2024年 CUMCM C题：农作物的种植策略
- 问题：问题 2
- 原问：根据经验，小麦和玉米未来的预期销售量有增长的趋势，平均年增长率介于5%~10% 之间， 其他农作物未来每年的预期销售量相对于 2023 年大约有±5%的变化。农作物的亩产量往往会 受气候等因素的影响， 每年会有±10%的变化。因受市场条件影响，农作物的种植成本平均每年增长 5%左右。粮食类作物的销售价格基本稳定；蔬菜类作物的销售价格有增长的趋势， 平均每年增长5% 左右。食用菌的销售价格稳中有降， 大约每年可下降1%~5%， 特别是羊肚菌的销售价格每年下降幅 度为5%。 请综合考虑各种农作物的预期销售量、亩产量、种植成本和销售价格的不确定性以及潜在的种 植风险，给出该乡村 2024~2030 年农作物的最优种植方案，将结果填入 result2.xlsx 中（模板文件见 附件 3）。

## 通用模型选择

- 模型：规划优化与资源配置（CH3：函数极值与规划模型）
- 教程参考：../My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md
- 通用方法：`linear_programming`

## 变量、约束与公式

### 变量定义
- x_i: 第 i 个方案/资源的选择强度
- c_i: 单位收益或效用
- A_ji: 第 j 类资源消耗
- b_j: 第 j 类资源上限

### 约束条件
- A x <= b
- x_i >= 0
- 资源容量按题面约束映射为 b_j

### 模型公式 / 目标函数
- `max sum_i c_i*x_i`
- `s.t. A*x <= b, x >= 0`

## 运行与产物

- 通用代码：cumcm/generic_baselines/solutions/2024/C/q02/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2024/C/q02/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2024/C/q02/result.json
- 实验报告：cumcm/generic_baselines/reports/2024/C/q02/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2024/C/q02/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：../../Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/C题/附件1.xlsx
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "linear_programming",
  "success": true,
  "objective_max": 23.963979880339547,
  "decision": [
    0.0,
    0.0,
    0.0,
    1.569817
  ],
  "resource_slack": [
    44.996458,
    0.0,
    1.037074
  ]
}
```
