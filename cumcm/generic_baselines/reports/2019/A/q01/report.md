# 2019-A 问题1 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2019年 CUMCM A题：高压油管的压力控制
- 问题：问题1
- 原问：某型号高压油管的内腔长度为500mm，内直径为10mm，供油入口A处小孔的直径为1.4mm，通过单向阀开关控制供油时间的长短，单向阀每打开一次后就要关闭10ms。喷油器每秒工作10次，每次工作时喷油时间为2.4ms，喷油器工作时从喷油嘴B处向外喷油的速率如图2所示。高压油泵在入口A处提供的压力恒为160 MPa，高压油管内的初始压力为100 MPa。如果要将高压油管内的压力尽可能稳定在100 MPa左右，如何设置单向阀每次开启的时长？如果要将高压油管内的压力从100 MPa增加到150 MPa，且分别经过约2 s、5 s和10 s的调整过程后稳定在150 MPa，单向阀开启的时长应如何调整？

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

- 通用代码：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2019/A/q01/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2019/A/q01/solution.py`
- 结果 JSON：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/results/2019/A/q01/result.json
- 实验报告：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/reports/2019/A/q01/report.md
- 实验产物：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/artifacts/2019/A/q01/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/A-2019中文/附件1-凸轮边缘曲线.xlsx
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "first_order_dynamic_simulation",
  "y0": 0.0,
  "steady_state": 0.985,
  "k": 0.005,
  "final_value": 0.32473422048021644
}
```
