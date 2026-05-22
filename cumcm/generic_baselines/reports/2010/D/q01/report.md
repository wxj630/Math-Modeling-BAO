# 2010-D 问题 1 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2010年 CUMCM D题：对学生宿舍设计方案的评价
- 问题：问题 1
- 原问：附件是四种比较典型的学生宿舍的设计方案。请你们用数学建模的方法就它们的经济性、舒适性和安全性作出综合量化评价和比较

## 通用模型选择

- 模型：综合评价与权重决策（CH7：权重生成与评价模型）
- 教程参考：../My-Agent/intro-mathmodel/docs/CH7/第7章-权重生成与评价模型.md
- 通用方法：`std_weight_topsis`

## 变量、约束与公式

### 变量定义
- a_ij: 方案 i 在指标 j 上的标准化表现
- w_j: 指标权重
- D_i^+: 到理想解距离
- C_i: TOPSIS 贴近度

### 约束条件
- 各指标同向化后归一化
- sum_j w_j = 1, w_j >= 0

### 模型公式 / 目标函数
- `w_j = std(a_.j)/sum_j std(a_.j)`
- `C_i = D_i^-/(D_i^+ + D_i^-)`
- `rank = argsort(-C_i)`

## 运行与产物

- 通用代码：cumcm/generic_baselines/solutions/2010/D/q01/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2010/D/q01/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2010/D/q01/result.json
- 实验报告：cumcm/generic_baselines/reports/2010/D/q01/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2010/D/q01/experiment_table.csv

## 数据来源

- 类型：problem_statement
- 路径：cumcm/problems/2010/D.md
- 说明：未找到可直接读取的数值附件，本问改用题目原文中的参数/表格数字生成实验结果。

## 核心结果

```json
{
  "method": "std_weight_topsis",
  "weights": [
    0.245406,
    0.141754,
    0.193767,
    0.211041,
    0.208031
  ],
  "scores": [
    0.435249,
    0.297741,
    0.368314,
    0.578679,
    0.664767,
    0.396939,
    0.120209
  ],
  "best_option": 5
}
```
