# 2021-B 问题 4 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2021年 CUMCM B题：乙醇偶合制备 C4 烯烃
- 问题：问题 4
- 原问：如果允许再增加 5 次实验，应如何设计，并给出详细理由。 附录：名词解释与附件说明 温度：反应温度。 选择性：某一个产物在所有产物中的占比。 时间：催化剂在乙醇氛围下的反应时间，单位分钟（min）。 Co 负载量： Co 与 SiO2 的重量之比。例如，“Co 负载量为 1wt%”表示 Co 与 SiO2 的重量之比为 1:100，记作“1wt%Co/SiO2”，依次类推。 HAP：一种催化剂载体，中文名称羟基磷灰石。 Co /SiO2 和 HAP 装料比：指 Co/SiO2 和 HAP 的质量比。 例如附件 1 中编号为 A14 的 催化剂组合 “33mg 1wt%Co/SiO2-67mg HAP -乙 醇浓度 1.68ml/min” 指 Co/SiO2 和 HAP 质量比为 33mg：67mg 且乙醇按每分钟 1.68 毫升加入，依次类推。 乙醇转化率：单位时间内乙醇的单程转化率，其值为 100 %  (乙醇进气量-乙 醇剩余量)/乙醇进气量。 C4 烯烃收率：其值为乙醇转化率  C4 烯烃的选择性。 附件 1：性能数据表。表中乙烯、C4 烯烃、乙醛、碳数为 4-12 脂肪醇等均为 反应的生成物；编号 A1~A14 的催化剂实验中使用装料方式 I，B1～B7 的催化剂实 验中使用装料方式 II。 附件 2：350 度时给定的某种催化剂组合的测试数据。

## 通用模型选择

- 模型：微分方程与动态仿真（CH2：微分方程与动力系统）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH2/第2章-微分方程与动力系统.md
- 通用方法：`first_order_dynamic_simulation`

## 变量、约束与公式

### 变量定义
- y(t): 系统状态
- k: 调节/衰减系数
- y_env: 环境或稳态值
- t: 时间

### 约束条件
- k > 0
- 初值 y(0)=y0
- 状态向稳态单调或振荡趋近

### 模型公式 / 目标函数
- `dy/dt = -k*(y-y_env)`
- `y(0)=y0`

## 运行与产物

- 通用代码：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2021/B/q04/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2021/B/q04/solution.py`
- 结果 JSON：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/results/2021/B/q04/result.json
- 实验报告：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/reports/2021/B/q04/report.md
- 实验产物：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/artifacts/2021/B/q04/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/B/附件1.xlsx
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "first_order_dynamic_simulation",
  "y0": 4.0,
  "steady_state": 300.0,
  "k": 0.008695652173913044,
  "final_value": 152.36591898718711
}
```
