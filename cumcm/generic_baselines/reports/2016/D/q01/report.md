# 2016-D 问题 1 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2016年 CUMCM D题：风电场运行状况分析及优化
- 问题：问题 1
- 原问：附件1给出了该风电场一年内每隔15分钟的各风机安装处的平均风速和风电场日实际输出功率。试利用这些数据对该风电场的风能资源及其利用情况进行评估。

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

- 通用代码：cumcm/generic_baselines/solutions/2016/D/q01/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2016/D/q01/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2016/D/q01/result.json
- 实验报告：cumcm/generic_baselines/reports/2016/D/q01/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2016/D/q01/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：../../Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016D-Chinese/CUMCM2016-D-Appendix-Chinese/附件1  平均风速和风电场日实际输出功率表/201501.xls
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "quadratic_least_squares",
  "coefficients": [
    46.393142,
    -11.125929,
    0.000265
  ],
  "r2": 0.0036810413025210043,
  "mean_abs_error": 28.546858464562767
}
```
