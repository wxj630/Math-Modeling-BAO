# 2025-E 问题2 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2025年 CUMCM E题：AI 辅助智能体测
- 问题：问题2
- 原问：经过短时间的专业训练，跳远成绩便可有较大幅度的提升。附件3 是一些立定 跳远运动者在纠正前、教练纠正姿势后的跳远视频、位置信息和跳远成绩。附件4 是运动 者的个人体质报告，包括年龄、身高、体重和体脂率等。请根据相关资料，分析影响运动 者跳远成绩的主要因素。

## 通用模型选择

- 模型：图像文本与信号特征（CH10：图像、文本与信号数据）
- 教程参考：../My-Agent/intro-mathmodel/docs/CH10/第10章-图像、文本与信号数据.md
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

- 通用代码：cumcm/generic_baselines/solutions/2025/E/q02/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2025/E/q02/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2025/E/q02/result.json
- 实验报告：cumcm/generic_baselines/reports/2025/E/q02/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2025/E/q02/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件1/运动者1的跳远位置信息.xlsx
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
    8
  ],
  "top_amplitudes": [
    14515.818864,
    7258.286605,
    4839.276864,
    3629.897806,
    2904.371078,
    2420.770579,
    2075.413706,
    1816.459166
  ],
  "signal_energy": 2294975.4966887417
}
```
