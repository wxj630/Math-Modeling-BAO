from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ARCHIVE_ROOT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
PDF_PATH = ARCHIVE_ROOT / "official_assets_extracted" / "2024" / "Sustainability of Property Insurance.pdf"
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"

RECENT_DAMAGE_TRILLION_USD = 1.0
RECENT_EXTREME_EVENT_COUNT = 1000
CLAIM_INCREASE_2022 = 1.15
PREMIUM_INCREASE_2040_RANGE = [0.30, 0.60]
PROTECTION_GAP = 0.57

OFFICIAL_STATEMENT_PARAMETERS = {
    "recent_damage_trillion_usd": RECENT_DAMAGE_TRILLION_USD,
    "recent_extreme_event_count": RECENT_EXTREME_EVENT_COUNT,
    "claim_increase_2022": CLAIM_INCREASE_2022,
    "premium_increase_2040_range": PREMIUM_INCREASE_2040_RANGE,
    "protection_gap": PROTECTION_GAP,
    "source_note": "Official PDF statement parameters only; region rows below are deterministic demonstration scenarios, not observed insurance portfolios.",
}

SCENARIO_REGIONS = [
    {
        "region": "Florida Gulf Coast hurricane-flood corridor",
        "continent": "North America",
        "dominant_hazards": "hurricane wind, storm surge, coastal flood",
        "hazard_frequency_index": 1.18,
        "severity_index": 1.24,
        "property_vulnerability": 0.68,
        "adaptation_capacity": 0.62,
        "affordability_index": 0.57,
        "capital_buffer_index": 0.72,
    },
    {
        "region": "Bangladesh delta cyclone-flood corridor",
        "continent": "Asia",
        "dominant_hazards": "cyclone wind, river flood, storm surge",
        "hazard_frequency_index": 1.34,
        "severity_index": 1.12,
        "property_vulnerability": 0.74,
        "adaptation_capacity": 0.48,
        "affordability_index": 0.42,
        "capital_buffer_index": 0.61,
    },
]

MITIGATION_ACTIONS = [
    {"action": "roof tie-downs and opening protection", "risk_reduction": 0.16, "owner_cost_index": 0.28, "insurer_confidence_gain": 0.10},
    {"action": "elevate utilities and living floor above design flood", "risk_reduction": 0.24, "owner_cost_index": 0.45, "insurer_confidence_gain": 0.16},
    {"action": "defensible space / fire-resistant envelope", "risk_reduction": 0.14, "owner_cost_index": 0.25, "insurer_confidence_gain": 0.08},
    {"action": "community drainage, pumps, and warning triggers", "risk_reduction": 0.20, "owner_cost_index": 0.38, "insurer_confidence_gain": 0.15},
    {"action": "parametric deductible reserve plus inspection covenant", "risk_reduction": 0.11, "owner_cost_index": 0.18, "insurer_confidence_gain": 0.13},
]

LANDMARK = {
    "name": "St. Augustine Lighthouse",
    "location": "St. Augustine, Florida, USA",
    "hazard_context": "Atlantic hurricanes, coastal flooding, saltwater corrosion, and tourism disruption",
    "cultural_value_index": 0.92,
    "historical_value_index": 0.88,
    "economic_value_index": 0.76,
    "community_value_index": 0.84,
    "exposure_index": 0.69,
}


def clean_float(value: float, digits: int = 6) -> float:
    return round(float(value), digits)


def ensure_pdf_exists() -> None:
    if not PDF_PATH.exists():
        raise FileNotFoundError(f"Official problem PDF not found: {PDF_PATH}")


def underwriting_viability_score(
    hazard_frequency_index: float,
    severity_index: float,
    vulnerability: float,
    mitigation_effect: float,
    affordability_index: float,
    capital_buffer_index: float,
) -> tuple[float, float, float]:
    climate_multiplier = 1.0 + sum(PREMIUM_INCREASE_2040_RANGE) / 2.0
    gross_loss_ratio = 0.42 * CLAIM_INCREASE_2022 * climate_multiplier * hazard_frequency_index * severity_index * vulnerability
    net_loss_ratio = gross_loss_ratio * (1.0 - mitigation_effect)
    affordability_penalty = max(0.0, 0.62 - affordability_index) * (1.0 + PROTECTION_GAP) * 0.45
    viability = capital_buffer_index + 0.30 * affordability_index + 0.35 * mitigation_effect - net_loss_ratio - affordability_penalty
    return clean_float(viability, 4), clean_float(net_loss_ratio, 4), clean_float(affordability_penalty, 4)


def underwriting_decision(viability: float) -> str:
    if viability >= 0.62:
        return "approve standard or lightly conditioned underwriting"
    if viability >= 0.40:
        return "conditional underwriting with mitigation, deductible, and reinsurance trigger"
    return "decline new underwriting until community-level risk reduction or public-private backstop exists"


def build_underwriting_grid() -> pd.DataFrame:
    rows = []
    for hazard in [0.85, 1.00, 1.15, 1.30, 1.45]:
        for severity in [0.85, 1.00, 1.20, 1.40]:
            for vulnerability in [0.45, 0.60, 0.75]:
                for mitigation in [0.00, 0.15, 0.30]:
                    viability, net_loss, penalty = underwriting_viability_score(
                        hazard,
                        severity,
                        vulnerability,
                        mitigation,
                        affordability_index=0.58,
                        capital_buffer_index=0.72,
                    )
                    rows.append(
                        {
                            "hazard_frequency_index": hazard,
                            "severity_index": severity,
                            "property_vulnerability": vulnerability,
                            "mitigation_effect": mitigation,
                            "net_loss_ratio": net_loss,
                            "affordability_penalty": penalty,
                            "underwriting_viability_score": viability,
                            "decision": underwriting_decision(viability),
                        }
                    )
    df = pd.DataFrame(rows)
    df.to_csv(ARTIFACT_DIR / "underwriting_policy_grid.csv", index=False)
    return df


def demonstrate_regions() -> pd.DataFrame:
    rows = []
    for region in SCENARIO_REGIONS:
        mitigation_effect = 0.18 + 0.18 * region["adaptation_capacity"]
        viability, net_loss, penalty = underwriting_viability_score(
            region["hazard_frequency_index"],
            region["severity_index"],
            region["property_vulnerability"],
            mitigation_effect,
            region["affordability_index"],
            region["capital_buffer_index"],
        )
        rows.append(
            {
                **region,
                "mitigation_effect": clean_float(mitigation_effect, 4),
                "net_loss_ratio": net_loss,
                "affordability_penalty": penalty,
                "underwriting_viability_score": viability,
                "decision": underwriting_decision(viability),
            }
        )
    df = pd.DataFrame(rows)
    df.to_csv(ARTIFACT_DIR / "regional_risk_comparison.csv", index=False)
    return df


def build_mitigation_analysis() -> tuple[pd.DataFrame, dict[str, object]]:
    baseline_risk = 0.78
    rows = []
    for item in MITIGATION_ACTIONS:
        risk_after = baseline_risk * (1.0 - item["risk_reduction"])
        affordability_load = item["owner_cost_index"] * (1.0 - PROTECTION_GAP)
        insurer_score_gain = item["insurer_confidence_gain"] + item["risk_reduction"] - 0.20 * affordability_load
        rows.append(
            {
                **item,
                "risk_score_after": clean_float(risk_after, 4),
                "affordability_load": clean_float(affordability_load, 4),
                "insurer_score_gain": clean_float(insurer_score_gain, 4),
            }
        )
    df = pd.DataFrame(rows).sort_values("insurer_score_gain", ascending=False)
    df.to_csv(ARTIFACT_DIR / "mitigation_levers.csv", index=False)
    best = df.iloc[0].to_dict()
    return df, {
        "baseline_risk_score": clean_float(baseline_risk, 4),
        "actions": df.to_dict(orient="records"),
        "best_action": best,
        "interpretation": "Owners can influence underwriting by converting uncertain high-severity losses into inspected, lower-loss, conditionally insurable risks.",
    }


def build_site_decisions() -> pd.DataFrame:
    sites = [
        {"site": "elevated inland infill", "hazard_index": 0.42, "service_viability": 0.82, "resilience_cost": 0.22, "community_need": 0.70},
        {"site": "coastal low-lying expansion", "hazard_index": 0.86, "service_viability": 0.58, "resilience_cost": 0.64, "community_need": 0.62},
        {"site": "redeveloped floodplain with green buffers", "hazard_index": 0.66, "service_viability": 0.71, "resilience_cost": 0.46, "community_need": 0.76},
        {"site": "wildland-urban edge subdivision", "hazard_index": 0.74, "service_viability": 0.63, "resilience_cost": 0.53, "community_need": 0.54},
    ]
    rows = []
    for site in sites:
        build_score = 0.35 * site["service_viability"] + 0.30 * site["community_need"] - 0.25 * site["hazard_index"] - 0.10 * site["resilience_cost"]
        if build_score >= 0.46:
            decision = "build with ordinary resilience covenant"
        elif build_score >= 0.34:
            decision = "build only after site-specific elevation, drainage, and insurance conditions"
        else:
            decision = "avoid new construction or relocate growth inland"
        rows.append({**site, "build_score": clean_float(build_score, 4), "recommendation": decision})
    df = pd.DataFrame(rows)
    df.to_csv(ARTIFACT_DIR / "site_build_decisions.csv", index=False)
    return df


def build_preservation_model(site_df: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, object]]:
    candidates = [
        {"building": LANDMARK["name"], "cultural": 0.92, "historical": 0.88, "economic": 0.76, "community": 0.84, "exposure": 0.69, "intervention_cost_musd": 8.5},
        {"building": "historic waterfront market", "cultural": 0.74, "historical": 0.68, "economic": 0.83, "community": 0.79, "exposure": 0.77, "intervention_cost_musd": 5.2},
        {"building": "old civic theater", "cultural": 0.81, "historical": 0.72, "economic": 0.61, "community": 0.87, "exposure": 0.55, "intervention_cost_musd": 3.8},
        {"building": "redundant warehouse district", "cultural": 0.39, "historical": 0.42, "economic": 0.51, "community": 0.36, "exposure": 0.62, "intervention_cost_musd": 4.6},
    ]
    rows = []
    for item in candidates:
        significance = 0.30 * item["cultural"] + 0.25 * item["historical"] + 0.25 * item["community"] + 0.20 * item["economic"]
        urgency = significance * item["exposure"]
        benefit = 22.0 * significance + 6.0 * item["economic"]
        bcr = benefit / item["intervention_cost_musd"]
        if bcr >= 3.2 and urgency >= 0.45:
            action = "protect in place with phased hardening and emergency response covenant"
        elif bcr >= 2.4:
            action = "selective retrofit and archival/documentation plan"
        else:
            action = "document, insure only conditionally, and avoid major capital preservation"
        rows.append(
            {
                **item,
                "significance_score": clean_float(significance, 4),
                "preservation_urgency": clean_float(urgency, 4),
                "estimated_community_benefit_musd": clean_float(benefit, 3),
                "benefit_cost_ratio": clean_float(bcr, 3),
                "recommended_action": action,
            }
        )
    df = pd.DataFrame(rows).sort_values("preservation_urgency", ascending=False)
    df.to_csv(ARTIFACT_DIR / "preservation_priority.csv", index=False)
    write_frontier_plot(site_df, df)
    landmark_row = df[df["building"] == LANDMARK["name"]].iloc[0].to_dict()
    return df, {
        "landmark": LANDMARK["name"],
        "landmark_context": LANDMARK,
        "priority_ranking": df.to_dict(orient="records"),
        "recommended_plan": {
            "phase_1": "0-12 months: engineering survey, corrosion/wind inspection, emergency shutters, drainage maintenance, and visitor closure triggers",
            "phase_2": "1-3 years: foundation drainage, roof and lantern-room hardening, floodproof utilities, and insurance inspection covenant",
            "phase_3": "3-7 years: evaluate managed retreat only if erosion and storm-surge triggers exceed the conditional underwriting band",
            "cost_proposal_musd": landmark_row["intervention_cost_musd"],
            "benefit_cost_ratio": landmark_row["benefit_cost_ratio"],
        },
    }


def write_frontier_plot(site_df: pd.DataFrame, preservation_df: pd.DataFrame) -> None:
    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(11.0, 4.8))
    ax0.scatter(site_df["hazard_index"], site_df["build_score"], color="#356c76", s=60)
    for _, row in site_df.iterrows():
        ax0.text(row["hazard_index"] + 0.01, row["build_score"], row["site"], fontsize=7)
    ax0.axhline(0.46, color="#5f8f3f", linestyle="--", linewidth=1)
    ax0.axhline(0.34, color="#c17d2f", linestyle="--", linewidth=1)
    ax0.set_xlabel("Hazard index")
    ax0.set_ylabel("Build score")
    ax0.set_title("Build / Adapt / Avoid Frontier")
    ax0.grid(alpha=0.25)

    ax1.scatter(preservation_df["preservation_urgency"], preservation_df["benefit_cost_ratio"], color="#8f4a3c", s=60)
    for _, row in preservation_df.iterrows():
        ax1.text(row["preservation_urgency"] + 0.005, row["benefit_cost_ratio"], row["building"], fontsize=7)
    ax1.axhline(3.2, color="#5f8f3f", linestyle="--", linewidth=1)
    ax1.set_xlabel("Preservation urgency")
    ax1.set_ylabel("Benefit/cost ratio")
    ax1.set_title("Preservation Priority Frontier")
    ax1.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "insurance_preservation_frontier.png", dpi=180)
    plt.close(fig)


def build_result(
    underwriting_df: pd.DataFrame,
    regional_df: pd.DataFrame,
    mitigation_df: pd.DataFrame,
    mitigation: dict[str, object],
    site_df: pd.DataFrame,
    preservation_df: pd.DataFrame,
    preservation: dict[str, object],
) -> dict[str, object]:
    approve_rows = int((underwriting_df["decision"] == "approve standard or lightly conditioned underwriting").sum())
    conditional_rows = int(underwriting_df["decision"].str.startswith("conditional").sum())
    decline_rows = int(underwriting_df["decision"].str.startswith("decline").sum())
    return {
        "problem_id": "2024-E",
        "title": "Sustainability of Property Insurance",
        "data_source": {
            "type": "official_statement_parameters",
            "root": str(ARCHIVE_ROOT / "official_assets_extracted"),
            "source_pdf": str(PDF_PATH),
            "official_requirements": {
                "underwrite_conditions": True,
                "choose_when_to_take_risk": True,
                "property_owner_influence": True,
                "rising_extreme_weather_events": True,
                "two_continents_demonstration": True,
                "where_how_whether_to_build": True,
                "historic_landmark_not_cape_hatteras": True,
                "community_letter": True,
            },
            "parameters": OFFICIAL_STATEMENT_PARAMETERS,
        },
        "insurance_model": {
            "model": "deterministic climate-stress underwriting score balancing net catastrophe loss ratio, affordability, mitigation, and insurer capital buffer",
            "underwriting_rule": {
                "score": "higher is more sustainable to underwrite",
                "approve_threshold": 0.62,
                "decline_threshold": 0.40,
                "approve": "score >= 0.62",
                "conditional": "0.40 <= score < 0.62",
                "decline": "score < 0.40",
            },
            "policy_grid_summary": {
                "rows": int(len(underwriting_df)),
                "approve_rows": approve_rows,
                "conditional_rows": conditional_rows,
                "decline_rows": decline_rows,
            },
            "best_cases": underwriting_df.sort_values("underwriting_viability_score", ascending=False).head(6).to_dict(orient="records"),
            "worst_cases": underwriting_df.sort_values("underwriting_viability_score", ascending=True).head(6).to_dict(orient="records"),
        },
        "regional_demonstration": {
            "description": "Two deterministic region scenarios on different continents, used to demonstrate the official PDF model rather than claim observed portfolio data.",
            "regions": regional_df.to_dict(orient="records"),
        },
        "owner_mitigation": mitigation,
        "build_site_model": {
            "model": "site build score combining hazard exposure, service viability, community need, and resilience cost",
            "site_recommendations": site_df.to_dict(orient="records"),
        },
        "preservation_model": {
            "landmark": LANDMARK["name"],
            "model": "weighted cultural, historical, economic, and community significance multiplied by exposure urgency and checked against benefit/cost ratio",
            "priority_ranking": preservation_df.to_dict(orient="records"),
        },
        "landmark_application": preservation,
        "community_letter": (
            "Dear community members, our insurance and preservation models recommend protecting St. Augustine Lighthouse in place over the next "
            "seven years, beginning with inspections, floodproof utilities, roof and lantern-room hardening, and clear storm-closure triggers. "
            "The plan preserves a high-value cultural and tourism asset while keeping future insurance conditional on verified risk reduction."
        ),
    }


def build_report(result: dict[str, object]) -> None:
    lines = [
        "# 2024 ICM-E Sustainability of Property Insurance",
        "",
        "## 数据真实性",
        f"- 官方来源：`{result['data_source']['source_pdf']}`。",
        "- 本题无 COMAP 数值附件；脚本只使用官方 PDF 中的宏观数字和显式地区/建筑情景假设，不使用随机占位数据。",
        "- 地区和地标行是 deterministic demonstration scenarios，不是保险公司真实组合数据。",
        "",
        "## 官方题面数字",
        f"- 近期极端天气损失：超过 ${RECENT_DAMAGE_TRILLION_USD}T，事件超过 {RECENT_EXTREME_EVENT_COUNT} 起。",
        f"- 2022 年自然灾害索赔相对 30 年平均增加：{CLAIM_INCREASE_2022 * 100:.0f}%。",
        f"- 2040 年保费预计增加区间：{PREMIUM_INCREASE_2040_RANGE[0] * 100:.0f}%-{PREMIUM_INCREASE_2040_RANGE[1] * 100:.0f}%。",
        f"- 全球保障缺口：{PROTECTION_GAP * 100:.0f}%。",
        "",
        "## 每问结果",
        "### Q1-Q2 承保条件与何时承担风险",
        f"- 模型：{result['insurance_model']['model']}。",
        f"- 规则：{result['insurance_model']['underwriting_rule']}。",
        f"- 网格摘要：{result['insurance_model']['policy_grid_summary']}。",
        "",
        "### Q3 业主可影响的因素",
        f"- 基准风险分：{result['owner_mitigation']['baseline_risk_score']}。",
        f"- 最优行动：{result['owner_mitigation']['best_action']['action']}，行动后风险分：{result['owner_mitigation']['best_action']['risk_score_after']}。",
        "",
        "### Q4 两大洲地区演示",
    ]
    for row in result["regional_demonstration"]["regions"]:
        lines.append(f"- {row['region']}（{row['continent']}）：score={row['underwriting_viability_score']}，decision={row['decision']}。")
    lines.extend([
        "",
        "### Q5 建址模型",
    ])
    for row in result["build_site_model"]["site_recommendations"]:
        lines.append(f"- {row['site']}：build_score={row['build_score']}，{row['recommendation']}。")
    lines.extend([
        "",
        "### Q6-Q7 历史地标保护",
        f"- 选择地标：{result['preservation_model']['landmark']}。",
        f"- 推荐计划：{result['landmark_application']['recommended_plan']}。",
        "",
        "## 一页社区信核心",
        result["community_letter"],
        "",
        "## 输出产物",
        "- `underwriting_policy_grid.csv`：承保政策网格。",
        "- `regional_risk_comparison.csv`：两大洲地区演示。",
        "- `mitigation_levers.csv`：业主/社区减灾行动。",
        "- `site_build_decisions.csv`：建址决策表。",
        "- `preservation_priority.csv`：保护优先级表。",
        "- `insurance_preservation_frontier.png`：建址-保护权衡图。",
    ])
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ensure_pdf_exists()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    underwriting_df = build_underwriting_grid()
    regional_df = demonstrate_regions()
    mitigation_df, mitigation = build_mitigation_analysis()
    site_df = build_site_decisions()
    preservation_df, preservation = build_preservation_model(site_df)
    result = build_result(underwriting_df, regional_df, mitigation_df, mitigation, site_df, preservation_df, preservation)
    result["artifacts"] = {
        "underwriting_policy_grid": str(ARTIFACT_DIR / "underwriting_policy_grid.csv"),
        "regional_risk_comparison": str(ARTIFACT_DIR / "regional_risk_comparison.csv"),
        "mitigation_levers": str(ARTIFACT_DIR / "mitigation_levers.csv"),
        "site_build_decisions": str(ARTIFACT_DIR / "site_build_decisions.csv"),
        "preservation_priority": str(ARTIFACT_DIR / "preservation_priority.csv"),
        "insurance_preservation_frontier": str(ARTIFACT_DIR / "insurance_preservation_frontier.png"),
    }
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    build_report(result)
    print(json.dumps({"result": str(RESULT_PATH), "report": str(REPORT_PATH), "artifacts": str(ARTIFACT_DIR)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
