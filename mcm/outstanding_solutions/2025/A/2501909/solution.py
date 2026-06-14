from __future__ import annotations

import json
import shutil
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[5]
ROOT = Path(__file__).resolve().parent
REAL_DIR = REPO_ROOT / "docs" / "mcm-2015-2025" / "real_solutions" / "2025" / "MCM-A"
REAL_RESULT = REAL_DIR / "result.json"
REAL_ARTIFACTS = REAL_DIR / "artifacts"
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"

PAPER_ID = "2501909"
PAPER_TITLE = "Stair Wear: Traces of History"
PAPER_SOURCE_OCR = "Outstanding_Solutions/MCM/OCR-results/A/2501909/2501909.md"
PAPER_SOURCE_PDF = "Outstanding_Solutions/MCM/PDF-2025/A/2501909.pdf"


def repo_rel(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def copy_artifacts() -> dict[str, str]:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    copied: dict[str, str] = {}
    for source in sorted(REAL_ARTIFACTS.glob("*")):
        if source.is_file():
            target = ARTIFACT_DIR / source.name
            shutil.copy2(source, target)
            copied[source.stem] = repo_rel(target)
    return copied


def write_report(result: dict) -> None:
    kernel = result["advanced_kernel"]
    exp = result["experiment_result"]
    lines = [
        "# 2025 MCM-A Outstanding 复现：2501909",
        "",
        "## 复现对象",
        f"- 获奖论文：`{PAPER_ID}`，{PAPER_TITLE}",
        f"- OCR 来源：`{PAPER_SOURCE_OCR}`",
        f"- PDF 来源：`{PAPER_SOURCE_PDF}`",
        "- 复现定位：以当前已验证的 MCM-A real solution 为计算核，对齐论文中的 WVM/WDM、年龄可靠性、修复检测和材料一致性叙事。",
        "",
        "## 问题与建模",
        "论文 2501909 将台阶磨损拆成 Wear Volume Model 和 Wear Distribution Model：先用 Archard wear law 把磨损深度、材料硬度、脚步载荷和时间联系起来，再用横向/纵向磨损分布判断行走方向、并排行走人数和修复异常。当前计算核已经包含非破坏测量模板、逆磨损模型、年龄可靠性网格和修复候选检测，因此适合作为该论文的可验证复现版本。",
        "",
        "## 代码与实验",
        "- `solution.py` 读取 `docs/mcm-2015-2025/real_solutions/2025/MCM-A/result.json`。",
        "- 复制当前 advanced 的测量模板、年龄网格、磨损剖面、修复候选和可视化 artifacts。",
        "- 在 `result.json` 中补充获奖论文方法、复现范围和相对 advanced 的升级说明。",
        "",
        "## 关键结果",
        f"- 测量原则：{kernel['measurement_protocol']['principle']}。",
        f"- 中位中心磨损深度：{exp['median_center_wear_depth_mm']} mm。",
        f"- 估计日使用人数：{exp['estimated_daily_users']}。",
        f"- 偏好方向：{exp['favored_direction']}；并排行走模式：{exp['simultaneous_pattern']}。",
        f"- 年龄估计：{exp['estimated_age_years']} 年，可靠区间 {exp['age_interval_years']}。",
        f"- 修复候选数量：{exp['repair_candidate_count']}。",
        "",
        "## 相对 Advanced 的优势",
        "- Advanced 已经给出可运行的逆磨损计算和 artifacts；Outstanding 把这些结果重组为获奖论文的 WVM/WDM 主线。",
        "- 报告显式连接 Archard 磨损、测量矩阵、年龄可靠性、修复检测和材料来源，便于写成完整论文段落。",
        "- 后续可以在此基础上加入真实扫描矩阵和 Gaussian mixture 横向/纵向分布拟合，替代当前 worked example。",
        "",
        "## 输出产物",
    ]
    for key, path in result["artifact_paths"].items():
        lines.append(f"- `{key}`：`{path}`")
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    if not REAL_RESULT.exists():
        raise FileNotFoundError(f"missing advanced result: {REAL_RESULT}")
    advanced = read_json(REAL_RESULT)
    artifacts = copy_artifacts()
    inverse = advanced["inverse_wear_model"]
    age = advanced["age_reliability"]
    repairs = advanced["renovation_detection"]["repair_candidates"]
    result = {
        "problem_id": "2025-A",
        "year": 2025,
        "code": "A",
        "paper_id": PAPER_ID,
        "paper_title": PAPER_TITLE,
        "paper_source_ocr": PAPER_SOURCE_OCR,
        "paper_source_pdf": PAPER_SOURCE_PDF,
        "reproduction_scope": "用当前 MCM-A real solution 的非破坏测量、逆磨损、年龄可靠性和修复检测结果，对齐 2501909 的 WVM/WDM 获奖论文模型链。",
        "selected_model": {
            "name": "Wear Volume Model + Wear Distribution Model",
            "chapter": "Outstanding reproduction of 2501909",
        },
        "data_source": advanced["data_source"],
        "advanced_kernel": advanced,
        "paper_model_alignment": {
            "paper_methods": [
                "Wear Volume Model based on Archard wear law",
                "Wear Distribution Model from rasterized wear matrix",
                "age and usage frequency inversion",
                "repair and material consistency checks",
            ],
            "repo_kernel": [
                "non-destructive measurement template",
                "inverse Archard-style wear balance",
                "age reliability grid",
                "renovation candidate detection",
            ],
        },
        "experiment_result": {
            "median_center_wear_depth_mm": inverse["usage_frequency"]["median_center_wear_depth_mm"],
            "estimated_daily_users": inverse["usage_frequency"]["estimated_daily_users"],
            "favored_direction": inverse["direction_preference"]["favored_direction"],
            "simultaneous_pattern": inverse["simultaneous_use"]["pattern"],
            "estimated_age_years": age["estimated_age_years"],
            "age_interval_years": age["plausible_interval_years"],
            "repair_candidate_count": len(repairs),
        },
        "difference_from_advanced": "把 advanced 的逆磨损脚手架整理为获奖论文式 WVM/WDM 全局模型，并补充论文级问题、建模、结果和局限叙事。",
        "artifact_paths": artifacts,
        "limitations": [
            "当前复现使用 worked example 测量表；真实考古扫描矩阵可替换 artifacts 中的 measurement_template。",
            "Gaussian mixture 横向/纵向分布拟合尚未单独重写，当前以 side-to-center ratio 和 edge-rounding asymmetry 作为可验证近似。",
        ],
    }
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_report(result)
    print(json.dumps({"result": repo_rel(RESULT_PATH), "report": repo_rel(REPORT_PATH)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
