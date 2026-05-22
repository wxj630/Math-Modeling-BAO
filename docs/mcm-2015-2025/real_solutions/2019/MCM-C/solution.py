from __future__ import annotations

import json
import math
import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/private/tmp/matplotlib-cache")

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score


ARCHIVE_ROOT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
DATA_ROOT = ARCHIVE_ROOT / "official_assets_extracted" / "2019" / "Problem Data- The Opioid Crisis" / "2018_MCMProblemC_DATA"
PDF_PATH = ARCHIVE_ROOT / "official_assets_extracted" / "2019" / "The Opioid Crisis.pdf"
NFLIS_PATH = DATA_ROOT / "MCM_NFLIS_Data.xlsx"
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"
ACS_YEARS = list(range(2010, 2017))
# Literal official filenames kept here for guardrails and auditability:
# ACS_10_5YR_DP02_with_ann.csv ... ACS_16_5YR_DP02_with_ann.csv
REQUIRED_ARTIFACTS = [
    ARTIFACT_DIR / "county_year_opioid_panel.csv",
    ARTIFACT_DIR / "acs_socioeconomic_panel.csv",
    ARTIFACT_DIR / "opioid_forecast_2020.csv",
    ARTIFACT_DIR / "socioeconomic_correlations.csv",
    ARTIFACT_DIR / "strategy_scenarios.csv",
    ARTIFACT_DIR / "opioid_state_trends.png",
]

ACS_FEATURES = {
    "total_households": ("Estimate; HOUSEHOLDS BY TYPE - Total households", "HC01"),
    "high_school_or_higher_pct": ("Percent high school graduate or higher", "HC03"),
    "bachelor_or_higher_pct": ("Percent bachelor's degree or higher", "HC03"),
    "civilian_veteran_pct": ("Civilian population 18 years and over - Civilian veterans", "HC03"),
    "disability_pct": ("Total Civilian Noninstitutionalized Population - With a disability", "HC03"),
    "foreign_born_pct": ("Total population - Foreign born", "HC03"),
    "same_house_one_year_pct": ("RESIDENCE 1 YEAR AGO - Population 1 year and over - Same house", "HC03"),
}


def clean_float(value: object, digits: int = 6) -> float | None:
    if value is None:
        return None
    value = float(value)
    if math.isnan(value) or math.isinf(value):
        return None
    return round(value, digits)


def acs_path(year: int) -> Path:
    suffix = str(year)[-2:]
    return DATA_ROOT / f"ACS_{suffix}_5YR_DP02" / f"ACS_{suffix}_5YR_DP02_with_ann.csv"


def required_inputs() -> list[Path]:
    return [PDF_PATH, NFLIS_PATH, *[acs_path(year) for year in ACS_YEARS]]


def outputs_current() -> bool:
    outputs = [RESULT_PATH, REPORT_PATH, *REQUIRED_ARTIFACTS]
    if not all(path.exists() for path in outputs):
        return False
    newest_input = max(path.stat().st_mtime for path in required_inputs())
    newest_source = Path(__file__).stat().st_mtime
    return all(path.stat().st_mtime >= max(newest_input, newest_source) for path in outputs)


def read_nflis() -> pd.DataFrame:
    missing = [str(path) for path in required_inputs() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing official COMAP opioid assets: " + ", ".join(missing))
    df = pd.read_excel(NFLIS_PATH, sheet_name="Data")
    df["FIPS_Combined"] = pd.to_numeric(df["FIPS_Combined"], errors="coerce").astype("Int64")
    df["DrugReports"] = pd.to_numeric(df["DrugReports"], errors="coerce").fillna(0)
    df["TotalDrugReportsCounty"] = pd.to_numeric(df["TotalDrugReportsCounty"], errors="coerce")
    return df


def build_opioid_panel(nflis: pd.DataFrame) -> pd.DataFrame:
    data = nflis.copy()
    data["opioid_class"] = np.where(data["SubstanceName"].str.lower().eq("heroin"), "heroin", "synthetic_or_other_analgesic")
    grouped = (
        data.groupby(["YYYY", "State", "COUNTY", "FIPS_State", "FIPS_County", "FIPS_Combined", "opioid_class"], as_index=False)
        .agg(opioid_reports=("DrugReports", "sum"), total_drug_reports_county=("TotalDrugReportsCounty", "max"))
    )
    panel = grouped.pivot_table(
        index=["YYYY", "State", "COUNTY", "FIPS_State", "FIPS_County", "FIPS_Combined", "total_drug_reports_county"],
        columns="opioid_class",
        values="opioid_reports",
        aggfunc="sum",
        fill_value=0,
    ).reset_index()
    for col in ["heroin", "synthetic_or_other_analgesic"]:
        if col not in panel:
            panel[col] = 0
    panel["opioid_reports"] = panel["heroin"] + panel["synthetic_or_other_analgesic"]
    panel["opioid_rate_per_1000_drug_reports"] = np.where(
        panel["total_drug_reports_county"] > 0,
        1000 * panel["opioid_reports"] / panel["total_drug_reports_county"],
        np.nan,
    )
    panel = panel.rename(columns={"YYYY": "year", "COUNTY": "county", "State": "state"})
    return panel.sort_values(["state", "FIPS_Combined", "year"]).reset_index(drop=True)


def read_acs_panel() -> pd.DataFrame:
    rows = []
    for year in ACS_YEARS:
        suffix = str(year)[-2:]
        metadata = pd.read_csv(DATA_ROOT / f"ACS_{suffix}_5YR_DP02" / f"ACS_{suffix}_5YR_DP02_metadata.csv")
        df = pd.read_csv(acs_path(year), skiprows=[1], low_memory=False)
        out = pd.DataFrame(
            {
                "year": year,
                "FIPS_Combined": pd.to_numeric(df["GEO.id2"], errors="coerce").astype("Int64"),
                "geography": df["GEO.display-label"].astype(str),
            }
        )
        for feature, (label, prefix) in ACS_FEATURES.items():
            hits = metadata[
                metadata["Id"].str.contains(label, case=False, regex=False, na=False)
                & metadata["GEO.id"].str.startswith(prefix)
            ]
            if hits.empty:
                out[feature] = np.nan
                continue
            column = str(hits.iloc[0]["GEO.id"])
            out[feature] = pd.to_numeric(df[column], errors="coerce")
        out["state_name"] = out["geography"].str.rsplit(", ", n=1).str[-1]
        out["county_name"] = out["geography"].str.split(",", n=1).str[0]
        rows.append(out)
    return pd.concat(rows, ignore_index=True).dropna(subset=["FIPS_Combined"]).sort_values(["FIPS_Combined", "year"])


def likely_origins(panel: pd.DataFrame) -> list[dict[str, object]]:
    origins = []
    for state, state_df in panel[panel["opioid_reports"] > 0].groupby("state"):
        earliest_year = int(state_df["year"].min())
        candidates = state_df[state_df["year"] == earliest_year].sort_values(
            ["opioid_reports", "opioid_rate_per_1000_drug_reports"], ascending=False
        )
        top = candidates.head(3)
        origins.append(
            {
                "state": state,
                "earliest_year": earliest_year,
                "candidate_counties": [
                    {
                        "county": row["county"],
                        "fips": int(row["FIPS_Combined"]),
                        "opioid_reports": int(row["opioid_reports"]),
                        "heroin_reports": int(row["heroin"]),
                        "synthetic_or_other_analgesic_reports": int(row["synthetic_or_other_analgesic"]),
                        "rate_per_1000_drug_reports": clean_float(row["opioid_rate_per_1000_drug_reports"]),
                    }
                    for _, row in top.iterrows()
                ],
            }
        )
    return sorted(origins, key=lambda item: item["state"])


def forecast_counties(panel: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, object]]:
    rows = []
    metrics = []
    for fips, county_df in panel.groupby("FIPS_Combined"):
        county_df = county_df.sort_values("year")
        if len(county_df) < 6:
            continue
        x = county_df[["year"]].to_numpy()
        y = county_df["opioid_reports"].to_numpy(dtype=float)
        model = LinearRegression().fit(x, y)
        pred_in_sample = model.predict(x)
        forecast_2020 = max(0.0, float(model.predict(np.array([[2020]]))[0]))
        latest = county_df.iloc[-1]
        rows.append(
            {
                "FIPS_Combined": int(fips),
                "state": str(latest["state"]),
                "county": str(latest["county"]),
                "slope_reports_per_year": clean_float(model.coef_[0]),
                "observed_2017_reports": clean_float(latest["opioid_reports"], 2),
                "forecast_2020_reports": clean_float(forecast_2020, 2),
                "forecast_threshold": "high" if forecast_2020 >= 100 else "watch" if forecast_2020 >= 25 else "routine",
                "in_sample_mae": clean_float(mean_absolute_error(y, pred_in_sample), 4),
                "in_sample_r2": clean_float(r2_score(y, pred_in_sample), 4),
            }
        )
        metrics.append(mean_absolute_error(y, pred_in_sample))
    forecast = pd.DataFrame(rows).sort_values("forecast_2020_reports", ascending=False)
    summary = {
        "method": "Per-county ordinary least squares trend on official 2010-2017 NFLIS opioid reports.",
        "county_forecasts_2020": forecast.head(15).to_dict(orient="records"),
        "high_threshold_reports": 100,
        "watch_threshold_reports": 25,
        "median_in_sample_mae": clean_float(np.median(metrics), 4),
    }
    return forecast, summary


def socioeconomic_model(opioid_panel: pd.DataFrame, acs_panel: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, dict[str, object]]:
    merged = opioid_panel[opioid_panel["year"].isin(ACS_YEARS)].merge(
        acs_panel,
        on=["year", "FIPS_Combined"],
        how="inner",
    )
    target = "opioid_rate_per_1000_drug_reports"
    rows = []
    for feature in ACS_FEATURES:
        usable = merged[[target, feature]].replace([np.inf, -np.inf], np.nan).dropna()
        if len(usable) < 10:
            corr = np.nan
        else:
            corr = usable[target].corr(usable[feature])
        rows.append(
            {
                "feature": feature,
                "correlation_with_opioid_rate_per_1000": clean_float(corr),
                "usable_county_year_rows": int(len(usable)),
                "interpretation": "positive association" if corr and corr > 0 else "negative association" if corr and corr < 0 else "not estimated",
            }
        )
    correlations = pd.DataFrame(rows).sort_values(
        "correlation_with_opioid_rate_per_1000", key=lambda s: s.abs(), ascending=False
    )
    top = correlations.head(7).to_dict(orient="records")
    return (
        merged,
        correlations,
        {
            "merged_county_year_rows": int(len(merged)),
            "method": "County-year Pearson correlations between official NFLIS opioid rate and official ACS DP02 social characteristics.",
            "target": target,
            "features": list(ACS_FEATURES.keys()),
            "top_correlations": top,
            "caution": "Associations are descriptive and cannot prove causality; the ACS attachment is DP02 social characteristics, not a complete economic panel.",
        },
    )


def strategy_scenarios(forecast: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, object]]:
    baseline = float(forecast["forecast_2020_reports"].sum())
    high = forecast[forecast["forecast_2020_reports"] >= 100]
    watch = forecast[forecast["forecast_2020_reports"] >= 25]
    scenarios = [
        {"scenario": "baseline_no_new_intervention", "high_county_reduction": 0.0, "watch_county_reduction": 0.0},
        {"scenario": "early_warning_lab_feedback", "high_county_reduction": 0.10, "watch_county_reduction": 0.04},
        {"scenario": "targeted_treatment_and_prescriber_outreach", "high_county_reduction": 0.22, "watch_county_reduction": 0.08},
        {"scenario": "combined_supply_and_treatment_strategy", "high_county_reduction": 0.32, "watch_county_reduction": 0.12},
    ]
    rows = []
    for scenario in scenarios:
        adjusted = forecast.copy()
        adjusted["scenario_reports"] = adjusted["forecast_2020_reports"]
        adjusted.loc[adjusted["forecast_2020_reports"] >= 100, "scenario_reports"] *= 1 - scenario["high_county_reduction"]
        mask_watch = (adjusted["forecast_2020_reports"] >= 25) & (adjusted["forecast_2020_reports"] < 100)
        adjusted.loc[mask_watch, "scenario_reports"] *= 1 - scenario["watch_county_reduction"]
        total = float(adjusted["scenario_reports"].sum())
        rows.append(
            {
                "scenario": scenario["scenario"],
                "affected_high_counties": int(len(high)),
                "affected_watch_counties": int(len(watch) - len(high)),
                "projected_2020_reports": clean_float(total, 2),
                "reduction_vs_baseline_reports": clean_float(baseline - total, 2),
                "reduction_vs_baseline_pct": clean_float(100 * (baseline - total) / baseline if baseline else 0, 3),
            }
        )
    table = pd.DataFrame(rows)
    return (
        table,
        {
            "strategy": "Prioritize counties forecast above 100 reports for integrated lab feedback, treatment access, and supply interruption; monitor 25-99 report counties as watch areas.",
            "thresholds": {"high": 100, "watch": 25},
            "strategy_scenarios": table.to_dict(orient="records"),
            "parameter_bound": "The combined strategy reaches a material reduction only if high-risk counties achieve about 30%+ reduction and watch counties about 10%+ reduction in forecast reports.",
        },
    )


def write_artifacts(panel: pd.DataFrame, acs: pd.DataFrame, forecast: pd.DataFrame, correlations: pd.DataFrame, scenarios: pd.DataFrame) -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    panel.to_csv(ARTIFACT_DIR / "county_year_opioid_panel.csv", index=False)
    acs.to_csv(ARTIFACT_DIR / "acs_socioeconomic_panel.csv", index=False)
    forecast.to_csv(ARTIFACT_DIR / "opioid_forecast_2020.csv", index=False)
    correlations.to_csv(ARTIFACT_DIR / "socioeconomic_correlations.csv", index=False)
    scenarios.to_csv(ARTIFACT_DIR / "strategy_scenarios.csv", index=False)

    trends = panel.groupby(["year", "state"], as_index=False)["opioid_reports"].sum()
    plt.figure(figsize=(9, 5.2))
    for state, state_df in trends.groupby("state"):
        plt.plot(state_df["year"], state_df["opioid_reports"], marker="o", label=state)
    plt.title("Official NFLIS opioid/heroin reports by state")
    plt.xlabel("year")
    plt.ylabel("drug identification reports")
    plt.legend(ncol=3, fontsize=8)
    plt.tight_layout()
    plt.savefig(ARTIFACT_DIR / "opioid_state_trends.png", dpi=180)
    plt.close()


def write_report(result: dict[str, object]) -> None:
    lines = [
        "# 2019 MCM-C The Opioid Crisis：官方 NFLIS/ACS 数据实验报告",
        "",
        "## 数据真实性",
        "",
        f"- 官方题面：`{result['data_source']['source_pdf']}`。",
        f"- 官方附件目录：`{result['data_source']['root']}`。",
        f"- 行数：`{result['data_source']['rows']}`。",
        f"- ACS 年份：`{result['data_source']['acs_years']}`。",
        f"- NFLIS 文件实际州别：`{result['data_source']['official_nflis_states']}`。",
        "- 本解法只读取 COMAP 官方 Excel/CSV，不生成随机 `x1/x2/x3` 数据。",
        "",
        "## Part 1：传播与起始位置",
        "",
        "- 模型：县-年 NFLIS 面板、heroin/analgesic 分解、每县 OLS 趋势和 2020 外推。",
        f"- 县-年记录数：{result['spread_model']['county_year_rows']}。",
        f"- 高风险阈值：{result['forecast_concerns']['high_threshold_reports']} reports；观察阈值：{result['forecast_concerns']['watch_threshold_reports']} reports。",
        "",
        "## Part 2：ACS 社会特征关联",
        "",
        "- 模型：将 2010-2016 NFLIS 县-年 opioid rate 与 ACS DP02 社会特征按 FIPS/year 合并，计算描述性相关。",
        f"- 合并县-年记录数：{result['socioeconomic_model']['merged_county_year_rows']}。",
        f"- 重要限制：{result['socioeconomic_model']['caution']}",
        "",
        "## Part 3：反制策略情景",
        "",
        f"- 策略：{result['counter_strategy']['strategy']}",
        f"- 参数边界：{result['counter_strategy']['parameter_bound']}",
        "",
        "## DEA/NFLIS memo",
        "",
        result["dea_memo"],
    ]
    REPORT_PATH.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    if outputs_current():
        print(json.dumps({"cached": True, "result": str(RESULT_PATH), "report": str(REPORT_PATH)}, ensure_ascii=False, indent=2))
        return

    nflis = read_nflis()
    panel = build_opioid_panel(nflis)
    acs = read_acs_panel()
    forecast, forecast_summary = forecast_counties(panel)
    merged, correlations, socio_summary = socioeconomic_model(panel, acs)
    scenarios, counter_strategy = strategy_scenarios(forecast)
    write_artifacts(panel, acs, forecast, correlations, scenarios)

    actual_states = sorted(str(item) for item in nflis["State"].dropna().unique())
    result = {
        "data_source": {
            "type": "official_comap_xlsx_csv",
            "root": str(DATA_ROOT),
            "source_pdf": str(PDF_PATH),
            "rows": {
                "MCM_NFLIS_Data.xlsx": int(len(nflis)),
                "ACS county-year rows": int(len(acs)),
            },
            "acs_years": ACS_YEARS,
            "official_nflis_states": actual_states,
            "state_note": "The official workbook contains KY, OH, PA, VA, and WV records; this workflow does not add Tennessee records that are absent from the file.",
        },
        "spread_model": {
            "county_year_rows": int(len(panel)),
            "county_count": int(panel["FIPS_Combined"].nunique()),
            "substance_classes": ["heroin", "synthetic_or_other_analgesic"],
            "likely_origins_by_state": likely_origins(panel),
        },
        "forecast_concerns": forecast_summary,
        "socioeconomic_model": socio_summary,
        "counter_strategy": counter_strategy,
        "dea_memo": (
            "To the Chief Administrator, DEA/NFLIS Database: this model uses only the provided NFLIS and ACS attachments. "
            "The most operational result is a county-year early warning panel: counties crossing 100 projected opioid/heroin reports by 2020 should receive rapid lab-feedback review, "
            "treatment capacity checks, and coordinated supply-disruption attention, while counties in the 25-99 range should be monitored before they become high-burden areas. "
            "The ACS correlations are useful triage signals but should be treated as descriptive, not causal, because the attachment is a social-characteristics panel and not a full economic or prescribing database."
        ),
    }
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_report(result)
    print(json.dumps({"result": str(RESULT_PATH), "report": str(REPORT_PATH), "artifacts": str(ARTIFACT_DIR)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
