# 2018-D 问题 二 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2018年 CUMCM D题：汽车总装线的配置
- 问题：问题 二
- 原问：装配要求 由于工艺流程的制约和质量控制的需要以及降低成本的考虑，总装和喷涂作业对经过生产线车辆型号有多种要求：

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

- 通用代码：cumcm/generic_baselines/solutions/2018/D/q02/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2018/D/q02/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2018/D/q02/result.json
- 实验报告：cumcm/generic_baselines/reports/2018/D/q02/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2018/D/q02/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：../../Documents/Playground/cumcm_unzipped/2018_lcGi8NeCd14458641de55ec1d705ea01714ff2dd/2018-D-Chinese/CUMCM-2018-Problem-D-Chinese-Appendix.xlsx
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "linear_programming",
  "success": true,
  "objective_max": 5.132766306798882,
  "decision": [
    0.0,
    0.0,
    0.0,
    2.891141
  ],
  "resource_slack": [
    11557.380772,
    0.0,
    1.028052
  ]
}
```
