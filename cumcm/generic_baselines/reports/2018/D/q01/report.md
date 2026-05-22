# 2018-D 问题 一 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2018年 CUMCM D题：汽车总装线的配置
- 问题：问题 一
- 原问：问题背景 某汽车公司生产多种型号的汽车，每种型号由品牌、配置、动力、驱动、颜色5种属性确定。品牌分为A1和A2两种，配置分为B1、B2、B3、B4、B5和B6六种，动力分为汽油和柴油2种，驱动分为两驱和四驱2种，颜色分为黑、白、蓝、黄、红、银、棕、灰、金9种。 公司每天可装配各种型号的汽车460辆，其中白班、晚班（每班12小时）各230辆。每天生产各种型号车辆的具体数量根据市场需求和销售情况确定。附件给出了该企业2018年9月17日至9月23日一周的生产计划。 公司的装配流程如图1所示。待装配车辆按一定顺序排成一列，首先匀速通过总装线依次进行总装作业，随后按序分为C1、C2线进行喷涂作业。

## 通用模型选择

- 模型：规划优化与资源配置（CH3：函数极值与规划模型）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md
- 通用方法：`linear_programming`

## 变量、约束与公式

### 变量定义
- x_i: 第 i 个方案/资源的选择强度
- c_i: 单位收益或效用
- A_ji: 第 j 类资源消耗
- b_j: 第 j 类资源上限

### 约束条件
- A x <= b
- x_i >= 0
- 资源容量按题面约束映射为 b_j

### 模型公式 / 目标函数
- `max sum_i c_i*x_i`
- `s.t. A*x <= b, x >= 0`

## 运行与产物

- 通用代码：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2018/D/q01/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2018/D/q01/solution.py`
- 结果 JSON：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/results/2018/D/q01/result.json
- 实验报告：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/reports/2018/D/q01/report.md
- 实验产物：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/artifacts/2018/D/q01/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2018_lcGi8NeCd14458641de55ec1d705ea01714ff2dd/2018-D-Chinese/CUMCM-2018-Problem-D-Chinese-Appendix.xlsx
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "linear_programming",
  "success": true,
  "objective_max": 5.132766306798882,
  "decision": [
    0.0,
    0.0,
    0.0,
    2.891141
  ],
  "resource_slack": [
    11557.380772,
    0.0,
    1.028052
  ]
}
```
