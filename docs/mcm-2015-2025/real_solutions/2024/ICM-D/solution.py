from __future__ import annotations

import json
import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ARCHIVE_ROOT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
DATA_PATH = ARCHIVE_ROOT / "official_assets_extracted" / "2024" / "Data- Great Lakes Water Problem" / "2024_Problem_D_Great_Lakes.xlsx"
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
MONTH_NUMBER = {name: i for i, name in enumerate(MONTHS, start=1)}

LAKE_NAMES = ["Lake Superior", "Lake Michigan and Lake Huron", "Lake St. Clair", "Lake Erie", "Lake Ontario"]
FLOW_NAMES = ["St. Mary's River", "St. Clair River", "Detroit River", "Niagara River", "Ottawa River", "St. Lawrence River"]
CONTROL_FLOWS = {"Lake Superior": "St. Mary's River", "Lake Ontario": "St. Lawrence River"}
DOWNSTREAM_INFLOW = {"Lake Ontario": "Niagara River"}


def clean_float(value: object, digits: int = 6) -> float | None:
    if value is None:
        return None
    value = float(value)
    if math.isnan(value) or math.isinf(value):
        return None
    return round(value, digits)


def parse_sheet(path: Path, sheet_name: str) -> pd.DataFrame:
    raw = pd.read_excel(path, sheet_name=sheet_name, header=None)
    title = str(raw.iloc[0, 0])
    units = str(raw.iloc[1, 0]).replace("Units:", "").strip()
    kind = "level_m" if "Mean Water Level" in title else "flow_cms"
    table = raw.iloc[6:, :13].copy()
    table.columns = ["Year"] + MONTHS
    rows = []
    for _, row in table.iterrows():
        year = pd.to_numeric(row["Year"], errors="coerce")
        if pd.isna(year):
            continue
        for month in MONTHS:
            value = pd.to_numeric(row[month], errors="coerce")
            if pd.isna(value):
                continue
            rows.append(
                {
                    "component": sheet_name,
                    "kind": kind,
                    "units": units,
                    "year": int(year),
                    "month": MONTH_NUMBER[month],
                    "month_name": month,
                    "date": f"{int(year):04d}-{MONTH_NUMBER[month]:02d}-01",
                    "value": float(value),
                }
            )
    return pd.DataFrame(rows)


def read_official_data() -> pd.DataFrame:
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"missing official Great Lakes workbook: {DATA_PATH}")
    frames = [parse_sheet(DATA_PATH, sheet) for sheet in pd.ExcelFile(DATA_PATH).sheet_names]
    return pd.concat(frames, ignore_index=True)


def monthly_targets(levels: pd.DataFrame) -> tuple[pd.DataFrame, list[dict[str, object]]]:
    target_rows = []
    for (lake, month), group in levels.groupby(["component", "month"]):
        values = group["value"]
        target_rows.append(
            {
                "lake": lake,
                "month": int(month),
                "target_m": float(values.median()),
                "low_band_m": float(values.quantile(0.25)),
                "high_band_m": float(values.quantile(0.75)),
                "historical_min_m": float(values.min()),
                "historical_max_m": float(values.max()),
            }
        )
    targets = pd.DataFrame(target_rows).sort_values(["lake", "month"])
    summary = []
    for lake, part in targets.groupby("lake"):
        summary.append(
            {
                "lake": lake,
                "annual_target_mean_m": clean_float(part["target_m"].mean()),
                "mean_operating_band_width_m": clean_float((part["high_band_m"] - part["low_band_m"]).mean()),
                "seasonal_target_min_m": clean_float(part["target_m"].min()),
                "seasonal_target_max_m": clean_float(part["target_m"].max()),
            }
        )
    return targets, summary


def stakeholder_cost(level: float, low: float, target: float, high: float) -> dict[str, float]:
    flood = max(0.0, level - high)
    navigation = max(0.0, low - level)
    ecology = abs(level - target)
    total = 3.0 * flood + 2.0 * navigation + 1.0 * ecology
    return {"flood": flood, "navigation": navigation, "ecology": ecology, "total": total}


def attach_targets(levels: pd.DataFrame, targets: pd.DataFrame) -> pd.DataFrame:
    merged = levels.merge(targets, left_on=["component", "month"], right_on=["lake", "month"], how="left")
    costs = [stakeholder_cost(row.value, row.low_band_m, row.target_m, row.high_band_m) for row in merged.itertuples(index=False)]
    for key in ["flood", "navigation", "ecology", "total"]:
        merged[f"cost_{key}"] = [item[key] for item in costs]
    merged["deviation_m"] = merged["value"] - merged["target_m"]
    return merged


def fit_flow_response(levels_with_targets: pd.DataFrame, flows: pd.DataFrame, lake: str, outflow: str, inflow: str | None = None) -> dict[str, object]:
    lake_series = levels_with_targets[levels_with_targets["component"] == lake].sort_values(["year", "month"]).copy()
    lake_series["next_value"] = lake_series["value"].shift(-1)
    lake_series["next_delta_m"] = lake_series["next_value"] - lake_series["value"]
    lake_series = lake_series.dropna(subset=["next_delta_m"])
    flow_wide = flows.pivot_table(index=["year", "month"], columns="component", values="value", aggfunc="mean").reset_index()
    model_data = lake_series.merge(flow_wide, on=["year", "month"], how="left")
    cols = [outflow]
    if inflow is not None:
        cols.append(inflow)
    model_data = model_data.dropna(subset=cols + ["next_delta_m"])
    if len(model_data) < 24:
        return {"lake": lake, "outflow": outflow, "rows": int(len(model_data)), "status": "insufficient data"}
    x = model_data[cols].to_numpy(dtype=float)
    x_scaled = (x - x.mean(axis=0)) / x.std(axis=0)
    design = np.column_stack([np.ones(len(x_scaled)), x_scaled])
    coef, *_ = np.linalg.lstsq(design, model_data["next_delta_m"].to_numpy(dtype=float), rcond=None)
    pred = design @ coef
    rmse = math.sqrt(float(np.mean((pred - model_data["next_delta_m"].to_numpy(dtype=float)) ** 2)))
    return {
        "lake": lake,
        "outflow": outflow,
        "inflow": inflow,
        "rows": int(len(model_data)),
        "status": "fit",
        "rmse_m": clean_float(rmse),
        "intercept_m": clean_float(coef[0]),
        "standardized_coefficients": {col: clean_float(coef[i + 1]) for i, col in enumerate(cols)},
    }


def control_policy(levels_with_targets: pd.DataFrame, flows: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, object]]:
    rows = []
    flow_stats = flows.groupby(["component", "month"])["value"].agg(q10=lambda s: s.quantile(0.1), median="median", q90=lambda s: s.quantile(0.9)).reset_index()
    for lake, flow in CONTROL_FLOWS.items():
        lake_rows = levels_with_targets[levels_with_targets["component"] == lake].copy()
        stats = flow_stats[flow_stats["component"] == flow].rename(columns={"component": "flow_component"})
        lake_rows = lake_rows.merge(stats, on="month", how="left")
        for row in lake_rows.itertuples(index=False):
            if pd.isna(row.median):
                continue
            deviation = row.value - row.target_m
            recommended = row.median + deviation * 900.0
            recommended = min(max(recommended, row.q10), row.q90)
            rows.append(
                {
                    "lake": lake,
                    "control_flow": flow,
                    "year": int(row.year),
                    "month": int(row.month),
                    "date": row.date,
                    "level_m": float(row.value),
                    "target_m": float(row.target_m),
                    "deviation_m": float(deviation),
                    "historical_median_flow_cms": float(row.median),
                    "recommended_flow_cms": float(recommended),
                    "recommended_change_cms": float(recommended - row.median),
                    "q10_flow_cms": float(row.q10),
                    "q90_flow_cms": float(row.q90),
                }
            )
    policy = pd.DataFrame(rows)
    summary = []
    for lake, part in policy.groupby("lake"):
        summary.append(
            {
                "lake": lake,
                "control_flow": part["control_flow"].iloc[0],
                "mean_abs_level_deviation_m": clean_float(part["deviation_m"].abs().mean()),
                "mean_abs_recommended_change_cms": clean_float(part["recommended_change_cms"].abs().mean()),
                "max_recommended_change_cms": clean_float(part["recommended_change_cms"].abs().max()),
            }
        )
    return policy, {"rule": "monthly median flow plus 900 cms per meter above target, clipped to historical 10th-90th percentile by month", "summary": summary}


def evaluate_2017(levels_with_targets: pd.DataFrame, policy: pd.DataFrame) -> dict[str, object]:
    actual = levels_with_targets[levels_with_targets["year"] == 2017]
    total_actual_cost = float(actual["cost_total"].sum())
    high_risk = actual.sort_values("cost_total", ascending=False).head(10)
    policy_2017 = policy[policy["year"] == 2017]
    control_effort = float(policy_2017["recommended_change_cms"].abs().mean()) if not policy_2017.empty else 0.0
    return {
        "year": 2017,
        "actual_total_stakeholder_cost": clean_float(total_actual_cost),
        "mean_control_effort_cms": clean_float(control_effort),
        "highest_cost_months": [
            {
                "lake": row.component,
                "date": row.date,
                "level_m": clean_float(row.value),
                "target_m": clean_float(row.target_m),
                "deviation_m": clean_float(row.deviation_m),
                "cost_total": clean_float(row.cost_total),
            }
            for row in high_risk.itertuples(index=False)
        ],
        "interpretation": "The policy is evaluated as an advisory release rule, not a full hydraulic simulator; it flags months where controlled outflow should move toward historical operating bands.",
    }


def sensitivity_analysis(responses: list[dict[str, object]], policy: pd.DataFrame, levels_with_targets: pd.DataFrame) -> dict[str, object]:
    dam_rows = []
    for item in responses:
        if item.get("status") != "fit":
            continue
        outflow = item["outflow"]
        coef = item["standardized_coefficients"].get(outflow)
        dam_rows.append(
            {
                "lake": item["lake"],
                "control_flow": outflow,
                "rows": item["rows"],
                "rmse_m": item["rmse_m"],
                "standardized_outflow_sensitivity": coef,
                "interpretation": "negative means larger outflow tends to lower next-month lake level" if coef is not None and coef < 0 else "positive/weak response in fitted monthly data",
            }
        )
    lake_costs = levels_with_targets.groupby("component")["cost_total"].mean().sort_values(ascending=False)
    env_rows = []
    for lake, value in lake_costs.items():
        part = levels_with_targets[levels_with_targets["component"] == lake]
        env_rows.append(
            {
                "lake": lake,
                "mean_monthly_cost": clean_float(value),
                "high_water_months": int((part["value"] > part["high_band_m"]).sum()),
                "low_water_months": int((part["value"] < part["low_band_m"]).sum()),
                "max_abs_deviation_m": clean_float(part["deviation_m"].abs().max()),
            }
        )
    return {"dam_outflow_sensitivity": dam_rows, "environmental_condition_sensitivity": env_rows}


def lake_ontario_focus(levels_with_targets: pd.DataFrame, flows: pd.DataFrame, policy: pd.DataFrame) -> dict[str, object]:
    ontario = levels_with_targets[levels_with_targets["component"] == "Lake Ontario"].copy()
    high = int((ontario["value"] > ontario["high_band_m"]).sum())
    low = int((ontario["value"] < ontario["low_band_m"]).sum())
    worst = ontario.sort_values("cost_total", ascending=False).head(8)
    flow_wide = flows.pivot_table(index=["year", "month", "date"], columns="component", values="value", aggfunc="mean").reset_index()
    merged = ontario.merge(flow_wide, on=["year", "month", "date"], how="left")
    correlations = {}
    for col in ["Niagara River", "Ottawa River", "St. Lawrence River"]:
        part = merged[["deviation_m", col]].dropna()
        correlations[col] = clean_float(part["deviation_m"].corr(part[col])) if len(part) > 5 else None
    policy_ont = policy[policy["lake"] == "Lake Ontario"]
    return {
        "lake": "Lake Ontario",
        "records": int(len(ontario)),
        "high_water_months": high,
        "low_water_months": low,
        "mean_abs_deviation_m": clean_float(ontario["deviation_m"].abs().mean()),
        "correlation_with_flows": correlations,
        "average_recommended_st_lawrence_adjustment_cms": clean_float(policy_ont["recommended_change_cms"].abs().mean()) if not policy_ont.empty else None,
        "stakeholder_factors": [
            "shoreline flood risk when levels exceed the monthly high operating band",
            "navigation draft risk when levels fall below the monthly low operating band",
            "hydropower and downstream flow constraints at Moses-Saunders",
            "ecosystem and wetland exposure to prolonged high or low deviations",
            "Ottawa River inflow contribution to downstream Montreal/St. Lawrence flooding context",
        ],
        "highest_cost_months": [
            {
                "date": row.date,
                "level_m": clean_float(row.value),
                "target_m": clean_float(row.target_m),
                "deviation_m": clean_float(row.deviation_m),
                "cost_total": clean_float(row.cost_total),
            }
            for row in worst.itertuples(index=False)
        ],
    }


def write_artifacts(long_data: pd.DataFrame, targets: pd.DataFrame, policy: pd.DataFrame, result: dict[str, object]) -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    long_data.to_csv(ARTIFACT_DIR / "great_lakes_long_data.csv", index=False, encoding="utf-8-sig")
    targets.to_csv(ARTIFACT_DIR / "monthly_level_targets.csv", index=False, encoding="utf-8-sig")
    policy.to_csv(ARTIFACT_DIR / "control_policy_releases.csv", index=False, encoding="utf-8-sig")
    pd.DataFrame(result["sensitivity"]["dam_outflow_sensitivity"]).to_csv(ARTIFACT_DIR / "dam_outflow_sensitivity.csv", index=False, encoding="utf-8-sig")
    pd.DataFrame(result["lake_ontario_focus"]["highest_cost_months"]).to_csv(ARTIFACT_DIR / "lake_ontario_highest_cost_months.csv", index=False, encoding="utf-8-sig")

    levels = long_data[long_data["kind"] == "level_m"]
    plt.figure(figsize=(10, 5.8))
    for lake in LAKE_NAMES:
        part = levels[levels["component"] == lake].copy()
        if part.empty:
            continue
        annual = part.groupby("year")["value"].mean()
        plt.plot(annual.index, annual.values, label=lake)
    plt.title("Great Lakes annual mean water levels from official workbook")
    plt.xlabel("Year")
    plt.ylabel("Water level (m)")
    plt.legend(fontsize=7)
    plt.tight_layout()
    plt.savefig(ARTIFACT_DIR / "annual_mean_levels.png", dpi=180)
    plt.close()

    ontario = levels[levels["component"] == "Lake Ontario"].copy()
    ontario["date_dt"] = pd.to_datetime(ontario["date"])
    ont_targets = targets[targets["lake"] == "Lake Ontario"]
    ontario = ontario.merge(ont_targets[["month", "target_m", "low_band_m", "high_band_m"]], on="month", how="left")
    plt.figure(figsize=(10, 4.8))
    plt.plot(ontario["date_dt"], ontario["value"], label="actual", color="#245c8a")
    plt.plot(ontario["date_dt"], ontario["target_m"], label="monthly target", color="#3f7d20", linewidth=1)
    plt.fill_between(ontario["date_dt"], ontario["low_band_m"], ontario["high_band_m"], color="#9ccf8a", alpha=0.25, label="IQR operating band")
    plt.title("Lake Ontario level vs monthly target band")
    plt.xlabel("Date")
    plt.ylabel("Water level (m)")
    plt.legend()
    plt.tight_layout()
    plt.savefig(ARTIFACT_DIR / "lake_ontario_target_band.png", dpi=180)
    plt.close()


def write_report(result: dict[str, object]) -> None:
    lines = [
        "# 2024 ICM-D Great Lakes Water Problem 真实数据解法",
        "",
        "## 数据来源",
        "- 使用 COMAP 官方 `2024_Problem_D_Great_Lakes.xlsx` 的 11 个工作表。",
        "- 将湖泊水位和连接河流流量整理为月度长表；未生成随机水位或流量。",
        "",
        "## 数据规模",
        f"- 总有效月度记录：{result['data_source']['records']}。",
        f"- 湖泊水位记录：{result['data_source']['level_records']}；河流流量记录：{result['data_source']['flow_records']}。",
        "",
        "## Q1 最优水位",
        "- 以 2000-2023 历史月度中位数作为分月目标水位，以 25%-75% 分位数作为运行带。",
        "",
        "| lake | target mean | band width | seasonal min | seasonal max |",
        "|---|---:|---:|---:|---:|",
    ]
    for row in result["target_levels"]["lake_summary"]:
        lines.append(f"| {row['lake']} | {row['annual_target_mean_m']} | {row['mean_operating_band_width_m']} | {row['seasonal_target_min_m']} | {row['seasonal_target_max_m']} |")
    lines.extend([
        "",
        "## Q2 控制算法",
        f"- 规则：{result['control_policy']['rule']}",
        "",
        "| lake | control flow | mean abs level deviation | mean abs flow adjustment | max adjustment |",
        "|---|---|---:|---:|---:|",
    ])
    for row in result["control_policy"]["summary"]:
        lines.append(f"| {row['lake']} | {row['control_flow']} | {row['mean_abs_level_deviation_m']} | {row['mean_abs_recommended_change_cms']} | {row['max_recommended_change_cms']} |")
    lines.extend([
        "",
        "## Q3 2017 年控制评价和坝出流敏感性",
        f"- 2017 实际 stakeholder cost：{result['evaluation_2017']['actual_total_stakeholder_cost']}。",
        f"- 2017 平均建议控制幅度：{result['evaluation_2017']['mean_control_effort_cms']} cms。",
        "",
        "| lake | flow | rows | rmse | standardized sensitivity | interpretation |",
        "|---|---|---:|---:|---:|---|",
    ])
    for row in result["sensitivity"]["dam_outflow_sensitivity"]:
        lines.append(f"| {row['lake']} | {row['control_flow']} | {row['rows']} | {row['rmse_m']} | {row['standardized_outflow_sensitivity']} | {row['interpretation']} |")
    lines.extend([
        "",
        "## Q4 环境条件敏感性",
        "| lake | mean cost | high months | low months | max abs deviation |",
        "|---|---:|---:|---:|---:|",
    ])
    for row in result["sensitivity"]["environmental_condition_sensitivity"]:
        lines.append(f"| {row['lake']} | {row['mean_monthly_cost']} | {row['high_water_months']} | {row['low_water_months']} | {row['max_abs_deviation_m']} |")
    ont = result["lake_ontario_focus"]
    lines.extend([
        "",
        "## Q5 Lake Ontario 专项",
        f"- 高水位月份：{ont['high_water_months']}；低水位月份：{ont['low_water_months']}。",
        f"- 平均绝对偏离：{ont['mean_abs_deviation_m']} m。",
        f"- 与 Niagara/Ottawa/St. Lawrence 流量相关：{ont['correlation_with_flows']}。",
        "",
        "### Stakeholder factors",
    ])
    lines.extend([f"- {item}" for item in ont["stakeholder_factors"]])
    lines.extend([
        "",
        "## IJC 一页备忘录摘要",
        result["ijc_memo"],
        "",
        "## 输出文件",
        "- `artifacts/great_lakes_long_data.csv`：官方数据长表。",
        "- `artifacts/monthly_level_targets.csv`：分月目标水位带。",
        "- `artifacts/control_policy_releases.csv`：控制坝建议出流。",
        "- `artifacts/dam_outflow_sensitivity.csv`：坝出流敏感性。",
        "- `artifacts/lake_ontario_target_band.png`：Lake Ontario 水位与目标带。",
    ])
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    long_data = read_official_data()
    levels = long_data[long_data["kind"] == "level_m"].copy()
    flows = long_data[long_data["kind"] == "flow_cms"].copy()
    targets, target_summary = monthly_targets(levels)
    levels_with_targets = attach_targets(levels, targets)
    policy, policy_summary = control_policy(levels_with_targets, flows)
    responses = [
        fit_flow_response(levels_with_targets, flows, "Lake Superior", "St. Mary's River"),
        fit_flow_response(levels_with_targets, flows, "Lake Ontario", "St. Lawrence River", "Niagara River"),
    ]
    sensitivity = sensitivity_analysis(responses, policy, levels_with_targets)
    eval_2017 = evaluate_2017(levels_with_targets, policy)
    ontario = lake_ontario_focus(levels_with_targets, flows, policy)
    result: dict[str, object] = {
        "problem": "2024 ICM-D Great Lakes Water Problem",
        "data_source": {
            "type": "official_comap_xlsx",
            "root": str(DATA_PATH),
            "records": int(len(long_data)),
            "level_records": int(len(levels)),
            "flow_records": int(len(flows)),
            "sheets": sorted(long_data["component"].unique().tolist()),
        },
        "network_model": {
            "lakes": LAKE_NAMES,
            "connecting_flows": FLOW_NAMES,
            "control_dams": [
                {"lake": "Lake Superior", "controlled_outflow": "St. Mary's River", "control": "Soo Locks / Compensating Works"},
                {"lake": "Lake Ontario", "controlled_outflow": "St. Lawrence River", "control": "Moses-Saunders Dam"},
            ],
        },
        "target_levels": {"method": "monthly historical median with interquartile operating band", "lake_summary": target_summary},
        "control_policy": policy_summary,
        "evaluation_2017": eval_2017,
        "sensitivity": sensitivity,
        "lake_ontario_focus": ontario,
        "ijc_memo": "IJC should select a transparent monthly target-band controller: it uses official historical lake levels to define stakeholder operating bands, then adjusts the two controllable outflows toward those bands while clipping releases to historical monthly 10th-90th percentile flow ranges. The model is auditable, shows where 2017 levels were costly, and highlights Lake Ontario months where Moses-Saunders decisions should balance shoreline flooding, navigation drafts, hydropower, wetlands, and downstream Ottawa/St. Lawrence flood context.",
    }
    ROOT.mkdir(parents=True, exist_ok=True)
    write_artifacts(long_data, targets, policy, result)
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_report(result)
    print(json.dumps({"result": str(RESULT_PATH), "report": str(REPORT_PATH)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
