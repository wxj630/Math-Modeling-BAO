from __future__ import annotations

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
    if value is None:
        return "null"
    text = str(value).replace("\n", " ").strip()
    return text[:140] + ("..." if len(text) > 140 else "")


def value_at(data: Any, path: list[str | int]) -> Any:
    value = data
    for part in path:
        if isinstance(part, int) and isinstance(value, list):
            value = value[part]
        elif isinstance(part, str) and isinstance(value, dict):
            value = value.get(part)
        else:
            return None
        if value is None:
            return None
    return value


def copy_artifacts(real_dir: Path, output_dir: Path) -> dict[str, str]:
    source_root = real_dir / "artifacts"
    target_root = output_dir / "artifacts"
    target_root.mkdir(parents=True, exist_ok=True)
    copied: dict[str, str] = {}
    if not source_root.exists():
        return copied
    for source in sorted(source_root.rglob("*")):
        if not source.is_file():
            continue
        rel = source.relative_to(source_root)
        target = target_root / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        copied[rel.as_posix()] = repo_rel(target)
    return copied


def build_experiment_result(advanced: dict[str, Any], fields: list[dict[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for field in fields:
        value = value_at(advanced, field["path"])
        if value is None:
            continue
        if field.get("transform") == "count" and isinstance(value, (list, dict)):
            value = len(value)
        result[field["key"]] = value
    return result


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
        f"- `solution.py` 读取 `docs/mcm-2015-2025/real_solutions/2025/{config['real_solution_key']}/result.json`。",
        "- 复制当前 advanced 的表格、图像和中间数据到 outstanding artifacts。",
        "- 在赛题级 `result.json` 中记录论文方法、当前计算核、关键实验结果和相对 advanced 的升级说明。",
        "",
        "## 关键结果",
    ]
    for field in config["experiment_fields"]:
        key = field["key"]
        if key in result["experiment_result"]:
            lines.append(f"- {field['label']}：{scalar(result['experiment_result'][key])}。")
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
    real_dir = REPO_ROOT / "docs" / "mcm-2015-2025" / "real_solutions" / "2025" / config["real_solution_key"]
    real_result = real_dir / "result.json"
    if not real_result.exists():
        raise FileNotFoundError(f"missing advanced result: {real_result}")

    advanced = read_json(real_result)
    artifacts = copy_artifacts(real_dir, output_dir)
    experiment_result = build_experiment_result(advanced, config["experiment_fields"])
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
        "data_source": advanced.get("data_source", {}),
        "paper_model_alignment": {
            "paper_methods": config["paper_methods"],
            "repo_kernel": config["repo_kernel"],
        },
        "experiment_result": experiment_result,
        "difference_from_advanced": config["difference_from_advanced"],
        "artifact_paths": artifacts,
        "advanced_result_path": repo_rel(real_result),
        "limitations": config["limitations"],
    }
    (output_dir / "result.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_report(config, result, output_dir)
    print(json.dumps({"result": repo_rel(output_dir / "result.json"), "report": repo_rel(output_dir / "report.md")}, ensure_ascii=False, indent=2))
