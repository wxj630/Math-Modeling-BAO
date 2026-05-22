# 2022-F q07：条件变化对全球公平的敏感性

## 题目原问
How do changes in the conditions that you selected in defining a vision for the future of asteroid mining impact global equity?

## 适合模型
逐一改变 benefit fund、license transparency、technology pool、exclusive claims、debris liability、dual-use pressure，输出公平分变化。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets/2022/All for One and One (Space) for All!`。
- 行数/记录数：{}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 情境化敏感性分析
- 方法：one-at-a-time deterministic condition sensitivity on the recommended asteroid-mining vision。

#### 有利条件

无可展示记录。

#### 不利条件

无可展示记录。

### 敏感性分析
- 方法：one-at-a-time deterministic condition sensitivity on the recommended asteroid-mining vision。

无可展示记录。

## 模型限制
- 这是可复现的官方数据基线实验，适合做论文骨架和结果表，不应把随机森林相关性解释为严格因果。
- 对异常国家/代表队名称、教练履历、项目规则变化等，需要在竞赛论文中追加人工核验和敏感性分析。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2022/F/q07/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2022/F/q07/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2022/F/q07/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2022/F/q07`
