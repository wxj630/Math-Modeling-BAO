# 2023-E 问题2 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2023年 CUMCM E题：黄河水沙监测数据分析
- 问题：问题2
- 原问：分析近6 年该水文站水沙通量的突变性、季节性和周期性等特性，研究水沙通量 的变化规律。

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

- 通用代码：cumcm/generic_baselines/solutions/2023/E/q02/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2023/E/q02/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2023/E/q02/result.json
- 实验报告：cumcm/generic_baselines/reports/2023/E/q02/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2023/E/q02/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：../../Documents/Playground/cumcm_unzipped/2023_Y20WPner9fa62862794e6dc82731a5561ce1132f/E题/附件1.xlsx
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "first_order_dynamic_simulation",
  "y0": 0.0,
  "steady_state": 15.0,
  "k": 0.005,
  "final_value": 4.945191174825627
}
```
