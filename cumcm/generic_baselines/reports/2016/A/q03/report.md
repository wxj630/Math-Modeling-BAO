# 2016-A 问题3 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2016年 CUMCM A题：系泊系统的设计
- 问题：问题3
- 原问：由于潮汐等因素的影响，布放海域的实测水深介于16m~20m之间。布放点的海水速度最大可达到1.5m/s、风速最大可达到36m/s。请给出考虑风力、水流力和水深情况下的系泊系统设计，分析不同情况下钢桶、钢管的倾斜角度、锚链形状、浮标的吃水深度和游动区域。 说明 近海风荷载可通过近似公式F=0.625×Sv2(N) QUOTE \* MERGEFORMAT 计算，其中S为物体在风向法平面的投影面积(m2)，v为风速(m/s）。近海水流力可通过近似公式F=374×Sv2(N)计算，其中S为物体在水流速度法平面的投影面积(m2)，v为水流速度(m/s）。 附表 锚链型号和参数表 型号 长度(mm) 单位长度的质量(kg/m) I 78 3.2 II 105 7 III 120 12.5 IV 150 19.5 V 180 28.12 表注：长度是指每节链环的长度。

## 通用模型选择

- 模型：几何解析与运动学参数方程（CH1：解析方法与几何模型）
- 教程参考：../My-Agent/intro-mathmodel/docs/CH1/第1章-解析方法与几何模型.md
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

- 通用代码：cumcm/generic_baselines/solutions/2016/A/q03/solution.py
- 单问运行：`.venv/bin/python cumcm/generic_baselines/solutions/2016/A/q03/solution.py`
- 结果 JSON：cumcm/generic_baselines/results/2016/A/q03/result.json
- 实验报告：cumcm/generic_baselines/reports/2016/A/q03/report.md
- 实验产物：cumcm/generic_baselines/artifacts/2016/A/q03/experiment_table.csv

## 数据来源

- 类型：problem_statement
- 路径：cumcm/problems/2016/A.md
- 说明：未找到可直接读取的数值附件，本问改用题目原文中的参数/表格数字生成实验结果。

## 核心结果

```json
{
  "method": "least_squares_geometry_fit",
  "center": [
    2.129798,
    1.807868
  ],
  "radius": 3.127188339356696,
  "mean_squared_error": 0.025087927656259716,
  "success": true
}
```
