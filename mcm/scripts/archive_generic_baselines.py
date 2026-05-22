from __future__ import annotations

import argparse
import csv
import json
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
MCM_ROOT = REPO_ROOT / "mcm"
DEFAULT_BASE = MCM_ROOT / "generic_baselines"
VENV_PYTHON = REPO_ROOT / ".venv" / "bin" / "python"
sys.path.insert(0, str(MCM_ROOT / "lib"))
from generic_baseline import select_generic_model


SCRIPT_TEMPLATE = '''from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path({repo_root!r})
BASE = Path({base!r})
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {payload}
RESULT_PATH = BASE / "results" / {year!r} / {code!r} / {question!r} / "result.json"
REPORT_PATH = BASE / "reports" / {year!r} / {code!r} / {question!r} / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / {year!r} / {code!r} / {question!r}


def main() -> None:
    result = solve_question_generic_baseline(PAYLOAD, ARTIFACT_DIR)
    RESULT_PATH.parent.mkdir(parents=True, exist_ok=True)
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_generic_report(result, REPORT_PATH, Path(__file__).resolve())
    print(f"wrote {{RESULT_PATH}}")
    print(f"wrote {{REPORT_PATH}}")
    print(f"wrote artifacts under {{ARTIFACT_DIR}}")


if __name__ == "__main__":
    main()
'''


def display_path(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(path.resolve())


def question_index_rows(problem_filter: set[str] | None) -> list[dict[str, str]]:
    rows = json.loads((MCM_ROOT / "question_solution_index.json").read_text(encoding="utf-8"))
    if problem_filter is None:
        return rows
    return [row for row in rows if row["problem_id"] in problem_filter]


def write_readme(base: Path, index_rows: list[dict[str, str]]) -> None:
    method_counts: dict[str, int] = {}
    for row in index_rows:
        method_counts[row["method"]] = method_counts.get(row["method"], 0) + 1
    command_base = ".venv/bin/python mcm/scripts/archive_generic_baselines.py --all"
    lines = [
        "# MCM 通用基线归档",
        "",
        "本目录保存 MCM 真实赛题工作流之上的最低可运行通用基线。它用于保留第一版建模脚手架和覆盖检查，不替代 `mcm/question_solutions` 中的真实数据工作流。",
        "",
        "## 目录",
        "",
        "- `solutions/`：每问一个可重新运行的通用基线 `solution.py`。",
        "- `results/`：通用基线 `result.json`。",
        "- `reports/`：通用基线 Markdown 报告。",
        "- `artifacts/`：通用基线实验表。",
        "- `generic_baseline_index.csv/json`：通用基线索引。",
        "",
        "## 重新生成",
        "",
        "```bash",
        command_base,
        "```",
        "",
        "## 方法分布",
        "",
    ]
    for method, count in sorted(method_counts.items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"- `{method}`：{count} 问")
    lines.append("")
    base.mkdir(parents=True, exist_ok=True)
    (base / "README.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Archive MCM first-pass generic baselines.")
    parser.add_argument("--all", action="store_true", help="archive all MCM question-index rows")
    parser.add_argument("--problems", nargs="*", help="problem ids to archive, e.g. 2018-A 2025-C")
    parser.add_argument("--output-root", help="override generic baseline output root")
    parser.add_argument("--no-run", action="store_true", help="write solution scripts and index without executing them")
    args = parser.parse_args()

    base = Path(args.output_root).resolve() if args.output_root else DEFAULT_BASE
    if args.problems:
        problem_filter = set(args.problems)
    else:
        problem_filter = None
    rows = question_index_rows(problem_filter)
    if not rows:
        raise SystemExit("no MCM question rows matched the requested filter")

    index_rows: list[dict[str, str]] = []
    for row in rows:
        year = row["year"]
        code = row["code"]
        question = row["question"]
        solution = base / "solutions" / year / code / question / "solution.py"
        result_path = base / "results" / year / code / question / "result.json"
        report_path = base / "reports" / year / code / question / "report.md"
        artifact_dir = base / "artifacts" / year / code / question
        payload = {
            "problem_id": row["problem_id"],
            "year": year,
            "code": code,
            "question": question,
            "question_title": row["title"],
            "statement": row["statement"],
            "methods": row["methods"],
            "source_type": row["source_type"],
            "solution_path": row["solution_path"],
            "result_path": row["result_path"],
            "report_path": row["report_path"],
            "artifact_path": row["artifact_path"],
        }
        solution.parent.mkdir(parents=True, exist_ok=True)
        solution.write_text(
            SCRIPT_TEMPLATE.format(
                repo_root=str(REPO_ROOT),
                base=str(base),
                payload=json.dumps(payload, ensure_ascii=False, indent=2),
                year=year,
                code=code,
                question=question,
            ),
            encoding="utf-8",
        )
        model = select_generic_model(payload)
        if not args.no_run:
            completed = subprocess.run([str(VENV_PYTHON), str(solution)], cwd=str(REPO_ROOT), text=True, capture_output=True, timeout=120)
            if completed.returncode != 0:
                raise RuntimeError(f"{solution} failed\nSTDOUT:\n{completed.stdout}\nSTDERR:\n{completed.stderr}")
            result = json.loads(result_path.read_text(encoding="utf-8"))
            method = result["experiment_result"]["method"]
        else:
            method = model["method"]
        index_rows.append(
            {
                "problem_id": row["problem_id"],
                "year": year,
                "code": code,
                "question": question,
                "question_index": question.lstrip("q"),
                "question_label": row["title"],
                "method": method,
                "solution_path": display_path(solution),
                "result_path": display_path(result_path),
                "report_path": display_path(report_path),
                "artifact_dir": display_path(artifact_dir),
                "real_solution_path": row["solution_path"],
            }
        )

    base.mkdir(parents=True, exist_ok=True)
    (base / "generic_baseline_index.json").write_text(json.dumps(index_rows, ensure_ascii=False, indent=2), encoding="utf-8")
    with (base / "generic_baseline_index.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        fieldnames = [
            "problem_id",
            "year",
            "code",
            "question",
            "question_index",
            "question_label",
            "method",
            "solution_path",
            "result_path",
            "report_path",
            "artifact_dir",
            "real_solution_path",
        ]
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(index_rows)
    write_readme(base, index_rows)
    print(f"archived {len(index_rows)} MCM generic baselines under {base}")


if __name__ == "__main__":
    main()
