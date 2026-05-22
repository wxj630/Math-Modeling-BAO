# 2018-D 问题 4 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2018年 CUMCM D题：汽车总装线的配置
- 问题：问题 4
- 原问：对于颜色有如下要求： 1）蓝、黄、红三种颜色汽车的喷涂只能在C1线上进行，金色汽车的喷涂只能在C2线上进行，其他颜色汽车的喷涂可以在C1和C2任意一条喷涂线上进行。 2）除黑、白两种颜色外，在同一条喷涂线上，同种颜色的汽车应尽量连续喷涂作业。 3）喷涂线上不同颜色汽车之间的切换次数尽可能少，特别地，黑色汽车与其它颜色的汽车之间的切换代价很高。 4）不同颜色汽车在总装线上排列时的具体要求如下： （a）黑色汽车连续排列的数量在50-70辆之间，两批黑色汽车在总装线上需间隔至少20辆。 （b）白色汽车可以连续排列，也可以与颜色为蓝或棕的汽车间隔排列； （c）颜色为黄或红的汽车必须与颜色为银、灰、棕、金中的一种颜色的汽车间隔排列； （d）蓝色汽车必须与白色汽车间隔排列； （e）金色汽车要求与颜色为黄或红的汽车间隔排列；若无法满足要求，也可以与颜色为灰、棕、银中的一种颜色的汽车间隔排列； （f）颜色为灰或银的汽车可以连续排列，也可以与颜色为黄、红、金中的一种颜色的汽车间隔排列； （g）棕色汽车可以连续排列，也可以与颜色为黄、红、金、白中的一种颜色的汽车间隔排列。 （h）关于其他颜色的搭配，遵循“没有允许即为禁止”的原则。 由于该公司的生产线24小时不间断作业，以上总装线和喷涂线的各项要求对相邻班次（包括当日晚班与次日白班）的车辆同样适用。

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

- 通用代码：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2018/D/q06/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2018/D/q06/solution.py`
- 结果 JSON：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/results/2018/D/q06/result.json
- 实验报告：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/reports/2018/D/q06/report.md
- 实验产物：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/artifacts/2018/D/q06/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2018_lcGi8NeCd14458641de55ec1d705ea01714ff2dd/2018-D-Chinese/CUMCM-2018-Problem-D-Chinese-Appendix.xlsx
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
