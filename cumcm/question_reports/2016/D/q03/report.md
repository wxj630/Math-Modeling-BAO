# 2016-D 问题 3 建模求解实验报告

## 题目原文与任务拆解

- 题目：2016年 CUMCM D题：风电场运行状况分析及优化
- 问题：问题 3
- 原问：为安全生产需要，风机每年需进行两次停机维护，两次维护之间的连续工作时间不超过270天，每次维护需一组维修人员连续工作2天。同时风电场每天需有一组维修人员值班以应对突发情况。风电场现有4组维修人员可从事值班或维护工作，每组维修人员连续工作时间（值班或维护）不超过6天。请制定维修人员的排班方案与风机维护计划，使各组维修人员的工作任务相对均衡，且风电场具有较好的经济效益，试给出你的方法和结果。 附件1 平均风速和风电场日实际输出功率表。 附件2 风电场典型风机报表。 附件3 风电场风机型号及其参数。 附件4 风机生产企业提供的新型号风机主要参数。

### 本问需要完成什么
- 任务 1：请制定维修人员的排班方案与风机维护计划，使各组维修人员的工作任务相对均衡，且风电场具有较好的经济效益，试给出你的方法和结果

## 适配模型

- 主模型：风资源评估、机型匹配与维护排班优化（CH3：函数极值与规划模型）
- 教程参考：/Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md

### 候选模型与适配理由
- 综合评价与权重决策（CH7）：问题1需要综合风速、发电量、容量因子和低风停发等指标评价风资源利用情况。；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH7/第7章-权重生成与评价模型.md
- 数据拟合与回归分析（CH6）：问题2需要把风速样本映射到机型功率曲线，比较现有机型和新机型的匹配程度。；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH6/第六章-数据处理与拟合模型.md
- 规划优化与资源配置（CH3）：问题3是典型维护计划与人员排班优化，目标兼顾经济损失和工作量均衡。；参考 /Users/wuxiaojun/code/My-Agent/intro-mathmodel/docs/CH3/第三章-函数极值与规划模型.md

## 变量、约束与公式

### 建模假设
- 附件1中功率单位为MW、风速单位为m/s，每个工作表对应一天，每天96个15分钟记录。
- 附件2为6台典型风机每2小时风速样本，4/16/24号代表一期，33/49/57号代表二期。
- 附件3现有机型I/II功率曲线按文档转换结果录入；附件4新机型III/IV/V用切入、额定、切出和额定功率构造三次功率曲线。
- 风机实际发电量按15分钟功率积分；装机容量按题面约20万kW取200MW计算容量因子。
- 维护排班把124台风机各安排两次2天维护，第二次与第一次间隔180天，满足不超过270天连续运行要求。
- 通用基线保留在 cumcm/generic_baselines，当前结果为附件驱动的风电场运行分析版本。

### 变量定义
- v_t: t时刻风电场平均风速
- P_t: t时刻风电场实际输出功率
- E_day: 日发电量
- CF: 容量因子
- f_m(v): 机型m在风速v下的功率曲线
- x_{i,k}: 风机i第k次维护开始日期
- y_{g,d}: 维修组g在日期d的任务（值班/维护/休息）

### 约束条件
- 每台风机每年维护两次，每次连续2天。
- 两次维护之间间隔设置为180天，小于270天上限。
- 每天至少一组维修人员值班。
- 每组维修人员连续工作天数不超过6天。
- 维护尽量安排在相对低发电量时段，以降低经济损失。

### 模型公式 / 目标函数
- `E_day=sum_t P_t*0.25`
- `CF=sum_day E_day/(200MW*24h*365)`
- `available_energy_m = mean(f_m(v_t))*8760/1000`
- `wind_match_score = expected_energy / rated_power`
- `minimize lost_energy + workload_imbalance_penalty`

## Python 代码与运行方式

- 代码文件：/Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2016/D/q03/solution.py
- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_solutions/2016/D/q03/solution.py`
- 批量运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/scripts/run_question_all.py`

### 求解步骤
- 步骤 1：利用附件1日发电量识别相对低损失维护窗口。
- 步骤 2：为124台风机生成两次维护计划，间隔180天，每次持续2天。
- 步骤 3：4组人员按每日值班和维护任务轮换，保证每组连续工作不超过6天。
- 步骤 4：输出维护计划、人员日程和维护期损失估算。

## 实验结果与解释

### 产物文件
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2016/D/q03/maintenance_plan.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2016/D/q03/crew_daily_schedule.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2016/D/q03/maintenance_economic_loss.csv
- /Users/wuxiaojun/code/Math-Modeling-World/cumcm/question_artifacts/2016/D/q03/experiment_table.csv

### 数据来源
- 类型：attachment
- 附件：/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016D-Chinese/CUMCM2016-D-Appendix-Chinese/附件1  平均风速和风电场日实际输出功率表/201501.xls; /Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016D-Chinese/CUMCM2016-D-Appendix-Chinese/附件1  平均风速和风电场日实际输出功率表/201502.xls; /Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016D-Chinese/CUMCM2016-D-Appendix-Chinese/附件1  平均风速和风电场日实际输出功率表/201503.xls; /Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016D-Chinese/CUMCM2016-D-Appendix-Chinese/附件1  平均风速和风电场日实际输出功率表/201504.xls; /Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016D-Chinese/CUMCM2016-D-Appendix-Chinese/附件1  平均风速和风电场日实际输出功率表/201505.xls; /Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016D-Chinese/CUMCM2016-D-Appendix-Chinese/附件1  平均风速和风电场日实际输出功率表/201506.xls; /Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016D-Chinese/CUMCM2016-D-Appendix-Chinese/附件1  平均风速和风电场日实际输出功率表/201507.xls; /Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016D-Chinese/CUMCM2016-D-Appendix-Chinese/附件1  平均风速和风电场日实际输出功率表/201508.xls; ...
- 读取规模：56940 行 x 3 列
- 说明：本题专用算法读取附件1全年15分钟风速/功率、附件2典型风机风速报表，以及附件3/4风机参数，完成风资源评估、机型匹配和维护排班。

### result.json 核心结果

```json
{
  "method": "wind_farm_maintenance_crew_schedule_optimization",
  "turbine_count": 124,
  "maintenance_event_count": 248,
  "crew_count": 4,
  "min_crew_work_days": 215,
  "max_crew_work_days": 216,
  "max_consecutive_work_days": 3,
  "total_estimated_lost_energy_mwh": 3667.170118,
  "report": [
    "问题3为124台风机各安排两次2天维护，第二次距第一次约180天，满足连续运行不超过270天。",
    "每天按4组人员轮换设置一组值班；维护组避开当天和次日值班组，使每组有规律休息并控制连续工作天数。",
    "经济损失按维护两天风场日发电量的单机份额估算，维护计划、人员日程和损失明细均输出为CSV。"
  ]
}
```

### 结果解释
- 本问用 `wind_farm_maintenance_crew_schedule_optimization` 将题面任务转化为可计算实验，并把关键数值写入 JSON 和 CSV 产物。
- CSV 表是后续写论文表格、画图或替换真实附件数据的主要入口；如果题面要求 result*.xlsx，可在该表基础上按模板导出。
- 数据来源字段会标明本问使用官方附件、题面参数还是专用题面常量；后续冲论文质量时，可在现有 CSV/JSON 基础上补充图表、误差分析和敏感性分析。

## 专用实验报告

- 问题3为124台风机各安排两次2天维护，第二次距第一次约180天，满足连续运行不超过270天。
- 每天按4组人员轮换设置一组值班；维护组避开当天和次日值班组，使每组有规律休息并控制连续工作天数。
- 经济损失按维护两天风场日发电量的单机份额估算，维护计划、人员日程和损失明细均输出为CSV。

## 实验报告

本问的核心是：为安全生产需要，风机每年需进行两次停机维护，两次维护之间的连续工作时间不超过270天，每次维护需一组维修人员连续工作2天。同时风电场每天需有一组维修人员值班以应对突发情况。风电场现有4组维修人员可从事值班或维护工作，每组维修人员连续工作时间（值班或维护）不超过6天。请制定维修人员的排班方案与风机维护计划，使各组维修人员的工作任务相对均衡，且风电场具有较好的…

建模时先将题目要求拆成 1 个任务，再选择 `风资源评估、机型匹配与维护排班优化`。求解过程严格对应变量定义、约束条件和目标函数：先构造可计算数据表，再调用 Python 数值算法得到实验结果，最后把结果写入 `result.json` 与 `experiment_table.csv`。

报告写作时建议按以下结构展开：问题重述、符号说明、模型假设、模型建立、算法实现、结果表格、误差/敏感性分析、模型评价。
