from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import shutil
from pathlib import Path
from typing import Iterable


REPO_ROOT = Path(__file__).resolve().parents[2]
MCM_ROOT = REPO_ROOT / "mcm"
DOC_ROOT = REPO_ROOT / "docs" / "mcm-2015-2025"
DEFAULT_OUTPUT = MCM_ROOT / "source_materials"


def repo_display(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(path.resolve())


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def wanted_problem_ids(args: argparse.Namespace) -> set[str] | None:
    requested: set[str] = set(args.problems or [])
    years = {str(year) for year in args.years or []}
    if years:
        for row in read_csv(MCM_ROOT / "problem_index.csv"):
            if row.get("year") in years:
                requested.add(row["problem_id"])
    return requested or None


def problem_rows(problem_filter: set[str] | None) -> list[dict[str, str]]:
    rows = read_csv(MCM_ROOT / "problem_index.csv")
    if problem_filter is None:
        return rows
    return [row for row in rows if row["problem_id"] in problem_filter]


def problem_statement_paths(problem_filter: set[str] | None) -> list[Path]:
    if problem_filter is None:
        return sorted((MCM_ROOT / "problems").glob("*/*.md"))
    paths: list[Path] = []
    for row in problem_rows(problem_filter):
        path = MCM_ROOT / row["problem_path"]
        if path.exists():
            paths.append(path)
    for problem_id in problem_filter:
        year, _, code = problem_id.partition("-")
        path = MCM_ROOT / "problems" / year / f"{code}.md"
        if path.exists() and path not in paths:
            paths.append(path)
    return sorted(paths)


def data_manifest_rows(problem_filter: set[str] | None) -> list[dict[str, str]]:
    rows = read_csv(MCM_ROOT / "data_manifest.csv")
    if problem_filter is None:
        return rows
    return [row for row in rows if row["problem_id"] in problem_filter]


def raw_asset_paths(problem_filter: set[str] | None) -> set[Path]:
    if problem_filter is None:
        root = DOC_ROOT / "official_assets"
        return {
            path
            for path in root.rglob("*")
            if path.is_file() and path.name != "manifest.json"
        }
    paths: set[Path] = set()
    for row in data_manifest_rows(problem_filter):
        path = (REPO_ROOT / row["relative_path"]).resolve()
        try:
            path.relative_to(DOC_ROOT / "official_assets")
        except ValueError:
            continue
        paths.add(path)
    return paths


def extracted_asset_paths(problem_filter: set[str] | None) -> set[Path]:
    if problem_filter is None:
        root = DOC_ROOT / "official_assets_extracted"
        return {
            path
            for path in root.rglob("*")
            if path.is_file() and path.name != "extract_manifest.json"
        }
    paths: set[Path] = set()
    for row in data_manifest_rows(problem_filter):
        path = (REPO_ROOT / row["relative_path"]).resolve()
        try:
            path.relative_to(DOC_ROOT / "official_assets_extracted")
        except ValueError:
            continue
        paths.add(path)
    return paths


def curated_problem_doc_paths(problem_filter: set[str] | None) -> set[Path]:
    if problem_filter is not None:
        return set()
    return {
        path
        for path in DOC_ROOT.glob("[0-9][0-9][0-9][0-9]/*/*")
        if path.is_file() and path.name in {"problem_config.json", "题目与问题.md"}
    }


def manifest_paths() -> list[tuple[str, Path]]:
    candidates = [
        ("mcm_data_manifest.csv", MCM_ROOT / "data_manifest.csv"),
        ("mcm_data_manifest.json", MCM_ROOT / "data_manifest.json"),
        ("mcm_problem_index.csv", MCM_ROOT / "problem_index.csv"),
        ("mcm_problem_index.json", MCM_ROOT / "problem_index.json"),
        ("mcm_question_solution_index.csv", MCM_ROOT / "question_solution_index.csv"),
        ("mcm_question_solution_index.json", MCM_ROOT / "question_solution_index.json"),
        ("official_assets_manifest.json", DOC_ROOT / "official_assets" / "manifest.json"),
        ("official_assets_extract_manifest.json", DOC_ROOT / "official_assets_extracted" / "extract_manifest.json"),
    ]
    return [(name, path) for name, path in candidates if path.exists()]


def relative_dest_for_source(path: Path, output_root: Path) -> tuple[str, Path]:
    raw_root = DOC_ROOT / "official_assets"
    extracted_root = DOC_ROOT / "official_assets_extracted"
    problems_root = MCM_ROOT / "problems"

    try:
        return "official_download", output_root / "official_downloads" / path.relative_to(raw_root)
    except ValueError:
        pass
    try:
        return "official_extracted", output_root / "official_extracted" / path.relative_to(extracted_root)
    except ValueError:
        pass
    try:
        return "problem_statement_markdown", output_root / "problem_statements" / path.relative_to(problems_root)
    except ValueError:
        pass
    try:
        return "curated_problem_doc", output_root / "curated_problem_docs" / path.relative_to(DOC_ROOT)
    except ValueError:
        pass
    raise ValueError(f"cannot place source path: {path}")


def place_file(source: Path, destination: Path, storage: str) -> str:
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists() or destination.is_symlink():
        destination.unlink()
    if storage == "copy":
        shutil.copy2(source, destination)
        return "copy"
    if storage == "symlink":
        os.symlink(source, destination)
        return "symlink"
    try:
        os.link(source, destination)
        return "hardlink"
    except OSError:
        shutil.copy2(source, destination)
        return "copy_fallback"


def source_lookup_by_path() -> dict[Path, dict[str, str]]:
    lookup: dict[Path, dict[str, str]] = {}
    for row in read_csv(MCM_ROOT / "data_manifest.csv"):
        if not row.get("relative_path"):
            continue
        lookup[(REPO_ROOT / row["relative_path"]).resolve()] = row
    return lookup


def problem_lookup_by_statement_path() -> dict[Path, dict[str, str]]:
    lookup: dict[Path, dict[str, str]] = {}
    for row in read_csv(MCM_ROOT / "problem_index.csv"):
        path = MCM_ROOT / row["problem_path"]
        lookup[path.resolve()] = row
    return lookup


def infer_problem_from_statement_path(path: Path) -> dict[str, str]:
    try:
        rel = path.relative_to(MCM_ROOT / "problems")
    except ValueError:
        return {}
    if len(rel.parts) != 2:
        return {}
    year = rel.parts[0]
    code = rel.stem
    return {"problem_id": f"{year}-{code}", "year": year, "code": code}


def infer_year_from_path(path: Path) -> str:
    for root in [DOC_ROOT / "official_assets", DOC_ROOT / "official_assets_extracted", DOC_ROOT, MCM_ROOT / "problems"]:
        try:
            rel = path.relative_to(root)
        except ValueError:
            continue
        if rel.parts:
            return rel.parts[0]
    return ""


def write_manifest_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "collection",
        "problem_id",
        "year",
        "kind",
        "source_path",
        "archive_path",
        "size_bytes",
        "sha256",
        "storage_mode",
    ]
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_readme(output_root: Path, rows: list[dict[str, object]], storage: str) -> None:
    counts: dict[str, int] = {}
    bytes_by_collection: dict[str, int] = {}
    for row in rows:
        collection = str(row["collection"])
        counts[collection] = counts.get(collection, 0) + 1
        bytes_by_collection[collection] = bytes_by_collection.get(collection, 0) + int(row["size_bytes"])

    lines = [
        "# MCM 赛题源资料归档",
        "",
        "本目录集中保存 MCM/ICM 赛题原文件、官方下载数据、解压附件，以及真实数据工作流使用的规范化题面 Markdown。",
        "",
        "## 目录",
        "",
        "- `official_downloads/`：从 COMAP 下载的原始文件，包括 PDF、ZIP、工作簿和无扩展名下载件。",
        "- `official_extracted/`：解压后的 PDF、CSV、XLSX 等附件数据。",
        "- `problem_statements/`：来自 `mcm/problems` 的规范化题面 Markdown。",
        "- `curated_problem_docs/`：早期逐题整理的题面说明和 `problem_config.json`。",
        "- `manifests/`：复制过来的索引、下载清单和解压清单。",
        "- `material_manifest.csv/json`：本目录每个文件的审计清单，含来源路径、归档路径、大小和 SHA-256。",
        "",
        "## 重新生成",
        "",
        "```bash",
        "/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python mcm/scripts/organize_source_materials.py --all",
        "```",
        "",
        f"默认存储方式：`{storage}`。脚本会优先使用 hardlink，让资料夹可直接浏览，同时避免在磁盘上重复复制大数据集。",
        "",
        "## 文件统计",
        "",
    ]
    for collection, count in sorted(counts.items()):
        size_mb = bytes_by_collection[collection] / (1024 * 1024)
        lines.append(f"- `{collection}`: {count} files, {size_mb:.2f} MiB")
    lines.append("")
    output_root.mkdir(parents=True, exist_ok=True)
    (output_root / "README.md").write_text("\n".join(lines), encoding="utf-8")


def iter_material_sources(problem_filter: set[str] | None) -> Iterable[Path]:
    for path in problem_statement_paths(problem_filter):
        yield path.resolve()
    yield from sorted(raw_asset_paths(problem_filter))
    yield from sorted(extracted_asset_paths(problem_filter))
    yield from sorted(curated_problem_doc_paths(problem_filter))


def organize(output_root: Path, problem_filter: set[str] | None, storage: str) -> list[dict[str, object]]:
    data_lookup = source_lookup_by_path()
    problem_lookup = problem_lookup_by_statement_path()
    rows: list[dict[str, object]] = []
    seen_sources: set[Path] = set()

    for source in iter_material_sources(problem_filter):
        source = source.resolve()
        if source in seen_sources:
            continue
        seen_sources.add(source)
        collection, destination = relative_dest_for_source(source, output_root)
        storage_mode = place_file(source, destination, storage)
        data_row = data_lookup.get(source, {})
        problem_row = problem_lookup.get(source, {}) or infer_problem_from_statement_path(source)
        year = data_row.get("year") or problem_row.get("year") or infer_year_from_path(source)
        rows.append(
            {
                "collection": collection,
                "problem_id": data_row.get("problem_id") or problem_row.get("problem_id", ""),
                "year": year,
                "kind": data_row.get("kind") or source.suffix.lower().lstrip(".") or "file",
                "source_path": repo_display(source),
                "archive_path": repo_display(destination),
                "size_bytes": source.stat().st_size,
                "sha256": sha256_file(source),
                "storage_mode": storage_mode,
            }
        )

    for name, source in manifest_paths():
        destination = output_root / "manifests" / name
        storage_mode = place_file(source.resolve(), destination, storage)
        rows.append(
            {
                "collection": "manifest",
                "problem_id": "",
                "year": "",
                "kind": source.suffix.lower().lstrip(".") or "file",
                "source_path": repo_display(source),
                "archive_path": repo_display(destination),
                "size_bytes": source.stat().st_size,
                "sha256": sha256_file(source),
                "storage_mode": storage_mode,
            }
        )

    rows.sort(key=lambda row: (str(row["collection"]), str(row["year"]), str(row["archive_path"])))
    (output_root / "material_manifest.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    write_manifest_csv(output_root / "material_manifest.csv", rows)
    write_readme(output_root, rows, storage)
    return rows


def verify(output_root: Path) -> list[str]:
    manifest_path = output_root / "material_manifest.json"
    if not manifest_path.exists():
        return [f"missing manifest: {manifest_path}"]
    rows = json.loads(manifest_path.read_text(encoding="utf-8"))
    errors: list[str] = []
    for row in rows:
        path = REPO_ROOT / row["archive_path"]
        if not path.exists():
            errors.append(f"missing archived file: {row['archive_path']}")
            continue
        if path.stat().st_size != int(row["size_bytes"]):
            errors.append(f"size mismatch: {row['archive_path']}")
            continue
        if sha256_file(path) != row["sha256"]:
            errors.append(f"sha256 mismatch: {row['archive_path']}")
    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description="Organize MCM original problem files and official data attachments into one source-materials folder.")
    parser.add_argument("--all", action="store_true", help="organize all MCM source materials; this is also the default")
    parser.add_argument("--problems", nargs="*", help="limit to problem ids such as 2018-A 2025-C")
    parser.add_argument("--years", nargs="*", help="limit to years such as 2024 2025")
    parser.add_argument("--output-root", default=str(DEFAULT_OUTPUT), help="target source-materials folder")
    parser.add_argument("--storage", choices=["hardlink", "copy", "symlink"], default="hardlink", help="how to place files in the organized folder")
    parser.add_argument("--verify-only", action="store_true", help="only verify an existing organized folder")
    args = parser.parse_args()

    output_root = Path(args.output_root).resolve()
    problem_filter = wanted_problem_ids(args)
    if args.verify_only:
        rows = json.loads((output_root / "material_manifest.json").read_text(encoding="utf-8"))
    else:
        rows = organize(output_root, problem_filter, args.storage)
    errors = verify(output_root)
    summary = {
        "source_materials": str(output_root),
        "file_count": len(rows),
        "storage": args.storage,
        "verification_errors": len(errors),
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    if errors:
        for error in errors[:50]:
            print(f"- {error}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
