# -*- coding: utf-8 -*-
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "lib"))
from cumcm_models import parse_problem

SCRIPT_TEMPLATE = '''# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {payload}
RESULT_PATH = ROOT / "question_results" / "{year}" / "{code}" / "q{qnum:02d}" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "{year}" / "{code}" / "q{qnum:02d}" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "{year}" / "{code}" / "q{qnum:02d}"


def main() -> None:
    result = solve_question(PAYLOAD, ARTIFACT_DIR)
    RESULT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_question_report(result, REPORT_PATH)
    print(f"wrote {{RESULT_PATH}}")
    print(f"wrote {{REPORT_PATH}}")
    print(f"wrote artifacts under {{ARTIFACT_DIR}}")


if __name__ == "__main__":
    main()
'''


def main() -> None:
    generated = []
    index = []
    manifest_path = ROOT / "attachment_manifest.json"
    attachment_manifest = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else {}
    for problem_path in sorted((ROOT / "problems").glob("*/*.md")):
        year = problem_path.parent.name
        code = problem_path.stem
        problem_id = f"{year}-{code}"
        parsed = parse_problem(problem_path)
        attachments = attachment_manifest.get(problem_id, {}).get("attachments", [])
        for qnum, question in enumerate(parsed["questions"], start=1):
            payload = {
                "problem_id": problem_id,
                "title": parsed["title"],
                "problem_path": str(problem_path),
                "question_index": qnum,
                "question": question,
                "attachments": attachments,
            }
            out_dir = ROOT / "question_solutions" / year / code / f"q{qnum:02d}"
            out_dir.mkdir(parents=True, exist_ok=True)
            script = out_dir / "solution.py"
            script.write_text(
                SCRIPT_TEMPLATE.format(
                    payload=json.dumps(payload, ensure_ascii=False, indent=2),
                    year=year,
                    code=code,
                    qnum=qnum,
                ),
                encoding="utf-8",
            )
            generated.append(script)
            index.append({
                "problem_id": problem_id,
                "year": year,
                "code": code,
                "question_index": qnum,
                "question_label": question.get("label", f"问题 {qnum}"),
                "statement": question.get("statement", ""),
                "solution_path": str(script.relative_to(ROOT.parent)),
                "result_path": str((ROOT / "question_results" / year / code / f"q{qnum:02d}" / "result.json").relative_to(ROOT.parent)),
                "report_path": str((ROOT / "question_reports" / year / code / f"q{qnum:02d}" / "report.md").relative_to(ROOT.parent)),
                "artifact_path": str((ROOT / "question_artifacts" / year / code / f"q{qnum:02d}" / "experiment_table.csv").relative_to(ROOT.parent)),
                "attachment_count": len(attachments),
            })
    (ROOT / "question_solution_index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")
    with (ROOT / "question_solution_index.csv").open("w", encoding="utf-8-sig", newline="") as f:
        fieldnames = ["problem_id", "year", "code", "question_index", "question_label", "statement", "solution_path", "result_path", "report_path", "artifact_path", "attachment_count"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(index)
    print(f"generated {len(generated)} question solution scripts")


if __name__ == "__main__":
    main()
