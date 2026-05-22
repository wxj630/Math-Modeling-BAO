# -*- coding: utf-8 -*-
"""Archive first-pass generic per-question baselines.

Specialized solvers are intentionally allowed to replace the current
question_results/question_reports outputs. This script keeps the earlier generic
modeling step reproducible under cumcm/generic_baselines so the learning and
improvement path is preserved instead of overwritten.
"""
from __future__ import annotations

import argparse
import csv
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "lib"))
from cumcm_models import parse_problem

GENERIC_ROOT = ROOT / "generic_baselines"

SCRIPT_TEMPLATE = '''# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question_generic_baseline

PAYLOAD = {payload}
RESULT_PATH = ROOT / "generic_baselines" / "results" / "{year}" / "{code}" / "q{qnum:02d}" / "result.json"
REPORT_PATH = ROOT / "generic_baselines" / "reports" / "{year}" / "{code}" / "q{qnum:02d}" / "report.md"
ARTIFACT_DIR = ROOT / "generic_baselines" / "artifacts" / "{year}" / "{code}" / "q{qnum:02d}"


def write_generic_report(result: dict, solution_path: Path) -> None:
    f = result["formulation"]
    lines = [
        f"# {{result['problem_id']}} {{result['question_label']}} 通用基线报告",
        "",
        "> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。",
        "",
        "## 题目与任务",
        "",
        f"- 题目：{{result['title']}}",
        f"- 问题：{{result['question_label']}}",
        f"- 原问：{{result['statement']}}",
        "",
        "## 通用模型选择",
        "",
        f"- 模型：{{result['selected_model']['name']}}（{{result['selected_model']['chapter']}}：{{result['selected_model']['chapter_title']}}）",
        f"- 教程参考：{{result['selected_model']['doc']}}",
        f"- 通用方法：`{{result['experiment_result'].get('method', 'generic_model')}}`",
        "",
        "## 变量、约束与公式",
        "",
        "### 变量定义",
    ]
    lines.extend(f"- {{item}}" for item in f.get("decision_variables", []))
    lines += ["", "### 约束条件"]
    lines.extend(f"- {{item}}" for item in f.get("constraints", []))
    lines += ["", "### 模型公式 / 目标函数"]
    lines.extend(f"- `{{item}}`" for item in f.get("objective_or_equations", []))
    lines += ["", "## 运行与产物", ""]
    lines.append(f"- 通用代码：{{solution_path}}")
    lines.append(f"- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python {{solution_path}}`")
    lines.append(f"- 结果 JSON：{{RESULT_PATH}}")
    lines.append(f"- 实验报告：{{REPORT_PATH}}")
    for artifact in result.get("artifact_paths", []):
        lines.append(f"- 实验产物：{{ROOT / artifact}}")
    lines += ["", "## 数据来源", ""]
    ds = result.get("data_source", {{}})
    lines.append(f"- 类型：{{ds.get('source_type', 'unknown')}}")
    if ds.get("path"):
        lines.append(f"- 路径：{{ds['path']}}")
    lines.append(f"- 说明：{{ds.get('note', '')}}")
    lines += ["", "## 核心结果", "", "```json", json.dumps(result["experiment_result"], ensure_ascii=False, indent=2), "```", ""]
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text("\\n".join(lines), encoding="utf-8")


def main() -> None:
    result = solve_question_generic_baseline(PAYLOAD, ARTIFACT_DIR)
    RESULT_PATH.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_generic_report(result, Path(__file__).resolve())
    print(f"wrote {{RESULT_PATH}}")
    print(f"wrote {{REPORT_PATH}}")
    print(f"wrote artifacts under {{ARTIFACT_DIR}}")


if __name__ == "__main__":
    main()
'''


def iter_payloads(problem_filter: set[str] | None = None) -> list[dict]:
    manifest_path = ROOT / "attachment_manifest.json"
    attachment_manifest = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else {}
    payloads: list[dict] = []
    for problem_path in sorted((ROOT / "problems").glob("*/*.md")):
        year = problem_path.parent.name
        code = problem_path.stem
        problem_id = f"{year}-{code}"
        if problem_filter and problem_id not in problem_filter:
            continue
        parsed = parse_problem(problem_path)
        attachments = attachment_manifest.get(problem_id, {}).get("attachments", [])
        for qnum, question in enumerate(parsed["questions"], start=1):
            payloads.append({
                "problem_id": problem_id,
                "year": year,
                "code": code,
                "question_index": qnum,
                "title": parsed["title"],
                "problem_path": str(problem_path),
                "question": question,
                "attachments": attachments,
            })
    return payloads


def write_readme(index_rows: list[dict]) -> None:
    method_counts: dict[str, int] = {}
    for row in index_rows:
        method_counts[row["method"]] = method_counts.get(row["method"], 0) + 1
    lines = [
        "# CUMCM 通用基线归档",
        "",
        "本目录保存题目专用化之前的第一版通用模型结果，避免在后续深化算法时把早期思路直接覆盖掉。",
        "",
        "## 目录",
        "",
        "- `solutions/`：每问一个可重新运行的通用基线 `solution.py`。",
        "- `results/`：通用基线 `result.json`。",
        "- `reports/`：通用基线 Markdown 报告。",
        "- `artifacts/`：通用基线实验表和其它产物。",
        "- `generic_baseline_index.csv/json`：通用基线索引。",
        "",
        "## 重新生成",
        "",
        "```bash",
        "/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python cumcm/scripts/archive_generic_baselines.py --all",
        "```",
        "",
        "## 方法分布",
        "",
    ]
    for method, count in sorted(method_counts.items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"- `{method}`：{count} 问")
    lines.append("")
    (GENERIC_ROOT / "README.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Archive CUMCM generic baseline solutions/results/reports.")
    parser.add_argument("--all", action="store_true", help="archive all parsed per-question baselines")
    parser.add_argument("--problems", nargs="*", help="problem ids to archive, e.g. 2024-C 2024-D")
    parser.add_argument("--no-run", action="store_true", help="only write generic solution scripts and index skeleton")
    args = parser.parse_args()

    if args.all:
        problem_filter = None
    else:
        problem_filter = set(args.problems or ["2022-D", "2023-D", "2024-A", "2024-B", "2024-C", "2024-D"])

    payloads = iter_payloads(problem_filter)
    index_rows: list[dict] = []
    for payload in payloads:
        year = payload["year"]
        code = payload["code"]
        qnum = int(payload["question_index"])
        out_dir = GENERIC_ROOT / "solutions" / year / code / f"q{qnum:02d}"
        out_dir.mkdir(parents=True, exist_ok=True)
        script = out_dir / "solution.py"
        script.write_text(
            SCRIPT_TEMPLATE.format(
                payload=json.dumps({k: v for k, v in payload.items() if k not in {"year", "code"}}, ensure_ascii=False, indent=2),
                year=year,
                code=code,
                qnum=qnum,
            ),
            encoding="utf-8",
        )
        if not args.no_run:
            completed = subprocess.run([sys.executable, str(script)], cwd=str(ROOT.parents[0]))
            if completed.returncode != 0:
                raise SystemExit(completed.returncode)
            result_path = GENERIC_ROOT / "results" / year / code / f"q{qnum:02d}" / "result.json"
            result = json.loads(result_path.read_text(encoding="utf-8"))
            method = result["experiment_result"].get("method", "generic_model")
        else:
            method = ""
        index_rows.append({
            "problem_id": payload["problem_id"],
            "year": year,
            "code": code,
            "question_index": qnum,
            "question_label": payload["question"].get("label", f"问题 {qnum}"),
            "method": method,
            "solution_path": str(script.relative_to(ROOT.parent)),
            "result_path": str((GENERIC_ROOT / "results" / year / code / f"q{qnum:02d}" / "result.json").relative_to(ROOT.parent)),
            "report_path": str((GENERIC_ROOT / "reports" / year / code / f"q{qnum:02d}" / "report.md").relative_to(ROOT.parent)),
            "artifact_dir": str((GENERIC_ROOT / "artifacts" / year / code / f"q{qnum:02d}").relative_to(ROOT.parent)),
        })

    GENERIC_ROOT.mkdir(parents=True, exist_ok=True)
    (GENERIC_ROOT / "generic_baseline_index.json").write_text(json.dumps(index_rows, ensure_ascii=False, indent=2), encoding="utf-8")
    with (GENERIC_ROOT / "generic_baseline_index.csv").open("w", encoding="utf-8-sig", newline="") as f:
        fieldnames = ["problem_id", "year", "code", "question_index", "question_label", "method", "solution_path", "result_path", "report_path", "artifact_dir"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(index_rows)
    write_readme(index_rows)
    print(f"archived {len(index_rows)} generic baselines under {GENERIC_ROOT}")


if __name__ == "__main__":
    main()
