# 2016-C 问题2 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2016年 CUMCM C题：电池剩余放电时间预测
- 问题：问题2
- 原问：试建立以20A到100A之间任一恒定电流强度放电时的放电曲线的数学模型，并用MRE评估模型的精度。用表格和图形给出电流强度为55A时的放电曲线。

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

- 通用代码：cumcm/generic_baselines/solutions/2016/C/q02/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2016/C/q02/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2016/C/q02/result.json
- 实验报告：cumcm/generic_baselines/reports/2016/C/q02/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2016/C/q02/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：../../Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016C-Chinese/CUMCM2016-C-Appendix-Chinese.xlsx
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "first_order_dynamic_simulation",
  "y0": 15.0,
  "steady_state": 195.0,
  "k": 0.005,
  "final_value": 74.34234964193044
}
```
