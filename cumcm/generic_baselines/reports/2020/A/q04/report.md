# 2020-A 问题4 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2020年 CUMCM A题：炉温曲线
- 问题：问题4
- 原问：在焊接过程中，除满足制程界限外，还希望以峰值温度为中心线的两侧超过217ºC的炉温曲线应尽量对称（参见图2）。请结合问题3，进一步给出最优炉温曲线，以及各温区设定的温度及传送带过炉速度，并给出相应的指标值。

## 通用模型选择

- 模型：微分方程与动态仿真（CH2：微分方程与动力系统）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH2/第2章-微分方程与动力系统.md
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

- 通用代码：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2020/A/q04/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2020/A/q04/solution.py`
- 结果 JSON：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/results/2020/A/q04/result.json
- 实验报告：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/reports/2020/A/q04/report.md
- 实验产物：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/artifacts/2020/A/q04/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/A/result.csv
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "first_order_dynamic_simulation",
  "y0": 76.68933491220503,
  "steady_state": 17.4459978573747,
  "k": 0.050886969017455694,
  "final_value": 18.461787617029096
}
```
