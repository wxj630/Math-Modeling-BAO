# 2021-A 问题 4 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2021年 CUMCM A题：FAST”主动反射面的形状调节
- 问题：问题 4
- 原问：电磁波信号及反射信号均视为直线传播。

## 通用模型选择

- 模型：图像文本与信号特征（CH10：图像、文本与信号数据）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH10/第10章-图像、文本与信号数据.md
- 通用方法：`fft_feature_extraction`

## 变量、约束与公式

### 变量定义
- s_t: 信号/图像/文本序列特征
- S_k: 傅里叶谱
- k*: 主要频率成分
- E: 信号能量

### 约束条件
- 输入序列先中心化
- 主要特征取谱幅值最大的频段

### 模型公式 / 目标函数
- `S_k=|FFT(s_t-mean(s))|`
- `E=sum_t s_t^2`
- `top_k=argsort(S_k)`

## 运行与产物

- 通用代码：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2021/A/q07/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2021/A/q07/solution.py`
- 结果 JSON：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/results/2021/A/q07/result.json
- 实验报告：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/reports/2021/A/q07/report.md
- 实验产物：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/artifacts/2021/A/q07/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/A/附件1.csv
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "fft_feature_extraction",
  "top_frequency_bins": [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    10
  ],
  "top_amplitudes": [
    8350.455023,
    4186.760844,
    2806.391971,
    2125.452757,
    1731.030143,
    1489.231162,
    1304.123165,
    1045.149258
  ],
  "signal_energy": 454968.1171875
}
```
