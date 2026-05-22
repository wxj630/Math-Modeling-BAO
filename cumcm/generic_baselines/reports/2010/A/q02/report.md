# 2010-A 问题 2 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2010年 CUMCM A题：储油罐的变位识别与罐容表标定
- 问题：问题 2
- 原问：对于图1所示的实际储油罐，试建立罐体变位后标定罐容表的数学模型，即罐内储油量与油位高度及变位参数（纵向倾斜角度α和横向偏转角度β ）之间的一般关系。请利用罐体变位后在进/出油过程中的实际检测数据（附件2），根据你们所建立的数学模型确定变位参数，并给出罐体变位后油位高度间隔为10cm的罐容表标定值。进一步利用附件2中的实际检测数据来分析检验你们模型的正确性与方法的可靠性。 附件1：小椭圆储油罐的实验数据 附件2：实际储油罐的检测数据 PAGE PAGE 1

## 通用模型选择

- 模型：数据拟合与回归分析（CH6：数据处理与拟合模型）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH6/第六章-数据处理与拟合模型.md
- 通用方法：`quadratic_least_squares`

## 变量、约束与公式

### 变量定义
- x: 题面影响因素或测量自变量
- y: 待解释/待标定指标
- beta: 回归参数
- epsilon: 随机误差

### 约束条件
- 样本点按题面数值范围或标准化区间构造
- 最小二乘残差平方和最小

### 模型公式 / 目标函数
- `min_beta sum_i (y_i - beta0 - beta1*x_i - beta2*x_i^2)^2`
- `R^2 = 1 - SSE/SST`

## 运行与产物

- 通用代码：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2010/A/q02/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2010/A/q02/solution.py`
- 结果 JSON：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/results/2010/A/q02/result.json
- 实验报告：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/reports/2010/A/q02/report.md
- 实验产物：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/artifacts/2010/A/q02/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2010_rd4LEPmmd1095c70a7fb9d0898a08495837d8c93/2010A/问题A附件1：实验采集数据表.xls
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "quadratic_least_squares",
  "coefficients": [
    1099.484684,
    10.322237,
    -0.022967
  ],
  "r2": 0.11164130346540502,
  "mean_abs_error": 798.1218840784884
}
```
