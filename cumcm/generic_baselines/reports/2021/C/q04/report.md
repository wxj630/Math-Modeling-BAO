# 2021-C 问题 4 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2021年 CUMCM C题：生产企业原材料的订购与运输
- 问题：问题 4
- 原问：该企业通过技术改造已具备了提高产能的潜力。 根据现有原材料的供应商和转运 商的实际情况，确定该企业每周的产能可以提高多少，并给出未来 24 周的订购和转运 方案。 注：请将问题 2、问题 3 和问题 4 订购方案的数值结果填入附件 A，转运方案的数 值结果填入附件 B，并作为支撑材料（勿改变文件名）随论文一起提交。 附件 1 的数据说明

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

- 通用代码：cumcm/generic_baselines/solutions/2021/C/q04/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2021/C/q04/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2021/C/q04/result.json
- 实验报告：cumcm/generic_baselines/reports/2021/C/q04/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2021/C/q04/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：../../Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/C/附件1 近5年402家供应商的相关数据.xlsx
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "linear_programming",
  "success": true,
  "objective_max": 27.436065930478723,
  "decision": [
    0.0,
    2.094851,
    0.0,
    0.0
  ],
  "resource_slack": [
    450.196544,
    0.0,
    0.955585
  ]
}
```
