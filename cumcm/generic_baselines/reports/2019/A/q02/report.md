# 2019-A 问题2 通用基线报告

> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。

## 题目与任务

- 题目：2019年 CUMCM A题：高压油管的压力控制
- 问题：问题2
- 原问：在实际工作过程中，高压油管A处的燃油来自高压油泵的柱塞腔出口，喷油由喷油嘴的针阀控制。高压油泵柱塞的压油过程如图3所示，凸轮驱动柱塞上下运动，凸轮边缘曲线与角度的关系见附件1。柱塞向上运动时压缩柱塞腔内的燃油，当柱塞腔内的压力大于高压油管内的压力时，柱塞腔与高压油管连接的单向阀开启，燃油进入高压油管内。柱塞腔内直径为5mm，柱塞运动到上止点位置时，柱塞腔残余容积为20mm3。柱塞运动到下止点时，低压燃油会充满柱塞腔（包括残余容积），低压燃油的压力为0.5 MPa。喷油器喷嘴结构如图4所示，针阀直径为2.5mm、密封座是半角为9°的圆锥，最下端喷孔的直径为1.4mm。针阀升程为0时，针阀关闭；针阀升程大于0时，针阀开启，燃油向喷孔流动，通过喷孔喷出。在一个喷油周期内针阀升程与时间的关系由附件2给出。在问题1中给出的喷油器工作次数、高压油管尺寸和初始压力下，确定凸轮的角速度，使得高压油管内的压力尽量稳定在100 MPa左右。

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

- 通用代码：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2019/A/q02/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/solutions/2019/A/q02/solution.py`
- 结果 JSON：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/results/2019/A/q02/result.json
- 实验报告：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/reports/2019/A/q02/report.md
- 实验产物：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines/artifacts/2019/A/q02/experiment_table.csv

## 数据来源

- 类型：attachment
- 路径：/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/A-2019中文/附件1-凸轮边缘曲线.xlsx
- 说明：本问优先使用官方附件中的数值表生成实验结果。

## 核心结果

```json
{
  "method": "least_squares_geometry_fit",
  "center": [
    -0.159329,
    0.207654
  ],
  "radius": 1.3573739790697021,
  "mean_squared_error": 0.22569977251038287,
  "success": true
}
```
