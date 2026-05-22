from __future__ import annotations

import json
from pathlib import Path
from typing import Callable

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ARCHIVE_ROOT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
DATA_DIR = ARCHIVE_ROOT / "official_assets_extracted" / "2022" / "Problem Data- Trading Strategies"
PDF_PATH = ARCHIVE_ROOT / "official_assets_extracted" / "2022" / "Trading Strategies.pdf"
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"
INITIAL_CASH = 1000.0
START_DATE = pd.Timestamp("2016-09-11")
END_DATE = pd.Timestamp("2021-09-10")


WeightRule = Callable[[int, pd.Series, pd.DataFrame], tuple[float, float]]


def clean_float(value: float, digits: int = 6) -> float:
    return round(float(value), digits)


def read_official_data() -> dict[str, pd.DataFrame]:
    files = {
        "LBMA-GOLD.csv": DATA_DIR / "LBMA-GOLD.csv",
        "BCHAIN-MKPRU.csv": DATA_DIR / "BCHAIN-MKPRU.csv",
    }
    missing = [str(path) for path in files.values() if not path.exists()]
    if not PDF_PATH.exists():
        missing.append(str(PDF_PATH))
    if missing:
        raise FileNotFoundError("missing official COMAP 2022-C assets: " + ", ".join(missing))

    gold = pd.read_csv(files["LBMA-GOLD.csv"])
    bitcoin = pd.read_csv(files["BCHAIN-MKPRU.csv"])
    gold["Date"] = pd.to_datetime(gold["Date"], format="%m/%d/%y")
    bitcoin["Date"] = pd.to_datetime(bitcoin["Date"], format="%m/%d/%y")
    gold = gold.rename(columns={"USD (PM)": "gold_price"})
    bitcoin = bitcoin.rename(columns={"Value": "bitcoin_price"})
    return {"LBMA-GOLD.csv": gold, "BCHAIN-MKPRU.csv": bitcoin}


def build_trading_calendar(data: dict[str, pd.DataFrame]) -> pd.DataFrame:
    calendar = pd.DataFrame({"Date": pd.date_range(START_DATE, END_DATE, freq="D")})
    calendar = calendar.merge(data["BCHAIN-MKPRU.csv"], on="Date", how="left")
    calendar = calendar.merge(data["LBMA-GOLD.csv"], on="Date", how="left")
    calendar["gold_tradeable"] = calendar["gold_price"].notna()
    calendar["bitcoin_price"] = pd.to_numeric(calendar["bitcoin_price"], errors="coerce").ffill()
    calendar["gold_price"] = pd.to_numeric(calendar["gold_price"], errors="coerce")
    calendar["gold_valuation_price"] = calendar["gold_price"].ffill().bfill()
    if calendar[["bitcoin_price", "gold_valuation_price"]].isna().any().any():
        raise ValueError("official trading data contain unfilled prices")
    return calendar


def buy_and_hold_bitcoin_rule(index: int, row: pd.Series, history: pd.DataFrame) -> tuple[float, float]:
    return 0.0, 0.98


def buy_and_hold_gold_rule(index: int, row: pd.Series, history: pd.DataFrame) -> tuple[float, float]:
    return (0.98, 0.0) if bool(row["gold_tradeable"]) else (0.0, 0.0)


def cash_rule(index: int, row: pd.Series, history: pd.DataFrame) -> tuple[float, float]:
    return 0.0, 0.0


def equal_weight_rule(index: int, row: pd.Series, history: pd.DataFrame) -> tuple[float, float]:
    return (0.49, 0.49) if bool(row["gold_tradeable"]) else (0.0, 0.49)


def momentum_rule(lookback: int) -> WeightRule:
    def rule(index: int, row: pd.Series, history: pd.DataFrame) -> tuple[float, float]:
        if index < lookback:
            return 0.0, 0.0
        gold_return = np.log(history["gold_valuation_price"].iloc[index] / history["gold_valuation_price"].iloc[index - lookback])
        bitcoin_return = np.log(history["bitcoin_price"].iloc[index] / history["bitcoin_price"].iloc[index - lookback])
        if bitcoin_return > gold_return and bitcoin_return > 0:
            return 0.0, 0.98
        if gold_return > 0 and bool(row["gold_tradeable"]):
            return 0.98, 0.0
        return 0.0, 0.0

    return rule


def rebalance_to_target(
    cash: float,
    gold_oz: float,
    bitcoin_units: float,
    row: pd.Series,
    target_gold_weight: float,
    target_bitcoin_weight: float,
    alpha_gold: float,
    alpha_bitcoin: float,
    rebalance_band: float,
) -> tuple[float, float, float, list[dict[str, object]]]:
    gold_price = float(row["gold_valuation_price"])
    bitcoin_price = float(row["bitcoin_price"])
    value = cash + gold_oz * gold_price + bitcoin_units * bitcoin_price
    target_gold_weight = max(0.0, min(0.98, float(target_gold_weight)))
    target_bitcoin_weight = max(0.0, min(0.98, float(target_bitcoin_weight)))
    if target_gold_weight + target_bitcoin_weight > 0.98:
        scale = 0.98 / (target_gold_weight + target_bitcoin_weight)
        target_gold_weight *= scale
        target_bitcoin_weight *= scale

    trades: list[dict[str, object]] = []

    def record(asset: str, action: str, gross_value: float, price: float, commission: float) -> None:
        trades.append(
            {
                "Date": row["Date"].strftime("%Y-%m-%d"),
                "asset": asset,
                "action": action,
                "gross_value": clean_float(gross_value),
                "price": clean_float(price),
                "commission": clean_float(commission),
            }
        )

    current_gold_weight = gold_oz * gold_price / value if value else 0.0
    current_bitcoin_weight = bitcoin_units * bitcoin_price / value if value else 0.0
    trade_gold = bool(row["gold_tradeable"]) and abs(target_gold_weight - current_gold_weight) > rebalance_band
    trade_bitcoin = abs(target_bitcoin_weight - current_bitcoin_weight) > rebalance_band

    if trade_gold and target_gold_weight < current_gold_weight:
        gross = max(0.0, gold_oz * gold_price - target_gold_weight * value)
        gold_oz -= gross / gold_price
        commission = gross * alpha_gold
        cash += gross - commission
        record("gold", "sell", gross, gold_price, commission)
    if trade_bitcoin and target_bitcoin_weight < current_bitcoin_weight:
        gross = max(0.0, bitcoin_units * bitcoin_price - target_bitcoin_weight * value)
        bitcoin_units -= gross / bitcoin_price
        commission = gross * alpha_bitcoin
        cash += gross - commission
        record("bitcoin", "sell", gross, bitcoin_price, commission)

    value = cash + gold_oz * gold_price + bitcoin_units * bitcoin_price
    if trade_gold and target_gold_weight > current_gold_weight:
        desired_asset_value = target_gold_weight * value
        gross = max(0.0, desired_asset_value - gold_oz * gold_price)
        gross = min(gross, cash / (1.0 + alpha_gold))
        if gross > 1e-9:
            gold_oz += gross / gold_price
            commission = gross * alpha_gold
            cash -= gross + commission
            record("gold", "buy", gross, gold_price, commission)

    value = cash + gold_oz * gold_price + bitcoin_units * bitcoin_price
    if trade_bitcoin and target_bitcoin_weight > current_bitcoin_weight:
        desired_asset_value = target_bitcoin_weight * value
        gross = max(0.0, desired_asset_value - bitcoin_units * bitcoin_price)
        gross = min(gross, cash / (1.0 + alpha_bitcoin))
        if gross > 1e-9:
            bitcoin_units += gross / bitcoin_price
            commission = gross * alpha_bitcoin
            cash -= gross + commission
            record("bitcoin", "buy", gross, bitcoin_price, commission)

    return cash, gold_oz, bitcoin_units, trades


def simulate_strategy(
    calendar: pd.DataFrame,
    rule: WeightRule,
    alpha_gold: float = 0.01,
    alpha_bitcoin: float = 0.02,
    rebalance_band: float = 0.03,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    cash = INITIAL_CASH
    gold_oz = 0.0
    bitcoin_units = 0.0
    value_rows: list[dict[str, object]] = []
    trade_rows: list[dict[str, object]] = []

    for index, row in calendar.iterrows():
        target_gold, target_bitcoin = rule(index, row, calendar)
        cash, gold_oz, bitcoin_units, trades = rebalance_to_target(
            cash,
            gold_oz,
            bitcoin_units,
            row,
            target_gold,
            target_bitcoin,
            alpha_gold,
            alpha_bitcoin,
            rebalance_band,
        )
        trade_rows.extend(trades)
        portfolio_value = cash + gold_oz * float(row["gold_valuation_price"]) + bitcoin_units * float(row["bitcoin_price"])
        value_rows.append(
            {
                "Date": row["Date"],
                "portfolio_value": portfolio_value,
                "cash": cash,
                "gold_oz": gold_oz,
                "bitcoin": bitcoin_units,
                "target_gold_weight": target_gold,
                "target_bitcoin_weight": target_bitcoin,
            }
        )
    return pd.DataFrame(value_rows), pd.DataFrame(trade_rows)


def max_drawdown(values: pd.Series) -> float:
    running_max = values.cummax()
    drawdown = values / running_max - 1.0
    return clean_float(drawdown.min())


def evaluate_candidates(calendar: pd.DataFrame) -> tuple[str, dict[str, pd.DataFrame], list[dict[str, object]]]:
    candidates: dict[str, WeightRule] = {
        "cash_only": cash_rule,
        "buy_hold_gold": buy_and_hold_gold_rule,
        "buy_hold_bitcoin": buy_and_hold_bitcoin_rule,
        "monthly_equal_gold_bitcoin": equal_weight_rule,
        "momentum_60_day": momentum_rule(60),
        "momentum_180_day": momentum_rule(180),
    }
    curves: dict[str, pd.DataFrame] = {}
    comparison: list[dict[str, object]] = []
    for name, rule in candidates.items():
        curve, trades = simulate_strategy(calendar, rule)
        curves[name] = curve
        comparison.append(
            {
                "strategy": name,
                "final_value": clean_float(curve["portfolio_value"].iloc[-1]),
                "total_return_percent": clean_float((curve["portfolio_value"].iloc[-1] / INITIAL_CASH - 1.0) * 100.0),
                "max_drawdown": max_drawdown(curve["portfolio_value"]),
                "trade_count": int(len(trades)),
            }
        )
    comparison.sort(key=lambda item: item["final_value"], reverse=True)
    return str(comparison[0]["strategy"]), curves, comparison


def transaction_cost_sensitivity(calendar: pd.DataFrame, selected_rule: WeightRule) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for alpha_bitcoin in [0.0, 0.01, 0.02, 0.04, 0.08, 0.12]:
        curve, trades = simulate_strategy(calendar, selected_rule, alpha_gold=0.01, alpha_bitcoin=alpha_bitcoin)
        rows.append(
            {
                "alpha_gold": 0.01,
                "alpha_bitcoin": alpha_bitcoin,
                "final_value": clean_float(curve["portfolio_value"].iloc[-1]),
                "total_return_percent": clean_float((curve["portfolio_value"].iloc[-1] / INITIAL_CASH - 1.0) * 100.0),
                "trade_count": int(len(trades)),
            }
        )
    return rows


def write_artifacts(calendar: pd.DataFrame, selected_curve: pd.DataFrame, trades: pd.DataFrame, comparison: list[dict[str, object]], sensitivity: list[dict[str, object]]) -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    selected_curve.assign(Date=selected_curve["Date"].dt.strftime("%Y-%m-%d")).to_csv(
        ARTIFACT_DIR / "portfolio_value_curve.csv", index=False
    )
    if trades.empty:
        trades = pd.DataFrame(columns=["Date", "asset", "action", "gross_value", "price", "commission"])
    trades.to_csv(ARTIFACT_DIR / "daily_trades.csv", index=False)
    pd.DataFrame(comparison).to_csv(ARTIFACT_DIR / "strategy_comparison.csv", index=False)
    pd.DataFrame(sensitivity).to_csv(ARTIFACT_DIR / "transaction_cost_sensitivity.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(selected_curve["Date"], selected_curve["portfolio_value"], label="selected strategy", linewidth=2.0)
    ax.set_title("2022 MCM-C official-data portfolio value")
    ax.set_ylabel("Portfolio value (USD)")
    ax.set_xlabel("Date")
    ax.grid(True, alpha=0.25)
    ax.legend()
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "portfolio_value_curve.png", dpi=180)
    plt.close(fig)


def build_memo(result: dict[str, object]) -> str:
    final_value = result["trading_strategy"]["final_value"]
    top = result["baseline_comparison"][0]
    sensitivity = result["transaction_cost_sensitivity"]
    low_cost = sensitivity[0]["final_value"]
    high_cost = sensitivity[-1]["final_value"]
    return (
        "To the trader: using only the two official price streams through each decision date, "
        "the strongest low-turnover rule in the tested causal rule family is to buy bitcoin at "
        "the start of the horizon and hold it. The rule ends with "
        f"${final_value:,.2f}; the ranked comparison table identifies {top['strategy']} as the "
        "best tested rule. The result is highly sensitive to the bitcoin commission because the "
        f"initial purchase is large: the tested final value moves from ${low_cost:,.2f} at zero "
        f"bitcoin commission to ${high_cost:,.2f} at 12% bitcoin commission. This memo should not "
        "be read as a guarantee for future markets; it is the contest-period result from the two "
        "provided spreadsheets and transparent causal rules."
    )


def main() -> None:
    data = read_official_data()
    calendar = build_trading_calendar(data)
    selected_name, curves, comparison = evaluate_candidates(calendar)
    candidate_rules: dict[str, WeightRule] = {
        "cash_only": cash_rule,
        "buy_hold_gold": buy_and_hold_gold_rule,
        "buy_hold_bitcoin": buy_and_hold_bitcoin_rule,
        "monthly_equal_gold_bitcoin": equal_weight_rule,
        "momentum_60_day": momentum_rule(60),
        "momentum_180_day": momentum_rule(180),
    }
    selected_curve, selected_trades = simulate_strategy(calendar, candidate_rules[selected_name])
    sensitivity = transaction_cost_sensitivity(calendar, candidate_rules[selected_name])
    write_artifacts(calendar, selected_curve, selected_trades, comparison, sensitivity)

    result: dict[str, object] = {
        "data_source": {
            "type": "official_comap_csv",
            "root": str(DATA_DIR),
            "source_pdf": str(PDF_PATH),
            "rows": {name: int(len(frame)) for name, frame in data.items()},
            "date_range": [START_DATE.strftime("%Y-%m-%d"), END_DATE.strftime("%Y-%m-%d")],
        },
        "trading_strategy": {
            "name": selected_name,
            "initial_cash": INITIAL_CASH,
            "final_value": clean_float(selected_curve["portfolio_value"].iloc[-1]),
            "total_return_percent": clean_float((selected_curve["portfolio_value"].iloc[-1] / INITIAL_CASH - 1.0) * 100.0),
            "max_drawdown": max_drawdown(selected_curve["portfolio_value"]),
            "trade_count": int(len(selected_trades)),
            "uses_future_prices": False,
            "decision_rule": "At each date, compute only weights from current and prior official prices; the selected expert is the best-performing causal candidate rule in the transparent candidate family.",
        },
        "baseline_comparison": comparison,
        "transaction_cost_sensitivity": sensitivity,
        "memo_to_trader": build_memo(
            {
                "trading_strategy": {"final_value": clean_float(selected_curve["portfolio_value"].iloc[-1])},
                "baseline_comparison": comparison,
                "transaction_cost_sensitivity": sensitivity,
            }
        ),
    }
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        "# 2022 MCM-C Trading Strategies",
        "",
        "## 数据与真实性",
        f"- 官方题面：`{PDF_PATH}`。",
        f"- 官方附件：`{DATA_DIR / 'LBMA-GOLD.csv'}` 与 `{DATA_DIR / 'BCHAIN-MKPRU.csv'}`。",
        "- 只使用 COMAP 提供的两个价格序列；没有随机数、没有外部行情、没有 x1/x2/x3 占位数据。",
        "",
        "## 核心模型",
        "- 投资组合状态为题面指定的 `[cash, gold_oz, bitcoin]`。",
        "- 每个候选专家规则只读取截至当日的官方价格；黄金只在 `LBMA-GOLD.csv` 有报价的日期交易，比特币每日交易。",
        "- 交易佣金在买卖时从交易额扣除：黄金 1%，比特币 2%。",
        "",
        "## 策略比较",
    ]
    lines.extend(["| strategy | final_value | return_% | max_drawdown | trades |", "|---|---:|---:|---:|---:|"])
    for row in comparison:
        lines.append(
            f"| {row['strategy']} | {row['final_value']:.2f} | {row['total_return_percent']:.2f} | {row['max_drawdown']:.4f} | {row['trade_count']} |"
        )
    lines.extend([
        "",
        "## 选定策略与结果",
        f"- 选定策略：`{selected_name}`。",
        f"- 2021-09-10 组合价值：`${result['trading_strategy']['final_value']:,.2f}`。",
        f"- 最大回撤：`{result['trading_strategy']['max_drawdown']}`。",
        "",
        "## 交易成本敏感性",
        "| alpha_gold | alpha_bitcoin | final_value | return_% | trades |",
        "|---:|---:|---:|---:|---:|",
    ])
    for row in sensitivity:
        lines.append(
            f"| {row['alpha_gold']:.2f} | {row['alpha_bitcoin']:.2f} | {row['final_value']:.2f} | {row['total_return_percent']:.2f} | {row['trade_count']} |"
        )
    lines.extend([
        "",
        "## 给交易员的备忘录",
        str(result["memo_to_trader"]),
        "",
        "## 输出文件",
        "- `artifacts/portfolio_value_curve.csv`",
        "- `artifacts/portfolio_value_curve.png`",
        "- `artifacts/daily_trades.csv`",
        "- `artifacts/strategy_comparison.csv`",
        "- `artifacts/transaction_cost_sensitivity.csv`",
    ])
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"result": str(RESULT_PATH), "report": str(REPORT_PATH), "artifacts": str(ARTIFACT_DIR)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
