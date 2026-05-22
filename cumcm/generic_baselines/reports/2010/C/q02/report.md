# 2010-C 问题 2 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2010年 CUMCM C题：输油管的布置
- 问题：问题 2
- 原问：设计院目前需对一更为复杂的情形进行具体的设计。两炼油厂的具体位置由附图所示，其中A厂位于郊区（图中的I区域），B厂位于城区（图中的II区域），两个区域的分界线用图中的虚线表示。图中各字母表示的距离（单位：千米）分别为a = 5，b = 8，c = 15，l = 20。 若所有管线的铺设费用均为每千米7.2万元。 铺设在城区的管线还需增加拆迁和工程补偿等附加费用，为对此项附加费用进行估计，聘请三家工程咨询公司（其中公司一具有甲级资质，公司二和公司三具有乙级资质）进行了估算。估算结果如下表所示： 工程咨询公司 公司一 公司二 公司三 附加费用（万元/千米） 21 24 20 请为设计院给出管线布置方案及相应的费用。

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

- 通用代码：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2010/C/q02/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2010/C/q02/solution.py`
- 结果 JSON：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/results/2010/C/q02/result.json
- 实验报告：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/reports/2010/C/q02/report.md
- 实验产物：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/artifacts/2010/C/q02/experiment_table.csv

## 数据来源

- 类型：problem_statement
- 路径：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2010/C.md
- 说明：未找到可直接读取的数值附件，本问改用题目原文中的参数/表格数字生成实验结果。

## 核心结果

```json
{
  "method": "linear_programming",
  "success": true,
  "objective_max": 17.506230872827256,
  "decision": [
    4.547903,
    0.0,
    0.0,
    0.0
  ],
  "resource_slack": [
    2.589321,
    0.0,
    0.283858
  ]
}
```
