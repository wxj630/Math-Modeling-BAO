# 2017-C q05：给 Washington Governor 的建议信

## 题目原问
Prepare a concise letter to the Governor's office summarizing the model results and recommended transportation policy.

## 适合模型
把官方路网数据、10/50/90 情景、临界点和专用车道规则压缩为州长办公室可读建议。对应模型：非技术政策报告、模型结果解释、交通治理建议。

## 数据与真实性
- 数据类型：official_comap_xlsx。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2017/Problem Data- Cooperate and Navigate`。
- 行数/记录数：{'parsed mile posts': 224, 'definitions': 8}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 性能临界点
- 判据：first AV share where total peak vehicle-hours are at least 10% below the all-human baseline
- AV share：0.49。
- baseline peak vehicle-hours：19781.936124。
- target peak vehicle-hours：17803.742512。
- achieved peak vehicle-hours：17777.667893。

### 专用车道政策
- 规则：Do not reserve scarce two-lane facilities. Pilot one AV-only lane only on >=3 lane-per-direction segments when AV demand is at least 50% and modeled vehicle-hours beat mixed traffic.
- 候选路段数：0。

无可展示记录。

### Governor letter
To the Governor: the official 2017 MCM-C traffic workbook shows that the I-5/I-90/I-405/SR-520 corridor has many segments near or above a volume-capacity ratio of one under a simple peak-hour model. At 10% automated vehicles, the benefit is modest and should be handled in mixed traffic. Around the modeled tipping point, cooperative vehicles begin reducing total peak vehicle-hours materially. Dedicated AV lanes should therefore be piloted only on high-volume corridors with at least three lanes per direction and at least 50% AV demand; otherwise, taking a lane away from human drivers can make congestion worse.

## 模型限制
- 这是可复现的官方 Cooperate and Navigate 交通 workbook 实验；只使用 `2017_MCM_Problem_C_Data.xlsx` 的 `parsed mile posts` 与 `definitions` 工作表，不使用随机造数。
- 峰小时占比、每车道容量、AV 容量倍率和 BPR 速度函数是显式交通流假设，用于把官方 ADT/车道数转换成可比较性能指标；正式论文应补充小时级探测器速度、OD 需求和实际 AV 行为数据校准。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2017/C/q05/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2017/C/q05/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2017/C/q05/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2017/C/q05`
