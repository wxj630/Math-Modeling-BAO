# 2022-C q04：给交易员的两页以内备忘录

## 题目原问
Communicate your strategy, model, and results to the trader in a memorandum of at most two pages.

## 适合模型
把官方数据来源、交易日限制、佣金、候选策略排名、最终价值和手续费敏感性整理成交易员可读 memo。

## 数据与真实性
- 数据类型：official_comap_csv。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2022/Problem Data- Trading Strategies`。
- 行数/记录数：{'LBMA-GOLD.csv': 1265, 'BCHAIN-MKPRU.csv': 1826}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 交易策略结果
- 选定策略：buy_hold_bitcoin。
- 初始资金：1000.0 USD。
- 期末价值：73098.310721 USD。
- 总收益率：7209.831072%。
- 最大回撤：-0.8337。
- 交易次数：1。
- 是否使用未来价格：False。

#### 候选策略比较

| strategy | final_value | total_return_percent | max_drawdown | trade_count |
|---|---|---|---|---|
| buy_hold_bitcoin | 73098.310721 | 7209.831072 | -0.8337 | 1 |
| momentum_60_day | 19795.597005 | 1879.559701 | -0.816322 | 123 |
| momentum_180_day | 13378.185931 | 1237.818593 | -0.737174 | 50 |
| monthly_equal_gold_bitcoin | 12742.74497 | 1174.274497 | -0.555324 | 254 |
| buy_hold_gold | 1337.927616 | 33.792762 | -0.184148 | 1 |
| cash_only | 1000.0 | 0.0 | 0.0 | 0 |

### 交易成本敏感性

| alpha_gold | alpha_bitcoin | final_value | total_return_percent | trade_count |
|---|---|---|---|---|
| 0.01 | 0.0 | 73117.910721 | 7211.791072 | 1 |
| 0.01 | 0.01 | 73108.110721 | 7210.811072 | 1 |
| 0.01 | 0.02 | 73098.310721 | 7209.831072 | 1 |
| 0.01 | 0.04 | 71720.870017 | 7072.087002 | 1 |
| 0.01 | 0.08 | 69064.541498 | 6806.45415 | 1 |
| 0.01 | 0.12 | 66597.95073 | 6559.795073 | 1 |

### 给交易员的备忘录
To the trader: using only the two official price streams through each decision date, the strongest low-turnover rule in the tested causal rule family is to buy bitcoin at the start of the horizon and hold it. The rule ends with $73,098.31; the ranked comparison table identifies buy_hold_bitcoin as the best tested rule. The result is highly sensitive to the bitcoin commission because the initial purchase is large: the tested final value moves from $73,117.91 at zero bitcoin commission to $66,597.95 at 12% bitcoin commission. This memo should not be read as a guarantee for future markets; it is the contest-period result from the two provided spreadsheets and transparent causal rules.

## 模型限制
- 这是可复现的官方 Trading Strategies CSV 附件实验；只使用 LBMA-GOLD.csv 和 BCHAIN-MKPRU.csv 两个 COMAP 文件，不使用随机造数或外部行情。
- 候选策略最优性只在脚本中列出的透明因果规则族内成立；正式论文应扩展到风险约束、效用函数、滚动交叉验证和更严格的在线学习证明。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2022/C/q04/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2022/C/q04/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2022/C/q04/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2022/C/q04`
