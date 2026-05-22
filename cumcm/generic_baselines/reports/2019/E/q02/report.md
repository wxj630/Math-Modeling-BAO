# 2019-E 问题 2 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2019年 CUMCM E题：薄利多销”分析
- 问题：问题 2
- 原问：建立适当的指标衡量商场每天的打折力度，并计算该商场从2016年11月30日到2019年1月2日每天的打折力度

## 通用模型选择

- 模型：综合评价与权重决策（CH7：权重生成与评价模型）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH7/第7章-权重生成与评价模型.md
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

- 通用代码：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2019/E/q02/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2019/E/q02/solution.py`
- 结果 JSON：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/results/2019/E/q02/result.json
- 实验报告：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/reports/2019/E/q02/report.md
- 实验产物：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/artifacts/2019/E/q02/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/E-2019中文/data/附件1.csv
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "std_weight_topsis",
  "weights": [
    0.001177,
    0.998823
  ],
  "scores": [
    1e-06,
    0.999337,
    0.999337,
    0.999337,
    0.999393,
    0.999701,
    0.999701,
    0.999701,
    0.999701,
    0.999701,
    0.999701,
    0.999701,
    0.999707,
    0.999707,
    0.999707,
    0.999707,
    0.999707,
    0.999707,
    0.999707,
    0.999707,
    0.999707,
    0.999707,
    0.999707,
    0.999707,
    0.999707,
    0.999707,
    0.999819,
    0.999819,
    0.999845,
    0.999845,
    0.999845,
    0.999845,
    0.99987,
    0.99987,
    0.99987,
    0.99987,
    0.999872,
    0.999989,
    0.999989,
    0.999999
  ],
  "best_option": 40
}
```
