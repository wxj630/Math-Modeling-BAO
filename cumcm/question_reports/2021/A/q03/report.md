# 2021-A 问题 3 建模求解实验报告

## 题目原文与任务拆解

- 题目：2021年 CUMCM A题：FAST”主动反射面的形状调节
- 问题：问题 3
- 原问：基于第2 问的反射面调节方案， 计算调节后馈源舱的接收比， 即馈源舱有效区域接收到 的反射信号与 300 米口径内反射面的反射信号之比，并与基准反射球面的接收比作比较。 附录：要求及相关参数

### 本问需要完成什么
- 任务 1：基于第2 问的反射面调节方案， 计算调节后馈源舱的接收比， 即馈源舱有效区域接收到 的反射信号与 300 米口径内反射面的反射信号之比，并与基准反射球面的接收比作比较

## 适配模型

- 主模型：FAST主动反射面几何调节与反射接收评估（CH1：解析方法与几何模型）
- 教程参考：../My-Agent/intro-mathmodel/docs/CH1/第1章-解析方法与几何模型.md

### 候选模型与适配理由
- 图像文本与信号特征（CH10）：信号；参考 ../My-Agent/intro-mathmodel/docs/CH10/第10章-图像、文本与信号数据.md
- 规划优化与资源配置（CH3）：方案；参考 ../My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md
- 数据拟合与回归分析（CH6）：参数；参考 ../My-Agent/intro-mathmodel/docs/CH6/第六章-数据处理与拟合模型.md

## 变量、约束与公式

### 建模假设
- 基准球面球心位于坐标原点，主索节点坐标以附件1为准。
- 工作态只调节300米口径内的主索节点，口径外节点保持基准态。
- 促动器沿基准球面径向伸缩，趋向球心方向为正，伸缩量限制在[-0.6, 0.6]米。
- 下拉索长度固定，本实验用径向节点位移近似促动器顶端伸缩，并在结果中检查伸缩边界。
- 电磁波和反射波按直线传播，接收比用三角面板中心射线是否落入馈源舱1米直径有效圆盘估计。

### 变量定义
- u: 天体观测方向单位向量，由方位角alpha和仰角beta确定
- P: 馈源舱接收平面中心，位于焦面与SC直线交点
- d: 理想抛物面顶点沿观测轴的坐标
- f: 理想抛物面的焦距，满足P=(d+f)u
- rho_i: 主索节点i到观测轴的垂距
- delta_i: 促动器径向伸缩量
- x_i': 调节后主索节点坐标
- eta: 馈源舱接收比

### 约束条件
- rho_i <= 150 的节点进入300米工作口径。
- -0.6 <= delta_i <= 0.6。
- x_i' = x_i - delta_i * x_i/||x_i||。
- 相邻节点边长变化率以附件3三角面板边为近似检查，最大变化率应尽量小。
- 接收命中条件为反射射线与馈源接收平面的交点到P的距离不超过0.5米。

### 模型公式 / 目标函数
- `u=(cos(beta)cos(alpha), cos(beta)sin(alpha), sin(beta))`
- `paraboloid: t = d + rho^2/(4f), where t=x·u and f=P_axis-d`
- `delta_i = clip((t_paraboloid-t_i)/(-r_i·u), -0.6, 0.6)`
- `min RMS(t_i' - t_paraboloid) over candidate vertex coordinate d`
- `reflection: v_ref = v_in - 2(n·v_in)n`
- `eta = hit_panel_area / active_panel_area`

## Python 代码与运行方式

- 代码文件：cumcm/question_solutions/2021/A/q03/solution.py
- 单问运行：`.venv/bin/python cumcm/question_solutions/2021/A/q03/solution.py`
- 批量运行：`.venv/bin/python cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：复用第2问的调节方案，构造基准球面与调节后曲面的三角面板。
- 步骤 2：对每个主动三角面板计算法向量、入射方向和反射方向。
- 步骤 3：求反射射线与馈源舱接收平面的交点，统计落入0.5米半径有效圆盘的面板面积占比。
- 步骤 4：输出调节前后接收比、命中面板面积和改善倍数。

## 实验结果与解释

### 产物文件
- cumcm/question_artifacts/2021/A/q03/experiment_table.csv

### 数据来源
- 类型：attachment
- 附件：../../Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/A/附件1.csv; ../../Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/A/附件2.csv; ../../Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/A/附件3.csv; ../../Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/A/附件4.xlsx
- 读取规模：8752 行 x 14 列
- 说明：本题专用算法读取附件1主索节点坐标、附件2促动器上下端点、附件3三角反射面板和附件4结果模板，建立理想抛物面、径向伸缩调节和几何光线接收比实验。

### result.json 核心结果

```json
{
  "method": "fast_reflection_reception_ratio",
  "node_count": 2226,
  "panel_count": 4300,
  "active_node_count": 692,
  "baseline_reception_ratio": 0.0518562573123841,
  "adjusted_reception_ratio": 0.08701426203023177,
  "ratio_improvement": 1.6779896301820336,
  "baseline": {
    "active_panel_count": 1295,
    "total_panel_area_m2": 70995.37931563653,
    "hit_panel_area_m2": 3681.5546577819596,
    "reception_ratio": 0.0518562573123841,
    "hit_panel_count": 65,
    "median_hit_distance_m": 2.864902746463702
  },
  "adjusted": {
    "active_panel_count": 1295,
    "total_panel_area_m2": 70942.72925428975,
    "hit_panel_area_m2": 6173.029232472557,
    "reception_ratio": 0.08701426203023177,
    "hit_panel_count": 110,
    "median_hit_distance_m": 1.7555979212814106
  },
  "report": [
    "本问复用第2问调节方案，把每块主动三角面板视为局部平面镜。",
    "由入射方向、面板法向量和镜面反射公式得到反射射线，并检查其是否落入馈源舱0.5米半径有效圆盘。",
    "结果表比较基准球面和调节后抛物面的接收比，是一个可复现的几何光线追踪近似实验。"
  ]
}
```

### 结果解释
- 本问用 `fast_reflection_reception_ratio` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 专用实验报告

- 本问复用第2问调节方案，把每块主动三角面板视为局部平面镜。
- 由入射方向、面板法向量和镜面反射公式得到反射射线，并检查其是否落入馈源舱0.5米半径有效圆盘。
- 结果表比较基准球面和调节后抛物面的接收比，是一个可复现的几何光线追踪近似实验。

## 实验报告

本问的核心是：基于第2 问的反射面调节方案， 计算调节后馈源舱的接收比， 即馈源舱有效区域接收到 的反射信号与 300 米口径内反射面的反射信号之比，并与基准反射球面的接收比作比较。 附录：要求及相关参数

建模时先将题目要求拆成 1 个任务，再选择 `FAST主动反射面几何调节与反射接收评估`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
