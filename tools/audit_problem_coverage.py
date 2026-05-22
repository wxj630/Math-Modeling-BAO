#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit tutorial problem coverage against local source-material indexes."""
from __future__ import annotations

import csv
import json
import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class Coverage:
    track: str
    expected: set[str]
    indexed: set[str]
    missing_from_index: set[str]
    extra_indexed: set[str]
    local_problem_files: set[str]
    unindexed_local_files: set[str]
    duplicate_aliases: dict[str, str]


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def normalized_title(text: str) -> str:
    first = text.splitlines()[0].lstrip("# ").strip() if text.splitlines() else ""
    first = re.sub(r"^\d{4}[-年]\S+\s*", "", first)
    first = first.replace("MCM-C:", "").replace("ICM-C:", "").replace("ICM-D:", "")
    first = re.sub(r"\s+", " ", first)
    return first.lower().strip(" ：:-")


def local_problem_ids(root: Path) -> set[str]:
    return {f"{path.parent.name}-{path.stem}" for path in root.glob("*/*.md")}


def local_title_map(root: Path) -> dict[str, str]:
    mapping: dict[str, str] = {}
    for path in root.glob("*/*.md"):
        pid = f"{path.parent.name}-{path.stem}"
        mapping[pid] = normalized_title(path.read_text(encoding="utf-8", errors="ignore"))
    return mapping


def cumcm_expected() -> set[str]:
    rows = read_csv(REPO_ROOT / "cumcm" / "source_materials" / "manifest.csv")
    expected: set[str] = set()
    for row in rows:
        if row.get("file_kind") != "problem_document":
            continue
        year = row.get("year", "")
        code = row.get("problem_code", "")
        if year and code in {"A", "B", "C", "D", "E"}:
            expected.add(f"{year}-{code}")
    return expected


def mcm_expected() -> set[str]:
    rows = read_csv(REPO_ROOT / "mcm" / "source_materials" / "manifests" / "mcm_problem_index.csv")
    if rows:
        return {row["problem_id"] for row in rows if row.get("problem_id")}
    return {row["problem_id"] for row in read_csv(REPO_ROOT / "mcm" / "problem_index.csv") if row.get("problem_id")}


def indexed_problem_ids(path: Path) -> set[str]:
    return {row["problem_id"] for row in read_csv(path) if row.get("problem_id")}


def duplicate_aliases(problem_root: Path, indexed: set[str], unindexed: set[str]) -> dict[str, str]:
    titles = local_title_map(problem_root)
    indexed_by_title: dict[str, str] = {}
    for pid in indexed:
        title = titles.get(pid, "")
        if title:
            indexed_by_title.setdefault(title, pid)
    aliases: dict[str, str] = {}
    for pid in sorted(unindexed):
        title = titles.get(pid, "")
        canonical = indexed_by_title.get(title)
        if canonical:
            aliases[pid] = canonical
    return aliases


def build_coverage(track: str) -> Coverage:
    if track == "cumcm":
        problem_root = REPO_ROOT / "cumcm" / "problems"
        expected = cumcm_expected()
        index_path = REPO_ROOT / "cumcm" / "problem_index.csv"
    elif track == "mcm":
        problem_root = REPO_ROOT / "mcm" / "problems"
        expected = mcm_expected()
        index_path = REPO_ROOT / "mcm" / "problem_index.csv"
    else:
        raise ValueError(track)

    indexed = indexed_problem_ids(index_path)
    local = local_problem_ids(problem_root)
    unindexed = local - indexed
    aliases = duplicate_aliases(problem_root, indexed, unindexed)
    return Coverage(
        track=track,
        expected=expected,
        indexed=indexed,
        missing_from_index=expected - indexed,
        extra_indexed=indexed - expected,
        local_problem_files=local,
        unindexed_local_files=unindexed,
        duplicate_aliases=aliases,
    )


def year_groups(ids: set[str]) -> dict[str, list[str]]:
    groups: dict[str, list[str]] = defaultdict(list)
    for pid in sorted(ids):
        year, _, code = pid.partition("-")
        groups[year].append(code)
    return dict(sorted(groups.items()))


def table_from_groups(groups: dict[str, list[str]]) -> list[str]:
    if not groups:
        return ["| 年份 | 题号 |", "| --- | --- |", "| 无 | 无 |"]
    lines = ["| 年份 | 题号 |", "| --- | --- |"]
    for year, codes in groups.items():
        lines.append(f"| {year} | {', '.join(codes)} |")
    return lines


def write_report(cumcm: Coverage, mcm: Coverage, path: Path) -> None:
    lines = [
        "# Problem Coverage Audit",
        "",
        "这份报告对比本地归档材料、教程索引和本地题面 Markdown，用来回答“本地已有材料但没有进入教程”的缺口。",
        "",
        "## 结论",
        "",
        f"- CUMCM 本地归档题面：{len(cumcm.expected)} 题；教程索引：{len(cumcm.indexed)} 题；当前缺口：{len(cumcm.missing_from_index)} 题。",
        f"- MCM/ICM 本地规范索引：{len(mcm.expected)} 题；教程索引：{len(mcm.indexed)} 题；当前唯一题目缺口：{len(mcm.missing_from_index)} 题。",
        "- CUMCM 这次的根因是 2022/2023 年 A-E 已经解压到 `cumcm/source_materials/extracted/`，但旧清洗阶段只转出了 2022-B、2022-D、2023-D 三个 markdown，因此后续 `cumcm/problems`、逐问索引和教程页都只看到了这些题。",
        "",
        "## CUMCM 缺口",
        "",
        *table_from_groups(year_groups(cumcm.missing_from_index)),
        "",
        "## MCM/ICM 缺口",
        "",
        *table_from_groups(year_groups(mcm.missing_from_index)),
        "",
        "## MCM/ICM 本地重复别名",
        "",
        "| 本地文件题号 | 教程采用的规范题号 |",
        "| --- | --- |",
    ]
    if mcm.duplicate_aliases:
        for alias, canonical in sorted(mcm.duplicate_aliases.items()):
            lines.append(f"| {alias} | {canonical} |")
    else:
        lines.append("| 无 | 无 |")
    lines += [
        "",
        "这些重复别名来自早期抽取或命名方式，不代表新的独立赛题；教程只保留规范题号，避免同一题出现两套入口。",
        "",
        "## 机器可读摘要",
        "",
        "```json",
        json.dumps(
            {
                "cumcm": {
                    "expected": len(cumcm.expected),
                    "indexed": len(cumcm.indexed),
                    "missing_from_index": sorted(cumcm.missing_from_index),
                    "extra_indexed": sorted(cumcm.extra_indexed),
                },
                "mcm": {
                    "expected": len(mcm.expected),
                    "indexed": len(mcm.indexed),
                    "missing_from_index": sorted(mcm.missing_from_index),
                    "extra_indexed": sorted(mcm.extra_indexed),
                    "duplicate_aliases": mcm.duplicate_aliases,
                },
            },
            ensure_ascii=False,
            indent=2,
        ),
        "```",
        "",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    cumcm = build_coverage("cumcm")
    mcm = build_coverage("mcm")
    report_path = REPO_ROOT / "docs" / "reference" / "problem-coverage-audit.md"
    write_report(cumcm, mcm, report_path)
    summary = {
        "report": str(report_path.relative_to(REPO_ROOT)),
        "cumcm_missing": sorted(cumcm.missing_from_index),
        "mcm_missing": sorted(mcm.missing_from_index),
        "mcm_duplicate_aliases": mcm.duplicate_aliases,
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
