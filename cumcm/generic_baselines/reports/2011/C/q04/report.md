# 2011-C 问题四 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2011年 CUMCM C题：企业退休职工养老金制度的改革
- 问题：问题四
- 原问：如果既要达到目标替代率，又要维持养老保险基金收支平衡，你认为可以采取什么措施。请给出你的理由。

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

- 通用代码：cumcm/generic_baselines/solutions/2011/C/q04/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2011/C/q04/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2011/C/q04/result.json
- 实验报告：cumcm/generic_baselines/reports/2011/C/q04/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2011/C/q04/experiment_table.csv

## 数据来源

- 类型：problem_statement
- 路径：cumcm/problems/2011/C.md
- 说明：未找到可直接读取的数值附件，本问改用题目原文中的参数/表格数字生成实验结果。

## 核心结果

```json
{
  "method": "quadratic_least_squares",
  "coefficients": [
    786.947347,
    -39.430483,
    0.019488
  ],
  "r2": 0.15318442229993257,
  "mean_abs_error": 679.5401627333029
}
```
