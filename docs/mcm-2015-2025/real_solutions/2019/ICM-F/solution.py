from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import pandas as pd


ARCHIVE_ROOT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
PDF_PATH = ARCHIVE_ROOT / "official_assets" / "2019" / "Universal, Decentralized, Digital Currency- Is it possible-"
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"

COUNTRY_ARCHETYPES = [
    {"archetype": "high inflation cash-dependent economy", "unbanked_share": 0.54, "digital_access": 0.48, "regulatory_trust": 0.36, "currency_instability": 0.82, "illicit_flow_risk": 0.50},
    {"archetype": "advanced banking economy", "unbanked_share": 0.05, "digital_access": 0.92, "regulatory_trust": 0.84, "currency_instability": 0.18, "illicit_flow_risk": 0.32},
    {"archetype": "remittance-dependent middle-income economy", "unbanked_share": 0.28, "digital_access": 0.70, "regulatory_trust": 0.58, "currency_instability": 0.44, "illicit_flow_risk": 0.42},
    {"archetype": "capital-control cautious economy", "unbanked_share": 0.17, "digital_access": 0.78, "regulatory_trust": 0.62, "currency_instability": 0.30, "illicit_flow_risk": 0.66},
    {"archetype": "small open trade hub", "unbanked_share": 0.08, "digital_access": 0.88, "regulatory_trust": 0.76, "currency_instability": 0.27, "illicit_flow_risk": 0.45},
]

ADOPTION_STRATEGIES = [
    {"strategy": "wallet-first inclusion pilot", "access_gain": 0.30, "security_gain": 0.12, "stability_gain": 0.08, "sovereignty_cost": 0.18},
    {"strategy": "regulated stable settlement layer", "access_gain": 0.18, "security_gain": 0.24, "stability_gain": 0.27, "sovereignty_cost": 0.24},
    {"strategy": "cross-border remittance corridor", "access_gain": 0.22, "security_gain": 0.16, "stability_gain": 0.14, "sovereignty_cost": 0.12},
    {"strategy": "full national-currency substitution", "access_gain": 0.32, "security_gain": 0.18, "stability_gain": 0.22, "sovereignty_cost": 0.58},
    {"strategy": "public oversight plus privacy-preserving compliance", "access_gain": 0.20, "security_gain": 0.34, "stability_gain": 0.24, "sovereignty_cost": 0.20},
]

OVERSIGHT_MECHANISMS = [
    "transparent reserve or collateral audits for value stability",
    "privacy-preserving identity attestation for high-risk transactions",
    "international dispute, sanctions, and consumer-protection protocol",
    "cybersecurity stress tests and public incident reporting",
    "monetary-policy interface so countries do not have to abandon local currency",
]


def clean_float(value: float, digits: int = 6) -> float:
    return round(float(value), digits)


def ensure_pdf_exists() -> None:
    if not PDF_PATH.exists():
        raise FileNotFoundError(f"Official problem PDF not found: {PDF_PATH}")


def build_adoption_viability_model() -> tuple[pd.DataFrame, dict[str, Any]]:
    rows = []
    for country in COUNTRY_ARCHETYPES:
        growth_pressure = 0.40 * float(country["unbanked_share"]) + 0.35 * float(country["currency_instability"]) + 0.25 * float(country["digital_access"])
        access_score = 0.55 * float(country["digital_access"]) + 0.45 * float(country["unbanked_share"])
        security_score = 0.60 * float(country["regulatory_trust"]) + 0.40 * (1.0 - float(country["illicit_flow_risk"]))
        stability_score = 0.50 * (1.0 - float(country["currency_instability"])) + 0.30 * float(country["regulatory_trust"]) + 0.20 * float(country["digital_access"])
        viability = 0.28 * growth_pressure + 0.26 * access_score + 0.25 * security_score + 0.21 * stability_score
        rows.append(
            {
                **country,
                "growth_pressure": clean_float(growth_pressure, 4),
                "access_score": clean_float(access_score, 4),
                "security_score": clean_float(security_score, 4),
                "stability_score": clean_float(stability_score, 4),
                "adoption_viability_score": clean_float(viability, 4),
                "recommended_path": "pilot access layer before monetary substitution" if viability < 0.62 else "regulated settlement layer with phased consumer wallets",
            }
        )
    df = pd.DataFrame(rows).sort_values("adoption_viability_score", ascending=False)
    df.to_csv(ARTIFACT_DIR / "currency_adoption_viability.csv", index=False)
    return df, {
        "country_rows": df.to_dict(orient="records"),
        "model": "weighted viability model over growth, access, security, and stability factors named in the official statement",
    }


def build_strategy_scores(country_df: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, Any]]:
    mean_access_need = float((1.0 - country_df["access_score"]).mean())
    mean_security_need = float((1.0 - country_df["security_score"]).mean())
    mean_stability_need = float((1.0 - country_df["stability_score"]).mean())
    rows = []
    for strategy in ADOPTION_STRATEGIES:
        score = (
            mean_access_need * float(strategy["access_gain"])
            + mean_security_need * float(strategy["security_gain"])
            + mean_stability_need * float(strategy["stability_gain"])
            - 0.42 * float(strategy["sovereignty_cost"])
        )
        rows.append({**strategy, "portfolio_score": clean_float(score, 4)})
    df = pd.DataFrame(rows).sort_values("portfolio_score", ascending=False)
    df.to_csv(ARTIFACT_DIR / "currency_strategy_scores.csv", index=False)
    return df, {
        "strategy_rows": df.to_dict(orient="records"),
        "recommended_strategy": df.iloc[0].to_dict(),
        "adoption_rule": "start with regulated settlement, remittance, and wallet inclusion layers; avoid forcing full currency abandonment early.",
    }


def build_oversight_mechanism() -> dict[str, Any]:
    return {
        "mechanisms": OVERSIGHT_MECHANISMS,
        "oversight_design": "decentralized ledger operation can coexist with public oversight if high-risk entry points, reserves, consumer protection, and cybersecurity evidence are auditable.",
    }


def build_long_term_effects() -> tuple[pd.DataFrame, dict[str, Any]]:
    rows = [
        {"sector": "banking industry", "effect": "margin compression on payments, new custody and compliance services", "risk": 0.62, "opportunity": 0.74},
        {"sector": "local economy", "effect": "better inclusion and remittances, but faster capital flight if rules are weak", "risk": 0.58, "opportunity": 0.70},
        {"sector": "regional economy", "effect": "lower settlement friction and more visible cross-border flows", "risk": 0.44, "opportunity": 0.68},
        {"sector": "world economy", "effect": "common settlement rails improve liquidity but amplify cyber and governance shocks", "risk": 0.66, "opportunity": 0.72},
        {"sector": "international relations", "effect": "new disputes over oversight, sanctions, taxation, and monetary sovereignty", "risk": 0.71, "opportunity": 0.55},
    ]
    df = pd.DataFrame(rows)
    df.to_csv(ARTIFACT_DIR / "currency_long_term_effects.csv", index=False)
    return df, {
        "effect_rows": df.to_dict(orient="records"),
        "interpretation": "The system is possible only as a governed financial network, not as an unregulated replacement for every national currency.",
    }


def write_frontier(country_df: pd.DataFrame, strategy_df: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(9.0, 5.0))
    ax.bar(country_df["archetype"], country_df["adoption_viability_score"], color="#4d6f88")
    ax.set_ylabel("Adoption viability score")
    ax.set_title("Universal Digital Currency Viability by Country Archetype")
    ax.tick_params(axis="x", rotation=25)
    ax.grid(axis="y", alpha=0.22)
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "currency_viability_frontier.png", dpi=180)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(9.0, 5.0))
    ax.bar(strategy_df["strategy"], strategy_df["portfolio_score"], color="#6f8751")
    ax.set_ylabel("Portfolio score")
    ax.set_title("Adoption Strategy Scores")
    ax.tick_params(axis="x", rotation=25)
    ax.grid(axis="y", alpha=0.22)
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "currency_strategy_frontier.png", dpi=180)
    plt.close(fig)


def build_result(
    adoption_viability_model: dict[str, Any],
    adoption_strategy_model: dict[str, Any],
    oversight_mechanism: dict[str, Any],
    long_term_effects: dict[str, Any],
) -> dict[str, Any]:
    return {
        "problem_id": "2019-P06",
        "title": "Universal, Decentralized, Digital Currency: Is it possible?",
        "data_source": {
            "type": "official_statement_parameters",
            "root": str(ARCHIVE_ROOT / "official_assets"),
            "source_pdf": str(PDF_PATH),
            "official_requirements": {
                "universal_decentralized_digital_currency": True,
                "growth_access_security_stability": True,
                "individual_national_global_levels": True,
                "adoption_strategy_not_existing_coin": True,
                "oversight_mechanisms": True,
                "long_term_effects": True,
                "one_page_policy_recommendation": True,
            },
            "parameters": {
                "country_archetypes": COUNTRY_ARCHETYPES,
                "adoption_strategies": ADOPTION_STRATEGIES,
                "oversight_mechanisms": OVERSIGHT_MECHANISMS,
                "source_note": "Official PDF statement factors only; country archetypes and scores are explicit deterministic modeling inputs for audit and replacement.",
            },
        },
        "adoption_viability_model": adoption_viability_model,
        "adoption_strategy_model": adoption_strategy_model,
        "oversight_mechanism": oversight_mechanism,
        "long_term_effects": long_term_effects,
        "policy_recommendation": (
            "Policy recommendation for national leaders: support a universal decentralized digital currency only through phased pilots, regulated settlement rails, privacy-preserving compliance, and audited stability mechanisms. "
            "Do not require immediate abandonment of national currencies. Countries with high unbanked shares and unstable currency conditions should start with wallet access and remittance corridors; high-trust banking economies should focus on oversight, custody, and interoperability."
        ),
        "assumption_audit": {
            "truthfulness_note": "This workflow uses official statement parameters and transparent deterministic policy scenarios; it does not use random placeholder data.",
            "model_limits": [
                "COMAP did not provide country-level banking, crypto adoption, or cybersecurity data for this problem.",
                "Country archetypes and policy weights are transparent scenario inputs, not a forecast of any named existing currency.",
                "A full policy paper should calibrate with World Bank Findex, IMF inflation, BIS payment data, chain-risk metrics, and national legal constraints.",
            ],
        },
    }


def build_report(result: dict[str, Any]) -> None:
    lines = [
        "# 2019 ICM-F Universal, Decentralized, Digital Currency",
        "",
        "## Data Source",
        f"- Official PDF asset: `{result['data_source']['source_pdf']}`.",
        "- No numeric COMAP attachment is supplied; this workflow uses official statement factors and explicit deterministic policy inputs.",
        "",
        "## Model Summary",
        f"- Country archetype rows: {len(result['adoption_viability_model']['country_rows'])}.",
        f"- Strategy rows: {len(result['adoption_strategy_model']['strategy_rows'])}.",
        f"- Oversight mechanisms: {len(result['oversight_mechanism']['mechanisms'])}.",
        "",
        "## Policy Recommendation",
        result["policy_recommendation"],
        "",
        "## Output Files",
        "- `currency_adoption_viability.csv`",
        "- `currency_strategy_scores.csv`",
        "- `currency_long_term_effects.csv`",
        "- `currency_viability_frontier.png`",
    ]
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ensure_pdf_exists()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    country_df, adoption_viability_model = build_adoption_viability_model()
    strategy_df, adoption_strategy_model = build_strategy_scores(country_df)
    oversight_mechanism = build_oversight_mechanism()
    _, long_term_effects = build_long_term_effects()
    write_frontier(country_df, strategy_df)
    result = build_result(adoption_viability_model, adoption_strategy_model, oversight_mechanism, long_term_effects)
    result["artifacts"] = {
        "adoption_viability": str(ARTIFACT_DIR / "currency_adoption_viability.csv"),
        "strategy_scores": str(ARTIFACT_DIR / "currency_strategy_scores.csv"),
        "long_term_effects": str(ARTIFACT_DIR / "currency_long_term_effects.csv"),
        "viability_frontier": str(ARTIFACT_DIR / "currency_viability_frontier.png"),
    }
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    build_report(result)
    print(json.dumps({"result": str(RESULT_PATH), "report": str(REPORT_PATH), "artifacts": str(ARTIFACT_DIR)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
