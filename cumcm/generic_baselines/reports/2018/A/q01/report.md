# 2018-A 问题 2 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2018年 CUMCM A题：高温作业专用服装设计
- 问题：问题 2
- 原问：当环境温度为65ºC、IV层的厚度为5.5 mm时，确定II层的最优厚度，确保工作60分钟时，假人皮肤外侧温度不超过47ºC，且超过44ºC的时间不超过5分钟。

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

- 通用代码：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2018/A/q01/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2018/A/q01/solution.py`
- 结果 JSON：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/results/2018/A/q01/result.json
- 实验报告：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/reports/2018/A/q01/report.md
- 实验产物：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/artifacts/2018/A/q01/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2018_lcGi8NeCd14458641de55ec1d705ea01714ff2dd/2018-A-Chinese/CUMCM-2018-Problem-A-Chinese-Appendix.xlsx
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "first_order_dynamic_simulation",
  "y0": 9.0,
  "steady_state": 91.5,
  "k": 0.005,
  "final_value": 36.19857903152821
}
```
