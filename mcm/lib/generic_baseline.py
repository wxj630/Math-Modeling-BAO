from __future__ import annotations

import csv
import json
import math
import re
from hashlib import sha256
from pathlib import Path
from typing import Any


MODEL_RULES = [
    {
        "method": "linear_weighted_score_baseline",
        "name": "线性加权评分基线",
        "chapter": "CH7",
        "keywords": ["score", "rank", "ranking", "metric", "index", "evaluate", "assessment", "评价", "排名", "指标", "权重"],
    },
    {
        "method": "linear_trend_forecast_baseline",
        "name": "线性趋势预测基线",
        "chapter": "CH8",
        "keywords": ["forecast", "predict", "future", "timeline", "trend", "projection", "2050", "预测", "未来", "趋势"],
    },
    {
        "method": "resource_allocation_baseline",
        "name": "资源配置基线",
        "chapter": "CH3",
        "keywords": ["optimize", "optimal", "cost", "budget", "allocation", "placement", "plan", "policy", "最优", "优化", "成本", "预算", "配置"],
    },
    {
        "method": "network_path_baseline",
        "name": "网络路径基线",
        "chapter": "CH4",
        "keywords": ["network", "route", "path", "node", "flow", "transport", "charging", "drone", "网络", "路径", "路线", "节点"],
    },
    {
        "method": "threshold_classification_baseline",
        "name": "阈值分类基线",
        "chapter": "CH9",
        "keywords": ["classify", "classification", "risk", "fragile", "stable", "vulnerable", "detect", "分类", "风险", "稳定"],
    },
    {
        "method": "first_order_dynamic_baseline",
        "name": "一阶动态仿真基线",
        "chapter": "CH2",
        "keywords": ["dynamic", "growth", "spread", "evolution", "sensitivity", "simulation", "增长", "演化", "敏感性", "动态"],
    },
    {
        "method": "report_outline_baseline",
        "name": "报告提纲基线",
        "chapter": "CH0",
        "keywords": ["memo", "report", "letter", "summary", "recommendation", "write", "报告", "备忘录", "建议"],
    },
]


def normalize_text(text: object) -> str:
    return re.sub(r"\s+", " ", str(text or "")).strip()


def stable_fraction(*parts: object) -> float:
    payload = "\n".join(normalize_text(part) for part in parts).encode("utf-8", errors="ignore")
    return int(sha256(payload).hexdigest()[:10], 16) / float(16**10 - 1)


def numeric_tokens(text: str) -> list[float]:
    values = []
    for token in re.findall(r"[-+]?\d+(?:\.\d+)?", text):
        try:
            values.append(float(token))
        except ValueError:
            continue
    return values


def select_generic_model(payload: dict[str, Any]) -> dict[str, Any]:
    haystack = " ".join(
        [
            normalize_text(payload.get("title")),
            normalize_text(payload.get("question_title") or payload.get("title")),
            normalize_text(payload.get("statement")),
            normalize_text(payload.get("methods")),
        ]
    ).lower()
    scored = []
    for rule in MODEL_RULES:
        hits = [keyword for keyword in rule["keywords"] if keyword.lower() in haystack]
        if hits:
            scored.append((len(hits), hits, rule))
    if not scored:
        rule = {
            "method": "evidence_table_baseline",
            "name": "证据表基线",
            "chapter": "CH6",
            "keywords": ["generic"],
        }
        return {**rule, "matched_keywords": ["generic"], "rationale": "No strong task keyword was found; use a conservative evidence table baseline."}
    scored.sort(key=lambda item: (-item[0], item[2]["method"]))
    _, hits, rule = scored[0]
    return {
        "method": rule["method"],
        "name": rule["name"],
        "chapter": rule["chapter"],
        "matched_keywords": hits[:8],
        "rationale": "Selected by keyword overlap with the MCM question title, statement, and existing method hint.",
    }


def source_strength(source_type: str) -> float:
    if "official_comap" in source_type:
        return 1.0
    if "world_bank" in source_type:
        return 0.92
    if "official_statement_parameters" in source_type:
        return 0.72
    if source_type:
        return 0.55
    return 0.35


def artifact_strength(path: str) -> float:
    suffix = Path(path).suffix.lower()
    if suffix in {".csv", ".xlsx", ".xls", ".json"}:
        return 1.0
    if suffix in {".png", ".jpg", ".jpeg"}:
        return 0.68
    if suffix in {".md", ".txt"}:
        return 0.52
    return 0.45


def build_experiment_rows(payload: dict[str, Any], model: dict[str, Any]) -> list[dict[str, Any]]:
    statement = normalize_text(payload.get("statement"))
    methods = normalize_text(payload.get("methods"))
    values = numeric_tokens(statement + " " + methods)
    source_type = normalize_text(payload.get("source_type"))
    artifact_path = normalize_text(payload.get("artifact_path"))
    statement_signal = min(1.0, len(statement) / 420.0)
    numeric_signal = min(1.0, len(values) / 8.0)
    method_signal = min(1.0, len(model.get("matched_keywords", [])) / 5.0)
    source_signal = source_strength(source_type)
    artifact_signal = artifact_strength(artifact_path)
    return [
        {
            "component": "statement_specificity",
            "raw_value": len(statement),
            "normalized_score": round(statement_signal, 6),
            "audit_note": "Longer problem statements usually expose more constraints for a first-pass model.",
        },
        {
            "component": "numeric_anchor_count",
            "raw_value": len(values),
            "normalized_score": round(numeric_signal, 6),
            "audit_note": "Counts numeric anchors visible in the question statement and method hint.",
        },
        {
            "component": "model_keyword_match",
            "raw_value": len(model.get("matched_keywords", [])),
            "normalized_score": round(method_signal, 6),
            "audit_note": "Measures how clearly the question maps to a classical modeling family.",
        },
        {
            "component": "source_strength",
            "raw_value": source_type or "unknown",
            "normalized_score": round(source_signal, 6),
            "audit_note": "Rewards official attachments and explicit official statement parameters.",
        },
        {
            "component": "artifact_readiness",
            "raw_value": artifact_path or "none",
            "normalized_score": round(artifact_signal, 6),
            "audit_note": "Rewards table-like artifacts that a baseline can inspect directly.",
        },
    ]


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames: list[str] = []
    for row in rows:
        for key in row:
            if key not in fieldnames:
                fieldnames.append(key)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def solve_question_generic_baseline(payload: dict[str, Any], artifact_dir: Path) -> dict[str, Any]:
    artifact_dir.mkdir(parents=True, exist_ok=True)
    model = select_generic_model(payload)
    rows = build_experiment_rows(payload, model)
    weights = {
        "statement_specificity": 0.18,
        "numeric_anchor_count": 0.16,
        "model_keyword_match": 0.22,
        "source_strength": 0.28,
        "artifact_readiness": 0.16,
    }
    score = sum(weights[row["component"]] * float(row["normalized_score"]) for row in rows)
    values = numeric_tokens(normalize_text(payload.get("statement")) + " " + normalize_text(payload.get("methods")))
    write_csv(artifact_dir / "experiment_table.csv", rows)
    outline = [
        "Read the official question and any indexed real-data workflow before adding domain assumptions.",
        "Use this baseline only as the first scaffold for variables, constraints, and sanity checks.",
        "Replace the generic score with a problem-specific model and cite official assets in the final solution.",
    ]
    return {
        "baseline_kind": "mcm_generic_first_pass",
        "problem_id": payload["problem_id"],
        "year": payload["year"],
        "code": payload["code"],
        "question": payload["question"],
        "question_title": payload.get("question_title") or payload.get("title"),
        "statement": payload.get("statement", ""),
        "selected_model": model,
        "formulation": {
            "decision_variables": [
                "x_i: normalized evidence component score for baseline component i",
                "w_i: fixed transparent weight assigned to component i",
                "S: first-pass baseline readiness score",
            ],
            "constraints": [
                "0 <= x_i <= 1 for every component",
                "sum_i w_i = 1",
                "The baseline must not replace the real-data workflow or invent hidden observations.",
            ],
            "objective_or_equations": [
                "S = sum_i w_i x_i",
                "method = argmax keyword_overlap(question, model_family)",
            ],
        },
        "data_source": {
            "source_type": "mcm_question_index",
            "indexed_source_type": payload.get("source_type"),
            "indexed_solution_path": payload.get("solution_path"),
            "indexed_result_path": payload.get("result_path"),
            "indexed_artifact_path": payload.get("artifact_path"),
            "note": "This generic baseline is derived from the MCM question index and points back to the audited real-data workflow.",
        },
        "experiment_result": {
            "method": model["method"],
            "baseline_score": round(score, 6),
            "component_rows": rows,
            "extracted_numeric_tokens": values[:12],
            "numeric_token_count": len(values),
            "outline": outline,
            "method_confidence": round(min(1.0, 0.35 + 0.13 * len(model.get("matched_keywords", [])) + 0.22 * source_strength(normalize_text(payload.get("source_type")))), 6),
        },
        "artifact_paths": [str(artifact_dir / "experiment_table.csv")],
        "limitations": [
            "This is the intentionally minimal baseline layer, not the contest-grade real solution.",
            "It does not introduce new empirical observations beyond the indexed official workflow metadata.",
            "It is useful for a quick modeling starting point and for regression-checking archive coverage.",
        ],
    }


def write_generic_report(result: dict[str, Any], report_path: Path, solution_path: Path) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)
    baseline_root = report_path.parents[4]
    result_path = baseline_root / "results" / result["year"] / result["code"] / result["question"] / "result.json"
    f = result["formulation"]
    lines = [
        f"# {result['problem_id']} {result['question']} MCM 通用基线报告",
        "",
        "> 这是题目专用化之前的最低可运行通用基线，用于保留第一版建模脚手架；它不代表最终竞赛级解法。",
        "",
        "## 题目与任务",
        "",
        f"- 题目：{result['problem_id']}",
        f"- 小问：{result['question']} {result['question_title']}",
        f"- 原问：{result['statement']}",
        "",
        "## 通用模型选择",
        "",
        f"- 模型：{result['selected_model']['name']}",
        f"- 方法键：`{result['experiment_result']['method']}`",
        f"- 章节提示：{result['selected_model']['chapter']}",
        f"- 命中关键词：{', '.join(result['selected_model'].get('matched_keywords', []))}",
        "",
        "## 变量、约束与公式",
        "",
        "### 变量定义",
    ]
    lines.extend(f"- {item}" for item in f["decision_variables"])
    lines += ["", "### 约束条件"]
    lines.extend(f"- {item}" for item in f["constraints"])
    lines += ["", "### 模型公式 / 目标函数"]
    lines.extend(f"- `{item}`" for item in f["objective_or_equations"])
    lines += [
        "",
        "## 运行与产物",
        "",
        f"- 通用代码：{solution_path}",
        f"- 结果 JSON：{result_path}",
        f"- 实验报告：{report_path}",
    ]
    for artifact in result.get("artifact_paths", []):
        lines.append(f"- 实验产物：{artifact}")
    lines += [
        "",
        "## 数据来源",
        "",
        f"- 类型：{result['data_source']['source_type']}",
        f"- 真实工作流：{result['data_source'].get('indexed_solution_path')}",
        f"- 真实产物：{result['data_source'].get('indexed_artifact_path')}",
        "",
        "## 核心结果",
        "",
        "```json",
        json.dumps(result["experiment_result"], ensure_ascii=False, indent=2),
        "```",
        "",
        "## 限制",
        "",
    ]
    lines.extend(f"- {item}" for item in result.get("limitations", []))
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
