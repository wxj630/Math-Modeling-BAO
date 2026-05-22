# 2018-D 问题 2 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2018年 CUMCM D题：汽车总装线的配置
- 问题：问题 2
- 原问：根据（1）中的数学模型或算法，针对附件中的数据，给出你们的计算结果： （a）将9月20日的装配顺序按照下表格式填写在表中，并将此表放在论文的附录中。 9月20日的装配顺序 （b）按照上表的格式给出9月17日至9月23日每天的装配顺序，文件以“schedule.xlsx”命名，作为论文的支撑材料与论文同时提交。

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

- 通用代码：cumcm/generic_baselines/solutions/2018/D/q08/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2018/D/q08/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2018/D/q08/result.json
- 实验报告：cumcm/generic_baselines/reports/2018/D/q08/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2018/D/q08/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：../../Documents/Playground/cumcm_unzipped/2018_lcGi8NeCd14458641de55ec1d705ea01714ff2dd/2018-D-Chinese/CUMCM-2018-Problem-D-Chinese-Appendix.xlsx
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "quadratic_least_squares",
  "coefficients": [
    49.037512,
    -2.505397,
    8.1e-05
  ],
  "r2": 0.9999749966329079,
  "mean_abs_error": 34.687322582403986
}
```
