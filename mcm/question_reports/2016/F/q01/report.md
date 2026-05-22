# 2016-F q01：难民危机指标体系

## 题目原问
Determine the specific factors which can either enable or inhibit the safe and efficient movement of refugees.

## 适合模型
只使用官方题面中的 715,000+ 庇护申请、Hungary 1,450/100k、2014 年 32% 批准率和六条路线，构造可启用/抑制安全高效流动的因素列表与 route/resource/capacity 指标。对应模型：指标体系、多指标综合评价、容量约束建模。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted/2016`。
- 行数/记录数：{'official_problem_parameters': 7}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 难民危机指标体系
- 官方规模：715000。
- Hungary 未安置压力代理：986.0 / 100k。

#### 启用因素
- safe route segments
- available transport
- multiple entry points
- destination resource capacity
- legal processing capacity
- NGO mobile support

#### 抑制因素
- dangerous sea crossings
- bottlenecked borders
- low approval rates
- shelter and healthcare scarcity
- local backlash after security shocks
- rapidly changing political constraints

## 模型限制
- 这是可复现的官方题面参数难民政策实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中 715,000+ 申请、Hungary 1,450/100k、32% 批准率、六条路线、最热门/最危险路线、NGO、外生事件和 10 倍扩展等约束。
- 路线安全、可达性、临时容量、日处理能力、资源包和 NGO 增益是显式规划假设，不是边境观测数据；正式论文应补充 UNHCR/IOM/FRONTEX 路线流量、死亡风险、接收容量、庇护审批、公共卫生和本地融合数据校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2016/F/q01/solution.py`

## 输出
- `mcm/question_results/2016/F/q01/result.json`
- `mcm/question_reports/2016/F/q01/report.md`
- `mcm/question_artifacts/2016/F/q01`
