from __future__ import annotations

import json
import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


ARCHIVE_ROOT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
DATA_PATH = (
    ARCHIVE_ROOT
    / "official_assets_extracted"
    / "2023"
    / "Problem Data- Understanding Used Sailboat Prices"
    / "2023_MCM_Problem_Y_Data.xlsx"
)
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"
REFERENCE_YEAR = 2020
NUMERIC_FEATURES = ["length_ft", "age_years", "variant_observation_count"]
CATEGORICAL_FEATURES = ["hull_type", "make", "variant", "geographic_region", "country_region_state"]
MODEL_FEATURES = NUMERIC_FEATURES + CATEGORICAL_FEATURES

# Current Hong Kong listing comparables used only for Q3 scenario analysis.
# The COMAP workbook remains the mandatory training data source.
HK_COMPARABLES = [
    {
        "make": "Beneteau",
        "variant": "Sense 43",
        "hull_type": "monohull",
        "length_ft": 43.0,
        "year": 2013,
        "listing_price_usd": 230000.0,
        "source": "boats.com",
        "source_url": "https://www.boats.com/sailing-boats/2013-beneteau-sense-43-9833068/",
        "source_note": "Hong Kong listing page inspected from boats.com search result.",
    },
    {
        "make": "Beneteau",
        "variant": "Sense 51",
        "hull_type": "monohull",
        "length_ft": 51.0,
        "year": 2017,
        "listing_price_usd": 445000.0,
        "source": "boats.com",
        "source_url": "https://www.boats.com/sailing-boats/2013-beneteau-sense-43-9833068/",
        "source_note": "Similar Hong Kong listing shown on boats.com Beneteau Sense 43 page.",
    },
    {
        "make": "Jeanneau",
        "variant": "Sun Odyssey 389",
        "hull_type": "monohull",
        "length_ft": 38.9,
        "year": 2019,
        "listing_price_usd": 190000.0,
        "source": "boats.com",
        "source_url": "https://www.boats.com/sailing-boats/2013-beneteau-sense-43-9833068/",
        "source_note": "Similar Hong Kong listing shown on boats.com Beneteau Sense 43 page.",
    },
    {
        "make": "Lagoon",
        "variant": "46",
        "hull_type": "catamaran",
        "length_ft": 46.0,
        "year": 2020,
        "listing_price_usd": 973092.0,
        "source": "boats.com",
        "source_url": "https://www.boats.com/boats-for-sale/?condition=used&country=hong-kong&class=sail-catamaran",
        "source_note": "Hong Kong used catamaran listing in boats.com search result.",
    },
    {
        "make": "Lagoon",
        "variant": "42",
        "hull_type": "catamaran",
        "length_ft": 42.0,
        "year": 2022,
        "listing_price_usd": 904919.0,
        "source": "boats.com",
        "source_url": "https://www.boats.com/boats-for-sale/?condition=used&country=hong-kong&class=sail-catamaran",
        "source_note": "Hong Kong used catamaran listing in boats.com search result.",
    },
    {
        "make": "Lagoon",
        "variant": "450",
        "hull_type": "catamaran",
        "length_ft": 45.0,
        "year": 2014,
        "listing_price_usd": 745426.0,
        "source": "boats.com",
        "source_url": "https://www.boats.com/boats-for-sale/?condition=used&country=hong-kong&class=sail-catamaran",
        "source_note": "Hong Kong used catamaran listing in boats.com search result.",
    },
    {
        "make": "Fountaine Pajot",
        "variant": "Saba 50",
        "hull_type": "catamaran",
        "length_ft": 50.0,
        "year": 2016,
        "listing_price_usd": 1242844.0,
        "source": "boats.com",
        "source_url": "https://www.boats.com/boats-for-sale/?condition=used&country=hong-kong&class=sail-catamaran",
        "source_note": "Hong Kong used catamaran listing in boats.com search result.",
    },
]


def clean_float(value: float, digits: int = 6) -> float:
    return round(float(value), digits)


def read_official_boat_data() -> pd.DataFrame:
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"missing COMAP boat workbook: {DATA_PATH}")
    sheet_map = {
        "Monohulled Sailboats ": "monohull",
        "Catamarans": "catamaran",
    }
    frames = []
    for sheet_name, hull_type in sheet_map.items():
        raw = pd.read_excel(DATA_PATH, sheet_name=sheet_name)
        raw = raw.rename(
            columns={
                "Length \n(ft)": "length_ft",
                "Geographic Region": "geographic_region",
                "Country/Region/State ": "country_region_state",
                "Listing Price (USD)": "listing_price_usd",
                "Year": "year",
                "Make": "make",
                "Variant": "variant",
            }
        )
        raw["hull_type"] = hull_type
        frames.append(raw)
    df = pd.concat(frames, ignore_index=True)
    for col in ["make", "variant", "geographic_region", "country_region_state", "hull_type"]:
        df[col] = df[col].astype(str).str.replace("\xa0", " ", regex=False).str.strip()
    for col in ["length_ft", "listing_price_usd", "year"]:
        df[col] = pd.to_numeric(df[col].astype(str).str.replace("\xa0", " ", regex=False).str.strip(), errors="coerce")
    df = df.dropna(subset=["length_ft", "listing_price_usd", "year", "make", "variant", "geographic_region"])
    df = df[(df["listing_price_usd"] > 0) & (df["length_ft"] >= 30) & (df["year"].between(1900, 2025))].copy()
    df["year"] = df["year"].astype(int)
    df["age_years"] = REFERENCE_YEAR - df["year"]
    df["make_variant"] = df["make"] + " " + df["variant"]
    counts = df.groupby(["hull_type", "make", "variant"])["listing_price_usd"].transform("size")
    df["variant_observation_count"] = counts.astype(float)
    df["log_price"] = np.log(df["listing_price_usd"])
    return df.reset_index(drop=True)


def build_price_pipeline() -> Pipeline:
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", "passthrough", NUMERIC_FEATURES),
            ("cat", OneHotEncoder(handle_unknown="ignore", min_frequency=5), CATEGORICAL_FEATURES),
        ]
    )
    model = RandomForestRegressor(n_estimators=350, min_samples_leaf=3, random_state=202303, n_jobs=-1)
    return Pipeline([("preprocess", preprocessor), ("model", model)])


def price_model_analysis(df: pd.DataFrame) -> tuple[dict[str, object], Pipeline, pd.DataFrame]:
    train, holdout = train_test_split(df, test_size=0.2, random_state=202303, stratify=df["hull_type"])
    model = build_price_pipeline()
    model.fit(train[MODEL_FEATURES], np.log(train["listing_price_usd"]))
    holdout = holdout.copy()
    holdout["predicted_price_usd"] = np.exp(model.predict(holdout[MODEL_FEATURES]))
    holdout["absolute_error_usd"] = (holdout["predicted_price_usd"] - holdout["listing_price_usd"]).abs()
    holdout["absolute_pct_error"] = holdout["absolute_error_usd"] / holdout["listing_price_usd"]
    full_model = build_price_pipeline()
    full_model.fit(df[MODEL_FEATURES], np.log(df["listing_price_usd"]))

    variant_precision = (
        holdout.groupby(["hull_type", "make", "variant"], as_index=False)
        .agg(
            holdout_count=("listing_price_usd", "size"),
            observed_median_price=("listing_price_usd", "median"),
            predicted_median_price=("predicted_price_usd", "median"),
            median_abs_pct_error=("absolute_pct_error", "median"),
        )
        .sort_values(["holdout_count", "median_abs_pct_error"], ascending=[False, True])
    )
    variant_precision = variant_precision[variant_precision["holdout_count"] >= 2].head(30)
    variant_rows = [
        {
            "hull_type": row["hull_type"],
            "make": row["make"],
            "variant": row["variant"],
            "holdout_count": int(row["holdout_count"]),
            "observed_median_price": clean_float(row["observed_median_price"], 2),
            "predicted_median_price": clean_float(row["predicted_median_price"], 2),
            "median_abs_pct_error": clean_float(row["median_abs_pct_error"]),
        }
        for _, row in variant_precision.iterrows()
    ]
    analysis = {
        "model": "RandomForestRegressor on official COMAP rows with length, age, hull type, make, variant, region, country/state, and variant sample size",
        "target": "log(Listing Price USD)",
        "features": MODEL_FEATURES,
        "train_rows": int(len(train)),
        "holdout_rows": int(len(holdout)),
        "holdout_mae_usd": clean_float(mean_absolute_error(holdout["listing_price_usd"], holdout["predicted_price_usd"]), 2),
        "holdout_rmse_usd": clean_float(math.sqrt(mean_squared_error(holdout["listing_price_usd"], holdout["predicted_price_usd"])), 2),
        "holdout_mape": clean_float(holdout["absolute_pct_error"].mean()),
        "holdout_median_ape": clean_float(holdout["absolute_pct_error"].median()),
        "precision_by_variant": variant_rows,
    }
    return analysis, full_model, holdout


def ols_region_effects(df: pd.DataFrame) -> dict[str, object]:
    work = df.copy()
    work["catamaran"] = (work["hull_type"] == "catamaran").astype(float)
    work["region_caribbean"] = (work["geographic_region"] == "Caribbean").astype(float)
    work["region_usa"] = (work["geographic_region"] == "USA").astype(float)
    work["cat_x_caribbean"] = work["catamaran"] * work["region_caribbean"]
    work["cat_x_usa"] = work["catamaran"] * work["region_usa"]
    columns = [
        "intercept",
        "length_ft",
        "age_years",
        "catamaran",
        "region_caribbean",
        "region_usa",
        "cat_x_caribbean",
        "cat_x_usa",
    ]
    x = pd.DataFrame({"intercept": np.ones(len(work))})
    for col in columns[1:]:
        x[col] = work[col].astype(float).to_numpy()
    y = work["log_price"].to_numpy()
    x_matrix = x[columns].to_numpy(dtype=float)
    beta, *_ = np.linalg.lstsq(x_matrix, y, rcond=None)
    residual = y - x_matrix @ beta
    dof = len(y) - len(columns)
    sigma2 = float((residual @ residual) / dof)
    cov = sigma2 * np.linalg.inv(x_matrix.T @ x_matrix)
    se = np.sqrt(np.diag(cov))
    t_values = beta / se
    p_values = 2 * stats.t.sf(np.abs(t_values), df=dof)
    coef = dict(zip(columns, beta))
    pval = dict(zip(columns, p_values))

    effects = []
    for region, base_col, interaction_col in [
        ("Caribbean", "region_caribbean", "cat_x_caribbean"),
        ("USA", "region_usa", "cat_x_usa"),
    ]:
        mono_coef = coef[base_col]
        cat_coef = coef[base_col] + coef[interaction_col]
        effects.append(region_effect_row(region, "monohull", mono_coef, pval[base_col]))
        interaction_p = pval[interaction_col]
        effects.append(region_effect_row(region, "catamaran", cat_coef, max(pval[base_col], interaction_p)))
    practical = sorted(effects, key=lambda row: abs(row["price_effect_pct"]), reverse=True)
    return {
        "model": "OLS on log price with controls for length, age, hull type, region, and hull-by-region interactions; Europe is the baseline region",
        "controls": ["length_ft", "age_years", "hull_type", "region", "hull_type:region"],
        "baseline_region": "Europe",
        "effects": effects,
        "largest_practical_effects": practical,
        "consistency_across_hulls": [
            {
                "region": "Caribbean",
                "catamaran_minus_monohull_log_effect": clean_float(coef["cat_x_caribbean"]),
                "interaction_p_value": clean_float(pval["cat_x_caribbean"]),
                "consistent_at_5pct": bool(pval["cat_x_caribbean"] >= 0.05),
            },
            {
                "region": "USA",
                "catamaran_minus_monohull_log_effect": clean_float(coef["cat_x_usa"]),
                "interaction_p_value": clean_float(pval["cat_x_usa"]),
                "consistent_at_5pct": bool(pval["cat_x_usa"] >= 0.05),
            },
        ],
    }


def region_effect_row(region: str, hull_type: str, log_effect: float, p_value: float) -> dict[str, object]:
    return {
        "region": region,
        "hull_type": hull_type,
        "log_effect_vs_europe": clean_float(log_effect),
        "price_effect_pct": clean_float((math.exp(log_effect) - 1.0) * 100.0, 3),
        "p_value": clean_float(p_value),
        "statistically_significant_5pct": bool(p_value < 0.05),
    }


def hong_kong_market_analysis(df: pd.DataFrame, model: Pipeline) -> dict[str, object]:
    hk = pd.DataFrame(HK_COMPARABLES)
    hk["age_years"] = REFERENCE_YEAR - hk["year"]
    hk["country_region_state"] = "Hong Kong SAR"
    hk["variant_observation_count"] = [
        float(
            len(
                df[
                    (df["hull_type"] == row["hull_type"])
                    & (df["make"].str.lower() == str(row["make"]).lower())
                    & (df["variant"].str.lower() == str(row["variant"]).lower())
                ]
            )
        )
        for _, row in hk.iterrows()
    ]
    comparables = []
    known_regions = ["Europe", "USA", "Caribbean"]
    for _, row in hk.iterrows():
        scenario_rows = []
        for region in known_regions:
            scenario = row.copy()
            scenario["geographic_region"] = region
            scenario_rows.append(scenario)
        scenario_df = pd.DataFrame(scenario_rows)
        predicted = np.exp(model.predict(scenario_df[MODEL_FEATURES]))
        predicted_median = float(np.median(predicted))
        hk_effect = row["listing_price_usd"] / predicted_median - 1.0
        comparables.append(
            {
                "make": row["make"],
                "variant": row["variant"],
                "hull_type": row["hull_type"],
                "length_ft": clean_float(row["length_ft"], 2),
                "year": int(row["year"]),
                "listing_price_usd": clean_float(row["listing_price_usd"], 2),
                "known_region_model_price_median_usd": clean_float(predicted_median, 2),
                "hk_effect_pct_vs_known_region_model": clean_float(hk_effect * 100.0, 3),
                "source": row["source"],
                "source_url": row["source_url"],
            }
        )
    comp_df = pd.DataFrame(comparables)
    by_hull = (
        comp_df.groupby("hull_type", as_index=False)
        .agg(
            sample_count=("listing_price_usd", "size"),
            median_hk_effect_pct=("hk_effect_pct_vs_known_region_model", "median"),
            mean_hk_effect_pct=("hk_effect_pct_vs_known_region_model", "mean"),
            median_listing_price_usd=("listing_price_usd", "median"),
        )
        .sort_values("hull_type")
    )
    official_hk_rows = int(df["country_region_state"].str.contains("Hong Kong", case=False, na=False).sum())
    sources = sorted({row["source_url"] for row in HK_COMPARABLES})
    return {
        "official_hk_rows_in_workbook": official_hk_rows,
        "interpretation": "The COMAP workbook has no Hong Kong rows; the Hong Kong effect is therefore a transparent supplemental-market scenario, not an official-COMAP estimate.",
        "supplemental_source_count": len(sources),
        "supplemental_sources": sources,
        "comparables": comparables,
        "effect_by_hull_type": [
            {
                "hull_type": row["hull_type"],
                "sample_count": int(row["sample_count"]),
                "median_hk_effect_pct": clean_float(row["median_hk_effect_pct"], 3),
                "mean_hk_effect_pct": clean_float(row["mean_hk_effect_pct"], 3),
                "median_listing_price_usd": clean_float(row["median_listing_price_usd"], 2),
            }
            for _, row in by_hull.iterrows()
        ],
    }


def interesting_inferences(df: pd.DataFrame) -> dict[str, object]:
    summary = (
        df.groupby(["hull_type", "geographic_region"], as_index=False)
        .agg(count=("listing_price_usd", "size"), median_price=("listing_price_usd", "median"), median_length=("length_ft", "median"))
        .sort_values(["hull_type", "geographic_region"])
    )
    corr = df[["listing_price_usd", "length_ft", "age_years", "variant_observation_count"]].corr()
    cat_median = df.loc[df["hull_type"] == "catamaran", "listing_price_usd"].median()
    mono_median = df.loc[df["hull_type"] == "monohull", "listing_price_usd"].median()
    make_summary = (
        df.groupby(["hull_type", "make"], as_index=False)
        .agg(count=("listing_price_usd", "size"), median_price=("listing_price_usd", "median"))
        .query("count >= 20")
        .sort_values("median_price", ascending=False)
        .head(15)
    )
    return {
        "catamaran_median_price_usd": clean_float(cat_median, 2),
        "monohull_median_price_usd": clean_float(mono_median, 2),
        "catamaran_median_premium_pct": clean_float((cat_median / mono_median - 1) * 100.0, 3),
        "price_length_correlation": clean_float(corr.loc["listing_price_usd", "length_ft"]),
        "price_age_correlation": clean_float(corr.loc["listing_price_usd", "age_years"]),
        "region_hull_summary": [
            {
                "hull_type": row["hull_type"],
                "region": row["geographic_region"],
                "count": int(row["count"]),
                "median_price": clean_float(row["median_price"], 2),
                "median_length": clean_float(row["median_length"], 2),
            }
            for _, row in summary.iterrows()
        ],
        "high_median_price_makes": [
            {
                "hull_type": row["hull_type"],
                "make": row["make"],
                "count": int(row["count"]),
                "median_price": clean_float(row["median_price"], 2),
            }
            for _, row in make_summary.iterrows()
        ],
    }


def broker_report(result: dict[str, object]) -> str:
    model = result["price_model"]
    hk = result["hong_kong_market"]
    inferences = result["interesting_inferences"]
    hk_parts = "; ".join(
        f"{row['hull_type']}: median HK effect {row['median_hk_effect_pct']}% from {row['sample_count']} listings"
        for row in hk["effect_by_hull_type"]
    )
    return (
        "For the Hong Kong broker, the COMAP workbook supports a reliable baseline for Europe, USA, and Caribbean listings, "
        f"with a holdout MAPE of {model['holdout_mape']} on official rows. Catamarans have a median price of "
        f"${inferences['catamaran_median_price_usd']:,.0f}, compared with ${inferences['monohull_median_price_usd']:,.0f} for monohulls, "
        f"a median premium of {inferences['catamaran_median_premium_pct']}%. Region matters after controlling for length, age, and hull type, "
        "but the effect is not identical for monohulls and catamarans. The official workbook contains no Hong Kong listings, so the Hong Kong analysis "
        f"uses a separately documented current-listing scenario: {hk_parts}. Treat these Hong Kong effects as broker calibration signals, not as COMAP official data. "
        "For pricing practice, quote an interval around the model price, then adjust for local inventory scarcity, survey condition, and equipment quality."
    )


def write_artifacts(df: pd.DataFrame, holdout: pd.DataFrame, result: dict[str, object]) -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(ARTIFACT_DIR / "clean_boat_data.csv", index=False, encoding="utf-8-sig")
    pd.DataFrame(result["price_model"]["precision_by_variant"]).to_csv(
        ARTIFACT_DIR / "variant_precision.csv", index=False, encoding="utf-8-sig"
    )
    pd.DataFrame(result["region_effects"]["effects"]).to_csv(ARTIFACT_DIR / "region_effects.csv", index=False, encoding="utf-8-sig")
    pd.DataFrame(result["hong_kong_market"]["comparables"]).to_csv(
        ARTIFACT_DIR / "hong_kong_comparables.csv", index=False, encoding="utf-8-sig"
    )

    fig, ax = plt.subplots(figsize=(8.5, 4.8))
    plot_data = df.groupby(["hull_type", "geographic_region"], as_index=False)["listing_price_usd"].median()
    labels = plot_data["hull_type"] + "\n" + plot_data["geographic_region"]
    ax.bar(labels, plot_data["listing_price_usd"], color=["#2f6f73" if h == "monohull" else "#d98c3f" for h in plot_data["hull_type"]])
    ax.set_title("Median listing price by hull type and official region")
    ax.set_ylabel("Median listing price (USD)")
    ax.tick_params(axis="x", rotation=35)
    ax.grid(axis="y", alpha=0.25)
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "price_by_region_hull.png", dpi=180)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(5.8, 5.8))
    ax.scatter(holdout["listing_price_usd"], holdout["predicted_price_usd"], s=15, alpha=0.45, color="#456990")
    lo = min(holdout["listing_price_usd"].min(), holdout["predicted_price_usd"].min())
    hi = max(holdout["listing_price_usd"].max(), holdout["predicted_price_usd"].max())
    ax.plot([lo, hi], [lo, hi], color="#c1121f", linewidth=1.5)
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_title("Holdout actual vs predicted listing price")
    ax.set_xlabel("Actual USD")
    ax.set_ylabel("Predicted USD")
    ax.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "model_fit_actual_vs_predicted.png", dpi=180)
    plt.close(fig)


def write_report(result: dict[str, object]) -> None:
    lines = [
        "# 2023 MCM-C/Problem Y 二手帆船价格真实数据实验报告",
        "",
        "## 数据来源",
        f"- 官方附件：`{result['data_source']['path']}`。",
        f"- 清洗后记录数：{result['data_source']['records']}，单体船 {result['data_source']['rows']['monohull']}，双体船 {result['data_source']['rows']['catamaran']}。",
        "- 香港市场补充样本只用于 Q3 情景比较；训练和主模型必须读取 COMAP 官方 Excel。",
        "",
        "## Q1 挂牌价解释模型",
        f"- 模型：{result['price_model']['model']}。",
        f"- 留出集：{result['price_model']['holdout_rows']} 行；MAE/RMSE：{result['price_model']['holdout_mae_usd']} / {result['price_model']['holdout_rmse_usd']} USD。",
        f"- MAPE/Median APE：{result['price_model']['holdout_mape']} / {result['price_model']['holdout_median_ape']}。",
        "",
        "## Q2 区域效应",
        f"- 区域模型：{result['region_effects']['model']}。",
        "",
        "| region | hull_type | price_effect_pct | p_value | significant |",
        "|---|---|---:|---:|---|",
    ]
    for row in result["region_effects"]["effects"]:
        lines.append(
            f"| {row['region']} | {row['hull_type']} | {row['price_effect_pct']} | {row['p_value']} | {row['statistically_significant_5pct']} |"
        )
    lines.extend(
        [
            "",
            "## Q3 香港市场情景",
            result["hong_kong_market"]["interpretation"],
            "",
            "| hull_type | sample_count | median_hk_effect_pct | median_listing_price_usd |",
            "|---|---:|---:|---:|",
        ]
    )
    for row in result["hong_kong_market"]["effect_by_hull_type"]:
        lines.append(
            f"| {row['hull_type']} | {row['sample_count']} | {row['median_hk_effect_pct']} | {row['median_listing_price_usd']} |"
        )
    lines.extend(
        [
            "",
            "## Q4 其他结论",
            f"- 双体船中位价：{result['interesting_inferences']['catamaran_median_price_usd']} USD；单体船中位价：{result['interesting_inferences']['monohull_median_price_usd']} USD。",
            f"- 双体船中位溢价：{result['interesting_inferences']['catamaran_median_premium_pct']}%。",
            f"- 价格与长度相关系数：{result['interesting_inferences']['price_length_correlation']}；价格与船龄相关系数：{result['interesting_inferences']['price_age_correlation']}。",
            "",
            "## Q5 给香港经纪人的摘要报告",
            result["broker_report"],
            "",
            "## 输出文件",
            f"- `result.json`：{RESULT_PATH}",
            f"- `clean_boat_data.csv`：{ARTIFACT_DIR / 'clean_boat_data.csv'}",
            f"- `variant_precision.csv`：{ARTIFACT_DIR / 'variant_precision.csv'}",
            f"- `region_effects.csv`：{ARTIFACT_DIR / 'region_effects.csv'}",
            f"- `hong_kong_comparables.csv`：{ARTIFACT_DIR / 'hong_kong_comparables.csv'}",
            f"- `price_by_region_hull.png`：{ARTIFACT_DIR / 'price_by_region_hull.png'}",
        ]
    )
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    df = read_official_boat_data()
    price_model, trained_model, holdout = price_model_analysis(df)
    region_effects = ols_region_effects(df)
    hong_kong = hong_kong_market_analysis(df, trained_model)
    interesting = interesting_inferences(df)
    result = {
        "problem_id": "2023-C-Boats",
        "data_source": {
            "type": "official_comap_xlsx",
            "root": str(DATA_PATH.parent),
            "path": str(DATA_PATH),
            "records": int(len(df)),
            "rows": {
                "monohull": int((df["hull_type"] == "monohull").sum()),
                "catamaran": int((df["hull_type"] == "catamaran").sum()),
            },
            "sheets": ["Monohulled Sailboats ", "Catamarans"],
            "regions": sorted(df["geographic_region"].unique().tolist()),
            "columns": ["Make", "Variant", "Length (ft)", "Geographic Region", "Country/Region/State", "Listing Price (USD)", "Year"],
        },
        "model_features": MODEL_FEATURES,
        "price_model": price_model,
        "region_effects": region_effects,
        "hong_kong_market": hong_kong,
        "interesting_inferences": interesting,
    }
    result["broker_report"] = broker_report(result)
    write_artifacts(df, holdout, result)
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_report(result)
    print(f"wrote {RESULT_PATH}")
    print(f"wrote {REPORT_PATH}")
    print(f"wrote artifacts under {ARTIFACT_DIR}")


if __name__ == "__main__":
    main()
