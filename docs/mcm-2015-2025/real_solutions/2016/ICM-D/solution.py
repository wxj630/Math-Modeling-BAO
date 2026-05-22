from __future__ import annotations

import json
import math
import os
from pathlib import Path

import pandas as pd


ARCHIVE_ROOT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
PDF_PATH = ARCHIVE_ROOT / "official_assets_extracted" / "2016" / "Measuring the Evolution and Influence in Society's Information Networks.pdf"
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"
os.environ.setdefault("MPLCONFIGDIR", "/private/tmp/math_modeling_world_mplconfig")

import matplotlib.pyplot as plt


PREDICTION_YEAR = 2050
REFERENCE_TODAY_ERA = "2010s_smartphone"
OFFICIAL_PERIODS = [
    {
        "era": "1870s_telegraph_train_newspaper",
        "representative_year": 1875,
        "official_description": "newspapers delivered by trains and stories passed by telegraph",
        "media_access": 0.18,
        "transmission_speed": 0.10,
        "network_connectivity": 0.08,
        "gatekeeping_filter": 0.78,
        "channel_capacity": 1.0,
    },
    {
        "era": "1920s_radio",
        "representative_year": 1925,
        "official_description": "radios became a more common household item",
        "media_access": 0.36,
        "transmission_speed": 0.28,
        "network_connectivity": 0.20,
        "gatekeeping_filter": 0.70,
        "channel_capacity": 3.8,
    },
    {
        "era": "1970s_television",
        "representative_year": 1975,
        "official_description": "televisions were in most homes",
        "media_access": 0.72,
        "transmission_speed": 0.58,
        "network_connectivity": 0.42,
        "gatekeeping_filter": 0.58,
        "channel_capacity": 15.0,
    },
    {
        "era": "1990s_early_internet",
        "representative_year": 1995,
        "official_description": "households began connecting to the early internet",
        "media_access": 0.46,
        "transmission_speed": 0.74,
        "network_connectivity": 0.64,
        "gatekeeping_filter": 0.42,
        "channel_capacity": 85.0,
    },
    {
        "era": "2010s_smartphone",
        "representative_year": 2015,
        "official_description": "we can carry a connection to the world on our phones",
        "media_access": 0.82,
        "transmission_speed": 0.92,
        "network_connectivity": 0.88,
        "gatekeeping_filter": 0.22,
        "channel_capacity": 520.0,
    },
]

ASSUMPTIONS = {
    "era_coefficients": "media_access, transmission_speed, network_connectivity, gatekeeping_filter, and channel_capacity are transparent normalized assumptions anchored to the five eras named in the official PDF.",
    "awareness_model": "awareness(t) = reachable_population * (1 - exp(-diffusion_rate * t)); diffusion_rate increases with speed, connectivity, information value, and source credibility.",
    "news_filter_rule": "news_score = 0.34 value + 0.24 source credibility + 0.18 affected population + 0.14 novelty + 0.10 shareability; items above threshold qualify as news.",
    "opinion_model": "A one-step DeGroot-style influence score estimates opinion shift from value, source credibility, bias alignment, message format, and network strength.",
    "capacity_projection": "2050 capacity extrapolates log channel capacity against era year and caps the multiplier to avoid claiming an unbounded physical law.",
}


def clean_float(value: float, digits: int = 6) -> float:
    return round(float(value), digits)


def era_dataframe() -> pd.DataFrame:
    rows = []
    for period in OFFICIAL_PERIODS:
        openness = 1.0 - float(period["gatekeeping_filter"])
        diffusion_rate = 0.035 + 0.38 * float(period["transmission_speed"]) + 0.28 * float(period["network_connectivity"]) + 0.13 * openness
        reachable_population = min(0.98, 0.20 + 0.62 * float(period["media_access"]) + 0.20 * float(period["network_connectivity"]))
        influence_power = 0.30 * float(period["media_access"]) + 0.34 * float(period["network_connectivity"]) + 0.22 * float(period["transmission_speed"]) + 0.14 * openness
        rows.append(
            {
                **period,
                "openness": clean_float(openness),
                "diffusion_rate_per_hour": clean_float(diffusion_rate),
                "reachable_population_share": clean_float(reachable_population),
                "influence_power": clean_float(influence_power),
            }
        )
    return pd.DataFrame(rows)


def news_score(
    information_value: float,
    source_credibility: float,
    affected_population: float,
    novelty: float,
    shareability: float,
) -> float:
    return (
        0.34 * information_value
        + 0.24 * source_credibility
        + 0.18 * affected_population
        + 0.14 * novelty
        + 0.10 * shareability
    )


def news_filter_model() -> dict[str, object]:
    threshold = 0.58
    items = [
        ("presidential_assassination", 1.00, 0.96, 0.92, 0.84, 0.75),
        ("major_war_breaking_news", 0.94, 0.90, 0.88, 0.80, 0.70),
        ("celebrity_engagement_rumor", 0.32, 0.42, 0.30, 0.68, 0.88),
        ("local_storm_damage", 0.54, 0.72, 0.24, 0.50, 0.46),
        ("viral_cat_video", 0.14, 0.26, 0.18, 0.72, 0.94),
    ]
    rows = []
    for name, value, credibility, affected, novelty, shareability in items:
        score = news_score(value, credibility, affected, novelty, shareability)
        rows.append(
            {
                "item": name,
                "information_value": value,
                "source_credibility": credibility,
                "affected_population": affected,
                "novelty": novelty,
                "shareability": shareability,
                "news_score": clean_float(score),
                "qualifies_as_news": bool(score >= threshold),
            }
        )
    return {
        "threshold": threshold,
        "definition": "weighted information value and social transmissibility filter",
        "items": sorted(rows, key=lambda row: row["news_score"], reverse=True),
    }


def awareness_at_hours(era: dict[str, object], hours: float, information_value: float, source_credibility: float) -> float:
    openness = 1.0 - float(era["gatekeeping_filter"])
    diffusion_rate = 0.035 + 0.38 * float(era["transmission_speed"]) + 0.28 * float(era["network_connectivity"]) + 0.13 * openness
    diffusion_rate *= 0.55 + 0.55 * information_value + 0.24 * source_credibility
    reachable = min(0.98, 0.20 + 0.62 * float(era["media_access"]) + 0.20 * float(era["network_connectivity"]))
    return min(reachable, reachable * (1.0 - math.exp(-diffusion_rate * hours)))


def diffusion_comparison(eras: pd.DataFrame) -> dict[str, object]:
    scenario_defs = [
        ("taylor_swift_engagement_rumor_if_1860", "1870s_telegraph_train_newspaper", 0.34, 0.42),
        ("lincoln_assassination_historical_proxy", "1870s_telegraph_train_newspaper", 1.00, 0.92),
        ("important_person_assassinated_today", "2010s_smartphone", 1.00, 0.95),
        ("celebrity_rumor_today", "2010s_smartphone", 0.34, 0.44),
    ]
    hours_grid = [1, 3, 6, 12, 24, 48, 72, 168]
    rows = []
    era_lookup = {row["era"]: row for row in eras.to_dict("records")}
    for scenario, era_name, value, credibility in scenario_defs:
        for hours in hours_grid:
            rows.append(
                {
                    "scenario": scenario,
                    "era": era_name,
                    "hours": hours,
                    "awareness_share": clean_float(awareness_at_hours(era_lookup[era_name], hours, value, credibility)),
                    "information_value": value,
                    "source_credibility": credibility,
                }
            )
    by_key = {(row["scenario"], row["hours"]): row["awareness_share"] for row in rows}
    return {
        "method": "deterministic exponential diffusion over each official era's assumed reach and speed",
        "rows": rows,
        "taylor_1860_awareness_24h": by_key[("taylor_swift_engagement_rumor_if_1860", 24)],
        "lincoln_awareness_24h": by_key[("lincoln_assassination_historical_proxy", 24)],
        "important_assassination_today_awareness_24h": by_key[("important_person_assassinated_today", 24)],
    }


def validation(diffusion: dict[str, object]) -> dict[str, object]:
    today = float(diffusion["important_assassination_today_awareness_24h"])
    lincoln = float(diffusion["lincoln_awareness_24h"])
    return {
        "historical_proxy": "Compare a high-value assassination event under the newspaper/telegraph/train era to a high-value event under the smartphone era.",
        "lincoln_awareness_24h": clean_float(lincoln),
        "predicted_today_awareness_24h": clean_float(today),
        "today_to_lincoln_ratio_24h": clean_float(today / max(lincoln, 1e-9)),
        "reliability_note": "The validation is structural rather than archival: it checks that the model reproduces the expected order-of-magnitude shift from delayed broadcast to near-immediate connected reach.",
    }


def capacity_2050(eras: pd.DataFrame) -> dict[str, object]:
    first = eras.iloc[0]
    last = eras.iloc[-1]
    years = float(last["representative_year"] - first["representative_year"])
    log_growth = math.log(float(last["channel_capacity"]) / float(first["channel_capacity"])) / years
    projected_capacity = float(last["channel_capacity"]) * math.exp(log_growth * (PREDICTION_YEAR - int(last["representative_year"])))
    capped_capacity = min(projected_capacity, float(last["channel_capacity"]) * 35.0)
    multiplier = capped_capacity / float(last["channel_capacity"])
    relationships = {
        "human_to_human": "dense social graph remains dominant for interpretation and trust",
        "human_to_platform": "algorithmic filtering increasingly controls attention allocation",
        "machine_to_machine": "sensor and agent networks add high-volume low-latency communication",
        "local_to_global": "regional topology matters less for raw speed but still matters for trust and language communities",
    }
    return {
        "prediction_year": PREDICTION_YEAR,
        "baseline_era": REFERENCE_TODAY_ERA,
        "projected_channel_capacity_index": clean_float(capped_capacity, 3),
        "capacity_multiplier_vs_2010s": clean_float(multiplier, 3),
        "relationships": relationships,
        "method": "log-linear extrapolation of assumed era capacity, capped for conservative reporting",
    }


def opinion_influence() -> dict[str, object]:
    scenarios = [
        ("trusted_public_health_warning", 0.90, 0.92, 0.20, 0.70, 0.86),
        ("partisan_low_credibility_claim", 0.55, 0.28, 0.82, 0.62, 0.74),
        ("celebrity_rumor_visual_shortform", 0.30, 0.46, 0.55, 0.90, 0.88),
        ("local_emergency_from_official_source", 0.84, 0.88, 0.18, 0.66, 0.62),
        ("scientific_correction_after_false_post", 0.62, 0.82, 0.70, 0.48, 0.58),
    ]
    rows = []
    for name, value, credibility, initial_bias, message_form, network_strength in scenarios:
        persuasion = (
            0.30 * value
            + 0.26 * credibility
            + 0.20 * network_strength
            + 0.14 * message_form
            - 0.22 * initial_bias
        )
        final_support = min(0.98, max(0.02, 0.50 + 0.45 * persuasion))
        rows.append(
            {
                "scenario": name,
                "information_value": value,
                "source_credibility": credibility,
                "initial_bias": initial_bias,
                "message_form_strength": message_form,
                "network_strength": network_strength,
                "persuasion_index": clean_float(persuasion),
                "final_support_share": clean_float(final_support),
                "opinion_shift_from_neutral": clean_float(final_support - 0.50),
            }
        )
    return {
        "method": "one-step influence score inspired by DeGroot opinion updating and threshold persuasion",
        "scenarios": sorted(rows, key=lambda row: row["opinion_shift_from_neutral"], reverse=True),
    }


def factor_sensitivity() -> dict[str, object]:
    baseline = {
        "information_value": 0.62,
        "source_credibility": 0.62,
        "initial_bias": 0.45,
        "message_form_strength": 0.62,
        "network_strength": 0.62,
    }

    def score(values: dict[str, float]) -> float:
        return (
            0.30 * values["information_value"]
            + 0.26 * values["source_credibility"]
            + 0.20 * values["network_strength"]
            + 0.14 * values["message_form_strength"]
            - 0.22 * values["initial_bias"]
        )

    base_score = score(baseline)
    rows = []
    for factor in baseline:
        high = dict(baseline)
        low = dict(baseline)
        high[factor] = min(1.0, baseline[factor] + 0.20)
        low[factor] = max(0.0, baseline[factor] - 0.20)
        if factor == "initial_bias":
            direction = "negative"
        else:
            direction = "positive"
        rows.append(
            {
                "factor": factor,
                "direction": direction,
                "low_score": clean_float(score(low)),
                "baseline_score": clean_float(base_score),
                "high_score": clean_float(score(high)),
                "absolute_swing": clean_float(abs(score(high) - score(low))),
            }
        )
    rows = sorted(rows, key=lambda row: row["absolute_swing"], reverse=True)
    return {
        "method": "one-at-a-time sensitivity on the opinion influence score",
        "top_factor": rows[0]["factor"],
        "rows": rows,
    }


def write_artifacts(eras: pd.DataFrame, diffusion: dict[str, object], influence: dict[str, object], capacity: dict[str, object], sensitivity: dict[str, object]) -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    eras.to_csv(ARTIFACT_DIR / "era_parameters.csv", index=False, encoding="utf-8-sig")
    pd.DataFrame(diffusion["rows"]).to_csv(ARTIFACT_DIR / "diffusion_comparison.csv", index=False, encoding="utf-8-sig")
    pd.DataFrame(influence["scenarios"]).to_csv(ARTIFACT_DIR / "opinion_influence_scenarios.csv", index=False, encoding="utf-8-sig")
    pd.DataFrame([capacity]).drop(columns=["relationships"]).to_csv(ARTIFACT_DIR / "communication_capacity_2050.csv", index=False, encoding="utf-8-sig")
    pd.DataFrame(sensitivity["rows"]).to_csv(ARTIFACT_DIR / "factor_sensitivity.csv", index=False, encoding="utf-8-sig")

    curves = pd.DataFrame(diffusion["rows"])
    fig, ax = plt.subplots(figsize=(9, 5.2))
    for scenario, frame in curves.groupby("scenario"):
        ax.plot(frame["hours"], frame["awareness_share"], marker="o", linewidth=2, label=scenario.replace("_", " "))
    ax.set_xscale("log")
    ax.set_xlabel("Hours after event (log scale)")
    ax.set_ylabel("Population aware share")
    ax.set_title("2016 ICM-D Information Diffusion by Era and News Value")
    ax.grid(alpha=0.25)
    ax.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "information_spread_curves.png", dpi=180)
    plt.close(fig)


def write_report(result: dict[str, object]) -> None:
    lines = [
        "# 2016 ICM-D Society Information Networks 题面参数实验报告",
        "",
        "## 数据来源",
        f"- 官方 PDF：`{PDF_PATH}`。",
        "- 官方题面明确给出五个时期：1870s newspaper/train/telegraph、1920s radio、1970s television、1990s early internet、2010s smartphone。",
        "- 本题没有独立 CSV/XLSX 附件；时代速度、覆盖率、连通性、过滤强度和容量指数均为显式可替换建模假设。",
        "",
        "## Q1 信息流和新闻筛选",
        f"- 新闻阈值：{result['news_filter_model']['threshold']}。",
        f"- 排名最高的新闻项：{result['news_filter_model']['items'][0]['item']}。",
        "",
        "## Q2 过去到今天的验证",
        f"- Lincoln 时代高价值事件 24h awareness：{result['validation']['lincoln_awareness_24h']}。",
        f"- 今日高价值事件 24h awareness：{result['validation']['predicted_today_awareness_24h']}。",
        f"- 今日/历史 24h 比值：{result['validation']['today_to_lincoln_ratio_24h']}。",
        "",
        "## Q3 2050 通信网络容量",
        f"- 2050 容量指数：{result['capacity_2050']['projected_channel_capacity_index']}。",
        f"- 相对 2010s multiplier：{result['capacity_2050']['capacity_multiplier_vs_2010s']}。",
        "",
        "## Q4 公众兴趣和观点影响",
        f"- 最高正向观点变化情景：{result['opinion_influence']['scenarios'][0]['scenario']}。",
        "",
        "## Q5 因素敏感性",
        f"- 最敏感因素：{result['factor_sensitivity']['top_factor']}。",
        "",
        "## 输出文件",
        f"- `result.json`：{RESULT_PATH}",
        f"- `era_parameters.csv`：{ARTIFACT_DIR / 'era_parameters.csv'}",
        f"- `diffusion_comparison.csv`：{ARTIFACT_DIR / 'diffusion_comparison.csv'}",
        f"- `opinion_influence_scenarios.csv`：{ARTIFACT_DIR / 'opinion_influence_scenarios.csv'}",
        f"- `communication_capacity_2050.csv`：{ARTIFACT_DIR / 'communication_capacity_2050.csv'}",
        f"- `information_spread_curves.png`：{ARTIFACT_DIR / 'information_spread_curves.png'}",
    ]
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    if not PDF_PATH.exists():
        raise FileNotFoundError(f"Missing official PDF: {PDF_PATH}")
    eras = era_dataframe()
    news_filter = news_filter_model()
    diffusion = diffusion_comparison(eras)
    validation_result = validation(diffusion)
    capacity = capacity_2050(eras)
    influence = opinion_influence()
    sensitivity = factor_sensitivity()
    result = {
        "problem_id": "2016-D",
        "data_source": {
            "type": "official_statement_parameters",
            "root": str(PDF_PATH.parent),
            "source_pdf": str(PDF_PATH),
            "official_problem_parameters": {
                "periods": [period["era"] for period in OFFICIAL_PERIODS],
                "period_descriptions": {period["era"]: period["official_description"] for period in OFFICIAL_PERIODS},
                "prediction_year": PREDICTION_YEAR,
                "example_events_named_in_statement": [
                    "Taylor Swift engagement rumor if it had happened in 1860",
                    "important person assassinated today",
                    "US President Abraham Lincoln assassination",
                ],
                "required_factors": [
                    "information value",
                    "initial opinion and bias",
                    "message form or source",
                    "network topology or strength",
                ],
            },
            "assumptions": ASSUMPTIONS,
        },
        "era_model": {
            "periods": eras.to_dict("records"),
        },
        "news_filter_model": news_filter,
        "diffusion_comparison": diffusion,
        "validation": validation_result,
        "capacity_2050": capacity,
        "opinion_influence": influence,
        "factor_sensitivity": sensitivity,
        "assumption_audit": {
            "truthfulness_note": "This workflow uses official statement parameters and explicit deterministic assumptions; it does not claim that the normalized era coefficients are observed data.",
            "replaceable_assumptions": ASSUMPTIONS,
        },
    }
    write_artifacts(eras, diffusion, influence, capacity, sensitivity)
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_report(result)
    print(json.dumps({"result": str(RESULT_PATH), "report": str(REPORT_PATH), "artifacts": str(ARTIFACT_DIR)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
