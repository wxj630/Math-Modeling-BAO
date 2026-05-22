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


ARCHIVE_ROOT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
DATA_ROOT = ARCHIVE_ROOT / "official_assets_extracted" / "2018" / "Problem Data- Energy Production"
PDF_PATH = ARCHIVE_ROOT / "official_assets_extracted" / "2018" / "Energy Production.pdf"
WORKBOOK_PATH = DATA_ROOT / "2018_MCM_Problem_C_Data.xlsx"
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"
REQUIRED_ARTIFACTS = [
    ARTIFACT_DIR / "state_energy_profiles_2009.csv",
    ARTIFACT_DIR / "renewable_share_history.csv",
    ARTIFACT_DIR / "renewable_share_forecast.csv",
    ARTIFACT_DIR / "compact_targets.csv",
    ARTIFACT_DIR / "renewable_share_trends.png",
]

STATE_NAMES = {"AZ": "Arizona", "CA": "California", "NM": "New Mexico", "TX": "Texas"}
METRICS = {
    "renewable_consumption": "RETCB",
    "renewable_production": "REPRB",
    "total_consumption": "TETCB",
    "total_production": "TEPRB",
    "population": "TPOPP",
    "hydro": "HYTCB",
    "wind": "WYTCB",
    "solar": "SOTCB",
    "geothermal": "GETCB",
    "biomass": "BMTCB",
}


def clean_float(value: object, digits: int = 6) -> float | None:
    if value is None:
        return None
    value = float(value)
    if math.isnan(value) or math.isinf(value):
        return None
    return round(value, digits)


def outputs_current() -> bool:
    outputs = [RESULT_PATH, REPORT_PATH, *REQUIRED_ARTIFACTS]
    if not all(path.exists() for path in outputs):
        return False
    newest_input = max(PDF_PATH.stat().st_mtime, WORKBOOK_PATH.stat().st_mtime)
    newest_source = Path(__file__).stat().st_mtime
    return all(path.stat().st_mtime >= max(newest_input, newest_source) for path in outputs)


def read_official_workbook() -> tuple[pd.DataFrame, pd.DataFrame]:
    missing = [str(path) for path in [PDF_PATH, WORKBOOK_PATH] if not path.exists()]
    if missing:
        raise FileNotFoundError("missing official COMAP Energy Production assets: " + ", ".join(missing))
    seseds = pd.read_excel(WORKBOOK_PATH, sheet_name="seseds")
    msncodes = pd.read_excel(WORKBOOK_PATH, sheet_name="msncodes")
    return seseds, msncodes


def build_metric_panel(seseds: pd.DataFrame) -> pd.DataFrame:
    subset = seseds[seseds["MSN"].isin(METRICS.values())].copy()
    wide = subset.pivot_table(index=["StateCode", "Year"], columns="MSN", values="Data", aggfunc="first").reset_index()
    for metric, code in METRICS.items():
        wide[metric] = pd.to_numeric(wide.get(code), errors="coerce")
    panel = wide[["StateCode", "Year", *METRICS.keys()]].rename(columns={"StateCode": "state", "Year": "year"})
    panel["state_name"] = panel["state"].map(STATE_NAMES)
    panel["renewable_consumption_share"] = np.where(panel["total_consumption"] > 0, panel["renewable_consumption"] / panel["total_consumption"], np.nan)
    panel["renewable_production_share"] = np.where(panel["total_production"] > 0, panel["renewable_production"] / panel["total_production"], np.nan)
    panel["energy_consumption_per_capita_mmbtu"] = np.where(panel["population"] > 0, panel["total_consumption"] / panel["population"], np.nan)
    panel["renewable_consumption_per_capita_mmbtu"] = np.where(panel["population"] > 0, panel["renewable_consumption"] / panel["population"], np.nan)
    panel["nonhydro_renewable_consumption"] = panel[["wind", "solar", "geothermal", "biomass"]].sum(axis=1, min_count=1)
    panel["nonhydro_renewable_share"] = np.where(panel["total_consumption"] > 0, panel["nonhydro_renewable_consumption"] / panel["total_consumption"], np.nan)
    return panel.sort_values(["state", "year"]).reset_index(drop=True)


def state_profiles(panel: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, object]]:
    profiles = panel[panel["year"] == 2009].copy()
    profiles["clean_profile_score"] = (
        0.45 * profiles["renewable_consumption_share"].rank(pct=True)
        + 0.25 * profiles["nonhydro_renewable_share"].rank(pct=True)
        + 0.20 * profiles["renewable_consumption_per_capita_mmbtu"].rank(pct=True)
        - 0.10 * profiles["energy_consumption_per_capita_mmbtu"].rank(pct=True)
    )
    profiles = profiles.sort_values("clean_profile_score", ascending=False)
    return profiles, {
        "profile_year": 2009,
        "criteria": "45% renewable consumption share, 25% non-hydro renewable share, 20% renewable per capita, minus 10% total energy intensity rank.",
        "state_profiles": [
            {
                "state": row["state"],
                "state_name": row["state_name"],
                "renewable_consumption_share": clean_float(row["renewable_consumption_share"]),
                "renewable_production_share": clean_float(row["renewable_production_share"]),
                "nonhydro_renewable_share": clean_float(row["nonhydro_renewable_share"]),
                "energy_consumption_per_capita_mmbtu": clean_float(row["energy_consumption_per_capita_mmbtu"]),
                "clean_profile_score": clean_float(row["clean_profile_score"]),
            }
            for _, row in profiles.iterrows()
        ],
    }


def evolution(panel: pd.DataFrame) -> dict[str, object]:
    rows = []
    for state, state_df in panel.groupby("state"):
        recent = state_df[state_df["year"] >= 1990].dropna(subset=["renewable_consumption_share"])
        model = LinearRegression().fit(recent[["year"]], recent["renewable_consumption_share"])
        rows.append(
            {
                "state": state,
                "renewable_share_1960": clean_float(state_df.loc[state_df["year"].eq(1960), "renewable_consumption_share"].iloc[0]),
                "renewable_share_2009": clean_float(state_df.loc[state_df["year"].eq(2009), "renewable_consumption_share"].iloc[0]),
                "change_1960_2009": clean_float(
                    state_df.loc[state_df["year"].eq(2009), "renewable_consumption_share"].iloc[0]
                    - state_df.loc[state_df["year"].eq(1960), "renewable_consumption_share"].iloc[0]
                ),
                "recent_slope_per_year": clean_float(model.coef_[0]),
                "interpretation": "improving" if model.coef_[0] > 0 else "declining",
            }
        )
    return {"method": "OLS slope on 1990-2009 official renewable consumption share by state.", "state_trends": rows}


def forecast(panel: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, object]]:
    rows = []
    for state, state_df in panel.groupby("state"):
        recent = state_df[state_df["year"] >= 1990].dropna(subset=["renewable_consumption_share", "energy_consumption_per_capita_mmbtu"])
        share_model = LinearRegression().fit(recent[["year"]], recent["renewable_consumption_share"])
        intensity_model = LinearRegression().fit(recent[["year"]], recent["energy_consumption_per_capita_mmbtu"])
        for year in [2025, 2050]:
            share = float(share_model.predict(pd.DataFrame({"year": [year]}))[0])
            intensity = float(intensity_model.predict(pd.DataFrame({"year": [year]}))[0])
            rows.append(
                {
                    "state": state,
                    "year": year,
                    "baseline_renewable_consumption_share": clean_float(max(0.0, min(1.0, share))),
                    "baseline_energy_consumption_per_capita_mmbtu": clean_float(max(0.0, intensity)),
                    "model": "linear trend fit on 1990-2009 official SEDS variables",
                }
            )
    forecast_table = pd.DataFrame(rows)
    return forecast_table, {"method": "No-policy baseline linear trend using official 1990-2009 state SEDS shares.", "forecast_rows": forecast_table.to_dict(orient="records")}


def compact_targets(profile_table: pd.DataFrame, forecast_table: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, object]]:
    best_2009 = float(profile_table["renewable_consumption_share"].max())
    rows = []
    for year in [2025, 2050]:
        baseline_median = float(forecast_table[forecast_table["year"] == year]["baseline_renewable_consumption_share"].median())
        compact_goal = max(best_2009, baseline_median + (0.03 if year == 2025 else 0.08))
        for state in sorted(STATE_NAMES):
            baseline = float(
                forecast_table[(forecast_table["year"] == year) & (forecast_table["state"] == state)]["baseline_renewable_consumption_share"].iloc[0]
            )
            rows.append(
                {
                    "state": state,
                    "year": year,
                    "baseline_renewable_share": clean_float(baseline),
                    "compact_target_share": clean_float(min(0.75, compact_goal)),
                    "required_gap": clean_float(max(0.0, min(0.75, compact_goal) - baseline)),
                }
            )
    targets = pd.DataFrame(rows)
    return targets, {
        "target_rule": "Set compact targets at least as high as the 2009 best state and above the projected median baseline.",
        "targets": targets.to_dict(orient="records"),
    }


def actions() -> dict[str, object]:
    return {
        "actions": [
            {
                "action": "Create a four-state renewable portfolio standard with tradable clean-energy credits.",
                "model_link": "Raises renewable_consumption_share toward the compact target while allowing state-specific resource mixes.",
            },
            {
                "action": "Build transmission and storage projects that connect Texas wind, California solar, and Arizona/New Mexico solar resources.",
                "model_link": "Addresses geography differences visible in the official state profiles and reduces curtailment risk.",
            },
            {
                "action": "Pair demand efficiency with electrification so total energy per capita falls while renewable electricity grows.",
                "model_link": "Targets energy_consumption_per_capita_mmbtu as well as renewable share.",
            },
        ]
    }


def write_artifacts(panel: pd.DataFrame, profiles: pd.DataFrame, forecast_table: pd.DataFrame, targets: pd.DataFrame) -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    profiles.to_csv(ARTIFACT_DIR / "state_energy_profiles_2009.csv", index=False)
    panel[["state", "year", "renewable_consumption_share", "renewable_production_share", "nonhydro_renewable_share"]].to_csv(
        ARTIFACT_DIR / "renewable_share_history.csv", index=False
    )
    forecast_table.to_csv(ARTIFACT_DIR / "renewable_share_forecast.csv", index=False)
    targets.to_csv(ARTIFACT_DIR / "compact_targets.csv", index=False)

    plt.figure(figsize=(9, 5.2))
    for state, state_df in panel.groupby("state"):
        plt.plot(state_df["year"], 100 * state_df["renewable_consumption_share"], label=state)
    plt.title("Official SEDS renewable energy consumption share")
    plt.xlabel("year")
    plt.ylabel("renewable share of total consumption (%)")
    plt.legend()
    plt.tight_layout()
    plt.savefig(ARTIFACT_DIR / "renewable_share_trends.png", dpi=180)
    plt.close()


def write_report(result: dict[str, object]) -> None:
    lines = [
        "# 2018 MCM-C Energy Production：官方 SEDS Workbook 实验报告",
        "",
        "## 数据真实性",
        "",
        f"- 官方题面：`{result['data_source']['source_pdf']}`。",
        f"- 官方 workbook：`{result['data_source']['workbook']}`。",
        f"- 行数：`{result['data_source']['rows']}`。",
        "- 本解法只读取 COMAP 官方 workbook，不生成随机 `x1/x2/x3` 数据。",
        "",
        "## Part I：四州能源画像和演化",
        "",
        f"- 画像年份：{result['energy_profiles']['profile_year']}。",
        f"- 最佳 2009 profile：{result['best_profile_2009']['state']}，criteria={result['energy_profiles']['criteria']}",
        "",
        "## Part I-D：2025/2050 无政策预测",
        "",
        f"- 方法：{result['baseline_forecast']['method']}",
        "",
        "## Part II：Compact targets 与行动",
        "",
        f"- 目标规则：{result['compact_targets']['target_rule']}",
        "",
        "## Governors memo",
        "",
        result["governors_memo"],
    ]
    REPORT_PATH.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    if outputs_current():
        print(json.dumps({"cached": True, "result": str(RESULT_PATH), "report": str(REPORT_PATH)}, ensure_ascii=False, indent=2))
        return
    seseds, msncodes = read_official_workbook()
    panel = build_metric_panel(seseds)
    profiles, profile_result = state_profiles(panel)
    evolution_result = evolution(panel)
    forecast_table, forecast_result = forecast(panel)
    target_table, target_result = compact_targets(profiles, forecast_table)
    action_result = actions()
    write_artifacts(panel, profiles, forecast_table, target_table)
    best = profile_result["state_profiles"][0]
    result = {
        "data_source": {
            "type": "official_comap_xlsx",
            "root": str(DATA_ROOT),
            "source_pdf": str(PDF_PATH),
            "workbook": str(WORKBOOK_PATH),
            "rows": {"seseds": int(len(seseds)), "msncodes": int(len(msncodes))},
            "states": sorted(panel["state"].dropna().unique().tolist()),
            "years": [int(panel["year"].min()), int(panel["year"].max())],
        },
        "energy_profiles": profile_result,
        "evolution_model": evolution_result,
        "best_profile_2009": best,
        "baseline_forecast": forecast_result,
        "compact_targets": target_result,
        "compact_actions": action_result,
        "governors_memo": (
            "To the Governors of Arizona, California, New Mexico, and Texas: the official SEDS workbook shows that the four states start from different energy profiles, "
            "so the compact should set a shared renewable-share target while allowing different resource mixes. Use the 2009 best-profile benchmark as the minimum political target, "
            "then require each state to close its projected 2025 and 2050 gaps with renewable portfolio standards, transmission/storage cooperation, and demand efficiency."
        ),
    }
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_report(result)
    print(json.dumps({"result": str(RESULT_PATH), "report": str(REPORT_PATH), "artifacts": str(ARTIFACT_DIR)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
