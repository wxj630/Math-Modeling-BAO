#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Import CUMCM problem statements from organized source materials.

The source archive is intentionally kept outside Git because it contains large
PDFs and attachments. This script extracts the canonical problem statement text
from local `cumcm/source_materials/manifest.csv`, writes local problem Markdown,
and rebuilds the lightweight problem index used by the tutorial generator.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path
from typing import Iterable

import fitz

ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = ROOT.parent
sys.path.insert(0, str(ROOT / "lib"))
from cumcm_models import parse_problem, recommend_models

PROBLEM_FIELDS = [
    "year",
    "code",
    "problem_id",
    "title",
    "core",
    "question_count",
    "recommended_models",
    "problem_path",
    "solution_path",
    "result_path",
    "report_path",
]


def normalize_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [re.sub(r"[ \t]+", " ", line).strip() for line in text.splitlines()]
    compact: list[str] = []
    blank = False
    for line in lines:
        if not line:
            if not blank:
                compact.append("")
            blank = True
            continue
        compact.append(line)
        blank = False
    return "\n".join(compact).strip()


def extract_pdf_text(path: Path) -> str:
    with fitz.open(str(path)) as doc:
        pages = [page.get_text("text") for page in doc]
    return normalize_text("\n".join(pages))


def read_manifest() -> list[dict[str, str]]:
    path = ROOT / "source_materials" / "manifest.csv"
    if not path.exists():
        raise SystemExit(f"missing CUMCM source manifest: {path}")
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def problem_document_rows() -> dict[str, dict[str, str]]:
    rows: dict[str, dict[str, str]] = {}
    for row in read_manifest():
        if row.get("file_kind") != "problem_document":
            continue
        year = row.get("year", "")
        code = row.get("problem_code", "")
        if not year or code not in {"A", "B", "C", "D", "E"}:
            continue
        path = REPO_ROOT / row.get("dest_path", "")
        if not path.exists():
            continue
        key = f"{year}-{code}"
        current = rows.get(key)
        if current is None:
            rows[key] = row
            continue
        current_path = Path(current.get("dest_path", ""))
        # Prefer the direct problem PDF over nested archives when both exist.
        if path.suffix.lower() == ".pdf" and current_path.suffix.lower() != ".pdf":
            rows[key] = row
    return rows


def title_from_text(year: str, code: str, text: str) -> str:
    match = re.search(rf"(?m)^\s*{code}\s*题\s+(.+?)\s*$", text)
    raw_title = match.group(1).strip() if match else code
    raw_title = re.sub(r"\s+", " ", raw_title).strip(" ：:")
    return f"{year}年 CUMCM {code}题：{raw_title}"


def model_line(model: dict[str, object]) -> str:
    keywords = "、".join(str(item) for item in model.get("keywords", []))
    return f"    - {model['name']}（{model['chapter']}；关键词：{keywords or '通用'}）"


def build_core(title: str, text: str, questions: list[dict[str, object]]) -> str:
    models = recommend_models(text, limit=3)
    model_names = "、".join(str(item["name"]) for item in models)
    first_statement = ""
    for question in questions:
        statement = str(question.get("statement", "")).strip()
        if statement:
            first_statement = statement
            break
    if len(first_statement) > 220:
        first_statement = first_statement[:220].rstrip() + "..."
    suffix = f"第一问通常给出主要建模入口：{first_statement}" if first_statement else "建议先从题面数据、约束和目标函数三方面建立可计算结构。"
    return (
        f"本题核心是把 `{title}` 的业务场景转化为可计算的数学模型，"
        f"重点围绕 {model_names} 展开；起手应先梳理变量、约束、目标函数/评价指标，再按每问逐步建模。"
        f"{suffix}"
    )


def build_problem_markdown(year: str, code: str, text: str) -> str:
    title = title_from_text(year, code, text)
    temporary = f"# {title}\n\n## 题目原文\n{text}\n"
    tmp_path = ROOT / ".tmp_import_problem.md"
    tmp_path.write_text(temporary, encoding="utf-8")
    try:
        parsed = parse_problem(tmp_path)
    finally:
        tmp_path.unlink(missing_ok=True)

    questions = parsed["questions"]
    core = build_core(title, text, questions)
    lines = [
        f"# {title}",
        "",
        "## 题目原文",
        text,
        "",
        "## 题目核心",
        core,
        "",
        "## 每问/每小问与典型模型参考",
        "",
    ]
    for qnum, question in enumerate(questions, start=1):
        label = str(question.get("label") or f"问题{qnum}")
        statement = str(question.get("statement", "")).strip()
        lines += [f"### {label}", ""]
        if statement:
            lines += ["**原问摘录**：" + statement, ""]
        tasks = list(question.get("tasks", []))
        if tasks:
            lines += ["**需要完成**："]
            for idx, task in enumerate(tasks, start=1):
                lines.append(f"- 任务 {qnum}.{idx}：{task}")
            lines.append("")
        models = list(question.get("models", [])) or recommend_models(statement, limit=3)
        if models:
            lines += ["**适合模型**："]
            lines.extend(model_line(model) for model in models)
            lines.append("")
        lines += [
            f"**代码实现提示**：先在 `cumcm/solutions/{year}/{code}/solution.py` 中替换真实附件数据读取，再复用 `cumcm/lib/cumcm_models.py` 中同类模型函数完成可复现实验。",
            "",
        ]
    lines += [
        "## 使用说明",
        "- `题目原文` 保留原始赛题文本，便于论文复核。",
        "- `每问/每小问` 是面向建模训练的任务拆解，不替代正式论文中的变量定义与假设。",
        "- 对含附件数据的题目，应优先把附件读取、清洗和单位换算补入对应 `solution.py`。",
        "",
    ]
    return "\n".join(lines)


def selected_problem_ids(args: argparse.Namespace, rows: dict[str, dict[str, str]]) -> list[str]:
    if args.problems:
        return sorted(args.problems)
    years = {str(item) for item in args.years or []}
    if years:
        return sorted(pid for pid in rows if pid.split("-", 1)[0] in years)
    if args.missing_only:
        return sorted(pid for pid in rows if not (ROOT / "problems" / pid[:4] / f"{pid.split('-')[1]}.md").exists())
    return sorted(rows)


def import_problem(pid: str, row: dict[str, str], overwrite: bool) -> Path | None:
    year, code = pid.split("-", 1)
    output = ROOT / "problems" / year / f"{code}.md"
    if output.exists() and not overwrite:
        return None
    source = REPO_ROOT / row["dest_path"]
    if source.suffix.lower() != ".pdf":
        raise SystemExit(f"unsupported source type for {pid}: {source}")
    text = extract_pdf_text(source)
    if len(text) < 200:
        raise SystemExit(f"extracted text is too short for {pid}: {source}")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(build_problem_markdown(year, code, text), encoding="utf-8")
    return output


def extract_section(text: str, heading: str) -> str:
    marker = f"## {heading}"
    if marker not in text:
        return ""
    section = text.split(marker, 1)[1]
    match = re.search(r"\n##\s+", section)
    if match:
        section = section[: match.start()]
    return re.sub(r"\s+", " ", section).strip()


def iter_problem_paths() -> Iterable[Path]:
    return sorted((ROOT / "problems").glob("*/*.md"), key=lambda p: (p.parent.name, p.stem))


def rebuild_problem_index() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for path in iter_problem_paths():
        year = path.parent.name
        code = path.stem
        problem_id = f"{year}-{code}"
        parsed = parse_problem(path)
        text = path.read_text(encoding="utf-8", errors="ignore")
        models = recommend_models(parsed["text"])
        rows.append(
            {
                "year": year,
                "code": code,
                "problem_id": problem_id,
                "title": parsed["title"],
                "core": extract_section(text, "题目核心") or build_core(parsed["title"], parsed["text"], parsed["questions"]),
                "question_count": str(len(parsed["questions"])),
                "recommended_models": "；".join(f"{item['name']}({item['chapter']})" for item in models),
                "problem_path": str(path.relative_to(REPO_ROOT)),
                "solution_path": f"cumcm/solutions/{year}/{code}/solution.py",
                "result_path": f"cumcm/results/{year}/{code}/result.json",
                "report_path": f"cumcm/reports/{year}/{code}/report.md",
            }
        )

    with (ROOT / "problem_index.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=PROBLEM_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    json_rows = [
        {
            "year": row["year"],
            "code": row["code"],
            "problem_id": row["problem_id"],
            "problem": row["problem_path"],
            "solution": row["solution_path"],
            "result": row["result_path"],
            "report": row["report_path"],
        }
        for row in rows
    ]
    (ROOT / "problem_index.json").write_text(json.dumps(json_rows, ensure_ascii=False, indent=2), encoding="utf-8")
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--years", nargs="*", help="years to import, e.g. 2022 2023")
    parser.add_argument("--problems", nargs="*", help="problem ids to import, e.g. 2022-A 2023-C")
    parser.add_argument("--missing-only", action="store_true", help="only import statements not present under cumcm/problems")
    parser.add_argument("--overwrite", action="store_true", help="overwrite existing local problem markdown")
    parser.add_argument("--rebuild-index-only", action="store_true", help="skip import and only rebuild cumcm/problem_index.*")
    args = parser.parse_args()

    rows = problem_document_rows()
    imported: list[Path] = []
    if not args.rebuild_index_only:
        for pid in selected_problem_ids(args, rows):
            if pid not in rows:
                raise SystemExit(f"no local problem document found for {pid}")
            output = import_problem(pid, rows[pid], overwrite=args.overwrite)
            if output is not None:
                imported.append(output)

    index_rows = rebuild_problem_index()
    print(json.dumps({"imported": [str(path.relative_to(REPO_ROOT)) for path in imported], "problem_count": len(index_rows)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
