# 2022 MCM-C Trading Strategies

## 数据与真实性
- 官方题面：`docs/mcm-2015-2025/official_assets_extracted/2022/Trading Strategies.pdf`。
- 官方附件：`docs/mcm-2015-2025/official_assets_extracted/2022/Problem Data- Trading Strategies/LBMA-GOLD.csv` 与 `docs/mcm-2015-2025/official_assets_extracted/2022/Problem Data- Trading Strategies/BCHAIN-MKPRU.csv`。
- 只使用 COMAP 提供的两个价格序列；没有随机数、没有外部行情、没有 x1/x2/x3 占位数据。

## 核心模型
- 投资组合状态为题面指定的 `[cash, gold_oz, bitcoin]`。
- 每个候选专家规则只读取截至当日的官方价格；黄金只在 `LBMA-GOLD.csv` 有报价的日期交易，比特币每日交易。
- 交易佣金在买卖时从交易额扣除：黄金 1%，比特币 2%。

## 策略比较
| strategy | final_value | return_% | max_drawdown | trades |
|---|---:|---:|---:|---:|
| buy_hold_bitcoin | 73098.31 | 7209.83 | -0.8337 | 1 |
| momentum_60_day | 19795.60 | 1879.56 | -0.8163 | 123 |
| momentum_180_day | 13378.19 | 1237.82 | -0.7372 | 50 |
| monthly_equal_gold_bitcoin | 12742.74 | 1174.27 | -0.5553 | 254 |
| buy_hold_gold | 1337.93 | 33.79 | -0.1841 | 1 |
| cash_only | 1000.00 | 0.00 | 0.0000 | 0 |

## 选定策略与结果
- 选定策略：`buy_hold_bitcoin`。
- 2021-09-10 组合价值：`$73,098.31`。
- 最大回撤：`-0.8337`。

## 交易成本敏感性
| alpha_gold | alpha_bitcoin | final_value | return_% | trades |
|---:|---:|---:|---:|---:|
| 0.01 | 0.00 | 73117.91 | 7211.79 | 1 |
| 0.01 | 0.01 | 73108.11 | 7210.81 | 1 |
| 0.01 | 0.02 | 73098.31 | 7209.83 | 1 |
| 0.01 | 0.04 | 71720.87 | 7072.09 | 1 |
| 0.01 | 0.08 | 69064.54 | 6806.45 | 1 |
| 0.01 | 0.12 | 66597.95 | 6559.80 | 1 |

## 给交易员的备忘录
To the trader: using only the two official price streams through each decision date, the strongest low-turnover rule in the tested causal rule family is to buy bitcoin at the start of the horizon and hold it. The rule ends with $73,098.31; the ranked comparison table identifies buy_hold_bitcoin as the best tested rule. The result is highly sensitive to the bitcoin commission because the initial purchase is large: the tested final value moves from $73,117.91 at zero bitcoin commission to $66,597.95 at 12% bitcoin commission. This memo should not be read as a guarantee for future markets; it is the contest-period result from the two provided spreadsheets and transparent causal rules.

## 输出文件
- `artifacts/portfolio_value_curve.csv`
- `artifacts/portfolio_value_curve.png`
- `artifacts/daily_trades.csv`
- `artifacts/strategy_comparison.csv`
- `artifacts/transaction_cost_sensitivity.csv`
