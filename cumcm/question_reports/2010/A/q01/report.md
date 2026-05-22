# 2010-A 问题 1 建模求解实验报告

## 题目原文与任务拆解

- 题目：2010年 CUMCM A题：储油罐的变位识别与罐容表标定
- 问题：问题 1
- 原问：为了掌握罐体变位后对罐容表的影响，利用如图4的小椭圆型储油罐（两端平头的椭圆柱体），分别对罐体无变位和倾斜角为α=4.10的纵向变位两种情况做了实验，实验数据如附件1所示。请建立数学模型研究罐体变位后对罐容表的影响，并给出罐体变位后油位高度间隔为1cm的罐容表标定值。

### 本问需要完成什么
- 任务 1：请建立数学模型研究罐体变位后对罐容表的影响，并给出罐体变位后油位高度间隔为1cm的罐容表标定值

## 适配模型

- 主模型：储油罐变位识别与罐容表标定（CH6：数据处理与拟合模型）
- 教程参考：../My-Agent/intro-mathmodel/docs/CH6/第六章-数据处理与拟合模型.md

### 候选模型与适配理由
- 几何解析与运动学参数方程（CH1）：圆、油位；参考 ../My-Agent/intro-mathmodel/docs/CH1/第1章-解析方法与几何模型.md
- 数据拟合与回归分析（CH6）：数据、标定；参考 ../My-Agent/intro-mathmodel/docs/CH6/第六章-数据处理与拟合模型.md

## 变量、约束与公式

### 建模假设
- 附件流量计记录为区间进/出油量，油高记录为该区间结束后的油位高度。
- 第1问小椭圆罐容量曲线在实验高度范围内单调，采用PCHIP保持单调形状；端点用空罐0L和无变位实验估计总容量约束。
- 第2问实际罐用圆截面等效长度几何模型做变位参数代理识别；纵倾alpha主要表现为探针位置相对罐体中心的等效高度偏移，横偏beta表现为垂向投影缩放。
- 通用基线保留在 `cumcm/generic_baselines`，当前结果是从二次拟合推进到附件流量守恒与几何标定的专用版本。

### 变量定义
- h: 油位计显示高度(mm)
- V(h): 罐内油量(L)
- alpha: 纵向倾斜角
- beta: 横向偏转角
- L_eff: 实际储油罐的等效几何长度

### 约束条件
- V(h)随h单调非降，且空罐容量为0。
- 进油过程 V_t=V_0+累计进油量，出油过程 V_t=V_0-累计出油量。
- 实际罐截面高度限制在[0, 2R]；alpha、beta在小角度范围内识别。

### 模型公式 / 目标函数
- `第1问: 用倾斜进油曲线估计出油实验初始油量，再用PCHIP插值得到1cm罐容表。`
- `圆截面面积 A(h)=R^2 arccos((R-h)/R)-(R-h)sqrt(2Rh-h^2)。`
- `第2问: V_hat(h;alpha,beta,L_eff)=A((h+Delta_alpha)cos beta)L_eff/10^6，最小化与流量守恒体积的均方误差。`

## Python 代码与运行方式

- 代码文件：cumcm/question_solutions/2010/A/q01/solution.py
- 单问运行：`.venv/bin/python cumcm/question_solutions/2010/A/q01/solution.py`
- 批量运行：`.venv/bin/python cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：读取附件1四张实验表，解析累加进/出油量和油位高度。
- 步骤 2：用已知初始油量把倾斜进油转成体积样本，并反推倾斜出油实验初始体积。
- 步骤 3：生成1cm小罐倾斜罐容表，并与无变位曲线比较倾斜影响。
- 步骤 4：读取附件2实际检测数据，用进/出油量递推流量守恒体积。
- 步骤 5：在圆截面等效几何模型中识别alpha、beta和等效长度，输出10cm罐容表及残差验证表。

## 实验结果与解释

### 产物文件
- cumcm/question_artifacts/2010/A/q01/small_tank_tilted_capacity_1cm.csv
- cumcm/question_artifacts/2010/A/q01/small_tank_tilted_fit_samples.csv
- cumcm/question_artifacts/2010/A/q01/small_tank_tilt_impact_by_height.csv
- cumcm/question_artifacts/2010/A/q01/experiment_table.csv

### 数据来源
- 类型：attachment
- 附件：../../Documents/Playground/cumcm_unzipped/2010_rd4LEPmmd1095c70a7fb9d0898a08495837d8c93/2010A/cumcm2010A.doc; ../../Documents/Playground/cumcm_unzipped/2010_rd4LEPmmd1095c70a7fb9d0898a08495837d8c93/2010A/问题A附件1：实验采集数据表.xls; ../../Documents/Playground/cumcm_unzipped/2010_rd4LEPmmd1095c70a7fb9d0898a08495837d8c93/2010A/问题A附件2：实际采集数据表.xls; ../../Documents/Playground/cumcm_reextract/2010/2010_rd4LEPmmd1095c70a7fb9d0898a08495837d8c93/2010A/cumcm2010A.doc; ../../Documents/Playground/cumcm_reextract/2010/2010_rd4LEPmmd1095c70a7fb9d0898a08495837d8c93/2010A/问题A附件1：实验采集数据表.xls; ../../Documents/Playground/cumcm_reextract/2010/2010_rd4LEPmmd1095c70a7fb9d0898a08495837d8c93/2010A/问题A附件2：实际采集数据表.xls
- 读取规模：864 行 x 14 列
- 说明：本题专用算法读取附件1小椭圆罐四组进/出油实验和附件2实际罐检测数据，完成倾斜罐容表、变位参数识别和流量守恒验证。

### result.json 核心结果

```json
{
  "method": "oil_tank_tilted_pchip_capacity_table",
  "tilt_angle_deg": 4.1,
  "tilted_sample_count": 104,
  "estimated_tilt_out_initial_liter": 3514.813522,
  "small_tank_capacity_liter": 3968.91,
  "capacity_table_interval_mm": 10,
  "fit_mae_liter": 0.0,
  "report": [
    "附件1倾斜进油用已知初始215L转为体积样本；倾斜出油初始油量由进油PCHIP曲线反推。",
    "PCHIP保持罐容表单调，并用0L与无变位实验估计总容量补足端点。",
    "输出1cm间隔罐容表和同高度下倾斜-无变位容量差。"
  ]
}
```

### 结果解释
- 本问用 `oil_tank_tilted_pchip_capacity_table` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 专用实验报告

- 附件1倾斜进油用已知初始215L转为体积样本；倾斜出油初始油量由进油PCHIP曲线反推。
- PCHIP保持罐容表单调，并用0L与无变位实验估计总容量补足端点。
- 输出1cm间隔罐容表和同高度下倾斜-无变位容量差。

## 实验报告

本问的核心是：为了掌握罐体变位后对罐容表的影响，利用如图4的小椭圆型储油罐（两端平头的椭圆柱体），分别对罐体无变位和倾斜角为α=4.10的纵向变位两种情况做了实验，实验数据如附件1所示。请建立数学模型研究罐体变位后对罐容表的影响，并给出罐体变位后油位高度间隔为1cm的罐容表标定值。

建模时先将题目要求拆成 1 个任务，再选择 `储油罐变位识别与罐容表标定`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
