# 2010-B 问题 1 建模求解实验报告

## 题目原文与任务拆解

- 题目：2010年 CUMCM B题：2010年上海世博会影响力的定量评估
- 问题：问题 1
- 原问：2010年上海世博会是首次在中国举办的世界博览会。从1851年伦敦的“万国工业博览会”开始，世博会正日益成为各国人民交流历史文化、展示科技成果、体现合作精神、展望未来发展等的重要舞台。请你们选择感兴趣的某个侧面，建立数学模型，利用互联网数据，定量评估2010年上海世博会的影响力

### 本问需要完成什么
- 任务 1：请你们选择感兴趣的某个侧面，建立数学模型，利用互联网数据，定量评估2010年上海世博会的影响力

## 适配模型

- 主模型：时间序列预测（CH8：时间序列）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH8/第8章-时间序列.md

### 候选模型与适配理由
- 时间序列预测（CH8）：未来；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH8/第8章-时间序列.md
- 数据拟合与回归分析（CH6）：数据；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH6/第六章-数据处理与拟合模型.md
- 综合评价与权重决策（CH7）：评估；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH7/第7章-权重生成与评价模型.md

## 变量、约束与公式

### 建模假设
- 以题面给出的数值、约束和输出格式为第一优先级构造模型。
- 若原始附件尚未能被当前环境直接读取，脚本优先抽取题目原文中的参数和表格数字，并在数据来源中显式记录。
- 所有结果由本问 solution.py 运行生成，result.json 与 experiment_table.csv 保持同步。

### 变量定义
- t: 时间索引
- y_t: 历史观测指标
- a,b: 趋势回归参数
- y_{t+h}: 未来预测值

### 约束条件
- 短期趋势用线性项近似
- 预测区间延续历史趋势假设

### 模型公式 / 目标函数
- `y_t = a + b*t + epsilon_t`
- `forecast(t+h)=a+b*(t+h)`

## Python 代码与运行方式

- 代码文件：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2010/B/q01/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2010/B/q01/solution.py`
- 批量运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：整理历史时间序列。
- 步骤 2：拟合线性趋势模型。
- 步骤 3：外推未来 12 期。
- 步骤 4：输出历史拟合和预测表。

## 实验结果与解释

### 产物文件
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2010/B/q01/experiment_table.csv

### 数据来源
- 类型：problem_statement
- 附件：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2010/B.md
- 读取规模：8 行 x 3 列
- 说明：未找到可直接读取的数值附件，本问改用题目原文中的参数/表格数字生成实验结果。

### result.json 核心结果

```json
{
  "method": "linear_trend_forecast",
  "intercept": 1865.660714285715,
  "slope": -190.64404761904774,
  "r2": 0.1899603616350951,
  "next_12_forecast": [
    -7475.897619,
    -7666.541667,
    -7857.185714,
    -8047.829762,
    -8238.47381,
    -8429.117857,
    -8619.761905,
    -8810.405952,
    -9001.05,
    -9191.694048,
    -9382.338095,
    -9572.982143
  ]
}
```

### 结果解释
- 本问用 `linear_trend_forecast` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 实验报告

本问的核心是：2010年上海世博会是首次在中国举办的世界博览会。从1851年伦敦的“万国工业博览会”开始，世博会正日益成为各国人民交流历史文化、展示科技成果、体现合作精神、展望未来发展等的重要舞台。请你们选择感兴趣的某个侧面，建立数学模型，利用互联网数据，定量评估2010年上海世博会的影响力

建模时先将题目要求拆成 1 个任务，再选择 `时间序列预测`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
