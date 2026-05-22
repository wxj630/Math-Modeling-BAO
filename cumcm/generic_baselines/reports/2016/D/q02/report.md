# 2016-D 问题 2 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2016年 CUMCM D题：风电场运行状况分析及优化
- 问题：问题 2
- 原问：附件2给出了该风电场几个典型风机所在处的风速信息，其中4#、16#、24#风机属于一期工程，33#、49#、57#风机属于二期工程，它们的主要参数见附件3。风机生产企业还提供了部分新型号风机，它们的主要参数见附件4。试从风能资源与风机匹配角度判断新型号风机是否比现有风机更为适合。

## 通用模型选择

- 模型：几何解析与运动学参数方程（CH1：解析方法与几何模型）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH1/第1章-解析方法与几何模型.md
- 通用方法：`least_squares_geometry_fit`

## 变量、约束与公式

### 变量定义
- p_i=(x_i,y_i): 几何观测点
- c=(a,b): 中心或定位参数
- r: 半径/尺度参数
- e_i: 几何残差

### 约束条件
- r >= 0
- 观测点满足题面几何关系的近似约束

### 模型公式 / 目标函数
- `min_{a,b,r} mean_i (||p_i-c||_2-r)^2`
- `e_i=||p_i-c||_2-r`

## 运行与产物

- 通用代码：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2016/D/q02/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2016/D/q02/solution.py`
- 结果 JSON：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/results/2016/D/q02/result.json
- 实验报告：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/reports/2016/D/q02/report.md
- 实验产物：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/artifacts/2016/D/q02/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016D-Chinese/CUMCM2016-D-Appendix-Chinese/附件1  平均风速和风电场日实际输出功率表/201501.xls
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "least_squares_geometry_fit",
  "center": [
    2.291499,
    0.206145
  ],
  "radius": 2.6971297449493727,
  "mean_squared_error": 0.018940261363720644,
  "success": true
}
```
