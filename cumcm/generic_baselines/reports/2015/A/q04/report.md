# 2015-A 问题 4 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2015年 CUMCM A题：太阳影子定位
- 问题：问题 4
- 原问：附件4为一根直杆在太阳下的影子变化的视频，并且已通过某种方式估计出直杆的高度为2米。请建立确定视频拍摄地点的数学模型，并应用你们的模型给出若干个可能的拍摄地点。 如果拍摄日期未知，你能否根据视频确定出拍摄地点与日期？

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

- 通用代码：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2015/A/q04/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2015/A/q04/solution.py`
- 结果 JSON：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/results/2015/A/q04/result.json
- 实验报告：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/reports/2015/A/q04/report.md
- 实验产物：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/artifacts/2015/A/q04/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2015_m00L7uGp5743fadb9289f545d4ed5a1b300622fa/A/附件1-3.xls
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "fft_feature_extraction",
  "top_frequency_bins": [
    1,
    4,
    7,
    10,
    13,
    16,
    19,
    22
  ],
  "top_amplitudes": [
    2015.303575,
    2014.619473,
    2014.522313,
    2014.4838,
    2014.463312,
    2014.450696,
    2014.442216,
    2014.436175
  ],
  "signal_energy": 3994468.473011159
}
```
