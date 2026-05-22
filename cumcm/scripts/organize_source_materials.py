#!/usr/bin/env python3
"""Collect CUMCM original files, downloads, attachments, and converted text.

The script is intentionally conservative: it copies files into a single
repository folder and never deletes or moves the original working directories.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import shutil
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_TARGET_ROOT = REPO_ROOT / "cumcm" / "source_materials"
DEFAULT_PLAYGROUND_ROOT = Path(os.environ.get("CUMCM_PLAYGROUND_ROOT", "../../Documents/Playground"))


@dataclass(frozen=True)
class SourceStage:
    name: str
    source_root: Path
    description: str


STAGE_DEFINITIONS = (
    SourceStage(
        "raw_downloads",
        DEFAULT_PLAYGROUND_ROOT / "cumcm_raw",
        "官网下载页面、下载索引和原始赛题压缩包",
    ),
    SourceStage(
        "extracted",
        DEFAULT_PLAYGROUND_ROOT / "cumcm_unzipped",
        "原始压缩包解压后的赛题文件、数据和附件",
    ),
    SourceStage(
        "reextracted",
        DEFAULT_PLAYGROUND_ROOT / "cumcm_reextract",
        "对部分附件和文档进行补充重抽取后的材料",
    ),
    SourceStage(
        "cleaned_text",
        DEFAULT_PLAYGROUND_ROOT / "cumcm_clean",
        "题面转换后的 markdown、清洗摘要和索引",
    ),
    SourceStage(
        "markdown_exports",
        DEFAULT_PLAYGROUND_ROOT / "cumcm_markdown",
        "早期 markdown 转换输出目录；当前可能为空但保留过程节点",
    ),
)

PROBLEM_CODE_RE = re.compile(r"(?:^|[^A-Za-z])([A-E])(?:题|[-_ ]|$)", re.IGNORECASE)
YEAR_RE = re.compile(r"(20\d{2})")
DOC_SUFFIXES = {".pdf", ".doc", ".docx", ".wps", ".rtf"}
DATA_SUFFIXES = {".csv", ".tsv", ".xls", ".xlsx", ".mat", ".txt", ".json"}
ARCHIVE_SUFFIXES = {".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"}
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tif", ".tiff"}
VIDEO_SUFFIXES = {".mp4", ".avi", ".mov", ".mkv"}
TEXT_SUFFIXES = {".md", ".html", ".htm"}


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(chunk_size), b""):
            digest.update(chunk)
    return digest.hexdigest()


def iter_files(root: Path) -> Iterable[Path]:
    if not root.exists():
        return []
    return sorted(p for p in root.rglob("*") if p.is_file())


def infer_year(path: Path) -> str:
    match = YEAR_RE.search(str(path))
    return match.group(1) if match else ""


def infer_problem_code(path: Path) -> str:
    parts = [p for p in path.parts if p]
    for part in reversed(parts):
        cleaned = part.replace("Problem", "").replace("problem", "")
        match = PROBLEM_CODE_RE.search(cleaned)
        if match:
            return match.group(1).upper()
        if len(cleaned) == 1 and cleaned.upper() in {"A", "B", "C", "D", "E"}:
            return cleaned.upper()
        if cleaned in {"A题", "B题", "C题", "D题", "E题"}:
            return cleaned[0]
    return ""


def classify_file(path: Path, stage_name: str) -> str:
    suffix = path.suffix.lower()
    name = path.name.lower()
    if stage_name == "raw_downloads" and suffix in ARCHIVE_SUFFIXES:
        return "raw_archive"
    if suffix in ARCHIVE_SUFFIXES:
        return "nested_archive"
    if suffix in DOC_SUFFIXES:
        if "附件" in path.name and not re.search(r"(?:^|[-_ ])problem[-_ ]?[a-e]|[a-e]题", name):
            return "attachment_document"
        return "problem_document"
    if suffix in DATA_SUFFIXES:
        if path.name in {"problem_archives.csv", "cumcm_problem_summary.csv"}:
            return "source_index"
        return "data_attachment"
    if suffix in IMAGE_SUFFIXES:
        return "image_attachment"
    if suffix in VIDEO_SUFFIXES:
        return "media_attachment"
    if suffix in TEXT_SUFFIXES:
        return "converted_text"
    return "other_attachment"


def copy_if_needed(source: Path, destination: Path, digest: str) -> str:
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists() and destination.is_file():
        if destination.stat().st_size == source.stat().st_size and sha256_file(destination) == digest:
            return "skipped_existing"
        shutil.copy2(source, destination)
        return "updated"
    shutil.copy2(source, destination)
    return "copied"


def load_download_urls(raw_root: Path) -> dict[str, dict[str, str]]:
    csv_path = raw_root / "problem_archives.csv"
    if not csv_path.exists():
        return {}
    rows_by_token: dict[str, dict[str, str]] = {}
    with csv_path.open("r", encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            url = row.get("url", "")
            token = Path(url).name if url else ""
            if token:
                rows_by_token[token] = row
    return rows_by_token


def build_readme(target_root: Path, stages: tuple[SourceStage, ...], counts: Counter[str], total_bytes: int) -> None:
    readme = target_root / "README.md"
    stage_lines = "\n".join(
        f"| `{stage.name}` | `{stage.source_root}` | {stage.description} | {counts.get(stage.name, 0)} |"
        for stage in stages
    )
    size_mb = total_bytes / 1024 / 1024
    readme.write_text(
        "# CUMCM Source Materials\n\n"
        "这个目录集中保存 CUMCM 赛题原文件、官网下载数据、解压附件、补充重抽取文件和清洗后的 markdown/索引。\n\n"
        "整理脚本只复制文件，不移动、不删除原始工作目录；这样既能在仓库内集中查找，也保留下载和清洗过程。\n\n"
        "## 目录结构\n\n"
        "| 子目录 | 来源目录 | 内容 | 文件数 |\n"
        "| --- | --- | --- | ---: |\n"
        f"{stage_lines}\n\n"
        "## 索引文件\n\n"
        "- `manifest.csv`: 每个归档文件的来源、目标路径、年份、题号、类型、大小和 sha256。\n"
        "- `manifest.json`: 与 CSV 等价的机器可读索引。\n"
        "- `summary.json`: 各阶段文件数量、总大小和整理脚本信息。\n\n"
        "## 复跑方式\n\n"
        "```bash\n"
        "cd .\n"
        ".venv/bin/python cumcm/scripts/organize_source_materials.py\n"
        "```\n\n"
        f"当前 manifest 覆盖 `{sum(counts.values())}` 个文件，源文件总大小约 `{size_mb:.2f} MiB`。\n",
        encoding="utf-8",
    )


def organize(target_root: Path, stages: tuple[SourceStage, ...]) -> dict[str, object]:
    target_root.mkdir(parents=True, exist_ok=True)
    download_rows = load_download_urls(DEFAULT_PLAYGROUND_ROOT / "cumcm_raw")
    rows: list[dict[str, object]] = []
    stage_counts: Counter[str] = Counter()
    action_counts: Counter[str] = Counter()
    total_bytes = 0

    for stage in stages:
        stage_root = stage.source_root
        stage_target = target_root / stage.name
        stage_target.mkdir(parents=True, exist_ok=True)
        for source in iter_files(stage_root):
            relative = source.relative_to(stage_root)
            destination = stage_target / relative
            digest = sha256_file(source)
            action = copy_if_needed(source, destination, digest)
            size = source.stat().st_size
            total_bytes += size
            stage_counts[stage.name] += 1
            action_counts[action] += 1
            archive_meta = download_rows.get(source.name, {})
            rows.append(
                {
                    "stage": stage.name,
                    "file_kind": classify_file(source, stage.name),
                    "year": infer_year(source),
                    "problem_code": infer_problem_code(source.relative_to(stage_root)),
                    "filename": source.name,
                    "relative_source_path": str(relative),
                    "source_path": str(source),
                    "dest_path": str(destination.relative_to(REPO_ROOT)),
                    "dest_abs_path": str(destination),
                    "size_bytes": size,
                    "sha256": digest,
                    "download_url": archive_meta.get("url", ""),
                    "download_page": archive_meta.get("node", ""),
                }
            )

    fieldnames = [
        "stage",
        "file_kind",
        "year",
        "problem_code",
        "filename",
        "relative_source_path",
        "source_path",
        "dest_path",
        "dest_abs_path",
        "size_bytes",
        "sha256",
        "download_url",
        "download_page",
    ]
    manifest_csv = target_root / "manifest.csv"
    with manifest_csv.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    manifest_json = target_root / "manifest.json"
    manifest_json.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")

    summary = {
        "target_root": str(target_root),
        "source_stages": [
            {"name": stage.name, "source_root": str(stage.source_root), "description": stage.description}
            for stage in stages
        ],
        "stage_counts": dict(stage_counts),
        "action_counts": dict(action_counts),
        "file_kind_counts": dict(Counter(str(row["file_kind"]) for row in rows)),
        "total_manifest_rows": len(rows),
        "total_source_bytes": total_bytes,
    }
    (target_root / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    build_readme(target_root, stages, stage_counts, total_bytes)
    return summary


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--target-root",
        type=Path,
        default=DEFAULT_TARGET_ROOT,
        help="Destination folder for organized source materials.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    summary = organize(args.target_root, STAGE_DEFINITIONS)
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
