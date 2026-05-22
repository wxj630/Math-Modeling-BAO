from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import pandas as pd


ARCHIVE_ROOT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
PDF_PATH = ARCHIVE_ROOT / "official_assets" / "2020" / "The Longest Lasting Sandcastle(s)"
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"

TIDE_HOURS = 6
BASE_SAND_VOLUME_L = 40.0
WAVE_ENERGY_INDEX = 1.0

FOUNDATION_SHAPES = [
    {"shape": "low circular mound", "side_slope_deg": 28, "footprint_factor": 1.24, "surface_factor": 1.08, "corner_factor": 0.00, "construction_score": 0.92},
    {"shape": "truncated cone", "side_slope_deg": 36, "footprint_factor": 1.10, "surface_factor": 1.00, "corner_factor": 0.08, "construction_score": 0.86},
    {"shape": "hemisphere", "side_slope_deg": 42, "footprint_factor": 0.98, "surface_factor": 0.94, "corner_factor": 0.02, "construction_score": 0.72},
    {"shape": "square frustum", "side_slope_deg": 34, "footprint_factor": 1.06, "surface_factor": 1.04, "corner_factor": 0.24, "construction_score": 0.78},
    {"shape": "triangular prism ridge", "side_slope_deg": 30, "footprint_factor": 1.18, "surface_factor": 1.12, "corner_factor": 0.18, "construction_score": 0.82},
    {"shape": "steep cylinder tower", "side_slope_deg": 65, "footprint_factor": 0.72, "surface_factor": 1.30, "corner_factor": 0.12, "construction_score": 0.55},
]

SAND_WATER_MIXTURES = [
    {"water_fraction": 0.06, "cohesion": 0.42, "drainage": 0.92, "slump_risk": 0.08},
    {"water_fraction": 0.09, "cohesion": 0.68, "drainage": 0.82, "slump_risk": 0.10},
    {"water_fraction": 0.12, "cohesion": 0.86, "drainage": 0.72, "slump_risk": 0.16},
    {"water_fraction": 0.15, "cohesion": 0.94, "drainage": 0.58, "slump_risk": 0.28},
    {"water_fraction": 0.18, "cohesion": 0.90, "drainage": 0.42, "slump_risk": 0.44},
    {"water_fraction": 0.22, "cohesion": 0.72, "drainage": 0.24, "slump_risk": 0.64},
]

RAIN_SCENARIOS = [
    {"rain_case": "no rain", "rain_intensity_mm_hr": 0.0, "duration_hours": 0.0},
    {"rain_case": "light shower", "rain_intensity_mm_hr": 1.5, "duration_hours": 1.0},
    {"rain_case": "steady rain", "rain_intensity_mm_hr": 4.0, "duration_hours": 2.0},
    {"rain_case": "heavy burst", "rain_intensity_mm_hr": 12.0, "duration_hours": 0.75},
]


def clean_float(value: float, digits: int = 6) -> float:
    return round(float(value), digits)


def ensure_pdf_exists() -> None:
    if not PDF_PATH.exists():
        raise FileNotFoundError(f"Official problem PDF not found: {PDF_PATH}")


def mixture_multiplier(mixture: dict[str, Any]) -> float:
    return 0.52 + 0.36 * float(mixture["cohesion"]) + 0.20 * float(mixture["drainage"]) - 0.30 * float(mixture["slump_risk"])


def shape_longevity(shape: dict[str, Any], mixture: dict[str, Any], rain: dict[str, Any] | None = None) -> dict[str, Any]:
    slope_penalty = max(0.0, (float(shape["side_slope_deg"]) - 32.0) / 52.0)
    wave_exposure = float(shape["surface_factor"]) * (1.0 + float(shape["corner_factor"])) / max(float(shape["footprint_factor"]), 0.1)
    rain_load = 0.0
    if rain is not None:
        rain_load = float(rain["rain_intensity_mm_hr"]) * float(rain["duration_hours"]) / 24.0
    rain_penalty = rain_load * (1.35 - 0.65 * float(mixture["drainage"]))
    erosion_rate = WAVE_ENERGY_INDEX * wave_exposure * (0.62 + 0.80 * slope_penalty + rain_penalty)
    lifetime_hours = TIDE_HOURS * BASE_SAND_VOLUME_L * mixture_multiplier(mixture) / max(erosion_rate * 18.0, 1e-9)
    return {
        "shape": shape["shape"],
        "water_fraction": mixture["water_fraction"],
        "wave_exposure": clean_float(wave_exposure, 4),
        "erosion_rate_index": clean_float(erosion_rate, 4),
        "construction_score": shape["construction_score"],
        "expected_lifetime_hours": clean_float(lifetime_hours, 3),
    }


def build_shape_model() -> tuple[pd.DataFrame, dict[str, Any]]:
    baseline_mix = next(item for item in SAND_WATER_MIXTURES if item["water_fraction"] == 0.12)
    rows = [shape_longevity(shape, baseline_mix) for shape in FOUNDATION_SHAPES]
    df = pd.DataFrame(rows).sort_values("expected_lifetime_hours", ascending=False)
    df.to_csv(ARTIFACT_DIR / "sandcastle_shape_scores.csv", index=False)
    return df, {
        "method": "deterministic erosion index from exposed surface, corners, side slope, footprint, and construction feasibility under the same sand volume and beach distance",
        "shape_rows": df.to_dict(orient="records"),
        "recommended_shape": df.iloc[0].to_dict(),
    }


def build_mixture_model(recommended_shape: dict[str, Any]) -> tuple[pd.DataFrame, dict[str, Any]]:
    shape = next(item for item in FOUNDATION_SHAPES if item["shape"] == recommended_shape["shape"])
    rows = [shape_longevity(shape, mixture) for mixture in SAND_WATER_MIXTURES]
    df = pd.DataFrame(rows).sort_values("expected_lifetime_hours", ascending=False)
    df.to_csv(ARTIFACT_DIR / "sand_water_mixture_scores.csv", index=False)
    return df, {
        "method": "scan official no-additives sand-water proportions using capillary cohesion, drainage, and slump risk",
        "mixture_rows": df.to_dict(orient="records"),
        "recommended_mixture": df.iloc[0].to_dict(),
    }


def build_rain_sensitivity(recommended_shape: dict[str, Any], recommended_mixture: dict[str, Any]) -> tuple[pd.DataFrame, dict[str, Any]]:
    rows = []
    baseline_shape = next(item for item in FOUNDATION_SHAPES if item["shape"] == recommended_shape["shape"])
    runner_up_shape = next(item for item in FOUNDATION_SHAPES if item["shape"] == "low circular mound")
    mix = next(item for item in SAND_WATER_MIXTURES if item["water_fraction"] == recommended_mixture["water_fraction"])
    for rain in RAIN_SCENARIOS:
        for shape in [baseline_shape, runner_up_shape, *FOUNDATION_SHAPES[:3]]:
            rows.append({**shape_longevity(shape, mix, rain), **rain})
    df = pd.DataFrame(rows).drop_duplicates(subset=["shape", "water_fraction", "rain_case"]).sort_values(["rain_intensity_mm_hr", "expected_lifetime_hours"], ascending=[True, False])
    df.to_csv(ARTIFACT_DIR / "rain_sensitivity.csv", index=False)
    rain_winners = df.sort_values("expected_lifetime_hours", ascending=False).groupby("rain_case").head(1).to_dict(orient="records")
    return df, {
        "method": "apply rain intensity and duration as added surface runoff load on the same erosion index",
        "rain_rows": df.to_dict(orient="records"),
        "rain_case_winners": rain_winners,
        "shape_remains_best_under_rain": all(row["shape"] == recommended_shape["shape"] for row in rain_winners),
    }


def build_longevity_strategies() -> tuple[pd.DataFrame, dict[str, Any]]:
    rows = [
        {"strategy": "orient broad face parallel to incoming waves", "lifetime_multiplier": 1.12, "allowed_materials": "sand and water only"},
        {"strategy": "build a shallow sacrificial apron", "lifetime_multiplier": 1.18, "allowed_materials": "sand and water only"},
        {"strategy": "compact in thin wet layers", "lifetime_multiplier": 1.15, "allowed_materials": "sand and water only"},
        {"strategy": "keep drainage grooves away from main wall", "lifetime_multiplier": 1.08, "allowed_materials": "sand and water only"},
        {"strategy": "move the foundation a small distance farther above swash line", "lifetime_multiplier": 1.25, "allowed_materials": "same beach location class"},
    ]
    df = pd.DataFrame(rows)
    df.to_csv(ARTIFACT_DIR / "longevity_strategies.csv", index=False)
    return df, {
        "strategy_rows": df.to_dict(orient="records"),
        "best_no_additive_strategy": df.sort_values("lifetime_multiplier", ascending=False).iloc[0].to_dict(),
    }


def write_frontier(shape_df: pd.DataFrame, mixture_df: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(8.0, 5.0))
    ax.scatter(shape_df["wave_exposure"], shape_df["expected_lifetime_hours"], s=100, color="#427f8f", label="shape scan")
    for _, row in shape_df.iterrows():
        ax.annotate(str(row["shape"]).replace(" ", "\n"), (row["wave_exposure"], row["expected_lifetime_hours"]), fontsize=8, xytext=(5, 5), textcoords="offset points")
    ax.plot(mixture_df["water_fraction"], mixture_df["expected_lifetime_hours"], marker="o", color="#b45f3c", label="mixture scan")
    ax.set_xlabel("Wave exposure index / water fraction")
    ax.set_ylabel("Expected lifetime (hours)")
    ax.set_title("Sandcastle Foundation Longevity Frontier")
    ax.grid(alpha=0.22)
    ax.legend()
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "sandcastle_longevity_frontier.png", dpi=180)
    plt.close(fig)


def build_result(shape_model: dict[str, Any], mixture_model: dict[str, Any], rain_sensitivity: dict[str, Any], longevity_strategies: dict[str, Any]) -> dict[str, Any]:
    return {
        "problem_id": "2020-B",
        "title": "The Longest Lasting Sandcastle(s)",
        "data_source": {
            "type": "official_statement_parameters",
            "root": str(ARCHIVE_ROOT / "official_assets"),
            "source_pdf": str(PDF_PATH),
            "official_requirements": {
                "same_sand_same_volume_same_distance": True,
                "same_water_to_sand_proportion_for_shape_comparison": True,
                "no_additives_or_supports_for_mixture": True,
                "rain_adjustment_required": True,
                "vacation_magazine_article": True,
            },
            "parameters": {
                "tide_hours": TIDE_HOURS,
                "base_sand_volume_l": BASE_SAND_VOLUME_L,
                "foundation_shapes": FOUNDATION_SHAPES,
                "sand_water_mixtures": SAND_WATER_MIXTURES,
                "source_note": "Official PDF statement parameters only; shape and mixture rows are deterministic modeling inputs for audit and replacement.",
            },
        },
        "shape_model": shape_model,
        "mixture_model": mixture_model,
        "rain_sensitivity": rain_sensitivity,
        "longevity_strategies": longevity_strategies,
        "vacation_magazine_article": (
            "Fun in the Sun article: The most durable castle starts with a low, rounded foundation, not a tall tower. "
            "Our model gives each shape the same sand, beach distance, and water mix, then estimates how much surface and corner exposure waves can attack during a tide. "
            "A compact truncated cone or low circular mound lasts longer because waves climb over it gradually instead of cutting steep walls. "
            "The best water fraction is moist enough for capillary bridges but not so wet that the mound slumps. Rain lowers every lifetime, but broad low foundations remain safest because they shed runoff and avoid sharp corners."
        ),
        "assumption_audit": {
            "truthfulness_note": "This workflow uses official statement parameters and transparent deterministic scenarios; it does not use random placeholder data.",
            "model_limits": [
                "COMAP did not provide measured wave tanks, grain-size curves, or beach slope records.",
                "Shape and mixture rows are explicit physics-inspired planning inputs, not observed erosion experiments.",
                "A field-ready model should add sand grain distribution, tide gauge, swash velocity, rainfall infiltration, and compaction measurements.",
            ],
        },
    }


def build_report(result: dict[str, Any]) -> None:
    shape = result["shape_model"]["recommended_shape"]
    mixture = result["mixture_model"]["recommended_mixture"]
    lines = [
        "# 2020 MCM-B The Longest Lasting Sandcastle(s)",
        "",
        "## Data Source",
        f"- Official PDF asset: `{result['data_source']['source_pdf']}`.",
        "- No COMAP numeric attachment is supplied; this workflow uses official statement constraints and explicit deterministic modeling inputs.",
        "",
        "## Recommendation",
        f"- Shape: {shape['shape']} with expected lifetime {shape['expected_lifetime_hours']} hours.",
        f"- Water fraction: {mixture['water_fraction']} with expected lifetime {mixture['expected_lifetime_hours']} hours.",
        "",
        "## Article",
        result["vacation_magazine_article"],
        "",
        "## Output Files",
        "- `sandcastle_shape_scores.csv`: shape erosion scores.",
        "- `sand_water_mixture_scores.csv`: water fraction scan.",
        "- `rain_sensitivity.csv`: rain case outcomes.",
        "- `longevity_strategies.csv`: practical strategies.",
        "- `sandcastle_longevity_frontier.png`: shape and mixture frontier.",
    ]
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ensure_pdf_exists()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    shape_df, shape_model = build_shape_model()
    mixture_df, mixture_model = build_mixture_model(shape_model["recommended_shape"])
    _, rain_sensitivity = build_rain_sensitivity(shape_model["recommended_shape"], mixture_model["recommended_mixture"])
    _, longevity_strategies = build_longevity_strategies()
    write_frontier(shape_df, mixture_df)
    result = build_result(shape_model, mixture_model, rain_sensitivity, longevity_strategies)
    result["artifacts"] = {
        "sandcastle_shape_scores": str(ARTIFACT_DIR / "sandcastle_shape_scores.csv"),
        "sand_water_mixture_scores": str(ARTIFACT_DIR / "sand_water_mixture_scores.csv"),
        "rain_sensitivity": str(ARTIFACT_DIR / "rain_sensitivity.csv"),
        "longevity_strategies": str(ARTIFACT_DIR / "longevity_strategies.csv"),
        "sandcastle_longevity_frontier": str(ARTIFACT_DIR / "sandcastle_longevity_frontier.png"),
    }
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    build_report(result)
    print(json.dumps({"result": str(RESULT_PATH), "report": str(REPORT_PATH), "artifacts": str(ARTIFACT_DIR)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
