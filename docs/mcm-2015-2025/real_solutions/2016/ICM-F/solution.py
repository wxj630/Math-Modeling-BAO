from __future__ import annotations

import json
import math
import os
from pathlib import Path

import pandas as pd


ARCHIVE_ROOT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
PDF_PATH = ARCHIVE_ROOT / "official_assets_extracted" / "2016" / "Modeling Refugee Immigration Policies.pdf"
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"
os.environ.setdefault("MPLCONFIGDIR", "/private/tmp/math_modeling_world_mplconfig")

import matplotlib.pyplot as plt


ASYLUM_APPLICATIONS_BY_OCT_2015 = 715_000
HUNGARY_APPLICATIONS_PER_100K = 1_450
HUNGARY_APPROVAL_RATE_2014 = 0.32
CRISIS_SCALE_FACTOR = 10

OFFICIAL_ROUTES = [
    {
        "route": "West Mediterranean",
        "entry_point": "Spain",
        "popularity_weight": 0.08,
        "safety_score": 0.58,
        "accessibility_score": 0.50,
        "daily_processing_capacity": 2_100,
        "temporary_capacity": 55_000,
    },
    {
        "route": "Central Mediterranean",
        "entry_point": "Italy",
        "popularity_weight": 0.13,
        "safety_score": 0.28,
        "accessibility_score": 0.48,
        "daily_processing_capacity": 2_900,
        "temporary_capacity": 86_000,
    },
    {
        "route": "Eastern Mediterranean",
        "entry_point": "Greece/Turkey",
        "popularity_weight": 0.42,
        "safety_score": 0.62,
        "accessibility_score": 0.82,
        "daily_processing_capacity": 8_200,
        "temporary_capacity": 284_000,
    },
    {
        "route": "West Balkans",
        "entry_point": "Hungary/Serbia",
        "popularity_weight": 0.24,
        "safety_score": 0.50,
        "accessibility_score": 0.68,
        "daily_processing_capacity": 4_600,
        "temporary_capacity": 162_000,
    },
    {
        "route": "Eastern Borders",
        "entry_point": "Eastern EU border",
        "popularity_weight": 0.07,
        "safety_score": 0.54,
        "accessibility_score": 0.36,
        "daily_processing_capacity": 1_350,
        "temporary_capacity": 48_000,
    },
    {
        "route": "Albania to Greece",
        "entry_point": "Albania/Greece",
        "popularity_weight": 0.06,
        "safety_score": 0.60,
        "accessibility_score": 0.42,
        "daily_processing_capacity": 1_150,
        "temporary_capacity": 35_000,
    },
]

DESTINATIONS = [
    {"destination": "Germany", "integration_capacity": 240_000, "legal_access": 0.80, "local_safety": 0.82, "resource_readiness": 0.74},
    {"destination": "France", "integration_capacity": 160_000, "legal_access": 0.72, "local_safety": 0.78, "resource_readiness": 0.70},
    {"destination": "United Kingdom", "integration_capacity": 70_000, "legal_access": 0.58, "local_safety": 0.80, "resource_readiness": 0.76},
    {"destination": "Turkey", "integration_capacity": 135_000, "legal_access": 0.66, "local_safety": 0.62, "resource_readiness": 0.60},
    {"destination": "Hungary", "integration_capacity": 50_000, "legal_access": 0.32, "local_safety": 0.56, "resource_readiness": 0.48},
    {"destination": "Greece", "integration_capacity": 60_000, "legal_access": 0.50, "local_safety": 0.58, "resource_readiness": 0.46},
]

RESOURCE_STANDARDS = {
    "shelter": {"units_per_1000_refugees": 1.0, "government_ready_units": 560, "ngo_added_units": 170, "priority_weight": 0.33},
    "healthcare": {"units_per_1000_refugees": 0.38, "government_ready_units": 215, "ngo_added_units": 95, "priority_weight": 0.27},
    "water": {"units_per_1000_refugees": 1.45, "government_ready_units": 930, "ngo_added_units": 210, "priority_weight": 0.22},
    "food": {"units_per_1000_refugees": 1.28, "government_ready_units": 850, "ngo_added_units": 190, "priority_weight": 0.18},
}

ASSUMPTIONS = {
    "route_scores": "Route safety, accessibility, and temporary capacity are normalized deterministic assumptions anchored to the six routes named in the official problem statement.",
    "resource_units": "One shelter unit denotes capacity for 1,000 refugees; water, food, and healthcare units are comparable planning bundles per 1,000 refugees.",
    "ngo_effect": "NGOs add mobile health, water, food distribution, and temporary shelter capacity, while governments retain legal admission and security functions.",
    "allocation_rule": "Refugees are assigned to routes by attractiveness subject to route capacity, then resource gaps are prioritized by weighted unmet need.",
    "scale_rule": "The 10x crisis keeps the same first-order network but activates new time-dependent parameters for disease control, childbirth, education, and social cohesion.",
}


def clean_float(value: float, digits: int = 6) -> float:
    return round(float(value), digits)


def crisis_metrics() -> dict[str, object]:
    enabling = [
        "safe route segments",
        "available transport",
        "multiple entry points",
        "destination resource capacity",
        "legal processing capacity",
        "NGO mobile support",
    ]
    inhibiting = [
        "dangerous sea crossings",
        "bottlenecked borders",
        "low approval rates",
        "shelter and healthcare scarcity",
        "local backlash after security shocks",
        "rapidly changing political constraints",
    ]
    homeless_proxy = HUNGARY_APPLICATIONS_PER_100K * (1.0 - HUNGARY_APPROVAL_RATE_2014)
    return {
        "official_scale": ASYLUM_APPLICATIONS_BY_OCT_2015,
        "hungary_applications_per_100k": HUNGARY_APPLICATIONS_PER_100K,
        "hungary_approval_rate_2014": HUNGARY_APPROVAL_RATE_2014,
        "hungary_homeless_per_100k_proxy": clean_float(homeless_proxy, 3),
        "enabling_factors": enabling,
        "inhibiting_factors": inhibiting,
        "measure_definitions": {
            "route_attractiveness": "0.38 accessibility + 0.34 safety + 0.18 capacity share + 0.10 legal entry support",
            "resource_gap": "required resource units minus ready government and NGO units",
            "system_resilience": "ability to preserve safe flow when one route loses safety or capacity",
        },
    }


def route_dataframe() -> pd.DataFrame:
    rows = []
    total_temp_capacity = sum(route["temporary_capacity"] for route in OFFICIAL_ROUTES)
    for route in OFFICIAL_ROUTES:
        capacity_share = route["temporary_capacity"] / total_temp_capacity
        legal_entry_support = 0.65 if route["route"] in {"Eastern Mediterranean", "West Balkans"} else 0.55
        attractiveness = (
            0.38 * route["accessibility_score"]
            + 0.34 * route["safety_score"]
            + 0.18 * capacity_share
            + 0.10 * legal_entry_support
        )
        rows.append({**route, "capacity_share": capacity_share, "legal_entry_support": legal_entry_support, "route_attractiveness": attractiveness})
    return pd.DataFrame(rows)


def allocate_integer_flows(weights: list[float], total: int, caps: list[int]) -> tuple[list[int], list[int]]:
    raw = [total * weight / sum(weights) for weight in weights]
    allocation = [min(int(math.floor(value)), cap) for value, cap in zip(raw, caps)]
    emergency_overflow = [0 for _ in allocation]
    remaining = total - sum(allocation)
    while remaining > 0:
        candidates = [
            (raw[index] - allocation[index], index)
            for index in range(len(allocation))
            if allocation[index] < caps[index]
        ]
        if not candidates:
            best_index = max(range(len(weights)), key=lambda index: weights[index])
            allocation[best_index] += remaining
            emergency_overflow[best_index] += remaining
            break
        _, best_index = max(candidates)
        allocation[best_index] += 1
        remaining -= 1
    return allocation, emergency_overflow


def flow_model(routes: pd.DataFrame) -> dict[str, object]:
    weights = (routes["popularity_weight"] * (0.45 + routes["route_attractiveness"])).tolist()
    caps = routes["temporary_capacity"].astype(int).tolist()
    allocations, emergency_overflow = allocate_integer_flows(weights, ASYLUM_APPLICATIONS_BY_OCT_2015, caps)
    rows = []
    for row, refugees, overflow in zip(routes.to_dict("records"), allocations, emergency_overflow):
        processing_days = refugees / max(float(row["daily_processing_capacity"]), 1.0)
        risk_adjusted_flow = refugees * float(row["safety_score"])
        rows.append(
            {
                "route": row["route"],
                "entry_point": row["entry_point"],
                "allocated_refugees": int(refugees),
                "share_of_total": clean_float(refugees / ASYLUM_APPLICATIONS_BY_OCT_2015, 5),
                "safety_score": clean_float(row["safety_score"]),
                "accessibility_score": clean_float(row["accessibility_score"]),
                "route_attractiveness": clean_float(row["route_attractiveness"]),
                "daily_processing_capacity": int(row["daily_processing_capacity"]),
                "estimated_processing_days": clean_float(processing_days, 2),
                "risk_adjusted_safe_flow": clean_float(risk_adjusted_flow, 2),
                "capacity_binding": bool(refugees >= int(row["temporary_capacity"])),
                "emergency_overflow_refugees": int(overflow),
            }
        )
    return {
        "method": "capacity-constrained deterministic route allocation over the six official travel routes, with explicit emergency overflow when stated crisis scale exceeds temporary route capacity",
        "route_allocations": rows,
        "total_allocated_refugees": int(sum(allocations)),
        "temporary_capacity_total": int(sum(caps)),
        "emergency_overflow_total": int(sum(emergency_overflow)),
        "safest_high_volume_route": max(rows, key=lambda item: item["allocated_refugees"] * item["safety_score"])["route"],
        "most_dangerous_route_named_in_statement": "Central Mediterranean",
        "most_popular_route_named_in_statement": "Eastern Mediterranean",
    }


def resource_plan(total_refugees: int, include_ngo: bool) -> tuple[list[dict[str, object]], float]:
    rows = []
    weighted_unmet = 0.0
    for resource, values in RESOURCE_STANDARDS.items():
        required = total_refugees / 1000.0 * float(values["units_per_1000_refugees"])
        ready = float(values["government_ready_units"]) + (float(values["ngo_added_units"]) if include_ngo else 0.0)
        gap = max(0.0, required - ready)
        weighted = gap * float(values["priority_weight"])
        weighted_unmet += weighted
        rows.append(
            {
                "resource": resource,
                "required_units": clean_float(required, 3),
                "available_units": clean_float(ready, 3),
                "unmet_units": clean_float(gap, 3),
                "priority_weight": values["priority_weight"],
                "weighted_gap": clean_float(weighted, 3),
                "prepositioning_action": {
                    "shelter": "preposition modular shelter near route bottlenecks and high-capacity destinations",
                    "healthcare": "deploy mobile clinics and vaccination/triage teams at entry points",
                    "water": "stage purification, trucking, and sanitation units near camps",
                    "food": "stage dry rations and local procurement contracts",
                }[resource],
            }
        )
    return sorted(rows, key=lambda row: row["weighted_gap"], reverse=True), weighted_unmet


def dynamic_capacity(flow: dict[str, object]) -> dict[str, object]:
    resource_rows, weighted_unmet = resource_plan(int(flow["total_allocated_refugees"]), include_ngo=True)
    return {
        "method": "priority ranking by weighted unmet resource units after government plus NGO prepositioning",
        "resources": resource_rows,
        "highest_priority_resource": resource_rows[0]["resource"],
        "weighted_unmet_need": clean_float(weighted_unmet, 3),
        "dynamic_factors": [
            "destination capacity fills fastest in the most desired countries",
            "route safety changes after border closures or sea conditions",
            "transport availability changes daily",
            "local population health and safety constraints tighten when shelters remain crowded",
        ],
    }


def ngo_strategy(total_refugees: int) -> dict[str, object]:
    govt_rows, govt_unmet = resource_plan(total_refugees, include_ngo=False)
    ngo_rows, ngo_unmet = resource_plan(total_refugees, include_ngo=True)
    return {
        "government_only": {
            "unmet_need": clean_float(govt_unmet, 3),
            "resources": govt_rows,
        },
        "with_ngo": {
            "unmet_need": clean_float(ngo_unmet, 3),
            "resources": ngo_rows,
        },
        "strategy_change": "With NGOs, the model shifts from border-only processing to distributed mobile support: health, water, food, and shelter can move toward bottlenecks before destinations reach maximum capacity.",
    }


def regional_extension() -> dict[str, object]:
    rows = []
    for destination in [
        {"destination": "Canada", "distance_penalty": 0.42, "integration_capacity": 65_000, "legal_access": 0.74, "resource_readiness": 0.82},
        {"destination": "China", "distance_penalty": 0.55, "integration_capacity": 80_000, "legal_access": 0.42, "resource_readiness": 0.70},
        {"destination": "United States", "distance_penalty": 0.50, "integration_capacity": 95_000, "legal_access": 0.62, "resource_readiness": 0.78},
    ]:
        feasibility = (
            0.36 * destination["integration_capacity"] / 100_000
            + 0.28 * destination["legal_access"]
            + 0.24 * destination["resource_readiness"]
            - 0.18 * destination["distance_penalty"]
        )
        rows.append({**destination, "model_feasibility_score": clean_float(feasibility)})
    return {
        "destinations": sorted(rows, key=lambda row: row["model_feasibility_score"], reverse=True),
        "does_model_transfer": True,
        "transfer_note": "The network-flow/resource-capacity structure transfers, but distance, legal access, air/sea transport, and long-run integration parameters must be recalibrated.",
    }


def policy_package(flow: dict[str, object], capacity: dict[str, object]) -> dict[str, object]:
    return {
        "recommended_policies": [
            "Open multiple entry points on high-volume routes to prevent single-border bottlenecks.",
            "Shift refugees away from the Central Mediterranean when safer capacity exists.",
            "Preposition shelter and healthcare before destinations hit maximum capacity.",
            "Use a quota plus capacity trigger so France and Germany do not carry all resettlement burden.",
            "Give NGOs formal logistics lanes for mobile clinics, water, food, and temporary shelter.",
            "Protect local population health with registration, vaccination, sanitation, and transparent risk communication.",
        ],
        "priority_resource": capacity["highest_priority_resource"],
        "policy_objective": "minimize unsafe movement and unmet basic needs while respecting legal and cultural constraints of affected countries",
        "operational_metric": "weekly safe placements plus weighted unmet resource reduction",
    }


def exogenous_event(flow: dict[str, object]) -> dict[str, object]:
    baseline = pd.DataFrame(flow["route_allocations"])
    stress_rows = []
    for row in baseline.to_dict("records"):
        safety = float(row["safety_score"])
        capacity = float(row["daily_processing_capacity"])
        if row["route"] in {"West Balkans", "Eastern Mediterranean"}:
            safety *= 0.76
            capacity *= 0.68
        elif row["route"] == "Central Mediterranean":
            safety *= 0.90
            capacity *= 0.82
        else:
            safety *= 0.86
            capacity *= 0.78
        stress_rows.append(
            {
                "route": row["route"],
                "baseline_safety": row["safety_score"],
                "post_event_safety": clean_float(safety),
                "baseline_daily_capacity": row["daily_processing_capacity"],
                "post_event_daily_capacity": int(round(capacity)),
                "cascading_effect": "queue spillover to neighboring routes and higher shelter/healthcare pressure",
            }
        )
    return {
        "event": "major terrorist attack linked in public debate to the refugee crisis",
        "parameter_shifts": [
            "approval rate decreases",
            "border processing capacity decreases",
            "route safety decreases near closed borders",
            "local acceptance and housing readiness decrease",
            "security screening time increases",
        ],
        "route_stress": stress_rows,
        "resilience_design": [
            "pre-authorize contingency entry points",
            "separate humanitarian screening from long-run asylum adjudication",
            "keep NGO logistics corridors open during lockdowns",
            "maintain transparent communication with local populations",
        ],
    }


def scalability_10x(flow: dict[str, object]) -> dict[str, object]:
    baseline_daily_capacity = sum(row["daily_processing_capacity"] for row in flow["route_allocations"])
    baseline_days = ASYLUM_APPLICATIONS_BY_OCT_2015 / baseline_daily_capacity
    scaled_total = ASYLUM_APPLICATIONS_BY_OCT_2015 * CRISIS_SCALE_FACTOR
    scaled_days = scaled_total / baseline_daily_capacity
    threshold_days = 180
    return {
        "scale_factor": CRISIS_SCALE_FACTOR,
        "scaled_refugees": scaled_total,
        "baseline_resolution_days": clean_float(baseline_days, 2),
        "scaled_resolution_days_without_capacity_expansion": clean_float(scaled_days, 2),
        "time_threshold_days_for_new_considerations": threshold_days,
        "new_parameters_needed": [
            "disease surveillance and vaccination coverage",
            "birth and maternal care rate",
            "school-age child education capacity",
            "long-term employment and housing absorption",
            "local social cohesion and misinformation risk",
        ],
        "non_scalable_features": [
            "manual case processing",
            "single-route bottleneck relief",
            "short-term shelter-only planning",
            "government-only resource deployment",
        ],
        "becomes_irrelevant_or_changes": [
            "temporary camp capacity becomes less useful than long-term housing absorption",
            "route popularity becomes less important than international burden sharing",
            "daily transport becomes coupled to disease control and education continuity",
        ],
    }


def policy_letter(policy: dict[str, object], flow: dict[str, object], capacity: dict[str, object]) -> str:
    safest_route = flow["safest_high_volume_route"]
    return (
        "To the UN Secretary General and the Chief of Migration:\n\n"
        f"ICM-RUN recommends a capacity-triggered refugee movement policy for the {ASYLUM_APPLICATIONS_BY_OCT_2015:,} applications reported by the end of October 2015. "
        f"The model keeps the official six routes visible, shifts volume toward safer capacity such as {safest_route}, and flags {capacity['highest_priority_resource']} as the current priority resource. "
        "The UN should authorize multiple entry points, preposition shelter and healthcare, give NGOs formal logistics roles, and use quota triggers before Germany and France absorb a disproportionate burden. "
        "The policy should remain resilient to external security shocks by maintaining contingency entry points, humanitarian screening lanes, and transparent public health communication."
    )


def write_artifacts(
    routes: pd.DataFrame,
    flow: dict[str, object],
    capacity: dict[str, object],
    ngo: dict[str, object],
    exogenous: dict[str, object],
    scale: dict[str, object],
) -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(flow["route_allocations"]).to_csv(ARTIFACT_DIR / "route_flow_plan.csv", index=False, encoding="utf-8-sig")
    pd.DataFrame(capacity["resources"]).to_csv(ARTIFACT_DIR / "resource_prepositioning.csv", index=False, encoding="utf-8-sig")
    pd.DataFrame(
        [
            {"strategy": "government_only", "unmet_need": ngo["government_only"]["unmet_need"]},
            {"strategy": "with_ngo", "unmet_need": ngo["with_ngo"]["unmet_need"]},
        ]
    ).to_csv(ARTIFACT_DIR / "ngo_strategy_comparison.csv", index=False, encoding="utf-8-sig")
    pd.DataFrame(exogenous["route_stress"]).to_csv(ARTIFACT_DIR / "exogenous_event_stress.csv", index=False, encoding="utf-8-sig")
    pd.DataFrame([scale]).to_csv(ARTIFACT_DIR / "scalability_10x.csv", index=False, encoding="utf-8-sig")
    routes.to_csv(ARTIFACT_DIR / "route_parameters.csv", index=False, encoding="utf-8-sig")

    route_frame = pd.DataFrame(flow["route_allocations"])
    fig, ax1 = plt.subplots(figsize=(9.5, 5.4))
    ax1.bar(route_frame["route"], route_frame["allocated_refugees"], color="#356f8c", alpha=0.82)
    ax1.set_ylabel("Allocated refugees")
    ax1.set_xlabel("Official route")
    ax1.tick_params(axis="x", labelrotation=25)
    ax2 = ax1.twinx()
    ax2.plot(route_frame["route"], route_frame["safety_score"], color="#b24c3d", marker="o", linewidth=2)
    ax2.set_ylabel("Safety score")
    ax1.set_title("2016 ICM-F Capacity-Constrained Refugee Flow Plan")
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "refugee_flow_network.png", dpi=180)
    plt.close(fig)


def write_report(result: dict[str, object]) -> None:
    lines = [
        "# 2016 ICM-F Modeling Refugee Immigration Policies 题面参数实验报告",
        "",
        "## 数据来源",
        f"- 官方 PDF：`{PDF_PATH}`。",
        f"- 官方题面参数：2015 年 10 月底欧洲收到超过 {ASYLUM_APPLICATIONS_BY_OCT_2015:,} 份庇护申请；Hungary 约 {HUNGARY_APPLICATIONS_PER_100K:,}/100k；2014 年批准率 {HUNGARY_APPROVAL_RATE_2014:.0%}；六条路线；Eastern Mediterranean 最热门，Central Mediterranean 最危险。",
        "- 本题没有独立 CSV/XLSX 附件；路线容量、资源包和 NGO 增益是显式可替换规划假设。",
        "",
        "## Q1 危机指标",
        f"- Hungary 未安置压力代理：{result['crisis_metrics']['hungary_homeless_per_100k_proxy']} / 100k。",
        "",
        "## Q2 最优难民流动",
        f"- 总分配人数：{result['flow_model']['total_allocated_refugees']:,}。",
        f"- 安全高容量路线：{result['flow_model']['safest_high_volume_route']}。",
        "",
        "## Q3 动态容量和资源前置",
        f"- 最高优先资源：{result['dynamic_capacity']['highest_priority_resource']}。",
        f"- 加入 NGO 后未满足需求：{result['ngo_strategy']['with_ngo']['unmet_need']}。",
        "",
        "## Q4 政策包",
        f"- 目标：{result['policy_package']['policy_objective']}。",
        "",
        "## Q5 外生事件",
        f"- 事件：{result['exogenous_event']['event']}。",
        "",
        "## Q6 十倍扩展",
        f"- 10x 难民规模：{result['scalability_10x']['scaled_refugees']:,}。",
        f"- 若不扩容，处理天数：{result['scalability_10x']['scaled_resolution_days_without_capacity_expansion']}。",
        "",
        "## 给 UN 的一页政策信摘要",
        result["policy_letter"],
        "",
        "## 输出文件",
        f"- `result.json`：{RESULT_PATH}",
        f"- `route_flow_plan.csv`：{ARTIFACT_DIR / 'route_flow_plan.csv'}",
        f"- `resource_prepositioning.csv`：{ARTIFACT_DIR / 'resource_prepositioning.csv'}",
        f"- `ngo_strategy_comparison.csv`：{ARTIFACT_DIR / 'ngo_strategy_comparison.csv'}",
        f"- `exogenous_event_stress.csv`：{ARTIFACT_DIR / 'exogenous_event_stress.csv'}",
        f"- `scalability_10x.csv`：{ARTIFACT_DIR / 'scalability_10x.csv'}",
        f"- `refugee_flow_network.png`：{ARTIFACT_DIR / 'refugee_flow_network.png'}",
    ]
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    if not PDF_PATH.exists():
        raise FileNotFoundError(f"Missing official PDF: {PDF_PATH}")
    metrics = crisis_metrics()
    routes = route_dataframe()
    flow = flow_model(routes)
    capacity = dynamic_capacity(flow)
    ngo = ngo_strategy(int(flow["total_allocated_refugees"]))
    regional = regional_extension()
    policy = policy_package(flow, capacity)
    exogenous = exogenous_event(flow)
    scale = scalability_10x(flow)
    letter = policy_letter(policy, flow, capacity)
    result = {
        "problem_id": "2016-F",
        "data_source": {
            "type": "official_statement_parameters",
            "root": str(PDF_PATH.parent),
            "source_pdf": str(PDF_PATH),
            "official_problem_parameters": {
                "asylum_applications_by_oct_2015": ASYLUM_APPLICATIONS_BY_OCT_2015,
                "hungary_applications_per_100k": HUNGARY_APPLICATIONS_PER_100K,
                "hungary_approval_rate_2014": HUNGARY_APPROVAL_RATE_2014,
                "routes": [route["route"] for route in OFFICIAL_ROUTES],
                "most_popular_route": "Eastern Mediterranean",
                "most_dangerous_route": "Central Mediterranean",
                "scale_factor_required_in_task": CRISIS_SCALE_FACTOR,
            },
            "assumptions": ASSUMPTIONS,
        },
        "crisis_metrics": metrics,
        "flow_model": flow,
        "dynamic_capacity": capacity,
        "ngo_strategy": ngo,
        "regional_extension": regional,
        "policy_package": policy,
        "exogenous_event": exogenous,
        "scalability_10x": scale,
        "policy_letter": letter,
        "assumption_audit": {
            "truthfulness_note": "This workflow uses official statement parameters and explicit deterministic assumptions; it does not claim route capacity or resource bundle assumptions are observed data.",
            "replaceable_assumptions": ASSUMPTIONS,
        },
    }
    write_artifacts(routes, flow, capacity, ngo, exogenous, scale)
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_report(result)
    print(json.dumps({"result": str(RESULT_PATH), "report": str(REPORT_PATH), "artifacts": str(ARTIFACT_DIR)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
