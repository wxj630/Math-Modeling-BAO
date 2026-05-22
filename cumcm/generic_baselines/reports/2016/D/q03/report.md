# 2016-D 问题 3 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2016年 CUMCM D题：风电场运行状况分析及优化
- 问题：问题 3
- 原问：为安全生产需要，风机每年需进行两次停机维护，两次维护之间的连续工作时间不超过270天，每次维护需一组维修人员连续工作2天。同时风电场每天需有一组维修人员值班以应对突发情况。风电场现有4组维修人员可从事值班或维护工作，每组维修人员连续工作时间（值班或维护）不超过6天。请制定维修人员的排班方案与风机维护计划，使各组维修人员的工作任务相对均衡，且风电场具有较好的经济效益，试给出你的方法和结果。 附件1 平均风速和风电场日实际输出功率表。 附件2 风电场典型风机报表。 附件3 风电场风机型号及其参数。 附件4 风机生产企业提供的新型号风机主要参数。

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

- 通用代码：cumcm/generic_baselines/solutions/2016/D/q03/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2016/D/q03/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2016/D/q03/result.json
- 实验报告：cumcm/generic_baselines/reports/2016/D/q03/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2016/D/q03/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：../../Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016D-Chinese/CUMCM2016-D-Appendix-Chinese/附件1  平均风速和风电场日实际输出功率表/201501.xls
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "linear_programming",
  "success": true,
  "objective_max": 15.484762187661888,
  "decision": [
    0.0,
    0.0,
    0.0,
    2.426458
  ],
  "resource_slack": [
    4546.103469,
    0.0,
    0.528795
  ]
}
```
