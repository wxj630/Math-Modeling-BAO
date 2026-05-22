# 2022-C q03：交易成本敏感性

## 题目原问
Determine how sensitive the strategy is to transaction costs. How do transaction costs affect the strategy and results?

## 适合模型
保持官方黄金手续费 1% 基线，枚举比特币手续费 0%-12%，重新运行同一因果策略并输出最终价值、收益率和交易次数。

## 数据与真实性
- 数据类型：official_comap_csv。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted/2022/Problem Data- Trading Strategies`。
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

无可展示记录。

### 交易成本敏感性

| alpha_gold | alpha_bitcoin | final_value | total_return_percent | trade_count |
|---|---|---|---|---|
| 0.01 | 0.0 | 73117.910721 | 7211.791072 | 1 |
| 0.01 | 0.01 | 73108.110721 | 7210.811072 | 1 |
| 0.01 | 0.02 | 73098.310721 | 7209.831072 | 1 |
| 0.01 | 0.04 | 71720.870017 | 7072.087002 | 1 |
| 0.01 | 0.08 | 69064.541498 | 6806.45415 | 1 |
| 0.01 | 0.12 | 66597.95073 | 6559.795073 | 1 |

## 模型限制
- 这是可复现的官方 Trading Strategies CSV 附件实验；只使用 LBMA-GOLD.csv 和 BCHAIN-MKPRU.csv 两个 COMAP 文件，不使用随机造数或外部行情。
- 候选策略最优性只在脚本中列出的透明因果规则族内成立；正式论文应扩展到风险约束、效用函数、滚动交叉验证和更严格的在线学习证明。

## 运行方式
`.venv/bin/python mcm/question_solutions/2022/C/q03/solution.py`

## 输出
- `mcm/question_results/2022/C/q03/result.json`
- `mcm/question_reports/2022/C/q03/report.md`
- `mcm/question_artifacts/2022/C/q03`
