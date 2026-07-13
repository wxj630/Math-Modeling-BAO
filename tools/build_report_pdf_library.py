#!/usr/bin/env python3
"""Build the public report PDF manifest and VitePress index page.

The PDF files live outside this repository. This script records their relative
paths and generates stable public links once a hosting base URL is chosen.
"""

from __future__ import annotations

import argparse
import csv
import os
import re
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REPORTS_ROOT = REPO_ROOT.parent / "Math-Modeling-BAO-Reports"
DEFAULT_DOC = REPO_ROOT / "docs" / "reference" / "report-pdf-library.md"
DEFAULT_CSV = REPO_ROOT / "docs" / "public" / "reference" / "report-pdf-manifest.csv"
DEFAULT_PUBLIC_BASE_URL = os.environ.get("REPORT_PDF_PUBLIC_BASE_URL", "").strip()


@dataclass(frozen=True)
class ReportPdf:
    contest: str
    year: str
    problem: str
    level: str
    entry_id: str
    relative_path: str
    public_url: str
    size_mb: str

    @property
    def sort_key(self) -> tuple[str, str, str, str, str]:
        level_order = {"outstanding": "0", "advanced": "1", "baseline": "2"}
        return (
            self.contest,
            self.year,
            self.problem,
            level_order.get(self.level, "9"),
            self.entry_id,
        )


def parse_problem(value: str) -> tuple[str, str]:
    match = re.fullmatch(r"(\d{4})-([A-Z]+)", value)
    if not match:
        return "", ""
    return match.group(1), match.group(2)


def encoded_path_url(base_url: str, relative_path: str) -> str:
    if not base_url:
        return ""
    encoded = "/".join(quote(part) for part in relative_path.split("/"))
    return f"{base_url.rstrip('/')}/{encoded}"


def github_release_asset_name(relative_path: str) -> str:
    return relative_path.replace("/", "__")


def public_url(base_url: str, relative_path: str, url_style: str) -> str:
    if not base_url:
        return ""
    if url_style == "github-release":
        return f"{base_url.rstrip('/')}/{quote(github_release_asset_name(relative_path))}"
    return encoded_path_url(base_url, relative_path)


def classify_pdf(path: Path, reports_root: Path, base_url: str, url_style: str) -> ReportPdf | None:
    rel = path.relative_to(reports_root).as_posix()
    parts = rel.split("/")

    if parts[0] == "outstanding" and len(parts) >= 6 and parts[4] == "pdf":
        contest = parts[1]
        year, problem = parse_problem(parts[2])
        entry_id = parts[3]
        level = "outstanding"
    elif parts[0] in {"mcm", "cumcm"} and len(parts) >= 4:
        contest = parts[0]
        year, problem = parse_problem(parts[1])
        level = parts[2]
        entry_id = f"{year}-{problem}-{level}" if year and problem else parts[1]
        if level not in {"baseline", "advanced"}:
            return None
    else:
        return None

    if not year or not problem:
        return None

    size_mb = f"{path.stat().st_size / (1024 * 1024):.2f}"
    return ReportPdf(
        contest=contest,
        year=year,
        problem=problem,
        level=level,
        entry_id=entry_id,
        relative_path=rel,
        public_url=public_url(base_url, rel, url_style),
        size_mb=size_mb,
    )


def collect_pdfs(reports_root: Path, base_url: str, url_style: str) -> list[ReportPdf]:
    rows: list[ReportPdf] = []
    for path in reports_root.rglob("*.pdf"):
        item = classify_pdf(path, reports_root, base_url, url_style)
        if item is not None:
            rows.append(item)
    return sorted(rows, key=lambda item: item.sort_key)


def collect_dataset_manifest(manifest_path: Path, base_url: str, url_style: str) -> list[ReportPdf]:
    rows: list[ReportPdf] = []
    with manifest_path.open(encoding="utf-8", newline="") as fp:
        reader = csv.DictReader(fp)
        for item in reader:
            dataset_path = item.get("dataset_relative_path", "").strip()
            if not dataset_path:
                continue
            rows.append(
                ReportPdf(
                    contest=item["contest"],
                    year=item["year"],
                    problem=item["problem"],
                    level=item["level"],
                    entry_id=item["entry_id"],
                    relative_path=dataset_path,
                    public_url=public_url(base_url, dataset_path, url_style),
                    size_mb=item["size_mb"],
                )
            )
    return sorted(rows, key=lambda item: item.sort_key)


def write_csv(rows: list[ReportPdf], csv_path: Path) -> None:
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open("w", encoding="utf-8", newline="") as fp:
        writer = csv.DictWriter(
            fp,
            fieldnames=[
                "contest",
                "year",
                "problem",
                "level",
                "entry_id",
                "size_mb",
                "relative_path",
                "public_url",
            ],
        )
        writer.writeheader()
        for row in rows:
            writer.writerow(row.__dict__)


def table_row(row: ReportPdf) -> str:
    label = f"{row.contest.upper()} {row.year}-{row.problem}"
    link = f"[PDF]({row.public_url})" if row.public_url else "待上传"
    return (
        f"| {label} | {row.level} | {row.entry_id} | "
        f"{row.size_mb} | {link} | `{row.relative_path}` |"
    )


def write_markdown(rows: list[ReportPdf], doc_path: Path, csv_path: Path, base_url: str, url_style: str) -> None:
    doc_path.parent.mkdir(parents=True, exist_ok=True)
    counts: dict[tuple[str, str], int] = {}
    for row in rows:
        counts[(row.contest, row.level)] = counts.get((row.contest, row.level), 0) + 1

    outstanding_rows = [row for row in rows if row.level == "outstanding"]
    generated_rows = [row for row in rows if row.level in {"advanced", "baseline"}]
    try:
        csv_url = "/" + csv_path.relative_to(REPO_ROOT / "docs" / "public").as_posix()
        csv_label = csv_url.lstrip("/")
    except ValueError:
        csv_url = csv_path.relative_to(REPO_ROOT / "docs").as_posix()
        csv_label = csv_url
    status = "已生成公开下载链接" if base_url else "尚未配置公开下载基座，表格中的 PDF 链接显示为待上传"

    lines = [
        "# PDF 论文库",
        "",
        "这个页面只保存 PDF 的索引和下载入口，PDF 文件本体不进入主仓库。主仓库负责教程、代码、轻量结果和 manifest；PDF 原文放在外部资料库中。",
        "",
        "## 分享方案",
        "",
        "- 国内访问推荐：使用 ModelScope Dataset 托管纯 PDF 数据集，教程站只保存索引和下载链接。",
        "- 也可以把 `Math-Modeling-BAO-Reports` 上传到 Hugging Face Dataset、S3/R2 或其它能保留目录结构的对象存储，然后用相同目录结构生成下载链接。",
        "- 备选：使用 GitHub Release 存放 PDF asset，主仓库仍保持轻量；这种方式需要把路径扁平化为 asset 名。",
        "- 若某些论文或 OCR 文件没有明确再分发权限，只在 manifest 中放官方来源链接或访问说明，不直接公开文件。",
        "",
        "## 当前索引状态",
        "",
        f"- PDF 条目：{len(rows)}",
        f"- 链接状态：{status}",
        f"- URL 风格：`{url_style}`",
        f"- 公开基座：`{base_url or '未配置'}`",
        f"- 机器可读索引：[{csv_label}]({csv_url})",
        "",
        "按当前本地目录统计：",
        "",
        "| 竞赛 | Outstanding | Advanced | Baseline |",
        "|---|---:|---:|---:|",
    ]

    for contest in ["mcm", "cumcm"]:
        lines.append(
            f"| {contest.upper()} | "
            f"{counts.get((contest, 'outstanding'), 0)} | "
            f"{counts.get((contest, 'advanced'), 0)} | "
            f"{counts.get((contest, 'baseline'), 0)} |"
        )

    lines.extend(
        [
            "",
            "## Outstanding 论文",
            "",
            "| 赛题 | 层级 | 编号 | MB | 链接 | 路径 |",
            "|---|---|---:|---:|---|---|",
        ]
    )
    lines.extend(table_row(row) for row in outstanding_rows)

    lines.extend(
        [
            "",
            "## BAO 生成报告",
            "",
            "| 赛题 | 层级 | 编号 | MB | 链接 | 路径 |",
            "|---|---|---:|---:|---|---|",
        ]
    )
    lines.extend(table_row(row) for row in generated_rows)

    lines.extend(
        [
            "",
            "## 重建索引",
            "",
            "Hugging Face Dataset / S3 / R2 这类保留目录结构的存储：",
            "",
            "```bash",
            "REPORT_PDF_PUBLIC_BASE_URL=https://huggingface.co/datasets/wxj630/math-modeling-bao-reports/resolve/main \\",
            "python tools/build_report_pdf_library.py",
            "```",
            "",
            "ModelScope 纯 PDF 数据集：",
            "",
            "```bash",
            "python tools/build_report_pdf_library.py \\",
            "  --dataset-manifest ../open-source/Math-Modeling-BAO/manifest.csv \\",
            "  --public-base-url https://www.modelscope.cn/datasets/wuxiaojun/Math-Modeling-BAO/resolve/master",
            "```",
            "",
            "GitHub Release 这类扁平 asset 存储：",
            "",
            "```bash",
            "python tools/build_report_pdf_library.py \\",
            "  --public-base-url https://github.com/wxj630/Math-Modeling-BAO/releases/download/reports-v0.1 \\",
            "  --url-style github-release",
            "```",
        ]
    )

    doc_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--reports-root", type=Path, default=DEFAULT_REPORTS_ROOT)
    parser.add_argument("--dataset-manifest", type=Path)
    parser.add_argument("--public-base-url", default=DEFAULT_PUBLIC_BASE_URL)
    parser.add_argument("--url-style", choices=["path", "github-release"], default="path")
    parser.add_argument("--doc", type=Path, default=DEFAULT_DOC)
    parser.add_argument("--csv", type=Path, default=DEFAULT_CSV)
    args = parser.parse_args()

    if args.dataset_manifest:
        rows = collect_dataset_manifest(args.dataset_manifest, args.public_base_url.strip(), args.url_style)
    else:
        rows = collect_pdfs(args.reports_root, args.public_base_url.strip(), args.url_style)
    write_csv(rows, args.csv)
    write_markdown(rows, args.doc, args.csv, args.public_base_url.strip(), args.url_style)
    print(f"indexed {len(rows)} PDFs")
    print(f"wrote {args.csv}")
    print(f"wrote {args.doc}")


if __name__ == "__main__":
    main()
