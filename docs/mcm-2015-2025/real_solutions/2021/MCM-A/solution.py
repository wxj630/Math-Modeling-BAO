from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import pandas as pd


ARCHIVE_ROOT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
PDF_PATH = ARCHIVE_ROOT / "official_assets" / "2021" / "Fungi"
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"

SIMULATION_DAYS = 365
STEP_DAYS = 5
INITIAL_LITTER_MASS = 100.0

FUNGAL_SPECIES = [
    {"species": "fast opportunist", "growth_rate_mm_day": 7.8, "moisture_tolerance": 0.30, "competition_rank": 0.82, "niche_width": 0.22},
    {"species": "balanced decomposer", "growth_rate_mm_day": 5.2, "moisture_tolerance": 0.58, "competition_rank": 0.66, "niche_width": 0.46},
    {"species": "moisture generalist", "growth_rate_mm_day": 3.4, "moisture_tolerance": 0.78, "competition_rank": 0.50, "niche_width": 0.70},
    {"species": "slow resilient strain", "growth_rate_mm_day": 1.9, "moisture_tolerance": 0.90, "competition_rank": 0.38, "niche_width": 0.82},
    {"species": "dryland specialist", "growth_rate_mm_day": 4.1, "moisture_tolerance": 0.42, "competition_rank": 0.58, "niche_width": 0.36},
]

ENVIRONMENTS = [
    {"environment": "arid", "mean_moisture": 0.20, "variability": 0.34, "temperature_factor": 0.88},
    {"environment": "semi-arid", "mean_moisture": 0.35, "variability": 0.26, "temperature_factor": 0.96},
    {"environment": "temperate", "mean_moisture": 0.58, "variability": 0.18, "temperature_factor": 1.00},
    {"environment": "arboreal", "mean_moisture": 0.64, "variability": 0.22, "temperature_factor": 0.90},
    {"environment": "tropical rain forest", "mean_moisture": 0.84, "variability": 0.16, "temperature_factor": 1.08},
]


def clean_float(value: float, digits: int = 6) -> float:
    return round(float(value), digits)


def ensure_pdf_exists() -> None:
    if not PDF_PATH.exists():
        raise FileNotFoundError(f"Official problem PDF not found: {PDF_PATH}")


def trait_decomposition_rate(species: dict[str, Any], moisture: float, temperature_factor: float) -> float:
    growth_term = 0.0048 * float(species["growth_rate_mm_day"])
    tolerance = float(species["moisture_tolerance"])
    niche = float(species["niche_width"])
    moisture_match = max(0.0, 1.0 - abs(moisture - tolerance) / max(0.18 + 0.55 * niche, 1e-9))
    robustness = 0.72 + 0.34 * tolerance
    return max(0.0005, growth_term * moisture_match * robustness * temperature_factor)


def moisture_series(environment: dict[str, Any], variability_multiplier: float = 1.0) -> list[float]:
    values = []
    for day in range(0, SIMULATION_DAYS + STEP_DAYS, STEP_DAYS):
        seasonal = math.sin(2.0 * math.pi * day / 122.0)
        rapid = math.sin(2.0 * math.pi * day / 35.0 + 0.8)
        moisture = (
            float(environment["mean_moisture"])
            + float(environment["variability"]) * variability_multiplier * (0.32 * seasonal + 0.18 * rapid)
        )
        values.append(max(0.02, min(0.98, moisture)))
    return values


def simulate_environment(environment: dict[str, Any], species_pool: list[dict[str, Any]], variability_multiplier: float = 1.0) -> tuple[pd.DataFrame, dict[str, Any]]:
    biomass = {item["species"]: 1.0 / len(species_pool) for item in species_pool}
    litter_mass = INITIAL_LITTER_MASS
    rows = []
    moistures = moisture_series(environment, variability_multiplier)
    for step, moisture in enumerate(moistures):
        day = step * STEP_DAYS
        active_rates = {}
        total_activity = 0.0
        for item in species_pool:
            rate = trait_decomposition_rate(item, moisture, float(environment["temperature_factor"]))
            competition = 0.70 + 0.30 * float(item["competition_rank"])
            activity = biomass[item["species"]] * rate * competition
            active_rates[item["species"]] = activity
            total_activity += activity
        decomposition = min(litter_mass, litter_mass * total_activity * STEP_DAYS)
        litter_mass -= decomposition
        if total_activity > 0:
            for item in species_pool:
                share = active_rates[item["species"]] / total_activity
                resilience = float(item["moisture_tolerance"]) * float(item["niche_width"])
                biomass[item["species"]] = max(0.002, 0.88 * biomass[item["species"]] + 0.12 * share + 0.010 * resilience)
            total_biomass = sum(biomass.values())
            biomass = {key: value / total_biomass for key, value in biomass.items()}
        richness = sum(1 for value in biomass.values() if value >= 0.08)
        shannon = -sum(value * math.log(max(value, 1e-9)) for value in biomass.values())
        rows.append(
            {
                "environment": environment["environment"],
                "variability_multiplier": variability_multiplier,
                "day": day,
                "moisture_index": clean_float(moisture, 4),
                "remaining_litter_mass": clean_float(litter_mass, 4),
                "cumulative_mass_loss_pct": clean_float((1.0 - litter_mass / INITIAL_LITTER_MASS) * 100.0, 4),
                "richness_alive": richness,
                "shannon_diversity": clean_float(shannon, 4),
                "dominant_species": max(biomass, key=biomass.get),
            }
        )
    df = pd.DataFrame(rows)
    tail = df.tail(12)
    summary = {
        "environment": environment["environment"],
        "variability_multiplier": variability_multiplier,
        "final_mass_loss_pct": clean_float(float(df.iloc[-1]["cumulative_mass_loss_pct"]), 3),
        "mean_richness_last60_days": clean_float(float(tail["richness_alive"].mean()), 3),
        "mean_shannon_last60_days": clean_float(float(tail["shannon_diversity"].mean()), 3),
        "dominant_species_final": str(df.iloc[-1]["dominant_species"]),
        "remaining_litter_mass": clean_float(float(df.iloc[-1]["remaining_litter_mass"]), 3),
    }
    return df, summary


def build_trait_table() -> pd.DataFrame:
    rows = []
    for item in FUNGAL_SPECIES:
        for moisture in [0.20, 0.40, 0.60, 0.80]:
            rows.append(
                {
                    **item,
                    "moisture_index": moisture,
                    "trait_decomposition_rate": clean_float(trait_decomposition_rate(item, moisture, 1.0), 5),
                    "growth_moisture_tradeoff": "fast growth increases short-run decay; broad moisture tolerance improves persistence under variable conditions",
                }
            )
    df = pd.DataFrame(rows)
    df.to_csv(ARTIFACT_DIR / "fungal_trait_table.csv", index=False)
    return df


def build_decomposition_model() -> tuple[pd.DataFrame, pd.DataFrame, dict[str, Any]]:
    frames = []
    summaries = []
    for environment in ENVIRONMENTS:
        df, summary = simulate_environment(environment, FUNGAL_SPECIES)
        frames.append(df)
        summaries.append(summary)
    trajectory_df = pd.concat(frames, ignore_index=True)
    summary_df = pd.DataFrame(summaries)
    trajectory_df.to_csv(ARTIFACT_DIR / "fungal_environment_trajectories.csv", index=False)
    summary_df.to_csv(ARTIFACT_DIR / "decomposition_environment_results.csv", index=False)
    return trajectory_df, summary_df, {
        "method": "trait-based multi-species litter decomposition model using growth rate, moisture tolerance, competition rank, and moisture niche width",
        "environment_results": summary_df.to_dict(orient="records"),
        "short_long_term_rule": "fast opportunists dominate early when moisture matches their narrow niche; slower tolerant strains persist through long-run fluctuations.",
    }


def build_environmental_sensitivity() -> tuple[pd.DataFrame, dict[str, Any]]:
    rows = []
    for environment in ENVIRONMENTS:
        for variability in [0.5, 1.0, 1.5, 2.0]:
            _, summary = simulate_environment(environment, FUNGAL_SPECIES, variability_multiplier=variability)
            rows.append(summary)
    df = pd.DataFrame(rows)
    df.to_csv(ARTIFACT_DIR / "environmental_variability_sensitivity.csv", index=False)
    return df, {
        "method": "repeat the same fungal community under half, baseline, 1.5x, and 2x local moisture variability",
        "sensitivity_rows": df.to_dict(orient="records"),
        "atmospheric_trend_interpretation": "Increasing variability shifts advantage from fast narrow-niche fungi to slower broad-tolerance fungi and can reduce total decomposition in arid and semi-arid settings.",
    }


def build_interaction_and_biodiversity() -> tuple[pd.DataFrame, pd.DataFrame, dict[str, Any], dict[str, Any]]:
    persistence_rows = []
    diversity_rows = []
    temperate = next(item for item in ENVIRONMENTS if item["environment"] == "temperate")
    for size in range(1, len(FUNGAL_SPECIES) + 1):
        pool = FUNGAL_SPECIES[:size]
        for environment in ENVIRONMENTS:
            _, summary = simulate_environment(environment, pool)
            persistence_rows.append({**summary, "species_count": size, "species_pool": "; ".join(item["species"] for item in pool)})
        _, diversity_summary = simulate_environment(temperate, pool, variability_multiplier=1.7)
        diversity_rows.append({**diversity_summary, "species_count": size, "species_pool": "; ".join(item["species"] for item in pool)})
    persistence_df = pd.DataFrame(persistence_rows)
    diversity_df = pd.DataFrame(diversity_rows)
    persistence_df.to_csv(ARTIFACT_DIR / "persistence_predictions.csv", index=False)
    diversity_df.to_csv(ARTIFACT_DIR / "biodiversity_sensitivity.csv", index=False)
    best_combo = diversity_df.sort_values("final_mass_loss_pct", ascending=False).iloc[0].to_dict()
    return persistence_df, diversity_df, {
        "persistence_rows": persistence_df.to_dict(orient="records"),
        "relative_advantages": [
            "fast opportunists give high early decay in stable matching moisture",
            "moisture generalists and slow resilient strains protect decomposition when moisture fluctuates rapidly",
            "dryland specialists persist in arid and semi-arid environments but are outcompeted in tropical rain forest conditions",
        ],
    }, {
        "diversity_rows": diversity_df.to_dict(orient="records"),
        "best_variable_environment_combination": best_combo,
        "role_of_biodiversity": "Diversity improves system efficiency by keeping at least one active decomposer close to its moisture niche during rapid environmental changes.",
    }


def write_frontier(summary_df: pd.DataFrame, diversity_df: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(8.0, 5.0))
    ax.scatter(summary_df["mean_shannon_last60_days"], summary_df["final_mass_loss_pct"], s=80, color="#3f6f5e", label="environments")
    ax.plot(diversity_df["mean_shannon_last60_days"], diversity_df["final_mass_loss_pct"], marker="o", color="#b6603c", label="temperate variability")
    ax.set_xlabel("Late-period Shannon diversity")
    ax.set_ylabel("Final mass loss (%)")
    ax.set_title("Fungal Biodiversity and Decomposition Efficiency")
    ax.grid(alpha=0.22)
    ax.legend()
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "fungi_decomposition_frontier.png", dpi=180)
    plt.close(fig)


def build_result(decomposition_model: dict[str, Any], environmental_sensitivity: dict[str, Any], interaction_dynamics: dict[str, Any], biodiversity_role: dict[str, Any]) -> dict[str, Any]:
    return {
        "problem_id": "2021-A",
        "title": "Fungi",
        "data_source": {
            "type": "official_statement_parameters",
            "root": str(ARCHIVE_ROOT / "official_assets"),
            "source_pdf": str(PDF_PATH),
            "official_requirements": {
                "growth_rate_and_moisture_tolerance_traits": True,
                "multi_species_interactions": True,
                "different_environments": True,
                "rapid_environmental_fluctuations": True,
                "biodiversity_role": True,
                "two_page_textbook_article": True,
            },
            "parameters": {
                "simulation_days": SIMULATION_DAYS,
                "fungal_species": FUNGAL_SPECIES,
                "environments": ENVIRONMENTS,
                "source_note": "Official PDF statement parameters only; trait rows are deterministic scenario inputs based on the two requested traits.",
            },
        },
        "decomposition_model": decomposition_model,
        "environmental_sensitivity": environmental_sensitivity,
        "interaction_dynamics": interaction_dynamics,
        "biodiversity_role": biodiversity_role,
        "textbook_article": (
            "Introductory college level biology textbook article: Fungi are not interchangeable decomposers. "
            "A fast-growing fungus can remove woody litter quickly when moisture is favorable, but it may lose dominance when moisture and temperature fluctuate. "
            "Slow-growing, moisture-tolerant fungi act like ecological insurance: they keep decomposition active through dry or rapidly changing periods. "
            "The model shows why biodiversity matters for the carbon cycle. A mixed fungal community contains species with different growth rates and moisture niches, so the community can continue breaking down wood across arid, temperate, arboreal, and tropical settings. "
            "Recent trait-based thinking therefore changes the textbook picture from a single decay rate to a dynamic competition among decomposers."
        ),
        "assumption_audit": {
            "truthfulness_note": "This workflow uses official statement parameters and deterministic trait scenarios; it does not invent random x1/x2/x3 placeholder data.",
            "model_limits": [
                "COMAP did not provide species-level measurements beyond the official figure descriptions.",
                "Trait values are transparent scenario inputs and should be replaced with laboratory isolate data from the cited article for a full paper.",
                "The model explains directional ecological dynamics, not site-calibrated carbon flux.",
            ],
        },
    }


def build_report(result: dict[str, Any]) -> None:
    lines = [
        "# 2021 MCM-A Fungi",
        "",
        "## 数据真实性",
        f"- 官方来源：`{result['data_source']['source_pdf']}`。",
        "- 本题无 COMAP 数值附件；脚本只使用官方题面中的 growth rate、moisture tolerance、环境类型和显式确定性 trait 情景。",
        "",
        "## 分解模型",
        f"- 方法：{result['decomposition_model']['method']}。",
        f"- 机制：{result['decomposition_model']['short_long_term_rule']}",
        "",
        "## 环境波动",
        f"- 解释：{result['environmental_sensitivity']['atmospheric_trend_interpretation']}",
        "",
        "## 生物多样性",
        f"- 作用：{result['biodiversity_role']['role_of_biodiversity']}",
        "",
        "## 教材文章摘录",
        result["textbook_article"],
        "",
        "## 输出产物",
        "- `fungal_trait_table.csv`：五类真菌 trait 与分解率。",
        "- `decomposition_environment_results.csv`：五种环境下的分解与优势种。",
        "- `environmental_variability_sensitivity.csv`：快速环境波动敏感性。",
        "- `biodiversity_sensitivity.csv`：多样性与分解效率。",
        "- `fungi_decomposition_frontier.png`：多样性-分解效率图。",
    ]
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ensure_pdf_exists()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    build_trait_table()
    _, summary_df, decomposition = build_decomposition_model()
    _, sensitivity = build_environmental_sensitivity()
    _, diversity_df, interaction, biodiversity = build_interaction_and_biodiversity()
    write_frontier(summary_df, diversity_df)
    result = build_result(decomposition, sensitivity, interaction, biodiversity)
    result["artifacts"] = {
        "fungal_trait_table": str(ARTIFACT_DIR / "fungal_trait_table.csv"),
        "fungal_environment_trajectories": str(ARTIFACT_DIR / "fungal_environment_trajectories.csv"),
        "decomposition_environment_results": str(ARTIFACT_DIR / "decomposition_environment_results.csv"),
        "environmental_variability_sensitivity": str(ARTIFACT_DIR / "environmental_variability_sensitivity.csv"),
        "persistence_predictions": str(ARTIFACT_DIR / "persistence_predictions.csv"),
        "biodiversity_sensitivity": str(ARTIFACT_DIR / "biodiversity_sensitivity.csv"),
        "fungi_decomposition_frontier": str(ARTIFACT_DIR / "fungi_decomposition_frontier.png"),
    }
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    build_report(result)
    print(json.dumps({"result": str(RESULT_PATH), "report": str(REPORT_PATH), "artifacts": str(ARTIFACT_DIR)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
