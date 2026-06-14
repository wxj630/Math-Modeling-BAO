from __future__ import annotations

import csv
import json
import shutil
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[2]


def repo_rel(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def scalar(value: Any) -> str:
    if isinstance(value, float):
        return f"{value:.6g}"
    if isinstance(value, (int, bool)):
        return str(value)
    text = str(value).replace("\n", " ").strip()
    return text[:120] + ("..." if len(text) > 120 else "")


def summarize(value: Any, limit: int = 4) -> str:
    if isinstance(value, dict):
        parts = []
        for key, sub_value in value.items():
            if isinstance(sub_value, (str, int, float, bool)):
                parts.append(f"{key}={scalar(sub_value)}")
            elif isinstance(sub_value, list):
                parts.append(f"{key}={len(sub_value)}项")
            elif isinstance(sub_value, dict):
                parts.append(f"{key}={len(sub_value)}项")
            if len(parts) >= limit:
                break
        return "；".join(parts) or "见 result.json"
    if isinstance(value, list):
        return f"{len(value)}项"
    return scalar(value)


def copy_question_artifacts(code: str, output_dir: Path) -> dict[str, str]:
    source_root = REPO_ROOT / "cumcm" / "question_artifacts" / "2025" / code
    target_root = output_dir / "artifacts"
    target_root.mkdir(parents=True, exist_ok=True)
    copied: dict[str, str] = {}
    if not source_root.exists():
        return copied
    for source in sorted(source_root.glob("q*/*")):
        if source.is_file():
            qid = source.parent.name
            target_dir = target_root / qid
            target_dir.mkdir(parents=True, exist_ok=True)
            target = target_dir / source.name
            shutil.copy2(source, target)
            copied[f"{qid}/{source.stem}"] = repo_rel(target)
    return copied


def load_question_chain(code: str) -> list[dict[str, Any]]:
    result_root = REPO_ROOT / "cumcm" / "question_results" / "2025" / code
    rows: list[dict[str, Any]] = []
    for path in sorted(result_root.glob("q*/result.json")):
        result = read_json(path)
        qid = path.parent.name
        rows.append(
            {
                "question": qid,
                "question_label": result.get("question_label") or qid,
                "tasks": result.get("tasks", []),
                "selected_model": result.get("selected_model", {}),
                "experiment_result": result.get("experiment_result", {}),
                "result_path": repo_rel(path),
                "report_path": f"cumcm/question_reports/2025/{code}/{qid}/report.md",
                "artifact_dir": f"cumcm/question_artifacts/2025/{code}/{qid}",
            }
        )
    return rows


def write_summary_csv(question_chain: list[dict[str, Any]], output_dir: Path) -> str:
    artifact_dir = output_dir / "artifacts"
    artifact_dir.mkdir(parents=True, exist_ok=True)
    path = artifact_dir / "question_result_summary.csv"
    with path.open("w", encoding="utf-8-sig", newline="") as file:
        writer = csv.writer(file, lineterminator="\n")
        writer.writerow(["question", "selected_model", "experiment_summary", "result_path", "report_path"])
        for row in question_chain:
            selected = row.get("selected_model") or {}
            writer.writerow(
                [
                    row["question"],
                    selected.get("name") or selected.get("key") or "",
                    summarize(row.get("experiment_result", {}), limit=5),
                    row["result_path"],
                    row["report_path"],
                ]
            )
    return repo_rel(path)


def write_report(config: dict[str, Any], result: dict[str, Any], output_dir: Path) -> None:
    lines = [
        f"# {config['problem_id']} Outstanding 复现：{config['paper_id']}",
        "",
        "## 复现对象",
        f"- 获奖论文：`{config['paper_id']}`，{config['paper_title']}",
        f"- OCR 来源：`{config['paper_source_ocr']}`",
        f"- PDF 来源：`{config['paper_source_pdf']}`",
        f"- 复现定位：{config['scope']}",
        "",
        "## 问题与建模",
        config["narrative"],
        "",
        "## 代码与实验",
        "- `solution.py` 聚合当前 CUMCM advanced 的逐问 `result.json`、`report.md` 和 artifacts。",
        "- 输出赛题级 `result.json`、`report.md`、`artifacts/question_result_summary.csv` 和逐问 artifact 副本。",
        "- 这一步把逐问实验结果组织成获奖论文的整题模型链，后续可继续替换为更细的论文原算法。",
        "",
        "## 逐问结果",
        "",
        "| 小问 | Advanced 模型 | 实验摘要 |",
        "|---|---|---|",
    ]
    for row in result["question_chain"]:
        selected = row.get("selected_model") or {}
        lines.append(
            f"| {row['question']} | {selected.get('name') or selected.get('key') or '见报告'} | {summarize(row.get('experiment_result', {}), limit=4)} |"
        )
    lines.extend(
        [
            "",
            "## 相对 Advanced 的优势",
            result["difference_from_advanced"],
            "",
            "## 输出产物",
        ]
    )
    for key, path in result["artifact_paths"].items():
        lines.append(f"- `{key}`：`{path}`")
    (output_dir / "report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def run(config: dict[str, Any], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    question_chain = load_question_chain(config["code"])
    artifact_paths = copy_question_artifacts(config["code"], output_dir)
    artifact_paths["question_result_summary"] = write_summary_csv(question_chain, output_dir)
    key_models = sorted(
        {
            (row.get("selected_model") or {}).get("name") or (row.get("selected_model") or {}).get("key") or "见报告"
            for row in question_chain
        }
    )
    result = {
        "problem_id": config["problem_id"],
        "year": 2025,
        "code": config["code"],
        "paper_id": config["paper_id"],
        "paper_title": config["paper_title"],
        "paper_source_ocr": config["paper_source_ocr"],
        "paper_source_pdf": config["paper_source_pdf"],
        "reproduction_scope": config["scope"],
        "selected_model": {
            "name": config["selected_model"],
            "chapter": f"Outstanding reproduction of {config['paper_id']}",
        },
        "paper_model_alignment": {
            "paper_methods": config["paper_methods"],
            "repo_kernel": key_models,
        },
        "question_chain": question_chain,
        "experiment_result": {
            "implemented_questions": len(question_chain),
            "key_models": "；".join(key_models),
            "first_question_summary": summarize(question_chain[0]["experiment_result"], limit=5) if question_chain else "",
            "artifact_count": len(artifact_paths),
        },
        "difference_from_advanced": config["difference_from_advanced"],
        "artifact_paths": artifact_paths,
        "limitations": config["limitations"],
    }
    (output_dir / "result.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_report(config, result, output_dir)
    print(json.dumps({"result": repo_rel(output_dir / "result.json"), "report": repo_rel(output_dir / "report.md")}, ensure_ascii=False, indent=2))
