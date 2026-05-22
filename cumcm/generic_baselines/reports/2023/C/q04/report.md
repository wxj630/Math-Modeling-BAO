# 2023-C 问题4 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2023年 CUMCM C题：蔬菜类商品的自动定价与补货决策
- 问题：问题4
- 原问：为了更好地制定蔬菜商品的补货和定价决策，商超还需要采集哪些相关数据， 这些数据对解决上述问题有何帮助，请给出你们的意见和理由。 附件1 6 个蔬菜品类的商品信息 附件2 销售流水明细数据 附件3 蔬菜类商品的批发价格 附件4 蔬菜类商品的近期损耗率 注 (1) 附件1 中，部分单品名称包含的数字编号表示不同的供应来源。 (2) 附件4 中的损耗率反映了近期商品的损耗情况，通过近期盘点周期的数据计算得到。 2023 年高教社杯全国大学生数学建模竞赛题目 （请先阅读“全国大学生数学建模竞赛论文格式规范”）

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

- 通用代码：cumcm/generic_baselines/solutions/2023/C/q04/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2023/C/q04/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2023/C/q04/result.json
- 实验报告：cumcm/generic_baselines/reports/2023/C/q04/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2023/C/q04/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：../../Documents/Playground/cumcm_unzipped/2023_Y20WPner9fa62862794e6dc82731a5561ce1132f/C题/附件1.xlsx
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "linear_programming",
  "success": true,
  "objective_max": 5.7763291263739855,
  "decision": [
    1.474718,
    0.0,
    0.0,
    0.801792
  ],
  "resource_slack": [
    3.255199,
    0.0,
    0.0
  ]
}
```
