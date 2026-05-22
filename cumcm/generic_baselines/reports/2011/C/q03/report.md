# 2011-C 问题三 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2011年 CUMCM C题：企业退休职工养老金制度的改革
- 问题：问题三
- 原问：假设该企业某职工自 2000年起从30岁开始缴养老保险，一直缴费到退休（55岁，60岁，65岁），并从退休后一直领取养老金，至75岁死亡。计算养老保险基金的缺口情况，并计算该职工领取养老金到多少岁时，其缴存的养老保险基金与其领取的养老金之间达到收支平衡。

## 通用模型选择

- 模型：数据拟合与回归分析（CH6：数据处理与拟合模型）
- 教程参考：../My-Agent/intro-mathmodel/docs/CH6/第六章-数据处理与拟合模型.md
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

- 通用代码：cumcm/generic_baselines/solutions/2011/C/q03/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2011/C/q03/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2011/C/q03/result.json
- 实验报告：cumcm/generic_baselines/reports/2011/C/q03/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2011/C/q03/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：../../Documents/Playground/cumcm_unzipped/2011_LOsf8a1w1cfbe73ef037f2f60e5c144c0f96a94f/C/cumcm2011C附件1_山东省职工平均工资.xls
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "quadratic_least_squares",
  "coefficients": [
    9376.206145,
    -828.18141,
    0.414973
  ],
  "r2": 0.7819480295250987,
  "mean_abs_error": 3300.9459768207125
}
```
