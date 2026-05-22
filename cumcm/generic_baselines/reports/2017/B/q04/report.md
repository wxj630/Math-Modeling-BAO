# 2017-B 问题 4 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2017年 CUMCM B题：拍照赚钱”的任务定价
- 问题：问题 4
- 原问：实际情况下，多个任务可能因为位置比较集中，导致用户会争相选择，一种考虑是将这些任务联合在一起打包发布

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

- 通用代码：cumcm/generic_baselines/solutions/2017/B/q04/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2017/B/q04/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2017/B/q04/result.json
- 实验报告：cumcm/generic_baselines/reports/2017/B/q04/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2017/B/q04/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：../../Documents/Playground/cumcm_unzipped/2017_IqAO5Qqi8f23d8738a07a0604b8629ce9bb061ad/CUMCM2017Problems/B/附件一：已结束项目任务数据.xls
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "std_weight_topsis",
  "weights": [
    0.991484,
    0.008516
  ],
  "scores": [
    1.7e-05,
    0.025641,
    0.051282,
    0.076923,
    0.102564,
    0.128205,
    0.153846,
    0.179487,
    0.205128,
    0.230769,
    0.25641,
    0.282051,
    0.307692,
    0.333333,
    0.358974,
    0.384615,
    0.410256,
    0.435897,
    0.461538,
    0.487179,
    0.512821,
    0.538462,
    0.564103,
    0.589744,
    0.615385,
    0.641026,
    0.666667,
    0.692308,
    0.717949,
    0.74359,
    0.769231,
    0.794872,
    0.820513,
    0.846154,
    0.871795,
    0.897436,
    0.923077,
    0.948718,
    0.974359,
    0.999966
  ],
  "best_option": 40
}
```
