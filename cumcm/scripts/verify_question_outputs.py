# -*- coding: utf-8 -*-
"""Verify per-question CUMCM code, result artifacts, and reports."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_REPORT_SECTIONS = [
    "## 题目原文与任务拆解",
    "## 适配模型",
    "## 变量、约束与公式",
    "## Python 代码与运行方式",
    "## 实验结果与解释",
    "## 实验报告",
]


def main() -> None:
    scripts = sorted((ROOT / "question_solutions").glob("*/*/q*/solution.py"))
    results = sorted((ROOT / "question_results").glob("*/*/q*/result.json"))
    reports = sorted((ROOT / "question_reports").glob("*/*/q*/report.md"))
    errors: list[str] = []
    if not scripts:
        errors.append("missing question solution scripts")
    if len(results) != len(scripts):
        errors.append(f"result count mismatch: scripts={len(scripts)} results={len(results)}")
    if len(reports) != len(scripts):
        errors.append(f"report count mismatch: scripts={len(scripts)} reports={len(reports)}")

    for result_path in results:
        data = json.loads(result_path.read_text(encoding="utf-8"))
        rel = result_path.relative_to(ROOT / "question_results")
        report_path = ROOT / "question_reports" / rel.parent / "report.md"
        solution_path = ROOT / "question_solutions" / rel.parent / "solution.py"
        if not solution_path.exists():
            errors.append(f"missing solution for {rel}")
        if not report_path.exists():
            errors.append(f"missing report for {rel}")
            continue
        report = report_path.read_text(encoding="utf-8")
        for section in REQUIRED_REPORT_SECTIONS:
            if section not in report:
                errors.append(f"{report_path.relative_to(ROOT)} missing section {section}")
        for key in ["selected_model", "formulation", "experiment_result", "artifact_paths", "data_source"]:
            if key not in data:
                errors.append(f"{result_path.relative_to(ROOT)} missing json key {key}")
        for artifact in data.get("artifact_paths", []):
            artifact_path = ROOT / artifact
            if not artifact_path.exists():
                errors.append(f"{result_path.relative_to(ROOT)} missing artifact {artifact}")
        if len(data.get("tasks", [])) == 0:
            errors.append(f"{result_path.relative_to(ROOT)} has no task breakdown")
        if len(data.get("formulation", {}).get("decision_variables", [])) < 3:
            errors.append(f"{result_path.relative_to(ROOT)} has too few variables")
        if len(data.get("formulation", {}).get("objective_or_equations", [])) < 2:
            errors.append(f"{result_path.relative_to(ROOT)} has too few equations")

    print(f"question scripts: {len(scripts)}")
    print(f"question results: {len(results)}")
    print(f"question reports: {len(reports)}")
    print(f"verification errors: {len(errors)}")
    for item in errors[:80]:
        print(f"ERROR: {item}")
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
