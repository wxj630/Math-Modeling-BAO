# 2021-B 问题 3 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2021年 CUMCM B题：乙醇偶合制备 C4 烯烃
- 问题：问题 3
- 原问：如何选择催化剂组合与温度，使得在相同实验条件下 C4 烯烃收率尽可能 高。若使温度低于 350 度，又如何选择催化剂组合与温度，使得 C4 烯烃收率尽可 能高。

## 通用模型选择

- 模型：微分方程与动态仿真（CH2：微分方程与动力系统）
- 教程参考：../My-Agent/intro-mathmodel/docs/CH2/第2章-微分方程与动力系统.md
- 通用方法：`first_order_dynamic_simulation`

## 变量、约束与公式

### 变量定义
- y(t): 系统状态
- k: 调节/衰减系数
- y_env: 环境或稳态值
- t: 时间

### 约束条件
- k > 0
- 初值 y(0)=y0
- 状态向稳态单调或振荡趋近

### 模型公式 / 目标函数
- `dy/dt = -k*(y-y_env)`
- `y(0)=y0`

## 运行与产物

- 通用代码：cumcm/generic_baselines/solutions/2021/B/q03/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2021/B/q03/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2021/B/q03/result.json
- 实验报告：cumcm/generic_baselines/reports/2021/B/q03/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2021/B/q03/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：../../Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/B/附件1.xlsx
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "first_order_dynamic_simulation",
  "y0": 4.0,
  "steady_state": 300.0,
  "k": 0.008695652173913044,
  "final_value": 152.36591898718711
}
```
