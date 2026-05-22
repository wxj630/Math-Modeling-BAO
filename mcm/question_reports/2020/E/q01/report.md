# 2020-E q01：单次使用塑料废弃物安全缓解容量

## 题目原问
Develop a model to estimate maximum levels of single-use or disposable plastic product waste that can safely be mitigated without further environmental damage.

## 适合模型
使用官方 9% recycling、4-12 million tons ocean input 等题面数字，按区域 waste、single-use share、mitigation capacity 和 policy capacity 估算安全处理容量和溢出。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025/official_assets`。
- 行数/记录数：{'official_parameters': 5}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

## 模型限制
- 这是可复现的官方题面参数塑料废弃物规划实验；COMAP 没有提供国家塑料流量表，因此只使用 PDF 中 9% recycling、4-12 million tons ocean input、2050 more plastic than fish 和公平治理等题面约束。
- 区域废弃物流、政策减量率和公平责任分数是显式确定性情景输入，不是 UN/OECD/国家废弃物清单；正式论文应补充塑料生产、贸易、回收、泄漏、替代品和产业影响数据校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2020/E/q01/solution.py`

## 输出
- `mcm/question_results/2020/E/q01/result.json`
- `mcm/question_reports/2020/E/q01/report.md`
- `mcm/question_artifacts/2020/E/q01`
