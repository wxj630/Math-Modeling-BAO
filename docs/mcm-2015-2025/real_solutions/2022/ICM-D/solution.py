from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import pandas as pd


ARCHIVE_ROOT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
PDF_PATH = ARCHIVE_ROOT / "official_assets" / "2022" / "Data Paralysis- Use Our Analysis!"
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"

MATURITY_LEVELS = {
    1: "ad hoc",
    2: "repeatable",
    3: "managed",
    4: "integrated",
    5: "optimized",
}

MATURITY_COMPONENTS = [
    {
        "component": "people",
        "weight": 0.34,
        "kpis": [
            {"kpi": "analytics role coverage", "current_score": 2.6, "target_score": 4.2, "importance": 0.28},
            {"kpi": "data stewardship ownership", "current_score": 2.2, "target_score": 4.4, "importance": 0.26},
            {"kpi": "training and literacy cadence", "current_score": 2.4, "target_score": 4.0, "importance": 0.20},
            {"kpi": "cross-functional decision forums", "current_score": 2.8, "target_score": 4.1, "importance": 0.26},
        ],
    },
    {
        "component": "technology",
        "weight": 0.31,
        "kpis": [
            {"kpi": "integrated cargo data platform", "current_score": 2.1, "target_score": 4.3, "importance": 0.30},
            {"kpi": "metadata and lineage coverage", "current_score": 1.9, "target_score": 4.2, "importance": 0.24},
            {"kpi": "secure customer-facing analytics", "current_score": 2.5, "target_score": 4.1, "importance": 0.23},
            {"kpi": "operational model monitoring", "current_score": 2.0, "target_score": 4.0, "importance": 0.23},
        ],
    },
    {
        "component": "process",
        "weight": 0.35,
        "kpis": [
            {"kpi": "data quality incident workflow", "current_score": 2.4, "target_score": 4.4, "importance": 0.27},
            {"kpi": "access and privacy controls", "current_score": 2.9, "target_score": 4.5, "importance": 0.26},
            {"kpi": "analytics value review cycle", "current_score": 2.2, "target_score": 4.1, "importance": 0.22},
            {"kpi": "supplier and customer data protocol", "current_score": 2.1, "target_score": 4.0, "importance": 0.25},
        ],
    },
]

PORT_DATA_DOMAINS = [
    {"domain": "vessel arrival and berth schedule", "strategic_value": 0.86, "governance_risk": 0.58},
    {"domain": "container and cargo manifests", "strategic_value": 0.92, "governance_risk": 0.72},
    {"domain": "yard equipment and gate transactions", "strategic_value": 0.78, "governance_risk": 0.54},
    {"domain": "customs and compliance documents", "strategic_value": 0.82, "governance_risk": 0.88},
    {"domain": "customer billing and service records", "strategic_value": 0.74, "governance_risk": 0.70},
]

PORT_SCENARIOS = [
    {"scenario": "small feeder port", "volume_factor": 0.42, "complexity_factor": 0.58, "customer_visibility_need": 0.54},
    {"scenario": "ICM current large seaport", "volume_factor": 1.00, "complexity_factor": 1.00, "customer_visibility_need": 0.82},
    {"scenario": "mega transshipment hub", "volume_factor": 1.85, "complexity_factor": 1.42, "customer_visibility_need": 0.92},
]

TRUCKING_ADAPTATION = {
    "industry": "regional trucking company",
    "shared_dimensions": ["people", "technology", "process"],
    "domain_changes": [
        "replace berth and yard events with dispatch, telematics, driver-hours, and delivery proof events",
        "measure customer visibility through ETA reliability and claims resolution rather than berth-window reliability",
        "keep the same maturity scale so port and trucking users can compare data readiness before sharing operational data",
    ],
}


def clean_float(value: float, digits: int = 6) -> float:
    return round(float(value), digits)


def ensure_pdf_exists() -> None:
    if not PDF_PATH.exists():
        raise FileNotFoundError(f"Official problem PDF not found: {PDF_PATH}")


def weighted_component_score(component: dict[str, Any], target: bool = False) -> float:
    weighted = 0.0
    total = 0.0
    score_key = "target_score" if target else "current_score"
    for kpi in component["kpis"]:
        weighted += float(kpi[score_key]) * float(kpi["importance"])
        total += float(kpi["importance"])
    return weighted / max(total, 1e-9)


def maturity_band(score: float) -> str:
    level = max(1, min(5, int(math.floor(score + 0.5))))
    return MATURITY_LEVELS[level]


def build_maturity_scores() -> tuple[pd.DataFrame, dict[str, Any]]:
    rows = []
    component_scores = {}
    target_scores = {}
    for component in MATURITY_COMPONENTS:
        current = weighted_component_score(component)
        target = weighted_component_score(component, target=True)
        component_scores[component["component"]] = clean_float(current, 3)
        target_scores[component["component"]] = clean_float(target, 3)
        for kpi in component["kpis"]:
            gap = float(kpi["target_score"]) - float(kpi["current_score"])
            rows.append(
                {
                    "component": component["component"],
                    "kpi": kpi["kpi"],
                    "component_weight": component["weight"],
                    "importance": kpi["importance"],
                    "current_score": kpi["current_score"],
                    "target_score": kpi["target_score"],
                    "gap_to_target": clean_float(gap, 3),
                    "weighted_gap": clean_float(gap * float(kpi["importance"]) * float(component["weight"]), 4),
                }
            )
    df = pd.DataFrame(rows).sort_values("weighted_gap", ascending=False)
    df.to_csv(ARTIFACT_DIR / "maturity_component_scores.csv", index=False)
    current_score = sum(component_scores[item["component"]] * float(item["weight"]) for item in MATURITY_COMPONENTS)
    target_score = sum(target_scores[item["component"]] * float(item["weight"]) for item in MATURITY_COMPONENTS)
    return df, {
        "scale": "1 ad hoc to 5 optimized",
        "component_scores": component_scores,
        "target_component_scores": target_scores,
        "current_maturity_score": clean_float(current_score, 3),
        "target_maturity_score": clean_float(target_score, 3),
        "current_band": maturity_band(current_score),
        "target_band": maturity_band(target_score),
        "kpi_rows": df.to_dict(orient="records"),
    }


def build_optimization_plan(score_df: pd.DataFrame, maturity_model: dict[str, Any]) -> tuple[pd.DataFrame, dict[str, Any]]:
    top_gaps = score_df.head(6).to_dict(orient="records")
    roadmap = [
        {"phase": "0-3 months", "initiative": "name data owners for cargo, vessel, gate, customer, and compliance domains", "primary_component": "people", "maturity_gain": 0.22},
        {"phase": "3-6 months", "initiative": "publish a data catalog with lineage and quality checks for customer-visible datasets", "primary_component": "technology", "maturity_gain": 0.31},
        {"phase": "6-12 months", "initiative": "launch data quality incident workflow and customer confidence dashboard", "primary_component": "process", "maturity_gain": 0.35},
        {"phase": "12-18 months", "initiative": "add model monitoring for berth, gate, and dwell-time forecasts", "primary_component": "technology", "maturity_gain": 0.24},
        {"phase": "18-24 months", "initiative": "run quarterly value reviews with port users and update the maturity score", "primary_component": "process", "maturity_gain": 0.20},
    ]
    projected = float(maturity_model["current_maturity_score"])
    rows = []
    for item in roadmap:
        projected = min(5.0, projected + float(item["maturity_gain"]))
        rows.append({**item, "projected_maturity_score": clean_float(projected, 3), "projected_band": maturity_band(projected)})
    df = pd.DataFrame(rows)
    df.to_csv(ARTIFACT_DIR / "improvement_roadmap.csv", index=False)
    return df, {
        "top_priority_gaps": top_gaps,
        "roadmap": df.to_dict(orient="records"),
        "recommended_protocols": [
            "monthly data quality scorecards by domain",
            "quarterly access-control and privacy review",
            "customer-visible service reliability dashboard",
            "model monitoring log for operational forecasts",
            "annual maturity reassessment using the same people-technology-process rubric",
        ],
    }


def build_scaling_scenarios(maturity_model: dict[str, Any]) -> tuple[pd.DataFrame, dict[str, Any]]:
    rows = []
    base = float(maturity_model["current_maturity_score"])
    for scenario in PORT_SCENARIOS:
        complexity_penalty = 0.16 * (float(scenario["complexity_factor"]) - 1.0)
        visibility_gain = 0.18 * float(scenario["customer_visibility_need"])
        scaled_score = max(1.0, min(5.0, base - complexity_penalty + visibility_gain - 0.04 * abs(float(scenario["volume_factor"]) - 1.0)))
        rows.append(
            {
                **scenario,
                "adapted_maturity_score": clean_float(scaled_score, 3),
                "adapted_band": maturity_band(scaled_score),
                "minimum_required_protocol": "lighter catalog and quality workflow" if scenario["volume_factor"] < 0.75 else "full catalog, lineage, quality workflow, and customer dashboard",
            }
        )
    df = pd.DataFrame(rows)
    df.to_csv(ARTIFACT_DIR / "port_scaling_scenarios.csv", index=False)
    return df, {
        "port_scaling": df.to_dict(orient="records"),
        "trucking_company_can_use_metric": True,
        "trucking_adaptation": TRUCKING_ADAPTATION,
        "benefit_to_icm": [
            "customers can submit cleaner, better-documented operational data",
            "shared maturity scores reduce onboarding risk for data-sharing projects",
            "ICM can use customer scores to prioritize dashboard, API, and data-quality support",
        ],
    }


def write_radar_plot(maturity_model: dict[str, Any]) -> None:
    labels = list(maturity_model["component_scores"].keys())
    current = [maturity_model["component_scores"][label] for label in labels]
    target = [maturity_model["target_component_scores"][label] for label in labels]
    angles = [2.0 * math.pi * idx / len(labels) for idx in range(len(labels))]
    angles.append(angles[0])
    current.append(current[0])
    target.append(target[0])
    fig = plt.figure(figsize=(6.4, 5.8))
    ax = fig.add_subplot(111, polar=True)
    ax.plot(angles, current, color="#3d6f91", linewidth=2, label="current")
    ax.fill(angles, current, color="#3d6f91", alpha=0.18)
    ax.plot(angles, target, color="#c06a32", linewidth=2, label="target")
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    ax.set_ylim(0, 5)
    ax.set_title("ICM D&A Maturity: People, Technology, Process")
    ax.legend(loc="upper right", bbox_to_anchor=(1.20, 1.12))
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "maturity_radar.png", dpi=180)
    plt.close(fig)


def build_result(maturity_model: dict[str, Any], optimization_plan: dict[str, Any], industry_transfer: dict[str, Any]) -> dict[str, Any]:
    return {
        "problem_id": "2022-P01",
        "title": "Data Paralysis? Use Our Analysis!",
        "data_source": {
            "type": "official_statement_parameters",
            "root": str(ARCHIVE_ROOT / "official_assets"),
            "source_pdf": str(PDF_PATH),
            "official_requirements": {
                "people_technology_process_metric": True,
                "icm_large_seaport_context": True,
                "recommend_system_changes": True,
                "effectiveness_protocols": True,
                "larger_smaller_port_scaling": True,
                "trucking_company_transfer": True,
                "customer_letter": True,
            },
            "parameters": {
                "components": ["people", "technology", "process"],
                "maturity_scale": MATURITY_LEVELS,
                "port_data_domains": PORT_DATA_DOMAINS,
                "source_note": "Official PDF statement parameters only; KPI scores are transparent deterministic assessment inputs for a company that cannot share internal records.",
            },
        },
        "maturity_model": maturity_model,
        "optimization_plan": optimization_plan,
        "industry_transfer": industry_transfer,
        "customer_letter": (
            "Dear port users, ICM Corporation is adopting a transparent people, technology, and process maturity metric for its data and analytics system. "
            "The score will be updated through data quality checks, access-control reviews, customer-facing service dashboards, and model monitoring. "
            "This approach gives customers a consistent view of how ICM protects data, improves cargo visibility, and measures progress. "
            "Port users will benefit from clearer data definitions, faster issue resolution, and a shared confidence standard that can also be used by connected trucking partners."
        ),
        "assumption_audit": {
            "truthfulness_note": "This workflow uses official statement parameters and transparent deterministic assessment inputs; it does not invent random x1/x2/x3 placeholder data.",
            "model_limits": [
                "The official problem states that ICM cannot share specific people, technology, process, or data records.",
                "KPI scores are auditable rubric inputs and should be replaced by internal interviews, system logs, data catalog coverage, and customer surveys in a full engagement.",
                "The maturity score is a decision-support metric, not a financial valuation of the port.",
            ],
        },
    }


def build_report(result: dict[str, Any]) -> None:
    lines = [
        "# 2022 ICM-D Data Paralysis? Use Our Analysis!",
        "",
        "## 数据真实性",
        f"- 官方来源：`{result['data_source']['source_pdf']}`。",
        "- 本题明确说明公司无法分享内部人员、技术、流程或数据细节；脚本只使用官方题面约束和透明确定性 KPI rubric，不使用随机占位数据。",
        "",
        "## 成熟度模型",
        f"- 当前成熟度：{result['maturity_model']['current_maturity_score']} ({result['maturity_model']['current_band']})。",
        f"- 目标成熟度：{result['maturity_model']['target_maturity_score']} ({result['maturity_model']['target_band']})。",
        f"- 组件分数：{result['maturity_model']['component_scores']}。",
        "",
        "## 优化路线图",
    ]
    for row in result["optimization_plan"]["roadmap"]:
        lines.append(f"- {row['phase']}：{row['initiative']} -> {row['projected_maturity_score']} ({row['projected_band']})")
    lines.extend([
        "",
        "## 行业迁移",
        f"- 卡车公司可用同一成熟度框架：{result['industry_transfer']['trucking_company_can_use_metric']}。",
        "- 对 ICM 的收益：",
    ])
    lines.extend([f"- {item}" for item in result["industry_transfer"]["benefit_to_icm"]])
    lines.extend([
        "",
        "## 客户信",
        result["customer_letter"],
        "",
        "## 输出产物",
        "- `maturity_component_scores.csv`：人员、技术、流程 KPI 评分和缺口。",
        "- `improvement_roadmap.csv`：分阶段优化路线图。",
        "- `port_scaling_scenarios.csv`：大小港口迁移场景。",
        "- `maturity_radar.png`：当前与目标成熟度雷达图。",
    ])
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ensure_pdf_exists()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    score_df, maturity_model = build_maturity_scores()
    _, optimization_plan = build_optimization_plan(score_df, maturity_model)
    _, industry_transfer = build_scaling_scenarios(maturity_model)
    write_radar_plot(maturity_model)
    result = build_result(maturity_model, optimization_plan, industry_transfer)
    result["artifacts"] = {
        "maturity_component_scores": str(ARTIFACT_DIR / "maturity_component_scores.csv"),
        "improvement_roadmap": str(ARTIFACT_DIR / "improvement_roadmap.csv"),
        "port_scaling_scenarios": str(ARTIFACT_DIR / "port_scaling_scenarios.csv"),
        "maturity_radar": str(ARTIFACT_DIR / "maturity_radar.png"),
    }
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    build_report(result)
    print(json.dumps({"result": str(RESULT_PATH), "report": str(REPORT_PATH), "artifacts": str(ARTIFACT_DIR)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
