# 2021-C 问题 2 建模求解实验报告

## 题目原文与任务拆解

- 题目：2021年 CUMCM C题：生产企业原材料的订购与运输
- 问题：问题 2
- 原问：供应商的供货量：第一列为供应商的名称； 第二列为供应商供应原材料的类别； 第三列及以后共240 列为各供应商每周的供货量 （单位： 立方米） ； 数值 “0” 表示相应 的周（所在列）供应商（所在行）没有供货。 附件 2 的数据说明 第一列为转运商的名称； 第二列及以后共240 列为每周各转运商的运输损耗率 （%）， 即 100%−=供货量 接收量损耗率 供货量 ；数值“0”表示没有运送。

### 本问需要完成什么
- 任务 1：供应商的供货量：第一列为供应商的名称
- 任务 2：第二列为供应商供应原材料的类别
- 任务 3：第三列及以后共240 列为各供应商每周的供货量 （单位： 立方米）
- 任务 4：数值 “0” 表示相应 的周（所在列）供应商（所在行）没有供货
- 任务 5：附件 2 的数据说明 第一列为转运商的名称
- 任务 6：第二列及以后共240 列为每周各转运商的运输损耗率 （%）， 即 100%−=供货量 接收量损耗率 供货量

## 适配模型

- 主模型：订购-转运联合规划优化（CH3：函数极值与规划模型）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md

### 候选模型与适配理由
- 图论网络与路径调度（CH4）：运输、转运；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH4/第4章-复杂网络与图论模型.md
- 数据拟合与回归分析（CH6）：数据；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH6/第六章-数据处理与拟合模型.md

## 变量、约束与公式

### 建模假设
- 附件1的近240周订货量、供货量可代表供应商未来短期供给能力和履约稳定性。
- A、B、C类原材料单位产品消耗量分别为0.60、0.66、0.72立方米，采购单价相对C类分别为1.20、1.10、1.00。
- 每家转运商每周运输能力为6000立方米，供应商每周供货尽量由一家转运商承运；超出容量时才拆分。
- 未来24周计划使用历史近48周和近24周供给统计形成稳健供给上限，方案结果是可复现实验基线而非官方唯一最优解。

### 变量定义
- s_i: 第 i 家供应商的重要性综合得分
- x_{i,t}: 第 t 周向供应商 i 的订货量
- y_{i,t}: 第 t 周供应商 i 的预期供货量
- z_{i,k,t}: 第 t 周由转运商 k 承运供应商 i 的供货量
- I_t: 第 t 周折算为产成品体积的可用接收原料能力

### 约束条件
- 0 <= y_{i,t} <= cap_i，其中 cap_i 由供应商近48周稳健供给能力估计。
- sum_i received_{i,t}/coef_i >= 28200，保证每周2.82万立方米产能需求。
- sum_i z_{i,k,t} <= 6000，任一转运商每周承运量不超过6000立方米。
- sum_k z_{i,k,t} = y_{i,t}，所有预期供货量均安排转运。
- 问题3增加A类优先、C类惩罚；问题4放松产能目标并最大化可实现周产能。

### 模型公式 / 目标函数
- `data_audit = shape(orders, supply, losses) + missing_rate + nonzero_rate`
- `validate attachment fields before optimization.`

## Python 代码与运行方式

- 代码文件：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2021/C/q06/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2021/C/q06/solution.py`
- 批量运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：读取附件1和附件2，核对供应商数、周数、转运商数。
- 步骤 2：统计订货、供货和损耗率数据的非零比例。
- 步骤 3：输出附件字段说明与可用于前4问建模的数据字典。

## 实验结果与解释

### 产物文件
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2021/C/q06/experiment_table.csv

### 数据来源
- 类型：attachment
- 附件：/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/C/附件1 近5年402家供应商的相关数据.xlsx; /Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/C/附件2 近5年8家转运商的相关数据.xlsx; /Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/C/附件A 订购方案数据结果.xlsx; /Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/C/附件B 转运方案数据结果.xlsx
- 读取规模：410 行 x 240 列
- 说明：本题专用算法读取附件1的402家供应商240周订货/供货量、附件2的8家转运商240周损耗率，并按附件A/B模板生成24周订购与转运方案。

### result.json 核心结果

```json
{
  "method": "attachment_data_dictionary_audit",
  "orders_shape": [
    402,
    240
  ],
  "supply_shape": [
    402,
    240
  ],
  "loss_shape": [
    8,
    240
  ],
  "supplier_count": 402,
  "transporter_count": 8,
  "report": [
    "该条目来自题面附件说明被解析成的附加问题，不是正式竞赛第5问/第6问。",
    "实验在这里保留数据字典审计结果，说明前4问专用模型使用的数据字段、规模和非零比例。"
  ]
}
```

### 结果解释
- 本问用 `attachment_data_dictionary_audit` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 专用实验报告

- 该条目来自题面附件说明被解析成的附加问题，不是正式竞赛第5问/第6问。
- 实验在这里保留数据字典审计结果，说明前4问专用模型使用的数据字段、规模和非零比例。

## 实验报告

本问的核心是：供应商的供货量：第一列为供应商的名称； 第二列为供应商供应原材料的类别； 第三列及以后共240 列为各供应商每周的供货量 （单位： 立方米） ； 数值 “0” 表示相应 的周（所在列）供应商（所在行）没有供货。 附件 2 的数据说明 第一列为转运商的名称； 第二列及以后共240 列为每周各转运商的运输损耗率 （%）， 即 100%−=供货量 接收量损耗率…

建模时先将题目要求拆成 6 个任务，再选择 `订购-转运联合规划优化`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
